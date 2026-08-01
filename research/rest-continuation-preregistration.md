# PRE-REGISTRATION — Rest-Continuation cohort (ADOPTED by Omar 2026-08-01)

**Frozen at commit time. The git timestamp of this file's first commit is the
pre-registration proof. No edits to the rule, metric, schedule, or kill
criterion after this commit — amendments require a new dated section that
never overwrites this one.**

## Origin

`research/winner-factor-study-2026-08-01.md` (exploratory, one month of
picks, n=16 winners): July's +15% winners were overwhelmingly RESTED
momentum leaders — powerful established trend, buyers in control, low
readiness (post-move consolidation), quiet pick-day volume — not coiled
squeezes (COILED tab 1/98, TTM squeeze 0/30). This test decides whether
that profile is real or one month's noise.

## Frozen cohort rule

A nightly scan candidate (any hit or gated long in
`watchlists/universe-results-<date>.json`) is a **REST-CONTINUATION
member** on the night it appears iff ALL of:

1. **DI margin >= +10** (Wilder +DI minus -DI, 14-day, computed from
   Yahoo-adjusted daily OHLC — same code path as the study)
2. **ADX(14) >= 25** (same computation)
3. **Readiness score <= 30** (the nightly `readiness_batch.py` stamp)
4. **RVOL < 1.2** (that day's volume vs 50-day average)

Non-members = every other candidate the same night (the control pool).
Missing data on any factor = NOT a member, logged with nulls (fails closed).

## Frozen outcome metric

**Win = the stock's best CLOSE within the next 15 trading sessions reaches
>= +15% over its tag-night close** (Yahoo-adjusted closes, same series for
everyone). Each ticker is graded on its FIRST tagged night only (later
re-appearances tracked but excluded from the primary comparison).

**Primary comparison:** cohort win-rate vs non-cohort win-rate, same nights.

## Frozen schedule and kill criterion

- Tagging: automatic, every nightly chain run from 2026-08-03 onward
  (`scripts/rest_continuation_tracker.py`, chain step 4, non-fatal).
- Friday reviews from **2026-08-07**: report cohort size and any early
  outcomes (no verdict before minimums are met).
- **First real read: Friday 2026-08-28** (first tags fully aged 15 sessions).
- **Verdict: Friday 2026-09-25** (8 weeks).
- **Minimums for ANY verdict:** >= 15 first-tag cohort members aged >= 15
  sessions AND >= 8 total winners across both groups; otherwise extend, no
  conclusion.
- **KILL: if cohort win-rate lift < 1.5x vs non-cohort at the 8-week
  verdict, the rule is dropped** and the study's finding is recorded as
  not-replicated.
- **SUCCESS: lift >= 1.5x at verdict** -> the profile earns a labeled
  column/flag in the workbook and a Friday re-registration for whether it
  deserves ranking power. It does NOT gain veto or sizing power from this
  test alone.

## Until the verdict

Nothing changes: gates, sizing, vetoes, readiness label, no-chase — all
unchanged. The cohort tag is measurement only. Nobody trades off it.

## Addendum 2026-08-01 (display only — rule/metric/schedule untouched)

Omar directed the cohort tag be SHOWN on recommendations under a
self-explanatory name: **"RESTED LEADER — on trial"**. Appears as a column
on the workbook's Fresh Buys / Gated Longs tabs and on per-pick recs in
briefs. Presentation only: the tag carries zero weight in gates, sizing,
ranking, or advice until the 2026-09-25 verdict. Ledger keys and the frozen
rule above are unchanged.
