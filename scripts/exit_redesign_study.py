"""Exit redesign study. Pre-registered 2026-07-25.

Read research/exit-redesign-preregistration.md FIRST. The rules, universe,
metrics, success bar and every conclusion were committed to git BEFORE this
file existed. Nothing here may be tuned after a result is seen.

Entries are held constant — the exact gate-passing fresh BUY signals of
sector_vs_stockpicking.py (imported, not re-implemented). Only the exit varies:

  A     live rule: static entry stop + 2:1 target, 21d max (as the Jan-Jun replay)
  B     same static stop, NO target, 120d max
  C     classic Chandelier trail: highest close - 3*ATR(22) raw, ratchet, 120d
  D     20% ratchet below highest close, 120d
  P21   pure hold 21 days   (comparator for A)
  P120  pure hold 120 days  (comparator for B/C/D)

All fills at REAL prices. Entry at the signal day's real close.

Usage: python scripts/exit_redesign_study.py
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_stack import evaluate, MissingGateData, DEFAULT_POSITION  # noqa: E402
from historical_replay import build_features, true_range, FRESH_BARS  # noqa: E402
from sector_vs_stockpicking import SECTORS, load_all, START, END  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES = ["A", "B", "C", "D", "P21", "P120"]
MAXH, H_A = 120, 21
ATR_PER, ATR_MULT = 22, 3.0     # rule C, frozen
RATCHET = 0.80                  # rule D, frozen
COST_PT = 0.10                  # round-trip cost, reported
YEARS = ["2021", "2022", "2023", "2024", "2025"]


def simulate(i, close, high, low, atr22, stop_pct):
    """Return {rule: (ret_pct, exit_i, exit_kind, worst_dd_pct)} for one signal."""
    n = len(close)
    entry = close[i]
    out = {}

    def grade(exit_px, exit_i, kind):
        trough = np.nanmin(close[i:exit_i + 1])
        return (round((exit_px / entry - 1) * 100, 3), int(exit_i), kind,
                round((trough / entry - 1) * 100, 3))

    real_stop = entry * (1 - stop_pct)
    target = entry * (1 + 2 * stop_pct)

    # A - live: static stop + 2:1 target, intraday fills, 21d
    end = min(i + H_A, n - 1)
    hit = None
    for j in range(i + 1, end + 1):
        if low[j] <= real_stop:
            hit = (real_stop, j, "STOP")
            break
        if high[j] >= target:
            hit = (target, j, "TARGET")
            break
    out["A"] = grade(*(hit or (close[end], end, "TIME")))

    # B - static stop, no target, 120d
    end = min(i + MAXH, n - 1)
    hit = None
    for j in range(i + 1, end + 1):
        if low[j] <= real_stop:
            hit = (real_stop, j, "STOP")
            break
    out["B"] = grade(*(hit or (close[end], end, "TIME")))

    # C / D - close-based ratcheting trails, no target, 120d
    for rule, init, upd in (
        ("C", lambda pk, j: pk - ATR_MULT * atr22[j], lambda pk, j: pk - ATR_MULT * atr22[j]),
        ("D", lambda pk, j: RATCHET * pk, lambda pk, j: RATCHET * pk),
    ):
        peak, trail = entry, init(entry, i)
        hit = None
        for j in range(i + 1, end + 1):
            if close[j] < trail:               # trail established through j-1
                hit = (close[j], j, "TRAIL")
                break
            peak = max(peak, close[j])
            trail = max(trail, upd(peak, j))   # ratchet: never down
        out[rule] = grade(*(hit or (close[end], end, "TIME")))

    out["P21"] = grade(close[min(i + H_A, n - 1)], min(i + H_A, n - 1), "TIME")
    out["P120"] = grade(close[end], end, "TIME")
    return out


def main():
    px = load_all()
    rows, skipped_stop = [], 0
    for sector, (etf, names) in SECTORS.items():
        for s in names:
            df = px.get(s)
            if df is None:
                continue
            try:
                f = build_features(df, regime_on_ha=True)
            except Exception:
                continue
            atr22 = true_range(df["High"], df["Low"], df["Close"]).shift(1) \
                .rolling(ATR_PER).mean().to_numpy()
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
            close = f["raw_close"].to_numpy()
            high = f["high"].to_numpy()
            low = f["low"].to_numpy()
            for i, d in enumerate(f.index):
                if not (START <= d <= END):
                    continue
                if not (0 <= since[i] <= FRESH_BARS):
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
                entry = close[i]
                stop_pct = (r["last"] - r["long_stop"]) / r["last"]
                if not (np.isfinite(entry) and entry > 0 and np.isfinite(stop_pct)
                        and stop_pct > 0 and np.isfinite(atr22[i])):
                    skipped_stop += 1          # skipped for ALL rules: sample stays identical
                    continue
                rec = {"sector": sector, "sym": s, "date": d, "year": d[:4]}
                for rule, (ret, ei, kind, dd) in simulate(i, close, high, low, atr22, stop_pct).items():
                    rec[rule] = ret
                    rec[f"{rule}_days"] = ei - i
                    rec[f"{rule}_kind"] = kind
                    rec[f"{rule}_dd"] = dd
                rows.append(rec)
        print(f"  {sector:16s} signals so far {len(rows)}", flush=True)

    if not rows:
        raise SystemExit("no signals")

    def stats(rs, rule):
        v = np.array([r[rule] for r in rs])
        dd = np.array([r[f"{rule}_dd"] for r in rs])
        days = np.array([r[f"{rule}_days"] for r in rs])
        kinds = {}
        for r in rs:
            kinds[r[f"{rule}_kind"]] = kinds.get(r[f"{rule}_kind"], 0) + 1
        return {"n": len(v), "mean": round(float(v.mean()), 2),
                "net_mean": round(float(v.mean()) - COST_PT, 2),
                "median": round(float(np.median(v)), 2),
                "hit": round(float(100 * (v > 0).mean()), 1),
                "mean_dd": round(float(dd.mean()), 2),
                "worst": round(float(v.min()), 2),
                "mean_days": round(float(days.mean()), 1),
                "exits": {k: round(100 * c / len(rs), 1) for k, c in sorted(kinds.items())}}

    # dedup cut: first signal per name per 30 calendar days
    import datetime as dt
    last_kept, dedup = {}, []
    for r in sorted(rows, key=lambda r: (r["sym"], r["date"])):
        t = dt.date.fromisoformat(r["date"])
        if r["sym"] in last_kept and (t - last_kept[r["sym"]]).days < 30:
            continue
        last_kept[r["sym"]] = t
        dedup.append(r)

    syms = sorted({r["sym"] for r in rows})
    parity = {s: k % 2 for k, s in enumerate(syms)}
    halves = {"odd": [r for r in rows if parity[r["sym"]] == 1],
              "even": [r for r in rows if parity[r["sym"]] == 0]}

    summary = {"n_signals": len(rows), "skipped_no_stop_or_atr": skipped_stop,
               "overall": {ru: stats(rows, ru) for ru in RULES},
               "by_year": {y: {ru: stats([r for r in rows if r["year"] == y], ru)
                               for ru in RULES} for y in YEARS},
               "dedup": {ru: stats(dedup, ru) for ru in RULES},
               "dedup_n": len(dedup),
               "halves": {h: {ru: stats(rs, ru) for ru in RULES}
                          for h, rs in halves.items()}}

    # ---- pre-registered criteria, evaluated mechanically ----
    verdicts = {}
    for ch in ["B", "C", "D"]:
        o, p, a = summary["overall"][ch], summary["overall"]["P120"], summary["overall"]["A"]
        y22c = summary["by_year"]["2022"][ch]["mean"]
        y22p = summary["by_year"]["2022"]["P120"]["mean"]
        crit = {"c1_tail": o["mean"] >= p["mean"] - 1.0,
                "c2_drawdown": o["mean_dd"] >= p["mean_dd"] + 3.0,
                "c3_2022": y22c >= y22p + 1.0,
                "c4_beats_A": o["mean"] >= a["mean"] + 2.0}
        robust = all(
            summary["halves"][h][ch]["mean"] >= summary["halves"][h]["P120"]["mean"] - 1.0
            and summary["by_year"]["2022"][ch]["mean"] >= y22p + 1.0  # 2022 not split: n too small per half; full-sample 2022 applies
            for h in halves)
        # per-half 2022 as declared:
        rob22 = all(
            stats([r for r in halves[h] if r["year"] == "2022"], ch)["mean"]
            >= stats([r for r in halves[h] if r["year"] == "2022"], "P120")["mean"] + 1.0
            for h in halves)
        verdicts[ch] = {"criteria": crit, "all_four": all(crit.values()),
                        "robust_c1": robust, "robust_c3_2022": rob22,
                        "PASS": all(crit.values()) and robust and rob22}

    json.dump({"rows": rows, "summary": summary, "verdicts": verdicts},
              open(os.path.join(REPO, "research", "exit-redesign.json"), "w"), indent=1)

    print(f"\n{'='*78}\nEXIT REDESIGN — {len(rows)} signals, 2021-2025 "
          f"(skipped {skipped_stop} lacking stop/ATR)\n{'='*78}")
    print(f"{'rule':6s}{'mean':>8s}{'median':>8s}{'hit%':>7s}{'meanDD':>8s}"
          f"{'worst':>8s}{'days':>7s}  exits")
    for ru in RULES:
        s = summary["overall"][ru]
        print(f"{ru:6s}{s['mean']:>+8.2f}{s['median']:>+8.2f}{s['hit']:>7.1f}"
              f"{s['mean_dd']:>+8.2f}{s['worst']:>+8.2f}{s['mean_days']:>7.1f}  {s['exits']}")
    print("\nBY YEAR (mean per rule):")
    hdr = "  year " + "".join(f"{ru:>9s}" for ru in RULES)
    print(hdr)
    for y in YEARS:
        line = f"  {y} " + "".join(f"{summary['by_year'][y][ru]['mean']:>+9.2f}" for ru in RULES)
        print(line + f"   n={summary['by_year'][y]['A']['n']}")
    print("\nPRE-REGISTERED VERDICTS:")
    for ch, v in verdicts.items():
        print(f"  {ch}: {v['criteria']}  robust_c1={v['robust_c1']} "
              f"robust_2022={v['robust_c3_2022']}  ==> {'PASS' if v['PASS'] else 'FAIL'}")
    print("\nwrote research/exit-redesign.json")


if __name__ == "__main__":
    main()
