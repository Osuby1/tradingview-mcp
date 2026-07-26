# Initial-stop sweep — pre-registration

Committed 2026-07-26, BEFORE any study code exists. Question from Omar: the 20%
ratchet governs winners, but most gate-passing signals never appreciate enough
to arm it — what initial stop is optimal for that dead zone?

This is explicitly a PARAMETER SWEEP, the thing every registration this week
has warned about. The guard rails are therefore declared here, in advance:
the selection rule, the splits that must agree, and the conclusion if they
don't. A curve that improves monotonically to the boundary means NO optimum
exists (the ZLSMA lesson), and will be reported as exactly that.

## Frozen design

**Entries:** identical to the exit-redesign study — same 12 sector baskets,
2021–2025, same gate stack, fresh-BUY definition, ~12,230 signals. Entry at the
signal-day real close.

**The rule under sweep** is the LIVE rule as of 2026-07-25: hold with a static
initial stop; once 0.8 × highest-close-since-entry rises above that stop, the
20% close-based ratchet governs instead (exit line = max(stop, 0.8 × high));
120-trading-day cap. Only the INITIAL STOP DISTANCE varies.

**Grid (frozen):** fixed percentages below entry — 2, 3, 4, 5, 6, 8, 10, 12,
15, 20 — plus `CE1x` (the entry-day Chandelier distance, the pre-7/25 live
stop, median ≈3–4%) and `NOSTOP` (ratchet-only). Twelve rules, no additions
after seeing results.

**Fill model — stricter than the prior studies, declared now:** if a day OPENS
below the effective stop, the fill is the OPEN (gap-through modeled), else an
intraday breach fills at the stop. Ratchet exits fill at the close, as tested.
10 bp round-trip cost reported.

**Primary metric: mean $ P&L per signal under Omar's real sizing formula**
(notional = min($100,000, $5,000 / stop-distance); NOSTOP sized at the $100k
cap). This is the money answer: it prices the fact that a wider stop buys a
smaller position. Secondary: mean R-multiple (trade % / stop %), raw mean %,
median, hit rate, stop-out %, mean days held, mean worst $ drawdown while
open, and the by-year table with 2022 always shown.

## Selection rule — declared before any number

1. Compute the $-expectancy argmax on each half of TWO independent splits:
   odd/even alphabetical names, and 2021–2023 vs 2024–2025.
2. **A stop level is declared "the optimum" only if the argmax lands within
   ±1 grid step of the same level on BOTH halves of BOTH splits.** Otherwise
   the pre-committed conclusion is: *"No stable optimum exists; the stop is a
   risk-budget dial, not a performance parameter — pick it from drawdown
   tolerance and sizing, not from backtest rank."*
3. If the $-curve is monotonic to either boundary, that boundary is NOT an
   optimum — report the monotonic story and what it converges to.
4. The 2022 column is reported for whatever wins; if the winner's 2022 mean $
   is materially worse than NOSTOP's 2022 (>$1,000/signal worse), that is
   flagged as trend-year dependence, same shape as the ZLSMA result.

## Biases, stated in advance

Survivor universe and hand-picked names (shared by all rules — comparisons
mostly cancel). Overlapping signals (dedup cut reported). The gap-through fill
model removes the prior studies' optimism on tight stops; slippage beyond the
open is still unmodeled and favors tight stops slightly. One run, no grid
changes after this commit.
