#!/usr/bin/env python3
"""Readiness scores for the whole nightly candidate list, in one batch.

WHY (Omar standing order 2026-07-31, the DGX post-mortem): DGX topped the scan
on the gates (ADX 42) while its readiness was 26/100 - and it went sideways
exactly as the score implied. Gates answer "is it SAFE to buy"; readiness
answers "is it about to MOVE". From now on every candidate the workbook shows
carries both, computed automatically by the chain instead of per-rec manual
`options_analysis.py --analyze` calls.

WHAT IT DOES
  * reads watchlists/universe-results-<date>.json (date arg, default today)
  * computes readiness (options_analysis.readiness - the SAME five-component
    0-100 score the options overlay uses, direction long/CALL) for every name
    in `hits` and `gated_longs` (~80-120 names; sell_mode is deliberately NOT
    scanned - that would triple the runtime for names nobody is buying)
  * one batched yfinance download for all names (plus one for SPY), then a
    single per-name retry for anything the batch missed; a name that still
    fails is LOGGED with its reason, never guessed
  * AUGMENTS the results JSON in place: each hit / gated-long entry gains
        "readiness": {"score": N, "driver": "<one line>", "label": "uncalibrated"}
    plus a top-level "readiness_asof" timestamp. Additive only - the schema
    contract (scripts/schema.py) checks required fields, extras are welcome.

The score stays UNCALIBRATED: it ranks candidates and gets graded in the
Friday reviews - it does not gate or veto until the data earns it that power.

Usage:
  python scripts/readiness_batch.py [YYYY-MM-DD] [--asof "2026-07-31 17:05"]

Exit code: 0 if the JSON was augmented (even with some per-name failures),
nonzero only if nothing could be done (file missing, total download failure).
The EOD chain treats a failure here as a WARNING - the compile still runs and
prints "n/a" in the Readiness column rather than dying.
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from options_analysis import readiness  # noqa: E402  (same maths as the overlay)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# notes[] in the readiness() result line up 1:1 with these component keys
_COMP_ORDER = ["squeeze", "trigger", "volume", "momentum", "rel_strength"]


def driver_line(rd):
    """One plain-English line naming what drives the score: the two WORST
    components when the score is low (why it is not poised), the two BEST
    when it is high (what is loading the spring)."""
    comps = rd.get("components") or {}
    notes = rd.get("notes") or []
    pairs = [(k, n) for k, n in zip(_COMP_ORDER, notes)]
    if not pairs:
        return rd.get("note") or "no component detail"
    ranked = sorted(pairs, key=lambda p: comps.get(p[0], 0))
    score = rd.get("score") or 0
    picked = list(reversed(ranked[-2:])) if score >= 60 else ranked[:2]
    return "; ".join(n for _, n in picked)


def batch_histories(syms):
    """One yfinance download for every name. Returns {sym: DataFrame}."""
    import yfinance as yf
    out = {}
    if not syms:
        return out
    df = yf.download(syms, period="1y", auto_adjust=True, group_by="ticker",
                     progress=False, threads=True)
    for s in syms:
        try:
            h = df[s] if len(syms) > 1 else df
            h = h.dropna(how="all")
            if h.empty:
                continue
            # yf.download returns a tz-NAIVE index while Ticker.history (which
            # readiness() uses for its SPY series) returns tz-aware New York
            # dates. Left naive, the relative-strength reindex against SPY
            # matches NOTHING and every name dies on an empty series - that is
            # exactly what happened on this script's first live run.
            if h.index.tz is None:
                h = h.tz_localize("America/New_York")
            out[s] = h
        except Exception:
            pass  # missing from the batch - per-name retry below
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("date", nargs="?", default=dt.date.today().isoformat())
    ap.add_argument("--asof", default=None,
                    help="timestamp recorded as readiness_asof "
                         "(default: now, falling back to the JSON's own date)")
    args = ap.parse_args()

    path = os.path.join(REPO, "watchlists", f"universe-results-{args.date}.json")
    if not os.path.exists(path):
        print(f"FAILED: {path} not found")
        return 1
    res = json.load(open(path, encoding="utf-8"))

    hits = res.get("hits") or []
    gated = res.get("gated_longs") or []
    entries = {}          # sym -> [entry dicts to augment]
    for e in hits + gated:
        s = e.get("sym")
        if s:
            entries.setdefault(s, []).append(e)
    syms = sorted(entries)
    print(f"readiness batch {args.date}: {len(hits)} hits + {len(gated)} gated "
          f"longs = {len(syms)} unique names (direction long)")

    try:
        hists = batch_histories(syms)
    except Exception as exc:
        print(f"WARNING: batched download failed ({exc}) - "
              f"falling back to per-name fetches")
        hists = {}

    ok, failures = 0, {}
    for s in syms:
        try:
            rd = readiness(s, "CALL", hist=hists.get(s))
            if rd.get("score") is None:
                # e.g. <130 sessions of history - logged, never guessed
                failures[s] = rd.get("note") or "no score"
                block = {"score": None,
                         "driver": f"not computed - {failures[s]}",
                         "label": "uncalibrated"}
            else:
                block = {"score": rd["score"], "driver": driver_line(rd),
                         "label": "uncalibrated"}
                ok += 1
        except Exception as exc:
            failures[s] = str(exc)
            block = {"score": None, "driver": f"not computed - {exc}",
                     "label": "uncalibrated"}
        for e in entries[s]:
            e["readiness"] = block

    if ok == 0 and syms:
        print(f"FAILED: 0 of {len(syms)} names scored - JSON left untouched")
        for s, why in failures.items():
            print(f"  {s}: {why}")
        return 1

    res["readiness_asof"] = (args.asof
                             or dt.datetime.now().strftime("%Y-%m-%d %H:%M")
                             or res.get("date"))
    with open(path, "w", encoding="utf-8") as f:
        json.dump(res, f, indent=1)
    print(f"scored {ok}/{len(syms)} names "
          f"({100.0 * ok / len(syms):.0f}% coverage); wrote {path}")
    if failures:
        print(f"failures ({len(failures)}) - shown as n/a in the workbook:")
        for s, why in failures.items():
            print(f"  {s}: {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
