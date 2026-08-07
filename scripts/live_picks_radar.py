#!/usr/bin/env python3
"""Live Picks Radar - spotlight OUR OWN recommendations that start running, in time to act.

The problem it solves (Omar 2026-07-23): a name we flagged (e.g. VSXY, Buy Zone 7/8) can
run +50% while buried in a report of dozens - we track it post-hoc but never get pinged to
ACT. This watches ONLY names we've already recommended, scores each for "is it running NOW",
and fires a push the moment one first crosses a confirming/extended threshold (state-diffed so
it pings once per transition, not every run). Runs 3x/day: 9:00 AM, ~11:45 AM, 3:05 PM CT.

Universe (active picks, flag within LOOKBACK days, not closed):
  - research/recommendations_log-<date>.csv  (origination scanner picks: price, tab, status)
  - research/calls-ledger.json               (pre-registered calls: sym, ref, dir=long)
  - watchlists/universe-results-<date>.json  (today's gate-passing CANDIDATEs)

Current prices: yfinance daily batch (cross-checked to the TV feed; ~15 min delayed intraday,
fine for catching multi-percent runs). Levels for any actual trade still come from the live feed.
Industry: one TradingView scanner request builds a market-wide ticker->industry map.

Outputs:
  - watchlists/live-picks-<date>.md          (full ranked report)
  - watchlists/live-picks-brief-block.md     (compact block pinned to the TOP of every brief)
  - watchlists/live-picks-state.json         (tier last-notified per ticker; drives push-once)

Exit code 10 = NEW confirmed/extended movers this run (the batch uses that to push). Else 0.
Pass --dry to compute + print + write reports but NOT touch state or signal a push.
"""
import csv, glob, json, os, sys, datetime, urllib.request
import warnings; warnings.filterwarnings("ignore")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE = os.path.join(REPO, "watchlists", "live-picks-state.json")
LOOKBACK_DAYS = 60
CONFIRM_RET = 0.08     # up >=8% from flag = it's working
EXTENDED_RET = 0.25    # up >=25% = already ran, do NOT chase
NEAR_HIGH = 0.99       # within 1% of the prior 20-day high = making highs

DRY = "--dry" in sys.argv


def today():
    return datetime.date.today()


def latest(pattern):
    fs = sorted(glob.glob(os.path.join(REPO, pattern)))
    return fs[-1] if fs else None


def load_picks():
    picks = {}
    cutoff = today() - datetime.timedelta(days=LOOKBACK_DAYS)

    def add(tkr, fdate, fprice, source, grade=""):
        tkr = (tkr or "").upper().strip()
        try:
            fprice = float(fprice)
        except (TypeError, ValueError):
            return
        if not tkr or fprice <= 0:
            return
        try:
            d = datetime.date.fromisoformat(str(fdate)[:10])
        except Exception:
            return
        if d < cutoff:
            return
        if tkr not in picks or d < picks[tkr]["flag_date"]:
            picks[tkr] = {"flag_date": d, "flag_price": fprice,
                          "source": source, "grade": grade}

    f = latest("research/recommendations_log-*.csv")
    if f:
        for r in csv.DictReader(open(f, encoding="utf-8", errors="replace")):
            if (r.get("status") or "").strip().upper() != "OPEN":
                continue
            add(r.get("ticker"), r.get("date"), r.get("price") or 0,
                f"origination:{(r.get('tab') or '').title()}", r.get("grade", ""))

    lf = os.path.join(REPO, "research", "calls-ledger.json")
    if os.path.exists(lf):
        raw = json.load(open(lf))
        calls = raw if isinstance(raw, list) else raw.get("calls", [])
        for c in calls:
            if not isinstance(c, dict) or (c.get("dir") or "").lower() != "long":
                continue
            add(c.get("sym"), c.get("date"), c.get("ref") or 0,
                f"call:{c.get('source', 'ledger')}")

    uf = latest("watchlists/universe-results-*.json")
    if uf:
        d = json.load(open(uf))
        for h in d.get("hits", []):
            if str(h.get("verdict", "")).startswith("CANDIDATE"):
                add(h.get("sym"), d.get("date"), h.get("last") or 0, "gate-passer", "")
    return picks


def fetch_current(tickers):
    import yfinance as yf
    out = {}
    if not tickers:
        return out
    df = yf.download(tickers, period="3mo", interval="1d",
                     auto_adjust=True, progress=False, threads=True)
    close, high, vol = df["Close"], df["High"], df["Volume"]
    for t in tickers:
        try:
            c = close[t].dropna()
            if len(c) < 5:
                continue
            h = high[t].dropna(); v = vol[t].dropna()
            cur = float(c.iloc[-1])
            high20 = float(h.iloc[-21:-1].max()) if len(h) >= 21 else float(h.max())
            ret1w = cur / float(c.iloc[-6]) - 1 if len(c) >= 6 else 0.0
            rvol = float(v.iloc[-1]) / float(v.iloc[-21:-1].mean()) if len(v) >= 21 else 1.0
            out[t] = {"cur": cur, "high20": high20, "ret1w": ret1w, "rvol": rvol}
        except Exception:
            continue
    return out


def fetch_industries():
    """One scanner request -> {bare_ticker: industry} for the whole US market."""
    try:
        body = json.dumps({
            "filter": [{"left": "type", "operation": "equal", "right": "stock"},
                       {"left": "exchange", "operation": "in_range",
                        "right": ["NASDAQ", "NYSE", "AMEX"]}],
            "options": {"lang": "en"}, "markets": ["america"],
            "columns": ["name", "industry"], "range": [0, 9000],
        }).encode()
        req = urllib.request.Request("https://scanner.tradingview.com/america/scan",
                                     data=body, headers={"User-Agent": "Mozilla/5.0",
                                                         "Content-Type": "application/json"})
        data = json.loads(urllib.request.urlopen(req, timeout=30).read()).get("data", [])
        return {r["s"].split(":")[-1]: (r["d"][1] or "") for r in data}
    except Exception:
        return {}


PE_WATCH = os.path.join(REPO, "watchlists", "post-earnings-watch.json")
PE_REACT = 0.04        # >=+4% first-day reaction = a positive earnings surprise
PE_HOLD = 0.95         # holding within 5% of the post-earnings high = not faded
PE_WINDOW_DAYS = 21    # drift window; drop from the watch after this


def post_earnings_check(state):
    """For names whose earnings have passed, detect BEAT-AND-HOLD (a clean PEAD entry):
    a clear positive reaction to the print AND price still holding the gap days later.
    Returns (results, fires). Prunes names whose window has expired."""
    if not os.path.exists(PE_WATCH):
        return [], []
    try:
        watch = json.load(open(PE_WATCH))
    except Exception:
        return [], []
    import yfinance as yf
    td = today()
    tickers = [w["ticker"] for w in watch]
    bars = {}
    if tickers:
        df = yf.download(tickers, period="4mo", interval="1d",
                         auto_adjust=True, progress=False, threads=True)
        cl = df["Close"] if "Close" in df else df
        for t in tickers:
            try:
                s = cl[t].dropna() if hasattr(cl, "columns") else cl.dropna()
                if len(s):
                    bars[t] = s
            except Exception:
                pass
    results, fires, keep = [], [], []
    for w in watch:
        t = w["ticker"]
        try:
            ed = datetime.date.fromisoformat(w["earnings_date"])
        except Exception:
            continue
        if td > ed + datetime.timedelta(days=PE_WINDOW_DAYS):
            continue                      # expired -> drop from the watch
        keep.append(w)
        if td <= ed:
            results.append({"t": t, "status": "PENDING", "ed": ed.isoformat(),
                            "note": w.get("flagged_from", "")})
            continue
        s = bars.get(t)
        if s is None or len(s) < 5:
            results.append({"t": t, "status": "NO-DATA", "ed": ed.isoformat()})
            continue
        pre = s[s.index.date < ed]
        post = s[s.index.date >= ed]
        if pre.empty or post.empty:
            results.append({"t": t, "status": "PENDING", "ed": ed.isoformat(),
                            "note": "awaiting reaction"})
            continue
        pre_ref = float(pre.iloc[-1]); cur = float(s.iloc[-1])
        post_high = float(post.max())
        react = float(post.iloc[0]) / pre_ref - 1
        overall = cur / pre_ref - 1
        if react >= PE_REACT and cur >= pre_ref and cur >= PE_HOLD * post_high:
            status = "BEAT-AND-HOLD"
        elif overall <= -0.02 or cur < pre_ref:
            status = "FADED"
        else:
            status = "SETTLING"
        rec = {"t": t, "status": status, "react": react, "overall": overall,
               "pre_ref": pre_ref, "cur": cur, "ed": ed.isoformat()}
        results.append(rec)
        if status == "BEAT-AND-HOLD" and state.get("PE:" + t) != "BEAT-AND-HOLD":
            fires.append(rec)
    if not DRY and len(keep) != len(watch):
        json.dump(keep, open(PE_WATCH, "w"), indent=1)
    return results, fires


def classify(ret, cur, high20):
    if ret >= EXTENDED_RET:
        return "EXTENDED"
    if ret >= CONFIRM_RET and cur >= NEAR_HIGH * high20:
        return "CONFIRMING"
    if ret >= CONFIRM_RET:
        return "UP-STALLED"
    return "WATCH"


TIER_RANK = {"WATCH": 0, "UP-STALLED": 1, "CONFIRMING": 2, "EXTENDED": 3}


def main():
    picks = load_picks()
    cur = fetch_current(list(picks.keys()))
    ind = fetch_industries()
    rows = []
    for t, p in picks.items():
        m = cur.get(t)
        if not m:
            continue
        ret = m["cur"] / p["flag_price"] - 1
        rows.append({"tkr": t, "tier": classify(ret, m["cur"], m["high20"]), "ret": ret,
                     "cur": m["cur"], "flag": p["flag_price"], "industry": ind.get(t, "?"),
                     "flag_date": p["flag_date"].isoformat(), "source": p["source"],
                     "grade": p["grade"], "rvol": m["rvol"],
                     "new_high": m["cur"] >= m["high20"]})
    rows.sort(key=lambda x: (-TIER_RANK[x["tier"]], -x["ret"]))

    state = {}
    if os.path.exists(STATE):
        try:
            state = json.load(open(STATE))
        except Exception:
            state = {}

    fires = []
    for r in rows:
        if r["tier"] in ("CONFIRMING", "EXTENDED"):
            if TIER_RANK[r["tier"]] > TIER_RANK.get(state.get(r["tkr"], "WATCH"), 0):
                fires.append(r)

    pe_results, pe_fires = post_earnings_check(state)

    def act_of(r):
        return ("do NOT chase - wait for a pullback" if r["tier"] == "EXTENDED"
                else "confirming its run - enter/add per plan")

    # ----- full report -----
    lines = [f"# Live Picks Radar - {today().isoformat()}", ""]
    if fires:
        lines.append("## NEW - act now")
        for r in fires:
            lines.append(f"- **{r['tkr']}** ({r['industry']}) {r['tier']} +{r['ret']*100:.0f}% "
                         f"from flag ({r['flag_date']} @ {r['flag']:.2f}, {r['source']}) - now "
                         f"{r['cur']:.2f}{' NEW HIGH' if r['new_high'] else ''}, "
                         f"RVOL {r['rvol']:.1f} -> {act_of(r)}")
        lines.append("")
    lines.append("## All active picks (ranked by what's running)")
    # first-recommended dates (Omar 8/7: every runners table shows WHEN we first called it)
    import json as _json
    from pathlib import Path as _P
    try:
        _seen = _json.loads((_P(__file__).resolve().parent.parent / "watchlists" / "live-picks-first-seen.json").read_text())
    except Exception:
        _seen = {}
    lines.append("| Ticker | First rec | Industry | Tier | Ret | Now | Reco px | Source | RVOL |")
    lines.append("|---|---|---|--:|--:|--:|---|--:|")
    for r in rows:
        lines.append(f"| {r['tkr']} | {_seen.get(r['tkr'],'?')} | {r['industry']} | {r['tier']} | {r['ret']*100:+.0f}% | "
                     f"{r['cur']:.2f} | {r['flag']:.2f} | {r['source']} | {r['rvol']:.1f} |")
    if pe_results:
        lines += ["", "## Post-earnings watch (beat-and-hold = clean entry)"]
        order = {"BEAT-AND-HOLD": 0, "SETTLING": 1, "PENDING": 2, "FADED": 3, "NO-DATA": 4}
        for pr in sorted(pe_results, key=lambda x: order.get(x["status"], 9)):
            if pr["status"] in ("BEAT-AND-HOLD", "SETTLING", "FADED"):
                tail = " -> CLEAN ENTRY: beat and holding the gap" if pr["status"] == "BEAT-AND-HOLD" else ""
                lines.append(f"- **{pr['t']}** {pr['status']} - earnings {pr['ed']}, "
                             f"reaction {pr['react']*100:+.0f}%, now {pr['cur']:.2f} "
                             f"({pr['overall']*100:+.0f}% vs pre-earnings){tail}")
            else:
                lines.append(f"- {pr['t']} {pr['status']} - earnings {pr['ed']}"
                             + (f" ({pr.get('note')})" if pr.get('note') else ""))
    open(os.path.join(REPO, "watchlists", f"live-picks-{today().isoformat()}.md"),
         "w", encoding="utf-8").write("\n".join(lines))

    # ----- compact BRIEF BLOCK (pinned to the top of every brief) -----
    movers = [r for r in rows if r["tier"] in ("CONFIRMING", "EXTENDED")]
    bb = [f"### Live Picks - what's running ({today().isoformat()})", ""]
    if not movers:
        bb.append("_No active picks currently confirming a run._")
    else:
        bb.append("| Ticker | First rec | Industry | Reco px | Now | Gain | Read |")
        bb.append("|---|---|--:|--:|--:|---|")
        for r in movers:
            read = ("DON'T CHASE - pullback only" if r["tier"] == "EXTENDED"
                    else "confirming - enter/add per plan")
            bb.append(f"| {r['tkr']} | {_seen.get(r['tkr'],'?')} | {r['industry']} | {r['flag']:.2f} | {r['cur']:.2f} | "
                      f"{r['ret']*100:+.0f}% | {read} |")
    pe_hold = [pr for pr in pe_results if pr["status"] == "BEAT-AND-HOLD"]
    if pe_hold:
        bb += ["", "**Post-earnings beat-and-hold (clean entries):** " +
               ", ".join(f"{pr['t']} ({pr['overall']*100:+.0f}% vs pre-earnings)" for pr in pe_hold)]
    bb.append("")
    bb.append("_Watches OUR own recommendations; alerts once per confirm/extend transition. "
              "Post-earnings watch re-surfaces beat-and-hold names. "
              "Prices ~15min delayed - take entry/stop from the live feed._")
    open(os.path.join(REPO, "watchlists", "live-picks-brief-block.md"),
         "w", encoding="utf-8").write("\n".join(bb))

    print(f"picks {len(picks)} | priced {len(cur)} | fires {len(fires)} | "
          f"pe_watch {len(pe_results)} | pe_fires {len(pe_fires)}")
    for r in fires:
        print(f"  FIRE {r['tkr']} ({r['industry']}) {r['tier']} +{r['ret']*100:.0f}% "
              f"reco {r['flag']:.2f} now {r['cur']:.2f}")
    for pr in pe_fires:
        print(f"  PE-FIRE {pr['t']} BEAT-AND-HOLD reaction {pr['react']*100:+.0f}% now {pr['cur']:.2f}")

    if not DRY:
        for r in fires:
            state[r["tkr"]] = r["tier"]
        for pr in pe_fires:
            state["PE:" + pr["t"]] = "BEAT-AND-HOLD"
        json.dump(state, open(STATE, "w"), indent=1)

    return 10 if ((fires or pe_fires) and not DRY) else 0


if __name__ == "__main__":
    sys.exit(main())
