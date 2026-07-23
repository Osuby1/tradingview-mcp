# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-07-23.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SMH | short | 568.92 | 580.17 | 5 | -2.0% | -0.3 | +5.6 | -4.1 | - | OPEN | LOSS (open) |
| KRE | long | 77.92 | 75.15 | 5 | -3.5% | -1.9 | +0.2 | -5.1 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 241.15 | 3 | +4.4% | +4.9 | +5.5 | -0.4 | - | OPEN | WIN (open) |
| PFE | long | 24.86 | 25.01 | 3 | +0.6% | +1.1 | +1.3 | -0.8 | - | OPEN | WIN (open) |
| AMT | long | 167.03 | 164.65 | 3 | -1.4% | -0.9 | +1.6 | -2.4 | STOP | STOPPED | LOSS |
| ECVT | long | 12.35 | 12.89 | 2 | +4.4% | +5.7 | +7.5 | -1.6 | - | OPEN | WIN (open) |
| GS | long | 1078.0 | 1074.72 | 2 | -0.3% | +1.1 | +2.7 | -1.4 | - | OPEN | AVOID VALIDATED |
| CEG | long | 253.73 | 275.6 | 2 | +8.6% | +10.0 | +9.6 | +0.8 | TARGET | TARGET HIT | AVOID WRONG (it ran) |
| GDX | long | 76.5 | 75.02 | 1 | -1.9% | -0.7 | +1.9 | -3.5 | - | OPEN | AVOID VALIDATED |
| DPZ | long | 319.83 | 323.25 | 1 | +1.1% | +2.3 | +3.7 | -1.3 | - | OPEN | WIN (open) |

## Scorecard

- Total calls logged: 10
- Directional (non-avoid): 7  |  matured/resolved: 1
- Win rate (resolved): 0/1 = 0%
- Mean return (resolved): -1.42%
- Mean excess vs SPY (resolved): -0.89%
- Avoids validated so far: 2/3 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
