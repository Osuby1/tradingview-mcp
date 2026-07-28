# Buyer/seller margin (+DI - -DI) - pre-registered predictive test

Run 2026-07-28 on the frozen 7/22 calibration set (170 signals, April-June window). Hypothesis came from the week-of-7/24 four-name batch (HAS/SJM dominant-buyer names outran MLI's +4 margin), so the dataset is independent of the trades that raised the question.

| Horizon | n | Spearman: DI margin | Spearman: raw ADX | Spearman: v2 trend sub | Top-25% mean | Bottom-25% mean |
|---|---|---|---|---|---|---|
| 5 days | 170 | -0.112 | +0.205 | +0.190 | +1.90% | +2.98% |
| 10 days | 170 | -0.134 | +0.184 | +0.169 | +0.45% | +3.03% |
| 21 days | 170 | -0.121 | +0.111 | +0.091 | +4.13% | +4.01% |

**Decision rule (set before the run):** margin earns ranking weight only if 21d Spearman beats raw ADX AND >= +0.10.
**Verdict: FAIL - margin stays a DISPLAY-ONLY column.**

Caveats: one tape regime (spring 2026), unrealized 21-day horizons, and a modest sample. A pass here means 'worth weighting and re-testing', never 'proven'. The Fresh Buys column ships either way - it is information, not a rule.
