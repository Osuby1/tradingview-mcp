#!/usr/bin/env python3
"""Tab-lifecycle price-action study (Omar 8/7, per research/tab-lifecycle-study-preregistration.md).
Events on the four origination tabs from the daily (date,ticker,tab) panel:
ARRIVAL / PERSISTENCE / TRANSITION (COOLING->BUY ZONE, COILED->FRESH IGNITION)
/ DROP-OFF. Forward +1/+3/+5/+10 sessions vs IWM. Bars: n>=15 + CI excludes 0."""
import glob, os, random, statistics as st, json
import pandas as pd, yfinance as yf
random.seed(7)
frames=[]
for f in sorted(glob.glob("research/recommendations_log-*.csv")):
    try:
        x=pd.read_csv(f); frames.append(x[["date","ticker","tab"]])
    except Exception: pass
panel=pd.concat(frames).dropna().drop_duplicates()
panel["tab"]=panel.tab.str.upper().str.strip()
panel["date"]=panel.date.astype(str).str[:10]
dates=sorted(panel.date.unique())
bytick={}
for _,r in panel.iterrows(): bytick.setdefault(r.ticker.upper(),{})[r.date]=r.tab
syms=sorted(bytick)
px=yf.download(syms+["IWM"],start="2026-05-01",end="2026-08-08",progress=False,auto_adjust=True,group_by="ticker",threads=True)
iwm=px["IWM"].dropna().Close
def fwd(sym,date,h):
    try: s=px[sym].dropna().Close
    except Exception: return None
    idx=s.index[s.index<=pd.Timestamp(date)]
    if len(idx)==0: return None
    p=s.index.get_loc(idx[-1])
    if p+h>=len(s): return None
    r=(float(s.iloc[p+h])/float(s.iloc[p])-1)*100
    ii=iwm.index[iwm.index<=pd.Timestamp(date)]
    q=iwm.index.get_loc(ii[-1])
    if q+h>=len(iwm): return None
    return r-(float(iwm.iloc[q+h])/float(iwm.iloc[q])-1)*100
events={}
for sym,hist in bytick.items():
    ds=sorted(hist)
    for i,dt_ in enumerate(ds):
        tab=hist[dt_]
        prev=hist.get(ds[i-1]) if i>0 else None
        # arrival: first day ever on this tab
        if all(hist[x]!=tab for x in ds[:i]):
            events.setdefault(f"ARRIVE {tab}",[]).append((sym,dt_))
        # persistence day 4+ consecutive same tab
        run=1; j=i-1
        while j>=0 and hist[ds[j]]==tab: run+=1; j-=1
        if run==4: events.setdefault(f"PERSIST4+ {tab}",[]).append((sym,dt_))
        # transitions
        if prev and prev!=tab:
            if prev=="COOLING" and tab=="BUY ZONE": events.setdefault("PROMO cooling->buyzone",[]).append((sym,dt_))
            if prev=="COILED" and tab=="FRESH IGNITION": events.setdefault("FIRE coiled->ignition",[]).append((sym,dt_))
    # drop-off: last panel date for a ticker that had >=3 tab-days, before the final panel date
    if len(ds)>=3 and ds[-1] < dates[-3]:
        events.setdefault("DROPOFF (left all tabs)",[]).append((sym,ds[-1]))
print(f"panel: {len(panel)} tab-days, {len(syms)} tickers, {dates[0]}..{dates[-1]}\n")
out={}
print(f"{'event':<28}{'n':>5} | mean excess vs IWM (95% CI) at +1 / +3 / +5 / +10 sessions")
for ev in sorted(events):
    res={}
    for h in (1,3,5,10):
        v=[x for x in (fwd(s,dt_,h) for s,dt_ in events[ev]) if x is not None]
        if len(v)<15: res[h]=(len(v),None,None,None); continue
        boots=sorted(st.mean(random.choices(v,k=len(v))) for _ in range(2000))
        res[h]=(len(v),st.mean(v),boots[50],boots[1949])
    cells=[]
    for h in (1,3,5,10):
        n,m,lo,hi=res[h]
        if m is None: cells.append(f"n={n}<15")
        else:
            star="*" if (lo>0 or hi<0) else ""
            cells.append(f"{m:+.1f}[{lo:+.1f},{hi:+.1f}]{star}")
    print(f"{ev:<28}{len(events[ev]):>5} | " + "  ".join(cells))
    out[ev]={"n":len(events[ev]),"horizons":{h:res[h] for h in (1,3,5,10)}}
json.dump({k:{"n":v["n"]} for k,v in out.items()}, open("research/tab-lifecycle-results.json","w"), indent=1)
print("\n* = CI excludes zero (candidate signal). wrote research/tab-lifecycle-results.json")
