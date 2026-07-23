"""Grade every pre-registered CALL against its own plan and against SPY.

This is the loop the whole system was missing (Omar, 2026-07-22): without it,
every claim of skill - including the assistant's - is unfalsifiable. It closes
the anti-sycophancy mandate's core requirement.

It grades at the CALL'S REFERENCE PRICE, not at any actual fill, because the
question is "was the ANALYSIS good", independent of whether Omar took it. A call
that was correctly AVOIDED is graded too: a good avoid means the would-be trade
went nowhere or down.

Per call it computes, over the holding window (default 21 trading days, or
however many have elapsed if still open):
  * return from ref to the marking price (respecting direction: short flips sign)
  * max favorable / adverse excursion within the window
  * whether the plan's target or stop was hit first
  * SPY return over the SAME calendar window
  * excess vs SPY (the number that says whether the call beat just buying the index)
  * a status: OPEN / TARGET / STOPPED / MATURED, and a verdict

Inputs:
  research/calls-ledger.json          - the calls (source of truth)
  research/call-prices-<date>.json    - {sym: [{d, c, h, l}, ...]} incl SPY,
                                        dumped from the chart

Usage:
    python scripts/outcome_tracker.py [YYYY-MM-DD]   # price-file date; default latest
"""
import glob
import json
import os
import sys


def _series(prices, sym):
    return {r["d"]: r for r in prices.get(sym, [])}


def _window(series_list, start_date, days):
    """The subset of dates >= start_date, capped to `days` sessions."""
    ds = sorted(d for d in series_list if d >= start_date)
    return ds[:days + 1]


def grade_call(call, prices, holding_days):
    sym = call["sym"]
    ser = {r["d"]: r for r in prices.get(sym, [])}
    spy = {r["d"]: r for r in prices.get("SPY", [])}
    if not ser:
        return {**call, "status": "NO PRICE DATA", "note": f"no bars for {sym}"}

    start = call["date"]
    dates = sorted(d for d in ser if d >= start)
    if len(dates) < 2:
        return {**call, "status": "TOO NEW", "elapsed": 0}

    win = dates[:holding_days + 1]
    ref = call["ref"]
    long = call["dir"] == "long"
    entry_close = ser[win[0]]["c"]
    mark = ser[win[-1]]["c"]
    elapsed = len(win) - 1

    def ret(px):
        r = (px / ref - 1) * 100
        return r if long else -r

    cur_ret = round(ret(mark), 2)

    # excursions within the window (intraday high/low)
    highs = [ser[d]["h"] for d in win if "h" in ser[d]]
    lows = [ser[d]["l"] for d in win if "l" in ser[d]]
    if long:
        mfe = round(ret(max(highs)), 2) if highs else None
        mae = round(ret(min(lows)), 2) if lows else None
    else:
        mfe = round(ret(min(lows)), 2) if lows else None    # short profits on down
        mae = round(ret(max(highs)), 2) if highs else None

    # did target or stop hit first?
    tgt, stp = call.get("target"), call.get("stop")
    hit = None
    for d in win[1:]:
        hi, lo = ser[d].get("h"), ser[d].get("l")
        if hi is None:
            continue
        if long:
            if stp and lo <= stp:
                hit = "STOP"; break
            if tgt and hi >= tgt:
                hit = "TARGET"; break
        else:
            if stp and hi >= stp:
                hit = "STOP"; break
            if tgt and lo <= tgt:
                hit = "TARGET"; break

    # SPY over the same window
    spy_excess = None
    if spy and win[0] in spy and win[-1] in spy:
        spy_ret = (spy[win[-1]]["c"] / spy[win[0]]["c"] - 1) * 100
        spy_excess = round(cur_ret - spy_ret, 2)

    matured = elapsed >= holding_days
    if hit == "STOP":
        status = "STOPPED"
    elif hit == "TARGET":
        status = "TARGET HIT"
    elif matured:
        status = "MATURED"
    else:
        status = "OPEN"

    avoid = "avoid" in call["id"]
    if avoid:
        # a good avoid = the would-be trade lost or went nowhere
        verdict = ("AVOID VALIDATED" if (cur_ret <= 0 or hit == "STOP")
                   else "AVOID QUESTIONABLE" if cur_ret < 3
                   else "AVOID WRONG (it ran)")
    else:
        verdict = ("WIN" if cur_ret > 0 else "LOSS") + (
            "" if matured or hit else " (open)")

    return {**call, "status": status, "elapsed": elapsed, "entry_close": round(entry_close, 2),
            "mark": round(mark, 2), "return_pct": cur_ret, "mfe": mfe, "mae": mae,
            "hit": hit, "spy_excess": spy_excess, "verdict": verdict, "matured": matured}


def main():
    led = json.load(open("research/calls-ledger.json"))
    holding = led.get("holding_days", 21)

    if len(sys.argv) > 1:
        pf = f"research/call-prices-{sys.argv[1]}.json"
    else:
        cands = sorted(glob.glob("research/call-prices-*.json"))
        pf = cands[-1] if cands else None
    if not pf or not os.path.exists(pf):
        raise SystemExit("no research/call-prices-<date>.json - dump prices from the chart first")
    prices = json.load(open(pf))

    graded = [grade_call(c, prices, holding) for c in led["calls"]]

    out = []
    out.append("# Call outcome tracker")
    out.append("")
    out.append(f"Graded at each call's REFERENCE price (analysis quality, not fills). "
               f"Holding window {holding} trading days. Price file: {os.path.basename(pf)}.")
    out.append("")
    out.append("| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for g in graded:
        if g["status"] in ("NO PRICE DATA", "TOO NEW"):
            out.append(f"| {g['sym']} | {g['dir']} | {g.get('ref')} | - | - | - | - | - | - | - | {g['status']} | - |")
            continue
        se = f"{g['spy_excess']:+.1f}" if g["spy_excess"] is not None else "-"
        out.append(f"| {g['sym']} | {g['dir']} | {g['ref']} | {g['mark']} | {g['elapsed']} "
                   f"| {g['return_pct']:+.1f}% | {se} | {g['mfe']:+.1f} | {g['mae']:+.1f} "
                   f"| {g['hit'] or '-'} | {g['status']} | {g['verdict']} |")
    out.append("")

    # scorecard over MATURED non-avoid calls only (the only honest win-rate)
    real = [g for g in graded if "avoid" not in g["id"] and g.get("return_pct") is not None]
    mature = [g for g in real if g.get("matured") or g.get("hit")]
    out.append("## Scorecard")
    out.append("")
    out.append(f"- Total calls logged: {len(graded)}")
    out.append(f"- Directional (non-avoid): {len(real)}  |  matured/resolved: {len(mature)}")
    if mature:
        wins = sum(1 for g in mature if g["return_pct"] > 0)
        avg = sum(g["return_pct"] for g in mature) / len(mature)
        exc = [g["spy_excess"] for g in mature if g["spy_excess"] is not None]
        out.append(f"- Win rate (resolved): {wins}/{len(mature)} = {100*wins/len(mature):.0f}%")
        out.append(f"- Mean return (resolved): {avg:+.2f}%")
        if exc:
            out.append(f"- Mean excess vs SPY (resolved): {sum(exc)/len(exc):+.2f}%")
    else:
        out.append("- **Nothing has matured yet.** Every directional call is younger than "
                   f"{holding} sessions. The tracker is BUILT; the verdict comes when the "
                   "windows close. Do not read the open marks as results.")
    avoids = [g for g in graded if "avoid" in g["id"] and g.get("return_pct") is not None]
    if avoids:
        val = sum(1 for g in avoids if g["verdict"].startswith("AVOID VALIDATED"))
        out.append(f"- Avoids validated so far: {val}/{len(avoids)} "
                   f"(would-be trade went nowhere/down)")
    out.append("")
    out.append("Open marks are NOT results - they are current unrealized reads that will "
               "move. The point of this file is that the calls are now tracked and will be "
               "graded automatically as each window closes.")

    with open("research/call-outcomes.md", "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")
    with open("research/call-outcomes.json", "w", encoding="utf-8") as fh:
        json.dump({"holding_days": holding, "graded": graded}, fh, indent=1)
    print("\n".join(out))
    print("\nwrote research/call-outcomes.md + .json")


if __name__ == "__main__":
    main()
