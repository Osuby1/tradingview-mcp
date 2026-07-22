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
    FMT_PRICE, FMT_PCT, FMT_X, BOLD, RED_FONT, GREEN, AMBER, RED, GREY, SECTION,
)
from gate_stack import evaluate, funnel, MissingGateData, DEFAULT_POSITION  # noqa: E402
from rank_candidates import (  # noqa: E402
    score_long, score_short, rank_blocked_severity, SHORT_POLICY, RANK_RATIONALE,
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

# Derive the market read from the scan itself + the radar/ignition state files,
# rather than leaving the tab empty waiting for a hand-written context file.
_ok_all = res.get("all_names") or []
_sell = len(res.get("sell_mode") or [])
_tot = len(_ok_all) or res.get("scanned") or 0
if _tot:
    _pct_sell = 100.0 * _sell / _tot
    ws.append(["Breadth - names in sell mode", f"{_sell}/{_tot} ({_pct_sell:.0f}%)",
               "Over half the market in downtrend means long setups are swimming "
               "against the tide - size down or wait."
               if _pct_sell >= 50 else
               "Most names are not in downtrend - a normal tape for long setups."])
_fresh_n = res.get("fresh_count") or 0
_pass_n = sum(1 for h in res.get("hits", [])
              if str(h.get("verdict") or "").startswith(("CANDIDATE", "STARTER")))
ws.append(["Fresh buy signals", str(_fresh_n),
           "Raw Chandelier flips before any gate."])
ws.append(["Signals surviving all gates", str(_pass_n),
           "What is actually tradeable. If this is 0, the honest answer is no trades."])
if _fresh_n:
    ws.append(["Signal survival rate", f"{100.0*_pass_n/_fresh_n:.0f}%",
               "Low survival means the indicator is firing into a hostile tape."])

# Pull the headline lines straight out of the radar / ignition state files.
def _state_headlines(path, limit=8, section_kw="NEW"):
    """Pull the bullet lines out of a state file's 'NEW since prior run' section.

    First version stripped '-*' from the line start, which destroyed the '**'
    it then tested for, so it silently returned nothing and the tab read
    '(state not found)'. Match the section, then take bullets.
    """
    try:
        txt = open(os.path.join(REPO, path), encoding="utf-8").read()
    except OSError:
        return []
    lines, out, in_sec = txt.splitlines(), [], False
    for ln in lines:
        st = ln.strip()
        if st.startswith("##"):
            in_sec = section_kw.upper() in st.upper()
            continue
        if not in_sec or not st:
            continue
        if st.startswith(("-", "*", "·", "•")):
            out.append(re.sub(r"\*\*", "", st.lstrip("-*·• ").strip()))
        if len(out) >= limit:
            break
    return out

ws.append([])
ws.append(["IGNITION SWEEP - new since prior run"])
ws.cell(row=ws.max_row, column=1).font = SECTION
_ig = _state_headlines("watchlists/ignition-sweep-state.md", 12)
if _ig:
    for line in _ig:
        ws.append(["", safe(line)])
else:
    ws.append(["", "(ignition sweep state not found - see Data Quality tab)"])

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
    Col("rank", "RANK", 7,
        "Priority order, 1 = look at this first. Ranked by the composite BUY SCORE. "
        "UNCALIBRATED - it is a transparent weighting of things that ought to matter, "
        "NOT a measured edge. Use it to decide what to examine first, never as the "
        "reason to take a trade."),
    Col("buy_score", "BUY SCORE", 11,
        "0-100 composite: risk quality 30 (how tight the stop is in ATR terms - "
        "weighted highest because stop distance decides position size), trend "
        "strength 25 (ADX + DI spread), regime 20 (distance above the 200-day), "
        "structure 10 (room above the ZLSMA), freshness 10, liquidity 5. "
        "Components are all shown on the Notes & Decisions tab.", FMT_PCT),
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


SCORED = {}   # sym -> (score, components, pros, cons); reused by Notes & Plans


def fresh_rows():
    out = []
    for sym, h in hits.items():
        e, o = enrich.get(sym, {}), orig.get(sym, {})
        last, stop = h.get("last"), h.get("ce_label") or h.get("flip_level")
        risk = round((last - stop) / last * 100, 1) if (last and stop and last > stop) else None
        _, why, _ = split_note(h.get("note"))

        g = h.get("gates") or {}
        sc, comp, pros, cons = score_long({
            "last": last, "long_stop": stop, "zlsma": h.get("zlsma"),
            "atr": h.get("atr"), "adx": g.get("adx"), "plus_di": g.get("plus_di"),
            "minus_di": g.get("minus_di"), "regime": g.get("regime") or h.get("regime"),
            "pct_vs_200": g.get("pct_vs_200"), "avg_dollar_vol": g.get("avg_dollar_vol"),
            "bars_back": h.get("bars_back"),
        }, position=DEFAULT_POSITION)
        # A blocked name can never outrank a live candidate, whatever it scores.
        if str(h.get("verdict") or "").startswith("BLOCKED"):
            sc = round(sc * 0.4, 1)
        SCORED[sym] = (sc, comp, pros, cons)

        out.append({
            "buy_score": sc,
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
    out.sort(key=lambda r: -(r["buy_score"] or 0))
    for i, r in enumerate(out, 1):
        r["rank"] = i
    return out


_fresh = fresh_rows()
ws = wb.create_sheet("2 - Fresh Buys")
write_table(ws, FRESH_COLS, _fresh, row_fill=verdict_fill)
ws.append([])
ws.append([safe("RANKED STRONGEST -> WEAKEST by BUY SCORE. The score is UNCALIBRATED - "
                "a transparent weighting, not a measured edge. Blocked names are scored "
                "down so they can never outrank a live candidate.")])
ws.cell(row=ws.max_row, column=1).font = BOLD
for k, v in RANK_RATIONALE.items():
    ws.append([safe(f"  {k}"), safe(v)])

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
# Build plans from the gated candidates. Previously this tab was fed only by a
# hand-written context file, so it was almost always EMPTY - which read as "no
# work done" rather than "no name qualified". Now it is always populated: either
# with real sized plans, or with an explicit statement of why there are none.
ACCOUNT, RISK_UNIT, MAX_ORDER = 1_000_000.0, 5_000.0, 100_000.0
plan_rows = []
for r in _fresh:
    v = str(r.get("verdict") or "")
    if not v.startswith(("CANDIDATE", "STARTER")):
        continue
    last, stop = r.get("last"), r.get("stop")
    if not (last and stop and last > stop):
        continue
    risk_ps = last - stop
    shares = int(min(MAX_ORDER / last, RISK_UNIT / risk_ps))
    dollars = shares * last
    starter = v.startswith("STARTER")
    if starter:                      # regime REPAIR -> half size
        shares, dollars = shares // 2, (shares // 2) * last
    target = last + 2 * risk_ps
    plan_rows.append({
        "a": r["sym"],
        "b": "LIMIT (starter)" if starter else "LIMIT",
        "c": round(last, 2), "d": round(stop, 2),
        "e": f"${dollars:,.0f} ({shares:,} sh)",
        "f": round(shares * risk_ps, 0),
        "g": f"{target:.2f} @ 2:1",
        "h": "VERIFY before entry - not captured by the scan",
        "i": "not yet armed",
        "j": (f"Rank #{r['rank']} of {len(_fresh)}, buy score {r['buy_score']}. "
              f"Stop is the Chandelier level ({r.get('risk_pct')}% away). "
              + ("HALF SIZE: regime REPAIR. " if starter else "")
              + "Confirm the earnings date and check the ATR floor by hand - "
                "neither is wired into the gate stack yet."),
    })

ws = wb.create_sheet("3 - Plans")
write_table(ws, PLAN_COLS, plan_rows)
if not plan_rows:
    ws.append([])
    ws.append([safe("NO PLANS - and that is a result, not an omission.")])
    ws.cell(row=ws.max_row, column=1).font = RED_FONT
    ws.append([safe(f"{len(_fresh)} fresh buy signals were scanned. None survived the "
                    f"gate stack (regime, ADX, DI direction, ZLSMA, liquidity), so "
                    f"there is nothing to size.")])
    ws.append([safe("Do NOT relax a gate to make this tab non-empty. See the Blocked "
                    "tab for exactly which gate stopped each name.")])
ws.append([])
ws.append([safe(f"Sizing basis: ${ACCOUNT:,.0f} account, ${RISK_UNIT:,.0f} risk per "
                f"trade (0.5%), ${MAX_ORDER:,.0f} max order. Shares = the SMALLER of "
                f"the order cap and the risk unit divided by stop distance.")])

# -------------------------------------------------------------- 4 Blocked ---
BLOCK_COLS = [
    Col("rank", "RANK", 7,
        "1 = WORST, i.e. furthest from ever being tradeable. The top of this list is "
        "what to stop looking at; the BOTTOM is what is nearly there and worth "
        "re-checking tomorrow."),
    Col("severity", "How Badly It Fails", 13,
        "Severity score. Higher = more gates failed and failed harder. Built from: "
        "regime DEEP-FAIL 40 / REPAIR 15, no trend 20, sellers in control 15, "
        "below ZLSMA 15, illiquid 25, plus distance below the 200-day.", FMT_PCT),
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
        g = h.get("gates") or {}
        sev, _reasons = rank_blocked_severity({
            "regime": g.get("regime") or h.get("regime"), "adx": g.get("adx"),
            "plus_di": g.get("plus_di"), "minus_di": g.get("minus_di"),
            "last": h.get("last"), "zlsma": h.get("zlsma"),
            "avg_dollar_vol": g.get("avg_dollar_vol"), "pct_vs_200": g.get("pct_vs_200"),
        })
        block_rows.append({"severity": sev,
                           "sym": sym, "company": e.get("description"),
                           "signal_date": h.get("signal_date_est"),
                           "magical": h.get("magical"), "regime": h.get("regime"),
                           "gate": v.replace("BLOCKED: ", ""), "why": why})
block_rows.sort(key=lambda r: -(r["severity"] or 0))
for i, r in enumerate(block_rows, 1):
    r["rank"] = i

ws = wb.create_sheet("4 - Blocked")
write_table(ws, BLOCK_COLS, block_rows,
            row_fill=lambda r: RED if (r["severity"] or 0) >= 60 else
                               (AMBER if (r["severity"] or 0) >= 30 else GREY))
ws.append([])
ws.append([safe("RANKED WORST FIRST. Rank 1 is the most comprehensively unsuitable; "
                "the names at the BOTTOM failed on one thing and are worth re-checking "
                "tomorrow.")])
ws.cell(row=ws.max_row, column=1).font = BOLD
ws.append([])
ws.append([safe("SHOULD YOU SHORT THESE? NO.")])
ws.cell(row=ws.max_row, column=1).font = RED_FONT
ws.append([safe("A failed long is not a good short. These names failed a test asking "
                "'is this going up?' - answering no is not the same as 'this is going "
                "down'. Many are blocked for reasons that say nothing about direction "
                "at all: illiquid, earnings too close, stop too tight. See the Sell "
                "Mode tab for the short discussion.")])

# ------------------------------------------------------------ 5 Sell Mode ---
SELL_COLS = [
    Col("rank", "SHORT RANK", 11,
        "1 = the most technically shortable name here. THIS IS NOT A RECOMMENDATION "
        "TO SHORT - read the policy block below the table. It ranks which names are "
        "in the cleanest downtrends, for exit/hedge decisions and for paper-trading "
        "a short book before risking money."),
    Col("short_score", "SHORT SCORE", 12,
        "0-100 mirror of the buy score: downtrend depth 30, trend strength 25 "
        "(ADX + DI spread the other way), structure below ZLSMA 15, stop quality 15, "
        "squeeze safety 15. UNCALIBRATED and, unlike the long side, never tested "
        "against forward returns at all.", FMT_PCT),
    Col("sym", "Ticker", 9, "The stock symbol."),
    Col("company", "Company", 32, "Company name."),
    Col("sector", "Sector", 22, "Sector."),
    Col("last", "Price", 10, "Latest price.", FMT_PRICE),
    Col("pct200", "% vs 200-Day Average", 14, "How far below its long-term average it is.", FMT_PCT),
    Col("adx", "Trend Strength (ADX)", 12, "Above 20 = a real downtrend, not chop.", FMT_PCT),
    Col("di", "-DI vs +DI", 12, "Sellers vs buyers. Sellers need to be clearly ahead."),
    Col("magical", "Overbought / Oversold (CCI-20)", 16, "20-period CCI.", FMT_PCT),
    Col("risk", "Main Short Risk", 46,
        "The specific reason this short could hurt you - squeeze, thinness, or being "
        "already too far gone."),
]
sell_rows = []
for s in res.get("sell_mode", []):
    a = allrows.get(s, {}) or {}
    row = {"last": a.get("last"), "zlsma": a.get("zlsma"),
           "short_stop": a.get("short_stop") or a.get("ce_label"),
           "adx": a.get("adx"), "plus_di": a.get("plus_di"),
           "minus_di": a.get("minus_di"), "pct_vs_200": a.get("pct_vs_200"),
           "avg_dollar_vol": a.get("avg_dollar_vol")}
    sc, comp, pros, cons = score_short(row, position=DEFAULT_POSITION)
    sell_rows.append({
        "short_score": sc, "sym": s,
        "company": enrich.get(s, {}).get("description"),
        "sector": enrich.get(s, {}).get("sector"),
        "last": a.get("last"), "pct200": row["pct_vs_200"], "adx": row["adx"],
        "di": (f"{row['minus_di']:.0f} vs {row['plus_di']:.0f}"
               if row["minus_di"] is not None and row["plus_di"] is not None else None),
        "magical": a.get("magical"),
        "risk": "; ".join(cons[:2]) if cons else "no specific flag - still unvalidated",
    })
sell_rows.sort(key=lambda r: -(r["short_score"] or 0))
for i, r in enumerate(sell_rows, 1):
    r["rank"] = i

ws = wb.create_sheet("5 - Sell Mode")
write_table(ws, SELL_COLS, sell_rows,
            row_fill=lambda r: RED if (r["short_score"] or 0) >= 70 else None)
ws.append([])
for line in SHORT_POLICY.strip().split("\n"):
    ws.append([safe(line)])
    if line.strip().startswith("SHOULD YOU SHORT"):
        ws.cell(row=ws.max_row, column=1).font = RED_FONT

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
_rank_of = {r["sym"]: r["rank"] for r in _fresh}
note_rows = []
for sym, h in hits.items():
    changed, _, full = split_note(h.get("note"))
    sc, comp, pros, cons = SCORED.get(sym, (None, {}, [], []))
    note_rows.append({
        "rank": _rank_of.get(sym),
        "sym": sym, "verdict": h.get("verdict"), "changed": changed,
        "pros": ("* " + "\n* ".join(pros)) if pros else "(nothing argues for it)",
        "cons": ("* " + "\n* ".join(cons)) if cons else "(no flags - genuinely clean)",
        "reasoning": full or "(no narrative recorded)",
    })
note_rows.sort(key=lambda r: (r["rank"] is None, r["rank"] or 999))
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
