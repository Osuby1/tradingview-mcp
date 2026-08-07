#!/usr/bin/env python3
"""Does a sector IGNITING transition predict forward gains? (pre-registered 8/7)

Replicates rotation_radar.py's EXACT rule daily over ~2 years:
  accel = 21-session return - (126-session return / 6)
  IGNITING day: accel >= 8 AND 21s return beats SPY's AND 5-session > -2%
  TRANSITION: first IGNITING day after >=5 non-igniting days (fresh ignition,
  matching how the radar surfaces "NEW entrant").
Measures forward 3/5/10-session ETF returns, raw and vs SPY. No look-ahead:
all inputs computed through the transition day's close; entry at that close.
"""
import statistics as st
import pandas as pd, yfinance as yf

ETFS = ["XLE","XOP","OIH","XLF","KRE","XLK","SMH","IGV","SKYY","XBI","IBB",
        "XLV","XLI","ITA","JETS","XLU","XLP","XLY","XLB","XME","GDX","URA",
        "KWEB","XRT","ARKK","IWM"]
px = yf.download(ETFS+["SPY"], start="2024-06-01", end="2026-08-08",
                 progress=False, auto_adjust=True)["Close"].dropna(how="all")
spy = px["SPY"]
events=[]
for t in ETFS:
    s = px[t].dropna()
    if len(s) < 200: continue
    m1 = s.pct_change(21)*100; m6 = s.pct_change(126)*100; w = s.pct_change(5)*100
    sm1 = spy.reindex(s.index).ffill().pct_change(21)*100
    accel = m1 - m6/6
    ign = (accel>=8) & (m1>sm1) & (w>-2)
    for i in range(131, len(s)-10):
        if ign.iloc[i] and not ign.iloc[i-5:i].any():
            fwd = {h: (float(s.iloc[i+h])/float(s.iloc[i])-1)*100 for h in (3,5,10)}
            spyf = {h: (float(spy.reindex(s.index).ffill().iloc[i+h])/float(spy.reindex(s.index).ffill().iloc[i])-1)*100 for h in (3,5,10)}
            events.append({"etf":t,"date":str(s.index[i].date()),"accel":round(float(accel.iloc[i]),1),
                           **{f"fwd{h}":round(fwd[h],2) for h in (3,5,10)},
                           **{f"exc{h}":round(fwd[h]-spyf[h],2) for h in (3,5,10)}})
print(f"fresh IGNITING transitions found: {len(events)} across {len(set(e['etf'] for e in events))} ETFs, Jun 2024 - Aug 2026\n")
for h in (3,5,10):
    f=[e[f"fwd{h}"] for e in events]; x=[e[f"exc{h}"] for e in events]
    import random; random.seed(7)
    boots=sorted(st.mean(random.choices(x,k=len(x))) for _ in range(2000))
    lo,hi=boots[50],boots[1949]
    print(f"+{h:>2} sessions: raw mean {st.mean(f):+.2f}% (median {st.median(f):+.2f}%) | "
          f"vs SPY {st.mean(x):+.2f}% CI[{lo:+.2f},{hi:+.2f}] | win {100*sum(1 for v in x if v>0)/len(x):.0f}% | "
          f">= +3%: {100*sum(1 for v in f if v>=3)/len(f):.0f}%")
# strength split: does BIGGER accel pay more?
hi_a=[e for e in events if e["accel"]>=12]; lo_a=[e for e in events if e["accel"]<12]
print(f"\naccel >= 12 (strong ignitions, n={len(hi_a)}): +5s vs SPY {st.mean([e['exc5'] for e in hi_a]):+.2f}% | win {100*sum(1 for e in hi_a if e['exc5']>0)/max(len(hi_a),1):.0f}%")
print(f"accel 8-12  (marginal,       n={len(lo_a)}): +5s vs SPY {st.mean([e['exc5'] for e in lo_a]):+.2f}% | win {100*sum(1 for e in lo_a if e['exc5']>0)/max(len(lo_a),1):.0f}%")
import json; json.dump(events, open("research/rotation-ignition-backtest.json","w"), indent=1)
print("\nwrote research/rotation-ignition-backtest.json")
