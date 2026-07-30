# Pre-registration: "Momentum flag into earnings" — is the reaction asymmetric?

**Registered:** 2026-07-30, before any cohort data is computed. Prompted by the
PBF forensic (run same day, data through the 7/29 close only): a top-decile
relative-strength refiner in a LOADED group made an orderly 5-session, -7%
flag off its 52-week high, bounced +3.9% on the week's highest volume the day
before its scheduled Q2 report, with rising near-dated OTM call open interest —
then gapped +15% on the print. The SAME stock's April print, from a similar
momentum posture, went -12.8%. This study decides which story the data tells
across a real cohort. Companion to
`extended-runner-options-study-preregistration.md`; run at the Friday
hard-stats review (2026-07-31 or the next one after).

## Question

For stocks entering a scheduled earnings report in a defined "poised momentum
flag" state, is the next-day earnings reaction asymmetrically positive — enough
to justify a strictly premium-capped, paper-only options tactic — or is the
apparent edge just hindsight on the winners?

## Cohort (fixed before looking)

Universe = our scan universe (russell3000.csv as used by the nightly chain).
Every scheduled earnings report in the lookback window (minimum 4 quarters,
extend to 8 if data allows) where ALL of the following were true at the close
of the last session BEFORE the report — computed from daily bars with no
lookahead:

1. 6-month total return beats SPY's by >= 40 points (top-decile RS proxy).
2. Price within 12% of its 52-week high, AND a pullback of 3-10% from that
   high occurred within the prior 10 sessions (the "flag").
3. The final pre-earnings session closed UP >= 1.5% on volume >= 1.1x its
   50-day average (the "bounce into the print").
4. Price above a rising 200-day SMA.

Optional overlay recorded but NOT required (data coverage is uncertain
historically): rising call volume/OI in near-dated OTM strikes. Logged where
obtainable; the primary verdict does not depend on it.

**No exclusions once the filters are set.** PBF's April loser-quarter type
events stay in. If the cohort is under 40 qualifying events, auto-verdict =
"insufficient data — earnings blackout stands unchanged."

## Measurements per event

- Next-session open-to-open and close-to-close reaction (the gap IS the trade).
- Distribution: median, mean, win rate, 10th/90th percentile tails.
- Benchmark 1: the SAME stock's unconditional earnings reactions (is the flag
  state adding anything beyond "this stock moves on earnings"?).
- Benchmark 2: all-universe earnings reactions in the window (base rate).
- Simulated capped-premium expression per event: nearest-monthly call closest
  to delta 0.35 (deliberately NOT the 0.60-0.75 overlay standard — this is a
  defined-risk binary ticket, different instrument class, labeled as such),
  priced synthetically (BS, IV = max(RV20, RV60) x 1.25 pre-earnings bump,
  LABELED SYNTHETIC), premium = 100% at risk, exit at next-session close.

## Pre-registered verdict lines (written before results)

- **Asymmetry bar:** median close-to-close reaction > +1.0% AND win rate
  >= 55% AND the 10th-percentile tail shallower than -8% AND the conditioned
  distribution beats Benchmark 1 (same-stock unconditional) on median. All
  four or it fails.
- **Options bar:** the synthetic capped-premium simulation shows positive
  expectancy after the -100% losers, across >= 40 events.
- **Action mapping:** BOTH pass -> design a paper-only "earnings ticket"
  tactic (max $1,000 premium = 0.1% of account per event, hard cap 2 events
  per week, its own pre-registration, minimum 30 paper events before any real
  dollar). Either fails -> **the earnings blackout stands exactly as written**
  and the PBF hypothetical is formally closed as a lucky coin flip.
- The blackout rule is NOT weakened by a pass — shares still never hold
  through a print; only the defined-risk paper ticket would exist.
- Thresholds change only via an explained commit BEFORE the study runs.
