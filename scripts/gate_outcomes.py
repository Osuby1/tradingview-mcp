"""Forward-grade THE GATE STACK's own output - does gating actually add anything?

Written 2026-07-25 to close the biggest measurement hole in the system.

The problem it fixes: `outcome_tracker.py` grades only the handful of calls that
were hand-registered in calls-ledger.json (14 of them as of today). The scan
produces ~48 fresh signals a day and culls them to ~6. NOTHING graded that cull.
So the gate stack - the thing we describe as "the scan's real strength" - was
completely unfalsifiable. If it added nothing, or actively hurt, no artifact in
this repo would have revealed it.

The measurement is deliberately a COMPARISON, not a score. Knowing that gated
names returned +2% means nothing on its own; the question is whether they beat
the names the stack THREW AWAY. So every fresh signal is bucketed:

    PASSED  - verdict CANDIDATE or STARTER ONLY (the stack would let you size it)
    BLOCKED - verdict BLOCKED (the stack vetoed it)

and the headline number is the SPREAD between them. If PASSED minus BLOCKED is
zero or negative over a real sample, the gate stack is not earning its keep and
we should say so out loud, the same way the BUY SCORE calibration did.

Deliberately NOT merged into outcome_tracker.py: that file grades hand-made
CALLS at their reference price and its scorecard is intentionally strict about
what counts as resolved. This grades POPULATIONS at the signal date. Mixing the
two would blur a call-quality number with a screen-quality number.

Honesty notes baked into the output:
  * Each signal is graded from the CLOSE of its signal date - no assumption that
    anyone got a better fill.
  * A name that stays fresh for days appears in several files. The headline
    dedupes to each symbol's FIRST appearance per cohort, because five correlated
    reads of the same move are not five observations. The raw event count is
    reported next to it.
  * Nothing is called a result until it has run the full holding window.

Usage:  python scripts/gate_outcomes.py [holding_days]      (default 21)
Writes: research/gate-outcomes.md + research/gate-outcomes.json
"""
import glob
import json
import os
import re
import sys
from collections import defaultdict

import numpy as np
import pandas as pd
import yfinance as yf

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schema  # noqa: E402

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOLDING = int(sys.argv[1]) if len(sys.argv) > 1 else 21
LOOKBACK = "6mo"


def cohort_of(verdict):
    """Normalize a verdict string to PASSED / BLOCKED / None (legacy free-text)."""
    v = (verdict or "").strip().upper()
    if v.startswith("BLOCKED"):
        return "BLOCKED"
    if v.startswith("CANDIDATE") or v.startswith("STARTER ONLY"):
        return "PASSED"
    return None          # 7/18-7/21 hand-written verdicts - not machine-comparable


def block_reason(verdict):
    """Which gate fired FIRST (gates run in order, so e.g. a VOLATILITY-CAP
    block means every earlier gate passed - exactly the shadow cohort the
    2026-07-26 re-justification promised to grade forward)."""
    v = (verdict or "").upper()
    if not v.startswith("BLOCKED"):
        return None
    if "DEEP-FAIL" in v:
        return "REGIME"
    if "ADX" in v:
        return "ADX FLOOR"
    if "+DI" in v or "-DI" in v:
        return "DIRECTION"
    if "ZLSMA" in v:
        return "ZLSMA"
    if "% AWAY" in v:
        return "VOLATILITY CAP (ex 2:1)"
    if "X ATR" in v:
        return "ATR GEOMETRY"
    if "ILLIQUID" in v:
        return "LIQUIDITY"
    return "OTHER"


def near_miss(e):
    """SHADOW COHORTS (pre-registered 2026-07-26, Omar-approved item 4).

    The Jan-Jun replay showed monsters missed by less than a point of ADX
    (TWST 19.15, HUT 19.47, HIMX 19.66) and DEEP-FAIL rejects that ran
    hundreds of percent (CAR +561%). Retro-lowering a threshold because of
    those names is forbidden curve-fitting. THIS is the legitimate version:
    grade the near-misses FORWARD, nightly, as their own cohorts.

    A near-miss must be a SOLE failure - every other gate passed - detected
    from the note (multiple failures are '; '-joined by gate_stack).

    PROMOTION BAR, declared now per the 2026-07-20 governance rules: a
    threshold change goes to a Friday review ONLY after >=30 MATURED signals
    in the cohort AND the cohort's mean forward return exceeds the PASSED
    cohort's mean over the same period. Until then these rows are
    observation, not evidence for any change.
    """
    note = e.get("note") or ""
    if e["cohort"] != "BLOCKED" or ";" in note:
        return None                      # not blocked, or more than one gate failed
    adx = e.get("adx")
    if "ADX" in note and adx is not None and 18.0 <= adx < 20.0:
        return "ADX 18-20, all else passed"
    if "DEEP-FAIL" in note:
        return "DEEP-FAIL, all else passed"
    return None


def collect_signals():
    """Every fresh signal ever written, with its cohort and signal date."""
    events, skipped = [], defaultdict(int)
    for f in sorted(glob.glob(os.path.join(REPO, "watchlists", "universe-results-*.json"))):
        date = re.search(r"(\d{4}-\d{2}-\d{2})", f).group(1)
        try:
            d = json.load(open(f, encoding="utf-8"))
            # Reads the WHOLE history, so most files here are legitimately legacy
            # (pre-2026-07-25, unstamped). Those are fine - cohort_of() below only
            # accepts machine verdicts anyway. What must not pass silently is a
            # FUTURE version this grader has not been taught to read.
            schema.require(d, understood=(2, 3), path=f, warn=lambda m: None)
        except schema.SchemaError as exc:
            skipped[f"unreadable contract: {exc}"] += 1
            continue
        except Exception:
            skipped["unreadable file"] += 1
            continue
        for h in d.get("hits") or []:
            c = cohort_of(h.get("verdict"))
            if c is None:
                skipped[f"legacy verdict ({date})"] += 1
                continue
            events.append({"date": date, "sym": h["sym"], "cohort": c,
                           "verdict": h.get("verdict"),
                           "regime": (h.get("gates") or {}).get("regime") or h.get("regime"),
                           "adx": (h.get("gates") or {}).get("adx"),
                           "note": h.get("note") or ""})
    return events, dict(skipped)


def grade(events, px, spy):
    """Attach forward returns to each signal event."""
    out = []
    for e in events:
        s = px.get(e["sym"])
        if s is None or s.empty:
            out.append({**e, "status": "NO PRICE DATA"})
            continue
        after = s[s.index >= e["date"]]
        if len(after) < 2:
            out.append({**e, "status": "TOO NEW"})
            continue
        win = after.iloc[:HOLDING + 1]
        entry = float(win["Close"].iloc[0])
        mark = float(win["Close"].iloc[-1])
        elapsed = len(win) - 1
        ret = (mark / entry - 1) * 100
        mfe = (float(win["High"].max()) / entry - 1) * 100
        mae = (float(win["Low"].min()) / entry - 1) * 100
        exc = None
        if spy is not None and not spy.empty:
            sa = spy[spy.index >= e["date"]].iloc[:HOLDING + 1]
            if len(sa) >= 2:
                exc = ret - (float(sa["Close"].iloc[-1]) / float(sa["Close"].iloc[0]) - 1) * 100
        out.append({**e, "status": "MATURED" if elapsed >= HOLDING else "OPEN",
                    "elapsed": elapsed, "entry": round(entry, 2), "mark": round(mark, 2),
                    "return_pct": round(ret, 2), "mfe": round(mfe, 2), "mae": round(mae, 2),
                    "spy_excess": round(exc, 2) if exc is not None else None})
    return out


def stats(rows):
    r = [x["return_pct"] for x in rows]
    e = [x["spy_excess"] for x in rows if x.get("spy_excess") is not None]
    if not r:
        return None
    return {"n": len(r), "mean": round(float(np.mean(r)), 2),
            "median": round(float(np.median(r)), 2),
            "win_pct": round(100 * sum(1 for x in r if x > 0) / len(r)),
            "mean_excess": round(float(np.mean(e)), 2) if e else None,
            "mean_mae": round(float(np.mean([x["mae"] for x in rows])), 2)}


def main():
    events, skipped = collect_signals()
    if not events:
        raise SystemExit("no machine-verdict signals found - nothing to grade")

    syms = sorted({e["sym"] for e in events})
    print(f"grading {len(events)} signal events across {len(syms)} symbols "
          f"(holding {HOLDING} sessions)...")
    data = yf.download(syms + ["SPY"], period=LOOKBACK, interval="1d",
                       group_by="ticker", auto_adjust=False, threads=True, progress=False)

    def frame(sym):
        try:
            df = data[sym].dropna(subset=["Close"])
        except Exception:
            return None
        df.index = df.index.strftime("%Y-%m-%d")
        return df

    px = {s: frame(s) for s in syms}
    spy = frame("SPY")
    graded = grade(events, px, spy)

    usable = [g for g in graded if g.get("return_pct") is not None]
    # dedupe: first appearance of each symbol per cohort
    seen, first = set(), []
    for g in sorted(usable, key=lambda x: x["date"]):
        k = (g["sym"], g["cohort"])
        if k in seen:
            continue
        seen.add(k)
        first.append(g)

    by = {c: [g for g in first if g["cohort"] == c] for c in ("PASSED", "BLOCKED")}
    st = {c: stats(v) for c, v in by.items()}
    matured = {c: stats([g for g in v if g["status"] == "MATURED"]) for c, v in by.items()}

    L = []
    L.append("# Gate stack forward grade")
    L.append("")
    L.append(f"Does THE GATE STACK earn its keep? Every fresh Chandelier signal is graded "
             f"forward from the CLOSE of its signal date over {HOLDING} trading sessions, "
             f"bucketed by what the stack decided. The number that matters is the SPREAD.")
    L.append("")
    L.append(f"- Signal events found: {len(events)}  |  priced: {len(usable)}  "
             f"|  unique symbol-cohort pairs (headline sample): {len(first)}")
    if skipped:
        L.append(f"- Skipped (pre-2026-07-22 hand-written verdicts, not machine-comparable): "
                 f"{sum(skipped.values())}")
    L.append("")
    L.append("## Headline - all signals, deduped to first appearance")
    L.append("")
    L.append("| Cohort | n | Win% | Mean | Median | Mean vs SPY | Mean worst drawdown |")
    L.append("|---|---|---|---|---|---|---|")
    for c in ("PASSED", "BLOCKED"):
        s = st[c]
        if not s:
            L.append(f"| {c} | 0 | - | - | - | - | - |")
            continue
        L.append(f"| {c} | {s['n']} | {s['win_pct']}% | {s['mean']:+.2f}% | {s['median']:+.2f}% "
                 f"| {s['mean_excess']:+.2f}% | {s['mean_mae']:+.2f}% |"
                 if s["mean_excess"] is not None else
                 f"| {c} | {s['n']} | {s['win_pct']}% | {s['mean']:+.2f}% | {s['median']:+.2f}% | - "
                 f"| {s['mean_mae']:+.2f}% |")
    L.append("")

    verdict_line = None
    if st["PASSED"] and st["BLOCKED"]:
        spread = st["PASSED"]["mean"] - st["BLOCKED"]["mean"]
        L.append(f"**Spread (PASSED minus BLOCKED): {spread:+.2f} percentage points.**")
        L.append("")
        n_small = st["PASSED"]["n"] < 30
        n_mature = (matured["PASSED"] or {}).get("n", 0)
        if n_mature == 0:
            verdict_line = ("NO VERDICT YET - not one gated signal has completed a full "
                            f"{HOLDING}-session window. Everything above is an open mark, "
                            "not a result. Do not quote the spread as evidence in either "
                            "direction.")
        elif spread <= 0:
            verdict_line = (f"The gate stack is NOT adding value on this sample: the names it "
                            f"passed did no better than the names it blocked ({spread:+.2f}pt). "
                            "If this holds as n grows, the stack is costing opportunities "
                            "without buying safety, and it should be re-examined.")
        else:
            verdict_line = (f"The gate stack is ahead by {spread:+.2f}pt on this sample"
                            + (" - but n is small, so treat it as directional, not proven."
                               if n_small else "."))
        L.append(verdict_line)
        L.append("")

    L.append("## Matured only (full window closed) - the only honest read")
    L.append("")
    L.append("| Cohort | n | Win% | Mean | Median | Mean vs SPY |")
    L.append("|---|---|---|---|---|---|")
    for c in ("PASSED", "BLOCKED"):
        s = matured[c]
        if not s:
            L.append(f"| {c} | 0 | - | - | - | - |")
        else:
            me = f"{s['mean_excess']:+.2f}%" if s["mean_excess"] is not None else "-"
            L.append(f"| {c} | {s['n']} | {s['win_pct']}% | {s['mean']:+.2f}% "
                     f"| {s['median']:+.2f}% | {me} |")
    L.append("")
    L.append("## Blocked names by the gate that fired first")
    L.append("")
    L.append("Added 2026-07-26 with the volatility-cap re-justification. Gates run in "
             "order, so each bucket contains names that PASSED every earlier gate. The "
             "VOLATILITY CAP row is the one on probation: its old 2:1 rationale died "
             "with the profit target, it blocked SOXL before +539%, and it keeps its "
             "job only if this table keeps saying its blocks were worth blocking.")
    L.append("")
    L.append("| First-failing gate | n | Win% | Mean | Median | Mean vs SPY |")
    L.append("|---|---|---|---|---|---|")
    blocked_first = [g for g in first if g["cohort"] == "BLOCKED"]
    reasons = sorted({block_reason(g.get("verdict")) for g in blocked_first} - {None})
    for reason in reasons:
        s = stats([g for g in blocked_first if block_reason(g.get("verdict")) == reason])
        if s:
            me = f"{s['mean_excess']:+.2f}%" if s["mean_excess"] is not None else "-"
            L.append(f"| {reason} | {s['n']} | {s['win_pct']}% | {s['mean']:+.2f}% "
                     f"| {s['median']:+.2f}% | {me} |")
    L.append("")
    L.append("## Shadow cohorts - the forbidden retro-tune, run forward instead")
    L.append("")
    L.append("Would lowering the ADX floor to 18, or softening DEEP-FAIL, have helped? "
             "The replay's missed monsters make that tempting; answering it by re-running "
             "history is curve-fitting. These cohorts answer it FORWARD: sole-failure "
             "near-misses graded nightly against the PASSED cohort. Promotion bar "
             "(pre-registered): >=30 MATURED signals AND mean above PASSED's - then it "
             "goes to a Friday review, not before.")
    L.append("")
    L.append("| Shadow cohort | n | Win% | Mean | Median | Mean vs SPY | PASSED mean (ref) |")
    L.append("|---|---|---|---|---|---|---|")
    passed_ref = (st["PASSED"] or {}).get("mean")
    for label in ("ADX 18-20, all else passed", "DEEP-FAIL, all else passed"):
        rows_nm = [g for g in first if near_miss(g) == label]
        s = stats(rows_nm)
        ref = f"{passed_ref:+.2f}%" if passed_ref is not None else "-"
        if not s:
            L.append(f"| {label} | 0 | - | - | - | - | {ref} |")
        else:
            me = f"{s['mean_excess']:+.2f}%" if s["mean_excess"] is not None else "-"
            L.append(f"| {label} | {s['n']} | {s['win_pct']}% | {s['mean']:+.2f}% "
                     f"| {s['median']:+.2f}% | {me} | {ref} |")
    L.append("")
    L.append("## Every graded signal")
    L.append("")
    L.append("| Date | Sym | Cohort | Regime | Entry | Mark | Days | Return | vs SPY | Status |")
    L.append("|---|---|---|---|---|---|---|---|---|---|")
    for g in sorted(usable, key=lambda x: (x["date"], x["cohort"], x["sym"])):
        ex = f"{g['spy_excess']:+.1f}" if g.get("spy_excess") is not None else "-"
        L.append(f"| {g['date']} | {g['sym']} | {g['cohort']} | {g.get('regime') or '-'} "
                 f"| {g['entry']} | {g['mark']} | {g['elapsed']} | {g['return_pct']:+.1f}% "
                 f"| {ex} | {g['status']} |")
    L.append("")
    L.append("Open marks are not results. This file exists so that the cull the scan performs "
             "every night is measured instead of assumed.")

    md = os.path.join(REPO, "research", "gate-outcomes.md")
    js = os.path.join(REPO, "research", "gate-outcomes.json")
    open(md, "w", encoding="utf-8").write("\n".join(L) + "\n")
    json.dump({"holding_days": HOLDING, "generated_from": "universe-results-*.json",
               "cohorts": st, "matured": matured, "graded": graded},
              open(js, "w", encoding="utf-8"), indent=1)
    # console is cp1252 on this box - never let an encoding slip kill a finished run
    def say(s):
        print(s.encode("ascii", "replace").decode("ascii"))

    say("\n".join(L[:24]))
    if verdict_line:
        say("\n" + verdict_line)
    print(f"\nwrote {md} + {js}")


if __name__ == "__main__":
    main()
