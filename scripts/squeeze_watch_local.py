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
        hits.append({
            "sym": row["s"],
            "price": close,
            "msg": (f"SQUEEZE WATCH: {name} +{chg:.1f}% RVOL {rvol:.1f}, SI {si}% float - "
                    f"CAR-style ignition. LOOK only: $300 OTM-call playbook (squeeze-watch.json), "
                    f"no chase, verify news+chain.")})
        state["alerted"][name] = close

    # market-wide blast - with SHORT-INTEREST GATE (added 8/6 after five
    # straight blast alerts (HNST/ASPN/AEVA/WPP/DCTH) all failed the squeeze
    # test on SI: the net was catching big movers, not squeezes. Now the
    # watcher does the verification BEFORE it interrupts Omar. Sub-bar names
    # are logged for the EOD brief's mover section, never pushed.)
    parked = []
    for row in scan({"columns": ["name", "close", "change", "relative_volume_10d_calc", "market_cap_basic"],
                     "sort": {"sortBy": "change", "sortOrder": "desc"}, "range": [0, 10],
                     "filter": [{"left": "change", "operation": "greater", "right": 18},
                                {"left": "relative_volume_10d_calc", "operation": "greater", "right": 4},
                                {"left": "market_cap_basic", "operation": "greater", "right": 500000000},
                                {"left": "close", "operation": "greater", "right": 3},
                                {"left": "exchange", "operation": "in_range", "right": ["NYSE", "NASDAQ", "AMEX"]}]}):
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
        si_txt = f"SI {si}% float - PASSES the squeeze bar" if si is not None else "SI unknown - verify"
        hits.append({
            "sym": row["s"],
            "price": close,
            "msg": (f"SQUEEZE WATCH (blast): {name} +{chg:.1f}% RVOL {rvol:.1f}, {si_txt}. "
                    f"$300 OTM-call playbook applies if the catalyst checks out - verify news+chain.")})
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
