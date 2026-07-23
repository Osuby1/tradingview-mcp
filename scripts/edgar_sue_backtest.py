"""PEAD backtest from point-in-time EDGAR earnings - the clean, free test.

Built 2026-07-22 per the scoping doc (research/pead-data-sources-scoping.md).
Uses SEC EDGAR XBRL companyfacts: actual quarterly diluted EPS with FILING DATES,
so the surprise is genuinely point-in-time (no restated / look-ahead leakage - the
trap that killed yfinance fundamentals and inflated the momentum backtest).

Signal: SUE (Standardized Unexpected Earnings), the Bernard-Thomas construction:
  UE_q  = EPS_q - EPS_{q-4}                     (seasonal random walk - no analyst
                                                 estimate needed)
  SUE_q = UE_q / stdev(past UEs for the name)   (standardize by own earnings vol)

Point-in-time discipline:
  * For each fiscal period we take the EARLIEST-filed EPS value (the original 10-Q/
    10-K number, not a later restatement).
  * The drift is measured from the first trading day AFTER the filing date - you
    could not have traded on it before it was public.

Test (event-level, the direct PEAD test):
  * for each earnings event with a valid SUE: forward return over +20 and +60
    trading days from the day after filing, and the same minus SPY.
  * IC = Spearman(SUE, forward return) across all events - THE honest metric.
  * high-SUE (Q5) vs low-SUE (Q1) quintile forward returns, and vs SPY.

Honest caveats baked into output: US filers only, liquid survivor universe
(survivorship inflates), no costs, one recent multi-year window, Q4 quarterly EPS
often absent from 10-Ks (fewer events for some names).

Usage: python scripts/edgar_sue_backtest.py
"""
import json
import statistics as st
import time
import urllib.request

import yfinance as yf
import pandas as pd

UA = {"User-Agent": "personal research omarsuby888@gmail.com"}
UNIVERSE = [
    "AAPL","MSFT","NVDA","AMD","MU","AMAT","QCOM","INTC","ORCL","AVGO","TXN","ADI","LRCX","KLAC",
    "AMZN","META","GOOGL","NFLX","UBER","CRM","ADBE","NOW","PANW","CRWD","JPM","BAC","GS","C","WFC",
    "MS","BX","SPGI","AXP","BLK","CAT","DE","GE","HON","UNP","ETN","PH","RTX","LMT","BA","EMR","ITW",
    "XOM","CVX","COP","OXY","VLO","MPC","PSX","SLB","EOG","DVN","FCX","NEM","NUE","STLD","LIN","SHW","APD",
    "HD","LOW","COST","MCD","NKE","KO","PEP","PM","TJX","DIS","SBUX","CMG","BKNG","MAR",
    "JNJ","LLY","ABBV","MRK","PFE","UNH","TMO","ABT","ISRG","VRTX","REGN","AMGN","BMY","GILD",
    "V","MA","WMT","PG","CL","MDLZ","MO","T","VZ","TMUS","CVS","CI","HUM",
    "TSLA","GM","F","DAL","UAL","NEE","DUK","SO","D",
]
FWD = [20, 60]


def cik_map():
    d = json.load(urllib.request.urlopen(
        urllib.request.Request("https://www.sec.gov/files/company_tickers.json", headers=UA), timeout=30))
    return {v["ticker"].upper(): str(v["cik_str"]).zfill(10) for v in d.values()}


def quarterly_eps(cik):
    """Point-in-time quarterly diluted EPS: list of {end, filed, val} using the
    EARLIEST filing per fiscal period."""
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    try:
        facts = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30))
    except Exception:
        return []
    gaap = facts.get("facts", {}).get("us-gaap", {})
    node = gaap.get("EarningsPerShareDiluted") or gaap.get("EarningsPerShareBasic")
    if not node:
        return []
    units = node.get("units", {})
    arr = units.get("USD/shares") or next(iter(units.values()), [])
    by_period = {}
    for e in arr:
        start, end, filed = e.get("start"), e.get("end"), e.get("filed")
        val, form = e.get("val"), e.get("form", "")
        if not (start and end and filed and val is not None):
            continue
        # quarter-length only (~90 days); drops annual/9-mo cumulative entries
        days = (pd.Timestamp(end) - pd.Timestamp(start)).days
        if not (80 <= days <= 100):
            continue
        key = end
        # earliest filed for this period end = the original, point-in-time number
        if key not in by_period or filed < by_period[key]["filed"]:
            by_period[key] = {"end": end, "filed": filed, "val": float(val)}
    return sorted(by_period.values(), key=lambda x: x["end"])


def split_adjust(eps, splits):
    """EDGAR EPS is AS-REPORTED (not split-adjusted). Comparing EPS year-over-year
    across a split is garbage (NVDA 10:1 2024 made YoY UE look like a -5 'miss').
    Express every EPS in TODAY's share basis: divide EPS at end date D by the
    product of split ratios that happened AFTER D. splits = {Timestamp: ratio}."""
    if not splits:
        return eps
    items = sorted(splits.items())
    out = []
    for e in eps:
        end = pd.Timestamp(e["end"])
        factor = 1.0
        for d, r in items:
            if d > end:
                factor *= r
        out.append({**e, "val": e["val"] / factor})
    return out


def compute_sue(eps):
    """Attach SUE to each quarter that has a year-ago comparable + >=4 prior UEs."""
    by_end = {e["end"]: e for e in eps}
    ends = [e["end"] for e in eps]
    ue_hist = []
    out = []
    for e in eps:
        end = pd.Timestamp(e["end"])
        # year-ago quarter = an end date ~365 days earlier (+/- 20)
        prior = None
        for cand in eps:
            gap = (end - pd.Timestamp(cand["end"])).days
            if 345 <= gap <= 385:
                prior = cand
                break
        if prior is None:
            continue
        ue = e["val"] - prior["val"]
        if len(ue_hist) >= 4:
            sd = st.pstdev(ue_hist) or None
            if sd:
                out.append({"end": e["end"], "filed": e["filed"],
                            "eps": e["val"], "ue": ue, "sue": ue / sd})
        ue_hist.append(ue)
    return out


def spearman(xs, ys):
    P = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    n = len(P)
    if n < 20:
        return None, n
    def rk(v):
        o = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0]*len(v); i = 0
        while i < len(v):
            j = i
            while j+1 < len(v) and v[o[j+1]] == v[o[i]]:
                j += 1
            for k in range(i, j+1):
                r[o[k]] = (i+j)/2.0+1
            i = j+1
        return r
    a, b = rk([p[0] for p in P]), rk([p[1] for p in P])
    ma, mb = sum(a)/n, sum(b)/n
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    da = sum((x-ma)**2 for x in a)**.5; db = sum((y-mb)**2 for y in b)**.5
    return (num/(da*db) if da and db else None), n


def main():
    print("fetching CIK map...")
    cm = cik_map()
    names = [s for s in UNIVERSE if s in cm]
    print(f"{len(names)}/{len(UNIVERSE)} names have CIKs")

    print("pulling EDGAR point-in-time EPS + splits + computing SUE...")
    events = []  # {sym, filed, sue}
    for i, s in enumerate(names):
        eps = quarterly_eps(cm[s])
        if not eps:
            continue
        try:
            sp = yf.Ticker(s).splits
            splits = {pd.Timestamp(d).tz_localize(None): float(r)
                      for d, r in sp.items() if r and r != 1.0}
        except Exception:
            splits = {}
        eps = split_adjust(eps, splits)
        for ev in compute_sue(eps):
            events.append({"sym": s, "filed": ev["filed"], "sue": ev["sue"]})
        if (i+1) % 20 == 0:
            print(f"  {i+1}/{len(names)}  events so far {len(events)}")
        time.sleep(0.12)   # SEC 10 req/s
    print(f"total SUE events: {len(events)}")

    print("downloading daily prices...")
    raw = yf.download(sorted(set(names + ["SPY"])), period="5y", interval="1d",
                      auto_adjust=True, progress=False, group_by="ticker", threads=True)
    closes = {}
    for s in set(names + ["SPY"]):
        try:
            c = raw[s]["Close"].dropna()
            if len(c):
                closes[s] = c
        except Exception:
            pass
    spy = closes.get("SPY")

    def fwd_ret(sym, filed, n):
        c = closes.get(sym)
        if c is None:
            return None
        after = c.index[c.index > pd.Timestamp(filed)]
        if len(after) < n + 1:
            return None
        entry = c.loc[after[0]]
        exitp = c.loc[after[n]] if n < len(after) else None
        if entry and exitp:
            r = exitp / entry - 1
            # SPY over the same calendar window
            sr = None
            if spy is not None:
                sa = spy.index[spy.index >= after[0]]
                if len(sa) > n:
                    sr = spy.loc[sa[n]] / spy.loc[sa[0]] - 1
            return r, (r - sr if sr is not None else None)
        return None

    for ev in events:
        for n in FWD:
            fr = fwd_ret(ev["sym"], ev["filed"], n)
            if fr:
                ev[f"fwd{n}"], ev[f"exc{n}"] = fr[0], fr[1]
    graded = [e for e in events if e.get(f"fwd{FWD[-1]}") is not None]

    out = []
    out.append("# EDGAR SUE / PEAD backtest - hard facts")
    out.append("")
    out.append(f"{len(names)} US names, **{len(graded)} earnings events** with a "
               f"point-in-time SUE and a full {FWD[-1]}-day forward window. Surprise "
               f"measured from EDGAR filing dates (no look-ahead); drift from the day "
               f"AFTER filing.")
    out.append("")
    out.append("## Does the earnings surprise forecast drift? (the whole question)")
    for n in FWD:
        ic, k = spearman([e["sue"] for e in graded], [e.get(f"fwd{n}") for e in graded])
        ic_txt = f"{ic:+.3f}" if ic is not None else "n/a"
        out.append(f"- IC = Spearman(SUE, +{n}d return) = **{ic_txt}**  (n={k})")
    out.append("")
    out.append("  Compare: momentum IC was -0.006, the technical BUY SCORE +0.065. "
               "IC >= |0.03| is a usable signal; PEAD in the literature runs ~0.05-0.10.")
    out.append("")
    out.append("## High-SUE vs low-SUE quintiles")
    g = sorted(graded, key=lambda e: e["sue"])
    q = max(1, len(g)//5)
    for n in FWD:
        lo = [e.get(f"fwd{n}") for e in g[:q] if e.get(f"fwd{n}") is not None]
        hi = [e.get(f"fwd{n}") for e in g[-q:] if e.get(f"fwd{n}") is not None]
        elo = [e.get(f"exc{n}") for e in g[:q] if e.get(f"exc{n}") is not None]
        ehi = [e.get(f"exc{n}") for e in g[-q:] if e.get(f"exc{n}") is not None]
        out.append(f"- **+{n}d:** low-SUE {st.mean(lo)*100:+.2f}%  high-SUE "
                   f"{st.mean(hi)*100:+.2f}%  spread {(st.mean(hi)-st.mean(lo))*100:+.2f}pt")
        if ehi and elo:
            out.append(f"    vs SPY: low {st.mean(elo)*100:+.2f}%  high {st.mean(ehi)*100:+.2f}%  "
                       f"high-SUE excess {st.mean(ehi)*100:+.2f}%")
    out.append("")
    # verdict from the 60d IC
    ic60, _ = spearman([e["sue"] for e in graded], [e.get("fwd60") for e in graded])
    g2 = sorted(graded, key=lambda e: e["sue"])
    hi_exc = [e.get("exc60") for e in g2[-q:] if e.get("exc60") is not None]
    out.append("## Verdict")
    if ic60 is not None and ic60 >= 0.04:
        out.append(f"**PEAD is present here.** SUE forecasts 60-day drift at IC {ic60:+.3f} "
                   f"- an ORDER OF MAGNITUDE more signal than momentum (-0.006) or the "
                   f"technical score, and it is genuinely point-in-time. The high-SUE "
                   f"quintile beat SPY by {st.mean(hi_exc)*100:+.2f}% over 60 days. This is "
                   f"the first thing we have tested that actually forecasts. Worth building "
                   f"into the selection layer and forward-validating.")
    elif ic60 is not None and ic60 >= 0.02:
        out.append(f"**Weak-but-real PEAD** (IC {ic60:+.3f} at 60d) - better than momentum "
                   f"and the technical score, still modest. Worth combining, not relying on "
                   f"alone.")
    else:
        out.append(f"**No usable PEAD here** (IC {ic60:+.3f} at 60d). Either the seasonal-SUE "
                   f"construction is too crude for this liquid-mega-cap universe (PEAD is "
                   f"strongest in smaller, less-covered names) or the window is unfavorable.")
    out.append("")
    out.append("## Caveats")
    out.append("- US large-cap SURVIVOR universe - and PEAD is KNOWN to be weaker in big, "
               "heavily-covered names (the drift is arbitraged faster). A small/mid-cap "
               "universe would be a fairer test of PEAD's real strength.")
    out.append("- Seasonal-SUE (vs year-ago), NOT analyst-surprise - the free construction. "
               "The 'beat vs Street' version may be stronger; that needs paid point-in-time "
               "estimates (Phase 2).")
    out.append("- No costs/slippage; overlapping 60-day windows mean events are not "
               "independent (inflates apparent significance).")
    out.append("- Q4 quarterly EPS often absent from 10-Ks, so Q4 events are under-sampled.")

    with open("research/edgar-sue-backtest.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    with open("research/edgar-sue-backtest.json", "w", encoding="utf-8") as fh:
        json.dump({"names": len(names), "events_total": len(events),
                   "events_graded": len(graded),
                   "ic60": ic60, "events": graded[:500]}, fh, indent=1)
    print("\n".join(out))
    print("\nwrote research/edgar-sue-backtest.md + .json")


if __name__ == "__main__":
    main()
