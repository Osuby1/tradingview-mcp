"""Prove the EOD scan actually produced TODAY's data. Exit non-zero if not.

Why this exists
---------------
On 2026-07-21 the chain's universe step died ("out of usage credits"), the batch
file logged a WARNING and carried on, and the compile step happily built a report
from 2026-07-20's leftover results - then logged "EOD chain done". The output
looked like a normal successful report. It was Monday's scan wearing Tuesday's
run stamp.

A chain that cannot fail loudly is worse than no chain, because you trust it.
This script is the thing that fails loudly.

Checks, in order:
  1. watchlists/universe-results-<date>.json exists at all
  2. its internal "date" field matches the date we asked for
  3. it was modified recently (not a stale file left from a previous run)
  4. it actually contains scan output (scanned > 0)
  5. every hit carries a verdict
  6. gate data is present, so the regime/liquidity gates really ran

Usage:
    python scripts/verify_eod_output.py 2026-07-22
    python scripts/verify_eod_output.py 2026-07-22 --max-age-hours 6
"""
import json
import os
import sys
import time

GATE_FIELDS = ("regime", "adx", "plus_di", "minus_di", "avg_dollar_vol")


def fail(msg):
    print(f"EOD-VERIFY FAIL: {msg}")
    sys.exit(1)


def warn(msg):
    print(f"EOD-VERIFY WARN: {msg}")


def main():
    if len(sys.argv) < 2:
        fail("no date argument given")
    date = sys.argv[1]
    max_age = 6.0
    if "--max-age-hours" in sys.argv:
        max_age = float(sys.argv[sys.argv.index("--max-age-hours") + 1])

    path = f"watchlists/universe-results-{date}.json"

    # 1. exists
    if not os.path.exists(path):
        fail(f"{path} does not exist - the universe scan did not produce output. "
             f"Do NOT compile a report; it would silently use an older run.")

    # 3. freshness
    age_h = (time.time() - os.path.getmtime(path)) / 3600.0
    if age_h > max_age:
        fail(f"{path} is {age_h:.1f}h old (limit {max_age:.0f}h) - this is a leftover "
             f"file from an earlier run, not today's scan.")

    try:
        d = json.load(open(path))
    except Exception as exc:
        fail(f"{path} is not readable JSON: {exc}")

    # 2. internal date
    if str(d.get("date")) != date:
        fail(f"{path} has internal date {d.get('date')!r} but we asked for {date!r} - "
             f"mismatched or copied file.")

    # 4. real content
    scanned = d.get("scanned") or 0
    if scanned <= 0:
        fail(f"scanned={scanned} - the scan produced no reads at all.")

    hits = d.get("hits") or []
    # 5. verdicts
    missing_verdict = [h.get("sym") for h in hits if not h.get("verdict")]
    if missing_verdict:
        fail(f"{len(missing_verdict)} hit(s) have no verdict: {missing_verdict[:5]}")

    # 6. did the gates actually run?
    gated = sum(1 for h in hits if isinstance(h.get("gates"), dict) and h["gates"])
    if hits and gated == 0:
        fail(f"{len(hits)} fresh signals but NONE carry gate detail - the regime and "
             f"liquidity gates did not run. Report would be unsafe to act on.")
    if hits and gated < len(hits):
        warn(f"only {gated}/{len(hits)} hits carry gate detail")

    blockers = [q for q in (d.get("data_quality") or [])
                if str(q.get("severity", "")).upper() == "BLOCKER"]

    print(f"EOD-VERIFY OK: {path}")
    print(f"  scanned {scanned} | fresh {len(hits)} | gated {gated} "
          f"| sell-mode {len(d.get('sell_mode') or [])} | age {age_h:.1f}h")
    if blockers:
        print(f"  NOTE: {len(blockers)} data-quality BLOCKER(s) recorded in the run:")
        for b in blockers[:3]:
            print(f"    - {str(b.get('finding'))[:110]}")
    sys.exit(0)


if __name__ == "__main__":
    main()
