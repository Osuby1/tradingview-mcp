# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-07-27.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DVN | long | 45.11 | 43.16 | 1 | -4.3% | -4.3 | +1.4 | -4.6 | STOP | STOPPED | LOSS |
| HAS | long | 88.17 | 90.61 | 1 | +2.8% | +2.8 | +2.9 | -1.0 | - | OPEN | WIN (open) |
| SJM | long | 117.21 | 121.05 | 1 | +3.3% | +3.3 | +3.8 | -1.1 | - | OPEN | WIN (open) |
| MLI | long | 63.53 | 64.17 | 1 | +1.0% | +1.0 | +2.9 | -1.2 | - | OPEN | WIN (open) |
| SMH | short | 568.92 | 548.55 | 7 | +3.6% | +5.1 | +5.9 | -4.1 | - | OPEN | WIN (open) |
| KRE | long | 77.92 | 75.52 | 7 | -3.1% | -1.5 | +0.2 | -5.1 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 247.86 | 5 | +7.3% | +7.7 | +8.8 | -0.4 | - | OPEN | WIN (open) |
| PFE | long | 24.86 | 24.67 | 5 | -0.8% | -0.4 | +0.1 | -2.5 | - | OPEN | LOSS (open) |
| AMT | long | 167.03 | 166.74 | 5 | -0.2% | +0.2 | +1.6 | -2.4 | STOP | STOPPED | LOSS |
| ECVT | long | 12.35 | 12.24 | 4 | -0.9% | +0.3 | +7.5 | -1.7 | - | OPEN | LOSS (open) |
| GS | long | 1078.0 | 1048.23 | 4 | -2.8% | -1.5 | +2.7 | -4.5 | - | OPEN | AVOID VALIDATED |
| CEG | long | 253.73 | 270.0 | 4 | +6.4% | +7.6 | +10.2 | +0.8 | TARGET | TARGET HIT | AVOID WRONG (it ran) |
| GDX | long | 76.5 | 75.73 | 3 | -1.0% | +0.1 | +1.9 | -3.5 | - | OPEN | AVOID VALIDATED |
| DPZ | long | 319.83 | 343.53 | 3 | +7.4% | +8.5 | +9.0 | -1.3 | - | OPEN | WIN (open) |

## Scorecard

- Total calls logged: 14
- Directional (non-avoid): 11  |  matured/resolved: 2
- Win rate (resolved): 0/2 = 0%
- Mean return (resolved): -2.25%
- Mean excess vs SPY (resolved): -2.05%
- Avoids validated so far: 2/3 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
