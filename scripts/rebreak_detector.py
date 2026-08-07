#!/usr/bin/env python3
"""BASE-AND-REBREAK detector (Omar decision #7, 8/7) - the PLTR pattern as a
first-class nightly screen. Pattern: a big earnings gap (>= +12% close-to-close),
then 2-5 sessions basing WITHOUT closing below the gap day's midpoint, then a
CLOSE above the gap day's HIGH = the re-break. That close IS the signal; the
morning brief presents it with the full protocol (per the standing order).
CREDIT + honest status: OMAR found the PLTR pattern (8/7 AM, asking why it was
never recommended); this detector reproduces his catch retroactively. It is NOT
validated until signals it finds FIRST (ZBRA/AUGO forward) are graded."""
import json, sys, datetime as dt
from pathlib import Path
import requests
import pandas as pd, yfinance as yf
REPO = Path(__file__).resolve().parent.parent

def main():
    today = dt.date.today().isoformat()
    # coarse pass: liquid names that reported in the last 10 days and are up on the week
    r = requests.post("https://scanner.tradingview.com/america/scan", json={
        "filter": [{"left":"market_cap_basic","operation":"egreater","right":2e9},
                   {"left":"type","operation":"equal","right":"stock"},
                   {"left":"is_primary","operation":"equal","right":True},
                   {"left":"exchange","operation":"in_range","right":["NYSE","NASDAQ","AMEX"]},
                   {"left":"Perf.W","operation":"egreater","right":6},
                   {"left":"average_volume_10d_calc","operation":"egreater","right":500000}],
        "columns": ["name","close","earnings_release_date","Perf.W"],
        "sort": {"sortBy":"Perf.W","sortOrder":"desc"}, "range":[0,120]},
        timeout=30, headers={"User-Agent": "Mozilla/5.0"})
    now = dt.datetime.now(dt.UTC).timestamp()
    cands = [e["d"][0] for e in r.json().get("data", [])
             if e["d"][2] and (now - e["d"][2]) < 12*86400]
    if not cands:
        print("[rebreak] no candidates in the coarse pass"); return 0
    px = yf.download(sorted(set(cands)), period="1mo", progress=False,
                     auto_adjust=True, group_by="ticker", threads=True)
    signals = []
    for s in sorted(set(cands)):
        try: h = px[s].dropna()
        except Exception: continue
        if len(h) < 8: continue
        c = h.Close
        for g in range(len(h)-7, len(h)-2):          # gap day 2-6 sessions back
            if g < 1: continue
            gap = (float(c.iloc[g])/float(c.iloc[g-1]) - 1)*100
            if gap < 12: continue
            gap_hi, gap_mid = float(h.High.iloc[g]), (float(h.High.iloc[g])+float(h.Low.iloc[g]))/2
            base = c.iloc[g+1:-1]
            if len(base) < 1 or (base < gap_mid).any(): continue     # base must hold the midpoint
            if (base > gap_hi).any(): continue                        # re-break must be TODAY, not stale
            if float(c.iloc[-1]) > gap_hi:                            # today's close re-breaks
                signals.append({"sym": s, "gap_day": str(h.index[g].date()), "gap_pct": round(gap,1),
                                "gap_high": round(gap_hi,2), "close": round(float(c.iloc[-1]),2),
                                "base_days": len(base)})
                break
    print(f"[rebreak] {len(cands)} recent gappers screened -> {len(signals)} RE-BREAK signal(s)")
    for s in signals:
        print(f"  REBREAK >> {s['sym']}: gapped +{s['gap_pct']}% {s['gap_day']}, based {s['base_days']}d, closed {s['close']} above the {s['gap_high']} gap high")
    (REPO/"watchlists"/f"rebreak-signals-{today}.json").write_text(json.dumps(signals, indent=1))
    return 0

if __name__ == "__main__":
    sys.exit(main())
