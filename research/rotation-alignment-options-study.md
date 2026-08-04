# Does sector-rotation alignment help OPTIONS entries? (2026-08-04, Omar hypothesis)

Hypothesis tested: option buys should require the underlying's sector to be
"in rotation" (radar-favorable). Method: all 34 closed Markman trades;
radar states RECONSTRUCTED at each entry date from ETF price history using
the radar's own classify() math; trade direction vs group state.

| Bucket | n | Record | Win | Avg P&L |
|---|---|---|---|---|
| ALIGNED with rotation | 8 | 4W-3L | 50% | **-22%** |
| NEUTRAL group | 17 | 12W-5L | 71% | **+22%** |
| CONTRA rotation | 9 | 6W-3L | 67% | +9% |
| (clean mappings only: ALIGNED -33% vs CONTRA +27%) |

By raw group state at entry (any direction):
IGNITING 1W-3L avg **-44%** (OKLO -100, HOOD -90, META -89 all bought in
igniting groups) · WATCH 75%/-11% · NEUTRAL 71%/+22% · ROLLING 75%/+21%.

**Finding: rotation-aligned option entries UNDERPERFORMED badly; the money
was in NEUTRAL (uncrowded) groups. Igniting-sector calls were the disaster
bucket.** Reading: radar heat measures CROWDING - by the time a group is
formally igniting, option premiums and entries are late; theta + convexity
punish buying group heat. Rhymes with the winner-factor study (rested >
excited) and the backwards Magical result.

Our own overlay book agrees anecdotally (8/4): neutral-group entries
(GE +$814, UAL, DAL) winning; aligned entries mixed (SLB +$603 but INTC put
-$682, AAPL put -$252).

**Decision: rotation-alignment is NOT added as a filter line (it would have
subtracted). Group state becomes a TRACKED FIELD on every screener card and
overlay pick - measurement, no veto - with a soft caution flag on
igniting-group call buys. Caveats: n=34, mapping fuzziness on 5 names,
multiple comparisons, single regime era. Forward data decides via Fridays.**
