# Does the Magical +/-100 cut actually separate returns?

**Written at** 2026-07-22 13:17 local  
**Signals** 1725 historical Chandelier BUY flips, candles, ~300 bars/symbol  
**Magical measured AT THE SIGNAL BAR**, not today  
**Forward returns** simple close-to-close, no stops, no costs

## The gate as currently written

| Group | Horizon | n | mean % | median % | win rate |
|---|---|---|---|---|---|
| Magical < 100 (ALLOWED) | 5d | 1114 | +1.13 | +0.43 | 53.2% |
| Magical < 100 (ALLOWED) | 10d | 1105 | +1.98 | +0.35 | 52.7% |
| Magical < 100 (ALLOWED) | 21d | 1045 | +2.20 | +0.72 | 52.1% |
| Magical >= 100 (REJECTED) | 5d | 587 | +1.20 | +0.35 | 52.6% |
| Magical >= 100 (REJECTED) | 10d | 587 | +0.59 | +0.06 | 50.4% |
| Magical >= 100 (REJECTED) | 21d | 568 | +2.17 | +0.40 | 51.1% |

## Return by Magical bucket

| Bucket | n | 5d mean | 10d mean | 21d mean | 21d median | 21d win |
|---|---|---|---|---|---|---|
| <= -100  (oversold) | 3 | +2.44 | +1.42 | +0.59 | +3.55 | 66.7% |
| -100 to -50 | 64 | -1.28 | -0.46 | -0.87 | -0.25 | 49.1% |
| -50 to 0 | 324 | +0.73 | +1.89 | +0.37 | -0.58 | 46.8% |
| 0 to 50 | 373 | +1.33 | +1.44 | +1.37 | +0.70 | 51.9% |
| 50 to 79 | 205 | +1.47 | +3.55 | +7.03 | +1.97 | 57.0% |
| 79 to 100  (untested band) | 163 | +1.96 | +2.35 | +2.73 | +1.92 | 57.1% |
| 100 to 130 (just over cut) | 198 | +0.87 | +1.25 | +2.75 | +0.46 | 52.1% |
| 130 to 200 | 275 | +0.71 | -0.12 | +0.86 | +0.00 | 49.8% |
| > 200  (extreme) | 120 | +2.85 | +1.14 | +4.20 | +0.85 | 52.1% |

## Every candidate cut, ranked by 21d mean separation

| Cut | n below | n above | 21d mean below | 21d mean above | gap |
|---|---|---|---|---|---|
| 150 | 1337 | 276 | +2.44 | +0.98 | +1.46 |
| 160 | 1379 | 234 | +2.39 | +1.02 | +1.37 |
| 140 | 1284 | 329 | +2.30 | +1.76 | +0.54 |
| 240 | 1552 | 61 | +2.21 | +1.68 | +0.53 |
| 130 | 1233 | 380 | +2.29 | +1.89 | +0.40 |
| 110 | 1113 | 500 | +2.24 | +2.09 | +0.15 |
| 90 | 977 | 636 | +2.23 | +2.14 | +0.09 |
| 100 | 1045 | 568 | +2.20 | +2.17 | +0.03 |
| 230 | 1544 | 69 | +2.19 | +2.19 | +0.00 |
| 170 | 1416 | 197 | +2.19 | +2.19 | +0.00 |

## Verdict on 100 specifically

- Below 100: n=1045, 21d mean +2.20%, win 52.1%
- At/above 100: n=568, 21d mean +2.17%, win 51.1%
- Separation: **+0.03 pts of 21-day return**

**The cut does essentially nothing.** A gate that does not separate returns is not risk control, it is just lost trades.

## Caveats

- Close-to-close returns. No stops, no slippage, no position sizing.
  The live system exits on the Chandelier stop, so real results differ.
- ~300 bars/symbol covers roughly mid-2025 to now: a strong tape for
  most of it. Momentum cuts flatter themselves in a bull market.
- Survivorship: the universe is today's watchlist, not the watchlist
  as it stood in 2025.
- Signals in the last 21 bars have no complete forward window and are
  excluded from that horizon automatically.
