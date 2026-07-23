"""Live PEAD signal: the freshest high-SUE mid-caps, as a PAPER basket to forward-test.

Omar, 2026-07-22: act on the 20-day mid-cap PEAD signal and forward-validate it.
The signal FAILED the strict two-horizon bar but showed a real, clean 20-day edge
(IC +0.051, high-SUE mid-caps +0.49% vs SPY over 20d). It is UNPROVEN LIVE, so we
do NOT size real money - we register a paper basket and let the outcome tracker
grade it against SPY over the next ~20 sessions. Real money only if it holds up.

Logic:
  * For each mid-cap name, compute point-in-time SUE (EDGAR, split-adjusted).
  * Keep names whose LATEST earnings filed within FRESH_DAYS calendar days - the
    20-day drift is still mostly ahead.
  * Rank by SUE; the top positive-SUE names are the paper LONG basket.
  * Register each as a paper call in calls-ledger.json (source PEAD-SUE-20d-paper)
    at today's price, so outcome_tracker.py grades it forward vs SPY.

Usage: python scripts/pead_live_signal.py [YYYY-MM-DD]
"""
import json
import os
import sys
import time

import pandas as pd
import yfinance as yf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edgar_sue_backtest import cik_map, quarterly_eps, split_adjust, compute_sue  # noqa

FRESH_DAYS = 18       # latest filing must be within this many calendar days
TOP_N = 12
MIN_SUE = 0.5         # only genuinely positive surprises


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else pd.Timestamp.today().strftime("%Y-%m-%d")
    uni = json.load(open("research/midcap-universe.json"))
    syms = uni["symbols"]
    print(f"scanning {len(syms)} mid-caps for fresh high-SUE earnings...")

    cm = cik_map()
    today = pd.Timestamp(date)
    cands = []
    for i, s in enumerate(syms):
        if s not in cm:
            continue
        try:
            sp = yf.Ticker(s).splits
            splits = {pd.Timestamp(d).tz_localize(None): float(r)
                      for d, r in sp.items() if r and r != 1.0}
        except Exception:
            splits = {}
        eps = split_adjust(quarterly_eps(cm[s]), splits)
        sue = compute_sue(eps)
        if not sue:
            continue
        latest = sue[-1]
        age = (today - pd.Timestamp(latest["filed"])).days
        if 0 <= age <= FRESH_DAYS and latest["sue"] >= MIN_SUE:
            cands.append({"sym": s, "sue": round(latest["sue"], 2),
                          "filed": latest["filed"], "age_days": age,
                          "eps": latest["eps"]})
        if (i + 1) % 25 == 0:
            print(f"  {i+1}/{len(syms)}  fresh candidates {len(cands)}")
        time.sleep(0.12)

    cands.sort(key=lambda x: -x["sue"])
    basket = cands[:TOP_N]
    print(f"\nfresh high-SUE candidates: {len(cands)}; basket top {len(basket)}")

    # current prices for entry reference
    if basket:
        px = yf.download([c["sym"] for c in basket], period="5d", interval="1d",
                         auto_adjust=True, progress=False, group_by="ticker", threads=True)
        for c in basket:
            try:
                cc = px[c["sym"]]["Close"].dropna()
                c["price"] = round(float(cc.iloc[-1]), 2)
            except Exception:
                c["price"] = None

    out = {"date": date, "signal": "PEAD-SUE-20d (mid-cap, PAPER)",
           "fresh_days": FRESH_DAYS, "min_sue": MIN_SUE,
           "n_candidates": len(cands), "basket": basket,
           "note": "Unproven-live signal (failed the 2-horizon bar; real 20d edge). "
                   "Paper basket for forward validation vs SPY over ~20 sessions - "
                   "NOT sized with real money."}
    json.dump(out, open(f"research/pead-signal-{date}.json", "w"), indent=1)

    print("\nPAPER LONG BASKET (fresh high-SUE mid-caps):")
    print(f"{'sym':6}{'SUE':>7}{'filed':>13}{'age':>5}{'price':>9}")
    for c in basket:
        print(f"{c['sym']:6}{c['sue']:>7}{c['filed']:>13}{c['age_days']:>5}"
              f"{('$'+str(c['price'])) if c.get('price') else '   -':>9}")

    # register as paper calls in the ledger
    led = json.load(open("research/calls-ledger.json"))
    have = {c["id"] for c in led["calls"]}
    added = 0
    for c in basket:
        if not c.get("price"):
            continue
        cid = f"{date}-{c['sym']}-pead-paper"
        if cid in have:
            continue
        led["calls"].append({
            "id": cid, "date": date, "sym": c["sym"], "dir": "long",
            "ref": c["price"], "stop": None, "target": None,
            "source": "PEAD-SUE-20d-paper",
            "fill": "paper (not sized - forward validation only)",
            "thesis": f"fresh high-SUE {c['sue']} (filed {c['filed']}, {c['age_days']}d ago); "
                      f"20-day drift test"})
        added += 1
    json.dump(led, open("research/calls-ledger.json", "w"), indent=1)
    print(f"\nregistered {added} paper calls in calls-ledger.json (source PEAD-SUE-20d-paper)")
    print("outcome_tracker.py will grade them vs SPY as the ~20-day window closes.")


if __name__ == "__main__":
    main()
