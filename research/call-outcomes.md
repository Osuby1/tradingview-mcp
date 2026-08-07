# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-08-07.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| JNJ | long | 265.53 | 259.24 | 7 | -2.4% | -8.4 | +1.4 | -5.7 | STOP | STOPPED | LOSS |
| DGX | long | 235.22 | 238.35 | 7 | +1.3% | -4.7 | +1.8 | -2.6 | - | OPEN | WIN (open) |
| DVN | long | 45.11 | 42.98 | 10 | -4.7% | -9.4 | +1.4 | -6.8 | STOP | STOPPED | LOSS |
| HAS | long | 88.17 | 93.52 | 10 | +6.1% | +1.4 | +10.0 | -1.0 | TARGET | TARGET HIT | WIN |
| SJM | long | 117.21 | 120.16 | 10 | +2.5% | -2.1 | +8.9 | -1.3 | TARGET | TARGET HIT | WIN |
| MLI | long | 63.53 | 68.85 | 10 | +8.4% | +3.7 | +11.9 | -1.2 | TARGET | TARGET HIT | WIN |
| SMH | short | 568.92 | 582.7 | 16 | -2.4% | -5.4 | +11.5 | -4.1 | - | OPEN | LOSS (open) |
| KRE | long | 77.92 | 76.21 | 16 | -2.2% | -5.2 | +0.6 | -5.1 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 272.63 | 14 | +18.0% | +13.8 | +21.3 | -0.4 | TARGET | TARGET HIT | WIN |
| PFE | long | 24.86 | 26.76 | 14 | +7.6% | +3.4 | +7.6 | -2.5 | - | OPEN | WIN (open) |
| AMT | long | 167.03 | 172.54 | 14 | +3.3% | -0.9 | +8.0 | -2.7 | STOP | STOPPED | WIN |
| ECVT | long | 12.35 | 10.38 | 13 | -15.9% | -19.3 | +7.5 | -16.5 | STOP | STOPPED | LOSS |
| GS | long | 1078.0 | 1039.61 | 13 | -3.6% | -6.9 | +2.7 | -9.3 | STOP | STOPPED | AVOID VALIDATED |
| CEG | long | 253.73 | 269.89 | 13 | +6.4% | +3.0 | +10.3 | +0.8 | TARGET | TARGET HIT | AVOID WRONG (it ran) |
| GDX | long | 76.5 | 89.89 | 12 | +17.5% | +14.0 | +18.4 | -5.7 | TARGET | TARGET HIT | AVOID WRONG (it ran) |
| DPZ | long | 319.83 | 350.95 | 12 | +9.7% | +6.3 | +16.4 | -1.3 | - | OPEN | WIN (open) |
| SPY | short (hedge) - DECLINED | 737.6 | 773.26 | 9 | -4.8% | -9.4 | +1.1 | -5.3 | - | OPEN | LOSS (open) |
| JNJ | long | 265.95 | 259.24 | 8 | -2.5% | -6.9 | +3.4 | -5.8 | - | OPEN | LOSS (open) |
| DGX | long | 231.84 | 238.35 | 8 | +2.8% | -1.6 | +3.6 | -1.2 | - | OPEN | WIN (open) |
| SPY | long-put-hedge | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| HQY | long | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| GE | long-call-REAL | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| UAL | long-call-REAL | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| RACE | long-starter | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| SHW | long-starter | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| LUV | long-call-REAL-WORKING | None | - | - | - | - | - | - | - | NOT GRADEABLE | - |
| IOVA | long-call-REAL | None | - | - | - | - | - | - | - | TOO NEW | - |
| PLTR | long-call-REAL | None | - | - | - | - | - | - | - | TOO NEW | - |
| GDX | long-call-REAL | None | - | - | - | - | - | - | - | TOO NEW | - |
| INDI | long-call-NOFILL | None | - | - | - | - | - | - | - | TOO NEW | - |

## Scorecard

- Total calls logged: 30
- Directional (non-avoid): 16  |  matured/resolved: 8
- Win rate (resolved): 5/8 = 62%
- Mean return (resolved): +1.91%
- Mean excess vs SPY (resolved): -2.64%
- Avoids validated so far: 1/3 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
