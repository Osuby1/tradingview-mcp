# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-07-24.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DVN | long | 45.11 | - | - | - | - | - | - | - | TOO NEW | - |
| HAS | long | 88.17 | - | - | - | - | - | - | - | TOO NEW | - |
| SJM | long | 117.21 | - | - | - | - | - | - | - | TOO NEW | - |
| MLI | long | 63.53 | - | - | - | - | - | - | - | TOO NEW | - |
| SMH | short | 568.92 | 561.19 | 6 | +1.4% | +2.9 | +5.6 | -4.1 | - | OPEN | WIN (open) |
| KRE | long | 77.92 | 75.73 | 6 | -2.8% | -1.2 | +0.2 | -5.1 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 247.56 | 4 | +7.2% | +7.6 | +7.8 | -0.4 | - | OPEN | WIN (open) |
| PFE | long | 24.86 | 24.54 | 4 | -1.3% | -0.9 | -0.4 | -2.5 | - | OPEN | LOSS (open) |
| AMT | long | 167.03 | 166.67 | 4 | -0.2% | +0.2 | +1.6 | -2.4 | STOP | STOPPED | LOSS |
| ECVT | long | 12.35 | 12.46 | 3 | +0.9% | +2.1 | +7.5 | -1.6 | - | OPEN | WIN (open) |
| GS | long | 1078.0 | 1061.23 | 3 | -1.6% | -0.3 | +2.7 | -2.4 | - | OPEN | AVOID VALIDATED |
| CEG | long | 253.73 | 274.35 | 3 | +8.1% | +9.4 | +10.2 | +0.8 | TARGET | TARGET HIT | AVOID WRONG (it ran) |
| GDX | long | 76.5 | 75.23 | 2 | -1.7% | -0.5 | +1.9 | -3.5 | - | OPEN | AVOID VALIDATED |
| DPZ | long | 319.83 | 332.97 | 2 | +4.1% | +5.2 | +5.0 | -1.3 | - | OPEN | WIN (open) |

## Scorecard

- Total calls logged: 14
- Directional (non-avoid): 7  |  matured/resolved: 1
- Win rate (resolved): 0/1 = 0%
- Mean return (resolved): -0.22%
- Mean excess vs SPY (resolved): +0.21%
- Avoids validated so far: 2/3 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
