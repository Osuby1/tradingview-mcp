"""One-off: record the 2026-07-23 EOD run's chart/web-side blockers into
watchlists/universe-results-2026-07-23.json data_quality.

build_universe_results.py only sees the sweep file, so it cannot know what
happened while the sweep was being taken. Everything below was found during the
chart work and would otherwise be invisible to whoever reads the workbook.
"""
import json

PATH = "watchlists/universe-results-2026-07-23.json"
d = json.load(open(PATH, encoding="utf-8"))

ADDS = [
    {
        "severity": "WARNING",
        "area": "Symbol resolution",
        "finding": "5 of 492 bare tickers resolved to FOREIGN listings, not the "
                   "US line: BHP -> ASX_DLY:BHP (AUD 60.55), EQR -> ASX_DLY:EQR "
                   "(EQ Resources Limited, AUD 0.27), COCO -> IDX_DLY:COCO "
                   "(IDR 141.25), DTE -> XETR_DLY:DTE (Deutsche Telekom, EUR "
                   "26.71), SFL -> NSE_DLY:SFL (INR 754.15).",
        "impact": "All five were re-read as NYSE:/NASDAQ: and the corrected rows "
                  "replaced the bad ones before gating, so today's numbers are "
                  "clean. Untouched, EQR and DTE would have been priced as "
                  "entirely different companies. The sweep's identity guard "
                  "cannot catch this - the TICKER matches, it is the EXCHANGE "
                  "that is wrong, so the read looks valid.",
        "action": "Add BHP, EQR, COCO, DTE and SFL to FORCE_PREFIX in "
                  "scripts/build_extended_universe.py (it currently only forces "
                  "FITB and SMCI) so the next run never reads them bare. Rows "
                  "that were swapped carry a resolution_fixup field in the raw "
                  "sweep JSON.",
    },
    {
        "severity": "WARNING",
        "area": "Coverage",
        "finding": "2 of 492 names could not be read completely and are NOT in "
                   "the scanned set: SPCX (Space Exploration Technologies, 28 "
                   "bars of history) and XMAX (50 bars). Both are too newly "
                   "listed for the 200-day regime test, which needs 210 bars.",
        "impact": "Scanned is 490, not 492. Per the fail-closed rule a name that "
                  "cannot be gate-evaluated is BLOCKED, so neither can appear as "
                  "a candidate - they are excluded, not silently passed.",
        "action": "Leave them blocked until they have ~10 months of history. Do "
                  "not hand-wave the regime gate for recent IPOs.",
    },
    {
        "severity": "WARNING",
        "area": "Signal quality",
        "finding": "LHX flipped to BUY TODAY (0 bars back) and is one of the four "
                   "STARTER ONLY names.",
        "impact": "0-bar flips repaint. This is the exact failure logged on "
                  "2026-07-22 (CENX and CRWV both flipped BUY intraday and were "
                  "back in SELL by 2pm).",
        "action": "Re-read LHX after the close before it is treated as a real "
                  "signal.",
    },
    {
        "severity": "INFO",
        "area": "Alert board",
        "finding": "Alert board refreshed from the live TradingView endpoint: 379 "
                   "raw alerts -> 287 unique symbols (254 active, 33 "
                   "auto-deactivated with a fire time). One junk row whose symbol "
                   "field had stringified to '[object Object]' was dropped. "
                   "Symbol list and fire timestamps were checksum-verified "
                   "against the page after writing.",
        "impact": "The tracked-symbols rule rescued 39 names that no watchlist "
                  "and no origination tab covers - including ECVT, which is one "
                  "of today's three full candidates and is exactly the name this "
                  "rule was built for after it vanished mid-trade on 2026-07-22.",
        "action": "",
    },
    {
        "severity": "INFO",
        "area": "Market movers",
        "finding": "stockanalysis.com gainers/losers captured to "
                   "watchlists/market-movers-2026-07-23.json. The source page "
                   "shows 20 rows per list, not 25.",
        "impact": "Tab 8 has 20 gainers and 20 losers.",
        "action": "Each still needs the liquidity screen (price >= $5, cap >= "
                  "$2B, $vol >= $25M) before any protocol run - most of today's "
                  "movers are sub-$100M microcaps that will screen out.",
    },
]

existing = {(x.get("area"), x.get("finding")) for x in d["data_quality"]}
added = [a for a in ADDS if (a["area"], a["finding"]) not in existing]
d["data_quality"].extend(added)

json.dump(d, open(PATH, "w", encoding="utf-8"), indent=1)
print("added %d data_quality entries (now %d)" % (len(added), len(d["data_quality"])))
for a in added:
    print("  [%s] %s" % (a["severity"], a["area"]))
