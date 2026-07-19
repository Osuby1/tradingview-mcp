#!/usr/bin/env python3
"""Export the origination scan's actionable tabs into the repo for "run the universe".

Reads Documents/Equities_Scanner/origination_scan.xlsx (the stage2_leader_scanner_v3
output) and writes watchlists/origination-tabs.md with the tickers from the
Buy Zone / Fresh Ignitions / Coiled tabs, so the run-the-universe command can
merge them into the O.G Chandelier scan universe.

Run right after the daily scan:
    python stage2_leader_scanner_v3.py && python <repo>/scripts/export_origination_tabs.py
or standalone any time after the xlsx exists. Robust to tab-name and ticker-column
naming variations; skips missing tabs with a warning instead of failing.
"""
import datetime
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
XLSX = os.path.join(os.path.expanduser("~"), "Documents", "Equities_Scanner", "origination_scan.xlsx")
OUT = os.path.join(REPO, "watchlists", "origination-tabs.md")

# case-insensitive substring match per target tab
TAB_PATTERNS = {"Buy Zone": "buy", "Fresh Ignitions": "ignit", "Coiled": "coil"}
# tracked past recommendations - exported separately (exit-watch, NOT merged into the buy-scan universe)
TRACKER_PATTERN = "track"
TICKER_RE = re.compile(r"^[A-Z][A-Z0-9.\-]{0,6}$")


def sheet_tickers(ws):
    """Pull tickers from a worksheet: prefer a Ticker/Symbol column, else column A."""
    rows = list(ws.iter_rows(values_only=True))
    if not rows:
        return []
    header = [str(c).strip().lower() if c is not None else "" for c in rows[0]]
    col = 0
    for i, h in enumerate(header):
        if "ticker" in h or "symbol" in h:
            col = i
            break
    out = []
    for row in rows[1:]:
        if col >= len(row) or row[col] is None:
            continue
        val = str(row[col]).strip().upper()
        val = val.split(":")[-1]  # strip any EXCHANGE: prefix
        if TICKER_RE.match(val) and val not in out:
            out.append(val)
    return out


def main():
    try:
        from openpyxl import load_workbook
    except ImportError:
        sys.exit("openpyxl not installed — pip install openpyxl")
    if not os.path.exists(XLSX):
        sys.exit(f"Scan output not found: {XLSX} — run the origination scan first.")

    wb = load_workbook(XLSX, read_only=True, data_only=True)
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(XLSX))
    tabs, missing = {}, []
    for label, pat in TAB_PATTERNS.items():
        match = next((n for n in wb.sheetnames if pat in n.lower()), None)
        if match is None:
            missing.append(label)
            continue
        tabs[label] = sheet_tickers(wb[match])

    tracker_match = next((n for n in wb.sheetnames if TRACKER_PATTERN in n.lower()), None)
    tracker = sheet_tickers(wb[tracker_match]) if tracker_match else []

    all_syms = sorted({s for syms in tabs.values() for s in syms})
    lines = [
        f"# Origination scan tabs — exported {datetime.date.today().isoformat()}",
        "",
        f"Source: origination_scan.xlsx (modified {mtime:%Y-%m-%d %H:%M}). "
        "Feeds the run-the-universe command: these tickers are merged into the "
        "O.G Chandelier scan universe alongside the three watchlists.",
        "",
    ]
    for label in TAB_PATTERNS:
        syms = tabs.get(label, [])
        lines.append(f"## {label} ({len(syms)})")
        lines.append(", ".join(syms) if syms else "(tab not found)" if label in missing else "(empty)")
        lines.append("")
    lines.append(f"## Tracker — open recommendations, exit-watch only ({len(tracker)})")
    lines.append(", ".join(tracker) if tracker else
                 "(Tracker tab not found)" if tracker_match is None else "(empty)")
    lines.append("")
    lines += [
        "```json",
        json.dumps(
            {"exported": datetime.date.today().isoformat(),
             "xlsx_modified": mtime.strftime("%Y-%m-%d %H:%M"),
             "tabs": tabs, "all": all_syms, "tracker": tracker},
            indent=1),
        "```",
        "",
    ]
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # dated archive of the scanner's xlsx (it overwrites itself daily)
    import shutil
    arch_dir = os.path.join(REPO, "reports")
    os.makedirs(arch_dir, exist_ok=True)
    arch = os.path.join(arch_dir, f"origination_scan_{datetime.date.today().isoformat()}.xlsx")
    try:
        shutil.copy2(XLSX, arch)
        print(f"Archived: {arch}")
    except OSError as e:
        print(f"WARNING: dated xlsx archive failed: {e}")

    print(f"Exported {len(all_syms)} unique tickers "
          f"({', '.join(f'{k}: {len(v)}' for k, v in tabs.items())})")
    if missing:
        print(f"WARNING — tabs not found in xlsx: {', '.join(missing)} "
              f"(available sheets: {', '.join(wb.sheetnames)})")
    print(f"Written: {OUT}")


if __name__ == "__main__":
    main()
