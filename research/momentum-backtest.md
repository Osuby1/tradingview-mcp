# Cross-sectional momentum backtest - hard facts

135 names, 23 monthly rebalances, 12-1 momentum, long top 20%, monthly hold. Benchmark SPY.

## The number that matters: does momentum forecast?
- **Average monthly IC (Spearman momentum vs next-month return): -0.006** (n=23 months)
  - Compare: the technical BUY SCORE managed +0.065 at 21d. IC >= |0.03| is a usable cross-sectional signal.
  - Months with positive IC: 52%

## Top vs bottom, and vs SPY
- Top 20% mean monthly: +3.44%
- Bottom 20% mean monthly: +2.34%
- **Top-minus-bottom spread: +1.10%/mo**
- SPY mean monthly: +1.40%
- **Top-minus-SPY (monthly excess): +2.04%**, hit rate 65%

## Compounded over the window
- Momentum top 20%: +105.8%  (annualized ~41%, Sharpe ~1.65)
- SPY: +35.7%  (annualized ~17%, Sharpe ~1.34)

## Verdict
Momentum did NOT forecast in this window (IC -0.006). Either the sample is a momentum-hostile stretch or the universe is too small. Do not adopt on this alone.

## Caveats (these INFLATE the result)
- SURVIVORSHIP: fixed list of names that exist today; delisted losers absent. A clean test needs point-in-time constituents.
- No costs/slippage; monthly turnover of ~40-60% of the book is real drag.
- One ~3-year window; momentum has rare violent crashes not necessarily here.
