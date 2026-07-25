"""ZLSMA scale-out study - semiconductors, 2025. Pre-registered 2026-07-25.

Read research/zlsma-exit-preregistration.md first. The method, the splits and the
bar to switch were committed to git before this file existed.

QUESTION (Omar's): price is above the ZLSMA; when it dips below, take 50% off,
then either reload on recovery or exit the rest some distance below the line.
What is that distance, and does the rule beat what we do today?

DESIGN NOTE: entries are held CONSTANT (same fresh Chandelier BUY + full gate
stack the live system runs). Only the exit varies, so any difference in outcome
is attributable to the exit rule and nothing else.

Usage: python scripts/zlsma_exit_study.py
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

# US-listed semiconductor + semi-equipment names. Fixed before any returns were
# examined (see the pre-registration).
SEMIS = [
    "NVDA", "AMD", "INTC", "MU", "AVGO", "QCOM", "TXN", "AMAT", "LRCX", "KLAC",
    "ADI", "MRVL", "NXPI", "ON", "MCHP", "SWKS", "QRVO", "TER", "ENTG", "MPWR",
    "ARM", "ASML", "TSM", "STX", "WDC", "HIMX", "NVTS", "ALGM", "AMKR", "COHR",
    "CRUS", "DIOD", "FORM", "LSCC", "OLED", "POWI", "RMBS", "SITM", "SLAB",
    "SYNA", "UCTT", "VECO", "WOLF", "AEIS", "ACLS", "CAMT", "NVMI", "SMTC",
    "ALAB", "CRDO", "MTSI", "INDI", "GFS", "QUIK", "SGH",
]
BENCH = "SOXX"
START, END = "2025-01-01", "2025-12-31"
WARMUP = "2023-09-01"          # runway for the 200-day regime test by Jan 2025
MAX_HOLD = 120
XS = [round(x, 3) for x in np.arange(0.0, 0.1501, 0.005)]   # 0% .. 15% below ZLSMA


def load():
    syms = SEMIS + [BENCH, "SPY"]
    d = yf.download(syms, start=WARMUP, end="2026-01-05", interval="1d",
                    group_by="ticker", auto_adjust=False, threads=True, progress=False)
    out = {}
    for s in syms:
        try:
            df = d[s].dropna(subset=["Close"])
            if len(df) > 300:
                df = df.copy()
                df.index = pd.Index([str(x)[:10] for x in df.index])
                out[s] = df
        except Exception:
            pass
    return out


def signals(px):
    """Fresh gate-passing BUY signals in 2025. Entries are held constant."""
    sigs = []
    for s in SEMIS:
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
        idx = list(f.index)
        for i, d in enumerate(idx):
            if not (START <= d <= END):
                continue
            if not (0 <= since[i] <= FRESH_BARS):
                continue
            row = f.iloc[i]
            gate = {"sym": s, "last": row["last"], "zlsma": row["zlsma"],
                    "regime": row["regime"], "adx": row["adx"],
                    "plus_di": row["plus_di"], "minus_di": row["minus_di"],
                    "avg_dollar_vol": row["avg_dollar_vol"], "atr": row["atr"],
                    "long_stop": row["long_stop"], "pct_vs_200": row["pct_vs_200"]}
            try:
                verdict, _, _ = evaluate(gate, position_size=DEFAULT_POSITION)
            except MissingGateData:
                continue
            if verdict.startswith("BLOCKED"):
                continue
            sigs.append({"sym": s, "date": d, "i": i, "half": "H1" if d < "2025-07-01" else "H2"})
    return sigs


def simulate(sig, f, rule, x=None):
    """Return the % result of one signal under one exit rule. Fills at REAL closes."""
    i = sig["i"]
    idx = list(f.index)
    end = min(i + MAX_HOLD, len(idx) - 1)
    if end <= i:
        return None
    rc = f["raw_close"].to_numpy()
    hi, lo = f["high"].to_numpy(), f["low"].to_numpy()
    ha_last, ha_stop = f["last"].to_numpy(), f["long_stop"].to_numpy()
    zl = f["zlsma"].to_numpy()
    ha_close = f["last"].to_numpy()
    entry = float(rc[i])
    if not np.isfinite(entry) or entry <= 0:
        return None

    if rule == "A":                      # live rule: Chandelier stop + 2:1 target
        if not (np.isfinite(ha_stop[i]) and ha_last[i] > ha_stop[i] > 0):
            return (float(rc[min(i + 21, end)]) / entry - 1) * 100
        pct = (ha_last[i] - ha_stop[i]) / ha_last[i]
        stop, tgt = entry * (1 - pct), entry * (1 + 2 * pct)
        cap = min(i + 21, end)
        for j in range(i + 1, cap + 1):
            if lo[j] <= stop:
                return (stop / entry - 1) * 100
            if hi[j] >= tgt:
                return (tgt / entry - 1) * 100
        return (float(rc[cap]) / entry - 1) * 100

    if rule == "B":
        return (float(rc[min(i + 21, end)]) / entry - 1) * 100
    if rule == "C":
        return (float(rc[end]) / entry - 1) * 100

    # D / E: 50% off on the first close below ZLSMA, remainder x% below the line.
    # ZLSMA is read on Heikin Ashi (the line Omar watches); fills are real closes.
    held, realised, scaled = 1.0, 0.0, False
    for j in range(i + 1, end + 1):
        if not np.isfinite(zl[j]):
            continue
        below = ha_close[j] < zl[j]
        if not scaled and below:
            realised += 0.5 * (float(rc[j]) / entry - 1) * 100
            held, scaled = 0.5, True
            continue
        if scaled:
            if ha_close[j] < zl[j] * (1 - x):                 # final exit
                return realised + held * (float(rc[j]) / entry - 1) * 100
            if rule == "E" and ha_close[j] > zl[j]:            # reload to full
                realised -= 0.5 * (float(rc[j]) / entry - 1) * 100
                held, scaled = 1.0, False
    return realised + held * (float(rc[end]) / entry - 1) * 100


def bench_return(px, d, days=21):
    b = px.get(BENCH)
    if b is None or d not in b.index:
        return None
    k = list(b.index).index(d)
    e = min(k + days, len(b) - 1)
    return (float(b["Close"].iloc[e]) / float(b["Close"].iloc[k]) - 1) * 100


def main():
    print("loading semiconductor history...", flush=True)
    px = load()
    print(f"  priced {len([s for s in SEMIS if s in px])}/{len(SEMIS)} semis", flush=True)
    feats = {}
    for s in SEMIS:
        if s in px:
            try:
                feats[s] = build_features(px[s], regime_on_ha=True)
            except Exception:
                pass
    sigs = signals(px)
    print(f"  {len(sigs)} gate-passing fresh BUY signals in 2025", flush=True)
    if not sigs:
        raise SystemExit("no signals - nothing to study")

    results = {"A": [], "B": [], "C": []}
    for s in sigs:
        f = feats[s["sym"]]
        for r in ("A", "B", "C"):
            v = simulate(s, f, r)
            if v is not None:
                results[r].append({**s, "ret": v})
    for rule in ("D", "E"):
        for x in XS:
            key = f"{rule}{x:.3f}"
            results[key] = []
            for s in sigs:
                v = simulate(s, feats[s["sym"]], rule, x)
                if v is not None:
                    results[key].append({**s, "ret": v})

    def mean(key, subset=None):
        rows = results[key]
        if subset:
            rows = [r for r in rows if subset(r)]
        return float(np.mean([r["ret"] for r in rows])) if rows else None

    out = {"n_signals": len(sigs), "xs": XS, "curve_D": [], "curve_E": [],
           "baselines": {k: mean(k) for k in ("A", "B", "C")}}
    for x in XS:
        out["curve_D"].append(mean(f"D{x:.3f}"))
        out["curve_E"].append(mean(f"E{x:.3f}"))

    # --- split-sample validation, both ways -------------------------------
    names = sorted({s["sym"] for s in sigs})
    odd = {n for i, n in enumerate(names) if i % 2 == 0}
    splits = {
        "calendar": (lambda r: r["half"] == "H1", lambda r: r["half"] == "H2", "H1", "H2"),
        "name": (lambda r: r["sym"] in odd, lambda r: r["sym"] not in odd, "odd", "even"),
    }
    out["splits"] = {}
    for label, (fa, fb, na, nb) in splits.items():
        rec = {}
        for rule in ("D", "E"):
            best_x, best_v = None, -1e9
            for x in XS:                              # optimise on side A only
                v = mean(f"{rule}{x:.3f}", fa)
                if v is not None and v > best_v:
                    best_x, best_v = x, v
            held = mean(f"{rule}{best_x:.3f}", fb)    # then test on side B
            rec[rule] = {"train": na, "test": nb, "best_x_in_sample": best_x,
                         "in_sample_mean": best_v, "held_out_mean": held,
                         "baseline_A_held_out": mean("A", fb),
                         "beats_A_by": (held - mean("A", fb)) if held is not None else None}
        out["splits"][label] = rec

    json.dump(out, open(os.path.join(REPO, "research", "zlsma-exit-study.json"), "w"), indent=1)

    # ---- console summary --------------------------------------------------
    print(f"\nBASELINES (mean % per signal, n={len(sigs)}):")
    print(f"  A  live rule (Chandelier stop + 2:1)   {out['baselines']['A']:+.2f}%")
    print(f"  B  pure 21-day hold                    {out['baselines']['B']:+.2f}%")
    print(f"  C  pure 120-day hold                   {out['baselines']['C']:+.2f}%")
    print("\nSWEEP - mean % by exit distance below ZLSMA:")
    print("   x     D (no reload)   E (with reload)")
    for k, x in enumerate(XS):
        d, e = out["curve_D"][k], out["curve_E"][k]
        print(f"  {x*100:4.1f}%   {d:+8.2f}%      {e:+8.2f}%")
    print("\nSPLIT-SAMPLE (optimise on one side, test on the other):")
    for label, rec in out["splits"].items():
        for rule, r in rec.items():
            print(f"  [{label:8s}] {rule}: best x on {r['train']} = {r['best_x_in_sample']*100:.1f}% "
                  f"(in-sample {r['in_sample_mean']:+.2f}%) -> held-out {r['test']} "
                  f"{r['held_out_mean']:+.2f}% vs live rule {r['baseline_A_held_out']:+.2f}% "
                  f"= {r['beats_A_by']:+.2f}pt")
    print("\nwrote research/zlsma-exit-study.json")


if __name__ == "__main__":
    main()
