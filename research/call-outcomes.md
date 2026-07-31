# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-07-31.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| JNJ | long | 265.53 | 256.35 | 2 | -3.5% | -5.9 | +1.4 | -4.6 | - | OPEN | LOSS (open) |
| DGX | long | 235.22 | 233.01 | 2 | -0.9% | -3.4 | +1.1 | -2.6 | - | OPEN | LOSS (open) |
| DVN | long | 45.11 | 45.13 | 5 | +0.0% | -1.1 | +1.4 | -6.0 | STOP | STOPPED | WIN |
| HAS | long | 88.17 | 93.94 | 5 | +6.5% | +5.4 | +10.0 | -1.0 | TARGET | TARGET HIT | WIN |
| SJM | long | 117.21 | 119.26 | 5 | +1.8% | +0.7 | +8.9 | -1.1 | TARGET | TARGET HIT | WIN |
| MLI | long | 63.53 | 66.41 | 5 | +4.5% | +3.4 | +7.8 | -1.2 | - | OPEN | WIN (open) |
| SMH | short | 568.92 | 540.53 | 11 | +5.0% | +5.5 | +11.5 | -4.1 | - | OPEN | WIN (open) |
| KRE | long | 77.92 | 76.06 | 11 | -2.4% | -1.9 | +0.2 | -5.1 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 257.29 | 9 | +11.4% | +10.7 | +16.9 | -0.4 | TARGET | TARGET HIT | WIN |
| PFE | long | 24.86 | 25.01 | 9 | +0.6% | -0.1 | +2.6 | -2.5 | - | OPEN | WIN (open) |
| AMT | long | 167.03 | 173.36 | 9 | +3.8% | +3.1 | +8.0 | -2.4 | STOP | STOPPED | WIN |
| ECVT | long | 12.35 | 12.06 | 8 | -2.4% | -2.2 | +7.5 | -4.0 | - | OPEN | LOSS (open) |
| GS | long | 1078.0 | 1018.38 | 8 | -5.5% | -5.4 | +2.7 | -9.3 | STOP | STOPPED | AVOID VALIDATED |
| CEG | long | 253.73 | 262.75 | 8 | +3.5% | +3.7 | +10.2 | +0.8 | TARGET | TARGET HIT | AVOID WRONG (it ran) |
| GDX | long | 76.5 | 74.1 | 7 | -3.1% | -3.1 | +1.9 | -5.7 | - | OPEN | AVOID VALIDATED |
| DPZ | long | 319.83 | 347.44 | 7 | +8.6% | +8.7 | +14.0 | -1.3 | - | OPEN | WIN (open) |
| SPY | short (hedge) - DECLINED | 737.6 | 747.03 | 4 | -1.3% | -2.4 | +1.1 | -1.5 | - | OPEN | LOSS (open) |
| JNJ | long | 265.95 | 256.35 | 3 | -3.6% | -4.4 | +3.4 | -4.8 | - | OPEN | LOSS (open) |
| DGX | long | 231.84 | 233.01 | 3 | +0.5% | -0.3 | +3.6 | -1.2 | - | OPEN | WIN (open) |
| SPY | long-put-hedge | None | - | - | - | - | - | - | - | TOO NEW | - |

## Scorecard

- Total calls logged: 20
- Directional (non-avoid): 16  |  matured/resolved: 5
- Win rate (resolved): 5/5 = 100%
- Mean return (resolved): +4.70%
- Mean excess vs SPY (resolved): +3.77%
- Avoids validated so far: 2/3 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
