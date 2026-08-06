"""A-LIST: the flag-to-fill conversion engine (Omar-approved 2026-08-06).

Nightly, after the scan chain: pick the 1-3 most compelling gate-passers,
wire REAL entry-door alerts at their plan limits (phone rings at the
actionable price), log forced ACT/PASS verdict slots, and write funnel
metrics so Friday reviews grade the conversion pipeline itself.

Leaks this fixes (diagnosed 8/6): firehose without hierarchy, no forced
decision, doors not pre-wired, funnel unmeasured.

Usage:
  python scripts/a_list.py              # full run (select + wire doors)
  python scripts/a_list.py --dry-run    # select + print only
Scheduled: Task 'AListNightly' daily 15:50 CT (after the 15:15 chain).
"""
import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
STATE = REPO / "watchlists" / "a-list-state.json"
VERDICTS = REPO / "research" / "a-list-verdicts.json"
DOOR_ACTIONS = REPO / "watchlists" / "door-actions.json"
BOOK = REPO / "watchlists" / "open-book.json"

MAX_CARDS = 3
MIN_READY = 55
MIN_DOLLAR_VOL = 20e6


def latest_results():
    files = sorted((REPO / "watchlists").glob("universe-results-*.json"))
    if not files:
        sys.exit("no universe results found")
    return files[-1], json.loads(files[-1].read_text(encoding="utf-8"))


def main():
    dry = "--dry-run" in sys.argv
    src, res = latest_results()
    date = res.get("date", "?")
    held = {p["sym"] for p in json.loads(BOOK.read_text()).get("positions", [])}

    passers = [h for h in res.get("hits", [])
               if "passes every gate" in str(h.get("verdict", "")).lower()]
    eligible = []
    for h in passers:
        r = (h.get("readiness") or {}).get("score") or 0
        dv = (h.get("gates") or {}).get("avg_dollar_vol") or 0
        if h["sym"] in held or r < MIN_READY or dv < MIN_DOLLAR_VOL:
            continue
        eligible.append(h)
    eligible.sort(key=lambda h: -h["readiness"]["score"])
    cards = eligible[:MAX_CARDS]

    # funnel metrics (stage counts for the Friday review)
    funnel = {
        "date": date, "scanned": res.get("scanned"), "fresh": res.get("fresh_count"),
        "full_passers": len(passers), "eligible": len(eligible),
        "a_list": [h["sym"] for h in cards],
        "doors_wired": 0, "note": f"selector: ready>={MIN_READY}, $vol>={MIN_DOLLAR_VOL/1e6:.0f}M, not-held, top {MAX_CARDS} by readiness",
        # SELECTOR CONTROL GROUP (Omar's challenge 8/6: how do we KNOW the
        # picks are right?): every eligible name is snapshotted with its
        # entry reference so Friday reviews can grade SELECTED vs REJECTED
        # vs random-3 vs a buy-score ordering - the selector must EARN its
        # ranking or be demoted to "any 3 passers with doors".
        "eligible_cohort": [{"sym": h["sym"], "readiness": h["readiness"]["score"],
                             "ref_price": h.get("real_close"), "selected": h in cards}
                            for h in eligible],
        "passers_below_floor": [{"sym": h["sym"],
                                 "readiness": (h.get("readiness") or {}).get("score")}
                                for h in passers if h not in eligible and h["sym"] not in held],
    }

    state = {"date": "", "doors": {}}
    if STATE.exists():
        state = json.loads(STATE.read_text())

    actions = []
    # drop doors for names no longer on the list (or now held)
    keep = {h["sym"] for h in cards}
    for sym, door in list(state.get("doors", {}).items()):
        if sym not in keep:
            actions.append({"op": "delete", "alert_id": door["alert_id"], "sym": sym})
            del state["doors"][sym]
    # wire doors for new cards
    for h in cards:
        sym = h["sym"]
        if sym in state["doors"]:
            continue  # door already live from a prior night
        entry, stop, target = h["plan_entry"], h["plan_stop"], h["plan_target"]
        risk_sh = int(5000 / max(entry - stop, 0.01))
        notional = min(100000, risk_sh * entry)
        shares = int(notional / entry)
        msg = (f"A-LIST DOOR: {sym.split(':')[-1]} at plan entry {entry} "
               f"(readiness {h['readiness']['score']}). Plan: ~{shares}sh, stop {round(stop,2)} "
               f"(${int((entry-stop)*shares)} risk), checkpoint {round(target,2)}. "
               f"VERIFY earnings + gate-recheck + sizing per protocol, then ACT or PASS - "
               f"verdict gets logged either way.")
        exch_sym = h.get("full_sym") or ("NASDAQ:" + sym if ":" not in sym else sym)
        actions.append({"op": "create", "sym": exch_sym, "level": entry, "msg": msg, "tag": sym})
    # audit fire-state of surviving doors (conversion tracking)
    for sym, door in state.get("doors", {}).items():
        actions.append({"op": "audit", "alert_id": door["alert_id"], "sym": sym})

    # forced-verdict slots
    verdicts = []
    if VERDICTS.exists():
        verdicts = json.loads(VERDICTS.read_text())
    existing = {(v["date"], v["sym"]) for v in verdicts}
    for h in cards:
        if (date, h["sym"]) not in existing:
            verdicts.append({"date": date, "sym": h["sym"],
                             "readiness": h["readiness"]["score"],
                             "plan_entry": h["plan_entry"], "plan_stop": h["plan_stop"],
                             "verdict": "PENDING", "reason": "",
                             "grade_at": "+1w and +1m vs plan entry"})

    # STRUCTURE TAG (added 8/6 after the BA-vs-GE post-mortem: BA was called
    # "the GE profile" when GE's defining trait - band width in the 2nd
    # percentile - was absent from BA entirely. A card may never be described
    # as a coil without the compression to prove it.)
    import re as _re
    def structure(h):
        drv = str((h.get("readiness") or {}).get("driver", ""))
        m = _re.search(r"band width in the (\d+)(?:st|nd|rd|th) percentile", drv)
        if m:
            p = int(m.group(1))
            if p <= 25:
                return f"COILED (band width {p}th pctile - GE-type compression)"
            return f"NEITHER (band width {p}th pctile - middling)"
        g = h.get("gates") or {}
        di = (g.get("plus_di") or 0) - (g.get("minus_di") or 0)
        return (f"POST-BREAKOUT (no compression component; DI margin {di:.1f} = "
                f"{'move already mature' if di > 10 else 'momentum just turning'})")

    print(f"A-LIST {date} (from {src.name}): "
          + (", ".join(f"{h['sym']}(r{h['readiness']['score']})" for h in cards) or "EMPTY - no eligible passers"))
    for h in cards:
        print(f"  {h['sym']:<6} entry {h['plan_entry']} stop {round(h['plan_stop'],2)} "
              f"target {round(h['plan_target'],2)} | STRUCTURE: {structure(h)}")
        print(f"         driver: {str(h['readiness'].get('driver',''))[:88]}")
    funnel["structure_tags"] = {h["sym"]: structure(h) for h in cards}
    if dry:
        print(f"[dry-run] would wire {sum(1 for a in actions if a['op']=='create')} door(s), "
              f"delete {sum(1 for a in actions if a['op']=='delete')}")
        return 0

    VERDICTS.write_text(json.dumps(verdicts, indent=1))
    if actions:
        DOOR_ACTIONS.write_text(json.dumps(actions, indent=1))
        rc = subprocess.run(["node", str(REPO / "scripts" / "wire_door_alerts.mjs")],
                            capture_output=True, text=True, timeout=180)
        print(rc.stdout.strip())
        if rc.returncode != 0:
            print("DOOR WIRING FAILED:", rc.stderr.strip()[:300])
        else:
            results = json.loads(DOOR_ACTIONS.read_text()) if DOOR_ACTIONS.exists() else []
            for r in results:
                if r.get("op") == "create" and r.get("alert_id"):
                    state["doors"][r["tag"]] = {"alert_id": r["alert_id"], "level": r["level"],
                                                "wired": date}
                    funnel["doors_wired"] += 1
                if r.get("op") == "audit" and r.get("fired"):
                    state["doors"].get(r["sym"], {})["fired"] = r["fired"]
    state["date"] = date
    STATE.write_text(json.dumps(state, indent=1))
    (REPO / "reports" / f"funnel-{date}.json").write_text(json.dumps(funnel, indent=1))
    print(f"funnel: {funnel['fresh']} fresh -> {funnel['full_passers']} passers -> "
          f"{len(cards)} A-list -> {funnel['doors_wired']} new doors")
    return 0


if __name__ == "__main__":
    sys.exit(main())
