"""Account-level portfolio study (firehose + sizing). Pre-registered 2026-07-26.

Read research/portfolio-study-preregistration.md FIRST. Grid, mechanics,
primary config (N=8 / FIFO / FLAT), benchmark and every conclusion band were
committed before this file existed.

Simulates running the satellite book for real: N slots x $100k committed,
signals compete for free slots daily, one position per name, entries at the
signal-day close, exits per the intended forward rule (5% stop with
gap-through fills -> 20% ratchet once earned -> 120d cap), 10bp round trip.
Benchmark: SPY bought with the same committed capital and held.

Usage: python scripts/portfolio_study.py
"""
import json
import os
import sys
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_stack import evaluate, MissingGateData, DEFAULT_POSITION  # noqa: E402
from historical_replay import build_features, FRESH_BARS  # noqa: E402
from sector_vs_stockpicking import SECTORS, load_all, START, END  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STOP_FRAC, RATCHET, MAXH, COST_FRAC = 0.05, 0.80, 120, 0.0010
SLOT_CAP = 100_000.0
SLOTS = [4, 8, 16]
SELECTS = ["FIFO", "LIQ", "EXT"]
SIZINGS = ["FLAT", "VOL"]
PRIMARY = (8, "FIFO", "FLAT")
YEARS = ["2021", "2022", "2023", "2024", "2025"]


def harvest(px):
    """Signals + per-symbol bar arrays, identical entry logic to prior studies."""
    bars, by_day = {}, defaultdict(list)
    n_sig = 0
    for sector, (etf, names) in SECTORS.items():
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
            bars[s] = {"dates": list(f.index),
                       "o": df["Open"].reindex(f.index).to_numpy(dtype=float),
                       "h": f["high"].to_numpy(), "l": f["low"].to_numpy(),
                       "c": f["raw_close"].to_numpy()}
            for i, d in enumerate(f.index):
                if not (START <= d <= END) or not (0 <= since[i] <= FRESH_BARS):
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
                entry = bars[s]["c"][i]
                atr_pct = (r["atr"] / r["last"] * 100) if r["atr"] else None
                if not (np.isfinite(entry) and entry > 0 and atr_pct
                        and np.isfinite(bars[s]["o"][i])):
                    continue
                by_day[d].append({"sym": s, "i": i, "adv": float(r["avg_dollar_vol"]),
                                  "pct200": float(r["pct_vs_200"]), "atr_pct": atr_pct})
                n_sig += 1
        print(f"  {sector:16s} signals so far {n_sig}", flush=True)
    return bars, by_day, n_sig


def run_config(nslots, select, sizing, cal, bars, by_day):
    committed = nslots * SLOT_CAP
    cash, positions = committed, {}
    curve, wins, losses, taken, offered = [], 0, 0, 0, 0
    exposure_sum = 0.0
    for d in cal:
        # 1. exits - advance each position through every bar up to and incl. day d
        #    (a halted/skipped bar must not freeze the position forever)
        for sym in list(positions):
            p = positions[sym]
            dates = bars[sym]["dates"]
            while sym in positions and p["last_idx"] + 1 < len(dates) \
                    and dates[p["last_idx"] + 1] <= d:
                idx = p["last_idx"] + 1
                o, l, c = bars[sym]["o"][idx], bars[sym]["l"][idx], bars[sym]["c"][idx]
                p["last_idx"] = idx
                trail = RATCHET * p["peak"]
                exit_px = None
                if trail > p["stop"]:
                    if c < trail:
                        exit_px = c
                else:
                    if o <= p["stop"]:
                        exit_px = o         # gap-through fills at the open
                    elif l <= p["stop"]:
                        exit_px = p["stop"]
                p["days"] += 1
                if exit_px is None and p["days"] >= MAXH:
                    exit_px = c             # 120d cap
                if exit_px is not None:
                    cash += p["shares"] * exit_px - p["notional"] * COST_FRAC
                    if exit_px > p["entry"]:
                        wins += 1
                    else:
                        losses += 1
                    del positions[sym]
                else:
                    p["peak"] = max(p["peak"], c)
                    p["mark"] = c
        # 2. new signals at today's close
        sigs = [s for s in by_day.get(d, []) if s["sym"] not in positions]
        offered += len(sigs)
        if select == "LIQ":
            sigs.sort(key=lambda s: -s["adv"])
        elif select == "EXT":
            sigs.sort(key=lambda s: s["pct200"])
        else:
            sigs.sort(key=lambda s: s["sym"])
        for s in sigs:
            if len(positions) >= nslots:
                break
            want = (SLOT_CAP if sizing == "FLAT"
                    else min(max(SLOT_CAP * 2.5 / s["atr_pct"], 50_000.0), 150_000.0))
            avail = min(want, cash)
            if avail < (100_000.0 if sizing == "FLAT" else 25_000.0):
                continue
            entry = bars[s["sym"]]["c"][s["i"]]
            shares = avail / entry
            positions[s["sym"]] = {"entry": entry, "shares": shares, "notional": avail,
                                   "stop": entry * (1 - STOP_FRAC), "peak": entry,
                                   "mark": entry, "days": 0, "last_idx": s["i"]}
            cash -= avail
            taken += 1
        equity = cash + sum(p["shares"] * p["mark"] for p in positions.values())
        exposure_sum += (committed - cash) / committed if committed else 0
        curve.append((d, equity))
    eq = np.array([e for _, e in curve])
    peak = np.maximum.accumulate(eq)
    maxdd = float(((eq - peak) / peak).min() * 100)
    total = (eq[-1] / committed - 1) * 100
    yrs = len(cal) / 252.0
    by_year = {}
    for y in YEARS:
        idxs = [k for k, (d, _) in enumerate(curve) if d[:4] == y]
        if idxs:
            a = eq[idxs[0] - 1] if idxs[0] > 0 else committed
            by_year[y] = round((eq[idxs[-1]] / a - 1) * 100, 2)
    return {"total_pct": round(total, 2),
            "cagr": round(((eq[-1] / committed) ** (1 / yrs) - 1) * 100, 2),
            "maxdd_pct": round(maxdd, 2), "trades": taken, "offered": offered,
            "win_pct": round(100 * wins / max(wins + losses, 1), 1),
            "avg_exposure": round(100 * exposure_sum / len(cal), 1),
            "final": round(float(eq[-1]), 0), "by_year": by_year}


def main():
    px = load_all()
    bars, by_day, n_sig = harvest(px)
    spy = px["SPY"]["Close"]
    cal = [str(d)[:10] for d in spy.index if "2021-01-01" <= str(d)[:10] <= "2026-01-09"]
    cal = [d for d in cal]
    print(f"{n_sig} signals over {len(cal)} trading days")

    sdates = [str(x)[:10] for x in spy.index]
    spy_arr = np.array([float(v) for d, v in zip(sdates, spy.to_numpy(dtype=float))
                        if cal[0] <= d <= cal[-1]])
    speak = np.maximum.accumulate(spy_arr)
    spy_bench = {"total_pct": round((spy_arr[-1] / spy_arr[0] - 1) * 100, 2),
                 "maxdd_pct": round(float(((spy_arr - speak) / speak).min() * 100), 2)}

    results = {}
    for n in SLOTS:
        for sel in SELECTS:
            for siz in SIZINGS:
                key = f"N{n}/{sel}/{siz}"
                results[key] = run_config(n, sel, siz, cal, bars, by_day)
                print(f"  {key:14s} total {results[key]['total_pct']:+7.1f}%  "
                      f"maxDD {results[key]['maxdd_pct']:+6.1f}%  "
                      f"trades {results[key]['trades']:4d}  "
                      f"win {results[key]['win_pct']:4.1f}%  "
                      f"expo {results[key]['avg_exposure']:4.1f}%", flush=True)

    prim = results[f"N{PRIMARY[0]}/{PRIMARY[1]}/{PRIMARY[2]}"]
    out = {"spy": spy_bench, "primary": f"N{PRIMARY[0]}/{PRIMARY[1]}/{PRIMARY[2]}",
           "configs": results}
    json.dump(out, open(os.path.join(REPO, "research", "portfolio-study.json"), "w"), indent=1)

    print(f"\nSPY same-capital benchmark: total {spy_bench['total_pct']:+.1f}%  "
          f"maxDD {spy_bench['maxdd_pct']:+.1f}%")
    print(f"PRIMARY (pre-registered) {out['primary']}: total {prim['total_pct']:+.1f}% "
          f"(final ${prim['final']:,.0f} on ${PRIMARY[0]*SLOT_CAP:,.0f}), "
          f"maxDD {prim['maxdd_pct']:+.1f}%, by year {prim['by_year']}")
    print("wrote research/portfolio-study.json")


if __name__ == "__main__":
    main()
