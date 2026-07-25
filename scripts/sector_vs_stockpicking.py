"""Does stock picking beat just buying the sector? Pre-registered 2026-07-25.

Read research/sector-vs-stockpicking-preregistration.md first. Sectors, baskets,
period, horizons and the conclusion for every outcome were committed to git
BEFORE this file existed, at Omar's instruction not to force-fit the result.

When the scan fires a gate-passing BUY on a stock, would you have done better
buying that stock's SECTOR ETF on the same day and holding it the same length of
time? Isolates SELECTION - not entries, not exits, not timing.

Pure hold, no exit rule: exits are already measured to destroy value, and leaving
them in would measure the exit rather than the selection.

Usage: python scripts/sector_vs_stockpicking.py
"""
import json
import os
import sys

import numpy as np
import pandas as pd
import yfinance as yf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_stack import evaluate, MissingGateData, DEFAULT_POSITION  # noqa: E402
from historical_replay import build_features, FRESH_BARS  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START, END = "2021-01-01", "2025-12-31"
WARMUP = "2019-06-01"
HORIZONS = [21, 60, 120]
PRIMARY_H = 60                     # declared in the pre-registration
YEARS = ["2021", "2022", "2023", "2024", "2025"]

# Frozen before any return was computed. Printed in full in the results.
SECTORS = {
    "Semiconductors": ("SOXX", [
        "NVDA", "AMD", "INTC", "MU", "AVGO", "QCOM", "TXN", "AMAT", "LRCX", "KLAC",
        "ADI", "MRVL", "NXPI", "ON", "MCHP", "SWKS", "QRVO", "TER", "MPWR", "AMKR"]),
    "Energy": ("XLE", [
        "XOM", "CVX", "COP", "EOG", "SLB", "PSX", "VLO", "MPC", "OXY", "WMB",
        "KMI", "HAL", "DVN", "FANG", "BKR", "HES", "OKE", "TRGP", "APA", "MRO"]),
    "Financials": ("XLF", [
        "JPM", "BAC", "WFC", "C", "GS", "MS", "SCHW", "BLK", "AXP", "USB",
        "PNC", "TFC", "COF", "BK", "STT", "FITB", "KEY", "RF", "CFG", "HBAN"]),
    "Healthcare": ("XLV", [
        "UNH", "JNJ", "LLY", "PFE", "ABBV", "MRK", "TMO", "ABT", "DHR", "BMY",
        "AMGN", "CVS", "MDT", "GILD", "ISRG", "SYK", "BSX", "ZTS", "CI", "HUM"]),
    "Biotech": ("XBI", [
        "VRTX", "REGN", "MRNA", "BIIB", "ALNY", "INCY", "NBIX", "SRPT", "EXEL",
        "HALO", "IONS", "UTHR", "NTRA", "TECH", "RARE", "FOLD", "ARWR", "BMRN"]),
    "Industrials": ("XLI", [
        "GE", "CAT", "HON", "UNP", "BA", "RTX", "LMT", "DE", "UPS", "ETN",
        "EMR", "ITW", "CSX", "NSC", "PH", "GD", "NOC", "FDX", "CMI", "PCAR"]),
    "Software": ("IGV", [
        "MSFT", "ORCL", "CRM", "ADBE", "NOW", "INTU", "PANW", "SNPS", "CDNS",
        "ADSK", "WDAY", "TEAM", "DDOG", "ZS", "CRWD", "NET", "HUBS", "SNOW"]),
    "Discretionary": ("XLY", [
        "AMZN", "TSLA", "HD", "MCD", "NKE", "LOW", "SBUX", "TJX", "BKNG", "CMG",
        "ORLY", "AZO", "ROST", "YUM", "DHI", "LEN", "GM", "F", "MAR", "HLT"]),
    "Materials": ("XLB", [
        "LIN", "APD", "SHW", "ECL", "FCX", "NEM", "NUE", "DOW", "DD", "PPG",
        "VMC", "MLM", "ALB", "IFF", "CE", "STLD", "PKG", "IP", "CF", "MOS"]),
    "Utilities": ("XLU", [
        "NEE", "DUK", "SO", "D", "AEP", "SRE", "EXC", "XEL", "ED", "WEC",
        "ES", "PEG", "AWK", "DTE", "PPL", "FE", "AEE", "CMS", "CNP", "ATO"]),
    "Homebuilders": ("ITB", [
        "DHI", "LEN", "PHM", "NVR", "TOL", "KBH", "MTH", "TMHC", "MHO", "CCS",
        "BLDR", "MAS", "MHK", "OC", "AZEK", "TREX", "FBIN", "WSM"]),
    "Retail": ("XRT", [
        "WMT", "COST", "TGT", "DG", "DLTR", "KR", "BJ", "ULTA", "GPS", "ANF",
        "AEO", "URBN", "FL", "BBY", "DKS", "TSCO", "WSM", "RH", "M", "JWN"]),
}


def load_all():
    syms = sorted({s for _, (etf, names) in SECTORS.items() for s in names}
                  | {etf for etf, _ in SECTORS.values()} | {"SPY"})
    print(f"downloading {len(syms)} symbols...", flush=True)
    out, CH = {}, 100
    for i in range(0, len(syms), CH):
        part = syms[i:i + CH]
        d = yf.download(part, start=WARMUP, end="2026-01-10", interval="1d",
                        group_by="ticker", auto_adjust=False, threads=True, progress=False)
        for s in part:
            try:
                df = d[s].dropna(subset=["Close"])
                if len(df) > 400:
                    df = df.copy()
                    df.index = pd.Index([str(x)[:10] for x in df.index])
                    out[s] = df
            except Exception:
                pass
        print(f"  {min(i+CH, len(syms))}/{len(syms)}", flush=True)
    return out


def fwd(series, date, days):
    idx = list(series.index)
    if date not in idx:
        return None
    k = idx.index(date)
    e = min(k + days, len(idx) - 1)
    if e <= k:
        return None
    a, b = float(series.iloc[k]), float(series.iloc[e])
    return (b / a - 1) * 100 if a > 0 else None


def main():
    px = load_all()
    rows = []
    for sector, (etf, names) in SECTORS.items():
        if etf not in px:
            print(f"  !! benchmark {etf} unavailable - {sector} skipped, reported as such")
            continue
        bench = px[etf]["Close"]
        for s in names:
            df = px.get(s)
            if df is None:
                continue
            try:
                f = build_features(df, regime_on_ha=True)
            except Exception:
                continue
            dirn = f["dirn"].to_numpy()
            since, run = np.full(len(dirn), 10**6), 10**6
            for i in range(len(dirn)):
                if dirn[i] == 1 and (i == 0 or dirn[i - 1] != 1):
                    run = 0
                elif dirn[i] == 1:
                    run += 1
                else:
                    run = 10**6
                since[i] = run
            close = f["raw_close"]
            for i, d in enumerate(f.index):
                if not (START <= d <= END):
                    continue
                if not (0 <= since[i] <= FRESH_BARS):
                    continue
                r = f.iloc[i]
                gate = {"sym": s, "last": r["last"], "zlsma": r["zlsma"],
                        "regime": r["regime"], "adx": r["adx"], "plus_di": r["plus_di"],
                        "minus_di": r["minus_di"], "avg_dollar_vol": r["avg_dollar_vol"],
                        "atr": r["atr"], "long_stop": r["long_stop"],
                        "pct_vs_200": r["pct_vs_200"]}
                try:
                    verdict, _, _ = evaluate(gate, position_size=DEFAULT_POSITION)
                except MissingGateData:
                    continue
                if verdict.startswith("BLOCKED"):
                    continue
                rec = {"sector": sector, "etf": etf, "sym": s, "date": d, "year": d[:4]}
                ok = True
                for h in HORIZONS:
                    sr, br = fwd(close, d, h), fwd(bench, d, h)
                    if sr is None or br is None:
                        ok = False
                        break
                    rec[f"stock_{h}"] = round(sr, 3)
                    rec[f"etf_{h}"] = round(br, 3)
                    rec[f"excess_{h}"] = round(sr - br, 3)
                if ok:
                    rows.append(rec)
        print(f"  {sector:16s} {etf:5s} signals so far {len(rows)}", flush=True)

    if not rows:
        raise SystemExit("no signals - nothing to compare")

    def stats(rs, h):
        if not rs:
            return None
        e = np.array([r[f"excess_{h}"] for r in rs])
        return {"n": len(e), "mean_excess": round(float(e.mean()), 2),
                "median_excess": round(float(np.median(e)), 2),
                "hit_rate": round(float(100 * (e > 0).mean()), 1),
                "mean_stock": round(float(np.mean([r[f"stock_{h}"] for r in rs])), 2),
                "mean_etf": round(float(np.mean([r[f"etf_{h}"] for r in rs])), 2)}

    out = {"n_signals": len(rows), "primary_horizon": PRIMARY_H,
           "overall": {h: stats(rows, h) for h in HORIZONS},
           "by_sector": {}, "by_year": {}}
    for sector in SECTORS:
        rs = [r for r in rows if r["sector"] == sector]
        out["by_sector"][sector] = {h: stats(rs, h) for h in HORIZONS}
    for y in YEARS:
        rs = [r for r in rows if r["year"] == y]
        out["by_year"][y] = {h: stats(rs, h) for h in HORIZONS}

    json.dump({"rows": rows, "summary": out},
              open(os.path.join(REPO, "research", "sector-vs-stockpicking.json"), "w"), indent=1)

    P = PRIMARY_H
    print(f"\n{'='*74}\nPRIMARY HORIZON: {P} trading days   (n={len(rows)} signals)\n{'='*74}")
    o = out["overall"][P]
    print(f"  stock picks     {o['mean_stock']:+7.2f}%")
    print(f"  their sector ETF{o['mean_etf']:+7.2f}%")
    print(f"  EXCESS          {o['mean_excess']:+7.2f}pt      hit rate {o['hit_rate']:.1f}%")
    print("\nOther horizons (context only, not the headline):")
    for h in HORIZONS:
        s = out["overall"][h]
        print(f"  {h:3d}d  excess {s['mean_excess']:+6.2f}pt  hit {s['hit_rate']:5.1f}%  "
              f"(stock {s['mean_stock']:+6.2f}% vs etf {s['mean_etf']:+6.2f}%)")
    print(f"\nBY SECTOR at {P}d - every sector reported:")
    for sector, d in out["by_sector"].items():
        s = d[P]
        if not s:
            print(f"  {sector:16s} no signals")
            continue
        print(f"  {sector:16s} n={s['n']:4d}  excess {s['mean_excess']:+6.2f}pt  "
              f"hit {s['hit_rate']:5.1f}%")
    print(f"\nBY YEAR at {P}d - every year reported, 2022 included:")
    for y, d in out["by_year"].items():
        s = d[P]
        if not s:
            print(f"  {y} no signals")
            continue
        print(f"  {y}  n={s['n']:4d}  excess {s['mean_excess']:+6.2f}pt  hit {s['hit_rate']:5.1f}%  "
              f"(stock {s['mean_stock']:+6.2f}% vs etf {s['mean_etf']:+6.2f}%)")
    print("\nwrote research/sector-vs-stockpicking.json")


if __name__ == "__main__":
    main()
