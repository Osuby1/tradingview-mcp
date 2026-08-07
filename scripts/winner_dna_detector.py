#!/usr/bin/env python3
"""Winner-DNA study — DETECTOR SOURCE as the lead variable.

Promoted 2026-08-06 after band width died: source spread was ~8x the trait spread
(+4.03% orig-COILED to -4.24% orig-COOLING at +21) in the second cut. This runs it
properly, with the controls that cut lacked.

WHAT THE SECOND CUT GOT WRONG AND THIS FIXES
  1. RAW returns confound the detector with WHEN it fired. If COOLING happened to
     flag into a down week it looks bad for reasons that have nothing to do with
     the detector. Everything here is EXCESS OVER SPY across the identical window.
  2. No error bars. n=31-112 per cell can produce an 8-point spread from noise
     alone, so every mean carries a bootstrap 95% interval. If the interval spans
     zero, the cell is not evidence.
  3. No stability check. The sample is split by flag date into halves; a source
     whose ranking flips between halves is noise, however big its full-sample mean.
  4. Overlap unreported. Sources share names; shared flags are not independent
     observations and the overlap is printed.

NO LOOK-AHEAD: returns measured forward from each flag date's close only.

Usage: python scripts/winner_dna_detector.py
"""
import json
import random
import statistics as st
from pathlib import Path

import pandas as pd
import yfinance as yf

REPO = Path(__file__).resolve().parent.parent
SCANNER_LOG = Path.home() / "Documents" / "Equities_Scanner" / "recommendations_log.csv"
HORIZONS = [5, 10, 21]
WIN_HI = 15.0
random.seed(7)                      # deterministic bootstrap (scripts may not use Date/random-time)


def collect():
    """[(sym, source, date, grade)] - first flag per (sym, source)."""
    seen, out = set(), []
    for f in sorted((REPO / "watchlists").glob("universe-results-*.json")):
        date = f.stem.replace("universe-results-", "")
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for e in d.get("hits", []):
            if isinstance(e, dict) and e.get("sym"):
                k = (e["sym"], "sweep-CE")
                if k not in seen:
                    seen.add(k); out.append((e["sym"], "sweep-CE", date, ""))
    frames = []
    if SCANNER_LOG.exists():
        frames.append(pd.read_csv(SCANNER_LOG))
    for f in sorted((REPO / "research").glob("recommendations_log-*.csv")):
        try:
            frames.append(pd.read_csv(f))
        except Exception:
            pass
    if frames:
        big = pd.concat(frames, ignore_index=True).dropna(subset=["date", "ticker"])
        for _, r in big.sort_values("date").iterrows():
            sym = str(r["ticker"]).strip().upper()
            src = f"orig-{str(r.get('tab', '?')).strip().upper()}"
            k = (sym, src)
            if k not in seen:
                seen.add(k)
                out.append((sym, src, str(r["date"])[:10], str(r.get("grade", "")).strip()))
    return out


def boot_ci(vals, n=2000):
    if len(vals) < 3:
        return (float("nan"), float("nan"))
    means = []
    for _ in range(n):
        means.append(st.mean(random.choices(vals, k=len(vals))))
    means.sort()
    return (means[int(0.025 * n)], means[int(0.975 * n)])


def main():
    flags = collect()
    syms = sorted({s for s, _, _, _ in flags})
    print(f"flag records: {len(flags)} across {len(syms)} symbols")

    px = yf.download(syms + ["SPY", "IWM"], start="2026-01-01", end="2026-08-07",
                     progress=False, auto_adjust=True, group_by="ticker", threads=True)
    spy = px["SPY"].dropna()
    iwm = px["IWM"].dropna()   # small-cap benchmark: most flags are not S&P names

    rows, skipped = [], 0
    for sym, src, fdate, grade in flags:
        try:
            df = px[sym].dropna()
        except Exception:
            skipped += 1; continue
        idx = df.index[df.index <= pd.Timestamp(fdate)]
        sidx = spy.index[spy.index <= pd.Timestamp(fdate)]
        widx = iwm.index[iwm.index <= pd.Timestamp(fdate)]
        if len(idx) == 0 or len(sidx) == 0 or len(widx) == 0:
            skipped += 1; continue
        pos, spos = df.index.get_loc(idx[-1]), spy.index.get_loc(sidx[-1])
        wpos = iwm.index.get_loc(widx[-1])
        c0, s0 = float(df["Close"].iloc[pos]), float(spy["Close"].iloc[spos])
        w0 = float(iwm["Close"].iloc[wpos])
        rec = {"sym": sym, "src": src, "flag": fdate, "grade": grade}
        any_h = False
        for h in HORIZONS:
            if pos + h < len(df) and spos + h < len(spy):
                r = (float(df["Close"].iloc[pos + h]) / c0 - 1) * 100
                m = (float(spy["Close"].iloc[spos + h]) / s0 - 1) * 100
                rec[f"fwd{h}"], rec[f"exc{h}"] = round(r, 2), round(r - m, 2)
                if wpos + h < len(iwm):
                    wm = (float(iwm["Close"].iloc[wpos + h]) / w0 - 1) * 100
                    rec[f"exw{h}"] = round(r - wm, 2)
                any_h = True
        if any_h:
            rows.append(rec)
        else:
            skipped += 1
    print(f"graded {len(rows)}, skipped {skipped}\n")

    sources = sorted({r["src"] for r in rows})

    for h in HORIZONS:
        print("=" * 96)
        print(f"HORIZON +{h} SESSIONS — EXCESS OVER SPY (the number that isn't just market timing)")
        print("=" * 96)
        print(f"{'source':<22}{'n':>5}{'mean exc':>10}{'95% CI':>20}{'median':>9}"
              f"{'beat SPY':>10}{'>=+15%':>8}{'raw mean':>10}")
        allx = []
        for src in sources:
            g = [r for r in rows if r["src"] == src and f"exc{h}" in r]
            if len(g) < 5:
                continue
            x = [r[f"exc{h}"] for r in g]
            raw = [r[f"fwd{h}"] for r in g]
            allx += x
            lo, hi = boot_ci(x)
            beat = 100 * sum(1 for v in x if v > 0) / len(x)
            big = 100 * sum(1 for v in raw if v >= WIN_HI) / len(raw)
            star = "  <-- CI excludes 0" if (lo > 0 or hi < 0) else ""
            print(f"{src:<22}{len(g):>5}{st.mean(x):>+9.2f}%"
                  f"{f'[{lo:+.2f}, {hi:+.2f}]':>20}{st.median(x):>+8.2f}%"
                  f"{beat:>9.0f}%{big:>7.0f}%{st.mean(raw):>+9.2f}%{star}")
        if allx:
            print(f"{'ALL FLAGS POOLED':<22}{len(allx):>5}{st.mean(allx):>+9.2f}%"
                  f"{'':>20}{st.median(allx):>+8.2f}%"
                  f"{100*sum(1 for v in allx if v>0)/len(allx):>9.0f}%")
        print()

    print("=" * 96)
    print("ROBUSTNESS — same thing benchmarked against IWM (small caps), +21 sessions")
    print("=" * 96)
    for src in sources:
        g = [r["exw21"] for r in rows if r["src"] == src and "exw21" in r]
        if len(g) >= 5:
            lo, hi = boot_ci(g)
            print(f"  {src:<22} n={len(g):<4} mean vs IWM {st.mean(g):>+7.2f}%  "
                  f"95% CI [{lo:+.2f}, {hi:+.2f}]  beat IWM "
                  f"{100*sum(1 for v in g if v>0)/len(g):.0f}%")
    pooled = [r["exw21"] for r in rows if "exw21" in r]
    if pooled:
        print(f"  {'ALL FLAGS POOLED':<22} n={len(pooled):<4} mean vs IWM {st.mean(pooled):>+7.2f}%  "
              f"beat IWM {100*sum(1 for v in pooled if v>0)/len(pooled):.0f}%")
    print()

    # ---- stability: split by flag date ----
    print("=" * 96)
    print("STABILITY — does the ranking survive splitting the sample in half by date?")
    print("=" * 96)
    g21 = [r for r in rows if "exc21" in r]
    if g21:
        dates = sorted(r["flag"] for r in g21)
        cut = dates[len(dates) // 2]
        print(f"early half: flags <= {cut} | late half: flags > {cut}\n")
        print(f"{'source':<22}{'early n':>9}{'early exc':>11}{'late n':>8}{'late exc':>11}{'consistent?':>13}")
        for src in sources:
            e = [r["exc21"] for r in g21 if r["src"] == src and r["flag"] <= cut]
            l = [r["exc21"] for r in g21 if r["src"] == src and r["flag"] > cut]
            if len(e) < 4 or len(l) < 4:
                print(f"{src:<22}{len(e):>9}{'-':>11}{len(l):>8}{'-':>11}{'too few':>13}")
                continue
            same = (st.mean(e) > 0) == (st.mean(l) > 0)
            print(f"{src:<22}{len(e):>9}{st.mean(e):>+10.2f}%{len(l):>8}{st.mean(l):>+10.2f}%"
                  f"{('YES' if same else 'NO - flips'):>13}")
    print()

    # ---- grade within origination ----
    print("=" * 96)
    print("GRADE (origination A vs B) — excess over SPY at +21")
    print("=" * 96)
    for gr in ("A", "B"):
        g = [r["exc21"] for r in rows if r.get("grade") == gr and "exc21" in r]
        if len(g) >= 5:
            lo, hi = boot_ci(g)
            print(f"  grade {gr}: n={len(g):<4} mean {st.mean(g):+.2f}%  "
                  f"95% CI [{lo:+.2f}, {hi:+.2f}]  beat SPY "
                  f"{100*sum(1 for v in g if v>0)/len(g):.0f}%")

    # ---- overlap ----
    print("\n" + "=" * 96)
    print("OVERLAP — shared names are not independent observations")
    print("=" * 96)
    setmap = {s: {r["sym"] for r in rows if r["src"] == s} for s in sources}
    for i, a in enumerate(sources):
        for b in sources[i + 1:]:
            ov = setmap[a] & setmap[b]
            if ov:
                print(f"  {a} AND {b}: {len(ov)} names "
                      f"({100*len(ov)/min(len(setmap[a]), len(setmap[b])):.0f}% of the smaller)")

    out = REPO / "research" / "winner-dna-detector.json"
    out.write_text(json.dumps(rows, indent=1))
    print(f"\nwrote {out.name} ({len(rows)} graded flags)")


if __name__ == "__main__":
    main()
