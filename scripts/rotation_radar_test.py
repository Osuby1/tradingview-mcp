"""Does the rotation radar predict? Pre-registered 2026-07-25.

Read research/rotation-radar-preregistration.md first. Universe, thresholds,
horizons, sampling and the conclusion for every outcome were committed to git
before this file existed.

The radar's own formula and thresholds are imported/copied verbatim - nothing is
tuned. Reconstruction is VALIDATED against the live 2026-07-24 radar output
before any forward return is computed; a failed validation stops the test.

Usage:
    python scripts/rotation_radar_test.py --validate
    python scripts/rotation_radar_test.py --run
"""
import json
import os
import re
import sys

import numpy as np
import pandas as pd
import yfinance as yf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rotation_radar import UNIVERSE, classify  # the LIVE formula, unchanged

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START, END = "2021-01-01", "2025-12-31"
WARMUP = "2020-01-01"
W, M1, M6 = 5, 21, 126          # trading days for Perf.W / Perf.1M / Perf.6M
HORIZONS = [21, 60, 120]
PRIMARY = 60
SAMPLE_EVERY = 5                # weekly sampling, pre-declared primary
BENCH = "SPY"

TICKERS = {t.split(":")[1]: lab for t, (lab, _) in UNIVERSE.items()}
ETFS = [t for t in TICKERS if t != BENCH]


def load():
    syms = list(TICKERS)
    d = yf.download(syms, start=WARMUP, end="2026-07-26", interval="1d",
                    group_by="ticker", auto_adjust=False, threads=True, progress=False)
    out = {}
    for s in syms:
        try:
            df = d[s].dropna(subset=["Close"])
            if len(df) > 300:
                c = df["Close"].copy()
                c.index = pd.Index([str(x)[:10] for x in c.index])
                out[s] = c
        except Exception:
            pass
    return out


def perf_frame(px):
    """Perf.W / 1M / 6M / accel / rel1M per ETF per date, exactly as the radar defines."""
    frames = {}
    for s, c in px.items():
        f = pd.DataFrame(index=c.index)
        f["close"] = c
        f["w"] = c.pct_change(W) * 100
        f["m1"] = c.pct_change(M1) * 100
        f["m6"] = c.pct_change(M6) * 100
        f["accel"] = f["m1"] - f["m6"] / 6
        frames[s] = f
    spy = frames[BENCH]
    for s, f in frames.items():
        f["rel1m"] = f["m1"] - spy["m1"].reindex(f.index)
        f["state"] = [classify(a, r, w, m6) if not any(pd.isna(x) for x in (a, r, w, m6)) else None
                      for a, r, w, m6 in zip(f["accel"], f["rel1m"], f["w"], f["m6"])]
    return frames


def validate(frames):
    """Reproduce the live radar's 2026-07-24 output, or refuse to run the test."""
    path = os.path.join(REPO, "watchlists", "rotation-radar-state.md")
    txt = open(path, encoding="utf-8").read()
    live = {}
    for m in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*([A-Z]+)\s*\|\s*(\w+|-)\s*\|\s*([+-][\d.]+)\s*\|", txt, re.M):
        _, tk, state, accel = m.groups()
        live[tk] = (state, float(accel))
    if not live:
        print("could not parse the live radar state file - cannot validate")
        return False
    date = "2026-07-24"
    rows, ok_state, n = [], 0, 0
    for tk, (lstate, laccel) in sorted(live.items()):
        f = frames.get(tk)
        if f is None or date not in f.index:
            continue
        r = f.loc[date]
        if pd.isna(r["accel"]):
            continue
        n += 1
        match = (r["state"] == lstate) or (tk == BENCH)
        ok_state += match
        rows.append((tk, laccel, float(r["accel"]), lstate, r["state"], match))
    errs = [abs(a - b) for _, a, b, _, _, _ in rows]
    print(f"validating reconstruction against the live radar, {date} (n={n})")
    print(f"  accel  median abs err {np.median(errs):.2f}pt   90th {np.percentile(errs, 90):.2f}pt   max {max(errs):.2f}pt")
    print(f"  state  match {ok_state}/{n} = {100*ok_state/n:.0f}%")
    print("\n  worst accel mismatches:")
    for tk, a, b, ls, rs, _ in sorted(rows, key=lambda x: -abs(x[1] - x[2]))[:6]:
        print(f"    {tk:5s} live {a:+6.1f} vs rebuilt {b:+6.1f}   live state {ls:9s} rebuilt {rs}")
    passed = np.median(errs) < 2.0 and ok_state / n >= 0.75
    print(f"\n  VALIDATION {'PASSED' if passed else 'FAILED'} "
          f"(bar: median accel error < 2.0pt and state match >= 75%)")
    return passed


def run(frames):
    dates = [d for d in frames[BENCH].index if START <= d <= END]
    dates = dates[::SAMPLE_EVERY]
    spy = frames[BENCH]["close"]        # the close series, not the whole frame
    recs = []
    for d in dates:
        snap = []
        for s in ETFS:
            f = frames.get(s)
            if f is None or d not in f.index:
                continue
            r = f.loc[d]
            if r["state"] is None or pd.isna(r["accel"]):
                continue
            fwd = {}
            idx = list(f.index)
            k = idx.index(d)
            for h in HORIZONS:
                e = min(k + h, len(idx) - 1)
                fwd[h] = (float(f["close"].iloc[e]) / float(f["close"].iloc[k]) - 1) * 100 if e > k else None
            si = list(spy.index)
            sk = si.index(d) if d in spy.index else None
            sf = {}
            for h in HORIZONS:
                if sk is None:
                    sf[h] = None
                    continue
                se = min(sk + h, len(si) - 1)
                sf[h] = (float(spy.iloc[se]) / float(spy.iloc[sk]) - 1) * 100 if se > sk else None
            snap.append({"date": d, "year": d[:4], "etf": s, "state": r["state"],
                         "accel": float(r["accel"]), "m1": float(r["m1"]),
                         **{f"fwd_{h}": fwd[h] for h in HORIZONS},
                         **{f"spy_{h}": sf[h] for h in HORIZONS}})
        if not snap:
            continue
        # cross-sectional ranks for the IC and the momentum control
        for h in HORIZONS:
            vals = [x[f"fwd_{h}"] for x in snap]
            if any(v is None for v in vals):
                continue
            ra = pd.Series([x["accel"] for x in snap]).rank()
            rm = pd.Series([x["m1"] for x in snap]).rank()
            rf = pd.Series(vals).rank()
            for x in snap:
                x[f"ic_accel_{h}"] = float(ra.corr(rf))
                x[f"ic_mom_{h}"] = float(rm.corr(rf))
        recs += snap
    return recs


def summarise(recs):
    H = PRIMARY
    ok = [r for r in recs if r.get(f"fwd_{H}") is not None and r.get(f"spy_{H}") is not None]
    out = {"n_obs": len(ok), "primary": H}

    def st(rows, h):
        if not rows:
            return None
        f = np.array([r[f"fwd_{h}"] for r in rows])
        s = np.array([r[f"spy_{h}"] for r in rows])
        return {"n": len(f), "mean": round(float(f.mean()), 2),
                "vs_spy": round(float((f - s).mean()), 2),
                "win_vs_spy": round(float(100 * (f > s).mean()), 1)}

    allmean = {h: float(np.mean([r[f"fwd_{h}"] for r in recs if r.get(f"fwd_{h}") is not None]))
               for h in HORIZONS}
    out["equal_weight_all_sectors"] = {h: round(allmean[h], 2) for h in HORIZONS}
    out["by_state"] = {}
    for state in ("IGNITING", "WATCH", "NEUTRAL", "ROLLING"):
        rows = [r for r in ok if r["state"] == state]
        out["by_state"][state] = {h: st([r for r in recs if r["state"] == state
                                         and r.get(f"fwd_{h}") is not None], h) for h in HORIZONS}
    ics = {h: [r[f"ic_accel_{h}"] for r in recs if f"ic_accel_{h}" in r] for h in HORIZONS}
    icm = {h: [r[f"ic_mom_{h}"] for r in recs if f"ic_mom_{h}" in r] for h in HORIZONS}
    out["ic_accel"] = {h: round(float(np.mean(ics[h])), 4) for h in HORIZONS if ics[h]}
    out["ic_momentum"] = {h: round(float(np.mean(icm[h])), 4) for h in HORIZONS if icm[h]}
    out["by_year"] = {}
    for y in ("2021", "2022", "2023", "2024", "2025"):
        rows = [r for r in ok if r["year"] == y]
        ign = [r for r in rows if r["state"] == "IGNITING"]
        out["by_year"][y] = {"igniting": st(ign, H), "all": st(rows, H)}
    return out


def main():
    px = load()
    print(f"loaded {len(px)}/{len(TICKERS)} ETFs")
    frames = perf_frame(px)
    if "--validate" in sys.argv:
        validate(frames)
        return
    if not validate(frames):
        raise SystemExit("\nreconstruction did not validate - refusing to run the test "
                         "(per the pre-registration)")
    recs = run(frames)
    out = summarise(recs)
    json.dump({"summary": out, "n": len(recs)},
              open(os.path.join(REPO, "research", "rotation-radar-test.json"), "w"), indent=1)

    H = PRIMARY
    print(f"\n{'='*70}\nPRIMARY: {H} trading days, weekly sampling  (n={out['n_obs']} observations)\n{'='*70}")
    print(f"  equal-weight ALL sectors: {out['equal_weight_all_sectors'][H]:+.2f}%")
    print(f"\n  {'state':10s} {'n':>6s} {'fwd ret':>9s} {'vs SPY':>9s} {'beat SPY':>9s}")
    for state, d in out["by_state"].items():
        s = d[H]
        if not s:
            print(f"  {state:10s}      -")
            continue
        print(f"  {state:10s} {s['n']:6d} {s['mean']:+8.2f}% {s['vs_spy']:+8.2f}pt {s['win_vs_spy']:8.1f}%")
    ig, ro = out["by_state"]["IGNITING"][H], out["by_state"]["ROLLING"][H]
    if ig and ro:
        print(f"\n  IGNITING minus ROLLING: {ig['mean'] - ro['mean']:+.2f}pt")
    print(f"  IGNITING minus equal-weight-all: {ig['mean'] - out['equal_weight_all_sectors'][H]:+.2f}pt")
    print(f"\n  rank correlation accel vs forward return: {out['ic_accel'].get(H)}")
    print(f"  same for plain 1-month momentum:          {out['ic_momentum'].get(H)}")
    print("\n  other horizons (context only):")
    for h in HORIZONS:
        s = out["by_state"]["IGNITING"][h]
        if s:
            print(f"    {h:3d}d IGNITING {s['mean']:+6.2f}% vs SPY {s['vs_spy']:+6.2f}pt | "
                  f"IC accel {out['ic_accel'].get(h)} mom {out['ic_momentum'].get(h)}")
    print("\n  by year (IGNITING vs SPY), every year reported:")
    for y, d in out["by_year"].items():
        s = d["igniting"]
        print(f"    {y}  n={s['n']:4d}  {s['mean']:+6.2f}%  vs SPY {s['vs_spy']:+6.2f}pt" if s
              else f"    {y}  no IGNITING observations")
    print("\nwrote research/rotation-radar-test.json")


if __name__ == "__main__":
    main()
