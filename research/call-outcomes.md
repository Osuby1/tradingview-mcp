# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-08-06.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| JNJ | long | 265.53 | 256.98 | 6 | -3.2% | -8.6 | +1.4 | -5.7 | STOP | STOPPED | LOSS |
| DGX | long | 235.22 | 238.5 | 6 | +1.4% | -4.0 | +1.5 | -2.6 | - | OPEN | WIN (open) |
| DVN | long | 45.11 | 43.11 | 9 | -4.4% | -8.4 | +1.4 | -6.8 | STOP | STOPPED | LOSS |
| HAS | long | 88.17 | 91.69 | 9 | +4.0% | -0.0 | +10.0 | -1.0 | TARGET | TARGET HIT | WIN |
| SJM | long | 117.21 | 118.8 | 9 | +1.4% | -2.6 | +8.9 | -1.3 | TARGET | TARGET HIT | WIN |
| MLI | long | 63.53 | 69.46 | 9 | +9.3% | +5.3 | +11.9 | -1.2 | TARGET | TARGET HIT | WIN |
| SMH | short | 568.92 | 571.48 | 15 | -0.5% | -2.8 | +11.5 | -4.1 | - | OPEN | LOSS (open) |
| KRE | long | 77.92 | 76.49 | 15 | -1.8% | -4.2 | +0.6 | -5.1 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 272.0 | 13 | +17.8% | +14.2 | +21.3 | -0.4 | TARGET | TARGET HIT | WIN |
| PFE | long | 24.86 | 26.2 | 13 | +5.4% | +1.8 | +5.4 | -2.5 | - | OPEN | WIN (open) |
| AMT | long | 167.03 | 171.2 | 13 | +2.5% | -1.1 | +8.0 | -2.7 | STOP | STOPPED | WIN |
| ECVT | long | 12.35 | 11.0 | 12 | -10.9% | -13.6 | +7.5 | -12.0 | STOP | STOPPED | LOSS |
| GS | long | 1078.0 | 1032.58 | 12 | -4.2% | -6.9 | +2.7 | -9.3 | STOP | STOPPED | AVOID VALIDATED |
| CEG | long | 253.73 | 261.1 | 12 | +2.9% | +0.2 | +10.3 | +0.8 | TARGET | TARGET HIT | AVOID QUESTIONABLE |
| GDX | long | 76.5 | 83.92 | 11 | +9.7% | +6.9 | +10.4 | -5.7 | - | OPEN | AVOID WRONG (it ran) |
| DPZ | long | 319.83 | 358.43 | 11 | +12.1% | +9.2 | +16.4 | -1.3 | - | OPEN | WIN (open) |
| SPY | short (hedge) - DECLINED | 737.6 | 768.56 | 8 | -4.2% | -8.2 | +1.1 | -5.3 | - | OPEN | LOSS (open) |
| JNJ | long | 265.95 | 256.98 | 7 | -3.4% | -7.1 | +3.4 | -5.8 | - | OPEN | LOSS (open) |
| DGX | long | 231.84 | 238.5 | 7 | +2.9% | -0.9 | +3.6 | -1.2 | - | OPEN | WIN (open) |
| SPY | long-put-hedge | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| HQY | long | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| GE | long-call-REAL | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| UAL | long-call-REAL | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| RACE | long-starter | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| SHW | long-starter | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| LUV | long-call-REAL-WORKING | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |

## Scorecard

- Total calls logged: 26
- Directional (non-avoid): 16  |  matured/resolved: 8
- Win rate (resolved): 5/8 = 62%
- Mean return (resolved): +2.04%
- Mean excess vs SPY (resolved): -1.86%
- Avoids validated so far: 1/3 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
