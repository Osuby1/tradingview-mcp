#!/usr/bin/env python3
"""Compile the run-the-universe results into a rich Excel workbook (v2).

Replaces the sparse compile_daily_report.py output. Reads:
  - watchlists/universe-results-<date>.json  (needs all_names + scanner_enrich; hits/verdicts)
  - reports/origination_scan_<date>.xlsx     (Score/Grade/Category join, optional)
  - watchlists/rotation-radar-state.md       (radar states, optional)
  - watchlists/universe-context-<date>.json  (market context lines, optional)

Usage: python scripts/compile_universe_report_v2.py [YYYY-MM-DD]
Writes: reports/universe_<date>.xlsx  (8 sheets, origination-workbook style)
"""
import json
import os
import re
import sys

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = sys.argv[1] if len(sys.argv) > 1 else None
if not DATE:
    cands = sorted(f for f in os.listdir(os.path.join(REPO, "watchlists"))
                   if re.match(r"universe-results-\d{4}-\d{2}-\d{2}\.json$", f))
    DATE = cands[-1][17:-5]

res = json.load(open(os.path.join(REPO, "watchlists", f"universe-results-{DATE}.json")))
enrich = res.get("scanner_enrich", {})
allrows = {r["sym"]: r for r in res.get("all_names", [])}
hits = {h["sym"]: h for h in res.get("hits", [])}

# --- origination join (Score/Grade/Category) ---
orig = {}
opath = os.path.join(REPO, "reports", f"origination_scan_{DATE}.xlsx")
if os.path.exists(opath):
    wb0 = load_workbook(opath, read_only=True)
    for ws in wb0.worksheets:
        if not re.match(r"\d ", ws.title):
            continue
        rows = ws.iter_rows(values_only=True)
        header = [str(c) if c else "" for c in next(rows)]
        try:
            it, isc, igr, icat = (header.index(x) for x in
                                  ("Ticker", "Score (0-100)", "Grade", "Category / What To Do"))
        except ValueError:
            continue
        for row in rows:
            if row[it] and str(row[it]).strip() not in orig:
                orig[str(row[it]).strip()] = {"score": row[isc], "grade": row[igr],
                                              "cat": row[icat], "tab": ws.title}

# --- radar parse ---
radar_lines = []
rpath = os.path.join(REPO, "watchlists", "rotation-radar-state.md")
if os.path.exists(rpath):
    txt = open(rpath, encoding="utf-8").read()
    m = re.search(r"```json\s*(.*?)```", txt, re.S)
    if m:
        try:
            rj = json.loads(m.group(1))
            groups = rj.get("groups", rj if isinstance(rj, list) else [])
            for g in sorted(groups, key=lambda x: -(x.get("accel") or 0)):
                radar_lines.append([g.get("group", g.get("name", "?")), g.get("state", "?"),
                                    g.get("accel"), g.get("perf_w"), g.get("perf_1m"), g.get("perf_6m")])
        except Exception:
            pass

ctx = {}
cpath = os.path.join(REPO, "watchlists", f"universe-context-{DATE}.json")
if os.path.exists(cpath):
    ctx = json.load(open(cpath))

# --- workbook helpers ---
wb = Workbook()
HDR = Font(bold=True, color="FFFFFF")
FILL = PatternFill("solid", fgColor="305496")
RED = Font(bold=True, color="C00000")
GRN = PatternFill("solid", fgColor="C6EFCE")
YEL = PatternFill("solid", fgColor="FFF2CC")

def style_header(ws, ncols, widths):
    for c in ws[1][:ncols]:
        c.font = HDR
        c.fill = FILL
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[ws.cell(row=1, column=i).column_letter].width = w
    ws.freeze_panes = "A2"

def wrap(ws):
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.alignment = Alignment(wrap_text=True, vertical="top")

# 1. READ ME
ws = wb.active
ws.title = "READ ME FIRST"
ws.column_dimensions["A"].width = 110
for line in [
    f"RUN-THE-UNIVERSE WORKBOOK — {DATE}  (auto-written by compile_universe_report_v2.py)",
    "",
    "WHAT THIS IS: every stock Omar follows (3 watchlists) + the origination scanner's actionable tabs,",
    "read through the O.G Chandelier stack (CE 1/2 + ZLSMA-50 + Magical OB/OS) on the LIVE chart.",
    "The origination scanner finds candidates; this run tells you which ones actually TRIGGERED.",
    "",
    "SHEET GUIDE:",
    "  Market & Rotation — the tape and where money is flowing, in plain English. Read this first.",
    "  Fresh Buys — every buy signal <=5 sessions old, enriched with scanner data + origination score.",
    "      Verdict column = what the frozen rule set says to do. ACTIVE = alert armed with a plan.",
    "  Plans — the sized trades: entry, stop, size, dollar risk, targets, earnings gates, alert IDs.",
    "  Blocked — fresh signals the gates rejected, with the reason. These are NOT trades.",
    "  Sell Mode (veto) — names in downtrend per the indicator. Rule 10: do not buy these.",
    "  Tracker Broken — past recommendations whose trend broke (exit/bank-it flags).",
    "  Summary — run stats and data-quality notes.",
    "",
    "KEY READINGS: Magical > +100 = too hot, pullback-only. < -100 = washed out.",
    "Regime: PASS = above rising 200-day + beating SPY -> normal size. REPAIR = below 200-day -> starter.",
    "DEEP-FAIL = >10% below 200-day -> watch only.",
    "Prices from the Heikin-Ashi chart are composites — approximate, not tradeable prints.",
]:
    ws.append([line])
ws["A1"].font = Font(bold=True, size=13)

# 2. Market & Rotation
ws = wb.create_sheet("Market & Rotation")
ws.append(["MARKET & ROTATION", "", "What this means"])
style_header(ws, 3, [34, 18, 90])
for row in ctx.get("market_lines", []):
    ws.append(row)
ws.append([])
ws.append(["ROTATION RADAR (group, state, accel)", "", ""])
ws[ws.max_row][0].font = Font(bold=True)
if radar_lines:
    ws.append(["Group", "State", "Accel", "1W %", "1M %", "6M %"])
    for r in radar_lines:
        ws.append(r)
        if r[1] == "IGNITING":
            for c in ws[ws.max_row]:
                c.fill = GRN
        elif r[1] == "ROLLING":
            for c in ws[ws.max_row]:
                c.fill = YEL
for row in ctx.get("rotation_commentary", []):
    ws.append([row[0] if isinstance(row, list) else row])
wrap(ws)

# 3. Fresh Buys
ws = wb.create_sheet("Fresh Buys")
cols = ["Ticker", "Company", "Sector", "Source", "Signal date", "Last", "Magical", "ZLSMA",
        "RSI", "Vol vs normal", "% of 52wk high", "% vs 200d", "ADX", "1M %", "6M %",
        "Orig Score", "Orig Grade", "Regime", "Verdict", "Notes"]
ws.append(cols)
style_header(ws, len(cols), [8, 30, 20, 12, 11, 9, 9, 9, 7, 11, 12, 10, 7, 8, 8, 10, 9, 10, 30, 46])
for sym, h in hits.items():
    e = enrich.get(sym, {})
    o = orig.get(sym, {})
    row = [sym, e.get("description"), e.get("sector"), h.get("source"), h.get("signal_date_est"),
           h.get("last"), h.get("magical"), h.get("zlsma"), e.get("rsi") and round(e["rsi"], 1),
           e.get("relvol") and round(e["relvol"], 2), e.get("pct_of_52wk_high"),
           e.get("pct_vs_200d"), e.get("adx") and round(e["adx"], 1),
           e.get("p1m") and round(e["p1m"], 1), e.get("p6m") and round(e["p6m"], 1),
           o.get("score"), o.get("grade"), h.get("regime"), h.get("verdict"), h.get("note")]
    ws.append(row)
    v = str(h.get("verdict", ""))
    if v.startswith(("ACTIVE", "NEW ACTIVE")):
        for c in ws[ws.max_row]:
            c.fill = GRN
    elif "CONFLICT" in v:
        for c in ws[ws.max_row]:
            c.fill = YEL
wrap(ws)

# 4. Plans
ws = wb.create_sheet("Plans")
ws.append(["Ticker", "Type", "Entry", "Stop", "Size", "Risk $", "Targets", "Earnings gate", "Alert", "Notes"])
style_header(ws, 10, [8, 16, 10, 9, 18, 9, 14, 24, 12, 60])
for row in ctx.get("plans", []):
    ws.append(row)
wrap(ws)

# 5. Blocked
ws = wb.create_sheet("Blocked")
ws.append(["Ticker", "Company", "Signal date", "Magical", "Regime", "Reason"])
style_header(ws, 6, [8, 30, 11, 9, 10, 80])
for sym, h in hits.items():
    v = str(h.get("verdict", ""))
    if v.startswith("BLOCKED"):
        e = enrich.get(sym, {})
        ws.append([sym, e.get("description"), h.get("signal_date_est"), h.get("magical"),
                   h.get("regime"), v.replace("BLOCKED: ", "") + (" — " + h["note"] if h.get("note") else "")])
wrap(ws)

# 6. Sell Mode veto
ws = wb.create_sheet("Sell Mode (veto)")
ws.append(["Ticker", "Company", "Sector", "Last", "Magical", "% vs 200d", "RSI"])
style_header(ws, 7, [8, 32, 22, 10, 9, 10, 7])
for sym in res.get("sell_mode", []):
    e = enrich.get(sym, {})
    a = allrows.get(sym, {})
    ws.append([sym, e.get("description"), e.get("sector"), a.get("last"), a.get("magical"),
               e.get("pct_vs_200d"), e.get("rsi") and round(e["rsi"], 1)])

# 7. Tracker Broken
ws = wb.create_sheet("Tracker Broken")
tw = res.get("tracker_exit_watch", {})
ws.append(["Ticker", "% since rec", "Rec price", "Last", "Magical", "Reason"])
style_header(ws, 6, [8, 11, 10, 10, 9, 55])
for b in sorted(tw.get("broken", []), key=lambda x: x["since_rec_pct"]):
    ws.append([b["sym"], b["since_rec_pct"], b["rec"], b["last"], b["magical"], b["reason"]])
ws["H1"] = tw.get("breakage_stat", "")
ws["H1"].font = RED
ws["H2"] = f"Coverage: {tw.get('coverage', '?')} — {tw.get('gap_note', '')}"

# 8. Summary
ws = wb.create_sheet("Summary")
ws.append(["Field", "Value"])
style_header(ws, 2, [30, 110])
fresh_n = res.get("fresh_count")
ws.append(["Date / variant / system", f"{res.get('date')} / {res.get('variant')} / {res.get('system_version')}"])
ws.append(["Universe / scanned / fresh", f"{res.get('universe_size')} / {res.get('scanned')} / {fresh_n}"])
ws.append(["Sell-mode count", len(res.get("sell_mode", []))])
ws.append(["Combined risk", res.get("combined_risk_new_actives", "")])
ws.append(["Run note", res.get("run_note", "")])
for q in res.get("data_quality", []):
    ws.append(["Data quality", q])
wrap(ws)

out = os.path.join(REPO, "reports", f"universe_{DATE}.xlsx")
wb.save(out)
print("written", out)
