#!/usr/bin/env python3
"""Compile the day's run-the-universe results into a formatted Excel workbook.

Reads watchlists/universe-results-<date>.json (written by the run-the-universe
command; falls back to the newest one present) and writes
reports/universe_<date>.xlsx with four sheets:
  Fresh Buys & Plans | Blocked | Sell Mode | Summary
Safe to run any time; exits quietly (code 0) if no results file exists yet.
"""
import datetime
import glob
import json
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def newest_results():
    files = sorted(glob.glob(os.path.join(REPO, "watchlists", "universe-results-*.json")))
    return files[-1] if files else None


def main():
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill
    except ImportError:
        sys.exit("openpyxl not installed - pip install openpyxl")

    path = newest_results()
    if not path:
        print("No universe-results-*.json yet - nothing to compile (ok).")
        return
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    date = data.get("date") or os.path.basename(path)[17:27] or datetime.date.today().isoformat()

    wb = Workbook()
    head_font = Font(bold=True, color="FFFFFF")
    head_fill = PatternFill("solid", fgColor="1F4E79")

    def sheet(title, headers, rows, first=False):
        ws = wb.active if first else wb.create_sheet()
        ws.title = title
        ws.append(headers)
        for c in ws[1]:
            c.font, c.fill = head_font, head_fill
        for r in rows:
            ws.append(r)
        for i, h in enumerate(headers, 1):
            width = max([len(str(h))] + [len(str(r[i - 1])) for r in rows if len(r) >= i]) + 2
            ws.column_dimensions[ws.cell(1, i).column_letter].width = min(width, 60)
        ws.freeze_panes = "A2"
        return ws

    hits = data.get("hits", [])
    sheet(
        "Fresh Buys & Plans",
        ["Ticker", "Source", "Signal date", "Last price", "Entry", "Dist %", "Stop",
         "Size", "Risk $", "Targets", "Earnings gate", "Magical", "Regime", "Verdict", "Notes"],
        [[h.get("sym"), h.get("source", "watchlist"), h.get("fresh"), h.get("last"),
          h.get("entry"), h.get("dist_pct"), h.get("stop"), h.get("size"), h.get("risk"),
          h.get("targets"), h.get("earnings"), h.get("magical"), h.get("regime"),
          h.get("verdict"), h.get("note")] for h in hits],
        first=True,
    )
    sheet(
        "Blocked",
        ["Ticker", "Source", "Signal date", "Reason"],
        [[b.get("sym"), b.get("source", "watchlist"), b.get("fresh"), b.get("reason")]
         for b in data.get("blocked", [])],
    )
    sm = data.get("sell_mode", [])
    sheet("Sell Mode (veto)", ["Ticker"], [[s] for s in sm])
    sheet(
        "Summary",
        ["Field", "Value"],
        [["Scan date", date],
         ["Variant", data.get("variant", "?")],
         ["Universe size", data.get("universe_size", "?")],
         ["Fresh buys", len(hits)],
         ["Active plans", sum(1 for h in hits if str(h.get("verdict", "")).lower().startswith("active"))],
         ["Blocked", len(data.get("blocked", []))],
         ["Sell mode", len(sm)],
         ["Combined plan risk $", data.get("combined_risk", "?")],
         ["Notes", data.get("notes", "")]],
    )

    out_dir = os.path.join(REPO, "reports")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, f"universe_{date}.xlsx")
    wb.save(out)
    print(f"Report written: {out}")


if __name__ == "__main__":
    main()
