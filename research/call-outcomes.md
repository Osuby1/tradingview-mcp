# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-07-28.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DVN | long | 45.11 | 42.66 | 2 | -5.4% | -5.7 | +1.4 | -6.0 | STOP | STOPPED | LOSS |
| HAS | long | 88.17 | 96.34 | 2 | +9.3% | +9.0 | +9.4 | -1.0 | TARGET | TARGET HIT | WIN |
| SJM | long | 117.21 | 123.04 | 2 | +5.0% | +4.7 | +7.0 | -1.1 | - | OPEN | WIN (open) |
| MLI | long | 63.53 | 66.49 | 2 | +4.7% | +4.4 | +5.2 | -1.2 | - | OPEN | WIN (open) |
| SMH | short | 568.92 | 529.6 | 8 | +6.9% | +8.2 | +8.9 | -4.1 | - | OPEN | WIN (open) |
| KRE | long | 77.92 | 76.79 | 8 | -1.4% | -0.1 | +0.2 | -5.1 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 265.62 | 6 | +15.0% | +15.2 | +16.2 | -0.4 | TARGET | TARGET HIT | WIN |
| PFE | long | 24.86 | 25.25 | 6 | +1.6% | +1.7 | +2.6 | -2.5 | - | OPEN | WIN (open) |
| AMT | long | 167.03 | 171.5 | 6 | +2.7% | +2.9 | +6.9 | -2.4 | STOP | STOPPED | WIN |
| ECVT | long | 12.35 | 12.32 | 5 | -0.2% | +0.8 | +7.5 | -1.7 | - | OPEN | LOSS (open) |
| GS | long | 1078.0 | 1033.34 | 5 | -4.1% | -3.1 | +2.7 | -6.1 | STOP | STOPPED | AVOID VALIDATED |
| CEG | long | 253.73 | 259.82 | 5 | +2.4% | +3.4 | +10.2 | +0.8 | TARGET | TARGET HIT | AVOID QUESTIONABLE |
| GDX | long | 76.5 | 74.21 | 4 | -3.0% | -2.1 | +1.9 | -4.1 | - | OPEN | AVOID VALIDATED |
| DPZ | long | 319.83 | 350.47 | 4 | +9.6% | +10.5 | +12.5 | -1.3 | - | OPEN | WIN (open) |
| SPY | short (hedge) - DECLINED | 737.6 | 740.86 | 1 | -0.4% | -0.7 | +0.2 | -1.1 | - | OPEN | LOSS (open) |
| JNJ | long | 265.95 | - | - | - | - | - | - | - | TOO NEW | - |
| DGX | long | 231.84 | - | - | - | - | - | - | - | TOO NEW | - |

## Scorecard

- Total calls logged: 17
- Directional (non-avoid): 12  |  matured/resolved: 4
- Win rate (resolved): 3/4 = 75%
- Mean return (resolved): +5.38%
- Mean excess vs SPY (resolved): +5.33%
- Avoids validated so far: 2/3 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
