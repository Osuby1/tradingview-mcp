# BUY SCORE v2 (re-weighted) vs v1 - honest test

v2 weights: trend 0.45, structure 0.35, regime 0.15, freshness 0.03, liquidity 0.02. Risk quality REMOVED from the sort.

**The v2 weights were picked from this very sample, so the full-sample row below is CIRCULAR and optimistic. Read the held-out rows.**

## Spearman(score, forward return)
```
FULL (circular)         5d v1=-0.009 v2=+0.103  10d v1=+0.082 v2=+0.186  21d v1=+0.065 v2=+0.148  (n=170)
TIME held-out (40%)     5d v1=+0.257 v2=+0.319  10d v1=+0.361 v2=+0.309  21d v1=+0.375 v2=+0.206  (n=68)
SYMBOL held-out (odd)   5d v1=+0.093 v2=+0.088  10d v1=+0.178 v2=+0.202  21d v1=+0.192 v2=+0.217  (n=92)
```

## Top-minus-bottom quintile, 21-day (pts)
```
FULL (circular)        v1=+0.86   v2=+3.04   delta=+2.18
TIME held-out (40%)    v1=+15.18   v2=+9.32   delta=-5.86
SYMBOL held-out (odd)  v1=+7.58   v2=+2.91   delta=-4.67
```

## Verdict

On held-out time data v2 (+0.206 at 21d) does NOT beat v1 (+0.375) enough to claim an edge. The re-weight removes the return-negative risk-quality component (a real improvement in honesty) but does not buy predictive power. Do not sell v2 as calibrated.

Caveats unchanged from the calibration: one ~4-month strong tape, 60 liquid survivors, close-to-close no costs, freshness untested, and the held-out cuts are only PARTIALLY clean (weight direction was read off the full sample). Run out-of-period before trusting any of this live.
