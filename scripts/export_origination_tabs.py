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

    # Tracker source = recommendations_log.csv (clean header) - the xlsx TRACKER
    # tab has a decorative layout that defeats column sniffing (learned 7/19).
    tracker, tracker_note = [], ""
    reco_csv = os.path.join(os.path.dirname(XLSX), "recommendations_log.csv")
    if os.path.exists(reco_csv):
        import csv
        with open(reco_csv, newline="", encoding="utf-8-sig", errors="replace") as f:
            reader = csv.DictReader(f)
            fields = reader.fieldnames or []
            low = [c.lower() if c else "" for c in fields]
            tick_col = next((fields[i] for i, c in enumerate(low) if "ticker" in c or "symbol" in c), None)
            date_col = next((fields[i] for i, c in enumerate(low) if "date" in c or c == "day"), None)
            price_col = next((fields[i] for i, c in enumerate(low)
                              if "price" in c or "entry" in c or "close" in c or c.endswith("px") or "ref" in c), None)
            if tick_col:
                seen = set()
                for row in reader:
                    val = str(row.get(tick_col) or "").strip().upper().split(":")[-1]
                    if not TICKER_RE.match(val) or val in seen:
                        continue  # keep FIRST occurrence = earliest recommendation
                    seen.add(val)
                    rec = {"sym": val}
                    if date_col:
                        rec["rec_date"] = str(row.get(date_col) or "").strip()
                    if price_col:
                        try:
                            rec["rec_price"] = float(str(row.get(price_col)).replace("$", "").replace(",", ""))
                        except (TypeError, ValueError):
                            pass
                    tracker.append(rec)
                if not (date_col and price_col):
                    tracker_note = f"(date/price columns not fully identified - headers: {', '.join(map(str, fields))})"
            else:
                tracker_note = f"(no ticker column found in recommendations_log.csv - headers: {', '.join(map(str, fields))})"
    else:
        tracker_note = "(recommendations_log.csv not found)"

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
    lines.append(f"## Tracker — logged recommendations, exit-watch only ({len(tracker)})")
    lines.append(", ".join(r["sym"] for r in tracker) if tracker else (tracker_note or "(empty)"))
    if tracker_note and tracker:
        lines.append(tracker_note)
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
    print(f"Tracker (exit-watch): {len(tracker)} tickers {tracker_note}".rstrip())
    if missing:
        print(f"WARNING — tabs not found in xlsx: {', '.join(missing)} "
              f"(available sheets: {', '.join(wb.sheetnames)})")
    print(f"Written: {OUT}")


if __name__ == "__main__":
    main()
