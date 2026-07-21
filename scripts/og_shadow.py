#!/usr/bin/env python3
"""SHADOW detector: Python port of the O.G Chandelier stack, graded vs live-chart reads.

GOVERNANCE (rule freeze through 2026-08-31): this is a SHADOW-LANE detector per the
7/20 policy — it has ZERO effect on live signals/plans/alerts. Its only output is a
grade report comparing its computed modes/flip-dates against the chart truth recorded
in watchlists/universe-results-<date>.json (all_names). Promotion to live requires the
shadow matching the chart over the trial window, decided by Omar after 8/31.

Port spec (mirrors the chart layout):
  - Chart is HEIKIN-ASHI -> all indicators computed on HA candles built from raw daily OHLC.
  - Chandelier Exit inputs 1/2 (ATR period 1, mult 2), everget-style with stop ratchet,
    extremes from HA high/low.
  - ZLSMA(50) on HA close.
  - "Magical OB/OS" proxied by CCI(20) on HA typical price (internals unknown — the grade
    report tracks correlation so we learn how good the proxy is).

Usage: python scripts/og_shadow.py [YYYY-MM-DD]   (date of the universe-results file)
Writes: watchlists/shadow-og-grade-<date>.md and appends a "shadow" entry to the results JSON.
"""
import json
import os
import re
import sys

import numpy as np
import pandas as pd
import yfinance as yf

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = sys.argv[1] if len(sys.argv) > 1 else None
if not DATE:
    cands = sorted(f for f in os.listdir(os.path.join(REPO, "watchlists"))
                   if re.match(r"universe-results-\d{4}-\d{2}-\d{2}\.json$", f))
    DATE = cands[-1][17:-5]

RES_PATH = os.path.join(REPO, "watchlists", f"universe-results-{DATE}.json")
res = json.load(open(RES_PATH))
truth = {r["sym"]: r for r in res.get("all_names", []) if r.get("mode") in ("long", "sell")}
if not truth:
    sys.exit("no all_names chart truth in the results JSON — nothing to grade against")

CE_LEN, CE_MULT, ZL_LEN, CCI_LEN, FRESH_BARS = 1, 2.0, 50, 20, 5


def heikin_ashi(df):
    ha = pd.DataFrame(index=df.index)
    ha["close"] = (df["Open"] + df["High"] + df["Low"] + df["Close"]) / 4
    op = np.empty(len(df))
    op[0] = (df["Open"].iloc[0] + df["Close"].iloc[0]) / 2
    hc = ha["close"].to_numpy()
    for i in range(1, len(df)):
        op[i] = (op[i - 1] + hc[i - 1]) / 2
    ha["open"] = op
    ha["high"] = np.maximum.reduce([df["High"].to_numpy(), op, hc])
    ha["low"] = np.minimum.reduce([df["Low"].to_numpy(), op, hc])
    return ha


def atr(ha, length):
    prev_close = ha["close"].shift(1)
    tr = pd.concat([ha["high"] - ha["low"],
                    (ha["high"] - prev_close).abs(),
                    (ha["low"] - prev_close).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / length, adjust=False).mean()


def chandelier(ha):
    """Everget CE with ratchet; returns (direction array, last flip index)."""
    a = CE_MULT * atr(ha, CE_LEN)
    hi = ha["high"].rolling(CE_LEN).max()
    lo = ha["low"].rolling(CE_LEN).min()
    long_stop_base = (hi - a).to_numpy()
    short_stop_base = (lo + a).to_numpy()
    c = ha["close"].to_numpy()
    n = len(c)
    ls, ss = long_stop_base.copy(), short_stop_base.copy()
    dirn = np.ones(n, dtype=int)
    for i in range(1, n):
        ls[i] = max(long_stop_base[i], ls[i - 1]) if c[i - 1] > ls[i - 1] else long_stop_base[i]
        ss[i] = min(short_stop_base[i], ss[i - 1]) if c[i - 1] < ss[i - 1] else short_stop_base[i]
        if c[i] > ss[i - 1]:
            dirn[i] = 1
        elif c[i] < ls[i - 1]:
            dirn[i] = -1
        else:
            dirn[i] = dirn[i - 1]
    flips = np.where(dirn[1:] != dirn[:-1])[0] + 1
    last_flip = int(flips[-1]) if len(flips) else 0
    return dirn, last_flip


def linreg_last(s, length):
    """Rolling endpoint linear regression (Pine linreg(src, len, 0))."""
    x = np.arange(length)
    xm = x.mean()
    denom = ((x - xm) ** 2).sum()

    def endpoint(w):
        b = ((x - xm) * (w - w.mean())).sum() / denom
        a0 = w.mean() - b * xm
        return a0 + b * (length - 1)
    return s.rolling(length).apply(endpoint, raw=True)


def grade_symbol(sym, df):
    if len(df) < ZL_LEN + 10:
        return None
    ha = heikin_ashi(df)
    dirn, last_flip = chandelier(ha)
    mode = "long" if dirn[-1] == 1 else "sell"
    bars_since_flip = len(dirn) - 1 - last_flip
    fresh = mode == "long" and bars_since_flip <= FRESH_BARS
    lsma = linreg_last(ha["close"], ZL_LEN)
    zl = (2 * lsma - linreg_last(lsma, ZL_LEN)).iloc[-1]
    tp = (ha["high"] + ha["low"] + ha["close"]) / 3
    sma = tp.rolling(CCI_LEN).mean()
    mad = tp.rolling(CCI_LEN).apply(lambda w: np.abs(w - w.mean()).mean(), raw=True)
    cci = float(((tp - sma) / (0.015 * mad)).iloc[-1])
    return {"mode": mode, "fresh": fresh, "bars_since_flip": int(bars_since_flip),
            "zlsma": round(float(zl), 2), "cci": round(cci, 1),
            "last": round(float(ha["close"].iloc[-1]), 2)}


syms = sorted(truth)
print(f"shadow-grading {len(syms)} symbols vs chart truth {DATE}...")
data = yf.download(syms, period="9mo", interval="1d", group_by="ticker",
                   auto_adjust=False, threads=True, progress=False)

rows, errs = [], []
for sym in syms:
    try:
        df = data[sym].dropna(subset=["Close"]) if sym in data.columns.get_level_values(0) else None
        if df is None or df.empty:
            errs.append(sym)
            continue
        g = grade_symbol(sym, df)
        if g is None:
            errs.append(sym)
            continue
        t = truth[sym]
        g["sym"] = sym
        g["chart_mode"] = t["mode"]
        g["chart_fresh"] = bool(t.get("fresh"))
        g["chart_magical"] = t.get("magical")
        g["mode_match"] = g["mode"] == t["mode"]
        g["fresh_match"] = g["fresh"] == bool(t.get("fresh"))
        rows.append(g)
    except Exception as e:
        errs.append(f"{sym}:{type(e).__name__}")

n = len(rows)
mode_ok = sum(r["mode_match"] for r in rows)
fresh_ok = sum(r["fresh_match"] for r in rows)
both = sum(r["mode_match"] and r["fresh_match"] for r in rows)
cci_pairs = [(r["cci"], r["chart_magical"]) for r in rows if r["chart_magical"] is not None]
cci_corr = float(np.corrcoef([p[0] for p in cci_pairs], [p[1] for p in cci_pairs])[0, 1]) if len(cci_pairs) > 10 else None

mism = [r for r in rows if not r["mode_match"]]
fresh_mism = [r for r in rows if r["mode_match"] and not r["fresh_match"]]

out_md = os.path.join(REPO, "watchlists", f"shadow-og-grade-{DATE}.md")
with open(out_md, "w", encoding="utf-8") as f:
    f.write(f"# SHADOW O.G port grade — vs chart truth {DATE}\n\n")
    f.write("Shadow-lane detector (rule freeze compliant): zero live effect. ")
    f.write("Promotion requires sustained match, Omar's call after 8/31.\n\n")
    f.write(f"- Graded: {n} symbols ({len(errs)} data failures)\n")
    f.write(f"- **Mode match: {mode_ok}/{n} = {mode_ok / n * 100:.1f}%**\n")
    f.write(f"- **Freshness match (within mode-matched): {fresh_ok}/{n} = {fresh_ok / n * 100:.1f}%**\n")
    f.write(f"- Both match: {both}/{n} = {both / n * 100:.1f}%\n")
    f.write(f"- CCI(20)-proxy vs chart Magical correlation: {cci_corr:.3f}\n\n" if cci_corr is not None else "\n")
    f.write(f"## Mode mismatches ({len(mism)})\n\n")
    f.write("| Sym | shadow | chart | bars since shadow flip | shadow CCI | chart Magical |\n|---|---|---|---|---|---|\n")
    for r in sorted(mism, key=lambda x: x["sym"]):
        f.write(f"| {r['sym']} | {r['mode']} | {r['chart_mode']} | {r['bars_since_flip']} | {r['cci']} | {r['chart_magical']} |\n")
    f.write(f"\n## Freshness mismatches, mode agreed ({len(fresh_mism)})\n\n")
    f.write("| Sym | shadow fresh | chart fresh | shadow bars-since-flip |\n|---|---|---|---|\n")
    for r in sorted(fresh_mism, key=lambda x: x["sym"]):
        f.write(f"| {r['sym']} | {r['fresh']} | {r['chart_fresh']} | {r['bars_since_flip']} |\n")
    f.write("\nData failures: " + ", ".join(map(str, errs)) + "\n")

res.setdefault("shadow", []).append({
    "name": "og-python-port-v1", "date_graded": DATE,
    "mode_match_pct": round(mode_ok / n * 100, 1),
    "fresh_match_pct": round(fresh_ok / n * 100, 1),
    "cci_proxy_corr": round(cci_corr, 3) if cci_corr is not None else None,
    "graded": n, "grade_file": os.path.basename(out_md),
})
json.dump(res, open(RES_PATH, "w"), indent=1)
print(f"MODE match {mode_ok}/{n} ({mode_ok / n * 100:.1f}%) · FRESH match {fresh_ok}/{n} ({fresh_ok / n * 100:.1f}%)"
      + (f" · CCI-proxy corr {cci_corr:.3f}" if cci_corr is not None else ""))
print("report:", out_md)
