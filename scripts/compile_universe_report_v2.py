#!/usr/bin/env python3
"""Compile the run-the-universe results into a rich Excel workbook (v3).

v3 (2026-07-22): rebuilt on scripts/scan_workbook_style.py after Omar rejected
the v2 layout. Every column now carries a plain-English hover tooltip, tabs are
numbered in reading order, long notes moved out of a 46-wide cell onto their own
sheet, and data-quality findings are severity-ranked instead of being eleven
identical-looking rows of prose.

Reads:
  - watchlists/universe-results-<date>.json  (all_names + scanner_enrich; hits/verdicts)
  - reports/origination_scan_<date>.xlsx     (Score/Grade/Category join, optional)
  - watchlists/rotation-radar-state.md       (radar states, optional)
  - watchlists/universe-context-<date>.json  (market context lines, optional)

Usage: python scripts/compile_universe_report_v2.py [YYYY-MM-DD]
Writes: reports/universe_<date>.xlsx
"""
import datetime
import json
import os
import re
import sys

from openpyxl import Workbook, load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scan_workbook_style import (  # noqa: E402
    Col, write_table, readme_sheet, data_quality_sheet, notes_sheet,
    verdict_fill, split_note, safe, style_header_row,
    FMT_PRICE, FMT_PCT, FMT_X, BOLD, RED_FONT, GREEN, AMBER,
)

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
    for ws0 in wb0.worksheets:
        if not re.match(r"\d ", ws0.title):
            continue
        rows0 = ws0.iter_rows(values_only=True)
        header = [str(c) if c else "" for c in next(rows0)]
        try:
            it, isc, igr, icat = (header.index(x) for x in
                                  ("Ticker", "Score (0-100)", "Grade", "Category / What To Do"))
        except ValueError:
            continue
        for row in rows0:
            if row[it] and str(row[it]).strip() not in orig:
                orig[str(row[it]).strip()] = {"score": row[isc], "grade": row[igr],
                                              "cat": row[icat], "tab": ws0.title}

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
                radar_lines.append({"group": g.get("group", g.get("name", "?")),
                                    "state": g.get("state", "?"), "accel": g.get("accel"),
                                    "w": g.get("perf_w"), "m1": g.get("perf_1m"),
                                    "m6": g.get("perf_6m")})
        except Exception:
            pass

ctx = {}
cpath = os.path.join(REPO, "watchlists", f"universe-context-{DATE}.json")
if os.path.exists(cpath):
    ctx = json.load(open(cpath))

WRITTEN = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
ENRICH_AS_OF = res.get("scanner_enrich_asof", "n/a")
wb = Workbook()


def classify(note):
    """Legacy data-quality strings are plain prose. Rank them so the dangerous
    ones cannot hide. The 7/21 watchlist-truncation bug was recorded and still
    missed because every note looked equally important."""
    u = note.upper()
    if any(k in u for k in ("PARTIAL", "NOT SCANNED", "WAS WRONG", "STALE",
                            "CORRECTION", "ARE VOID", "OFF-STANDARD")):
        sev, act = "BLOCKER", "Fix before trusting the coverage or numbers in this run."
    elif any(k in u for k in ("SKIPPED", "DID NOT RUN", "REPAINT", "VERIFY",
                              "ARTIFACT", "APPROXIMATE", "NOT TRADEABLE")):
        sev, act = "WARNING", "Confirm on the live chart before sizing anything."
    else:
        sev, act = "INFO", ""
    area = ("Coverage" if "WATCHLIST" in u or "SCANNED" in u else
            "Data feed" if any(k in u for k in ("CHART", "PRICE", "HEIKIN", "SPLIT")) else
            "Signal quality" if any(k in u for k in ("REPAINT", "LABEL", "SIGNAL")) else
            "Pipeline")
    return {"severity": sev, "area": area, "finding": note,
            "impact": "", "action": act}


# ---------------------------------------------------------------- READ ME ---
ws = wb.active
ws.title = "READ ME FIRST"
readme_sheet(
    ws,
    f"RUN-THE-UNIVERSE WORKBOOK - {DATE}",
    stamps=[("Scan data as of", f"{DATE} close (live chart reads)"),
            ("Scanner enrich as of", ENRICH_AS_OF),
            ("Workbook written", f"{WRITTEN} local"),
            ("Generated by", "compile_universe_report_v2.py (v3 layout)")],
    what_this_is=[
        "Every stock on the watchlists, plus the origination scanner's actionable names,",
        "read through the O.G Chandelier stack (Chandelier Exit 1/2 + ZLSMA-50 + Magical",
        "OB/OS) on the LIVE chart, on CANDLES.",
        "",
        "The origination scanner finds candidates. THIS run tells you which ones actually",
        "triggered, which ones the gates rejected, and why.",
    ],
    sheet_guide=[
        ("1 - Market & Rotation", "The tape and where money is flowing. Read this first.",
         "If the regime is hostile, everything below gets smaller size or no size."),
        ("2 - Fresh Buys", "Every buy signal 5 sessions old or newer.",
         "The Verdict column is the decision. Green = actionable, amber = conflicted, red = blocked."),
        ("3 - Plans", "The sized trades: entry, stop, share count, dollar risk, targets, alerts."),
        ("4 - Blocked", "Fresh signals the gates rejected, and which gate did it.",
         "These are NOT trades. The reason column is the point of this tab."),
        ("5 - Sell Mode", "Names the indicator has in downtrend. Rule 10: do not buy these."),
        ("6 - Tracker Broken", "Past recommendations whose trend has broken. Exit / bank-it flags."),
        ("7 - Notes & Decisions", "The full reasoning per name, with room to actually read it.",
         "Anything that reversed or was downgraded since the last run is flagged here."),
        ("8 - Data Quality", "What was broken or partial in this run, ranked by severity.",
         "READ THE RED ROWS. A BLOCKER means conclusions in this file may be wrong."),
        ("9 - Run Summary", "Counts and run metadata."),
    ],
    how_to_act=[
        "1. Check tab 8 for BLOCKERS first. If coverage was partial, absence of a name",
        "   proves nothing - it may simply never have been scanned.",
        "2. Read the regime on tab 1. It sets your size for everything else.",
        "3. Work tab 2 top-down. Only green Verdicts are candidates.",
        "4. Cross-check each candidate against tab 5 - a sell-mode name is never a buy.",
        "5. Size it on tab 3. If the stop is wider than the risk unit allows, skip it.",
    ],
    key_readings=[
        ("Magical (CCI-20)", "Above +100 = overbought, below -100 = oversold. NOTE: measured "
                             "2026-07-22 across 1,725 signals, this cut does NOT separate "
                             "returns (0.03pt over 21 days). Treat as context, not a veto."),
        ("ZLSMA-50", "The trend line. Price below it on a buy signal is a structural fail."),
        ("Chandelier Exit", "Flips BUY/SELL. The label price is the STOP level, not an entry."),
        ("Regime PASS", "Above a rising 200-day and beating SPY -> normal size."),
        ("Regime REPAIR", "Below the 200-day -> starter size only."),
        ("Regime DEEP-FAIL", "More than 10% below the 200-day -> watch only, no size."),
    ],
)

# ------------------------------------------------------- 1 Market & Rotation ---
ws = wb.create_sheet("1 - Market & Rotation")
style_header_row(ws, ["Indicator", "Reading", "What This Means For Today"],
                 ["The market measure being quoted.",
                  "Its current value.",
                  "Plain-English read: what this changes about how you trade today."],
                 [34, 18, 92], freeze="A2", autofilter=False)
for row in ctx.get("market_lines", []):
    ws.append([safe(x) for x in row])
ws.append([])
ws.append(["ROTATION RADAR"])
ws.cell(row=ws.max_row, column=1).font = BOLD
if radar_lines:
    hdr = ws.max_row + 1
    ws.append(["Group", "State", "Acceleration", "1 Week %", "1 Month %", "6 Month %"])
    for c in ws[hdr]:
        c.font = BOLD
    for r in radar_lines:
        ws.append([safe(r["group"]), safe(r["state"]), r["accel"], r["w"], r["m1"], r["m6"]])
        fill = GREEN if r["state"] == "IGNITING" else AMBER if r["state"] == "ROLLING" else None
        if fill:
            for c in ws[ws.max_row]:
                c.fill = fill
else:
    ws.append(["(rotation radar did not run - see Data Quality tab)"])
for row in ctx.get("rotation_commentary", []):
    ws.append([safe(row[0] if isinstance(row, list) else row)])

# ------------------------------------------------------------ 2 Fresh Buys ---
FRESH_COLS = [
    Col("sym", "Ticker", 9, "The stock symbol."),
    Col("company", "Company", 30, "Company name, so you know what you are buying."),
    Col("sector", "Sector", 20, "Sector - use it to spot when several signals are the same bet."),
    Col("signal_date", "Signal Date", 12, "The session the Chandelier flipped to BUY."),
    Col("age", "Sessions Old", 11,
        "How many sessions ago the signal fired. 0 = today's bar, which can still "
        "repaint before the close. Anything over 5 is not fresh."),
    Col("last", "Price", 10, "Latest price from the live feed.", FMT_PRICE),
    Col("stop", "Chandelier Stop", 13,
        "The Chandelier Exit level. This is the STOP, not an entry price - a common "
        "misreading. Price minus this level is your risk per share.", FMT_PRICE),
    Col("risk_pct", "Stop Distance %", 13,
        "How far the stop sits below price, as a percent. This decides your position "
        "size. Anything much over ~10% means a tiny position or no trade.", FMT_PCT),
    Col("magical", "Overbought / Oversold (CCI-20)", 16,
        "20-period CCI. Above +100 = stretched, below -100 = washed out. Measured "
        "2026-07-22: this does NOT predict returns, so it is context and never the "
        "sole reason to reject a name.", FMT_PCT),
    Col("zlsma", "Trend Line (ZLSMA-50)", 14,
        "Zero-lag moving average. Price BELOW this on a buy signal is a structural "
        "failure - the trend has not turned yet.", FMT_PRICE),
    Col("rsi", "Heat Gauge (RSI)", 11, "Daily RSI. Over 70 is hot, under 30 is cold.", FMT_PCT),
    Col("relvol", "Volume vs Normal", 12,
        "Today's volume against its average. 2.0 = twice normal interest. Real moves "
        "come with volume; a breakout on dry volume usually fails.", FMT_X),
    Col("pct52", "% of 52-Week High", 13,
        "100% means at the yearly high. Leaders live within about 15% of it.", FMT_PCT),
    Col("pct200", "% vs 200-Day Average", 14,
        "Above zero = long-term uptrend. Below = you are buying inside a downtrend.", FMT_PCT),
    Col("adx", "Trend Strength (ADX)", 12,
        "Above 20-25 means a real trend exists. Below that the move is noise.", FMT_PCT),
    Col("score", "Origination Score", 12,
        "The origination scanner's 0-100 quality score, if it also found this name.", FMT_PCT),
    Col("grade", "Origination Grade", 12, "A+ / A / B / C / SKIP from the origination scan."),
    Col("regime", "Regime", 12, "PASS = normal size, REPAIR = starter only, DEEP-FAIL = no size."),
    Col("verdict", "VERDICT", 26,
        "The decision the frozen rule set reached. Green = actionable, amber = "
        "conflicted (half size at most), red = blocked."),
    Col("why", "Why (short)", 55,
        "The one-line reason for the verdict. The FULL argument is on the "
        "'7 - Notes & Decisions' tab - this column is deliberately short so the "
        "table stays readable."),
]


def fresh_rows():
    out = []
    for sym, h in hits.items():
        e, o = enrich.get(sym, {}), orig.get(sym, {})
        last, stop = h.get("last"), h.get("ce_label") or h.get("flip_level")
        risk = round((last - stop) / last * 100, 1) if (last and stop and last > stop) else None
        _, why, _ = split_note(h.get("note"))
        out.append({
            "sym": sym, "company": e.get("description"), "sector": e.get("sector"),
            "signal_date": h.get("signal_date_est"), "age": h.get("bars_back"),
            "last": last, "stop": stop, "risk_pct": risk,
            "magical": h.get("magical"), "zlsma": h.get("zlsma"),
            "rsi": e.get("rsi") and round(e["rsi"], 1),
            "relvol": e.get("relvol") and round(e["relvol"], 2),
            "pct52": e.get("pct_of_52wk_high"), "pct200": e.get("pct_vs_200d"),
            "adx": e.get("adx") and round(e["adx"], 1),
            "score": o.get("score"), "grade": o.get("grade"),
            "regime": h.get("regime"), "verdict": h.get("verdict"), "why": why,
        })
    return sorted(out, key=lambda r: (str(r["verdict"] or "").startswith("BLOCKED"),
                                      r["age"] if r["age"] is not None else 99))


write_table(wb.create_sheet("2 - Fresh Buys"), FRESH_COLS, fresh_rows(),
            row_fill=verdict_fill)

# ---------------------------------------------------------------- 3 Plans ---
PLAN_COLS = [
    Col("a", "Ticker", 9, "The stock symbol."),
    Col("b", "Type", 16, "Order type - buy-stop, limit, or starter."),
    Col("c", "Entry", 10, "The price you are willing to pay.", FMT_PRICE),
    Col("d", "Stop", 10, "Where the trade is wrong and you are out.", FMT_PRICE),
    Col("e", "Size", 18, "Dollar size and share count."),
    Col("f", "Risk $", 10, "Dollars lost if the stop hits. Should be about 0.5% of the account.", FMT_PRICE),
    Col("g", "Targets", 16, "Where you take profit, and the reward-to-risk that implies."),
    Col("h", "Earnings Gate", 26,
        "Next earnings date and whether it blocks or shrinks this trade. Never full "
        "size into a report."),
    Col("i", "Alert", 14, "The alert ID armed for this level, so the trigger reminds you why."),
    Col("j", "Plan Notes", 60, "Conditions attached to the plan - what must be true to take it."),
]
plan_rows = [dict(zip("abcdefghij", (list(r) + [None] * 10)[:10]))
             for r in ctx.get("plans", [])]
write_table(wb.create_sheet("3 - Plans"), PLAN_COLS, plan_rows)

# -------------------------------------------------------------- 4 Blocked ---
BLOCK_COLS = [
    Col("sym", "Ticker", 9, "The stock symbol."),
    Col("company", "Company", 30, "Company name."),
    Col("signal_date", "Signal Date", 12, "When the buy signal fired."),
    Col("magical", "Overbought / Oversold (CCI-20)", 16, "20-period CCI at the read.", FMT_PCT),
    Col("regime", "Regime", 12, "PASS / REPAIR / DEEP-FAIL."),
    Col("gate", "Which Gate Blocked It", 30,
        "The specific rule that rejected this name. If you disagree with the rule, "
        "this is the column that tells you which rule to argue with."),
    Col("why", "Why (short)", 60, "One-line explanation. Full reasoning on the Notes tab."),
]
block_rows = []
for sym, h in hits.items():
    v = str(h.get("verdict") or "")
    if v.startswith("BLOCKED"):
        e = enrich.get(sym, {})
        _, why, _ = split_note(h.get("note"))
        block_rows.append({"sym": sym, "company": e.get("description"),
                           "signal_date": h.get("signal_date_est"),
                           "magical": h.get("magical"), "regime": h.get("regime"),
                           "gate": v.replace("BLOCKED: ", ""), "why": why})
write_table(wb.create_sheet("4 - Blocked"), BLOCK_COLS, block_rows)

# ------------------------------------------------------------ 5 Sell Mode ---
SELL_COLS = [
    Col("sym", "Ticker", 9, "The stock symbol."),
    Col("company", "Company", 32, "Company name."),
    Col("sector", "Sector", 22, "Sector."),
    Col("last", "Price", 10, "Latest price.", FMT_PRICE),
    Col("magical", "Overbought / Oversold (CCI-20)", 16, "20-period CCI.", FMT_PCT),
    Col("pct200", "% vs 200-Day Average", 14, "How far below its long-term average it is.", FMT_PCT),
    Col("rsi", "Heat Gauge (RSI)", 11, "Daily RSI.", FMT_PCT),
]
sell_rows = [{"sym": s, "company": enrich.get(s, {}).get("description"),
              "sector": enrich.get(s, {}).get("sector"),
              "last": allrows.get(s, {}).get("last"),
              "magical": allrows.get(s, {}).get("magical"),
              "pct200": enrich.get(s, {}).get("pct_vs_200d"),
              "rsi": enrich.get(s, {}).get("rsi") and round(enrich[s]["rsi"], 1)}
             for s in res.get("sell_mode", [])]
write_table(wb.create_sheet("5 - Sell Mode"), SELL_COLS, sell_rows)

# ------------------------------------------------------- 6 Tracker Broken ---
TRACK_COLS = [
    Col("sym", "Ticker", 9, "The stock symbol."),
    Col("since", "% Since Recommended", 16, "Return since the call was made.", FMT_PCT),
    Col("rec", "Recommended At", 13, "The price when it was recommended.", FMT_PRICE),
    Col("last", "Price Now", 11, "Latest price.", FMT_PRICE),
    Col("magical", "Overbought / Oversold (CCI-20)", 16, "20-period CCI.", FMT_PCT),
    Col("reason", "Why It Broke", 55, "What changed - the trend condition that failed."),
]
tw = res.get("tracker_exit_watch", {})
track_rows = [{"sym": b["sym"], "since": b.get("since_rec_pct"), "rec": b.get("rec"),
               "last": b.get("last"), "magical": b.get("magical"), "reason": b.get("reason")}
              for b in sorted(tw.get("broken", []), key=lambda x: x.get("since_rec_pct") or 0)]
ws = wb.create_sheet("6 - Tracker Broken")
write_table(ws, TRACK_COLS, track_rows)
ws.append([])
ws.append([safe(tw.get("breakage_stat", ""))])
ws.cell(row=ws.max_row, column=1).font = RED_FONT
ws.append([safe(f"Coverage: {tw.get('coverage', '?')} - {tw.get('gap_note', '')}")])

# ------------------------------------------------------ 7 Notes & Decisions ---
note_rows = []
for sym, h in hits.items():
    changed, _, full = split_note(h.get("note"))
    if full:
        note_rows.append({"sym": sym, "verdict": h.get("verdict"),
                          "changed": changed, "reasoning": full})
note_rows.sort(key=lambda r: (not r["changed"], r["sym"]))
notes_sheet(wb.create_sheet("7 - Notes & Decisions"), note_rows)

# ----------------------------------------------------------- 8 Data Quality ---
dq = [classify(q) if isinstance(q, str) else q for q in res.get("data_quality", [])]
data_quality_sheet(wb.create_sheet("8 - Data Quality"), dq)

# ------------------------------------------------------------ 9 Run Summary ---
SUM_COLS = [
    Col("field", "Field", 30, "The run attribute."),
    Col("value", "Value", 110, "Its value for this run."),
]
sum_rows = [
    {"field": "Scan data as of", "value": f"{DATE} close (live chart reads)"},
    {"field": "Scanner enrich as of", "value": ENRICH_AS_OF},
    {"field": "Workbook written", "value": f"{WRITTEN} local"},
    {"field": "Date / variant / system", "value":
        f"{res.get('date')} / {res.get('variant')} / {res.get('system_version')}"},
    {"field": "Universe / scanned / fresh", "value":
        f"{res.get('universe_size')} / {res.get('scanned')} / {res.get('fresh_count')}"},
    {"field": "Sell-mode count", "value": len(res.get("sell_mode", []))},
    {"field": "Blocked count", "value": len(block_rows)},
    {"field": "Combined risk", "value": res.get("combined_risk_new_actives", "")},
    {"field": "Data-quality BLOCKERS", "value":
        sum(1 for d in dq if str(d.get("severity")).upper() == "BLOCKER")},
    {"field": "Run note", "value": res.get("run_note", "")},
]
ws = wb.create_sheet("9 - Run Summary")
write_table(ws, SUM_COLS, sum_rows, autofilter=False)
for n in range(2, ws.max_row + 1):
    ws.row_dimensions[n].height = 44

out = os.path.join(REPO, "reports", f"universe_{DATE}.xlsx")
try:
    wb.save(out)
except PermissionError:
    # The workbook is almost always open in Excel while being reviewed.
    # Write beside it instead of failing the whole run.
    out = os.path.join(REPO, "reports", f"universe_{DATE}_new.xlsx")
    wb.save(out)
    print("NOTE: original was locked (open in Excel) - wrote a copy instead.")
print(f"written {out}")
print(f"  sheets: {len(wb.sheetnames)} | fresh {len(hits)} | blocked {len(block_rows)} "
      f"| notes {len(note_rows)} | dq {len(dq)} "
      f"(BLOCKERS {sum(1 for d in dq if str(d.get('severity')).upper() == 'BLOCKER')})")
