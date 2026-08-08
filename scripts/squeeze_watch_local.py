"""LOCAL squeeze ignition watcher (plan B after cloud watchers failed 8/6:
sandbox network policy blocked the scanner; local scanner access is proven).

Runs every 20 min via Task Scheduler (8:35-15:05 CT weekdays). Detects
CAR-style ignitions per watchlists/squeeze-watch.json, dedupes per day,
then pushes to Omar's phone by creating INSTANT-FIRE TradingView alerts
(node scripts/squeeze_alert_push.mjs via CDP - the channel his phone
already receives; instant-fire trick: a cross alert set a hair below the
live price fires on the next tick).

Usage:
  python scripts/squeeze_watch_local.py           # normal patrol
  python scripts/squeeze_watch_local.py --test    # force a validation push
"""
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent.parent
CFG = REPO / "watchlists" / "squeeze-watch.json"
STATE = REPO / "watchlists" / "squeeze-watch-state.json"
HITS = REPO / "watchlists" / "squeeze-hits.json"
SCAN = "https://scanner.tradingview.com/america/scan"
REALERT_GAIN = 1.07  # re-alert same name only if +7% beyond last alerted price


def in_window(now):
    if now.weekday() >= 5:
        return False
    t = now.hour * 60 + now.minute
    return (8 * 60 + 30) <= t <= (15 * 60 + 5)


def scan(body):
    r = requests.post(SCAN, json=body, timeout=30)
    r.raise_for_status()
    return r.json().get("data", [])


STAGED = REPO / "watchlists" / "staged-tickets.json"


def final_hour_check(now, state):
    """2026-08-07 timing-study workflow: a blast/tinder alert STAGES a candidate;
    the fill window is the FINAL HOUR (14:00-15:00 CT), where spike premium has
    deflated and the day-1 health verdict is readable (study: final-hour entry
    beat our fills AND day-2 opens on both SOUN and HTZ, ~35% chase tax).
    The 14:15/14:35/14:55 patrols push the window-open reminder with a live
    health read so Omar gets the GO/NO-GO on his phone even with no session.
    Detection pushes remain IMMEDIATE - only the fill waits.
    Staged entries: [{"sym","note","card_price"}] - written when a card is staged.
    """
    if not (14 <= now.hour < 15):
        return []
    out = []
    try:
        staged = json.loads(STAGED.read_text()) if STAGED.exists() else []
        if CANDIDATES.exists():   # auto-staged candidates join the window pings
            today = now.strftime("%Y-%m-%d")
            for r in json.loads(CANDIDATES.read_text()):
                if r.get("date") == today and not any(
                        s.get("sym","").split(":")[-1] == r["sym"] for s in staged):
                    ch = r.get("chain") or {}
                    staged.append({"sym": r["sym"],
                                   "note": f"{ch.get('contract','?')} ~{ch.get('mid','?')} - trade ONLY if 1:45 verification said READY"})
        syms = [s["sym"] if ":" in s["sym"] else None for s in staged]
        import requests as rq
        cands = [f"{ex}:{s['sym']}" for s in staged for ex in ("NASDAQ", "NYSE", "AMEX")
                 if ":" not in s["sym"]] + [x for x in syms if x]
        r = rq.post("https://scanner.tradingview.com/america/scan",
                    json={"symbols": {"tickers": cands, "query": {"types": []}},
                          "columns": ["close", "low", "high", "volume",
                                      "average_volume_10d_calc", "change"]},
                    timeout=25, headers={"User-Agent": "Mozilla/5.0"})
        live = {e["s"].split(":")[1]: e["d"] for e in r.json().get("data", [])
                if e.get("d", [None])[0] is not None}
        for s in staged:
            sym = s["sym"].split(":")[-1]
            key = f"FINALHOUR:{sym}"
            if state["alerted"].get(key):
                continue                      # one window push per name per day
            v = live.get(sym)
            if not v:
                continue
            close, lo, hi, vol, avol, chg = v
            rng = (close - lo) / max(hi - lo, 1e-9)
            healthy = (chg > 0) and (rng >= 0.5 or (avol and vol >= 2 * avol))
            out.append({"sym": sym, "px": close,
                        "msg": (f"FINAL-HOUR WINDOW {sym}: health "
                                f"{'PASS' if healthy else 'FAIL'} (day {chg:+.1f}%, "
                                f"{rng*100:.0f}% of range, vol {vol/max(avol,1):.1f}x). "
                                f"{'Fill per card, mid-or-better.' if healthy else 'Shadow rule says STAND DOWN - day-1 health failing.'} "
                                f"Card: {s.get('note','')[:60]}")})
            state["alerted"][key] = close
    except Exception as e:
        print(f"[squeeze] final-hour check failed: {e}")
    return out



CANDIDATES = REPO / "watchlists" / "squeeze-candidates-today.json"


def chain_gate(sym, spot):
    """MECHANICAL chain gate (Omar 2026-08-07: alerts must be pre-validated).
    Finds the playbook contract - Sep 18 monthly, ~25-50% OTM, OI>=100,
    spread<=30%, ticket <=$450 for 2-10 contracts. Returns dict or None.
    Wrapped fully in try: a chain-check failure must never kill a patrol -
    it returns None and the name is labeled 'chain unverified'.
    """
    try:
        sys.path.insert(0, str(REPO / "scripts"))
        from ts_api import ts_quotes
        if spot >= 100: grid = [5, 10, 2.5]
        elif spot >= 25: grid = [2.5, 5, 1]
        elif spot >= 10: grid = [1, 2.5, 0.5]
        else: grid = [0.5, 1, 2.5]
        strikes = set()
        for inc in grid:
            for mult in (1.15, 1.25, 1.35, 1.5):
                k = round(round(spot * mult / inc) * inc, 2)
                strikes.add(int(k) if k == int(k) else k)
        # 8/8 audit fix: expiry was hardcoded '260918' - dead code after Sep.
        # Pick the nearest MONTHLY (3rd Friday) 25-55 days out, per the playbook.
        import datetime as _dt
        _today = _dt.date.today()
        _exp = None
        for _m in range(0, 4):
            _y = _today.year + (_today.month - 1 + _m) // 12
            _mo = (_today.month - 1 + _m) % 12 + 1
            _first = _dt.date(_y, _mo, 1)
            _third_fri = _first + _dt.timedelta(days=((4 - _first.weekday()) % 7) + 14)
            if 25 <= (_third_fri - _today).days <= 55:
                _exp = _third_fri; break
        if _exp is None:
            print(f"[squeeze] chain gate: no monthly 25-55d out (?)"); return None
        _tag = _exp.strftime("%y%m%d")
        osyms = [f"{sym} {_tag}C{k}" for k in sorted(strikes)]
        q = ts_quotes(osyms)
        best = None
        for c, x in q.items():
            if not isinstance(x, dict):
                continue
            b, a = float(x.get("Bid") or 0), float(x.get("Ask") or 0)
            oi = int(x.get("DailyOpenInterest") or 0)
            if b <= 0 or a <= 0 or oi < 100:
                continue
            mid = (a + b) / 2
            spread = (a - b) / mid * 100
            if spread > 30 or not (0.05 <= mid <= 2.5):
                continue
            n = max(1, min(10, int(350 / (mid * 100))))
            cand = {"contract": c, "mid": round(mid, 2), "spread_pct": round(spread),
                    "oi": oi, "qty": n, "ticket_usd": int(n * mid * 100)}
            if best is None or oi > best["oi"]:
                best = cand
        return best
    except Exception as e:
        print(f"[squeeze] chain gate failed for {sym}: {e}")
        return None


def stage_candidate(sym, close, chg, si, chain, state, today):
    """Append a fully-mechanically-gated candidate to the staged file and push
    the repo so the 1:45 PM cloud verifier can read it. One stage per name/day."""
    try:
        rows = json.loads(CANDIDATES.read_text()) if CANDIDATES.exists() else []
    except Exception:
        rows = []
    if any(r.get("sym") == sym and r.get("date") == today for r in rows):
        return False
    rows.append({"date": today, "sym": sym, "detected_px": close, "day_chg_pct": chg,
                 "si_pct_float": si, "chain": chain,
                 "status": "MECHANICAL PASS - catalyst verification pending",
                 "fill_window": "14:00-15:00 CT, mid-or-better, health must pass"})
    CANDIDATES.write_text(json.dumps(rows, indent=1))
    try:
        subprocess.run(["git", "add", str(CANDIDATES)], cwd=REPO, capture_output=True, timeout=30)
        subprocess.run(["git", "commit", "-q", "-m",
                        f"squeeze candidate staged: {sym} (mechanical gates passed)"],
                       cwd=REPO, capture_output=True, timeout=30)
        subprocess.run(["git", "push", "fork", "add-watchlist-files:main"], cwd=REPO, capture_output=True, timeout=60)  # 8/8 audit: origin is 403; the cloud verifier reads the FORK
    except Exception as e:
        print(f"[squeeze] candidate git push failed (cloud verifier may not see it): {e}")
    return True


def main():
    test = "--test" in sys.argv
    now = dt.datetime.now()
    if not test and not in_window(now):
        print(f"[squeeze] {now:%H:%M} outside window")
        return 0

    cfg = json.loads(CFG.read_text(encoding="utf-8"))
    tinder = {t["sym"].split(":")[1]: t for t in cfg["tinder"]}
    tickers = [t["sym"] for t in cfg["tinder"]]

    state = {"date": "", "alerted": {}}
    if STATE.exists():
        state = json.loads(STATE.read_text())
    today = now.strftime("%Y-%m-%d")
    if state.get("date") != today:
        state = {"date": today, "alerted": {}}

    hits = []
    # tinder check
    for row in scan({"symbols": {"tickers": tickers},
                     "columns": ["name", "close", "change", "relative_volume_10d_calc"]}):
        name, close, chg, rvol = row["d"][0], row["d"][1], row["d"][2] or 0, row["d"][3] or 0
        fired = (chg >= 8 and rvol >= 3) or chg >= 15
        if not fired:
            continue
        last = state["alerted"].get(name)
        if last and close < last * REALERT_GAIN:
            continue
        si = tinder.get(name, {}).get("si_pct_float", "?")
        chain = chain_gate(name, close)
        if chain:
            stage_candidate(name, close, chg, si, chain, state, today)
            msg = (f"SQUEEZE CANDIDATE {name}: +{chg:.1f}% RVOL {rvol:.1f}, SI {si}%, "
                   f"chain PASS ({chain['contract'].split()[-1]} mid {chain['mid']} OI {chain['oi']}, "
                   f"~${chain['ticket_usd']}). Catalyst check ~1:45, fill window 2-3 PM if READY+health. NOT a buy yet.")
        else:
            msg = (f"SQUEEZE WATCH {name}: +{chg:.1f}% RVOL {rvol:.1f}, SI {si}% - anatomy fires "
                   f"but NO tradeable chain (or check failed). Watch only - no ticket exists.")
        hits.append({"sym": row["s"], "price": close, "msg": msg})
        state["alerted"][name] = close

    # market-wide blast - with SHORT-INTEREST GATE (added 8/6 after five
    # straight blast alerts (HNST/ASPN/AEVA/WPP/DCTH) all failed the squeeze
    # test on SI: the net was catching big movers, not squeezes. Now the
    # watcher does the verification BEFORE it interrupts Omar. Sub-bar names
    # are logged for the EOD brief's mover section, never pushed.)
    # TWO BLAST TIERS (2nd added 8/6 after IOVA - up 40.6% with 23.9% SI, a
    # textbook squeeze - was BLOCKED by the rvol>=4 filter at rvol 3.38.
    # Big-float names carry high average volume, so a monster % move can
    # print "only" 3x. Tier 2 catches size-of-move when volume is merely high.)
    base = [{"left": "market_cap_basic", "operation": "greater", "right": 500000000},
            {"left": "close", "operation": "greater", "right": 3},
            {"left": "exchange", "operation": "in_range", "right": ["NYSE", "NASDAQ", "AMEX"]}]
    blast_rows, seen_blast = [], set()
    for chg_min, rvol_min in ((18, 4), (30, 2.5)):
        for row in scan({"columns": ["name", "close", "change", "relative_volume_10d_calc", "market_cap_basic"],
                         "sort": {"sortBy": "change", "sortOrder": "desc"}, "range": [0, 10],
                         "filter": [{"left": "change", "operation": "greater", "right": chg_min},
                                    {"left": "relative_volume_10d_calc", "operation": "greater", "right": rvol_min}] + base}):
            if row["d"][0] not in seen_blast:
                seen_blast.add(row["d"][0])
                blast_rows.append(row)

    parked = []
    for row in blast_rows:
        name, close, chg, rvol = row["d"][0], row["d"][1], row["d"][2] or 0, row["d"][3] or 0
        if name in tinder:
            continue  # tinder path already handled it with SI context
        last = state["alerted"].get(name)
        if last and close < last * REALERT_GAIN:
            continue
        si = None
        try:
            import yfinance as yf
            spf = yf.Ticker(name).info.get("shortPercentOfFloat")
            si = round(spf * 100, 1) if spf is not None else None
        except Exception:
            si = None
        if si is not None and si < 15:
            parked.append({"sym": name, "chg": round(chg, 1), "rvol": round(rvol, 1), "si": si,
                           "why_parked": "SI below the 15% squeeze bar - big mover, not a squeeze"})
            state["alerted"][name] = close  # don't re-evaluate all day
            continue
        si_txt = f"SI {si}%" if si is not None else "SI unknown - verify"
        chain = chain_gate(name, close)
        if chain:
            stage_candidate(name, close, chg, si, chain, state, today)
            msg = (f"SQUEEZE CANDIDATE (blast) {name}: +{chg:.1f}% RVOL {rvol:.1f}, {si_txt}, "
                   f"chain PASS ({chain['contract'].split()[-1]} mid {chain['mid']} OI {chain['oi']}, "
                   f"~${chain['ticket_usd']}). Catalyst check ~1:45, fill window 2-3 PM if READY+health. NOT a buy yet.")
        else:
            msg = (f"SQUEEZE WATCH (blast) {name}: +{chg:.1f}% RVOL {rvol:.1f}, {si_txt} - "
                   f"anatomy fires but NO tradeable chain. Watch only - no ticket exists.")
        hits.append({"sym": row["s"], "price": close, "msg": msg})
        state["alerted"][name] = close
    if parked:
        pf = REPO / "watchlists" / "squeeze-parked.json"
        prior = json.loads(pf.read_text()) if pf.exists() else {}
        if prior.get("date") != today:
            prior = {"date": today, "parked": []}
        prior["parked"].extend(parked)
        pf.write_text(json.dumps(prior, indent=1))
        print(f"[squeeze] parked (big movers, sub-15% SI, NOT pushed): "
              f"{[p['sym'] + ' SI' + str(p['si']) for p in parked]}")

    if test:
        hits.insert(0, {"sym": "AMEX:SPY", "price": None,
                        "msg": f"SQUEEZE WATCHER (LOCAL) ONLINE {now:%H:%M} - scanner OK, "
                               f"{len(tickers)} tinder names patrolled. -Claude"})

    if not hits:
        print(f"[squeeze] {now:%H:%M} no ignition ({len(tickers)} tinder checked)")
        STATE.write_text(json.dumps(state, indent=1))
        return 0

    hits = hits[:3] if not test else hits[:4]  # push cap per patrol
    hits += final_hour_check(now, state)       # staged-ticket window reminders
    HITS.write_text(json.dumps(hits, indent=1))
    STATE.write_text(json.dumps(state, indent=1))
    print(f"[squeeze] {now:%H:%M} {len(hits)} push(es): {[h['sym'] for h in hits]}")
    rc = subprocess.run(["node", str(REPO / "scripts" / "squeeze_alert_push.mjs")],
                        capture_output=True, text=True, timeout=120)
    print(rc.stdout.strip())
    if rc.returncode != 0:
        print("PUSH FAILED:", rc.stderr.strip()[:300])
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
