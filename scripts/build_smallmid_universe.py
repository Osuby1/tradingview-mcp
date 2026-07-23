"""Build a small/mid-cap universe for the PEAD test - where the anomaly lives.

Reads the origination scanner's russell_starter.csv (~1200 Russell names), pulls
market cap via yfinance fast_info, keeps $300M-$12B (small + mid cap), and writes
research/smallmid-universe.json. Excludes the mega-caps already tested large-cap.
"""
import csv
import json
import os
import time

import yfinance as yf

SRC = os.path.expanduser("~/Documents/Equities_Scanner/russell_starter.csv")
MIN_CAP, MAX_CAP = 300_000_000, 12_000_000_000
MAX_NAMES = 300


def main():
    tickers = []
    with open(SRC) as fh:
        for row in csv.reader(fh):
            if row and row[0].strip().upper() != "SYMBOL":
                tickers.append(row[0].strip().upper())
    print(f"{len(tickers)} tickers in russell_starter")

    keep = []
    for i, t in enumerate(tickers):
        try:
            fi = yf.Ticker(t).fast_info
            # FastInfo.get() does NOT normalize snake_case keys; bracket/getattr do.
            cap = getattr(fi, "market_cap", None)
            px = getattr(fi, "last_price", None)
            if cap and MIN_CAP <= cap <= MAX_CAP and px and px >= 5:
                keep.append({"sym": t, "cap": int(cap), "px": round(float(px), 2)})
        except Exception:
            pass
        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{len(tickers)}  kept {len(keep)}")
        time.sleep(0.03)

    keep.sort(key=lambda x: x["cap"])          # smallest first (strongest PEAD)
    keep = keep[:MAX_NAMES]
    out = {"filter": f"${MIN_CAP/1e6:.0f}M-${MAX_CAP/1e9:.0f}B, price>=5",
           "count": len(keep), "symbols": [k["sym"] for k in keep], "detail": keep}
    with open("research/smallmid-universe.json", "w") as fh:
        json.dump(out, fh, indent=1)
    caps = [k["cap"] for k in keep]
    print(f"\nsmall/mid universe: {len(keep)} names")
    if caps:
        print(f"  cap range ${min(caps)/1e6:.0f}M - ${max(caps)/1e9:.1f}B, "
              f"median ${sorted(caps)[len(caps)//2]/1e9:.1f}B")
    print("wrote research/smallmid-universe.json")


if __name__ == "__main__":
    main()
