#!/usr/bin/env python3
"""Winner Score v1 validation - T2 (2-year replay) + T4 (stop width), per the
FROZEN prereg research/winner-score-v1-preregistration.md (commit c19b0a4).
No parameters here may differ from the prereg. Survivorship: universe = today's
466 names; absolutes never quoted as expectations; comparisons are the output."""
import json, math, random, statistics as st, sys, datetime as dt
from pathlib import Path
import numpy as np, pandas as pd, yfinance as yf
random.seed(7)
REPO = Path(__file__).resolve().parent.parent

def wilder(series, n):
    return series.ewm(alpha=1/n, adjust=False).mean()

def indicators(h):
    hi, lo, cl, vol = h.High, h.Low, h.Close, h.Volume
    tr = (hi-lo).combine((hi-cl.shift()).abs(), max).combine((lo-cl.shift()).abs(), max)
    atr14 = wilder(tr, 14); atr22 = wilder(tr, 22)
    up = hi.diff(); dn = -lo.diff()
    plus = ((up > dn) & (up > 0)) * up; minus = ((dn > up) & (dn > 0)) * dn
    pdi = 100 * wilder(plus, 14) / atr14; mdi = 100 * wilder(minus, 14) / atr14
    dx = 100 * (pdi - mdi).abs() / (pdi + mdi)
    adx = wilder(dx, 14)
    sma200 = cl.rolling(200).mean()
    dvol = (cl * vol).rolling(20).mean()
    return atr14, atr22, adx, pdi, mdi, sma200, dvol

def ce_flips(h, atr22):
    """Chandelier mode sim: long stop = HH22-3*ATR trailing up; short = LL22+3*ATR
    trailing down; flip on close crossing the active stop. Returns BUY-flip indices."""
    hh = h.High.rolling(22).max(); ll = h.Low.rolling(22).min()
    ls_raw = hh - 3*atr22; ss_raw = ll + 3*atr22
    mode, ls, ss, flips = None, -np.inf, np.inf, []
    cl = h.Close.values; lsr = ls_raw.values; ssr = ss_raw.values
    for i in range(len(h)):
        if np.isnan(lsr[i]) or np.isnan(ssr[i]): continue
        if mode is None: mode = "LONG" if len(flips) % 2 == 0 else "SHORT"; ls, ss = lsr[i], ssr[i]
        if mode == "LONG":
            ls = max(ls, lsr[i])
            if cl[i] < ls: mode, ss = "SHORT", ssr[i]
        else:
            ss = min(ss, ssr[i])
            if cl[i] > ss:
                mode, ls = "LONG", lsr[i]
                flips.append(i)
    return flips

def ws_traits(adx, dim, vs200, dvol_m):
    s = 0
    if adx >= 27: s += 1
    if adx >= 35: s += 1
    if dim >= 10: s += 1
    if dim >= 18: s += 1
    if vs200 >= 10: s += 1
    if 20 <= dvol_m <= 200: s += 1
    return s

def ci_diff(a, b, n=2000):
    d = sorted(st.mean(random.choices(a, k=len(a))) - st.mean(random.choices(b, k=len(b))) for _ in range(n))
    return d[50], d[1949]

def main():
    syms = sorted({e["sym"] for e in json.loads(
        (REPO/"watchlists"/"universe-results-2026-08-07.json").read_text()).get("all_names", [])
        if isinstance(e, dict) and e.get("sym")})
    print(f"universe: {len(syms)} names (today's - survivorship declared)")
    px = yf.download(syms + ["SPY"], start="2023-12-01", end="2026-08-08",
                     progress=False, auto_adjust=True, group_by="ticker", threads=True)
    spy = px["SPY"].dropna().Close
    W = [("W1", "2024-08-01", "2025-02-28"), ("W2", "2025-03-01", "2025-09-30"),
         ("W3", "2025-10-01", "2026-08-07")]
    events, t4 = [], []
    for s in syms:
        try: h = px[s].dropna()
        except Exception: continue
        if len(h) < 260: continue
        atr14, atr22, adx, pdi, mdi, sma200, dvol = indicators(h)
        for i in ce_flips(h, atr22):
            if i < 210 or i + 21 >= len(h): continue
            d0 = h.index[i]
            if d0 < pd.Timestamp("2024-08-01"): continue
            a, dm = float(adx.iloc[i]), float(pdi.iloc[i] - mdi.iloc[i])
            v2 = (float(h.Close.iloc[i]) / float(sma200.iloc[i]) - 1) * 100 if not np.isnan(sma200.iloc[i]) else -99
            dv = float(dvol.iloc[i]) / 1e6 if not np.isnan(dvol.iloc[i]) else 0
            if dv < 20: continue                      # hard liquidity floor (standing rule)
            if np.isnan(a) or np.isnan(dm): continue
            score = ws_traits(a, dm, v2, dv)
            c0 = float(h.Close.iloc[i])
            si = spy.index.searchsorted(d0)
            if si + 21 >= len(spy): continue
            f10 = (float(h.Close.iloc[i+10])/c0 - 1)*100 - (float(spy.iloc[si+10])/float(spy.iloc[si]) - 1)*100
            f21 = (float(h.Close.iloc[i+21])/c0 - 1)*100 - (float(spy.iloc[si+21])/float(spy.iloc[si]) - 1)*100
            win = next(w for w, a_, b_ in W if a_ <= str(d0.date()) <= b_)
            events.append({"score": score, "f10": f10, "f21": f21, "win": win})
            # T4 stop-width on the same flip
            stopA = float(h.Low.iloc[max(0, i-10):i].min())
            stopB = stopA - float(atr14.iloc[i])
            fwd = h.iloc[i+1:i+22]
            for lab, stop in (("A_structure", stopA), ("B_wider_1ATR", stopB)):
                if stop >= c0: continue
                shares = 5000 / (c0 - stop)
                hit15 = stopped = False; exitpx = float(fwd.Close.iloc[-1])
                for j in range(len(fwd)):
                    if float(fwd.Low.iloc[j]) <= stop: stopped, exitpx = True, stop; break
                    if float(fwd.Close.iloc[j]) >= c0 * 1.15: hit15, exitpx = True, float(fwd.Close.iloc[j]); break
                t4.append({"lab": lab, "pnl": shares*(exitpx-c0), "hit15": hit15, "stopped": stopped})
    print(f"replay flips scored: {len(events)}\n")
    print("=== T2: WS-traits terciles, +21 excess vs SPY ===")
    for wname in ["W1", "W2", "W3", "ALL"]:
        ev = events if wname == "ALL" else [e for e in events if e["win"] == wname]
        if len(ev) < 30: print(f"{wname}: n={len(ev)} too thin"); continue
        lo_t = [e["f21"] for e in ev if e["score"] <= 1]
        mid = [e["f21"] for e in ev if 2 <= e["score"] <= 3]
        hi_t = [e["f21"] for e in ev if e["score"] >= 4]
        line = f"{wname}: n={len(ev)}  LOW(0-1) {st.mean(lo_t):+.2f}% (n={len(lo_t)})  MID(2-3) {st.mean(mid):+.2f}% (n={len(mid)})  HIGH(4+) {st.mean(hi_t):+.2f}% (n={len(hi_t)})"
        if wname == "ALL" and hi_t and lo_t:
            lo_ci, hi_ci = ci_diff(hi_t, lo_t)
            line += f"  | HIGH-LOW diff CI [{lo_ci:+.2f},{hi_ci:+.2f}]" + ("  *EXCLUDES 0*" if (lo_ci > 0 or hi_ci < 0) else "  (spans 0)")
        print(line)
    print("\n=== T4: stop width (same flips, $5k risk each) ===")
    for lab in ("A_structure", "B_wider_1ATR"):
        g = [x for x in t4 if x["lab"] == lab]
        print(f"{lab}: n={len(g)}  mean P&L ${st.mean([x['pnl'] for x in g]):+,.0f}  "
              f"reached +15% first: {100*sum(x['hit15'] for x in g)/len(g):.0f}%  "
              f"stopped: {100*sum(x['stopped'] for x in g)/len(g):.0f}%")
    json.dump(events, open(REPO/"research"/"winner-score-replay-events.json", "w"))
    return 0

if __name__ == "__main__":
    sys.exit(main())
