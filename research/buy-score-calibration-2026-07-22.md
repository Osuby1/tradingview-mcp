# BUY SCORE calibration - hard facts

**Signals:** 170 historical Chandelier BUY flips across 60 names.  
**Forward return:** close-to-close, no stops/costs.  
**Scored with** the live `score_long()`.  

## Read this before the numbers
- Close-to-close return tests only the DIRECTIONAL half of the score. The risk-quality (stop in ATR) and liquidity components - about 35% of the weight - are about SURVIVAL and SIZING and a raw-return test cannot credit them. They are reported separately below, not blended.
- Freshness is constant (~every signal scored at age 0), so it carries ZERO discriminating power in this design.
- Sample skews to a strong tape and uses liquid survivors. Both inflate results. Treat these as an UPPER bound on real-world edge.

- Spearman(score, 5d return) = **-0.009**  (n=170)
- Spearman(score, 10d return) = **+0.082**  (n=170)
- Spearman(score, 21d return) = **+0.065**  (n=170)

  Reference: 0 = no relationship. |0.1| weak, |0.2| modest, |0.3|+ genuinely useful for ranking. Negative = the score is BACKWARDS.

## Return by score decile (21-day)

| Decile | Score range | n | mean % | median % | win % |
|---|---|---|---|---|---|
| 1 (worst) | 14-39 | 17 | +1.33 | -4.60 | 47% |
| 2  | 40-47 | 17 | +2.60 | +1.63 | 53% |
| 3  | 47-50 | 17 | +8.58 | +3.12 | 59% |
| 4  | 51-56 | 17 | +1.24 | -2.11 | 41% |
| 5  | 56-58 | 17 | +3.36 | -2.13 | 35% |
| 6  | 58-60 | 17 | +3.03 | +0.94 | 59% |
| 7  | 60-63 | 17 | +3.42 | +0.21 | 53% |
| 8  | 63-65 | 17 | +2.35 | +0.48 | 53% |
| 9  | 65-73 | 17 | +2.67 | +3.17 | 59% |
| 10 (best) | 73-85 | 17 | +2.97 | +1.79 | 59% |

## Top vs bottom quintile (21-day)

- Bottom 20% by score: mean +1.96%, win 50% (n=34)
- Top 20% by score: mean +2.82%, win 59% (n=34)
- **Spread (top - bottom): +0.86 pts.**
- **The score separates almost nothing.**

Monotonicity: 6/9 decile steps go the right way (9/9 = perfectly monotonic, ~4-5 = coin-flip noise).

## Which components carry it (21-day)

| Component | weight | Spearman vs return |
|---|---|---|
| risk quality (stop/ATR) | 30 | -0.052 |
| trend (ADX/DI) | 25 | +0.092 |
| regime (vs 200d) | 20 | +0.041 |
| structure (vs ZLSMA) | 10 | +0.086 |
| freshness | 10 | flat/none |
| liquidity | 5 | flat/none |

A component with near-zero or negative correlation is dead weight in the score, or actively wrong. This is where the score should be re-weighted.

---

## BOTTOM LINE - the cold facts

**The BUY SCORE does not predict forward returns. It is not calibrated; it is noise.**

- Rank correlation with 21-day return: **+0.065**. With 5-day: **-0.009** (literally
  backwards). Anything under |0.1| is "no relationship". This is under it at every horizon.
- Top-quintile minus bottom-quintile 21-day return: **+0.86 points**. A score that
  ranked anything would show several points of spread. This shows ~none.
- Deciles are **not monotonic** (6/9 steps, ~coin flip). The eye-catching +8.58% in
  decile 3 is a fat-tail artifact - its MEDIAN is +3.12%, and the medians are flat
  (roughly -2% to +3%) across all ten deciles with no trend. The mean is distorted by
  a handful of monster winners (INTC +107%, QCOM +60%, MU +59%) that landed in
  mid-range score buckets by luck.

**Component autopsy** (what's actually in the score vs what should be):
- **risk quality (30% weight): -0.052** - the single heaviest component is slightly
  NEGATIVE. Tighter stops did not predict better returns; if anything the reverse.
  This is the most damning line in the study.
- **trend ADX/DI (25%): +0.092** - the only component with a pulse, and it's weak.
- **regime vs 200d (20%): +0.041** - near zero.
- **structure vs ZLSMA (10%): +0.086** - weak but the second-best.
- **freshness (10%) and liquidity (5%): zero** by construction in this test.

So ~55% of the score's weight (risk quality + regime + freshness + liquidity) does
nothing or works against returns here. The ~35% that has any directional signal
(trend + structure) is weak.

## What this means, honestly

1. **Stop trusting the rank order.** CTRE being "#1" told you almost nothing about its
   forward return relative to the field. The rank is a reasonable-looking sort, not a
   forecast. Exactly what I warned "UNCALIBRATED" meant - now measured.

2. **The gate stack (pass/block) is a different thing and is NOT indicted here.** This
   study scored every signal 0-100; it did not test "gated PASS vs everything else".
   The binary gates (regime DEEP-FAIL, ATR floor, liquidity) are risk controls, not
   return predictors, and a close-to-close test can't judge them.

3. **The heavy risk-quality weight is defensible on RISK grounds even though it's
   return-negative** - a tight ATR stop is about survival and position size, not about
   forward return. But it should not be dressed up as, or dominate, a "quality" rank
   that users read as "most likely to go up".

## What I would change (not yet done - your call)

- **Demote the score from a ranking to a two-tier label**: "clears all gates" vs
  "starter" vs "blocked". That is the part with a real basis. Drop the 0-100 precision
  that implies a forecast it does not have.
- If a numeric rank is wanted, **re-weight toward trend (ADX/DI) and structure**, the
  only two components with any signal, and stop letting risk-quality dominate the sort.
- **Re-run this out-of-sample** on a different period and a wider name set before
  trusting ANY re-weighting - 170 signals in one strong-tape stretch is a small,
  biased sample and even the "winners" here (trend at +0.09) could be noise.

## Caveats that make even these weak numbers an UPPER bound
- One ~4-month window (Mar-Jun 2026), mostly a strong tape.
- 60 liquid survivors, chosen because they resolve cleanly = survivorship bias.
- Close-to-close, no stops/costs/slippage.
- Freshness untested (all signals scored at age 0).
- 170 signals is thin for decile work (17 per bucket).
