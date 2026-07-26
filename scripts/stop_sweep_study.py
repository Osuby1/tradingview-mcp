"""Initial-stop sweep under the live 7/25 exit rule. Pre-registered 2026-07-26.

Read research/stop-sweep-preregistration.md FIRST. Grid, fill model, primary
metric (dollar expectancy under Omar's real sizing) and the selection rule were
committed before this file existed.

Rule simulated: hold with a static initial stop; once 0.8 x highest close
exceeds it, the close-based 20% ratchet governs (exit = max(stop, 0.8 x high));
120-trading-day cap. Only the initial stop distance varies:

  pct stops  2,3,4,5,6,8,10,12,15,20  (% below entry, intraday fills,
                                       gap-through fills at the OPEN)
  CE1x       the entry-day Chandelier distance = the pre-7/25 live stop
  NOSTOP     ratchet-only (the 20% line governs from entry)

Sizing per signal: notional = min($100k, $5k / stop-distance); NOSTOP at $100k.

Usage: python scripts/stop_sweep_study.py
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_stack import evaluate, MissingGateData, DEFAULT_POSITION  # noqa: E402
from historical_replay import build_features, FRESH_BARS  # noqa: E402
from sector_vs_stockpicking import SECTORS, load_all, START, END  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAXH = 120
RATCHET = 0.80
COST_PT = 0.10
MAX_NOTIONAL, RISK_DOLLARS = 100_000.0, 5_000.0
PCT_GRID = [2, 3, 4, 5, 6, 8, 10, 12, 15, 20]
AXIS = [str(p) for p in PCT_GRID] + ["NOSTOP"]   # ordered axis for the argmax rule
RULES = AXIS + ["CE1x"]                          # CE1x = incumbent baseline, off-axis
YEARS = ["2021", "2022", "2023", "2024", "2025"]


def simulate(i, o, h, l, c, stop_frac):
    """One signal, one stop rule -> (ret_pct, exit_kind, days, dd_pct)."""
    n = len(c)
    entry = c[i]
    end = min(i + MAXH, n - 1)
    stop_price = entry * (1 - stop_frac) if stop_frac else None
    peak = entry
    exit_px, exit_i, kind = c[end], end, "TIME"
    for j in range(i + 1, end + 1):
        trail = RATCHET * peak
        if stop_price is None or trail > stop_price:
            if c[j] < trail:
                exit_px, exit_i, kind = c[j], j, "TRAIL"
                break
        else:
            if o[j] <= stop_price:
                exit_px, exit_i, kind = o[j], j, "GAP"     # gap-through: fill at open
                break
            if l[j] <= stop_price:
                exit_px, exit_i, kind = stop_price, j, "STOP"
                break
        peak = max(peak, c[j])
    trough = np.nanmin(c[i:exit_i + 1])
    return ((exit_px / entry - 1) * 100, kind, exit_i - i, (trough / entry - 1) * 100)


def main():
    px = load_all()
    rows = []
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
            c = f["raw_close"].to_numpy()
            o = df["Open"].reindex(f.index).to_numpy(dtype=float)
            h = f["high"].to_numpy()
            l = f["low"].to_numpy()
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
                entry = c[i]
                ce_frac = (r["last"] - r["long_stop"]) / r["last"]
                if not (np.isfinite(entry) and entry > 0 and np.isfinite(ce_frac)
                        and ce_frac > 0 and np.isfinite(o[i])):
                    continue
                rec = {"sym": s, "date": d, "year": d[:4]}
                for rule in RULES:
                    frac = (None if rule == "NOSTOP"
                            else ce_frac if rule == "CE1x" else int(rule) / 100.0)
                    ret, kind, days, dd = simulate(i, o, h, l, c, frac)
                    notional = (MAX_NOTIONAL if frac is None
                                else min(MAX_NOTIONAL, RISK_DOLLARS / frac))
                    rec[rule] = {"ret": round(ret, 3), "kind": kind, "days": days,
                                 "dd": round(dd, 3),
                                 "pnl": round(notional * (ret - COST_PT) / 100, 0),
                                 "dd_usd": round(notional * dd / 100, 0),
                                 "r": round(ret / (frac * 100), 3) if frac else None}
                rows.append(rec)
        print(f"  {sector:16s} signals so far {len(rows)}", flush=True)

    def stats(rs, rule):
        if not rs:
            return None
        g = [r[rule] for r in rs]
        pnl = np.array([x["pnl"] for x in g])
        ret = np.array([x["ret"] for x in g])
        dd = np.array([x["dd_usd"] for x in g])
        kinds = {}
        for x in g:
            kinds[x["kind"]] = kinds.get(x["kind"], 0) + 1
        rvals = [x["r"] for x in g if x["r"] is not None]
        return {"n": len(g), "mean_usd": round(float(pnl.mean()), 0),
                "median_usd": round(float(np.median(pnl)), 0),
                "mean_pct": round(float(ret.mean()), 2),
                "hit": round(float(100 * (ret > 0).mean()), 1),
                "mean_R": round(float(np.mean(rvals)), 3) if rvals else None,
                "mean_dd_usd": round(float(dd.mean()), 0),
                "stopped_pct": round(100 * (kinds.get("STOP", 0) + kinds.get("GAP", 0)) / len(g), 1),
                "mean_days": round(float(np.mean([x["days"] for x in g])), 1),
                "exits": {k: round(100 * v / len(g), 1) for k, v in sorted(kinds.items())}}

    import datetime as dt
    last, dedup = {}, []
    for r in sorted(rows, key=lambda r: (r["sym"], r["date"])):
        t = dt.date.fromisoformat(r["date"])
        if r["sym"] in last and (t - last[r["sym"]]).days < 30:
            continue
        last[r["sym"]] = t
        dedup.append(r)

    syms = sorted({r["sym"] for r in rows})
    parity = {s: k % 2 for k, s in enumerate(syms)}
    splits = {"odd": [r for r in rows if parity[r["sym"]] == 1],
              "even": [r for r in rows if parity[r["sym"]] == 0],
              "y2123": [r for r in rows if r["year"] <= "2023"],
              "y2425": [r for r in rows if r["year"] >= "2024"]}

    def argmax_axis(rs):
        vals = {ru: stats(rs, ru)["mean_usd"] for ru in AXIS}
        best = max(vals, key=vals.get)
        return best, vals

    summary = {"n": len(rows),
               "overall": {ru: stats(rows, ru) for ru in RULES},
               "by_year": {y: {ru: stats([r for r in rows if r["year"] == y], ru)
                               for ru in RULES} for y in YEARS},
               "dedup_n": len(dedup),
               "dedup": {ru: stats(dedup, ru) for ru in RULES}}
    full_best, full_vals = argmax_axis(rows)
    stability = {"full": full_best}
    idx = {ru: k for k, ru in enumerate(AXIS)}
    stable = True
    for name, rs in splits.items():
        b, _ = argmax_axis(rs)
        stability[name] = b
        if abs(idx[b] - idx[full_best]) > 1:
            stable = False
    summary["stability"] = {**stability, "stable_within_1_step": stable}

    json.dump({"summary": summary},
              open(os.path.join(REPO, "research", "stop-sweep.json"), "w"), indent=1)

    print(f"\n{'='*84}\nSTOP SWEEP — {len(rows)} signals, live hybrid rule, "
          f"gap-through fills, sized min($100k, $5k/stop)\n{'='*84}")
    print(f"{'stop':7s}{'mean$':>9s}{'med$':>8s}{'mean%':>8s}{'hit%':>7s}"
          f"{'meanR':>7s}{'DD$':>9s}{'stp%':>7s}{'days':>7s}")
    for ru in RULES:
        s = summary["overall"][ru]
        rr = f"{s['mean_R']:.3f}" if s["mean_R"] is not None else "  -  "
        print(f"{ru:7s}{s['mean_usd']:>+9,.0f}{s['median_usd']:>+8,.0f}"
              f"{s['mean_pct']:>+8.2f}{s['hit']:>7.1f}{rr:>7s}"
              f"{s['mean_dd_usd']:>+9,.0f}{s['stopped_pct']:>7.1f}{s['mean_days']:>7.1f}")
    print("\nBY YEAR mean$ per signal:")
    print("  year " + "".join(f"{ru:>9s}" for ru in RULES))
    for y in YEARS:
        print(f"  {y} " + "".join(
            f"{summary['by_year'][y][ru]['mean_usd']:>+9,.0f}" for ru in RULES))
    print(f"\nARGMAX on the pre-registered axis: {summary['stability']}")
    print("wrote research/stop-sweep.json")


if __name__ == "__main__":
    main()
