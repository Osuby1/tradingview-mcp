#!/usr/bin/env python3
"""Winner Score v1 FORWARD SHADOW (prereg bar 4). STANDALONE by design - the
live selector is never imported or altered; this reads tonight's funnel output,
scores the same eligible pool with WS-full (traits + source), and writes a side
file. I carry the readings into briefs; nothing here ranks a live card.
Promotion needs 2-3 weeks of these agreeing with the backtest, then Omar's word."""
import json, sys, datetime as dt
from pathlib import Path
import numpy as np, pandas as pd, yfinance as yf
REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from selection_validation import indicators, ws_traits

SOURCE_PTS = {"orig-COILED": 2, "orig-FRESH IGNITION": 1, "og-chandelier": 1,
              "sweep-CE": 1, "orig-BUY ZONE": 0}

def main():
    date = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat()
    fp = REPO / "reports" / f"funnel-{date}.json"
    if not fp.exists():
        print(f"[ws-shadow] no funnel for {date}"); return 0
    fn = json.loads(fp.read_text())
    pool = fn.get("eligible_cohort", [])
    if not pool:
        print("[ws-shadow] empty cohort"); return 0
    syms = sorted({p["sym"] for p in pool})
    px = yf.download(syms, period="1y", progress=False, auto_adjust=True,
                     group_by="ticker", threads=True)
    out = []
    for p in pool:
        s = p["sym"]
        try: h = px[s].dropna()
        except Exception: continue
        if len(h) < 210: continue
        atr14, atr22, adx, pdi, mdi, sma200, dvol = indicators(h)
        a, dm = float(adx.iloc[-1]), float(pdi.iloc[-1] - mdi.iloc[-1])
        v2 = (float(h.Close.iloc[-1]) / float(sma200.iloc[-1]) - 1) * 100 if not np.isnan(sma200.iloc[-1]) else -99
        dv = float(dvol.iloc[-1]) / 1e6 if not np.isnan(dvol.iloc[-1]) else 0
        wt = ws_traits(a, dm, v2, dv)
        wf = wt + SOURCE_PTS.get(str(p.get("source", "")), 0)
        out.append({"sym": s, "ws_traits": wt, "ws_full": wf,
                    "readiness": p.get("readiness"), "source": p.get("source"),
                    "selected_by_live": p.get("selected"), "ref_price": p.get("ref_price")})
    out.sort(key=lambda x: -x["ws_full"])
    live_picks = [x["sym"] for x in out if x["selected_by_live"]]
    ws_picks = [x["sym"] for x in out[:3]]
    rec = {"date": date, "rankings": out, "live_top3": live_picks, "ws_top3": ws_picks,
           "agreement": sorted(set(live_picks) & set(ws_picks))}
    (REPO / "research" / f"shadow-ws-{date}.json").write_text(json.dumps(rec, indent=1))
    print(f"[ws-shadow] {date}: WS top-3 = {ws_picks} | live picked {live_picks} | overlap {rec['agreement']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
