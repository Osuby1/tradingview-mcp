#!/usr/bin/env python3
"""Render the YTD options leaderboard: merge study passes, dedupe, rank by peak
premium gain, write reports/top-options-ytd-2026.xlsx per the workbook format
contract (title + timestamps + declared method/limits, tooltipped columns)."""
import json, glob, sys, datetime as dt
from pathlib import Path
sys.path.insert(0, "scripts")
from scan_workbook_style import Col, write_table, style_header_row, safe, GREEN, AMBER, FMT_PRICE, FMT_PCT, FMT_INT
import openpyxl

REPO = Path(".")
rows, seen = [], set()
for f in sorted(glob.glob("research/top-options-ytd-2026*.json")):
    for r in json.load(open(f)):
        if r["contract"] in seen: continue
        seen.add(r["contract"]); rows.append(r)
rows.sort(key=lambda x: -x["peak_pct"])
top = rows[:100]
for i, r in enumerate(top): r["rank"] = i + 1

COLS = [
    Col("rank", "Rank", 6, "Ranked by peak gain - the best the contract printed on a daily close this year."),
    Col("contract", "Contract", 20, "TradeStation symbol: underlying, expiry (YYMMDD), C=call / P=put, strike."),
    Col("underlying", "Stock", 8, "The company the option is on."),
    Col("sector", "Sector", 20, "The stock's sector."),
    Col("type", "Call / Put", 9, "Calls profit when the stock rises; puts when it falls."),
    Col("expiry", "Expires", 11, "The contract's expiration date. Everything here is still alive today."),
    Col("strike", "Strike", 9, "The price the option locks in.", FMT_PRICE),
    Col("jan_price", "Jan Price", 10, "What one contract cost at the FIRST session of 2026 (x100 = dollars).", FMT_PRICE),
    Col("peak_price", "Peak Price", 10, "Its best daily close of the year so far.", FMT_PRICE),
    Col("peak_pct", "Peak Gain %", 11, "January price to the peak. This assumes selling AT the best close - "
        "nobody times that perfectly; treat it as the ceiling, not the expectation.", FMT_INT),
    Col("peak_date", "Peak Day", 11, "When the peak printed - shows how long the winner took to develop."),
    Col("now_price", "Price Now", 10, "Friday's close.", FMT_PRICE),
    Col("now_pct", "Held-To-Now %", 12, "January price to Friday - what buy-and-hold actually kept. The gap "
        "between this and Peak is the round-trip risk, visible.", FMT_INT),
    Col("stock_ytd_pct", "Stock YTD %", 11, "The underlying stock's own move this year - the engine under the option.", FMT_PCT),
    Col("opt_volume_ytd", "Contracts Traded", 14, "Total contracts traded in it this year - how real the market was.", FMT_INT),
]
wb = openpyxl.Workbook(); ws = wb.active; ws.title = "TOP OPTIONS YTD"
ws.append([safe("THE 100 MOST PROFITABLE LISTED OPTION CONTRACTS OF 2026 (year to date)")])
ws.append([safe(f"Data: TradeStation daily option bars from 2026-01-02 + TradingView movers/sectors  |  Built {dt.datetime.now():%Y-%m-%d %H:%M} local")])
ws.append([safe("METHOD: universe = the year's biggest stock movers both directions; calls above the January price on gainers, "
                "puts below it on losers; every contract priced bar-by-bar from its first 2026 session.")])
ws.append([safe("DECLARED LIMITS: (1) contracts that ALREADY EXPIRED are purged from every feed - the year's true biggest "
                "winners (short-dated Feb-Jul tickets on these same stocks) cannot be priced, so this is the SURVIVING-contract "
                "leaderboard; (2) floors applied: listed by Jan 15, first price >= $0.05, >= 50 contracts traded, >= 60 sessions "
                "of bars; (3) thin names mark on sparse prints - the volume column is the credibility check.")])
ws.append([])
start = ws.max_row + 1
write_table(ws, COLS, top, freeze=f"A{start+1}",
            row_fill=lambda r: GREEN if r.get("peak_pct", 0) >= 1000 else (AMBER if r.get("peak_pct", 0) >= 500 else None))
wb.save("reports/top-options-ytd-2026.xlsx")
print(f"wrote reports/top-options-ytd-2026.xlsx with {len(top)} contracts (from {len(rows)} qualified)")
