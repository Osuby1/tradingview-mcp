# Momentum-flag-into-earnings study — RESULTS

**Run:** 2026-07-31, per the locked pre-registration in
`momentum-flag-into-earnings-preregistration.md` (registered 2026-07-30,
before any cohort data was computed). Thresholds were NOT changed.
Companion machine-readable output: `momentum-flag-earnings-study-results.json`.
Study code: `scripts/momentum_flag_earnings_study.py`.

## The verdict in one line

**FAIL. The earnings blackout stands exactly as written, and the PBF
hypothetical is formally closed as a lucky coin flip.** The "poised momentum
flag" setup did not just fail to add an edge into earnings — it did WORSE
than the same stocks' ordinary earnings reactions, on every single one of the
four pre-registered tests.

## What was actually done

The universe was the nightly chain's Russell list (`russell_starter.csv`,
1,200 tickers). Two and a half years of daily prices were pulled for all of
them plus SPY — every ticker came back, none failed. The full 8-quarter
lookback was used (events 2024-07-31 through 2026-07-29).

809 names had, at some point in the window, beaten SPY by 40+ points over six
months, so earnings dates were fetched for those 809 plus an 80-ticker random
sample for the base-rate benchmark — 833 tickers total, **zero fetch
failures, nothing guessed**. That produced 5,947 dateable earnings events to
test.

Each event was tested at the close of the last session before the report,
daily bars only, no lookahead. How the funnel narrowed:

| Filter (all four required) | Events passing |
|---|---|
| Events checked | 5,947 |
| 1. 6-mo return beats SPY by 40+ pts | 1,195 |
| 2. Within 12% of 52-wk high + 3-10% pullback in prior 10 sessions | 732 |
| 3. Final pre-earnings day up 1.5%+ on 1.1x volume | 1,292 |
| 4. Above a rising 200-day average | 3,062 |
| **All four at once (the cohort)** | **40** |

## A fragility warning on the cohort size, stated up front

The cohort is exactly 40 events — the pre-registered minimum, cleared with
zero margin. And two of those 40 are GOOG and GOOGL on the same Alphabet
report (October 2025): two share classes, one economic event. The prereg said
"no exclusions once the filters are set," so both stay in and the study
proceeds at 40. But de-duplicated it is 39 distinct reports, which would have
tripped the automatic "insufficient data" verdict. **Either reading ends in
the same place — the blackout stands** — one by failure, one by
insufficiency. There is no reading under which this setup earned a ticket.

## The numbers (next-day reaction, close before the report to close after)

| Sample | Events | Median | Mean | Win rate | Worst decile | Best decile |
|---|---|---|---|---|---|---|
| **Flag cohort** | 40 | **-1.3%** | -0.1% | **47.5%** | **-15.0%** | +12.3% |
| Benchmark 1: same stocks, all their reports | 302 | +1.7% | +1.6% | 56.0% | -11.1% | +14.7% |
| Benchmark 2: random base rate (labeled sample) | 589 | -0.3% | +0.4% | 47.9% | -10.9% | +12.6% |

The gap itself (close before to next open) was also negative at the median
(-1.4%), and buying the post-earnings open and selling the next open lost
too (-0.3% median). There was no window in which this setup made money.

## The four pre-registered asymmetry tests — all failed

1. **Median reaction above +1.0%?** NO. It was **-1.3%** — wrong sign.
2. **Win rate at least 55%?** NO. **47.5%** — a coin flip that leans against you.
3. **Worst-decile tail shallower than -8%?** NO. **-15.0%** — nearly double
   the allowed pain. Six of the 40 events lost 14% or more overnight.
4. **Beats the same stocks' unconditional earnings median?** NO — and this is
   the damning one. These exact stocks, across ALL their reports in the
   window, gained a median +1.7% on earnings. Conditioned on the "poised
   flag," the median was -1.3%. **The flag state subtracted about 3 points.**
   The bounce into the print looks like buyers showing up early and leaving
   nothing for the report.

Zero of four. The bar required four of four.

## The synthetic options ticket — a mechanical pass that is really a lottery

Per the prereg, each event got a synthetic delta-0.35 call (Black-Scholes,
volatility bumped 1.25x pre-earnings, premium 100% at risk, exit next close,
LABELED SYNTHETIC). The locked bar was "positive expectancy across 40+
events," and the mean return was +104% — so the bar mechanically passes.

Do not be fooled. **The entire profit is one trade**: DOCS, November 2024, a
+34% overnight gap worth +2,917% on the call. Remove that single event and
the mean drops to +32%; remove the top three and it is **-17%**. The median
ticket lost 47% of its premium, only 17 of 40 finished up at all, and 10 of
40 were wiped out near-completely. That is lottery math, not an edge — and
it is moot anyway, because the action mapping required BOTH bars, and the
asymmetry bar failed all four ways.

## What this means for money

- **The earnings blackout stands unchanged.** Shares never hold through a
  print. No paper "earnings ticket" gets designed. The PBF July gap was luck
  — the same posture across 40 real events lost money.
- If anything, the data whispers the opposite trade exists (fading the
  pre-earnings bounce), but that was NOT pre-registered and is noted only as
  a candidate for a future prereg, never acted on from this study.

## Implementation choices the prereg left open (fixed before results)

Rising 200-day = above its level 20 sessions earlier. Pullback measured on
closes vs the trailing 252-session high of daily highs. 50-day volume average
excludes the signal day. Reports time-stamped before noon Eastern count as
before-open. Adjusted (total-return) prices throughout. Option exit values
drop the 1.25x volatility bump (the crush); rate 4%; nearest monthly expiry
at least 5 days out. Full details in the docstring of
`scripts/momentum_flag_earnings_study.py`; per-event rows in the JSON.

## Appendix — all 40 cohort events

| Ticker | Report date | Timing | Close-to-close | Gap | Synthetic call |
|---|---|---|---|---|---|
| AEM | 2024-07-31 | AMC | -1.4% | -0.0% | -56% |
| KGC | 2024-07-31 | AMC | +1.0% | -0.9% | -28% |
| QTWO | 2024-07-31 | AMC | +3.8% | +4.4% | +12% |
| ZETA | 2024-07-31 | AMC | +12.0% | +8.9% | +137% |
| TIGO | 2024-08-05 | BMO | -2.6% | -2.2% | -78% |
| TRGP | 2024-11-05 | AMC | +4.9% | +3.3% | +143% |
| IRM | 2024-11-06 | BMO | -9.0% | -3.1% | -100% |
| KVYO | 2024-11-06 | AMC | -16.3% | -15.0% | -100% |
| DOCS | 2024-11-07 | AMC | +34.1% | +35.6% | +2917% |
| MNDY | 2024-11-11 | BMO | -15.1% | -17.1% | -100% |
| MAMA | 2024-12-16 | AMC | -14.9% | -15.1% | -96% |
| FFIV | 2025-01-28 | AMC | +11.4% | +13.8% | +426% |
| ATEN | 2025-02-04 | AMC | +2.7% | -8.0% | +23% |
| ATRC | 2025-02-12 | AMC | -6.5% | -0.8% | -93% |
| AHR | 2025-02-27 | AMC | -1.3% | -4.4% | -46% |
| KGC | 2025-05-06 | AMC | +2.7% | -2.2% | +0% |
| RBLX | 2025-07-31 | BMO | +10.3% | +19.7% | +186% |
| PLTR | 2025-08-04 | AMC | +7.8% | +6.9% | +113% |
| DLTR | 2025-09-03 | BMO | -8.4% | -9.5% | -99% |
| FEIM | 2025-09-11 | AMC | -21.0% | -8.4% | -100% |
| TSM | 2025-10-15 | AMC | -1.6% | +2.0% | -47% |
| FIX | 2025-10-23 | AMC | +19.0% | +15.8% | +386% |
| GLW | 2025-10-28 | BMO | -3.3% | -5.7% | -68% |
| GOOG | 2025-10-29 | AMC | +2.5% | +6.0% | +12% |
| GOOGL | 2025-10-29 | AMC | +2.5% | +6.2% | +12% |
| IDCC | 2025-10-30 | BMO | +3.5% | -3.4% | +15% |
| MKSI | 2025-11-05 | AMC | +11.0% | +5.2% | +96% |
| AORT | 2025-11-06 | AMC | -5.5% | -1.8% | -93% |
| MLI | 2026-02-03 | BMO | -11.2% | -10.9% | -100% |
| MRCY | 2026-02-03 | AMC | -22.3% | -12.4% | -100% |
| NOV | 2026-02-04 | AMC | -5.9% | -2.7% | -86% |
| NBR | 2026-02-11 | AMC | -9.9% | -6.2% | -97% |
| KGS | 2026-02-25 | AMC | +4.0% | +0.9% | +8% |
| PLAB | 2026-02-25 | BMO | +14.7% | +3.5% | +55% |
| APEI | 2026-03-12 | AMC | +21.2% | +4.7% | +1458% |
| NOV | 2026-04-27 | AMC | -2.5% | -3.8% | -63% |
| FTI | 2026-04-30 | BMO | -1.8% | -3.1% | -63% |
| HUN | 2026-04-30 | AMC | +1.8% | +4.9% | -22% |
| MRX | 2026-05-06 | BMO | -5.9% | -1.4% | -88% |
| SPB | 2026-05-07 | BMO | -7.5% | -1.4% | -98% |

GOOG/GOOGL = one Alphabet report counted twice via dual share classes (kept
per the no-exclusions rule; flagged above). BMO = report before the open,
AMC = after the close. Optional call-flow overlay from the prereg: historical
per-day option volume/open-interest was not obtainable from the free data
used here, so it is logged as unavailable rather than guessed — the prereg
explicitly said the primary verdict does not depend on it.
