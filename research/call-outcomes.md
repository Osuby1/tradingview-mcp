# Call outcome tracker

Graded at each call's REFERENCE price (analysis quality, not fills). Holding window 21 trading days. Price file: call-prices-2026-07-29.json.

| Call | Dir | Ref | Mark | Days | Return | vs SPY | MFE | MAE | Hit | Status | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DVN | long | 45.11 | 44.46 | 3 | -1.4% | -0.2 | +1.4 | -6.0 | STOP | STOPPED | LOSS |
| HAS | long | 88.17 | 95.17 | 3 | +7.9% | +9.2 | +10.0 | -1.0 | TARGET | TARGET HIT | WIN |
| SJM | long | 117.21 | 126.35 | 3 | +7.8% | +9.1 | +8.9 | -1.1 | TARGET | TARGET HIT | WIN |
| MLI | long | 63.53 | 65.4 | 3 | +2.9% | +4.2 | +5.2 | -1.2 | - | OPEN | WIN (open) |
| SMH | short | 568.92 | 504.22 | 9 | +11.4% | +14.2 | +11.5 | -4.1 | - | OPEN | WIN (open) |
| KRE | long | 77.92 | 76.18 | 9 | -2.2% | +0.6 | +0.2 | -5.1 | - | OPEN | LOSS (open) |
| NUE | long | 231.0 | 256.02 | 7 | +10.8% | +12.5 | +16.9 | -0.4 | TARGET | TARGET HIT | WIN |
| PFE | long | 24.86 | 25.15 | 7 | +1.2% | +2.9 | +2.6 | -2.5 | - | OPEN | WIN (open) |
| AMT | long | 167.03 | 179.26 | 7 | +7.3% | +9.0 | +8.0 | -2.4 | STOP | STOPPED | WIN |
| ECVT | long | 12.35 | 12.03 | 6 | -2.6% | -0.1 | +7.5 | -3.2 | - | OPEN | LOSS (open) |
| GS | long | 1078.0 | 980.75 | 6 | -9.0% | -6.5 | +2.7 | -9.3 | STOP | STOPPED | AVOID VALIDATED |
| CEG | long | 253.73 | 257.95 | 6 | +1.7% | +4.2 | +10.2 | +0.8 | TARGET | TARGET HIT | AVOID QUESTIONABLE |
| GDX | long | 76.5 | 73.57 | 5 | -3.8% | -1.4 | +1.9 | -5.7 | - | OPEN | AVOID VALIDATED |
| DPZ | long | 319.83 | 360.0 | 5 | +12.6% | +15.0 | +14.0 | -1.3 | - | OPEN | WIN (open) |
| SPY | short (hedge) - DECLINED | 737.6 | 729.46 | 2 | +1.1% | +2.4 | +1.1 | -1.1 | - | OPEN | WIN (open) |
| JNJ | long | 265.95 | 265.53 | 1 | -0.2% | +1.4 | +3.4 | -0.4 | - | OPEN | LOSS (open) |
| DGX | long | 231.84 | 235.22 | 1 | +1.5% | +3.0 | +3.6 | +0.5 | - | OPEN | WIN (open) |

## Scorecard

- Total calls logged: 17
- Directional (non-avoid): 14  |  matured/resolved: 5
- Win rate (resolved): 4/5 = 80%
- Mean return (resolved): +6.49%
- Mean excess vs SPY (resolved): +7.94%
- Avoids validated so far: 2/3 (would-be trade went nowhere/down)

Open marks are NOT results - they are current unrealized reads that will move. The point of this file is that the calls are now tracked and will be graded automatically as each window closes.
