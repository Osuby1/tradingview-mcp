# Winner-factor study — what the +15% picks had in common (2026-08-01)

**EXPLORATORY, not pre-registered.** Requested by Omar 8/1: "study which
combination of factors are consistent across recommended stocks that rose
over 15%." Data limit stated up front: the machine track record begins
**2026-07-01** — this is ONE month of picks (Omar asked for two; the second
month does not exist in recorded form).

## Method

- Universe: every track-record pick 7/01..7/17 (so every name had >=2 weeks
  of runway), deduped to earliest pick per ticker -> **293 names** (2 skipped
  on data).
- Factors computed from history truncated to the PICK DAY (no hindsight):
  the 5 readiness components + composite, squeeze percentile, TTM squeeze,
  distance-to-trigger, ADX(14), DI margin, extension vs 200d, 200d slope,
  pick-day RVOL vs 50d, pick-day % move, plus scan tab and grade.
- Outcome: max CLOSE after pick vs pick-day close (adjusted Yahoo series,
  conservative — no intraday spikes). **Winner = best close >= +15%.**
- 16 winners / 293 = **5.5% base rate**. 9 of 16 winners had a single
  post-pick day of +8% or more (catalyst-driven).

## Single factors — winner rate vs the 5.5% base

Helped (lift > 1.3x):
| factor | n | winners | rate | lift |
|---|---|---|---|---|
| grade A/A+ | 40 | 5 | 12.5% | 2.29x |
| **readiness <= 30 (RESTING)** | 98 | 9 | 9.2% | **1.68x** |
| extension > 20% above 200d | 208 | 16 | 7.7% | 1.41x |
| tab COOLING | 146 | 11 | 7.5% | 1.38x |
| DI margin >= 10 | 197 | 14 | 7.1% | 1.30x |
| ADX >= 25 | 185 | 13 | 7.0% | 1.29x |

Hurt (lift < 0.7x):
| factor | n | winners | rate | lift |
|---|---|---|---|---|
| readiness >= 60 | 81 | 3 | 3.7% | 0.68x |
| squeeze tight (pctile<=25) | 59 | 2 | 3.4% | 0.62x |
| **tab COILED** | 98 | 1 | 1.0% | **0.19x** |
| **TTM squeeze ON** | 30 | 0 | 0.0% | 0.00x |
| RVOL >= 1.5 on pick day | 29 | 0 | 0.0% | 0.00x |
| pick day already +3% | 34 | 0 | 0.0% | 0.00x |
| DI margin < 5 | 52 | 0 | 0.0% | 0.00x |
| ADX < 20 | 59 | 1 | 1.7% | 0.31x |

Best pair: **readiness<=30 AND DI margin>=10 -> 7/47 = 14.9% (2.73x)**.
Next: readiness<=30 + ADX>=25 -> 13.4% (2.46x).
Every single winner was >20% above its 200-day. ALL 16.

## The consistent winner profile (12-14 of the 16 fit it)

**A stock that had ALREADY proven itself with a powerful advance (ADX 35-60,
buyers firmly in control DI +10..+29, riding 25-85% above its 200-day),
that was RESTING at pick time (readiness low, bands wide from the PRIOR
move, quiet volume - winner median pick-day RVOL 0.88, none over 1.5) -
and then re-ignited, in over half the cases on a catalyst (earnings gap /
news day of +8%+).** Second-leg continuation, not spring-compression.

## What this overturns / confirms

1. **The coiled-spring theory failed this month.** COILED tab: 1 winner in
   98 picks. TTM squeeze ON: 0 in 30. Compression predicted a move coming
   but the moves went to the rested momentum names instead. (0/30 is NOT
   statistically damning on its own — expected ~1.7 winners by chance — but
   the whole compression family pointing the same way is the signal.)
2. **Low readiness out-performed high readiness** (9.2% vs 3.7%). Consistent
   with the 8/1 calibration look: the score does not time moves in this
   pool, and if anything leaned backwards this month. Both files now say it.
3. **Excitement at pick = poison.** Picks made ON a big-volume day (RVOL>=1.5)
   or an already-up-3% day: zero winners from 63 picks. The winners were
   picked quiet.
4. **The A-grade earned something** (12.5% vs 5.5%) — first evidence the
   grading layer adds value; thin (n=40), watch it.
5. **Catalysts matter more than posture:** 9/16 winners needed a news/earnings
   day. Tension to manage honestly: the earnings blackout (options) and the
   trim-before-print rule (stock) would have limited capture on some of
   these. Separate question, flagged not resolved.

## Caveats — read before believing

n=16 winners. One month, one regime (AI/energy chase tape, defensives
dumped). ~27 factors and dozens of pairs tested -> some lifts are chance
(multiple-comparison risk is REAL at this n). Outcome is close-based;
dedup keeps only each ticker's earliest July pick. Universe is gate-shaped
(everything above a rising 200d) so factors can only discriminate within
an already-filtered pool. **This is hypothesis-generating, not proof.**

## Proposed pre-registration (for the next Friday review to adopt/refuse)

Cohort rule, frozen before any forward data: **"REST-CONTINUATION
candidate" = DI margin >= 10 AND ADX >= 25 AND readiness <= 30 AND pick-day
RVOL < 1.2.** Track every nightly candidate for/against the rule; grade
after 4+ weeks: does the cohort hit +15%-within-15-sessions materially more
often than the rest? Kill criterion: if the cohort's edge is <1.5x after 8
weeks, drop the rule. Until adopted and proven, NOTHING in this file
changes sizing, gates, or vetoes.
