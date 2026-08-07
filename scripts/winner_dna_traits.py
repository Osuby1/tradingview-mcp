#!/usr/bin/env python3
"""Winner-DNA remaining-traits scan (pre-registered list): what did RUNNERS look
like on their first-recommendation day that same-period DUDS did not?

Sample: every ticker first-recommended by the origination scanner 7/1-7/25
(so every name has >=2 weeks of forward data). RUNNER = best close since rec
>= +15% above rec price. DUD = never exceeded +5%. Middle excluded.
Traits AS OF rec date (no look-ahead): RVOL(flag vol / 20d avg), % of 52wk
high, ADX14, DI margin, % vs 200d SMA, dollar-volume. SI and sector-state
excluded honestly (no historical snapshots exist for either).
Separation bar: bootstrap 95% CI of the runner-minus-dud mean difference
excluding zero."""
import statistics as st, random, json
import pandas as pd, yfinance as yf
from pathlib import Path
random.seed(7)
LOG = Path.home()/"Documents"/"Equities_Scanner"/"recommendations_log.csv"
d = pd.read_csv(LOG).dropna(subset=["date","ticker","price"]).sort_values("date")
first = d.groupby("ticker").first().reset_index()
first = first[(first.date>="2026-07-01")&(first.date<="2026-07-25")]
syms = sorted(set(first.ticker.str.upper()))
px = yf.download(syms, start="2025-07-01", end="2026-08-08", progress=False,
                 auto_adjust=True, group_by="ticker", threads=True)
def adx_di(h, n=14):
    up = h.High.diff(); dn = -h.Low.diff()
    plus = ((up>dn)&(up>0))*up; minus = ((dn>up)&(dn>0))*dn
    tr = (h.High-h.Low).combine((h.High-h.Close.shift()).abs(),max).combine((h.Low-h.Close.shift()).abs(),max)
    atr = tr.ewm(alpha=1/n, adjust=False).mean()
    pdi = 100*plus.ewm(alpha=1/n,adjust=False).mean()/atr
    mdi = 100*minus.ewm(alpha=1/n,adjust=False).mean()/atr
    dx = 100*(pdi-mdi).abs()/(pdi+mdi)
    return float(dx.ewm(alpha=1/n,adjust=False).mean().iloc[-1]), float(pdi.iloc[-1]-mdi.iloc[-1])
rows=[]
for _,r in first.iterrows():
    s=str(r.ticker).upper()
    try: h=px[s].dropna()
    except Exception: continue
    idx=h.index[h.index<=pd.Timestamp(str(r.date)[:10])]
    if len(idx)<210: continue
    pos=h.index.get_loc(idx[-1]); sub=h.iloc[:pos+1]
    entry=float(r.price)
    if entry<=0: continue
    fwd=h.iloc[pos+1:]
    if len(fwd)<8: continue
    best=(float(fwd.Close.max())/entry-1)*100
    cls="RUNNER" if best>=15 else ("DUD" if best<5 else None)
    if not cls: continue
    c=sub.Close
    try: adx,dim=adx_di(sub.tail(120))
    except Exception: continue
    rows.append({"sym":s,"cls":cls,"best":round(best,1),
        "rvol":round(float(sub.Volume.iloc[-1]/max(sub.Volume.tail(21).iloc[:-1].mean(),1)),2),
        "pct52h":round(float(c.iloc[-1]/sub.High.tail(252).max()*100),1),
        "adx":round(adx,1),"di_margin":round(dim,1),
        "vs200":round(float(c.iloc[-1]/c.tail(200).mean()-1)*100,1),
        "dvol_m":round(float((c*sub.Volume).tail(20).mean())/1e6,1)})
R=[x for x in rows if x["cls"]=="RUNNER"]; D=[x for x in rows if x["cls"]=="DUD"]
print(f"classified: {len(R)} RUNNERS (best >= +15%) vs {len(D)} DUDS (< +5%), middle excluded, of {len(rows)} total\n")
print(f"{'trait':<12}{'runners':>10}{'duds':>10}{'diff':>8}{'95% CI of diff':>20}{'verdict':>12}")
for t in ["rvol","pct52h","adx","di_margin","vs200","dvol_m"]:
    a=[x[t] for x in R]; b=[x[t] for x in D]
    diffs=sorted(st.mean(random.choices(a,k=len(a)))-st.mean(random.choices(b,k=len(b))) for _ in range(2000))
    lo,hi=diffs[50],diffs[1949]
    sig="SEPARATES" if (lo>0 or hi<0) else "noise"
    print(f"{t:<12}{st.mean(a):>10.1f}{st.mean(b):>10.1f}{st.mean(a)-st.mean(b):>8.1f}{f'[{lo:+.1f},{hi:+.1f}]':>20}{sig:>12}")
json.dump(rows, open("research/winner-dna-traits.json","w"), indent=1)
print("\nwrote research/winner-dna-traits.json")
