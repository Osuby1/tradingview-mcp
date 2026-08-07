#!/usr/bin/env python3
"""Winner-DNA band-width study v2 — ALL detectors + a properly powered history arm.

WHY v2 (Omar, 2026-08-06 PM): v1 used only the Chandelier sweep archive, which
starts 7/18 and never contained CDNA/EAT/IOVA/AMLX at all. Its sample did not
represent "our flags", and with 2 runners it could not answer the question.

ARM 1 - ALL-DETECTOR FLAGS. Union of every flag source we keep dated records for:
  * sweep-CE      : fresh Chandelier BUY, watchlists/universe-results-*.json (7/18+)
  * orig-<TAB>    : origination scanner recommendations_log (7/1+), carrying its
                    OWN independent COILED / FRESH IGNITION / COOLING / BUY ZONE
                    labels - which lets us cross-check our band-width measure
                    against a second opinion built by different code.
First flag per (symbol, source); a name re-flagged nightly is one observation.

ARM 2 - HISTORY (the power fix). The flag archive can never be big enough this
year, so we also ask the underlying question directly: across the SAME universe
of names we actually trade, over ~2 years, does a low band-width percentile
predict better forward returns? Every 5th session per name = thousands of
observations. This is NOT "our flags" and is labelled as such - it is the
statistical backstop that tells us whether the trait has any predictive content
at all before we blame the sample size.

NO LOOK-AHEAD ANYWHERE: band width percentile is ranked inside the 120 sessions
ENDING on the observation date.

Usage: python scripts/winner_dna_bandwidth_v2.py
"""
import json
import statistics as st
from pathlib import Path

import pandas as pd
import yfinance as yf

REPO = Path(__file__).resolve().parent.parent
SCANNER_LOG = Path.home() / "Documents" / "Equities_Scanner" / "recommendations_log.csv"
BB_N, PCT_WIN = 20, 120
HORIZONS = [5, 10, 21]
WIN_HI, DUD_HI = 15.0, 5.0


def collect_flags():
    """{(sym, source): first_flag_date}"""
    flags = {}

    for f in sorted((REPO / "watchlists").glob("universe-results-*.json")):
        date = f.stem.replace("universe-results-", "")
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for e in d.get("hits", []):
            if isinstance(e, dict) and e.get("sym"):
                flags.setdefault((e["sym"], "sweep-CE"), date)

    frames = []
    if SCANNER_LOG.exists():
        frames.append(pd.read_csv(SCANNER_LOG))
    for f in sorted((REPO / "research").glob("recommendations_log-*.csv")):
        try:
            frames.append(pd.read_csv(f))
        except Exception:
            pass
    if frames:
        big = pd.concat(frames, ignore_index=True)
        big = big.dropna(subset=["date", "ticker"]).sort_values("date")
        for _, r in big.iterrows():
            src = f"orig-{str(r.get('tab', '?')).strip().upper()}"
            flags.setdefault((str(r["ticker"]).strip().upper(), src), str(r["date"])[:10])
    return flags


def bw_pctile_series(close):
    """Rolling band-width percentile, each point ranked in its own trailing window."""
    mid = close.rolling(BB_N).mean()
    sd = close.rolling(BB_N).std()
    bw = ((mid + 2 * sd) - (mid - 2 * sd)) / mid
    return bw, bw.rolling(PCT_WIN).apply(
        lambda w: 100.0 * (w[:-1] < w[-1]).sum() / (len(w) - 1), raw=True)


def bucket(p):
    return "COILED" if p <= 25 else ("EXPANDED" if p >= 60 else "MIDDLE")


def main():
    flags = collect_flags()
    syms = sorted({s for s, _ in flags})
    print(f"flag records: {len(flags)} across {len(syms)} symbols")
    by_src = {}
    for (s, src), d in flags.items():
        by_src.setdefault(src, []).append(d)
    for src, ds in sorted(by_src.items()):
        print(f"   {src:<22} n={len(ds):<5} {min(ds)} .. {max(ds)}")

    print("\ndownloading ~2y history for the whole universe...")
    px = yf.download(syms, start="2024-07-01", end="2026-08-07", progress=False,
                     auto_adjust=True, group_by="ticker", threads=True)

    cache = {}
    for s in syms:
        try:
            df = px[s].dropna()
        except Exception:
            continue
        if len(df) < PCT_WIN + BB_N + max(HORIZONS):
            continue
        bw, pc = bw_pctile_series(df["Close"])
        df = df.assign(bw_pctile=pc)
        cache[s] = df
    print(f"usable price histories: {len(cache)} of {len(syms)}")

    # ---------------- ARM 1: all-detector flags ----------------
    rows = []
    excl = {}
    for (sym, src), fdate in flags.items():
        df = cache.get(sym)
        if df is None:
            excl[(sym, src)] = "no/short history"; continue
        idx = df.index[df.index <= pd.Timestamp(fdate)]
        if len(idx) == 0:
            excl[(sym, src)] = "flag predates history"; continue
        pos = df.index.get_loc(idx[-1])
        p = df["bw_pctile"].iloc[pos]
        if pd.isna(p):
            excl[(sym, src)] = "band width not computable"; continue
        c0 = float(df["Close"].iloc[pos])
        rec = {"sym": sym, "src": src, "flag": fdate, "bw": round(float(p)),
               "bucket": bucket(float(p))}
        got = False
        for h in HORIZONS:
            if pos + h < len(df):
                rec[f"fwd{h}"] = round((float(df["Close"].iloc[pos + h]) / c0 - 1) * 100, 2)
                got = True
        if not got:
            excl[(sym, src)] = "no forward data"; continue
        rows.append(rec)

    print(f"\n{'='*78}\nARM 1 — ALL-DETECTOR FLAGS: {len(rows)} graded, {len(excl)} excluded\n{'='*78}")
    for h in HORIZONS:
        g = [r for r in rows if f"fwd{h}" in r]
        if not g:
            continue
        print(f"\n--- horizon +{h} sessions (n={len(g)}) ---")
        for b in ("COILED", "MIDDLE", "EXPANDED"):
            sub = [r[f"fwd{h}"] for r in g if r["bucket"] == b]
            if not sub:
                print(f"  {b:<9} n=0"); continue
            wins = sum(1 for x in sub if x >= WIN_HI)
            print(f"  {b:<9} n={len(sub):<5} mean {st.mean(sub):>6.2f}%  "
                  f"median {st.median(sub):>6.2f}%  "
                  f">= +{WIN_HI:.0f}%: {wins}/{len(sub)} ({100*wins/len(sub):.0f}%)  "
                  f"win rate {100*sum(1 for x in sub if x>0)/len(sub):.0f}%")
        w = [r for r in g if r[f"fwd{h}"] >= WIN_HI]
        d = [r for r in g if r[f"fwd{h}"] < DUD_HI]
        if w and d:
            print(f"  >>> RUNNERS (n={len(w)}) median band width "
                  f"{st.median([r['bw'] for r in w]):.0f}th  |  "
                  f"DUDS (n={len(d)}) median {st.median([r['bw'] for r in d]):.0f}th")

    print("\n--- by detector, horizon +21 (does any source's coil label pay?) ---")
    for src in sorted(by_src):
        g = [r for r in rows if r["src"] == src and "fwd21" in r]
        if len(g) < 8:
            continue
        c = [r["fwd21"] for r in g if r["bucket"] == "COILED"]
        e = [r["fwd21"] for r in g if r["bucket"] == "EXPANDED"]
        m = [r["fwd21"] for r in g if r["bucket"] == "MIDDLE"]
        f = lambda x: f"{st.mean(x):+6.2f}% (n={len(x)})" if x else "     n=0"
        print(f"  {src:<22} ALL {st.mean([r['fwd21'] for r in g]):+6.2f}% (n={len(g):<4})"
              f" | COILED {f(c)} | MIDDLE {f(m)} | EXPANDED {f(e)}")

    # ---------------- ARM 2: history, all names, every 5th session ----------------
    hist = []
    for s, df in cache.items():
        cl = df["Close"].values
        pc = df["bw_pctile"].values
        for i in range(PCT_WIN + BB_N, len(df) - 21, 5):
            p = pc[i]
            if pd.isna(p):
                continue
            hist.append((float(p), (cl[i + 21] / cl[i] - 1) * 100))
    print(f"\n{'='*78}\nARM 2 — HISTORY ARM (not 'our flags'): {len(hist):,} observations, "
          f"{len(cache)} names, ~2 years, forward 21 sessions\n{'='*78}")
    for lo, hi, lab in [(0, 10, "0-10th   (extreme coil)"), (11, 25, "11-25th  (coiled)"),
                        (26, 59, "26-59th  (middle)"), (60, 89, "60-89th  (expanded)"),
                        (90, 100, "90-100th (blown out)")]:
        sub = [r for p, r in hist if lo <= p <= hi]
        if not sub:
            continue
        big = sum(1 for x in sub if x >= WIN_HI)
        print(f"  {lab:<24} n={len(sub):>6,}  mean {st.mean(sub):>6.2f}%  "
              f"median {st.median(sub):>6.2f}%  >= +{WIN_HI:.0f}%: {100*big/len(sub):>4.1f}%  "
              f"win rate {100*sum(1 for x in sub if x>0)/len(sub):.0f}%")
    allr = [r for _, r in hist]
    print(f"  {'UNIVERSE BASELINE':<24} n={len(allr):>6,}  mean {st.mean(allr):>6.2f}%  "
          f"median {st.median(allr):>6.2f}%  >= +{WIN_HI:.0f}%: "
          f"{100*sum(1 for x in allr if x>=WIN_HI)/len(allr):>4.1f}%")

    out = REPO / "research" / "winner-dna-bandwidth-v2.json"
    out.write_text(json.dumps({"flags": rows,
                               "excluded": {f"{k[0]}|{k[1]}": v for k, v in excl.items()},
                               "history_n": len(hist)}, indent=1))
    print(f"\nwrote {out.name}")


if __name__ == "__main__":
    main()
