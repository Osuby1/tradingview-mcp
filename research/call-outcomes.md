# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-07-30.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| JNJ | long | 265.53 | 255.82 | 1 | -3.7% | -5.3 | +1.4 | -4.1 | - | OPEN | LOSS (open) |
| DGX | long | 235.22 | 234.3 | 1 | -0.4% | -2.1 | +1.1 | -2.6 | - | OPEN | LOSS (open) |
| DVN | long | 45.11 | 44.17 | 4 | -2.1% | -2.5 | +1.4 | -6.0 | STOP | STOPPED | LOSS |
| HAS | long | 88.17 | 94.53 | 4 | +7.2% | +6.8 | +10.0 | -1.0 | TARGET | TARGET HIT | WIN |
| SJM | long | 117.21 | 122.21 | 4 | +4.3% | +3.9 | +8.9 | -1.1 | TARGET | TARGET HIT | WIN |
| MLI | long | 63.53 | 66.86 | 4 | +5.2% | +4.9 | +6.0 | -1.2 | - | OPEN | WIN (open) |
| SMH | short | 568.92 | 538.9 | 10 | +5.3% | +6.5 | +11.5 | -4.1 | - | OPEN | WIN (open) |
| KRE | long | 77.92 | 75.9 | 10 | -2.6% | -1.4 | +0.2 | -5.1 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 257.04 | 8 | +11.3% | +11.3 | +16.9 | -0.4 | TARGET | TARGET HIT | WIN |
| PFE | long | 24.86 | 24.91 | 8 | +0.2% | +0.2 | +2.6 | -2.5 | - | OPEN | WIN (open) |
| AMT | long | 167.03 | 174.46 | 8 | +4.5% | +4.5 | +8.0 | -2.4 | STOP | STOPPED | WIN |
| ECVT | long | 12.35 | 12.09 | 7 | -2.1% | -1.2 | +7.5 | -3.2 | - | OPEN | LOSS (open) |
| GS | long | 1078.0 | 1024.86 | 7 | -4.9% | -4.0 | +2.7 | -9.3 | STOP | STOPPED | AVOID VALIDATED |
| CEG | long | 253.73 | 263.56 | 7 | +3.9% | +4.8 | +10.2 | +0.8 | TARGET | TARGET HIT | AVOID WRONG (it ran) |
| GDX | long | 76.5 | 76.78 | 6 | +0.4% | +1.1 | +1.9 | -5.7 | - | OPEN | AVOID QUESTIONABLE |
| DPZ | long | 319.83 | 352.25 | 6 | +10.1% | +10.9 | +14.0 | -1.3 | - | OPEN | WIN (open) |
| SPY | short (hedge) - DECLINED | 737.6 | 741.69 | 3 | -0.6% | -0.9 | +1.1 | -1.1 | - | OPEN | LOSS (open) |
| JNJ | long | 265.95 | 255.82 | 2 | -3.8% | -3.9 | +3.4 | -4.3 | - | OPEN | LOSS (open) |
| DGX | long | 231.84 | 234.3 | 2 | +1.1% | +0.9 | +3.6 | -1.2 | - | OPEN | WIN (open) |

## Scorecard

- Total calls logged: 19
- Directional (non-avoid): 16  |  matured/resolved: 5
- Win rate (resolved): 4/5 = 80%
- Mean return (resolved): +5.02%
- Mean excess vs SPY (resolved): +4.82%
- Avoids validated so far: 1/3 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
