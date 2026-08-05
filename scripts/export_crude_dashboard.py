"""Export the key signals from Omar's Crude_Fundamental_Dashboard workbook
into research/crude-dashboard-snapshot.md so the cloud morning-brief writer
(which has no Excel) can read the model's latest baseline.

Run after every workbook refresh (weekly, post-EIA Wednesday):
  python scripts/export_crude_dashboard.py            # newest Downloads copy
  python scripts/export_crude_dashboard.py <path.xlsx>  # explicit file
then commit + push research/crude-dashboard-snapshot.md to fork main.
"""
import glob
import os
import sys
from pathlib import Path

import openpyxl

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "research" / "crude-dashboard-snapshot.md"
DOWNLOADS = Path.home() / "Downloads"


def newest_workbook() -> Path:
    cands = [p for p in glob.glob(str(DOWNLOADS / "Crude_Fundamental_Dashboard*.xlsx"))
             if not os.path.basename(p).startswith("~$")]
    if not cands:
        sys.exit("No Crude_Fundamental_Dashboard*.xlsx in Downloads")
    return Path(max(cands, key=os.path.getmtime))


def fmt(v, nd=2):
    if v is None:
        return "n/a"
    if isinstance(v, (int, float)):
        return f"{v:,.{nd}f}".rstrip("0").rstrip(".") if isinstance(v, float) else f"{v:,}"
    return str(v).strip()


def rows_of(ws):
    return [list(r) for r in ws.iter_rows(values_only=True)]


def find_row(rows, label, col=0):
    for r in rows:
        if r and r[col] is not None and label.lower() in str(r[col]).lower():
            return r
    return None


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else newest_workbook()
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    lines = []
    add = lines.append

    inputs = rows_of(wb["Inputs"])
    asof = find_row(inputs, "As-of date")
    asof_val = fmt(asof[1]) if asof else "unknown"
    add("# Crude Fundamental Dashboard - snapshot for the morning-brief writer")
    add(f"Source workbook: {src.name} | model as-of: {asof_val}")
    add("This is Omar's own fair-value model (weekly refresh). The daily brief")
    add("re-sources these metrics fresh each morning and reports where the")
    add("MARKET has moved vs this baseline. Stale vs fresh must be labeled.")
    add("")

    add("## Fair-value signals (Dashboard tab)")
    add("| Instrument | Market | Fair Value | Mispricing | Signal | Threshold |")
    add("|---|--:|--:|--:|---|--:|")
    for r in rows_of(wb["Dashboard"]):
        if r and r[0] and any(k in str(r[0]) for k in ("M1-M2", "WTI minus Brent")) and r[1] is not None:
            add(f"| {fmt(r[0])} | {fmt(r[1])} | {fmt(r[2])} | {fmt(r[3])} | {fmt(r[4])} | {fmt(r[5])} |")
    add("")
    add("### Key model drivers")
    drows = rows_of(wb["Dashboard"])
    for label in ("Cushing Z-score", "Cushing capacity utilization", "OECD commercial inventory Z-score",
                  "OPEC+ effective spare capacity", "Full carry cost", "WTI backwardation depth",
                  "Brent backwardation depth"):
        r = find_row(drows, label)
        if r:
            add(f"- {fmt(r[0])}: **{fmt(r[1])}** ({fmt(r[2])})")
    add("")

    add("## Heavy-light differentials (fair value vs market)")
    add("| Grade | Market | FV | Mispricing | Signal |")
    add("|---|--:|--:|--:|---|")
    for r in rows_of(wb["Heavy-Light Diffs"]):
        if r and r[0] and str(r[0]).split(" ")[0] in ("ASCI", "WCS", "Maya", "Mars", "SGC") and r[1] is not None:
            add(f"| {fmt(r[0])} | {fmt(r[1])} | {fmt(r[2])} | {fmt(r[3])} | {fmt(r[4])} |")
    add("")

    add("## East-West arb")
    ew = rows_of(wb["East-West Arb"])
    for label in ("Brent minus Dubai EFS", "Dubai geopolitical premium", "Aramco Official Selling Price signal"):
        r = find_row(ew, label)
        if r:
            add(f"- {fmt(r[0])}: **{fmt(r[1])}** " + (f"(FV {fmt(r[2])}, {fmt(r[4])})" if len(r) > 4 and r[4] else f"({fmt(r[2])})"))
    add("")

    add("## Crack spreads (market vs FV)")
    add("| Crack | Market | FV | Mispricing | Signal | Region |")
    add("|---|--:|--:|--:|---|---|")
    for r in rows_of(wb["Crack Spreads"]):
        if r and r[0] and any(k in str(r[0]) for k in ("3-2-1", "Gasoil minus Dubai", "Complex Margin")) and r[1] is not None:
            add(f"| {fmt(r[0])} | {fmt(r[1])} | {fmt(r[2])} | {fmt(r[3])} | {fmt(r[4])} | {fmt(r[6]) if len(r) > 6 else ''} |")
    add("")

    add("## Inventory tracker (WPSR week in model)")
    inv = rows_of(wb["Inventory Tracker"])
    for label in ("US crude C+C", "Cushing", "US gasoline", "US distillate", "US SPR", "Days of US cover"):
        r = find_row(inv, label)
        if r:
            add(f"- {fmt(r[0])}: level {fmt(r[1])} | WoW {fmt(r[2])} | note: {fmt(r[6]) if len(r) > 6 and r[6] else fmt(r[3])}")
    add("")
    add("### Floating storage by origin (kbbl)")
    started = False
    for r in inv:
        if r and r[0] and "FLOATING STORAGE" in str(r[0]).upper():
            started = True
            continue
        if started:
            if r and r[0] and str(r[0]).strip() in ("Iran", "Russia", "China", "Other"):
                add(f"- {fmt(r[0])}: {fmt(r[1])} (WoW {fmt(r[2])}, vs 5yr {fmt(r[3])}) {fmt(r[4]) if len(r) > 4 and r[4] else ''}")
            elif r and r[0] and str(r[0]).strip() and str(r[0]).strip() not in ("Origin",):
                break
    add("")

    add("## Demand engine composites (triangulated)")
    tri = rows_of(wb["Triangulation"])
    add("| Data point | Composite | Confidence |")
    add("|---|--:|---|")
    grab = False
    for r in tri:
        if r and r[0] and "Data Point" in str(r[0]):
            grab = True
            continue
        if grab:
            if r and r[0] and "DETAIL" in str(r[0]).upper():
                break
            if r and r[0] and r[1] is not None:
                add(f"| {fmt(r[0])} | {fmt(r[1])} | {fmt(r[5]) if len(r) > 5 else ''} |")
    add("")

    add("## Aramco OSP model")
    for r in rows_of(wb["OSP Predictions"]):
        if r and r[0] and str(r[0]).startswith("Arab") and r[1] is not None:
            add(f"- {fmt(r[0])}: current {fmt(r[1])} -> predicted {fmt(r[2])} ({fmt(r[4])}, conviction {fmt(r[5])})")
    add("")

    add("## Trade signal thresholds (Methodology tab)")
    add("WTI M1-M2 +/-$0.25 | Brent M1-M2 +/-$0.30 | WTI-Brent +/-$0.50 -")
    add("mispricing outside the band = model sees an edge; inside = no edge.")
    add("")
    add("## Triangulation discipline (carry into the brief)")
    add("Source tiers: T1 satellite/AIS (Kpler, Vortexa, Kayrros, Cirium, TSA)")
    add("> T2 official aggregations (IEA, IATA, PPAC, EIA STEO) > T3 surveys")
    add("(JLC teapots, OPEC MOMR secondary) > T4 cross-check only (China NBS).")
    add("When sources diverge materially, confidence is LOW - the dashboard's")
    add("rule is DO NOT TRADE on LOW-confidence data points; the brief should")
    add("flag them the same way.")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT} from {src} (model as-of {asof_val})")


if __name__ == "__main__":
    main()
