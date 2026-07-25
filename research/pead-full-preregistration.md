# Pre-registration: earnings-surprise signal, tested the way everything else was

Registered 2026-07-25 **before re-running anything**. The PEAD signal was tested
once on 2026-07-22 and failed its bar at 60 days while passing at 20. Since then,
five other components have been put through a harder standard and all failed.
This applies that same standard to the one signal that showed life.

## Why re-test something already tested

The 7/22 test measured **rank correlation and quintile spreads**. Today's standard
asks three further questions that killed other components:

1. Does it beat **just buying SPY**, in money?
2. Is the **median** positive, or only the mean? (Stock picking had a positive
   mean and a negative median — more than half the picks lost to their benchmark.)
3. Does it survive **removing the top 5% of outcomes**? (Stock picking did not —
   its entire excess came from 5% of trades.)

A signal can have a respectable IC and still fail all three.

## What is fixed now

- **Signal:** SUE (Standardized Unexpected Earnings), Bernard-Thomas
  construction, from EDGAR point-in-time filings. **Unchanged** from
  `scripts/edgar_sue_backtest.py`. No re-specification.
- **Universe:** the existing mid-cap set, 103 names, unchanged.
- **Period:** all available events, 2011–2026, reported **year by year**.
- **Primary horizon: 20 trading days**, declared now. This is the horizon where
  the signal showed life on 7/22; 60 days already failed and is reported for
  completeness, not as a headline.
- **Primary cohort:** top-quintile SUE (the names you would actually buy).
- **Benchmark:** SPY over the identical window. Entry the day AFTER the filing —
  no look-ahead.
- Winsorized at 2.5/97.5 as primary (carried over from the 7/22 registration),
  with **raw, unwinsorized numbers reported alongside**, because winsorizing caps
  exactly the tails the concentration test is designed to find.

## The bar — all four must hold at 20 days

| # | Requirement |
|---|---|
| 1 | Mean excess vs SPY **≥ +1.0 pt** |
| 2 | **Median excess > 0** |
| 3 | **Hit rate > 52%** |
| 4 | **Mean excess still > 0 after deleting the top 5% of raw outcomes** |

Requirement 4 is the one that matters most. It is the test stock picking failed,
and it is the difference between an edge and a lottery ticket.

## Pre-committed conclusions

| Result | Conclusion |
|---|---|
| **All four hold** | The first real edge measured in this system. Build here; it is the only non-price input tested and it survived the standard that broke everything else. |
| **1–3 hold, 4 fails** | A tail-driven signal. Real but not bankable at retail size — it needs many small positions and the discipline to hold through long stretches of nothing. Treat as research, not as a trade plan. |
| **Any of 1–3 fails** | The earnings-surprise signal does not survive the standard applied to everything else. The system has no measured edge anywhere, and the honest answer is a passive core. |

## Anti-force-fit rules

1. Every year reported, including bad ones. Nothing dropped.
2. No re-specification of SUE, no universe change, no threshold moved.
3. The horizon was declared above before the run.
4. One run. A genuine bug means a disclosed re-run with the pre-fix numbers.
5. The only code change permitted is **saving all events instead of the first
   500** — the current script truncates its own output, which prevents year-by-year
   analysis. That changes no calculation.

## Known limits

- **Survivor universe.** 103 mid-caps that exist today; delisted names absent.
  Favours the signal.
- **No transaction costs**, against a strategy trading every quarter across many
  names. Favours the signal.
- Seasonal-random-walk SUE is a crude surprise measure — no analyst estimates. A
  real PEAD implementation would use analyst surprise, which costs money. A
  failure here does not rule out the paid version working.
