"""Dump daily OHLC for every symbol in the calls ledger + SPY, for the outcome
tracker. yfinance-based so the whole forward-validation loop runs unattended
(no chart needed).

Usage: python scripts/dump_call_prices.py [YYYY-MM-DD]
"""
import json
import sys

import pandas as pd
import yfinance as yf


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else pd.Timestamp.today().strftime("%Y-%m-%d")
    led = json.load(open("research/calls-ledger.json"))
    syms = sorted({c["sym"] for c in led["calls"]} | {"SPY"})
    print(f"dumping prices for {len(syms)} symbols...")
    raw = yf.download(syms, period="6mo", interval="1d", auto_adjust=True,
                      progress=False, group_by="ticker", threads=True)
    out = {}
    for s in syms:
        try:
            df = raw[s][["Close", "High", "Low"]].dropna()
        except Exception:
            continue
        rows = [{"d": d.strftime("%Y-%m-%d"), "c": round(float(r.Close), 4),
                 "h": round(float(r.High), 4), "l": round(float(r.Low), 4)}
                for d, r in df.iterrows()]
        if rows:
            out[s] = rows
    path = f"research/call-prices-{date}.json"
    json.dump(out, open(path, "w"), indent=1)
    print(f"wrote {path} with {len(out)}/{len(syms)} symbols")


if __name__ == "__main__":
    main()
