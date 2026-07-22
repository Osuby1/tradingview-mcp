"""Names we have ACTED on - alerts armed, plans written - which must never fall
out of the scan universe.

Why this exists
---------------
2026-07-22, found by Omar. ECVT was recommended on 7/20 as "the cleanest new
chart of the run": sized plan, limit 12.35, stop 11.55, alert 5195389391 armed.
The alert FIRED on 7/21 and the trade worked without him (12.35 -> 12.94).

It then vanished from the scan completely.

Cause: ECVT is on NONE of the three watchlists. It entered the universe only via
the origination scanner's "Coiled" tab on 7/20. When the scanner demoted it to
"Excluded" on 7/21, it left the universe - because the universe was built purely
from TODAY'S CANDIDATE SOURCES and had no concept of "things we already acted on".

So a name could get a plan and an alert on Monday and be invisible by Tuesday.
Same failure class as SMCI, but worse: SMCI was merely unscanned, ECVT was
actively tracked and then silently dropped while its plan was live.

The rule
--------
A symbol is TRACKED, and therefore always in the universe, if:
  * it has any ACTIVE alert, or
  * any of its alerts FIRED within RECENT_DAYS (a fired alert is more reason to
    look, not less - ECVT's had fired and auto-deactivated), or
  * it appears in a plan file from the last PLAN_DAYS days.

Alert data comes from a dump of the TradingView alert board written to
watchlists/alert-board.json (the board is only reachable from the browser
session, so it cannot be fetched here).
"""
import datetime
import json
import os
import re

RECENT_DAYS = 21     # a fired alert stays in view for ~a month of sessions
PLAN_DAYS = 30

NON_EQUITY = {"BTCUSD", "ETHUSD", "SOLUSD", "ETPZ2030", "BIPZ2030", "WTI",
              "PURR", "HYPD", "CBRS", "ORBS"}


def _parse_iso(s):
    if not s:
        return None
    try:
        return datetime.datetime.strptime(s[:19], "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        return None


def from_alert_board(path="watchlists/alert-board.json", now=None):
    """Symbols with an active alert, or one that fired recently."""
    if not os.path.exists(path):
        return set(), {"error": f"{path} not found - alert board never dumped"}
    now = now or datetime.datetime.utcnow()
    rows = json.load(open(path))
    keep, why = set(), {}
    for r in rows:
        s = str(r.get("sym", "")).upper()
        if not s or s in NON_EQUITY:
            continue
        if r.get("active"):
            keep.add(s)
            why[s] = "active alert"
            continue
        lf = _parse_iso(r.get("last_fire"))
        if lf and (now - lf).days <= RECENT_DAYS:
            keep.add(s)
            why[s] = f"alert fired {lf.date()}"
    return keep, why


def from_plan_files(repo=".", now=None):
    """Symbols named in recent plan files under research/."""
    now = now or datetime.datetime.utcnow()
    keep, why = set(), {}
    research = os.path.join(repo, "research")
    if not os.path.isdir(research):
        return keep, why
    for fn in os.listdir(research):
        m = re.match(r"plans-(\d{4}-\d{2}-\d{2})\.md$", fn)
        if not m:
            continue
        d = _parse_iso(m.group(1) + "T00:00:00")
        if d and (now - d).days > PLAN_DAYS:
            continue
        text = open(os.path.join(research, fn), encoding="utf-8", errors="replace").read()
        # plan tables lead each row with "| N | TICKER (Company ..." or "| TICKER |"
        for tk in re.findall(r"\|\s*\d*\s*\|\s*\*{0,2}([A-Z][A-Z0-9.\-]{1,5})\b", text):
            if tk in NON_EQUITY:
                continue
            keep.add(tk)
            why.setdefault(tk, f"plan {m.group(1)}")
    return keep, why


def tracked(repo=".", now=None):
    """Union of alert-tracked and plan-tracked symbols, with reasons."""
    a, wa = from_alert_board(os.path.join(repo, "watchlists", "alert-board.json"), now)
    p, wp = from_plan_files(repo, now)
    why = dict(wp)
    why.update(wa)          # alert reason wins - it is the live one
    return (a | p), why


if __name__ == "__main__":
    syms, why = tracked()
    print(f"{len(syms)} tracked symbols (alerts + recent plans)")
    for s in sorted(syms)[:20]:
        print(f"  {s:<7} {why.get(s, '')}")
    if len(syms) > 20:
        print(f"  ... and {len(syms)-20} more")
