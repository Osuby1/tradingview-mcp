"""Cross-sectional momentum backtest - the falsifiable test.

Omar, 2026-07-22: build the momentum backtest. This is the one genuinely
predictive factor our price data can express, tested the honest way: walk-forward,
long the strongest-momentum names, measured against just holding SPY.

Construction (standard academic 12-1 momentum, no cleverness):
  * monthly rebalance
  * signal at month t = cumulative return from t-12 months to t-1 month (skip the
    most recent month - it mean-reverts and using it is a known mistake)
  * rank all names cross-sectionally, form deciles/quintiles
  * hold the top slice for the next 1 month, then rebalance
  * benchmark = SPY over the identical months

Honest metrics reported:
  * IC = average monthly Spearman(momentum rank, NEXT-month return) - directly
    comparable to the 0.06 we measured for the technical BUY SCORE
  * top-decile vs bottom-decile monthly spread
  * top-quintile cumulative vs SPY, hit rate of monthly excess, and a crude Sharpe

Caveats baked into the output:
  * SURVIVORSHIP: uses a fixed list of names that exist TODAY. Delisted losers are
    absent, which flatters momentum. A clean test needs point-in-time constituents.
  * No costs, no slippage, monthly close-to-close.
  * One ~3-year window. Momentum is regime-dependent and has violent crashes
    (2009, 2020-style) not necessarily in this sample.

Usage: python scripts/momentum_backtest.py
"""
import json
import statistics as st

import yfinance as yf
import pandas as pd

# ~130 liquid names across sectors. Fixed = survivorship; disclosed in output.
UNIVERSE = [
    "AAPL","MSFT","NVDA","AMD","MU","AMAT","QCOM","INTC","ORCL","ARM","AVGO","TXN","ADI","LRCX","KLAC",
    "AMZN","META","GOOG","NFLX","UBER","PLTR","SNOW","PANW","CRWD","NET","DDOG","SHOP","ABNB","SE","MELI",
    "JPM","BAC","GS","C","WFC","MS","BX","SPGI","PGR","AXP","BLK","SCHW","KRE",
    "CAT","DE","GE","HON","UNP","ETN","PH","URI","TDY","EMR","ITW","RTX","LMT","BA",
    "XOM","CVX","COP","OXY","VLO","MPC","PSX","SLB","EOG","DVN","WMB","KMI","ET",
    "FCX","NEM","GDX","MP","NUE","STLD","LIN","SHW","APD",
    "HD","LOW","COST","MCD","NKE","KO","PEP","PM","TJX","DIS","SBUX","CMG","BKNG","MAR","RCL",
    "JNJ","LLY","ABBV","MRK","PFE","UNH","TMO","ABT","ISRG","VRTX","REGN","AMGN","BMY","GILD","RMD",
    "V","MA","PYPL","COIN","HOOD","SOFI",
    "NEE","DUK","SO","VST","CEG","D",
    "WMT","PG","CL","MDLZ","MO","T","VZ","TMUS",
    "TSLA","GM","F","CVNA","DAL","UAL",
]
LOOKBACK, SKIP = 12, 1
TOP_FRAC = 0.20


def spearman(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x == x and y == y]
    n = len(pairs)
    if n < 5:
        return None
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0]*len(v); i = 0
        while i < len(v):
            j = i
            while j+1 < len(v) and v[order[j+1]] == v[order[i]]:
                j += 1
            for k in range(i, j+1):
                r[order[k]] = (i+j)/2.0 + 1
            i = j+1
        return r
    a, b = ranks([p[0] for p in pairs]), ranks([p[1] for p in pairs])
    ma, mb = sum(a)/n, sum(b)/n
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    da = sum((x-ma)**2 for x in a)**0.5
    db = sum((y-mb)**2 for y in b)**0.5
    return num/(da*db) if da and db else None


def main():
    syms = sorted(set(UNIVERSE + ["SPY"]))
    print(f"downloading {len(syms)} names, 3y monthly...")
    raw = yf.download(syms, period="3y", interval="1mo", auto_adjust=True,
                      progress=False, group_by="ticker", threads=True)

    # monthly close per symbol
    closes = {}
    for s in syms:
        try:
            d = raw[s]["Close"].dropna() if isinstance(raw.columns, pd.MultiIndex) else raw["Close"].dropna()
        except Exception:
            continue
        if len(d) >= LOOKBACK + 3:
            closes[s] = d
    spy = closes.pop("SPY", None)
    if spy is None:
        raise SystemExit("no SPY")
    print(f"usable names: {len(closes)}")

    months = list(spy.index)
    ics, top_rets, bot_rets, spy_rets, excess = [], [], [], [], []
    equity_top, equity_spy = 1.0, 1.0
    curve = []

    # walk forward: at each month i (>= LOOKBACK), signal uses [i-12, i-1], hold i..i+1
    for i in range(LOOKBACK, len(months) - 1):
        t = months[i]
        mom, fwd = {}, {}
        for s, ser in closes.items():
            if t not in ser.index:
                continue
            pos = ser.index.get_loc(t)
            if pos < LOOKBACK or pos + 1 >= len(ser):
                continue
            p_now, p_skip, p_look = ser.iloc[pos], ser.iloc[pos-SKIP], ser.iloc[pos-LOOKBACK]
            if p_look and p_skip:
                mom[s] = p_skip / p_look - 1                 # 12-1 momentum
                fwd[s] = ser.iloc[pos+1] / p_now - 1          # next-month fwd return
        common = [s for s in mom if s in fwd]
        if len(common) < 20:
            continue
        ic = spearman([mom[s] for s in common], [fwd[s] for s in common])
        if ic is not None:
            ics.append(ic)
        ranked = sorted(common, key=lambda s: mom[s], reverse=True)
        k = max(1, int(len(ranked)*TOP_FRAC))
        top = ranked[:k]; bot = ranked[-k:]
        tr = st.mean(fwd[s] for s in top)
        br = st.mean(fwd[s] for s in bot)
        sr = (spy.iloc[i+1]/spy.iloc[i] - 1) if (i+1) < len(spy) else None
        top_rets.append(tr); bot_rets.append(br)
        if sr is not None:
            spy_rets.append(sr); excess.append(tr - sr)
            equity_top *= (1+tr); equity_spy *= (1+sr)
            curve.append({"month": str(t.date()), "top": round(tr*100, 2),
                          "spy": round(sr*100, 2), "equity_top": round(equity_top, 3),
                          "equity_spy": round(equity_spy, 3)})

    n = len(top_rets)
    def ann(rets):
        m = st.mean(rets); s = st.pstdev(rets) or 1e-9
        return m*12*100, (m/s)*(12**0.5)
    top_ann, top_sh = ann(top_rets)
    spy_ann, spy_sh = ann(spy_rets)
    hit = 100*sum(1 for x in excess if x > 0)/len(excess)

    out = []
    out.append("# Cross-sectional momentum backtest - hard facts")
    out.append("")
    out.append(f"{len(closes)} names, {n} monthly rebalances, 12-1 momentum, long top "
               f"{int(TOP_FRAC*100)}%, monthly hold. Benchmark SPY.")
    out.append("")
    out.append("## The number that matters: does momentum forecast?")
    out.append(f"- **Average monthly IC (Spearman momentum vs next-month return): "
               f"{st.mean(ics):+.3f}** (n={len(ics)} months)")
    out.append(f"  - Compare: the technical BUY SCORE managed +0.065 at 21d. IC "
               f">= |0.03| is a usable cross-sectional signal.")
    out.append(f"  - Months with positive IC: {100*sum(1 for x in ics if x>0)/len(ics):.0f}%")
    out.append("")
    out.append("## Top vs bottom, and vs SPY")
    out.append(f"- Top {int(TOP_FRAC*100)}% mean monthly: {st.mean(top_rets)*100:+.2f}%")
    out.append(f"- Bottom {int(TOP_FRAC*100)}% mean monthly: {st.mean(bot_rets)*100:+.2f}%")
    out.append(f"- **Top-minus-bottom spread: {(st.mean(top_rets)-st.mean(bot_rets))*100:+.2f}%/mo**")
    out.append(f"- SPY mean monthly: {st.mean(spy_rets)*100:+.2f}%")
    out.append(f"- **Top-minus-SPY (monthly excess): {st.mean(excess)*100:+.2f}%**, "
               f"hit rate {hit:.0f}%")
    out.append("")
    out.append("## Compounded over the window")
    out.append(f"- Momentum top {int(TOP_FRAC*100)}%: {(equity_top-1)*100:+.1f}%  "
               f"(annualized ~{top_ann:.0f}%, Sharpe ~{top_sh:.2f})")
    out.append(f"- SPY: {(equity_spy-1)*100:+.1f}%  (annualized ~{spy_ann:.0f}%, "
               f"Sharpe ~{spy_sh:.2f})")
    out.append("")
    out.append("## Verdict")
    ic_m = st.mean(ics)
    beat = st.mean(excess) > 0 and equity_top > equity_spy
    if ic_m >= 0.03 and beat:
        out.append(f"Momentum forecasts here: IC {ic_m:+.3f} (vs the technical score's "
                   f"+0.065 at a DIFFERENT horizon), it beat SPY by {st.mean(excess)*100:+.2f}%/mo, "
                   f"and compounded ahead. This is a REAL, usable selection signal - far "
                   f"more than the technical score gave. Adopt it as the SELECTION layer.")
    elif ic_m >= 0.02:
        out.append(f"Momentum shows a weak-but-real edge (IC {ic_m:+.3f}). Better than the "
                   f"technical score but modest; worth combining with orthogonal data, not "
                   f"relied on alone.")
    else:
        out.append(f"Momentum did NOT forecast in this window (IC {ic_m:+.3f}). Either the "
                   f"sample is a momentum-hostile stretch or the universe is too small. Do "
                   f"not adopt on this alone.")
    out.append("")
    out.append("## Caveats (these INFLATE the result)")
    out.append("- SURVIVORSHIP: fixed list of names that exist today; delisted losers "
               "absent. A clean test needs point-in-time constituents.")
    out.append("- No costs/slippage; monthly turnover of ~40-60% of the book is real drag.")
    out.append("- One ~3-year window; momentum has rare violent crashes not necessarily here.")

    with open("research/momentum-backtest.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    with open("research/momentum-backtest.json", "w", encoding="utf-8") as fh:
        json.dump({"names": len(closes), "months": n, "ic_mean": st.mean(ics),
                   "top_excess_monthly": st.mean(excess), "hit_rate": hit,
                   "equity_top": equity_top, "equity_spy": equity_spy,
                   "curve": curve}, fh, indent=1)
    print("\n".join(out))
    print("\nwrote research/momentum-backtest.md + .json")


if __name__ == "__main__":
    main()
