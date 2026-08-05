"""One-shot market sweep for CAR-style squeeze candidates.
Universe: Russell starter list (~1200) + repo watchlist tickers.
Pulls short interest %float, days-to-cover, float, cap, liquidity via yfinance.
Output: ranked JSON + printed table of names meeting the tinder bar.
"""
import concurrent.futures as cf
import csv
import json
import re
import sys
from pathlib import Path

import yfinance as yf

REPO = Path(r"C:\Users\osuby\tradingview-mcp")
RUSSELL = Path(r"C:\Users\osuby\Documents\Equities_Scanner\russell_starter.csv")
OUT = Path(__file__).parent / "squeeze_sweep_results.json"

def universe():
    syms = set()
    with open(RUSSELL) as f:
        for row in csv.reader(f):
            s = row[0].strip().upper()
            if s and s != "SYMBOL":
                syms.add(s)
    for wl in ["main-watchlist.md", "hq-swing-analysis.md", "sector-themes-analysis.md"]:
        p = REPO / "watchlists" / wl
        if p.exists():
            for m in re.finditer(r"\b[A-Z]{1,5}\b", p.read_text(encoding="utf-8", errors="ignore")):
                pass  # watchlist parsing too noisy; russell + known tinder covers breadth
    # always include the current tinder list for fresh readings
    tw = json.loads((REPO / "watchlists" / "squeeze-watch.json").read_text())
    for t in tw["tinder"]:
        syms.add(t["sym"].split(":")[1])
    return sorted(syms)

def fetch(sym):
    try:
        info = yf.Ticker(sym).info
        spf = info.get("shortPercentOfFloat")
        if spf is None:
            return None
        return {
            "sym": sym,
            "si_pct": round(spf * 100, 1),
            "days_to_cover": info.get("shortRatio"),
            "float_m": round((info.get("floatShares") or 0) / 1e6, 1),
            "cap_m": round((info.get("marketCap") or 0) / 1e6, 0),
            "price": info.get("currentPrice") or info.get("regularMarketPrice"),
            "avg_vol_m": round((info.get("averageVolume") or 0) / 1e6, 2),
            "pct_of_52wk_high": round(100 * (info.get("currentPrice") or 0) / info["fiftyTwoWeekHigh"], 1) if info.get("fiftyTwoWeekHigh") and info.get("currentPrice") else None,
        }
    except Exception:
        return None

def main():
    syms = universe()
    print(f"sweeping {len(syms)} names...", flush=True)
    rows = []
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        for i, r in enumerate(ex.map(fetch, syms)):
            if r:
                rows.append(r)
            if i % 200 == 0:
                print(f"  {i}/{len(syms)}", flush=True)
    # tinder bar: SI >= 15%, tradable cap + liquidity
    hits = [r for r in rows if r["si_pct"] >= 15 and (r["cap_m"] or 0) >= 500 and (r["avg_vol_m"] or 0) >= 0.5]
    hits.sort(key=lambda r: -r["si_pct"])
    OUT.write_text(json.dumps({"swept": len(syms), "with_si_data": len(rows), "hits": hits}, indent=1))
    print(f"\n{len(rows)} names had SI data; {len(hits)} meet the bar (SI>=15%, cap>=$500M, vol>=0.5M):\n")
    print(f"{'SYM':<6} {'SI%':>6} {'DTC':>5} {'Float(M)':>9} {'Cap($M)':>9} {'AvgVol(M)':>10} {'%of52wkHi':>10}")
    for r in hits[:40]:
        print(f"{r['sym']:<6} {r['si_pct']:>6} {str(r['days_to_cover']):>5} {r['float_m']:>9} {r['cap_m']:>9.0f} {r['avg_vol_m']:>10} {str(r['pct_of_52wk_high']):>10}")

if __name__ == "__main__":
    main()
