# Gate stack forward grade

Does THE GATE STACK earn its keep? Every fresh Chandelier signal is graded forward from the CLOSE of its signal date over 21 trading sessions, bucketed by what the stack decided. The number that matters is the SPREAD.

- Signal events found: 672  |  priced: 592  |  unique symbol-cohort pairs (headline sample): 249
- Skipped (pre-2026-07-22 hand-written verdicts, not machine-comparable): 20

## Headline - all signals, deduped to first appearance

| Cohort | n | Win% | Mean | Median | Mean vs SPY | Mean worst drawdown |
|---|---|---|---|---|---|---|
| PASSED | 51 | 45% | +0.20% | -0.74% | -1.98% | -5.03% |
| BLOCKED | 198 | 52% | +0.19% | +0.17% | -1.74% | -5.79% |

**Spread (PASSED minus BLOCKED): +0.01 percentage points.**

NO VERDICT YET - not one gated signal has completed a full 21-session window. Everything above is an open mark, not a result. Do not quote the spread as evidence in either direction.

## Matured only (full window closed) - the only honest read

| Cohort | n | Win% | Mean | Median | Mean vs SPY |
|---|---|---|---|---|---|
| PASSED | 0 | - | - | - | - |
| BLOCKED | 0 | - | - | - | - |

## Blocked names by the gate that fired first

Added 2026-07-26 with the volatility-cap re-justification. Gates run in order, so each bucket contains names that PASSED every earlier gate. The VOLATILITY CAP row is the one on probation: its old 2:1 rationale died with the profit target, it blocked SOXL before +539%, and it keeps its job only if this table keeps saying its blocks were worth blocking.

| First-failing gate | n | Win% | Mean | Median | Mean vs SPY |
|---|---|---|---|---|---|
| ADX FLOOR | 60 | 52% | +0.57% | +0.17% | -1.38% |
| ATR GEOMETRY | 12 | 50% | -0.18% | +0.16% | -2.38% |
| DIRECTION | 15 | 33% | -2.79% | -1.95% | -4.40% |
| LIQUIDITY | 1 | 0% | -5.36% | -5.36% | -6.74% |
| OTHER | 30 | 43% | -0.83% | -0.47% | -2.45% |
| REGIME | 22 | 59% | +0.96% | +2.12% | -1.31% |
| VOLATILITY CAP (ex 2:1) | 6 | 33% | +0.06% | -2.12% | -1.93% |
| ZLSMA | 52 | 62% | +1.09% | +1.90% | -0.90% |

## Shadow cohorts - the forbidden retro-tune, run forward instead

Would lowering the ADX floor to 18, or softening DEEP-FAIL, have helped? The replay's missed monsters make that tempting; answering it by re-running history is curve-fitting. These cohorts answer it FORWARD: sole-failure near-misses graded nightly against the PASSED cohort. Promotion bar (pre-registered): >=30 MATURED signals AND mean above PASSED's - then it goes to a Friday review, not before.

| Shadow cohort | n | Win% | Mean | Median | Mean vs SPY | PASSED mean (ref) |
|---|---|---|---|---|---|---|
| ADX 18-20, all else passed | 7 | 43% | -1.20% | -0.23% | -3.30% | +0.20% |
| DEEP-FAIL, all else passed | 2 | 50% | +2.20% | +2.20% | -0.33% | +0.20% |

## Every graded signal

| Date | Sym | Cohort | Regime | Entry | Mark | Days | Return | vs SPY | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | BG | BLOCKED | n/a | 120.49 | 105.4 | 10 | -12.5% | -14.6 | OPEN |
| 2026-07-20 | CHRD | BLOCKED | n/a | 128.8 | 139.33 | 10 | +8.2% | +6.1 | OPEN |
| 2026-07-20 | CNOB | BLOCKED | n/a | 33.46 | 33.47 | 10 | +0.0% | -2.1 | OPEN |
| 2026-07-20 | COCO | BLOCKED | PASS | 73.87 | 63.39 | 10 | -14.2% | -16.3 | OPEN |
| 2026-07-20 | CVNA | BLOCKED | DEEP-FAIL | 64.14 | 66.13 | 10 | +3.1% | +1.0 | OPEN |
| 2026-07-20 | FLG | BLOCKED | n/a | 14.84 | 14.22 | 10 | -4.2% | -6.3 | OPEN |
| 2026-07-20 | FNB | BLOCKED | n/a | 18.75 | 19.19 | 10 | +2.4% | +0.2 | OPEN |
| 2026-07-20 | HAS | BLOCKED | REPAIR | 81.59 | 91.47 | 10 | +12.1% | +10.0 | OPEN |
| 2026-07-20 | HLX | BLOCKED | n/a | 9.43 | 9.26 | 10 | -1.8% | -3.9 | OPEN |
| 2026-07-20 | LCID | BLOCKED | n/a | 7.11 | 7.7 | 10 | +8.3% | +6.2 | OPEN |
| 2026-07-20 | M | BLOCKED | REPAIR | 23.31 | 25.95 | 10 | +11.3% | +9.2 | OPEN |
| 2026-07-20 | NOV | BLOCKED | REPAIR | 19.55 | 19.48 | 10 | -0.4% | -2.5 | OPEN |
| 2026-07-20 | ODFL | BLOCKED | PASS | 231.76 | 211.52 | 10 | -8.7% | -10.8 | OPEN |
| 2026-07-20 | RYZ | BLOCKED | n/a | 29.07 | 28.11 | 10 | -3.3% | -5.4 | OPEN |
| 2026-07-20 | SHAK | BLOCKED | DEEP-FAIL | 56.97 | 64.78 | 10 | +13.7% | +11.6 | OPEN |
| 2026-07-20 | SPG | BLOCKED | PASS | 228.19 | 229.16 | 10 | +0.4% | -1.7 | OPEN |
| 2026-07-20 | TRNS | BLOCKED | n/a | 86.09 | 89.58 | 10 | +4.0% | +1.9 | OPEN |
| 2026-07-20 | VVV | BLOCKED | PASS | 39.54 | 38.79 | 10 | -1.9% | -4.0 | OPEN |
| 2026-07-20 | VZ | BLOCKED | REPAIR | 43.5 | 47.36 | 10 | +8.9% | +6.8 | OPEN |
| 2026-07-20 | WPC | BLOCKED | REPAIR | 75.17 | 72.91 | 10 | -3.0% | -5.1 | OPEN |
| 2026-07-21 | ALKS | BLOCKED | TAPE OK | 52.85 | 49.53 | 9 | -6.3% | -7.5 | OPEN |
| 2026-07-21 | ATLC | BLOCKED | TAPE OK | 96.37 | 108.06 | 9 | +12.1% | +10.9 | OPEN |
| 2026-07-21 | BRKR | BLOCKED | TAPE OK | 60.43 | 64.31 | 9 | +6.4% | +5.2 | OPEN |
| 2026-07-21 | CB | BLOCKED | TAPE OK | 354.8 | 348.23 | 9 | -1.9% | -3.1 | OPEN |
| 2026-07-21 | CBL | BLOCKED | TAPE OK | 55.53 | 58.46 | 9 | +5.3% | +4.0 | OPEN |
| 2026-07-21 | CNOB | BLOCKED | TAPE OK | 33.41 | 33.47 | 9 | +0.2% | -1.1 | OPEN |
| 2026-07-21 | COCO | BLOCKED | TAPE OK | 75.89 | 63.39 | 9 | -16.5% | -17.7 | OPEN |
| 2026-07-21 | CTRE | BLOCKED | TAPE OK | 43.4 | 41.22 | 9 | -5.0% | -6.3 | OPEN |
| 2026-07-21 | ESQ | BLOCKED | TAPE OK | 122.83 | 129.05 | 9 | +5.1% | +3.8 | OPEN |
| 2026-07-21 | EXTR | BLOCKED | TAPE OK | 30.44 | 29.98 | 9 | -1.5% | -2.8 | OPEN |
| 2026-07-21 | FFIV | BLOCKED | TAPE OK | 408.74 | 406.35 | 9 | -0.6% | -1.8 | OPEN |
| 2026-07-21 | FRT | BLOCKED | TAPE OK | 125.59 | 123.65 | 9 | -1.5% | -2.8 | OPEN |
| 2026-07-21 | HCSG | BLOCKED | TAPE OK | 24.8 | 23.41 | 9 | -5.6% | -6.9 | OPEN |
| 2026-07-21 | HELE | BLOCKED | TAPE OK | 27.28 | 29.03 | 9 | +6.4% | +5.2 | OPEN |
| 2026-07-21 | HOMB | BLOCKED | TAPE OK | 30.42 | 31.28 | 9 | +2.8% | +1.6 | OPEN |
| 2026-07-21 | LQDA | BLOCKED | TAPE OK | 80.89 | 83.85 | 9 | +3.7% | +2.4 | OPEN |
| 2026-07-21 | NVRI | BLOCKED | TAPE OK | 21.87 | 23.15 | 9 | +5.8% | +4.6 | OPEN |
| 2026-07-21 | NWPX | BLOCKED | TAPE OK | 135.41 | 127.43 | 9 | -5.9% | -7.2 | OPEN |
| 2026-07-21 | OSCR | BLOCKED | TAPE OK | 30.77 | 30.74 | 9 | -0.1% | -1.4 | OPEN |
| 2026-07-21 | PNC | BLOCKED | TAPE OK | 250.38 | 251.72 | 9 | +0.5% | -0.7 | OPEN |
| 2026-07-21 | SION | BLOCKED | TAPE OK | 47.21 | 49.26 | 9 | +4.3% | +3.1 | OPEN |
| 2026-07-21 | TBLA | BLOCKED | TAPE OK | 5.11 | 5.19 | 9 | +1.6% | +0.3 | OPEN |
| 2026-07-21 | TFIN | BLOCKED | TAPE OK | 79.19 | 76.63 | 9 | -3.2% | -4.5 | OPEN |
| 2026-07-21 | TGTX | BLOCKED | TAPE OK | 53.95 | 46.17 | 9 | -14.4% | -15.7 | OPEN |
| 2026-07-21 | TVTX | BLOCKED | TAPE OK | 56.58 | 54.98 | 9 | -2.8% | -4.1 | OPEN |
| 2026-07-21 | VCYT | BLOCKED | TAPE OK | 59.53 | 44.85 | 9 | -24.7% | -25.9 | OPEN |
| 2026-07-21 | ZD | BLOCKED | TAPE OK | 52.39 | 54.01 | 9 | +3.1% | +1.8 | OPEN |
| 2026-07-21 | CYRX | PASSED | TAPE OK | 16.24 | 15.49 | 9 | -4.6% | -5.9 | OPEN |
| 2026-07-21 | FLEX | PASSED | TAPE OK | 127.39 | 117.45 | 9 | -7.8% | -9.1 | OPEN |
| 2026-07-21 | GDX | PASSED | TAPE OK | 74.19 | 76.05 | 9 | +2.5% | +1.2 | OPEN |
| 2026-07-21 | HON | PASSED | TAPE OK | 229.86 | 246.77 | 9 | +7.4% | +6.1 | OPEN |
| 2026-07-21 | KWEB | PASSED | TAPE OK | 27.02 | 28.74 | 9 | +6.4% | +5.1 | OPEN |
| 2026-07-21 | MSFT | PASSED | TAPE OK | 397.75 | 487.65 | 9 | +22.6% | +21.4 | OPEN |
| 2026-07-21 | MU | PASSED | TAPE OK | 970.82 | 829.5 | 9 | -14.6% | -15.8 | OPEN |
| 2026-07-21 | NKE | PASSED | TAPE OK | 42.96 | 42.64 | 9 | -0.7% | -2.0 | OPEN |
| 2026-07-21 | PM | PASSED | TAPE OK | 188.04 | 187.41 | 9 | -0.3% | -1.6 | OPEN |
| 2026-07-21 | SKYY | PASSED | TAPE OK | 136.02 | 147.98 | 9 | +8.8% | +7.5 | OPEN |
| 2026-07-21 | SNOW | PASSED | TAPE OK | 271.73 | 307.53 | 9 | +13.2% | +11.9 | OPEN |
| 2026-07-22 | ACTG | BLOCKED | REPAIR | 4.57 | 4.63 | 8 | +1.3% | -0.1 | OPEN |
| 2026-07-22 | AMCR | BLOCKED | PASS | 43.21 | 46.02 | 8 | +6.5% | +5.1 | OPEN |
| 2026-07-22 | AMGN | BLOCKED | PASS | 366.05 | 378.87 | 8 | +3.5% | +2.1 | OPEN |
| 2026-07-22 | ASB | BLOCKED | PASS | 30.7 | 31.4 | 8 | +2.3% | +0.9 | OPEN |
| 2026-07-22 | BCBP | BLOCKED | REPAIR | 10.29 | 9.79 | 8 | -4.9% | -6.2 | OPEN |
| 2026-07-22 | BHP | BLOCKED | REPAIR | 84.54 | 83.5 | 8 | -1.2% | -2.6 | OPEN |
| 2026-07-22 | BHRB | BLOCKED | PASS | 71.01 | 73.65 | 8 | +3.7% | +2.4 | OPEN |
| 2026-07-22 | BX | BLOCKED | REPAIR | 122.82 | 134.68 | 8 | +9.7% | +8.3 | OPEN |
| 2026-07-22 | BY | BLOCKED | PASS | 37.75 | 39.78 | 8 | +5.4% | +4.0 | OPEN |
| 2026-07-22 | CBSH | BLOCKED | PASS | 58.7 | 59.67 | 8 | +1.6% | +0.3 | OPEN |
| 2026-07-22 | CCJ | BLOCKED | DEEP-FAIL | 90.37 | 89.72 | 8 | -0.7% | -2.1 | OPEN |
| 2026-07-22 | CMP | BLOCKED | REPAIR | 30.14 | 28.76 | 8 | -4.6% | -6.0 | OPEN |
| 2026-07-22 | CNOB | BLOCKED | PASS | 33.0 | 33.47 | 8 | +1.4% | +0.1 | OPEN |
| 2026-07-22 | COKE | BLOCKED | PASS | 184.36 | 180.76 | 8 | -1.9% | -3.3 | OPEN |
| 2026-07-22 | COLB | BLOCKED | PASS | 32.63 | 31.5 | 8 | -3.5% | -4.8 | OPEN |
| 2026-07-22 | COST | BLOCKED | REPAIR | 927.31 | 954.08 | 8 | +2.9% | +1.5 | OPEN |
| 2026-07-22 | CRCL | BLOCKED | DEEP-FAIL | 66.16 | 60.35 | 8 | -8.8% | -10.2 | OPEN |
| 2026-07-22 | DE | BLOCKED | PASS | 607.33 | 605.06 | 8 | -0.4% | -1.8 | OPEN |
| 2026-07-22 | DELL | BLOCKED | PASS | 441.8 | 429.02 | 8 | -2.9% | -4.3 | OPEN |
| 2026-07-22 | DIS | BLOCKED | REPAIR | 95.87 | 98.14 | 8 | +2.4% | +1.0 | OPEN |
| 2026-07-22 | EQR | BLOCKED | PASS | 68.29 | 67.57 | 8 | -1.1% | -2.4 | OPEN |
| 2026-07-22 | F | BLOCKED | PASS | 14.42 | 14.43 | 8 | +0.1% | -1.3 | OPEN |
| 2026-07-22 | FCX | BLOCKED | PASS | 65.0 | 63.64 | 8 | -2.1% | -3.5 | OPEN |
| 2026-07-22 | FHB | BLOCKED | PASS | 28.81 | 28.01 | 8 | -2.8% | -4.2 | OPEN |
| 2026-07-22 | FITB | BLOCKED | PASS | 57.67 | 56.9 | 8 | -1.3% | -2.7 | OPEN |
| 2026-07-22 | FLEX | BLOCKED | REPAIR | 127.0 | 117.45 | 8 | -7.5% | -8.9 | OPEN |
| 2026-07-22 | FLG | BLOCKED | PASS | 14.88 | 14.22 | 8 | -4.4% | -5.8 | OPEN |
| 2026-07-22 | FNB | BLOCKED | PASS | 18.86 | 19.19 | 8 | +1.8% | +0.4 | OPEN |
| 2026-07-22 | FRT | BLOCKED | PASS | 125.05 | 123.65 | 8 | -1.1% | -2.5 | OPEN |
| 2026-07-22 | GBCI | BLOCKED | PASS | 51.17 | 50.49 | 8 | -1.3% | -2.7 | OPEN |
| 2026-07-22 | GDX | BLOCKED | DEEP-FAIL | 76.68 | 76.05 | 8 | -0.8% | -2.2 | OPEN |
| 2026-07-22 | GLD | BLOCKED | REPAIR | 379.12 | 371.71 | 8 | -1.9% | -3.3 | OPEN |
| 2026-07-22 | GM | BLOCKED | PASS | 82.13 | 87.68 | 8 | +6.8% | +5.4 | OPEN |
| 2026-07-22 | HBNC | BLOCKED | PASS | 20.21 | 20.77 | 8 | +2.8% | +1.4 | OPEN |
| 2026-07-22 | HON | BLOCKED | PASS | 232.99 | 246.77 | 8 | +5.9% | +4.5 | OPEN |
| 2026-07-22 | HOPE | BLOCKED | PASS | 13.54 | 14.19 | 8 | +4.8% | +3.4 | OPEN |
| 2026-07-22 | HSIC | BLOCKED | PASS | 84.81 | 86.51 | 8 | +2.0% | +0.6 | OPEN |
| 2026-07-22 | HTZ | BLOCKED | DEEP-FAIL | 1.93 | 1.53 | 8 | -20.7% | -22.1 | OPEN |
| 2026-07-22 | KRE | BLOCKED | PASS | 75.6 | 77.06 | 8 | +1.9% | +0.6 | OPEN |
| 2026-07-22 | LCID | BLOCKED | DEEP-FAIL | 6.78 | 7.7 | 8 | +13.6% | +12.2 | OPEN |
| 2026-07-22 | LZB | BLOCKED | PASS | 39.3 | 41.0 | 8 | +4.3% | +3.0 | OPEN |
| 2026-07-22 | M | BLOCKED | PASS | 24.33 | 25.95 | 8 | +6.7% | +5.3 | OPEN |
| 2026-07-22 | MFA | BLOCKED | REPAIR | 9.29 | 9.16 | 8 | -1.4% | -2.8 | OPEN |
| 2026-07-22 | MU | BLOCKED | PASS | 959.48 | 829.5 | 8 | -13.6% | -14.9 | OPEN |
| 2026-07-22 | NEE | BLOCKED | PASS | 89.41 | 86.55 | 8 | -3.2% | -4.6 | OPEN |
| 2026-07-22 | NEM | BLOCKED | REPAIR | 95.75 | 95.37 | 8 | -0.4% | -1.8 | OPEN |
| 2026-07-22 | OCFC | BLOCKED | PASS | 19.67 | 19.66 | 8 | -0.1% | -1.4 | OPEN |
| 2026-07-22 | PANW | BLOCKED | PASS | 335.28 | 347.13 | 8 | +3.5% | +2.2 | OPEN |
| 2026-07-22 | PB | BLOCKED | PASS | 73.06 | 75.25 | 8 | +3.0% | +1.6 | OPEN |
| 2026-07-22 | PM | BLOCKED | PASS | 194.3 | 187.41 | 8 | -3.5% | -4.9 | OPEN |
| 2026-07-22 | POWL | BLOCKED | REPAIR | 240.68 | 219.72 | 8 | -8.7% | -10.1 | OPEN |
| 2026-07-22 | PRLB | BLOCKED | PASS | 79.73 | 80.25 | 8 | +0.7% | -0.7 | OPEN |
| 2026-07-22 | RACE | BLOCKED | REPAIR | 371.61 | 401.28 | 8 | +8.0% | +6.6 | OPEN |
| 2026-07-22 | RCL | BLOCKED | REPAIR | 285.85 | 324.0 | 8 | +13.3% | +12.0 | OPEN |
| 2026-07-22 | RSPU | BLOCKED | PASS | 81.85 | 78.98 | 8 | -3.5% | -4.9 | OPEN |
| 2026-07-22 | SAIC | BLOCKED | PASS | 115.95 | 120.12 | 8 | +3.6% | +2.2 | OPEN |
| 2026-07-22 | SJM | BLOCKED | PASS | 118.05 | 117.5 | 8 | -0.5% | -1.8 | OPEN |
| 2026-07-22 | SKK | BLOCKED | PASS | 5.22 | 4.94 | 8 | -5.4% | -6.7 | OPEN |
| 2026-07-22 | SMCI | BLOCKED | REPAIR | 30.56 | 28.64 | 8 | -6.3% | -7.7 | OPEN |
| 2026-07-22 | SON | BLOCKED | PASS | 55.15 | 56.42 | 8 | +2.3% | +0.9 | OPEN |
| 2026-07-22 | SPG | BLOCKED | PASS | 226.22 | 229.16 | 8 | +1.3% | -0.1 | OPEN |
| 2026-07-22 | SSB | BLOCKED | PASS | 102.19 | 107.85 | 8 | +5.5% | +4.2 | OPEN |
| 2026-07-22 | STRL | BLOCKED | REPAIR | 719.34 | 611.47 | 8 | -15.0% | -16.4 | OPEN |
| 2026-07-22 | STX | BLOCKED | PASS | 908.1 | 831.06 | 8 | -8.5% | -9.9 | OPEN |
| 2026-07-22 | TDY | BLOCKED | PASS | 650.5 | 670.56 | 8 | +3.1% | +1.7 | OPEN |
| 2026-07-22 | TPL | BLOCKED | PASS | 433.1 | 406.15 | 8 | -6.2% | -7.6 | OPEN |
| 2026-07-22 | TPR | BLOCKED | PASS | 143.73 | 155.63 | 8 | +8.3% | +6.9 | OPEN |
| 2026-07-22 | URA | BLOCKED | DEEP-FAIL | 40.97 | 40.81 | 8 | -0.4% | -1.8 | OPEN |
| 2026-07-22 | USB | BLOCKED | PASS | 64.47 | 63.94 | 8 | -0.8% | -2.2 | OPEN |
| 2026-07-22 | VST | BLOCKED | REPAIR | 166.74 | 155.94 | 8 | -6.5% | -7.8 | OPEN |
| 2026-07-22 | VVV | BLOCKED | PASS | 39.03 | 38.79 | 8 | -0.6% | -2.0 | OPEN |
| 2026-07-22 | CTRE | PASSED | PASS | 42.38 | 41.22 | 8 | -2.7% | -4.1 | OPEN |
| 2026-07-22 | PFE | PASSED | REPAIR | 24.82 | 25.03 | 8 | +0.8% | -0.5 | OPEN |
| 2026-07-22 | TJX | PASSED | REPAIR | 155.41 | 157.5 | 8 | +1.3% | -0.0 | OPEN |
| 2026-07-22 | TXNM | PASSED | REPAIR | 58.3 | 57.6 | 8 | -1.2% | -2.6 | OPEN |
| 2026-07-22 | VZ | PASSED | REPAIR | 44.29 | 47.36 | 8 | +6.9% | +5.6 | OPEN |
| 2026-07-23 | ACTG | BLOCKED | REPAIR | 4.62 | 4.63 | 7 | +0.2% | -2.4 | OPEN |
| 2026-07-23 | ALSN | BLOCKED | PASS | 119.64 | 116.31 | 7 | -2.8% | -5.4 | OPEN |
| 2026-07-23 | AVT | BLOCKED | PASS | 89.92 | 88.88 | 7 | -1.2% | -3.8 | OPEN |
| 2026-07-23 | BUD | BLOCKED | REPAIR | 80.48 | 84.05 | 7 | +4.4% | +1.8 | OPEN |
| 2026-07-23 | COST | BLOCKED | REPAIR | 926.06 | 954.08 | 7 | +3.0% | +0.4 | OPEN |
| 2026-07-23 | CRCL | BLOCKED | DEEP-FAIL | 62.18 | 60.35 | 7 | -2.9% | -5.6 | OPEN |
| 2026-07-23 | DELL | BLOCKED | PASS | 439.34 | 429.02 | 7 | -2.4% | -5.0 | OPEN |
| 2026-07-23 | DGX | BLOCKED | PASS | 227.9 | 231.95 | 7 | +1.8% | -0.9 | OPEN |
| 2026-07-23 | F | BLOCKED | REPAIR | 14.15 | 14.43 | 7 | +2.0% | -0.7 | OPEN |
| 2026-07-23 | FCX | BLOCKED | REPAIR | 63.5 | 63.64 | 7 | +0.2% | -2.4 | OPEN |
| 2026-07-23 | FLG | BLOCKED | PASS | 14.71 | 14.22 | 7 | -3.3% | -6.0 | OPEN |
| 2026-07-23 | FNB | BLOCKED | PASS | 18.87 | 19.19 | 7 | +1.7% | -0.9 | OPEN |
| 2026-07-23 | FUTU | BLOCKED | DEEP-FAIL | 98.96 | 107.04 | 7 | +8.2% | +5.5 | OPEN |
| 2026-07-23 | GDX | BLOCKED | DEEP-FAIL | 75.02 | 76.05 | 7 | +1.4% | -1.3 | OPEN |
| 2026-07-23 | GLD | BLOCKED | REPAIR | 371.52 | 371.71 | 7 | +0.1% | -2.6 | OPEN |
| 2026-07-23 | GM | BLOCKED | PASS | 80.67 | 87.68 | 7 | +8.7% | +6.0 | OPEN |
| 2026-07-23 | HON | BLOCKED | PASS | 246.27 | 246.77 | 7 | +0.2% | -2.4 | OPEN |
| 2026-07-23 | IRM | BLOCKED | REPAIR | 124.55 | 124.08 | 7 | -0.4% | -3.0 | OPEN |
| 2026-07-23 | LCID | BLOCKED | DEEP-FAIL | 6.45 | 7.7 | 7 | +19.4% | +16.7 | OPEN |
| 2026-07-23 | LSTR | BLOCKED | PASS | 207.97 | 176.76 | 7 | -15.0% | -17.6 | OPEN |
| 2026-07-23 | M | BLOCKED | PASS | 23.33 | 25.95 | 7 | +11.2% | +8.6 | OPEN |
| 2026-07-23 | MAC | BLOCKED | PASS | 25.3 | 25.87 | 7 | +2.2% | -0.4 | OPEN |
| 2026-07-23 | NEM | BLOCKED | REPAIR | 94.72 | 95.37 | 7 | +0.7% | -1.9 | OPEN |
| 2026-07-23 | PLD | BLOCKED | PASS | 145.12 | 144.15 | 7 | -0.7% | -3.3 | OPEN |
| 2026-07-23 | PRLB | BLOCKED | PASS | 78.62 | 80.25 | 7 | +2.1% | -0.6 | OPEN |
| 2026-07-23 | RHP | BLOCKED | PASS | 128.89 | 131.71 | 7 | +2.2% | -0.5 | OPEN |
| 2026-07-23 | SMCI | BLOCKED | REPAIR | 31.2 | 28.64 | 7 | -8.2% | -10.8 | OPEN |
| 2026-07-23 | SON | BLOCKED | PASS | 56.32 | 56.42 | 7 | +0.2% | -2.5 | OPEN |
| 2026-07-23 | SPG | BLOCKED | PASS | 225.2 | 229.16 | 7 | +1.8% | -0.9 | OPEN |
| 2026-07-23 | TDY | BLOCKED | PASS | 651.22 | 670.56 | 7 | +3.0% | +0.3 | OPEN |
| 2026-07-23 | URA | BLOCKED | DEEP-FAIL | 41.13 | 40.81 | 7 | -0.8% | -3.4 | OPEN |
| 2026-07-23 | URI | BLOCKED | PASS | 1139.71 | 1115.92 | 7 | -2.1% | -4.7 | OPEN |
| 2026-07-23 | VST | BLOCKED | REPAIR | 168.98 | 155.94 | 7 | -7.7% | -10.4 | OPEN |
| 2026-07-23 | VVV | BLOCKED | PASS | 38.31 | 38.79 | 7 | +1.2% | -1.4 | OPEN |
| 2026-07-23 | ECVT | PASSED | PASS | 12.89 | 12.05 | 7 | -6.5% | -9.2 | OPEN |
| 2026-07-23 | FRT | PASSED | PASS | 124.83 | 123.65 | 7 | -0.9% | -3.6 | OPEN |
| 2026-07-23 | HAS | PASSED | PASS | 87.35 | 91.47 | 7 | +4.7% | +2.1 | OPEN |
| 2026-07-23 | LHX | PASSED | REPAIR | 299.67 | 277.86 | 7 | -7.3% | -9.9 | OPEN |
| 2026-07-23 | MLI | PASSED | REPAIR | 63.13 | 66.55 | 7 | +5.4% | +2.8 | OPEN |
| 2026-07-23 | PFE | PASSED | REPAIR | 25.01 | 25.03 | 7 | +0.1% | -2.6 | OPEN |
| 2026-07-23 | SJM | PASSED | PASS | 115.71 | 117.5 | 7 | +1.6% | -1.1 | OPEN |
| 2026-07-23 | VZ | PASSED | REPAIR | 43.82 | 47.36 | 7 | +8.1% | +5.4 | OPEN |
| 2026-07-24 | ALSN | BLOCKED | PASS | 122.34 | 116.31 | 6 | -4.9% | -7.5 | OPEN |
| 2026-07-24 | AVT | BLOCKED | PASS | 89.42 | 88.88 | 6 | -0.6% | -3.1 | OPEN |
| 2026-07-24 | BUD | BLOCKED | REPAIR | 81.66 | 84.05 | 6 | +2.9% | +0.4 | OPEN |
| 2026-07-24 | CB | BLOCKED | PASS | 359.75 | 348.23 | 6 | -3.2% | -5.7 | OPEN |
| 2026-07-24 | CNP | BLOCKED | PASS | 44.56 | 41.92 | 6 | -5.9% | -8.5 | OPEN |
| 2026-07-24 | COST | BLOCKED | REPAIR | 935.03 | 954.08 | 6 | +2.0% | -0.5 | OPEN |
| 2026-07-24 | CRCL | BLOCKED | DEEP-FAIL | 62.36 | 60.35 | 6 | -3.2% | -5.8 | OPEN |
| 2026-07-24 | DE | BLOCKED | PASS | 628.16 | 605.06 | 6 | -3.7% | -6.2 | OPEN |
| 2026-07-24 | DGX | BLOCKED | PASS | 227.86 | 231.95 | 6 | +1.8% | -0.7 | OPEN |
| 2026-07-24 | DLR | BLOCKED | PASS | 199.08 | 191.22 | 6 | -4.0% | -6.5 | OPEN |
| 2026-07-24 | EGBN | BLOCKED | PASS | 28.44 | 27.86 | 6 | -2.0% | -4.6 | OPEN |
| 2026-07-24 | F | BLOCKED | REPAIR | 14.37 | 14.43 | 6 | +0.4% | -2.1 | OPEN |
| 2026-07-24 | FCX | BLOCKED | REPAIR | 62.6 | 63.64 | 6 | +1.7% | -0.9 | OPEN |
| 2026-07-24 | FUTU | BLOCKED | DEEP-FAIL | 99.36 | 107.04 | 6 | +7.7% | +5.2 | OPEN |
| 2026-07-24 | GDX | BLOCKED | DEEP-FAIL | 75.23 | 76.05 | 6 | +1.1% | -1.4 | OPEN |
| 2026-07-24 | GE | BLOCKED | PASS | 353.73 | 368.93 | 6 | +4.3% | +1.8 | OPEN |
| 2026-07-24 | GLD | BLOCKED | REPAIR | 371.9 | 371.71 | 6 | -0.1% | -2.6 | OPEN |
| 2026-07-24 | GM | BLOCKED | PASS | 82.64 | 87.68 | 6 | +6.1% | +3.6 | OPEN |
| 2026-07-24 | HON | BLOCKED | PASS | 243.15 | 246.77 | 6 | +1.5% | -1.1 | OPEN |
| 2026-07-24 | IRM | BLOCKED | PASS | 128.31 | 124.08 | 6 | -3.3% | -5.8 | OPEN |
| 2026-07-24 | JNJ | BLOCKED | PASS | 263.4 | 254.41 | 6 | -3.4% | -6.0 | OPEN |
| 2026-07-24 | LCID | BLOCKED | DEEP-FAIL | 6.3 | 7.7 | 6 | +22.2% | +19.7 | OPEN |
| 2026-07-24 | LDOS | BLOCKED | DEEP-FAIL | 112.14 | 118.72 | 6 | +5.9% | +3.3 | OPEN |
| 2026-07-24 | LIND | BLOCKED | PASS | 26.85 | 33.12 | 6 | +23.4% | +20.8 | OPEN |
| 2026-07-24 | M | BLOCKED | PASS | 23.38 | 25.95 | 6 | +11.0% | +8.5 | OPEN |
| 2026-07-24 | NEM | BLOCKED | REPAIR | 93.19 | 95.37 | 6 | +2.3% | -0.2 | OPEN |
| 2026-07-24 | ORKA | BLOCKED | PASS | 92.16 | 94.79 | 6 | +2.9% | +0.3 | OPEN |
| 2026-07-24 | PH | BLOCKED | PASS | 987.54 | 997.52 | 6 | +1.0% | -1.5 | OPEN |
| 2026-07-24 | PRLB | BLOCKED | PASS | 78.24 | 80.25 | 6 | +2.6% | +0.0 | OPEN |
| 2026-07-24 | ROP | BLOCKED | REPAIR | 367.34 | 392.57 | 6 | +6.9% | +4.3 | OPEN |
| 2026-07-24 | RSPU | BLOCKED | PASS | 82.33 | 78.98 | 6 | -4.1% | -6.6 | OPEN |
| 2026-07-24 | SMCI | BLOCKED | REPAIR | 30.1 | 28.64 | 6 | -4.8% | -7.4 | OPEN |
| 2026-07-24 | SON | BLOCKED | PASS | 58.23 | 56.42 | 6 | -3.1% | -5.6 | OPEN |
| 2026-07-24 | SPG | BLOCKED | PASS | 229.78 | 229.16 | 6 | -0.3% | -2.8 | OPEN |
| 2026-07-24 | TDY | BLOCKED | PASS | 655.35 | 670.56 | 6 | +2.3% | -0.2 | OPEN |
| 2026-07-24 | URA | BLOCKED | DEEP-FAIL | 39.89 | 40.81 | 6 | +2.3% | -0.2 | OPEN |
| 2026-07-24 | URI | BLOCKED | PASS | 1141.59 | 1115.92 | 6 | -2.2% | -4.8 | OPEN |
| 2026-07-24 | VST | BLOCKED | REPAIR | 163.38 | 155.94 | 6 | -4.5% | -7.1 | OPEN |
| 2026-07-24 | XLI | BLOCKED | PASS | 182.66 | 183.16 | 6 | +0.3% | -2.3 | OPEN |
| 2026-07-24 | ACTG | PASSED | PASS | 4.66 | 4.63 | 6 | -0.6% | -3.2 | OPEN |
| 2026-07-24 | DELL | PASSED | PASS | 437.5 | 429.02 | 6 | -1.9% | -4.5 | OPEN |
| 2026-07-24 | EQIX | PASSED | PASS | 1084.24 | 1031.44 | 6 | -4.9% | -7.4 | OPEN |
| 2026-07-24 | LHX | PASSED | REPAIR | 300.21 | 277.86 | 6 | -7.4% | -10.0 | OPEN |
| 2026-07-24 | MLI | PASSED | REPAIR | 63.91 | 66.55 | 6 | +4.1% | +1.6 | OPEN |
| 2026-07-24 | MRK | PASSED | PASS | 131.07 | 127.77 | 6 | -2.5% | -5.0 | OPEN |
| 2026-07-24 | RHP | PASSED | PASS | 133.09 | 131.71 | 6 | -1.0% | -3.6 | OPEN |
| 2026-07-24 | SJM | PASSED | PASS | 118.32 | 117.5 | 6 | -0.7% | -3.2 | OPEN |
| 2026-07-24 | VZ | PASSED | REPAIR | 46.38 | 47.36 | 6 | +2.1% | -0.4 | OPEN |
| 2026-07-27 | ACGL | BLOCKED | PASS | 103.88 | 101.12 | 5 | -2.7% | -5.2 | OPEN |
| 2026-07-27 | ALSN | BLOCKED | PASS | 121.91 | 116.31 | 5 | -4.6% | -7.1 | OPEN |
| 2026-07-27 | AVT | BLOCKED | PASS | 88.38 | 88.88 | 5 | +0.6% | -1.9 | OPEN |
| 2026-07-27 | BUD | BLOCKED | REPAIR | 80.87 | 84.05 | 5 | +3.9% | +1.4 | OPEN |
| 2026-07-27 | CB | BLOCKED | PASS | 358.91 | 348.23 | 5 | -3.0% | -5.5 | OPEN |
| 2026-07-27 | CPRT | BLOCKED | DEEP-FAIL | 29.79 | 29.35 | 5 | -1.5% | -4.0 | OPEN |
| 2026-07-27 | CRCL | BLOCKED | DEEP-FAIL | 65.67 | 60.35 | 5 | -8.1% | -10.6 | OPEN |
| 2026-07-27 | DE | BLOCKED | PASS | 625.02 | 605.06 | 5 | -3.2% | -5.7 | OPEN |
| 2026-07-27 | DLR | BLOCKED | PASS | 195.76 | 191.22 | 5 | -2.3% | -4.8 | OPEN |
| 2026-07-27 | EGBN | BLOCKED | PASS | 28.15 | 27.86 | 5 | -1.0% | -3.5 | OPEN |
| 2026-07-27 | F | BLOCKED | PASS | 14.68 | 14.43 | 5 | -1.7% | -4.2 | OPEN |
| 2026-07-27 | FCX | BLOCKED | REPAIR | 62.72 | 63.64 | 5 | +1.5% | -1.1 | OPEN |
| 2026-07-27 | FUTU | BLOCKED | DEEP-FAIL | 104.27 | 107.04 | 5 | +2.7% | +0.1 | OPEN |
| 2026-07-27 | GDX | BLOCKED | DEEP-FAIL | 75.73 | 76.05 | 5 | +0.4% | -2.1 | OPEN |
| 2026-07-27 | GLD | BLOCKED | REPAIR | 374.63 | 371.71 | 5 | -0.8% | -3.3 | OPEN |
| 2026-07-27 | GM | BLOCKED | PASS | 87.04 | 87.68 | 5 | +0.7% | -1.8 | OPEN |
| 2026-07-27 | HON | BLOCKED | PASS | 245.75 | 246.77 | 5 | +0.4% | -2.1 | OPEN |
| 2026-07-27 | IRM | BLOCKED | PASS | 126.99 | 124.08 | 5 | -2.3% | -4.8 | OPEN |
| 2026-07-27 | LDOS | BLOCKED | DEEP-FAIL | 114.95 | 118.72 | 5 | +3.3% | +0.8 | OPEN |
| 2026-07-27 | LIND | BLOCKED | PASS | 28.09 | 33.12 | 5 | +17.9% | +15.4 | OPEN |
| 2026-07-27 | MAR | BLOCKED | PASS | 383.06 | 346.83 | 5 | -9.5% | -12.0 | OPEN |
| 2026-07-27 | NEM | BLOCKED | REPAIR | 93.47 | 95.37 | 5 | +2.0% | -0.5 | OPEN |
| 2026-07-27 | ORKA | BLOCKED | PASS | 90.2 | 94.79 | 5 | +5.1% | +2.6 | OPEN |
| 2026-07-27 | PGR | BLOCKED | REPAIR | 215.76 | 210.46 | 5 | -2.5% | -5.0 | OPEN |
| 2026-07-27 | PH | BLOCKED | PASS | 987.31 | 997.52 | 5 | +1.0% | -1.5 | OPEN |
| 2026-07-27 | PRLB | BLOCKED | PASS | 77.64 | 80.25 | 5 | +3.4% | +0.8 | OPEN |
| 2026-07-27 | RCL | BLOCKED | REPAIR | 305.04 | 324.0 | 5 | +6.2% | +3.7 | OPEN |
| 2026-07-27 | ROP | BLOCKED | REPAIR | 375.02 | 392.57 | 5 | +4.7% | +2.2 | OPEN |
| 2026-07-27 | RSPU | BLOCKED | PASS | 81.24 | 78.98 | 5 | -2.8% | -5.3 | OPEN |
| 2026-07-27 | SLB | BLOCKED | PASS | 51.53 | 49.31 | 5 | -4.3% | -6.8 | OPEN |
| 2026-07-27 | SMCI | BLOCKED | DEEP-FAIL | 29.81 | 28.64 | 5 | -3.9% | -6.4 | OPEN |
| 2026-07-27 | SON | BLOCKED | PASS | 58.68 | 56.42 | 5 | -3.9% | -6.4 | OPEN |
| 2026-07-27 | TDY | BLOCKED | PASS | 651.65 | 670.56 | 5 | +2.9% | +0.4 | OPEN |
| 2026-07-27 | TJX | BLOCKED | REPAIR | 156.38 | 157.5 | 5 | +0.7% | -1.8 | OPEN |
| 2026-07-27 | URA | BLOCKED | DEEP-FAIL | 40.32 | 40.81 | 5 | +1.2% | -1.3 | OPEN |
| 2026-07-27 | VRSN | BLOCKED | REPAIR | 274.82 | 298.89 | 5 | +8.8% | +6.2 | OPEN |
| 2026-07-27 | VST | BLOCKED | REPAIR | 157.08 | 155.94 | 5 | -0.7% | -3.2 | OPEN |
| 2026-07-27 | WWD | BLOCKED | PASS | 419.76 | 363.57 | 5 | -13.4% | -15.9 | OPEN |
| 2026-07-27 | XLI | BLOCKED | PASS | 183.2 | 183.16 | 5 | -0.0% | -2.5 | OPEN |
| 2026-07-27 | ACTG | PASSED | PASS | 4.63 | 4.63 | 5 | +0.0% | -2.5 | OPEN |
| 2026-07-27 | DELL | PASSED | PASS | 426.91 | 429.02 | 5 | +0.5% | -2.0 | OPEN |
| 2026-07-27 | DGX | PASSED | PASS | 231.84 | 231.95 | 5 | +0.1% | -2.5 | OPEN |
| 2026-07-27 | EQIX | PASSED | PASS | 1046.79 | 1031.44 | 5 | -1.5% | -4.0 | OPEN |
| 2026-07-27 | GE | PASSED | PASS | 361.61 | 368.93 | 5 | +2.0% | -0.5 | OPEN |
| 2026-07-27 | JNJ | PASSED | PASS | 265.95 | 254.41 | 5 | -4.3% | -6.8 | OPEN |
| 2026-07-27 | LHX | PASSED | REPAIR | 303.48 | 277.86 | 5 | -8.4% | -11.0 | OPEN |
| 2026-07-27 | MLI | PASSED | PASS | 64.17 | 66.55 | 5 | +3.7% | +1.2 | OPEN |
| 2026-07-27 | MRK | PASSED | PASS | 130.76 | 127.77 | 5 | -2.3% | -4.8 | OPEN |
| 2026-07-27 | RHP | PASSED | PASS | 134.94 | 131.71 | 5 | -2.4% | -4.9 | OPEN |
| 2026-07-27 | SJM | PASSED | PASS | 121.05 | 117.5 | 5 | -2.9% | -5.5 | OPEN |
| 2026-07-27 | URI | PASSED | PASS | 1127.91 | 1115.92 | 5 | -1.1% | -3.6 | OPEN |
| 2026-07-28 | ACGL | BLOCKED | PASS | 106.48 | 101.12 | 4 | -5.0% | -7.3 | OPEN |
| 2026-07-28 | AGNC | BLOCKED | PASS | 11.07 | 10.64 | 4 | -3.9% | -6.2 | OPEN |
| 2026-07-28 | AI | BLOCKED | DEEP-FAIL | 8.9 | 9.73 | 4 | +9.3% | +7.1 | OPEN |
| 2026-07-28 | AJG | BLOCKED | REPAIR | 265.31 | 247.79 | 4 | -6.6% | -8.9 | OPEN |
| 2026-07-28 | ALSN | BLOCKED | PASS | 121.11 | 116.31 | 4 | -4.0% | -6.2 | OPEN |
| 2026-07-28 | AVT | BLOCKED | REPAIR | 86.22 | 88.88 | 4 | +3.1% | +0.8 | OPEN |
| 2026-07-28 | AXON | BLOCKED | REPAIR | 547.65 | 575.88 | 4 | +5.2% | +2.9 | OPEN |
| 2026-07-28 | BUD | BLOCKED | PASS | 83.2 | 84.05 | 4 | +1.0% | -1.2 | OPEN |
| 2026-07-28 | CB | BLOCKED | PASS | 363.5 | 348.23 | 4 | -4.2% | -6.5 | OPEN |
| 2026-07-28 | CCL | BLOCKED | REPAIR | 28.23 | 28.74 | 4 | +1.8% | -0.5 | OPEN |
| 2026-07-28 | CHTR | BLOCKED | DEEP-FAIL | 139.97 | 144.1 | 4 | +3.0% | +0.7 | OPEN |
| 2026-07-28 | CLX | BLOCKED | REPAIR | 100.32 | 98.26 | 4 | -2.0% | -4.3 | OPEN |
| 2026-07-28 | CNP | BLOCKED | PASS | 44.1 | 41.92 | 4 | -4.9% | -7.2 | OPEN |
| 2026-07-28 | COKE | BLOCKED | PASS | 195.0 | 180.76 | 4 | -7.3% | -9.6 | OPEN |
| 2026-07-28 | CPRT | BLOCKED | DEEP-FAIL | 30.69 | 29.35 | 4 | -4.4% | -6.6 | OPEN |
| 2026-07-28 | CRCL | BLOCKED | DEEP-FAIL | 64.32 | 60.35 | 4 | -6.2% | -8.4 | OPEN |
| 2026-07-28 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.73 | 4 | +3.8% | +1.5 | OPEN |
| 2026-07-28 | DASH | BLOCKED | REPAIR | 195.52 | 200.5 | 4 | +2.5% | +0.3 | OPEN |
| 2026-07-28 | DUOL | BLOCKED | REPAIR | 140.73 | 135.8 | 4 | -3.5% | -5.8 | OPEN |
| 2026-07-28 | EGBN | BLOCKED | PASS | 28.39 | 27.86 | 4 | -1.9% | -4.1 | OPEN |
| 2026-07-28 | ERIE | BLOCKED | REPAIR | 242.43 | 236.86 | 4 | -2.3% | -4.6 | OPEN |
| 2026-07-28 | F | BLOCKED | PASS | 14.96 | 14.43 | 4 | -3.5% | -5.8 | OPEN |
| 2026-07-28 | FCX | BLOCKED | REPAIR | 61.64 | 63.64 | 4 | +3.2% | +1.0 | OPEN |
| 2026-07-28 | FUTU | BLOCKED | DEEP-FAIL | 101.84 | 107.04 | 4 | +5.1% | +2.8 | OPEN |
| 2026-07-28 | GDX | BLOCKED | DEEP-FAIL | 74.21 | 76.05 | 4 | +2.5% | +0.2 | OPEN |
| 2026-07-28 | GLD | BLOCKED | DEEP-FAIL | 369.37 | 371.71 | 4 | +0.6% | -1.6 | OPEN |
| 2026-07-28 | GM | BLOCKED | PASS | 90.3 | 87.68 | 4 | -2.9% | -5.2 | OPEN |
| 2026-07-28 | HD | BLOCKED | REPAIR | 344.47 | 340.02 | 4 | -1.3% | -3.6 | OPEN |
| 2026-07-28 | JETS | BLOCKED | PASS | 31.86 | 32.67 | 4 | +2.5% | +0.3 | OPEN |
| 2026-07-28 | LDOS | BLOCKED | DEEP-FAIL | 118.36 | 118.72 | 4 | +0.3% | -2.0 | OPEN |
| 2026-07-28 | LOW | BLOCKED | REPAIR | 218.24 | 212.06 | 4 | -2.8% | -5.1 | OPEN |
| 2026-07-28 | LZB | BLOCKED | PASS | 41.3 | 41.0 | 4 | -0.7% | -3.0 | OPEN |
| 2026-07-28 | MAR | BLOCKED | PASS | 383.52 | 346.83 | 4 | -9.6% | -11.8 | OPEN |
| 2026-07-28 | MCD | BLOCKED | REPAIR | 273.02 | 265.23 | 4 | -2.9% | -5.1 | OPEN |
| 2026-07-28 | MDT | BLOCKED | REPAIR | 86.88 | 86.68 | 4 | -0.2% | -2.5 | OPEN |
| 2026-07-28 | NCLH | BLOCKED | REPAIR | 21.22 | 19.76 | 4 | -6.9% | -9.2 | OPEN |
| 2026-07-28 | NEM | BLOCKED | DEEP-FAIL | 91.52 | 95.37 | 4 | +4.2% | +1.9 | OPEN |
| 2026-07-28 | NFLX | BLOCKED | DEEP-FAIL | 72.39 | 73.33 | 4 | +1.3% | -1.0 | OPEN |
| 2026-07-28 | NOW | BLOCKED | DEEP-FAIL | 110.62 | 114.19 | 4 | +3.2% | +1.0 | OPEN |
| 2026-07-28 | PGR | BLOCKED | REPAIR | 219.52 | 210.46 | 4 | -4.1% | -6.4 | OPEN |
| 2026-07-28 | PH | BLOCKED | PASS | 990.96 | 997.52 | 4 | +0.7% | -1.6 | OPEN |
| 2026-07-28 | RACE | BLOCKED | REPAIR | 390.14 | 401.28 | 4 | +2.9% | +0.6 | OPEN |
| 2026-07-28 | RCL | BLOCKED | REPAIR | 322.5 | 324.0 | 4 | +0.5% | -1.8 | OPEN |
| 2026-07-28 | RMD | BLOCKED | DEEP-FAIL | 208.96 | 215.19 | 4 | +3.0% | +0.7 | OPEN |
| 2026-07-28 | ROP | BLOCKED | REPAIR | 390.92 | 392.57 | 4 | +0.4% | -1.9 | OPEN |
| 2026-07-28 | RSPU | BLOCKED | PASS | 81.03 | 78.98 | 4 | -2.5% | -4.8 | OPEN |
| 2026-07-28 | SHAK | BLOCKED | DEEP-FAIL | 63.2 | 64.78 | 4 | +2.5% | +0.2 | OPEN |
| 2026-07-28 | SHW | BLOCKED | REPAIR | 354.27 | 354.22 | 4 | -0.0% | -2.3 | OPEN |
| 2026-07-28 | SMCI | BLOCKED | DEEP-FAIL | 28.45 | 28.64 | 4 | +0.7% | -1.6 | OPEN |
| 2026-07-28 | SON | BLOCKED | PASS | 60.56 | 56.42 | 4 | -6.8% | -9.1 | OPEN |
| 2026-07-28 | STGW | BLOCKED | PASS | 7.97 | 8.7 | 4 | +9.2% | +6.9 | OPEN |
| 2026-07-28 | TDY | BLOCKED | PASS | 649.67 | 670.56 | 4 | +3.2% | +0.9 | OPEN |
| 2026-07-28 | TOST | BLOCKED | REPAIR | 32.34 | 32.79 | 4 | +1.4% | -0.9 | OPEN |
| 2026-07-28 | TPR | BLOCKED | PASS | 150.9 | 155.63 | 4 | +3.1% | +0.9 | OPEN |
| 2026-07-28 | TYL | BLOCKED | DEEP-FAIL | 333.35 | 305.54 | 4 | -8.3% | -10.6 | OPEN |
| 2026-07-28 | URA | BLOCKED | DEEP-FAIL | 38.95 | 40.81 | 4 | +4.8% | +2.5 | OPEN |
| 2026-07-28 | URI | BLOCKED | PASS | 1091.26 | 1115.92 | 4 | +2.3% | -0.0 | OPEN |
| 2026-07-28 | VRSN | BLOCKED | REPAIR | 281.15 | 298.89 | 4 | +6.3% | +4.0 | OPEN |
| 2026-07-28 | WWD | BLOCKED | PASS | 410.55 | 363.57 | 4 | -11.4% | -13.7 | OPEN |
| 2026-07-28 | XLI | BLOCKED | PASS | 182.49 | 183.16 | 4 | +0.4% | -1.9 | OPEN |
| 2026-07-28 | ZTS | BLOCKED | DEEP-FAIL | 77.51 | 77.1 | 4 | -0.5% | -2.8 | OPEN |
| 2026-07-28 | ACTG | PASSED | PASS | 4.63 | 4.63 | 4 | +0.0% | -2.3 | OPEN |
| 2026-07-28 | CTS | PASSED | PASS | 64.82 | 65.23 | 4 | +0.6% | -1.6 | OPEN |
| 2026-07-28 | DAL | PASSED | PASS | 89.37 | 91.59 | 4 | +2.5% | +0.2 | OPEN |
| 2026-07-28 | DE | PASSED | PASS | 639.84 | 605.06 | 4 | -5.4% | -7.7 | OPEN |
| 2026-07-28 | DGX | PASSED | PASS | 235.94 | 231.95 | 4 | -1.7% | -4.0 | OPEN |
| 2026-07-28 | DLR | PASSED | PASS | 193.18 | 191.22 | 4 | -1.0% | -3.3 | OPEN |
| 2026-07-28 | EQIX | PASSED | REPAIR | 1034.86 | 1031.44 | 4 | -0.3% | -2.6 | OPEN |
| 2026-07-28 | GE | PASSED | PASS | 363.59 | 368.93 | 4 | +1.5% | -0.8 | OPEN |
| 2026-07-28 | HON | PASSED | PASS | 247.05 | 246.77 | 4 | -0.1% | -2.4 | OPEN |
| 2026-07-28 | JNJ | PASSED | PASS | 266.73 | 254.41 | 4 | -4.6% | -6.9 | OPEN |
| 2026-07-28 | LHX | PASSED | REPAIR | 305.2 | 277.86 | 4 | -9.0% | -11.2 | OPEN |
| 2026-07-28 | LLY | PASSED | PASS | 1220.66 | 1121.36 | 4 | -8.1% | -10.4 | OPEN |
| 2026-07-28 | MLI | PASSED | PASS | 66.49 | 66.55 | 4 | +0.1% | -2.2 | OPEN |
| 2026-07-28 | MNST | PASSED | PASS | 97.74 | 93.55 | 4 | -4.3% | -6.6 | OPEN |
| 2026-07-28 | MRK | PASSED | PASS | 131.82 | 127.77 | 4 | -3.1% | -5.3 | OPEN |
| 2026-07-28 | PEP | PASSED | REPAIR | 142.86 | 139.63 | 4 | -2.3% | -4.5 | OPEN |
| 2026-07-28 | SLB | PASSED | REPAIR | 49.98 | 49.31 | 4 | -1.3% | -3.6 | OPEN |
| 2026-07-28 | SSD | PASSED | PASS | 198.28 | 192.17 | 4 | -3.1% | -5.3 | OPEN |
| 2026-07-28 | TJX | PASSED | PASS | 160.8 | 157.5 | 4 | -2.0% | -4.3 | OPEN |
| 2026-07-29 | ABNB | BLOCKED | PASS | 153.01 | 150.64 | 3 | -1.6% | -5.4 | OPEN |
| 2026-07-29 | ACGL | BLOCKED | PASS | 104.55 | 101.12 | 3 | -3.3% | -7.2 | OPEN |
| 2026-07-29 | AGNC | BLOCKED | PASS | 10.9 | 10.64 | 3 | -2.4% | -6.2 | OPEN |
| 2026-07-29 | AI | BLOCKED | DEEP-FAIL | 8.85 | 9.73 | 3 | +9.9% | +6.1 | OPEN |
| 2026-07-29 | AJG | BLOCKED | REPAIR | 268.91 | 247.79 | 3 | -7.8% | -11.7 | OPEN |
| 2026-07-29 | AXON | BLOCKED | REPAIR | 531.2 | 575.88 | 3 | +8.4% | +4.5 | OPEN |
| 2026-07-29 | BFC | BLOCKED | PASS | 151.78 | 155.29 | 3 | +2.3% | -1.6 | OPEN |
| 2026-07-29 | CB | BLOCKED | PASS | 361.9 | 348.23 | 3 | -3.8% | -7.6 | OPEN |
| 2026-07-29 | CHTR | BLOCKED | DEEP-FAIL | 145.2 | 144.1 | 3 | -0.8% | -4.6 | OPEN |
| 2026-07-29 | CLX | BLOCKED | REPAIR | 99.63 | 98.26 | 3 | -1.4% | -5.2 | OPEN |
| 2026-07-29 | CMG | BLOCKED | REPAIR | 34.24 | 37.46 | 3 | +9.4% | +5.5 | OPEN |
| 2026-07-29 | CNP | BLOCKED | PASS | 42.93 | 41.92 | 3 | -2.4% | -6.2 | OPEN |
| 2026-07-29 | COKE | BLOCKED | PASS | 192.39 | 180.76 | 3 | -6.0% | -9.9 | OPEN |
| 2026-07-29 | CPRT | BLOCKED | DEEP-FAIL | 30.82 | 29.35 | 3 | -4.8% | -8.6 | OPEN |
| 2026-07-29 | CTM | BLOCKED | DEEP-FAIL | 0.66 | 0.73 | 3 | +10.7% | +6.8 | OPEN |
| 2026-07-29 | DASH | BLOCKED | REPAIR | 193.53 | 200.5 | 3 | +3.6% | -0.3 | OPEN |
| 2026-07-29 | DE | BLOCKED | PASS | 610.95 | 605.06 | 3 | -1.0% | -4.8 | OPEN |
| 2026-07-29 | DUOL | BLOCKED | REPAIR | 140.17 | 135.8 | 3 | -3.1% | -7.0 | OPEN |
| 2026-07-29 | EGBN | BLOCKED | PASS | 27.89 | 27.86 | 3 | -0.1% | -4.0 | OPEN |
| 2026-07-29 | EQIX | BLOCKED | REPAIR | 1008.02 | 1031.44 | 3 | +2.3% | -1.5 | OPEN |
| 2026-07-29 | ERIE | BLOCKED | REPAIR | 248.55 | 236.86 | 3 | -4.7% | -8.6 | OPEN |
| 2026-07-29 | ESQ | BLOCKED | PASS | 131.89 | 129.05 | 3 | -2.1% | -6.0 | OPEN |
| 2026-07-29 | FCX | BLOCKED | REPAIR | 59.99 | 63.64 | 3 | +6.1% | +2.2 | OPEN |
| 2026-07-29 | GDX | BLOCKED | DEEP-FAIL | 73.57 | 76.05 | 3 | +3.4% | -0.5 | OPEN |
| 2026-07-29 | GME | BLOCKED | REPAIR | 21.84 | 19.06 | 3 | -12.7% | -16.6 | OPEN |
| 2026-07-29 | GRND | BLOCKED | PASS | 17.21 | 17.9 | 3 | +4.0% | +0.1 | OPEN |
| 2026-07-29 | HD | BLOCKED | REPAIR | 338.27 | 340.02 | 3 | +0.5% | -3.4 | OPEN |
| 2026-07-29 | IBM | BLOCKED | DEEP-FAIL | 226.44 | 226.31 | 3 | -0.1% | -3.9 | OPEN |
| 2026-07-29 | JBLU | BLOCKED | PASS | 5.72 | 6.23 | 3 | +8.9% | +5.0 | OPEN |
| 2026-07-29 | JETS | BLOCKED | PASS | 30.97 | 32.67 | 3 | +5.5% | +1.6 | OPEN |
| 2026-07-29 | KWEB | BLOCKED | DEEP-FAIL | 27.8 | 28.74 | 3 | +3.4% | -0.5 | OPEN |
| 2026-07-29 | LDOS | BLOCKED | DEEP-FAIL | 114.37 | 118.72 | 3 | +3.8% | -0.1 | OPEN |
| 2026-07-29 | LOW | BLOCKED | REPAIR | 215.68 | 212.06 | 3 | -1.7% | -5.5 | OPEN |
| 2026-07-29 | LZB | BLOCKED | PASS | 40.93 | 41.0 | 3 | +0.2% | -3.7 | OPEN |
| 2026-07-29 | MAR | BLOCKED | PASS | 381.12 | 346.83 | 3 | -9.0% | -12.9 | OPEN |
| 2026-07-29 | MCD | BLOCKED | REPAIR | 271.52 | 265.23 | 3 | -2.3% | -6.2 | OPEN |
| 2026-07-29 | NCLH | BLOCKED | REPAIR | 20.75 | 19.76 | 3 | -4.8% | -8.6 | OPEN |
| 2026-07-29 | NEM | BLOCKED | DEEP-FAIL | 91.34 | 95.37 | 3 | +4.4% | +0.5 | OPEN |
| 2026-07-29 | NEO | BLOCKED | PASS | 15.27 | 15.84 | 3 | +3.7% | -0.1 | OPEN |
| 2026-07-29 | NFLX | BLOCKED | DEEP-FAIL | 73.63 | 73.33 | 3 | -0.4% | -4.3 | OPEN |
| 2026-07-29 | NIO | BLOCKED | DEEP-FAIL | 4.76 | 4.81 | 3 | +1.1% | -2.8 | OPEN |
| 2026-07-29 | NOW | BLOCKED | REPAIR | 115.76 | 114.19 | 3 | -1.4% | -5.2 | OPEN |
| 2026-07-29 | NVST | BLOCKED | PASS | 28.37 | 27.37 | 3 | -3.5% | -7.4 | OPEN |
| 2026-07-29 | PGR | BLOCKED | REPAIR | 219.99 | 210.46 | 3 | -4.3% | -8.2 | OPEN |
| 2026-07-29 | PH | BLOCKED | PASS | 951.07 | 997.52 | 3 | +4.9% | +1.0 | OPEN |
| 2026-07-29 | RCL | BLOCKED | REPAIR | 323.58 | 324.0 | 3 | +0.1% | -3.7 | OPEN |
| 2026-07-29 | RMD | BLOCKED | REPAIR | 214.29 | 215.19 | 3 | +0.4% | -3.5 | OPEN |
| 2026-07-29 | ROKU | BLOCKED | PASS | 145.33 | 145.84 | 3 | +0.3% | -3.5 | OPEN |
| 2026-07-29 | ROP | BLOCKED | REPAIR | 408.07 | 392.57 | 3 | -3.8% | -7.7 | OPEN |
| 2026-07-29 | RSPU | BLOCKED | PASS | 79.85 | 78.98 | 3 | -1.1% | -5.0 | OPEN |
| 2026-07-29 | SHAK | BLOCKED | DEEP-FAIL | 63.05 | 64.78 | 3 | +2.7% | -1.1 | OPEN |
| 2026-07-29 | SHW | BLOCKED | REPAIR | 343.88 | 354.22 | 3 | +3.0% | -0.9 | OPEN |
| 2026-07-29 | SKYY | BLOCKED | PASS | 138.56 | 147.98 | 3 | +6.8% | +2.9 | OPEN |
| 2026-07-29 | SMCI | BLOCKED | DEEP-FAIL | 25.7 | 28.64 | 3 | +11.4% | +7.6 | OPEN |
| 2026-07-29 | STGW | BLOCKED | PASS | 8.08 | 8.7 | 3 | +7.7% | +3.8 | OPEN |
| 2026-07-29 | TDY | BLOCKED | PASS | 631.35 | 670.56 | 3 | +6.2% | +2.3 | OPEN |
| 2026-07-29 | TOST | BLOCKED | REPAIR | 32.6 | 32.79 | 3 | +0.6% | -3.3 | OPEN |
| 2026-07-29 | TPR | BLOCKED | PASS | 150.11 | 155.63 | 3 | +3.7% | -0.2 | OPEN |
| 2026-07-29 | TYL | BLOCKED | DEEP-FAIL | 333.5 | 305.54 | 3 | -8.4% | -12.2 | OPEN |
| 2026-07-29 | URI | BLOCKED | PASS | 1055.11 | 1115.92 | 3 | +5.8% | +1.9 | OPEN |
| 2026-07-29 | VRSN | BLOCKED | REPAIR | 290.92 | 298.89 | 3 | +2.7% | -1.1 | OPEN |
| 2026-07-29 | WWD | BLOCKED | PASS | 385.42 | 363.57 | 3 | -5.7% | -9.5 | OPEN |
| 2026-07-29 | ZTS | BLOCKED | DEEP-FAIL | 77.93 | 77.1 | 3 | -1.1% | -4.9 | OPEN |
| 2026-07-29 | CCL | PASSED | REPAIR | 27.81 | 28.74 | 3 | +3.3% | -0.5 | OPEN |
| 2026-07-29 | CPT | PASSED | PASS | 116.37 | 110.72 | 3 | -4.9% | -8.7 | OPEN |
| 2026-07-29 | CTS | PASSED | PASS | 61.53 | 65.23 | 3 | +6.0% | +2.1 | OPEN |
| 2026-07-29 | DAL | PASSED | PASS | 86.25 | 91.59 | 3 | +6.2% | +2.3 | OPEN |
| 2026-07-29 | DGX | PASSED | PASS | 235.22 | 231.95 | 3 | -1.4% | -5.3 | OPEN |
| 2026-07-29 | DLR | PASSED | PASS | 188.18 | 191.22 | 3 | +1.6% | -2.2 | OPEN |
| 2026-07-29 | GE | PASSED | PASS | 350.63 | 368.93 | 3 | +5.2% | +1.4 | OPEN |
| 2026-07-29 | HON | PASSED | PASS | 241.12 | 246.77 | 3 | +2.3% | -1.5 | OPEN |
| 2026-07-29 | JNJ | PASSED | PASS | 265.53 | 254.41 | 3 | -4.2% | -8.1 | OPEN |
| 2026-07-29 | KDP | PASSED | PASS | 31.45 | 30.91 | 3 | -1.7% | -5.6 | OPEN |
| 2026-07-29 | LHX | PASSED | REPAIR | 297.53 | 277.86 | 3 | -6.6% | -10.5 | OPEN |
| 2026-07-29 | LLY | PASSED | PASS | 1210.02 | 1121.36 | 3 | -7.3% | -11.2 | OPEN |
| 2026-07-29 | MDT | PASSED | REPAIR | 87.54 | 86.68 | 3 | -1.0% | -4.8 | OPEN |
| 2026-07-29 | MNST | PASSED | PASS | 97.23 | 93.55 | 3 | -3.8% | -7.7 | OPEN |
| 2026-07-29 | MRK | PASSED | PASS | 130.36 | 127.77 | 3 | -2.0% | -5.8 | OPEN |
| 2026-07-29 | PEP | PASSED | REPAIR | 143.5 | 139.63 | 3 | -2.7% | -6.6 | OPEN |
| 2026-07-29 | RACE | PASSED | REPAIR | 385.69 | 401.28 | 3 | +4.0% | +0.2 | OPEN |
| 2026-07-29 | SLB | PASSED | REPAIR | 48.96 | 49.31 | 3 | +0.7% | -3.1 | OPEN |
| 2026-07-29 | SSD | PASSED | REPAIR | 189.48 | 192.17 | 3 | +1.4% | -2.5 | OPEN |
| 2026-07-29 | TJX | PASSED | PASS | 161.63 | 157.5 | 3 | -2.6% | -6.4 | OPEN |
| 2026-07-30 | ABNB | BLOCKED | PASS | 152.08 | 150.64 | 2 | -0.9% | -3.1 | OPEN |
| 2026-07-30 | ACGL | BLOCKED | PASS | 101.14 | 101.12 | 2 | -0.0% | -2.2 | OPEN |
| 2026-07-30 | AGNC | BLOCKED | PASS | 10.92 | 10.64 | 2 | -2.6% | -4.7 | OPEN |
| 2026-07-30 | AI | BLOCKED | DEEP-FAIL | 9.07 | 9.73 | 2 | +7.3% | +5.1 | OPEN |
| 2026-07-30 | AJG | BLOCKED | REPAIR | 256.46 | 247.79 | 2 | -3.4% | -5.5 | OPEN |
| 2026-07-30 | APD | BLOCKED | PASS | 300.2 | 292.94 | 2 | -2.4% | -4.6 | OPEN |
| 2026-07-30 | AXON | BLOCKED | REPAIR | 525.3 | 575.88 | 2 | +9.6% | +7.5 | OPEN |
| 2026-07-30 | CB | BLOCKED | PASS | 350.15 | 348.23 | 2 | -0.6% | -2.7 | OPEN |
| 2026-07-30 | CHTR | BLOCKED | DEEP-FAIL | 142.0 | 144.1 | 2 | +1.5% | -0.7 | OPEN |
| 2026-07-30 | CLX | BLOCKED | REPAIR | 96.73 | 98.26 | 2 | +1.6% | -0.6 | OPEN |
| 2026-07-30 | CMG | BLOCKED | REPAIR | 38.52 | 37.46 | 2 | -2.8% | -4.9 | OPEN |
| 2026-07-30 | CNP | BLOCKED | REPAIR | 42.15 | 41.92 | 2 | -0.6% | -2.7 | OPEN |
| 2026-07-30 | COKE | BLOCKED | PASS | 189.83 | 180.76 | 2 | -4.8% | -6.9 | OPEN |
| 2026-07-30 | CPRT | BLOCKED | DEEP-FAIL | 29.57 | 29.35 | 2 | -0.7% | -2.9 | OPEN |
| 2026-07-30 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.73 | 2 | +3.2% | +1.1 | OPEN |
| 2026-07-30 | DASH | BLOCKED | REPAIR | 197.53 | 200.5 | 2 | +1.5% | -0.7 | OPEN |
| 2026-07-30 | DE | BLOCKED | PASS | 599.47 | 605.06 | 2 | +0.9% | -1.2 | OPEN |
| 2026-07-30 | DUOL | BLOCKED | REPAIR | 133.6 | 135.8 | 2 | +1.6% | -0.5 | OPEN |
| 2026-07-30 | EGBN | BLOCKED | PASS | 27.49 | 27.86 | 2 | +1.4% | -0.8 | OPEN |
| 2026-07-30 | GME | BLOCKED | REPAIR | 21.88 | 19.06 | 2 | -12.9% | -15.0 | OPEN |
| 2026-07-30 | HD | BLOCKED | REPAIR | 333.35 | 340.02 | 2 | +2.0% | -0.1 | OPEN |
| 2026-07-30 | IBM | BLOCKED | DEEP-FAIL | 221.74 | 226.31 | 2 | +2.1% | -0.1 | OPEN |
| 2026-07-30 | JBLU | BLOCKED | PASS | 6.07 | 6.23 | 2 | +2.6% | +0.5 | OPEN |
| 2026-07-30 | KWEB | BLOCKED | DEEP-FAIL | 28.06 | 28.74 | 2 | +2.4% | +0.3 | OPEN |
| 2026-07-30 | LDOS | BLOCKED | DEEP-FAIL | 112.41 | 118.72 | 2 | +5.6% | +3.5 | OPEN |
| 2026-07-30 | LLY | BLOCKED | PASS | 1154.97 | 1121.36 | 2 | -2.9% | -5.1 | OPEN |
| 2026-07-30 | LOW | BLOCKED | DEEP-FAIL | 210.08 | 212.06 | 2 | +0.9% | -1.2 | OPEN |
| 2026-07-30 | LYV | BLOCKED | PASS | 183.56 | 181.69 | 2 | -1.0% | -3.2 | OPEN |
| 2026-07-30 | LZB | BLOCKED | PASS | 40.13 | 41.0 | 2 | +2.2% | +0.0 | OPEN |
| 2026-07-30 | MAR | BLOCKED | REPAIR | 375.48 | 346.83 | 2 | -7.6% | -9.8 | OPEN |
| 2026-07-30 | MCD | BLOCKED | DEEP-FAIL | 268.44 | 265.23 | 2 | -1.2% | -3.4 | OPEN |
| 2026-07-30 | MIDD | BLOCKED | PASS | 133.32 | 135.81 | 2 | +1.9% | -0.3 | OPEN |
| 2026-07-30 | MRK | BLOCKED | PASS | 129.79 | 127.77 | 2 | -1.6% | -3.7 | OPEN |
| 2026-07-30 | MSFT | BLOCKED | REPAIR | 451.1 | 487.65 | 2 | +8.1% | +6.0 | OPEN |
| 2026-07-30 | NCLH | BLOCKED | REPAIR | 18.72 | 19.76 | 2 | +5.6% | +3.4 | OPEN |
| 2026-07-30 | NFLX | BLOCKED | DEEP-FAIL | 73.17 | 73.33 | 2 | +0.2% | -1.9 | OPEN |
| 2026-07-30 | NIO | BLOCKED | DEEP-FAIL | 4.84 | 4.81 | 2 | -0.6% | -2.8 | OPEN |
| 2026-07-30 | NOW | BLOCKED | DEEP-FAIL | 110.07 | 114.19 | 2 | +3.7% | +1.6 | OPEN |
| 2026-07-30 | NVST | BLOCKED | PASS | 27.78 | 27.37 | 2 | -1.5% | -3.6 | OPEN |
| 2026-07-30 | PB | BLOCKED | PASS | 74.82 | 75.25 | 2 | +0.6% | -1.6 | OPEN |
| 2026-07-30 | PGR | BLOCKED | REPAIR | 213.28 | 210.46 | 2 | -1.3% | -3.5 | OPEN |
| 2026-07-30 | PH | BLOCKED | PASS | 962.79 | 997.52 | 2 | +3.6% | +1.4 | OPEN |
| 2026-07-30 | RCL | BLOCKED | REPAIR | 321.94 | 324.0 | 2 | +0.6% | -1.5 | OPEN |
| 2026-07-30 | RMD | BLOCKED | REPAIR | 208.56 | 215.19 | 2 | +3.2% | +1.0 | OPEN |
| 2026-07-30 | ROKU | BLOCKED | PASS | 145.09 | 145.84 | 2 | +0.5% | -1.6 | OPEN |
| 2026-07-30 | RSPU | BLOCKED | REPAIR | 79.51 | 78.98 | 2 | -0.7% | -2.8 | OPEN |
| 2026-07-30 | SFM | BLOCKED | REPAIR | 86.85 | 88.81 | 2 | +2.3% | +0.1 | OPEN |
| 2026-07-30 | SHAK | BLOCKED | DEEP-FAIL | 63.07 | 64.78 | 2 | +2.7% | +0.6 | OPEN |
| 2026-07-30 | SHW | BLOCKED | REPAIR | 344.84 | 354.22 | 2 | +2.7% | +0.6 | OPEN |
| 2026-07-30 | SKYY | BLOCKED | PASS | 140.03 | 147.98 | 2 | +5.7% | +3.5 | OPEN |
| 2026-07-30 | SSD | BLOCKED | REPAIR | 186.67 | 192.17 | 2 | +3.0% | +0.8 | OPEN |
| 2026-07-30 | STGW | BLOCKED | PASS | 8.49 | 8.7 | 2 | +2.5% | +0.3 | OPEN |
| 2026-07-30 | TDY | BLOCKED | PASS | 649.18 | 670.56 | 2 | +3.3% | +1.1 | OPEN |
| 2026-07-30 | TOST | BLOCKED | REPAIR | 32.85 | 32.79 | 2 | -0.2% | -2.3 | OPEN |
| 2026-07-30 | TPR | BLOCKED | PASS | 152.58 | 155.63 | 2 | +2.0% | -0.2 | OPEN |
| 2026-07-30 | TYL | BLOCKED | DEEP-FAIL | 323.31 | 305.54 | 2 | -5.5% | -7.7 | OPEN |
| 2026-07-30 | URI | BLOCKED | PASS | 1068.63 | 1115.92 | 2 | +4.4% | +2.3 | OPEN |
| 2026-07-30 | ZTS | BLOCKED | DEEP-FAIL | 76.03 | 77.1 | 2 | +1.4% | -0.8 | OPEN |
| 2026-07-30 | CCL | PASSED | REPAIR | 27.77 | 28.74 | 2 | +3.5% | +1.3 | OPEN |
| 2026-07-30 | CPT | PASSED | PASS | 113.29 | 110.72 | 2 | -2.3% | -4.4 | OPEN |
| 2026-07-30 | CTS | PASSED | REPAIR | 62.7 | 65.23 | 2 | +4.0% | +1.9 | OPEN |
| 2026-07-30 | DAL | PASSED | PASS | 88.59 | 91.59 | 2 | +3.4% | +1.2 | OPEN |
| 2026-07-30 | DGX | PASSED | PASS | 234.3 | 231.95 | 2 | -1.0% | -3.2 | OPEN |
| 2026-07-30 | EQIX | PASSED | PASS | 1047.53 | 1031.44 | 2 | -1.5% | -3.7 | OPEN |
| 2026-07-30 | ERIE | PASSED | REPAIR | 233.67 | 236.86 | 2 | +1.4% | -0.8 | OPEN |
| 2026-07-30 | GE | PASSED | PASS | 355.04 | 368.93 | 2 | +3.9% | +1.8 | OPEN |
| 2026-07-30 | JETS | PASSED | PASS | 31.68 | 32.67 | 2 | +3.1% | +1.0 | OPEN |
| 2026-07-30 | KDP | PASSED | PASS | 31.57 | 30.91 | 2 | -2.1% | -4.2 | OPEN |
| 2026-07-30 | MDT | PASSED | REPAIR | 85.71 | 86.68 | 2 | +1.1% | -1.0 | OPEN |
| 2026-07-30 | MNST | PASSED | PASS | 97.65 | 93.55 | 2 | -4.2% | -6.3 | OPEN |
| 2026-07-30 | PEP | PASSED | REPAIR | 140.2 | 139.63 | 2 | -0.4% | -2.6 | OPEN |
| 2026-07-30 | RACE | PASSED | REPAIR | 397.73 | 401.28 | 2 | +0.9% | -1.3 | OPEN |
| 2026-07-30 | ROP | PASSED | REPAIR | 389.25 | 392.57 | 2 | +0.8% | -1.3 | OPEN |
| 2026-07-30 | ST | PASSED | PASS | 47.99 | 46.82 | 2 | -2.4% | -4.6 | OPEN |
| 2026-07-30 | TJX | PASSED | PASS | 159.26 | 157.5 | 2 | -1.1% | -3.3 | OPEN |
| 2026-07-30 | VRSN | PASSED | REPAIR | 286.58 | 298.89 | 2 | +4.3% | +2.1 | OPEN |
| 2026-07-31 | ABNB | BLOCKED | PASS | 151.52 | 150.64 | 1 | -0.6% | -2.0 | OPEN |
| 2026-07-31 | ACGL | BLOCKED | PASS | 100.53 | 101.12 | 1 | +0.6% | -0.8 | OPEN |
| 2026-07-31 | AGNC | BLOCKED | PASS | 10.66 | 10.64 | 1 | -0.2% | -1.6 | OPEN |
| 2026-07-31 | AI | BLOCKED | DEEP-FAIL | 9.18 | 9.73 | 1 | +6.0% | +4.6 | OPEN |
| 2026-07-31 | AJG | BLOCKED | REPAIR | 249.42 | 247.79 | 1 | -0.7% | -2.1 | OPEN |
| 2026-07-31 | AMZN | BLOCKED | PASS | 271.58 | 284.02 | 1 | +4.6% | +3.2 | OPEN |
| 2026-07-31 | APD | BLOCKED | PASS | 294.89 | 292.94 | 1 | -0.7% | -2.1 | OPEN |
| 2026-07-31 | APH | BLOCKED | PASS | 160.7 | 163.34 | 1 | +1.6% | +0.2 | OPEN |
| 2026-07-31 | AXON | BLOCKED | REPAIR | 527.76 | 575.88 | 1 | +9.1% | +7.7 | OPEN |
| 2026-07-31 | BABA | BLOCKED | DEEP-FAIL | 122.25 | 127.3 | 1 | +4.1% | +2.7 | OPEN |
| 2026-07-31 | CB | BLOCKED | PASS | 350.68 | 348.23 | 1 | -0.7% | -2.1 | OPEN |
| 2026-07-31 | CCL | BLOCKED | REPAIR | 27.81 | 28.74 | 1 | +3.3% | +1.9 | OPEN |
| 2026-07-31 | CHTR | BLOCKED | DEEP-FAIL | 144.98 | 144.1 | 1 | -0.6% | -2.0 | OPEN |
| 2026-07-31 | CLX | BLOCKED | REPAIR | 95.53 | 98.26 | 1 | +2.9% | +1.4 | OPEN |
| 2026-07-31 | CMG | BLOCKED | REPAIR | 37.22 | 37.46 | 1 | +0.6% | -0.8 | OPEN |
| 2026-07-31 | COKE | BLOCKED | PASS | 187.9 | 180.76 | 1 | -3.8% | -5.2 | OPEN |
| 2026-07-31 | CPRT | BLOCKED | DEEP-FAIL | 29.12 | 29.35 | 1 | +0.8% | -0.6 | OPEN |
| 2026-07-31 | CPT | BLOCKED | REPAIR | 110.81 | 110.72 | 1 | -0.1% | -1.5 | OPEN |
| 2026-07-31 | CTM | BLOCKED | DEEP-FAIL | 0.72 | 0.73 | 1 | +2.4% | +0.9 | OPEN |
| 2026-07-31 | DAL | BLOCKED | PASS | 87.44 | 91.59 | 1 | +4.8% | +3.3 | OPEN |
| 2026-07-31 | DASH | BLOCKED | REPAIR | 196.16 | 200.5 | 1 | +2.2% | +0.8 | OPEN |
| 2026-07-31 | DE | BLOCKED | PASS | 592.67 | 605.06 | 1 | +2.1% | +0.7 | OPEN |
| 2026-07-31 | DUOL | BLOCKED | REPAIR | 134.81 | 135.8 | 1 | +0.7% | -0.7 | OPEN |
| 2026-07-31 | EGBN | BLOCKED | PASS | 27.75 | 27.86 | 1 | +0.4% | -1.0 | OPEN |
| 2026-07-31 | EME | BLOCKED | PASS | 797.43 | 817.42 | 1 | +2.5% | +1.1 | OPEN |
| 2026-07-31 | EQIX | BLOCKED | REPAIR | 1019.28 | 1031.44 | 1 | +1.2% | -0.2 | OPEN |
| 2026-07-31 | ERIE | BLOCKED | REPAIR | 242.04 | 236.86 | 1 | -2.1% | -3.6 | OPEN |
| 2026-07-31 | GH | BLOCKED | PASS | 161.99 | 158.83 | 1 | -1.9% | -3.4 | OPEN |
| 2026-07-31 | GME | BLOCKED | REPAIR | 21.72 | 19.06 | 1 | -12.2% | -13.7 | OPEN |
| 2026-07-31 | GOOG | BLOCKED | REPAIR | 356.65 | 372.47 | 1 | +4.4% | +3.0 | OPEN |
| 2026-07-31 | GRND | BLOCKED | PASS | 17.34 | 17.9 | 1 | +3.2% | +1.8 | OPEN |
| 2026-07-31 | HD | BLOCKED | REPAIR | 331.96 | 340.02 | 1 | +2.4% | +1.0 | OPEN |
| 2026-07-31 | IBM | BLOCKED | DEEP-FAIL | 223.65 | 226.31 | 1 | +1.2% | -0.2 | OPEN |
| 2026-07-31 | IGV | BLOCKED | REPAIR | 94.58 | 97.42 | 1 | +3.0% | +1.6 | OPEN |
| 2026-07-31 | JBLU | BLOCKED | PASS | 6.03 | 6.23 | 1 | +3.3% | +1.9 | OPEN |
| 2026-07-31 | JETS | BLOCKED | PASS | 31.28 | 32.67 | 1 | +4.4% | +3.0 | OPEN |
| 2026-07-31 | KWEB | BLOCKED | DEEP-FAIL | 28.49 | 28.74 | 1 | +0.9% | -0.6 | OPEN |
| 2026-07-31 | LDOS | BLOCKED | DEEP-FAIL | 115.6 | 118.72 | 1 | +2.7% | +1.3 | OPEN |
| 2026-07-31 | LOW | BLOCKED | DEEP-FAIL | 207.81 | 212.06 | 1 | +2.0% | +0.6 | OPEN |
| 2026-07-31 | LYV | BLOCKED | PASS | 174.13 | 181.69 | 1 | +4.3% | +2.9 | OPEN |
| 2026-07-31 | LZB | BLOCKED | PASS | 39.38 | 41.0 | 1 | +4.1% | +2.7 | OPEN |
| 2026-07-31 | MAR | BLOCKED | REPAIR | 372.83 | 346.83 | 1 | -7.0% | -8.4 | OPEN |
| 2026-07-31 | MCD | BLOCKED | DEEP-FAIL | 270.64 | 265.23 | 1 | -2.0% | -3.4 | OPEN |
| 2026-07-31 | MDT | BLOCKED | REPAIR | 85.39 | 86.68 | 1 | +1.5% | +0.1 | OPEN |
| 2026-07-31 | MIDD | BLOCKED | PASS | 133.58 | 135.81 | 1 | +1.7% | +0.2 | OPEN |
| 2026-07-31 | MRK | BLOCKED | PASS | 130.2 | 127.77 | 1 | -1.9% | -3.3 | OPEN |
| 2026-07-31 | MSFT | BLOCKED | REPAIR | 464.72 | 487.65 | 1 | +4.9% | +3.5 | OPEN |
| 2026-07-31 | NCLH | BLOCKED | REPAIR | 18.53 | 19.76 | 1 | +6.6% | +5.2 | OPEN |
| 2026-07-31 | NFLX | BLOCKED | DEEP-FAIL | 71.71 | 73.33 | 1 | +2.3% | +0.8 | OPEN |
| 2026-07-31 | NIO | BLOCKED | DEEP-FAIL | 4.88 | 4.81 | 1 | -1.4% | -2.9 | OPEN |
| 2026-07-31 | NOW | BLOCKED | DEEP-FAIL | 111.23 | 114.19 | 1 | +2.7% | +1.2 | OPEN |
| 2026-07-31 | PEP | BLOCKED | REPAIR | 139.56 | 139.63 | 1 | +0.1% | -1.4 | OPEN |
| 2026-07-31 | PGR | BLOCKED | REPAIR | 211.42 | 210.46 | 1 | -0.5% | -1.9 | OPEN |
| 2026-07-31 | PH | BLOCKED | PASS | 976.53 | 997.52 | 1 | +2.1% | +0.7 | OPEN |
| 2026-07-31 | PLPC | BLOCKED | PASS | 356.98 | 358.15 | 1 | +0.3% | -1.1 | OPEN |
| 2026-07-31 | PWR | BLOCKED | REPAIR | 667.36 | 680.2 | 1 | +1.9% | +0.5 | OPEN |
| 2026-07-31 | RCL | BLOCKED | REPAIR | 318.3 | 324.0 | 1 | +1.8% | +0.4 | OPEN |
| 2026-07-31 | RMD | BLOCKED | DEEP-FAIL | 210.98 | 215.19 | 1 | +2.0% | +0.6 | OPEN |
| 2026-07-31 | ROKU | BLOCKED | PASS | 145.01 | 145.84 | 1 | +0.6% | -0.8 | OPEN |
| 2026-07-31 | ROP | BLOCKED | REPAIR | 391.97 | 392.57 | 1 | +0.1% | -1.3 | OPEN |
| 2026-07-31 | SFM | BLOCKED | REPAIR | 87.16 | 88.81 | 1 | +1.9% | +0.5 | OPEN |
| 2026-07-31 | SHAK | BLOCKED | DEEP-FAIL | 62.75 | 64.78 | 1 | +3.2% | +1.8 | OPEN |
| 2026-07-31 | SHW | BLOCKED | REPAIR | 340.85 | 354.22 | 1 | +3.9% | +2.5 | OPEN |
| 2026-07-31 | SKYY | BLOCKED | PASS | 143.0 | 147.98 | 1 | +3.5% | +2.1 | OPEN |
| 2026-07-31 | SSD | BLOCKED | REPAIR | 187.74 | 192.17 | 1 | +2.4% | +0.9 | OPEN |
| 2026-07-31 | TOST | BLOCKED | REPAIR | 32.27 | 32.79 | 1 | +1.6% | +0.2 | OPEN |
| 2026-07-31 | TPR | BLOCKED | PASS | 152.37 | 155.63 | 1 | +2.1% | +0.7 | OPEN |
| 2026-07-31 | TYL | BLOCKED | DEEP-FAIL | 309.6 | 305.54 | 1 | -1.3% | -2.7 | OPEN |
| 2026-07-31 | XLY | BLOCKED | REPAIR | 116.09 | 118.21 | 1 | +1.8% | +0.4 | OPEN |
| 2026-07-31 | ZTS | BLOCKED | DEEP-FAIL | 77.29 | 77.1 | 1 | -0.2% | -1.7 | OPEN |
| 2026-07-31 | CTS | PASSED | PASS | 64.12 | 65.23 | 1 | +1.7% | +0.3 | OPEN |
| 2026-07-31 | FIVN | PASSED | PASS | 27.51 | 28.95 | 1 | +5.2% | +3.8 | OPEN |
| 2026-07-31 | GE | PASSED | PASS | 360.07 | 368.93 | 1 | +2.5% | +1.0 | OPEN |
| 2026-07-31 | KDP | PASSED | PASS | 31.12 | 30.91 | 1 | -0.7% | -2.1 | OPEN |
| 2026-07-31 | RACE | PASSED | REPAIR | 393.87 | 401.28 | 1 | +1.9% | +0.5 | OPEN |
| 2026-07-31 | ST | PASSED | REPAIR | 46.29 | 46.82 | 1 | +1.1% | -0.3 | OPEN |
| 2026-07-31 | TJX | PASSED | PASS | 157.34 | 157.5 | 1 | +0.1% | -1.3 | OPEN |
| 2026-07-31 | VRSN | PASSED | REPAIR | 290.02 | 298.89 | 1 | +3.1% | +1.6 | OPEN |

Open marks are not results. This file exists so that the cull the scan performs every night is measured instead of assumed.
