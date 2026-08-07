#!/usr/bin/env python3
"""Is the COOLING tab fat-tailed or just bad? (Omar, 2026-08-06)

The tension this settles: the detector study measured COOLING at -5.52% vs IWM
over 112 flags with the interval excluding zero, so I built it into the A-List as
a veto. The runner backtest then showed that veto blocks TEN of the twenty names
on the runners list, four of them with readiness 70. Both are true. The question
is WHY.

  * If COOLING is FAT-TAILED - a handful of large winners funding many small
    laggards - then a hard veto throws away the winners with the chaff, and the
    right answer is smaller size, not exclusion.
  * If COOLING is BROADLY NEGATIVE - most flags down, the mean not rescued by
    the tail - the veto stands and the runners list is simply survivorship.

Three tests, because buy-and-hold means are the wrong lens for how we trade:
  1. FULL DISTRIBUTION - deciles, median vs mean, both tails, skew.
  2. TAIL ARITHMETIC - do the top decile's gains cover the rest's losses?
  3. THE WAY WE ACTUALLY TRADE - entry at the scanner's own price, exit on its
     own stop (daily LOW touch) or at 21 sessions. A stop changes fat-tailed
     distributions more than any other intervention, so a verdict that ignores
     it is not a verdict about our system.

A buy-intent control (COILED / FRESH IGNITION) runs through the identical code
so every number has something to be compared against.

Usage: python scripts/cooling_distribution.py
"""
import statistics as st
from pathlib import Path

import pandas as pd
import yfinance as yf

REPO = Path(__file__).resolve().parent.parent
SCANNER_LOG = Path.home() / "Documents" / "Equities_Scanner" / "recommendations_log.csv"
import os
HOLD = int(os.environ.get("HOLD", "21"))


def load(tabs):
    df = pd.read_csv(SCANNER_LOG)
    df = df.dropna(subset=["date", "ticker", "price"])
    df["tab"] = df["tab"].astype(str).str.strip().str.upper()
    return df[df["tab"].isin(tabs)].copy()


def simulate(rows, px, label):
    bh, managed, stopped, held = [], [], 0, 0
    for _, r in rows.iterrows():
        sym = str(r["ticker"]).strip().upper()
        try:
            df = px[sym].dropna()
        except Exception:
            continue
        idx = df.index[df.index <= pd.Timestamp(str(r["date"])[:10])]
        if len(idx) == 0:
            continue
        pos = df.index.get_loc(idx[-1])
        if pos + HOLD >= len(df):
            continue
        entry = float(r["price"])
        if entry <= 0:
            continue
        win = df.iloc[pos + 1:pos + HOLD + 1]
        bh.append((float(df["Close"].iloc[pos + HOLD]) / entry - 1) * 100)
        stop = float(r["stop"]) if pd.notna(r["stop"]) and 0 < float(r["stop"]) < entry else None
        if stop is not None and (win["Low"] <= stop).any():
            managed.append((stop / entry - 1) * 100)      # filled at the stop
            stopped += 1
        else:
            managed.append((float(win["Close"].iloc[-1]) / entry - 1) * 100)
            held += 1
    return bh, managed, stopped, held


def describe(v, label):
    v = sorted(v)
    n = len(v)
    if n < 10:
        print(f"  {label}: n={n} - too few"); return
    dec = [v[int(n * i / 10)] for i in range(10)]
    print(f"\n  {label}  (n={n})")
    print(f"    mean {st.mean(v):+7.2f}%   median {st.median(v):+7.2f}%   "
          f"win rate {100*sum(1 for x in v if x > 0)/n:.0f}%")
    print(f"    deciles: " + " ".join(f"{d:+.0f}" for d in dec))
    print(f"    worst {v[0]:+.1f}%  |  best {v[-1]:+.1f}%  |  "
          f">= +15%: {sum(1 for x in v if x >= 15)} ({100*sum(1 for x in v if x >= 15)/n:.0f}%)  "
          f">= +25%: {sum(1 for x in v if x >= 25)}  |  <= -15%: {sum(1 for x in v if x <= -15)}")
    top = v[int(n * 0.9):]
    rest = v[:int(n * 0.9)]
    print(f"    TAIL ARITHMETIC: top decile contributes {sum(top)/n:+.2f} pts of the "
          f"{st.mean(v):+.2f}% mean; the other 90% contribute {sum(rest)/n:+.2f} pts")
    print(f"    -> without its top decile the mean would be "
          f"{st.mean(rest) if rest else 0:+.2f}%")


def main():
    cool = load({"COOLING"})
    buy = load({"COILED", "FRESH IGNITION"})
    syms = sorted(set(cool["ticker"].astype(str).str.upper()) |
                  set(buy["ticker"].astype(str).str.upper()))
    print(f"[HOLD = {HOLD} sessions]")
    print(f"COOLING rows {len(cool)} | buy-intent rows {len(buy)} | {len(syms)} symbols")
    px = yf.download(syms, start="2026-01-01", end="2026-08-07", progress=False,
                     auto_adjust=True, group_by="ticker", threads=True)

    print("\n" + "=" * 84)
    print("TEST 1+2 — FULL DISTRIBUTION AND TAIL ARITHMETIC (buy and hold 21 sessions)")
    print("=" * 84)
    cb, cm, cs, ch = simulate(cool, px, "cooling")
    bb, bm, bs, bh_ = simulate(buy, px, "buy")
    describe(cb, "COOLING")
    describe(bb, "BUY-INTENT control (COILED + FRESH IGNITION)")

    print("\n" + "=" * 84)
    print("TEST 3 — THE WAY WE ACTUALLY TRADE (scanner entry, scanner stop, 21-session cap)")
    print("=" * 84)
    describe(cm, f"COOLING managed  [{cs} stopped out, {ch} held to time]")
    describe(bm, f"BUY-INTENT managed  [{bs} stopped out, {bh_} held to time]")

    print("\n" + "=" * 84)
    print("VERDICT INPUTS")
    print("=" * 84)
    if cb and cm:
        print(f"  COOLING     buy&hold mean {st.mean(cb):+.2f}%  ->  with its stop "
              f"{st.mean(cm):+.2f}%   (stop-out rate {100*cs/(cs+ch):.0f}%)")
    if bb and bm:
        print(f"  BUY-INTENT  buy&hold mean {st.mean(bb):+.2f}%  ->  with its stop "
              f"{st.mean(bm):+.2f}%   (stop-out rate {100*bs/(bs+bh_):.0f}%)")


if __name__ == "__main__":
    main()
