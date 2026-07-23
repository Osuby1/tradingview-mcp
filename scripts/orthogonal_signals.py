"""Orthogonal (non-price) signal layer - earnings + fundamentals + analyst.

Omar, 2026-07-22: add orthogonal, non-price data. The whole technical system is
ONE data family (price); every "component" is collinear. Real forecasting power
can only come from information that is NOT price. This builds that layer.

IMPORTANT HONESTY: this is a CURRENT signal, forward-validated via the outcome
tracker - NOT a clean historical backtest. yfinance fundamentals are not
point-in-time (they show today's restated numbers on old dates), so backtesting
them invites look-ahead bias. So we build the signal now, prove it is actually
ORTHOGONAL to price momentum (low correlation), add it to enrichment, and let the
outcome tracker grade it going forward. Do not claim a backtested edge for it.

Per name, via yfinance .info + .earnings_dates:
  * earnings surprise (latest reported EPS vs estimate) + beat-rate last 4 quarters
    -> the PEAD signal, the most robust non-price anomaly
  * revenue growth YoY and earnings growth -> fundamental momentum
  * analyst recommendation mean + target upside -> revision/positioning proxy

Combined 0-100 orthogonal score. Then correlate with 12-1 price momentum to PROVE
it carries different information (if it correlated highly, it would be redundant).

Usage: python scripts/orthogonal_signals.py [SYM ...]   (default: followed set)
"""
import json
import statistics as st
import sys
import time

import yfinance as yf

FOLLOWED = [
    "AAPL","MSFT","NVDA","AMD","MU","AMAT","QCOM","INTC","ORCL","ARM","AMZN","META","GOOG","NFLX",
    "UBER","PLTR","SNOW","PANW","CRWD","JPM","BAC","GS","C","BX","SPGI","PGR","COIN","DELL","CAT","DE",
    "GE","HON","UNP","ETN","PH","URI","TDY","XOM","CVX","COP","OXY","VLO","DVN","FCX","NEM","MP","HD",
    "LOW","COST","MCD","NKE","KO","PEP","PM","TJX","DIS","JNJ","LLY","ABBV","PFE","CTRE","TXNM","VZ",
]


def _num(x):
    try:
        v = float(x)
        return v if v == v else None
    except (TypeError, ValueError):
        return None


def _clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def signal_for(sym):
    t = yf.Ticker(sym)
    info = {}
    try:
        info = t.info or {}
    except Exception:
        pass

    rev_g = _num(info.get("revenueGrowth"))         # YoY, fraction
    eps_g = _num(info.get("earningsGrowth"))
    q_eps_g = _num(info.get("earningsQuarterlyGrowth"))
    rec = _num(info.get("recommendationMean"))       # 1=strong buy .. 5=sell
    price = _num(info.get("currentPrice")) or _num(info.get("regularMarketPrice"))
    tgt = _num(info.get("targetMeanPrice"))
    upside = (tgt/price - 1) if (tgt and price) else None

    # earnings surprise: latest reported vs estimate + beat rate
    surprise, beat_rate = None, None
    try:
        ed = t.get_earnings_dates(limit=8)
        if ed is not None and len(ed):
            rep = ed.dropna(subset=["Reported EPS", "EPS Estimate"])
            if len(rep):
                s = (rep["Reported EPS"] - rep["EPS Estimate"]) / rep["EPS Estimate"].abs()
                surprise = float(s.iloc[0]) if len(s) else None      # most recent
                beat_rate = float((rep["Reported EPS"] > rep["EPS Estimate"]).mean())
    except Exception:
        pass

    # 0-1 sub-signals
    subs = {}
    subs["surprise"] = _clamp((surprise + 0.05) / 0.20) if surprise is not None else None
    subs["beat_rate"] = beat_rate
    subs["rev_growth"] = _clamp((rev_g + 0.0) / 0.30) if rev_g is not None else None
    subs["eps_growth"] = _clamp((q_eps_g + 0.0) / 0.40) if q_eps_g is not None else None
    subs["analyst"] = _clamp((3.0 - rec) / 2.0) if rec is not None else None   # 1->1.0, 3->0
    subs["upside"] = _clamp((upside + 0.0) / 0.30) if upside is not None else None

    have = {k: v for k, v in subs.items() if v is not None}
    score = round(100 * (sum(have.values()) / len(have)), 1) if have else None
    return {"sym": sym, "score": score, "n_signals": len(have),
            "surprise": surprise, "beat_rate": beat_rate, "rev_growth": rev_g,
            "eps_growth": q_eps_g, "rec_mean": rec, "upside": upside, "subs": subs}


def momentum_12_1(sym):
    try:
        d = yf.download(sym, period="14mo", interval="1mo", auto_adjust=True,
                        progress=False, threads=False)["Close"].dropna()
        if len(d) >= 13:
            return float(d.iloc[-2] / d.iloc[-13] - 1)
    except Exception:
        pass
    return None


def spearman(xs, ys):
    pairs = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None and x == x and y == y]
    n = len(pairs)
    if n < 8:
        return None
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0]*len(v); i = 0
        while i < len(v):
            j = i
            while j+1 < len(v) and v[order[j+1]] == v[order[i]]:
                j += 1
            for k in range(i, j+1):
                r[order[k]] = (i+j)/2.0+1
            i = j+1
        return r
    a, b = ranks([p[0] for p in pairs]), ranks([p[1] for p in pairs])
    ma, mb = sum(a)/n, sum(b)/n
    num = sum((x-ma)*(y-mb) for x, y in zip(a, b))
    da = sum((x-ma)**2 for x in a)**0.5; db = sum((y-mb)**2 for y in b)**0.5
    return num/(da*db) if da and db else None


def main():
    syms = [s.upper() for s in sys.argv[1:]] or FOLLOWED
    print(f"pulling orthogonal signals for {len(syms)} names...")
    rows, moms = [], {}
    for i, s in enumerate(syms):
        r = signal_for(s)
        rows.append(r)
        moms[s] = momentum_12_1(s)
        if (i+1) % 15 == 0:
            print(f"  {i+1}/{len(syms)}")
        time.sleep(0.15)

    scored = [r for r in rows if r["score"] is not None]
    # orthogonality check: correlation of the fundamental score vs price momentum
    ortho = spearman([r["score"] for r in scored],
                     [moms.get(r["sym"]) for r in scored])

    scored.sort(key=lambda r: -r["score"])
    out = []
    out.append("# Orthogonal (non-price) signal layer")
    out.append("")
    out.append(f"{len(scored)}/{len(syms)} names scored. Earnings surprise + beat rate + "
               f"revenue/EPS growth + analyst rating + target upside, blended 0-100.")
    out.append("")
    out.append("## Is it actually orthogonal to price?")
    if ortho is not None:
        out.append(f"- Spearman(fundamental score, 12-1 price momentum) = **{ortho:+.3f}**")
        if abs(ortho) < 0.3:
            out.append("  - LOW correlation = it carries DIFFERENT information than the "
                       "technicals. That is the whole point - orthogonal data can add "
                       "forecasting power the price signals cannot.")
        else:
            out.append("  - Moderate correlation - partly redundant with momentum; less "
                       "additive than hoped.")
    out.append("")
    out.append("## Top 15 by fundamental score")
    out.append("| Sym | Score | Surprise | Beat | RevGrow | Analyst | Upside |")
    out.append("|---|---|---|---|---|---|---|")
    for r in scored[:15]:
        def pc(x): return f"{x*100:+.0f}%" if x is not None else "-"
        out.append(f"| {r['sym']} | {r['score']} | {pc(r['surprise'])} "
                   f"| {pc(r['beat_rate'])} | {pc(r['rev_growth'])} "
                   f"| {r['rec_mean'] if r['rec_mean'] else '-'} | {pc(r['upside'])} |")
    out.append("")
    out.append("## Honest status")
    out.append("- This is a CURRENT signal, NOT backtested. yfinance fundamentals are not "
               "point-in-time, so a historical test would leak look-ahead. It is added to "
               "enrichment and will be FORWARD-graded by the outcome tracker.")
    out.append("- The value proposition is orthogonality: if it forecasts even weakly AND "
               "is uncorrelated with the price signals, the COMBINATION beats either alone. "
               "That is the only honest path to 'hugely better' - more independent signals, "
               "not re-weighted price.")

    with open("research/orthogonal-signals.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    with open("research/orthogonal-signals.json", "w", encoding="utf-8") as fh:
        json.dump({"orthogonality_vs_momentum": ortho,
                   "rows": scored}, fh, indent=1)
    print("\n".join(out))
    print("\nwrote research/orthogonal-signals.md + .json")


if __name__ == "__main__":
    main()
