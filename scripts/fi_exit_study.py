"""Fresh-Ignition exit search. Pre-registered 2026-07-26.

Read research/fi-exit-preregistration.md FIRST. Three mechanism-chosen exit
candidates on the SAME 1,512 A-grade Fresh Ignition entries, vs pure holds,
the live stop+ratchet, and Omar's original sell-on-Cooling. Entry generation
is imported from fresh_ignition_backtest.py so the episodes are identical.

Usage: python scripts/fi_exit_study.py
"""
import json
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fresh_ignition_backtest import (  # noqa: E402
    load_prices, features, score_and_tab, grade_of, TAB,
    START, END, COST_PT, YEARS)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAP = 250
RULES = ["E1_trendbreak", "E2_structure", "E3_cooling_plus_floor",
         "R1_cooling", "H60", "H120", "H250", "R4_stop_ratchet"]


def main():
    px = load_prices()
    spy = px.pop("SPY")
    cal = spy.index
    spy_c = spy["Close"]
    spy_arr = spy_c.to_numpy(dtype=float)
    dates = [str(d)[:10] for d in cal]
    i0 = next(i for i, d in enumerate(dates) if d >= START)
    i1 = max(i for i, d in enumerate(dates) if d <= END)

    feats = {}
    for k, (s, df) in enumerate(px.items()):
        try:
            feats[s] = features(df, spy_c, cal)
        except Exception:
            pass
        if (k + 1) % 200 == 0:
            print(f"  features {k + 1}/{len(px)}", flush=True)
    cap_rank = pd.DataFrame({s: f["atr_pct"] for s, f in feats.items()}).rank(axis=1, pct=True)

    trades = {r: [] for r in RULES}
    for s, f in feats.items():
        score, tab = score_and_tab(f, cap_rank[s].to_numpy(dtype=float))
        g = grade_of(score)
        cl = f["close"].to_numpy(dtype=float)
        op = f["open"].to_numpy(dtype=float)
        lo = f["low"].to_numpy(dtype=float)
        stage2 = f["stage2"].to_numpy(dtype=float)
        # scanner's pullback-zone FLOOR, on native bars then aligned to calendar
        nat = f["close"].dropna()
        ema20 = nat.ewm(span=20, adjust=False).mean()
        sma50 = nat.rolling(50).mean()
        pb_lo = pd.concat([ema20, sma50], axis=1).min(axis=1) \
            .reindex(f.index).to_numpy(dtype=float)

        fresh_a = (tab == TAB["FRESH"]) & (g == 3)
        prev = np.concatenate([[False], fresh_a[:-1]])
        last_exit = -1
        for i in np.where(fresh_a & ~prev)[0]:
            if not (i0 <= i <= i1) or i <= last_exit:
                continue
            entry = cl[i]
            if not (np.isfinite(entry) and entry > 0):
                continue
            end = min(i + CAP, len(cl) - 1)
            e_cool = e_trend = e_struct = end
            for j in range(i + 1, end + 1):
                if not np.isfinite(cl[j]):
                    continue
                if e_cool == end and tab[j] == TAB["COOLING"]:
                    e_cool = j
                if e_trend == end and stage2[j] == 0.0:
                    e_trend = j
                if e_struct == end and np.isfinite(pb_lo[j]) and cl[j] < pb_lo[j]:
                    e_struct = j
                if e_cool < end and e_trend < end and e_struct < end:
                    break
            # live stop+ratchet
            stop, peak, e4, px4 = entry * 0.95, entry, min(i + 120, len(cl) - 1), None
            for j in range(i + 1, min(i + 120, len(cl) - 1) + 1):
                if not np.isfinite(cl[j]):
                    continue
                trail = 0.80 * peak
                if trail > stop:
                    if cl[j] < trail:
                        e4, px4 = j, cl[j]
                        break
                else:
                    if np.isfinite(op[j]) and op[j] <= stop:
                        e4, px4 = j, op[j]
                        break
                    if np.isfinite(lo[j]) and lo[j] <= stop:
                        e4, px4 = j, stop
                        break
                peak = max(peak, cl[j])
            exits = {
                "E1_trendbreak": (e_trend, cl[e_trend]),
                "E2_structure": (e_struct, cl[e_struct]),
                "E3_cooling_plus_floor": ((m := min(e_cool, e_struct)), cl[m]),
                "R1_cooling": (e_cool, cl[e_cool]),
                "H60": ((h := min(i + 60, len(cl) - 1)), cl[h]),
                "H120": ((h2 := min(i + 120, len(cl) - 1)), cl[h2]),
                "H250": (end, cl[end]),
                "R4_stop_ratchet": (e4, px4 if px4 is not None else cl[e4]),
            }
            for rule, (ei, pxx) in exits.items():
                if not np.isfinite(pxx):
                    continue
                ret = (pxx / entry - 1) * 100 - COST_PT
                sp = (spy_arr[ei] / spy_arr[i] - 1) * 100
                trades[rule].append({"sym": s, "date": dates[i], "year": dates[i][:4],
                                     "ret": round(ret, 2), "exc": round(ret - sp, 2),
                                     "days": int(ei - i)})
            last_exit = e_cool

    def stats(rs):
        if not rs:
            return None
        e = np.array([r["exc"] for r in rs])
        return {"n": len(e), "mean_exc": round(float(e.mean()), 2),
                "median_exc": round(float(np.median(e)), 2),
                "hit": round(float(100 * (e > 0).mean()), 1),
                "worst": round(float(e.min()), 1),
                "mean_days": round(float(np.mean([x["days"] for x in rs])), 1)}

    syms_sorted = sorted({t["sym"] for t in trades["R1_cooling"]})
    par = {s: k % 2 for k, s in enumerate(syms_sorted)}
    summary = {"rules": {r: stats(v) for r, v in trades.items()},
               "by_year": {y: {r: stats([t for t in trades[r] if t["year"] == y])
                               for r in RULES} for y in YEARS},
               "halves": {h: {r: stats([t for t in trades[r] if par[t["sym"]] == p])
                              for r in RULES} for h, p in (("odd", 1), ("even", 0))}}

    best_hold = max(("H60", "H120", "H250"),
                    key=lambda r: summary["rules"][r]["mean_exc"])
    verdicts = {}
    for c in ("E1_trendbreak", "E2_structure", "E3_cooling_plus_floor"):
        s = summary["rules"][c]
        c1 = s["mean_exc"] >= summary["rules"][best_hold]["mean_exc"] + 1.0
        c2 = all(summary["halves"][h][c]["mean_exc"]
                 > summary["halves"][h]["R1_cooling"]["mean_exc"] for h in ("odd", "even"))
        y22c = summary["by_year"]["2022"][c]["mean_exc"]
        y22h = summary["by_year"]["2022"][best_hold]["mean_exc"]
        c3 = y22c >= y22h - 2.0
        verdicts[c] = {"c1_beats_best_hold_by_1pt": c1, "c2_beats_R1_both_halves": c2,
                       "c3_2022_ok": c3, "PASS": c1 and c2 and c3}
    summary["best_hold"] = best_hold
    summary["verdicts"] = verdicts

    json.dump({"summary": summary},
              open(os.path.join(REPO, "research", "fi-exit-study.json"), "w"), indent=1)

    print(f"\n{'='*80}\nFI EXIT SEARCH — {len(trades['R1_cooling'])} identical entries\n{'='*80}")
    for r in RULES:
        s = summary["rules"][r]
        print(f"  {r:22s} mean {s['mean_exc']:+6.2f}  med {s['median_exc']:+6.2f}  "
              f"hit {s['hit']:4.1f}%  worst {s['worst']:+7.1f}  days {s['mean_days']:5.1f}")
    print(f"\nbest pure hold: {best_hold}")
    for c, v in verdicts.items():
        print(f"  {c}: {v}")
    print("wrote research/fi-exit-study.json")


if __name__ == "__main__":
    main()
