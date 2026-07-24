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
    FMT_PRICE, FMT_PCT, FMT_X, FMT_INT, BOLD, RED_FONT, GREEN, AMBER, RED, GREY, SECTION,
)
from gate_stack import evaluate, funnel, MissingGateData, DEFAULT_POSITION  # noqa: E402
from rank_candidates import (  # noqa: E402
    score_long, score_long_v2, score_short, rank_blocked_severity,
    SHORT_POLICY, RANK_RATIONALE,
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


def _fmt_cap(x):
    """Money in human units: 19770000000 -> '$19.8B'."""
    if not x:
        return None
    for suf, div in (("B", 1e9), ("M", 1e6), ("K", 1e3)):
        if abs(x) >= div:
            return f"${x/div:.1f}{suf}"
    return f"${x:.0f}"


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
        "OB/OS) on the LIVE chart, on HEIKIN ASHI (Omar's 2026-07-23 standard).",
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
        ("8 - Market Movers", "The day's biggest gainers/losers in the WHOLE market, each screened.",
         "Almost all are microcap SKIPs; the few liquid movers get a real buy/short call."),
        ("9 - Track Record", "How the scanner's past picks have actually done - the honest scorecard.",
         "Broken down by grade and tab; shows whether a higher grade is worth more (so far, no)."),
        ("10 - Data Quality", "What was broken or partial in this run, ranked by severity.",
         "READ THE RED ROWS. A BLOCKER means conclusions in this file may be wrong."),
        ("11 - Run Summary", "Counts and run metadata."),
    ],
    how_to_act=[
        "1. Check tab 10 for BLOCKERS first. If coverage was partial, absence of a name",
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
# ---- Catalyst calendar join (Omar 2026-07-23): catalyst as columns on the ticker rows,
# not a standalone tab. Fed by research/catalyst-calendar.json (build_catalyst_calendar.py). ----
try:
    _cat_raw = json.load(open(os.path.join(REPO, "research", "catalyst-calendar.json")))
    CATALYST = {r["ticker"].upper(): r for r in _cat_raw.get("records", [])}
except Exception:
    CATALYST = {}

CAT_COL = Col("catalyst", "Catalyst", 22,
              "Next scheduled catalyst for this name - earnings within 7 days, or a Phase-3 "
              "trial readout window. Blank = none flagged. From build_catalyst_calendar.py.")
CATVIEW_COL = Col("catview", "Catalyst View", 62,
                  "What the catalyst is and the suggested ACTION. Earnings: trim into the print, "
                  "re-enter post-print only if it beats AND holds (PEAD). Biopharma: BINARY - "
                  "defined-risk / awareness only, never hold a momentum long through it.")


def _inject_cat(rows):
    """Attach Catalyst + Catalyst View onto each ticker row before rendering."""
    for r in rows:
        sym = (r.get("sym") or r.get("a") or r.get("ticker") or "").upper()
        c = CATALYST.get(sym)
        r["catalyst"] = f"{c['event_type']} {c['date_or_window']}" if c else ""
        r["catview"] = c["view"] if c else ""


FRESH_COLS = [
    Col("rank", "RANK", 7,
        "Priority order, 1 = look at this first. Ranked by the composite BUY SCORE. "
        "UNCALIBRATED - it is a transparent weighting of things that ought to matter, "
        "NOT a measured edge. Use it to decide what to examine first, never as the "
        "reason to take a trade."),
    Col("buy_score", "BUY SCORE v2", 12,
        "0-100 rank, re-weighted 2026-07-22 after calibration: trend (ADX/DI) 45, "
        "structure (vs ZLSMA) 35, regime 15, freshness/liquidity 5. Risk quality "
        "was REMOVED from the sort - it correlated NEGATIVELY with returns (-0.05) "
        "and now shows only in the Risk column. STILL UNCALIBRATED: even v2 only "
        "rank-correlates ~+0.1-0.2 with forward returns and did NOT beat v1 out of "
        "sample. Use it to decide what to look at first, never as a forecast.", FMT_PCT),
    Col("risk_flag", "Risk (stop x ATR)", 15,
        "Stop distance in ATR multiples - the sizing/survival read, kept OUT of the "
        "ranking because it does not predict returns. 1.0-4.0x is healthy; below 1x "
        "gets noise-stopped, above 4x is a token position."),
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
        feat = {
            "last": last, "long_stop": stop, "zlsma": h.get("zlsma"),
            "atr": h.get("atr") or g.get("atr"), "adx": g.get("adx"), "plus_di": g.get("plus_di"),
            "minus_di": g.get("minus_di"), "regime": g.get("regime") or h.get("regime"),
            "pct_vs_200": g.get("pct_vs_200"), "avg_dollar_vol": g.get("avg_dollar_vol"),
            "bars_back": h.get("bars_back"),
        }
        # v2 ranks; v1 kept only for its pros/cons narrative (component breakdown).
        sc, _v2comp, rflag = score_long_v2(feat, position=DEFAULT_POSITION)
        _v1sc, comp, pros, cons = score_long(feat, position=DEFAULT_POSITION)
        # A blocked name can never outrank a live candidate, whatever it scores.
        if str(h.get("verdict") or "").startswith("BLOCKED"):
            sc = round(sc * 0.4, 1)
        SCORED[sym] = (sc, comp, pros, cons)
        risk_txt = (f"{rflag['stop_x_atr']}x ({rflag['stop_pct']}%)"
                    + ("" if rflag.get("ok") else " !") if rflag else "-")

        out.append({
            "buy_score": sc, "risk_flag": risk_txt,
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
_inject_cat(_fresh)
write_table(ws, FRESH_COLS + [CAT_COL, CATVIEW_COL], _fresh, row_fill=verdict_fill)
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


def _earn_txt(h):
    """Earnings cell - never leave it as a bare 'verify', say what is known."""
    e = h.get("earnings") or {}
    if not e:
        return "NOT CHECKED - verify before entry; the scan cannot see earnings"
    est = e.get("estimate", "?")
    tag = "CONFIRMED" if e.get("confirmed") else "ESTIMATED"
    days = e.get("days_out")
    out = f"{est} ({tag}"
    if days is not None:
        out += f", ~{days}d out"
    out += ")"
    if e.get("rule"):
        out += f" - {e['rule']}"
    return out


def _alert_txt(h):
    """Alert cell - show the armed IDs so the plan and the alert board agree."""
    a = h.get("alerts") or {}
    if not a:
        return "NOT ARMED"
    return "; ".join(f"{k} {v.get('level')} (id {v.get('id')})" for k, v in a.items())


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
        "h": _earn_txt(hits.get(r["sym"], {})),
        "i": _alert_txt(hits.get(r["sym"], {})),
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
_inject_cat(block_rows)
write_table(ws, BLOCK_COLS + [CAT_COL, CATVIEW_COL], block_rows,
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
_inject_cat(sell_rows)
write_table(ws, SELL_COLS + [CAT_COL, CATVIEW_COL], sell_rows,
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

# ---------------------------------------------------------- 8 Market Movers ---
# The day's biggest gainers/losers across the ENTIRE market, each run through the
# protocol. Requested by Omar 2026-07-22. Data from watchlists/market-movers-
# <date>.json (fetched from stockanalysis.com). Key honesty: the raw biggest
# movers are almost always microcaps you cannot trade, so each carries a SKIP
# reason, and only names clearing the liquidity screen get the full protocol.
from market_movers import parse_num, screen, classify_untradeable  # noqa: E402

MOVER_COLS = [
    Col("side", "Gainer / Loser", 13, "Which list the stock topped today."),
    Col("sym", "Ticker", 9, "The stock symbol."),
    Col("company", "Company", 30, "Company name."),
    Col("price", "Price", 10, "Price at the close.", FMT_PRICE),
    Col("pct", "Day Change %", 12, "The move that put it on the list.", FMT_PCT),
    Col("mcap", "Market Cap", 13,
        "Company size. Under ~$2B = microcap: it gaps, halts, and cannot absorb a "
        "$100k order. The single biggest reason most movers are untradeable."),
    Col("dvol", "$ Traded Today", 14,
        "Price x volume. A $100k order needs this to be large, or you move the "
        "price against yourself getting in and out."),
    Col("verdict", "PROTOCOL VERDICT", 24,
        "What to do. SKIP = untradeable at your size (almost all of them). The few "
        "that clear the screen get a real buy/short call."),
    Col("why", "Reasoning", 78,
        "Plain-English why. For SKIPs, the specific disqualifier. For survivors, "
        "the full gate-stack read."),
]


def _load_movers():
    path = os.path.join(REPO, "watchlists", f"market-movers-{DATE}.json")
    if not os.path.exists(path):
        return None
    return json.load(open(path))


mv_data = _load_movers()
ws = wb.create_sheet("8 - Market Movers")
if not mv_data:
    style_header_row(ws, ["Market Movers"], ["No movers file for this date."],
                     [40], freeze=None, autofilter=False)
    ws.append([safe(f"No watchlists/market-movers-{DATE}.json found. Fetch the day's "
                    "gainers/losers (stockanalysis.com) and re-run.")])
else:
    mrows = []
    # liquid movers first (they got full protocol), then the raw microcap movers
    for lm in mv_data.get("liquid_movers", []):
        mrows.append({
            "side": lm.get("side", "gainer").upper() + " (liquid)",
            "sym": lm["sym"], "company": lm.get("company"), "price": lm.get("price"),
            "pct": lm.get("pct_change"), "mcap": _fmt_cap(lm.get("market_cap")),
            "dvol": _fmt_cap(lm.get("avg_dollar_vol")),
            "verdict": lm.get("protocol", "NEEDS CHART"),
            "why": lm.get("protocol_why", ""),
        })
    for side_key in ("gainers", "losers"):
        for m in mv_data.get(side_key, []):
            side = m.get("side", side_key[:-1])
            if m.get("tradeable"):
                verdict, why = "TRADEABLE - see chart", \
                    "Cleared the liquidity screen; chart it and run the gate stack."
            else:
                verdict, why = classify_untradeable(m, side)
                why = f"{m.get('skip_reason','')}. {why}"
            mrows.append({
                "side": side.upper(), "sym": m["sym"], "company": m.get("company"),
                "price": m.get("price"), "pct": m.get("pct_change"),
                "mcap": _fmt_cap(m.get("market_cap")),
                "dvol": _fmt_cap((m.get("price") or 0) * (m.get("volume") or 0)),
                "verdict": verdict, "why": why,
            })

    def _mv_fill(r):
        v = str(r.get("verdict") or "")
        if v.startswith(("BUY", "STARTER")):
            return GREEN
        if "SHORT" in v or "TRADEABLE" in v:
            return AMBER
        return GREY   # the SKIPs - visually recede so the tradeable rows pop

    write_table(ws, MOVER_COLS, mrows, autofilter=True, row_fill=_mv_fill)
    for n in range(2, ws.max_row + 1):
        ws.row_dimensions[n].height = 44
    ws.append([])
    ws.append([safe(f"Source: {mv_data.get('source','?')}, captured {mv_data.get('captured','?')}.")])
    ws.append([safe("WHY ALMOST EVERYTHING HERE IS 'SKIP': the biggest raw percentage "
                    "movers in the whole market are nearly always microcaps and penny "
                    "stocks - pumps, post-halt spikes, Chinese small-caps. They cannot "
                    "absorb a $100k order and are not shortable (no borrow, squeeze "
                    "risk). Only names clearing the liquidity screen (price >= $5, cap "
                    ">= $2B, decent $ volume) get a real buy/short call.")])
    ws.cell(row=ws.max_row, column=1).font = BOLD
    ws.append([safe("For the big LIQUID movers that reflect real rotation, the "
                    "'1 - Market & Rotation' tab and the ranked buy list are the "
                    "actionable views - this tab is the raw market-wide scan.")])

# ------------------------------------------------------- 9 Track Record ---
# The origination scanner's own performance history (recommendations_log.csv),
# tracked since the scans began. Surfaced here per Omar 2026-07-22.
_tr = None
_trpath = os.path.join(REPO, "research", "track-record.json")
if os.path.exists(_trpath):
    _tr = json.load(open(_trpath))

TR_COLS = [
    Col("bucket", "Group", 20, "The pick group being scored - all picks, then by "
        "grade, then by origination tab."),
    Col("n", "Picks", 8, "How many recommendations in this group.", FMT_INT),
    Col("win", "Green %", 9, "Share currently in profit (unrealized).", FMT_PCT),
    Col("mean", "Mean Return %", 13, "Average unrealized return since the pick.", FMT_PCT),
    Col("median", "Median Return %", 15, "Median - less distorted by outliers.", FMT_PCT),
    Col("mfe", "Avg Best %", 11, "Average best excursion reached - upside that was on "
        "the table.", FMT_PCT),
    Col("mae", "Avg Worst %", 12, "Average worst drawdown suffered - pain held through.", FMT_PCT),
]
ws = wb.create_sheet("9 - Track Record")
if not _tr or _tr.get("error"):
    style_header_row(ws, ["Track Record"], ["Run track_record.py first."],
                     [40], freeze=None, autofilter=False)
    ws.append([safe("No research/track-record.json - run scripts/track_record.py.")])
else:
    o = _tr["overall"]
    trows = [{"bucket": "ALL PICKS", "n": o["n"], "win": o["win_pct"], "mean": o["mean"],
              "median": o["median"], "mfe": o["mfe"], "mae": o["mae"]}]
    for g, v in _tr["by_grade"].items():
        trows.append({"bucket": f"grade {g}", "n": v["n"], "win": v["win_pct"],
                      "mean": v["mean"], "median": v["median"], "mfe": v["mfe"], "mae": v["mae"]})
    for t, v in _tr["by_tab"].items():
        trows.append({"bucket": f"tab {t}", "n": v["n"], "win": v["win_pct"],
                      "mean": v["mean"], "median": v["median"], "mfe": v["mfe"], "mae": v["mae"]})

    def _tr_fill(r):
        if r["bucket"] == "ALL PICKS":
            return None
        m = r.get("mean") or 0
        return GREEN if m > 0 else (RED if m < -3 else AMBER)

    write_table(ws, TR_COLS, trows, autofilter=False, row_fill=_tr_fill)
    ws.append([])
    ws.append([safe(f"ORIGINATION SCANNER TRACK RECORD - {_tr['total']} picks, "
                    f"{_tr['date_range'][0]} to {_tr['date_range'][1]}. Returns are "
                    f"UNREALIZED (matured {o['matured']}/{_tr['total']} at the 21-day "
                    f"mark; the log only started 7/1). This grades the scanner's own "
                    f"A/B/C picks, separate from the trade-call ledger.")])
    ws.cell(row=ws.max_row, column=1).font = BOLD
    q = _tr.get("score_quartile")
    if q:
        ws.append([safe(f"DOES THE SCORE PREDICT? bottom-25% by score mean "
                        f"{q['bottom_q_mean']:+.2f}%, top-25% mean {q['top_q_mean']:+.2f}%, "
                        f"spread {q['spread']:+.2f}pt.")])
        ws.cell(row=ws.max_row, column=1).font = RED_FONT if q["spread"] <= 0 else BOLD
        if q["spread"] <= 0:
            ws.append([safe("The origination score does NOT predict returns here - flat/"
                            "backwards, the SAME result as the BUY SCORE calibration. Two "
                            "independent scores, same verdict: sort what to look at, do "
                            "not forecast.")])
    ws.append([safe("Unrealized reads on OPEN positions, not final results. Grade A "
                    "(mean -2.8%) is NOT beating grade B (-2.0%) - higher grade has not "
                    "paid so far. Real win-rates land as the July picks reach 21 days "
                    "through early August.")])

# ---------------------------------------------------------- 10 Data Quality ---
dq = [classify(q) if isinstance(q, str) else q for q in res.get("data_quality", [])]
data_quality_sheet(wb.create_sheet("10 - Data Quality"), dq)

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
ws = wb.create_sheet("11 - Run Summary")
write_table(ws, SUM_COLS, sum_rows, autofilter=False)
for n in range(2, ws.max_row + 1):
    ws.row_dimensions[n].height = 44

# Save, stepping around whatever is currently open in Excel. The first fallback
# was a single "_new" name, which broke the moment BOTH files were open - the
# fallback itself raised. Keep trying until something lands.
_stamp = datetime.datetime.now().strftime("%H%M%S")
_candidates = [f"universe_{DATE}.xlsx", f"universe_{DATE}_new.xlsx",
               f"universe_{DATE}_{_stamp}.xlsx"]
out, _err = None, None
for _name in _candidates:
    _path = os.path.join(REPO, "reports", _name)
    try:
        wb.save(_path)
        out = _path
        break
    except PermissionError as exc:
        _err = exc
        continue
if out is None:
    raise SystemExit(f"could not write any workbook - all candidates locked: {_err}")
if out != os.path.join(REPO, "reports", _candidates[0]):
    print(f"NOTE: earlier filename(s) locked in Excel - wrote {os.path.basename(out)} instead.")
print(f"written {out}")
print(f"  sheets: {len(wb.sheetnames)} | fresh {len(hits)} | blocked {len(block_rows)} "
      f"| notes {len(note_rows)} | dq {len(dq)} "
      f"(BLOCKERS {sum(1 for d in dq if str(d.get('severity')).upper() == 'BLOCKER')})")
