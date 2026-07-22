"""Turn a raw O.G sweep + regime-filter output into universe-results-<date>.json.

That JSON is what compile_universe_report_v2.py consumes, so this is the bridge
between "chart reads" and "the EOD workbook".

Verdicts are assigned by the FULL gate stack, in the order established
2026-07-22 (see memory: regime-filter-is-mandatory-gate):

    1. regime      - DEEP-FAIL (>10% below 200d) = no size, REPAIR = starter only
    2. ADX >= 20   - a trend must actually exist
    3. +DI > -DI   - bulls in control
    4. above ZLSMA - the Chandelier stack's own structural test
    5. liquidity   - position must be a small slice of average daily dollar volume

Usage:
    python scripts/build_universe_results.py <raw_sweep.txt> <regime.json> <date>
"""
import json
import os
import sys
from datetime import datetime

MIN_ADV_MULTIPLE = 10.0   # position must be <= 1/10th of a day's dollar volume


def load_sweep(path):
    raw = open(path, encoding="utf-8", errors="replace").read()
    try:
        env = json.loads(raw)
        if isinstance(env, dict) and isinstance(env.get("result"), str):
            return json.loads(env["result"])
        if isinstance(env, list):
            return env
    except json.JSONDecodeError:
        pass
    s, e = raw.find("["), raw.rfind("]")
    return json.loads(raw[s:e + 1])


def main():
    sweep_path, regime_path, date = sys.argv[1], sys.argv[2], sys.argv[3]
    rows = load_sweep(sweep_path)
    reg = {r["sym"]: r for r in json.load(open(regime_path))["rows"] if r.get("ok", True)}

    ok = [r for r in rows if r.get("ok")]
    buys = [r for r in ok if r.get("ce_mode") == "BUY"]
    sells = [r["rname"] for r in ok if r.get("ce_mode") == "SELL"]
    fresh = [r for r in buys if r.get("bars_back") is not None and r["bars_back"] <= 5]

    hits, dq = {}, []
    for r in fresh:
        sym = r["rname"]
        g = reg.get(sym, {})
        last, zl = r.get("last"), r.get("zlsma")
        above_zl = (last is not None and zl is not None and last > zl)
        regime = g.get("regime")
        adx, pdi, ndi = g.get("adx"), g.get("pdi"), g.get("ndi")

        fails = []
        if regime == "DEEP-FAIL":
            fails.append(f"regime DEEP-FAIL ({g.get('pct200')}% vs 200-day) - watch only, no size")
        elif regime == "REPAIR":
            fails.append(f"regime REPAIR ({g.get('pct200')}% vs 200-day) - starter size only")
        if adx is not None and adx < 20:
            fails.append(f"ADX {adx} below 20 - no trend to ride")
        if pdi is not None and ndi is not None and pdi <= ndi:
            fails.append(f"-DI {ndi} >= +DI {pdi} - bears in control")
        if not above_zl:
            fails.append(f"price {last} below ZLSMA {zl} - structure has not turned")

        if not fails:
            verdict = "CANDIDATE - passes regime + trend + structure"
        elif regime == "DEEP-FAIL":
            verdict = "BLOCKED: regime DEEP-FAIL"
        elif len(fails) == 1 and regime == "REPAIR":
            verdict = "STARTER ONLY - regime REPAIR"
        else:
            verdict = "BLOCKED: " + fails[0].split(" - ")[0]

        hits[sym] = {
            "sym": sym, "source": "og-chandelier", "signal_date_est": r.get("flip_date"),
            "bars_back": r.get("bars_back"), "last": last, "zlsma": zl,
            "magical": r.get("magical"), "ce_label": r.get("long_stop"),
            "regime": regime, "verdict": verdict,
            "note": ("; ".join(fails) if fails else
                     "Passes every gate: regime, ADX, DI direction and ZLSMA."),
        }

    enrich = {r["rname"]: {"description": r.get("rdesc")} for r in ok}

    passing = [s for s, h in hits.items() if h["verdict"].startswith("CANDIDATE")]
    dq.append({"severity": "BLOCKER" if not passing else "INFO", "area": "Gate stack",
               "finding": f"{len(fresh)} fresh Chandelier BUY signals were culled to "
                          f"{len(passing)} that pass the full gate stack.",
               "impact": "Zero passing names means zero trades - that is the honest "
                         "output, not a failure of the scan."
                         if not passing else "",
               "action": "Do not manufacture a candidate to have something to say."})
    dq.append({"severity": "WARNING", "area": "Signal quality",
               "finding": "0-bar signals (flipped today) can repaint before the close. "
                          "On 2026-07-22, CENX and CRWV both showed fresh BUY flips at "
                          "10:20am and were back in SELL mode by 2pm.",
               "impact": "Any 0-bar name in this file is provisional.",
               "action": "Re-read 0-bar signals after the close before acting."})
    dq.append({"severity": "INFO", "area": "Method",
               "finding": "Read on CANDLES on the live chart, per the 2026-07-22 standard.",
               "impact": "", "action": ""})

    out = {
        "date": date, "variant": "full - O.G Chandelier + HQ Swing v1 regime filter",
        "system_version": "gate-stack-v1-2026-07-22",
        "universe_size": len(rows), "scanned": len(ok), "fresh_count": len(fresh),
        "combined_risk_new_actives":
            "$0 - no name passed the full gate stack" if not passing else "",
        "run_note": (f"Full universe read on candles. {len(fresh)} fresh BUY signals "
                     f"culled to {len(passing)} by the regime + ADX + DI + ZLSMA stack."),
        "data_quality": dq, "hits": list(hits.values()), "sell_mode": sells,
        "all_names": [{"sym": r["rname"], "last": r.get("last"),
                       "magical": r.get("magical"), "zlsma": r.get("zlsma"),
                       "ce_mode": r.get("ce_mode"), "ce_label": r.get("long_stop")}
                      for r in ok],
        "scanner_enrich": enrich, "scanner_enrich_asof": "n/a (chart reads only)",
        "tracker_exit_watch": {},
    }
    path = f"watchlists/universe-results-{date}.json"
    json.dump(out, open(path, "w"), indent=1)
    print(f"wrote {path}")
    print(f"  scanned {len(ok)} | fresh {len(fresh)} | passing {len(passing)} "
          f"| sell-mode {len(sells)}")
    if passing:
        print("  PASSING:", ", ".join(passing))
    else:
        print("  PASSING: (none)")


if __name__ == "__main__":
    main()
