# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-07-22.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SMH | short | 568.92 | 586.91 | 4 | -3.2% | -2.7 | +5.6 | -4.1 | - | OPEN | LOSS (open) |
| KRE | long | 77.92 | 75.6 | 4 | -3.0% | -2.5 | +0.2 | -3.8 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 235.9 | 2 | +2.1% | +1.4 | +3.5 | -0.4 | - | OPEN | WIN (open) |
| PFE | long | 24.86 | 24.82 | 2 | -0.2% | -0.9 | +1.3 | -0.9 | - | OPEN | LOSS (open) |
| AMT | long | 167.03 | 166.06 | 2 | -0.6% | -1.3 | +1.6 | -2.4 | STOP | STOPPED | LOSS |
| ECVT | long | 12.35 | 12.94 | 1 | +4.8% | +4.9 | +6.5 | -1.6 | - | OPEN | WIN (open) |
| GS | long | 1078.0 | 1098.2 | 1 | +1.9% | +2.0 | +2.7 | -1.4 | - | OPEN | AVOID QUESTIONABLE |
| CEG | long | 253.73 | 274.9 | 1 | +8.3% | +8.5 | +8.6 | +0.8 | TARGET | TARGET HIT | AVOID WRONG (it ran) |
| GDX | long | 76.5 | - | - | - | - | - | - | - | TOO NEW | - |

## Scorecard

- Total calls logged: 9
- Directional (non-avoid): 6  |  matured/resolved: 1
- Win rate (resolved): 0/1 = 0%
- Mean return (resolved): -0.58%
- Mean excess vs SPY (resolved): -1.30%
- Avoids validated so far: 0/2 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
