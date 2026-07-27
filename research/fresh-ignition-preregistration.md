# Fresh-Ignition "A" grade backtest — pre-registration

Committed 2026-07-26, BEFORE any study code exists.

## Where this hypothesis comes from — stated honestly

Omar looked at the origination scanner's recent recommendations and saw a
pattern: **Fresh Ignitions with an "A" grade look strong; anything on the
Cooling tab looks bad; Coiled names look like they never deliver.** That
observation was made AFTER seeing recent outcomes, which is exactly how
curve-fitting starts — so the test runs on FIVE YEARS (2021–2025) where the
recent observation window is a tiny slice, and the pass/fail bands are frozen
here first. His proposed exit is also under test: **sell the moment an
A-grade Fresh Ignition name moves to the Cooling tab.**

Context worth remembering: the scanner's own 406-pick logbook averaged −2.2%
with grades showing no edge — but that mixed ALL tabs and a fixed 21-day
window. This test asks the sharper question the logbook cannot answer:
does the tab × grade combination, managed by tab transitions, work?

## Frozen design

**Rules replicated from `stage2_leader_scanner_v3.py` verbatim** (config
values, score weights, grade bands, flag logic — the file is the spec):
- FRESH IGNITION = flag LEADER: stage-2 trend + within 15% of 52-wk high +
  fresh volume ignition with persistence + OBV accumulation + NOT extended.
- COOLING = extended (RSI14>70 or >25% over 50-SMA or +30%/60d) but trend and
  leadership intact, pre-cap score ≥65 or 60-day run ≥25%, not yet at the
  pullback zone.
- COILED = trend + leadership + squeeze, no ignition.
- Grade from the scored bands: A+ ≥85, A ≥70, B ≥60. Capacity ranking is
  computed cross-sectionally within the universe daily, as the scanner does.

**Universe:** `russell_starter.csv` (1,200 current names) — TODAY'S list, so
survivorship bias flatters every cohort; declared, and it makes a failure
verdict conservative. Technical-only (no Finviz fundamental gate), matching
how the scan actually runs nightly.

**Known approximation, declared:** weekly RSI/ROC use completed weeks
(values lag the scanner's intraweek reads by up to 4 days). Applied
identically to every cohort and both directions of every comparison.

**Episodes:** enter at the CLOSE of the first day a name qualifies as
FRESH IGNITION with the grade under test; one open episode per name;
re-entry allowed after exit. 10 bp round trip.

**Exit rules (all four run on the same entries):**
- **R1 — Omar's rule (primary):** exit at the close of the first day the name
  sits on COOLING. Otherwise hold; 250-trading-day cap.
- R2 — stricter variant: exit when the name stops being a LEADER for ANY
  reason (cooling, squeeze, broken trend, excluded).
- R3 — plain 60-day hold (no management).
- R4 — the current live exit (5% stop, gap-aware; 20% ratchet once earned;
  120-day cap) for comparison with everything measured this week.

**Cohorts:** A-grade (primary), A+ and B (controls — does the "A" itself
carry signal?), plus forward 60-day returns of COOLING-tab and COILED-tab
names to test the "dismiss them" halves of the hypothesis.

**Primary metric:** mean excess vs SPY over each trade's own holding window,
for A-grade Fresh Ignitions under R1. Hit rate, median, per-year (2022 always
shown), odd/even alphabetical split.

## Pre-committed conclusions (primary cohort, R1)

- **Mean excess ≥ +2.0 pt AND median > 0 AND holds directionally in both
  odd/even halves** → "The tab × grade signal is real on this sample —
  promote to the shadow lane for live forward grading. NOT live money; the
  freeze and promotion rules stand."
- **Mean excess between −2 and +2 pt, or median ≤ 0, or halves disagree** →
  "Looks-good-recently was recency: the A-grade Fresh Ignition cohort is
  ordinary once five years are counted. No change to anything."
- **Mean excess ≤ −2.0 pt** → "The tab actively selects bad entries; the
  scanner stays a watchlist feeder only."
- **Exit comparison:** R1 is judged against R3 (does tab-exit beat doing
  nothing?) and R4 (does it beat the current rule?). If R1 < R3 − 1 pt, the
  pre-committed read is "the Cooling exit sells strength — same defect as the
  2:1 target, measured before it touches money."

One run. No parameter changes after this commit. Grid additions forbidden.
