#!/usr/bin/env python3
"""Winner-DNA first cut: does BAND-WIDTH PERCENTILE at flag separate runners
from duds?

Pre-registered 2026-08-06 (research/winner-dna-preregistration.md), amended the
same day with Omar's design: contrast winners against same-period duds, never
profile winners alone. Band width was promoted to LEAD hypothesis after the
GE-vs-BA post-mortem, and again after the structure-tag bug showed we had been
ASSERTING compression without measuring it.

MEASUREMENT (no look-ahead): band width = (upper - lower) / mid on a 20-day
Bollinger (2 sd). Its percentile is that day's value ranked inside the trailing
120 sessions ENDING ON THE FLAG DATE. Nothing after the flag touches the trait.

SAMPLE: every fresh Chandelier BUY flag ('hits') in watchlists/universe-results-*.json,
first flag per symbol only. Forward return measured from the flag date's close.

HONEST HORIZON PROBLEM, stated not hidden: the sweep archive starts 2026-07-18,
so NO flag has the pre-registered +1 month of forward data yet. This cut grades at
+5 and +10 trading days and is labelled PRELIMINARY. The +1m cut runs in September.

Usage: python scripts/winner_dna_bandwidth.py [--horizon 10]
"""
import argparse
import json
import statistics as st
from pathlib import Path

import pandas as pd
import yfinance as yf

REPO = Path(__file__).resolve().parent.parent
WIN_HI, DUD_HI = 15.0, 5.0          # frozen thresholds from the pre-registration
BB_N, PCTILE_WINDOW = 20, 120


def collect_flags():
    """First-ever flag date per symbol across the sweep archive."""
    flags = {}
    for f in sorted((REPO / "watchlists").glob("universe-results-*.json")):
        date = f.stem.replace("universe-results-", "")
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for e in d.get("hits", []):
            if isinstance(e, dict) and e.get("sym"):
                flags.setdefault(e["sym"], date)   # first occurrence wins
    return flags


def band_width_series(df):
    mid = df["Close"].rolling(BB_N).mean()
    sd = df["Close"].rolling(BB_N).std()
    return ((mid + 2 * sd) - (mid - 2 * sd)) / mid


def analyse(horizon):
    flags = collect_flags()
    syms = sorted(flags)
    print(f"flags collected: {len(syms)} unique symbols, "
          f"{min(flags.values())} .. {max(flags.values())}")

    px = yf.download(syms, start="2025-10-01", end="2026-08-07",
                     progress=False, auto_adjust=True, group_by="ticker",
                     threads=True)

    rows, skipped = [], []
    for sym in syms:
        try:
            df = px[sym].dropna()
        except Exception:
            skipped.append((sym, "no data")); continue
        if len(df) < PCTILE_WINDOW + BB_N:
            skipped.append((sym, f"only {len(df)} bars")); continue
        fd = pd.Timestamp(flags[sym])
        idx = df.index[df.index <= fd]
        if len(idx) == 0:
            skipped.append((sym, "flag date before history")); continue
        pos = df.index.get_loc(idx[-1])
        if pos + horizon >= len(df):
            skipped.append((sym, f"only {len(df)-1-pos}d forward"))
            continue

        bw = band_width_series(df.iloc[:pos + 1])          # <= flag date ONLY
        win = bw.dropna().iloc[-PCTILE_WINDOW:]
        if len(win) < PCTILE_WINDOW // 2:
            skipped.append((sym, "band-width window too short")); continue
        pct = round(100.0 * (win < win.iloc[-1]).sum() / len(win))

        c0 = float(df["Close"].iloc[pos])
        cN = float(df["Close"].iloc[pos + horizon])
        fwd = (cN / c0 - 1) * 100
        mfe = (float(df["High"].iloc[pos + 1:pos + horizon + 1].max()) / c0 - 1) * 100
        rows.append({"sym": sym, "flag": flags[sym], "bw_pctile": pct,
                     "fwd": round(fwd, 2), "mfe": round(mfe, 2)})

    win = [r for r in rows if r["fwd"] >= WIN_HI]
    dud = [r for r in rows if r["fwd"] < DUD_HI]
    mid = [r for r in rows if DUD_HI <= r["fwd"] < WIN_HI]

    def desc(g, label):
        if not g:
            return f"  {label:<26} n=0"
        v = sorted(r["bw_pctile"] for r in g)
        coiled = sum(1 for x in v if x <= 25)
        return (f"  {label:<26} n={len(g):<4} median band-width pctile "
                f"{st.median(v):>5.1f}  mean {st.mean(v):>5.1f}  "
                f"quartiles {v[len(v)//4]:>3}/{v[len(v)//2]:>3}/{v[3*len(v)//4]:>3}  "
                f"COILED(<=25th) {coiled}/{len(g)} = {100*coiled/len(g):.0f}%")

    print(f"\n=== WINNER-DNA FIRST CUT — BAND WIDTH — horizon +{horizon} sessions ===")
    print(f"graded {len(rows)} flags | excluded {len(skipped)} "
          f"(insufficient forward data or history)\n")
    print(desc(win, f"RUNNERS (>= +{WIN_HI:.0f}%)"))
    print(desc(mid, f"MIDDLE (+{DUD_HI:.0f}% to +{WIN_HI:.0f}%)"))
    print(desc(dud, f"DUDS (< +{DUD_HI:.0f}%)"))

    print("\n--- the question that decides it: does compression pay? ---")
    for lo, hi, lab in [(0, 25, "COILED    (0-25th)"), (26, 59, "MIDDLE   (26-59th)"),
                        (60, 100, "EXPANDED (60-100th)")]:
        g = [r for r in rows if lo <= r["bw_pctile"] <= hi]
        if not g:
            print(f"  {lab}: n=0"); continue
        f = [r["fwd"] for r in g]
        hit = sum(1 for x in f if x >= WIN_HI)
        print(f"  {lab}: n={len(g):<4} mean fwd {st.mean(f):>6.2f}%  "
              f"median {st.median(f):>6.2f}%  >= +{WIN_HI:.0f}%: {hit}/{len(g)} "
              f"({100*hit/len(g):.0f}%)  mean MFE {st.mean([r['mfe'] for r in g]):>5.2f}%")

    if win:
        print("\n--- every runner, with its measured band width at flag ---")
        for r in sorted(win, key=lambda x: -x["fwd"]):
            tag = "COILED" if r["bw_pctile"] <= 25 else (
                "expanded" if r["bw_pctile"] >= 60 else "middle")
            print(f"  {r['sym']:<7} flagged {r['flag']}  bw {r['bw_pctile']:>3}th "
                  f"({tag:<8}) -> {r['fwd']:+6.2f}%  MFE {r['mfe']:+6.2f}%")

    out = REPO / "research" / f"winner-dna-bandwidth-h{horizon}.json"
    out.write_text(json.dumps({"horizon": horizon, "rows": rows,
                               "skipped": skipped}, indent=1))
    print(f"\nwrote {out.name} ({len(rows)} graded, {len(skipped)} excluded)")
    return rows


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--horizon", type=int, default=10)
    a = ap.parse_args()
    analyse(a.horizon)
