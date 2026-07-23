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
    lines.append("| Ticker | Industry | Tier | Ret | Now | Reco px | Source | RVOL |")
    lines.append("|---|---|---|--:|--:|--:|---|--:|")
    for r in rows:
        lines.append(f"| {r['tkr']} | {r['industry']} | {r['tier']} | {r['ret']*100:+.0f}% | "
                     f"{r['cur']:.2f} | {r['flag']:.2f} | {r['source']} | {r['rvol']:.1f} |")
    open(os.path.join(REPO, "watchlists", f"live-picks-{today().isoformat()}.md"),
         "w", encoding="utf-8").write("\n".join(lines))

    # ----- compact BRIEF BLOCK (pinned to the top of every brief) -----
    movers = [r for r in rows if r["tier"] in ("CONFIRMING", "EXTENDED")]
    bb = [f"### Live Picks - what's running ({today().isoformat()})", ""]
    if not movers:
        bb.append("_No active picks currently confirming a run._")
    else:
        bb.append("| Ticker | Industry | Reco px | Now | Gain | Read |")
        bb.append("|---|---|--:|--:|--:|---|")
        for r in movers:
            read = ("DON'T CHASE - pullback only" if r["tier"] == "EXTENDED"
                    else "confirming - enter/add per plan")
            bb.append(f"| {r['tkr']} | {r['industry']} | {r['flag']:.2f} | {r['cur']:.2f} | "
                      f"{r['ret']*100:+.0f}% | {read} |")
    bb.append("")
    bb.append("_Watches OUR own recommendations; alerts once per confirm/extend transition. "
              "Prices ~15min delayed - take entry/stop from the live feed._")
    open(os.path.join(REPO, "watchlists", "live-picks-brief-block.md"),
         "w", encoding="utf-8").write("\n".join(bb))

    print(f"picks {len(picks)} | priced {len(cur)} | industries {len(ind)} | fires {len(fires)}")
    for r in fires:
        print(f"  FIRE {r['tkr']} ({r['industry']}) {r['tier']} +{r['ret']*100:.0f}% "
              f"reco {r['flag']:.2f} now {r['cur']:.2f}")

    if not DRY:
        for r in fires:
            state[r["tkr"]] = r["tier"]
        json.dump(state, open(STATE, "w"), indent=1)

    return 10 if (fires and not DRY) else 0


if __name__ == "__main__":
    sys.exit(main())
