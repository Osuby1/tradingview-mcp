#!/usr/bin/env python3
"""Morning pack (8/6 speed commitment): the EOD chain pre-computes everything the
morning brief needs so the 8:35 AM build is one file read + one live volley.
Writes reports/morning-pack-<date>.json."""
import json, datetime as dt, sys
from pathlib import Path
REPO = Path(__file__).resolve().parent.parent
date = sys.argv[1] if len(sys.argv) > 1 else dt.date.today().isoformat()
pack = {"built_at": "", "date": date}
try:
    pack["open_book"] = json.loads((REPO/"watchlists"/"open-book.json").read_text())
except Exception as e: pack["open_book"] = f"unreadable: {e}"
for name, path in [("a_list_state","watchlists/a-list-state.json"),
                   ("staged_tickets","watchlists/staged-tickets.json"),
                   ("squeeze_parked","watchlists/squeeze-parked.json"),
                   ("final_hour_marks",f"research/final-hour-marks-{date}.json"),
                   ("funnel",f"reports/funnel-{date}.json")]:
    try: pack[name] = json.loads((REPO/path).read_text())
    except Exception: pack[name] = None
try:
    res = json.loads((REPO/"watchlists"/f"universe-results-{date}.json").read_text())
    pack["kill_lines_and_modes"] = {e["sym"]: {"ce": e.get("ce_mode"), "adx": e.get("adx")}
        for e in res.get("all_names", []) if isinstance(e, dict) and
        e.get("sym") in {p_["sym"] for p_ in pack["open_book"].get("positions", [])} | {"SOUN","HTZ","PLTR","GDX","INDI"}}
    pack["scan_counts"] = {"scanned": res.get("scanned"), "fresh": res.get("fresh_count")}
except Exception: pack["kill_lines_and_modes"] = None
pack["built_at"] = dt.datetime.now().isoformat(timespec="seconds")
out = REPO/"reports"/f"morning-pack-{date}.json"
out.write_text(json.dumps(pack, indent=1))
print(f"morning pack written: {out.name}")
