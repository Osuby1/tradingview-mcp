# Pre-registration: single PEAD refinement test

Registered 2026-07-22 BEFORE running, so the criterion cannot move after the result.

## The test (ONE run, no parameter sweep)

Take the clean EDGAR seasonal-SUE PEAD pipeline and apply the two theory-justified
refinements TOGETHER, once:

1. **Universe = mid-cap band, $2B-$12B** (drop the sub-$2B names from the small/mid
   set - that is where small-cap idiosyncratic noise is worst).
2. **Winsorize forward returns at the 2.5 / 97.5 percentiles** before computing IC
   and quintile means, so a handful of 40%+ movers cannot hijack the result.

Everything else identical: seasonal-SUE, point-in-time filing dates, drift from the
day after filing, +20d and +60d, event-level.

## Pre-specified success criterion

The refinement SUCCEEDS if, and only if, the **top-minus-bottom quintile spread
turns POSITIVE at BOTH 20d and 60d** (baseline small/mid was -2.44pt at 20d,
+0.06pt at 60d - it did not sort). IC is expected to stay ~+0.05 (rank-based, so
winsorizing barely moves it); the whole question is whether cleaning the noise makes
the tradeable extremes sort the right way.

- **PASS** -> a clean, free, tradeable PEAD edge. Forward-validate via the outcome
  tracker. Stop refining.
- **FAIL** -> seasonal-SUE has hit its ceiling; the paid analyst-surprise data
  (~$59/mo FMP) is the next real decision. Stop refining either way - no more
  free-parameter tinkering, that is just overfitting.

This is the LAST free refinement. One test. Whatever it says, we act on it and stop.
