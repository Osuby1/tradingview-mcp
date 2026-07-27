# Gate stack forward grade

Does THE GATE STACK earn its keep? Every fresh Chandelier signal is graded forward from the CLOSE of its signal date over 21 trading sessions, bucketed by what the stack decided. The number that matters is the SPREAD.

- Signal events found: 275  |  priced: 224  |  unique symbol-cohort pairs (headline sample): 157
- Skipped (pre-2026-07-22 hand-written verdicts, not machine-comparable): 20

## Headline - all signals, deduped to first appearance

| Cohort | n | Win% | Mean | Median | Mean vs SPY | Mean worst drawdown |
|---|---|---|---|---|---|---|
| PASSED | 27 | 48% | -0.11% | -0.07% | +0.56% | -3.61% |
| BLOCKED | 130 | 50% | -0.13% | +0.02% | +0.70% | -4.15% |

**Spread (PASSED minus BLOCKED): +0.02 percentage points.**

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
| ADX FLOOR | 41 | 56% | +0.39% | +0.48% | +1.22% |
| ATR GEOMETRY | 4 | 25% | -0.86% | -1.35% | -0.65% |
| DIRECTION | 9 | 11% | -5.39% | -3.54% | -4.28% |
| LIQUIDITY | 1 | 0% | -9.20% | -9.20% | -8.08% |
| OTHER | 30 | 53% | +0.37% | +0.61% | +1.24% |
| REGIME | 9 | 44% | +1.64% | -0.16% | +2.33% |
| VOLATILITY CAP (ex 2:1) | 1 | 0% | -3.37% | -3.37% | -2.26% |
| ZLSMA | 35 | 57% | +0.17% | +0.48% | +0.98% |

## Shadow cohorts - the forbidden retro-tune, run forward instead

Would lowering the ADX floor to 18, or softening DEEP-FAIL, have helped? The replay's missed monsters make that tempting; answering it by re-running history is curve-fitting. These cohorts answer it FORWARD: sole-failure near-misses graded nightly against the PASSED cohort. Promotion bar (pre-registered): >=30 MATURED signals AND mean above PASSED's - then it goes to a Friday review, not before.

| Shadow cohort | n | Win% | Mean | Median | Mean vs SPY | PASSED mean (ref) |
|---|---|---|---|---|---|---|
| ADX 18-20, all else passed | 0 | - | - | - | - | -0.11% |
| DEEP-FAIL, all else passed | 1 | 100% | +2.51% | +2.51% | +2.48% | -0.11% |

## Every graded signal

| Date | Sym | Cohort | Regime | Entry | Mark | Days | Return | vs SPY | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | BG | BLOCKED | n/a | 120.49 | 117.5 | 5 | -2.5% | -2.1 | OPEN |
| 2026-07-20 | CHRD | BLOCKED | n/a | 128.8 | 131.8 | 5 | +2.3% | +2.7 | OPEN |
| 2026-07-20 | CNOB | BLOCKED | n/a | 33.46 | 32.82 | 5 | -1.9% | -1.5 | OPEN |
| 2026-07-20 | COCO | BLOCKED | PASS | 73.87 | 67.35 | 5 | -8.8% | -8.4 | OPEN |
| 2026-07-20 | CVNA | BLOCKED | DEEP-FAIL | 64.14 | 64.04 | 5 | -0.2% | +0.2 | OPEN |
| 2026-07-20 | FLG | BLOCKED | n/a | 14.84 | 13.76 | 5 | -7.3% | -6.9 | OPEN |
| 2026-07-20 | FNB | BLOCKED | n/a | 18.75 | 18.84 | 5 | +0.5% | +0.9 | OPEN |
| 2026-07-20 | HAS | BLOCKED | REPAIR | 81.59 | 90.61 | 5 | +11.1% | +11.5 | OPEN |
| 2026-07-20 | HLX | BLOCKED | n/a | 9.43 | 9.64 | 5 | +2.2% | +2.6 | OPEN |
| 2026-07-20 | LCID | BLOCKED | n/a | 7.11 | 6.5 | 5 | -8.6% | -8.2 | OPEN |
| 2026-07-20 | M | BLOCKED | REPAIR | 23.31 | 24.96 | 5 | +7.1% | +7.5 | OPEN |
| 2026-07-20 | NOV | BLOCKED | REPAIR | 19.55 | 20.47 | 5 | +4.7% | +5.1 | OPEN |
| 2026-07-20 | ODFL | BLOCKED | PASS | 231.76 | 226.77 | 5 | -2.1% | -1.8 | OPEN |
| 2026-07-20 | RYZ | BLOCKED | n/a | 29.07 | 30.62 | 5 | +5.3% | +5.7 | OPEN |
| 2026-07-20 | SHAK | BLOCKED | DEEP-FAIL | 56.97 | 61.57 | 5 | +8.1% | +8.5 | OPEN |
| 2026-07-20 | SPG | BLOCKED | PASS | 228.19 | 231.67 | 5 | +1.5% | +1.9 | OPEN |
| 2026-07-20 | TRNS | BLOCKED | n/a | 86.09 | 86.14 | 5 | +0.1% | +0.5 | OPEN |
| 2026-07-20 | VVV | BLOCKED | PASS | 39.54 | 39.56 | 5 | +0.1% | +0.5 | OPEN |
| 2026-07-20 | VZ | BLOCKED | REPAIR | 43.5 | 47.32 | 5 | +8.8% | +9.2 | OPEN |
| 2026-07-20 | WPC | BLOCKED | REPAIR | 75.17 | 76.21 | 5 | +1.4% | +1.8 | OPEN |
| 2026-07-21 | ALKS | BLOCKED | TAPE OK | 52.85 | 52.73 | 4 | -0.2% | +1.0 | OPEN |
| 2026-07-21 | ATLC | BLOCKED | TAPE OK | 96.37 | 104.2 | 4 | +8.1% | +9.3 | OPEN |
| 2026-07-21 | BRKR | BLOCKED | TAPE OK | 60.43 | 60.05 | 4 | -0.6% | +0.6 | OPEN |
| 2026-07-21 | CB | BLOCKED | TAPE OK | 354.8 | 358.91 | 4 | +1.2% | +2.4 | OPEN |
| 2026-07-21 | CBL | BLOCKED | TAPE OK | 55.53 | 58.41 | 4 | +5.2% | +6.4 | OPEN |
| 2026-07-21 | CNOB | BLOCKED | TAPE OK | 33.41 | 32.82 | 4 | -1.8% | -0.5 | OPEN |
| 2026-07-21 | COCO | BLOCKED | TAPE OK | 75.89 | 67.35 | 4 | -11.2% | -10.0 | OPEN |
| 2026-07-21 | CTRE | BLOCKED | TAPE OK | 43.4 | 42.96 | 4 | -1.0% | +0.2 | OPEN |
| 2026-07-21 | ESQ | BLOCKED | TAPE OK | 122.83 | 120.49 | 4 | -1.9% | -0.7 | OPEN |
| 2026-07-21 | EXTR | BLOCKED | TAPE OK | 30.44 | 29.95 | 4 | -1.6% | -0.4 | OPEN |
| 2026-07-21 | FFIV | BLOCKED | TAPE OK | 408.74 | 407.96 | 4 | -0.2% | +1.0 | OPEN |
| 2026-07-21 | FRT | BLOCKED | TAPE OK | 125.59 | 127.13 | 4 | +1.2% | +2.5 | OPEN |
| 2026-07-21 | HCSG | BLOCKED | TAPE OK | 24.8 | 22.95 | 4 | -7.5% | -6.2 | OPEN |
| 2026-07-21 | HELE | BLOCKED | TAPE OK | 27.28 | 28.27 | 4 | +3.6% | +4.9 | OPEN |
| 2026-07-21 | HOMB | BLOCKED | TAPE OK | 30.42 | 30.98 | 4 | +1.8% | +3.1 | OPEN |
| 2026-07-21 | LQDA | BLOCKED | TAPE OK | 80.89 | 84.42 | 4 | +4.4% | +5.6 | OPEN |
| 2026-07-21 | NVRI | BLOCKED | TAPE OK | 21.87 | 22.07 | 4 | +0.9% | +2.1 | OPEN |
| 2026-07-21 | NWPX | BLOCKED | TAPE OK | 135.41 | 128.26 | 4 | -5.3% | -4.0 | OPEN |
| 2026-07-21 | OSCR | BLOCKED | TAPE OK | 30.77 | 28.34 | 4 | -7.9% | -6.7 | OPEN |
| 2026-07-21 | PNC | BLOCKED | TAPE OK | 250.38 | 249.64 | 4 | -0.3% | +0.9 | OPEN |
| 2026-07-21 | SION | BLOCKED | TAPE OK | 47.21 | 45.38 | 4 | -3.9% | -2.6 | OPEN |
| 2026-07-21 | TBLA | BLOCKED | TAPE OK | 5.11 | 4.95 | 4 | -3.1% | -1.9 | OPEN |
| 2026-07-21 | TFIN | BLOCKED | TAPE OK | 79.19 | 75.38 | 4 | -4.8% | -3.6 | OPEN |
| 2026-07-21 | TGTX | BLOCKED | TAPE OK | 53.95 | 55.75 | 4 | +3.3% | +4.6 | OPEN |
| 2026-07-21 | TVTX | BLOCKED | TAPE OK | 56.58 | 56.68 | 4 | +0.2% | +1.4 | OPEN |
| 2026-07-21 | VCYT | BLOCKED | TAPE OK | 59.53 | 55.61 | 4 | -6.6% | -5.4 | OPEN |
| 2026-07-21 | ZD | BLOCKED | TAPE OK | 52.39 | 52.36 | 4 | -0.1% | +1.2 | OPEN |
| 2026-07-21 | CYRX | PASSED | TAPE OK | 16.24 | 15.15 | 4 | -6.7% | -5.5 | OPEN |
| 2026-07-21 | FLEX | PASSED | TAPE OK | 127.39 | 116.07 | 4 | -8.9% | -7.7 | OPEN |
| 2026-07-21 | GDX | PASSED | TAPE OK | 74.19 | 75.73 | 4 | +2.1% | +3.3 | OPEN |
| 2026-07-21 | HON | PASSED | TAPE OK | 229.86 | 245.75 | 4 | +6.9% | +8.1 | OPEN |
| 2026-07-21 | KWEB | PASSED | TAPE OK | 27.02 | 27.0 | 4 | -0.1% | +1.1 | OPEN |
| 2026-07-21 | MSFT | PASSED | TAPE OK | 397.75 | 389.1 | 4 | -2.2% | -0.9 | OPEN |
| 2026-07-21 | MU | PASSED | TAPE OK | 970.82 | 900.2 | 4 | -7.3% | -6.0 | OPEN |
| 2026-07-21 | NKE | PASSED | TAPE OK | 42.96 | 42.14 | 4 | -1.9% | -0.7 | OPEN |
| 2026-07-21 | PM | PASSED | TAPE OK | 188.04 | 195.66 | 4 | +4.0% | +5.3 | OPEN |
| 2026-07-21 | SKYY | PASSED | TAPE OK | 136.02 | 135.84 | 4 | -0.1% | +1.1 | OPEN |
| 2026-07-21 | SNOW | PASSED | TAPE OK | 271.73 | 272.92 | 4 | +0.4% | +1.7 | OPEN |
| 2026-07-22 | ACTG | BLOCKED | REPAIR | 4.57 | 4.63 | 3 | +1.3% | +2.4 | OPEN |
| 2026-07-22 | AMCR | BLOCKED | PASS | 43.21 | 45.24 | 3 | +4.7% | +5.8 | OPEN |
| 2026-07-22 | AMGN | BLOCKED | PASS | 366.05 | 376.26 | 3 | +2.8% | +3.9 | OPEN |
| 2026-07-22 | ASB | BLOCKED | PASS | 30.7 | 30.64 | 3 | -0.2% | +0.9 | OPEN |
| 2026-07-22 | BCBP | BLOCKED | REPAIR | 10.29 | 10.31 | 3 | +0.2% | +1.3 | OPEN |
| 2026-07-22 | BHP | BLOCKED | REPAIR | 84.54 | 83.93 | 3 | -0.7% | +0.4 | OPEN |
| 2026-07-22 | BHRB | BLOCKED | PASS | 71.01 | 72.5 | 3 | +2.1% | +3.2 | OPEN |
| 2026-07-22 | BX | BLOCKED | REPAIR | 122.82 | 132.6 | 3 | +8.0% | +9.1 | OPEN |
| 2026-07-22 | BY | BLOCKED | PASS | 37.75 | 38.68 | 3 | +2.5% | +3.6 | OPEN |
| 2026-07-22 | CBSH | BLOCKED | PASS | 58.7 | 59.0 | 3 | +0.5% | +1.6 | OPEN |
| 2026-07-22 | CCJ | BLOCKED | DEEP-FAIL | 90.37 | 89.35 | 3 | -1.1% | -0.0 | OPEN |
| 2026-07-22 | CMP | BLOCKED | REPAIR | 30.14 | 29.77 | 3 | -1.2% | -0.1 | OPEN |
| 2026-07-22 | CNOB | BLOCKED | PASS | 33.0 | 32.82 | 3 | -0.6% | +0.6 | OPEN |
| 2026-07-22 | COKE | BLOCKED | PASS | 184.36 | 186.28 | 3 | +1.0% | +2.1 | OPEN |
| 2026-07-22 | COLB | BLOCKED | PASS | 32.63 | 30.9 | 3 | -5.3% | -4.2 | OPEN |
| 2026-07-22 | COST | BLOCKED | REPAIR | 927.31 | 951.58 | 3 | +2.6% | +3.7 | OPEN |
| 2026-07-22 | CRCL | BLOCKED | DEEP-FAIL | 66.16 | 65.67 | 3 | -0.7% | +0.4 | OPEN |
| 2026-07-22 | DE | BLOCKED | PASS | 607.33 | 625.02 | 3 | +2.9% | +4.0 | OPEN |
| 2026-07-22 | DELL | BLOCKED | PASS | 441.8 | 426.91 | 3 | -3.4% | -2.3 | OPEN |
| 2026-07-22 | DIS | BLOCKED | REPAIR | 95.87 | 96.65 | 3 | +0.8% | +1.9 | OPEN |
| 2026-07-22 | EQR | BLOCKED | PASS | 68.29 | 67.24 | 3 | -1.5% | -0.4 | OPEN |
| 2026-07-22 | F | BLOCKED | PASS | 14.42 | 14.68 | 3 | +1.8% | +2.9 | OPEN |
| 2026-07-22 | FCX | BLOCKED | PASS | 65.0 | 62.72 | 3 | -3.5% | -2.4 | OPEN |
| 2026-07-22 | FHB | BLOCKED | PASS | 28.81 | 27.79 | 3 | -3.5% | -2.4 | OPEN |
| 2026-07-22 | FITB | BLOCKED | PASS | 57.67 | 57.0 | 3 | -1.2% | -0.1 | OPEN |
| 2026-07-22 | FLEX | BLOCKED | REPAIR | 127.0 | 116.07 | 3 | -8.6% | -7.5 | OPEN |
| 2026-07-22 | FLG | BLOCKED | PASS | 14.88 | 13.76 | 3 | -7.5% | -6.4 | OPEN |
| 2026-07-22 | FNB | BLOCKED | PASS | 18.86 | 18.84 | 3 | -0.1% | +1.0 | OPEN |
| 2026-07-22 | FRT | BLOCKED | PASS | 125.05 | 127.13 | 3 | +1.7% | +2.8 | OPEN |
| 2026-07-22 | GBCI | BLOCKED | PASS | 51.17 | 49.0 | 3 | -4.2% | -3.1 | OPEN |
| 2026-07-22 | GDX | BLOCKED | DEEP-FAIL | 76.68 | 75.73 | 3 | -1.2% | -0.1 | OPEN |
| 2026-07-22 | GLD | BLOCKED | REPAIR | 379.12 | 374.63 | 3 | -1.2% | -0.1 | OPEN |
| 2026-07-22 | GM | BLOCKED | PASS | 82.13 | 87.04 | 3 | +6.0% | +7.1 | OPEN |
| 2026-07-22 | HBNC | BLOCKED | PASS | 20.21 | 20.36 | 3 | +0.7% | +1.9 | OPEN |
| 2026-07-22 | HON | BLOCKED | PASS | 232.99 | 245.75 | 3 | +5.5% | +6.6 | OPEN |
| 2026-07-22 | HOPE | BLOCKED | PASS | 13.54 | 13.82 | 3 | +2.1% | +3.2 | OPEN |
| 2026-07-22 | HSIC | BLOCKED | PASS | 84.81 | 84.61 | 3 | -0.2% | +0.9 | OPEN |
| 2026-07-22 | HTZ | BLOCKED | DEEP-FAIL | 1.93 | 2.0 | 3 | +3.6% | +4.7 | OPEN |
| 2026-07-22 | KRE | BLOCKED | PASS | 75.6 | 75.52 | 3 | -0.1% | +1.0 | OPEN |
| 2026-07-22 | LCID | BLOCKED | DEEP-FAIL | 6.78 | 6.5 | 3 | -4.1% | -3.0 | OPEN |
| 2026-07-22 | LZB | BLOCKED | PASS | 39.3 | 40.38 | 3 | +2.8% | +3.9 | OPEN |
| 2026-07-22 | M | BLOCKED | PASS | 24.33 | 24.96 | 3 | +2.6% | +3.7 | OPEN |
| 2026-07-22 | MFA | BLOCKED | REPAIR | 9.29 | 9.12 | 3 | -1.8% | -0.7 | OPEN |
| 2026-07-22 | MU | BLOCKED | PASS | 959.48 | 900.2 | 3 | -6.2% | -5.1 | OPEN |
| 2026-07-22 | NEE | BLOCKED | PASS | 89.41 | 88.83 | 3 | -0.7% | +0.5 | OPEN |
| 2026-07-22 | NEM | BLOCKED | REPAIR | 95.75 | 93.47 | 3 | -2.4% | -1.3 | OPEN |
| 2026-07-22 | OCFC | BLOCKED | PASS | 19.67 | 19.6 | 3 | -0.4% | +0.8 | OPEN |
| 2026-07-22 | PANW | BLOCKED | PASS | 335.28 | 317.32 | 3 | -5.4% | -4.2 | OPEN |
| 2026-07-22 | PB | BLOCKED | PASS | 73.06 | 72.54 | 3 | -0.7% | +0.4 | OPEN |
| 2026-07-22 | PM | BLOCKED | PASS | 194.3 | 195.66 | 3 | +0.7% | +1.8 | OPEN |
| 2026-07-22 | POWL | BLOCKED | REPAIR | 240.68 | 219.23 | 3 | -8.9% | -7.8 | OPEN |
| 2026-07-22 | PRLB | BLOCKED | PASS | 79.73 | 77.64 | 3 | -2.6% | -1.5 | OPEN |
| 2026-07-22 | RACE | BLOCKED | REPAIR | 371.61 | 380.01 | 3 | +2.3% | +3.4 | OPEN |
| 2026-07-22 | RCL | BLOCKED | REPAIR | 285.85 | 305.04 | 3 | +6.7% | +7.8 | OPEN |
| 2026-07-22 | RSPU | BLOCKED | PASS | 81.85 | 81.24 | 3 | -0.8% | +0.4 | OPEN |
| 2026-07-22 | SAIC | BLOCKED | PASS | 115.95 | 118.48 | 3 | +2.2% | +3.3 | OPEN |
| 2026-07-22 | SJM | BLOCKED | PASS | 118.05 | 121.05 | 3 | +2.5% | +3.6 | OPEN |
| 2026-07-22 | SKK | BLOCKED | PASS | 5.22 | 4.74 | 3 | -9.2% | -8.1 | OPEN |
| 2026-07-22 | SMCI | BLOCKED | REPAIR | 30.56 | 29.81 | 3 | -2.5% | -1.3 | OPEN |
| 2026-07-22 | SON | BLOCKED | PASS | 55.15 | 58.68 | 3 | +6.4% | +7.5 | OPEN |
| 2026-07-22 | SPG | BLOCKED | PASS | 226.22 | 231.67 | 3 | +2.4% | +3.5 | OPEN |
| 2026-07-22 | SSB | BLOCKED | PASS | 102.19 | 105.16 | 3 | +2.9% | +4.0 | OPEN |
| 2026-07-22 | STRL | BLOCKED | REPAIR | 719.34 | 634.63 | 3 | -11.8% | -10.7 | OPEN |
| 2026-07-22 | STX | BLOCKED | PASS | 908.1 | 816.99 | 3 | -10.0% | -8.9 | OPEN |
| 2026-07-22 | TDY | BLOCKED | PASS | 650.5 | 651.65 | 3 | +0.2% | +1.3 | OPEN |
| 2026-07-22 | TPL | BLOCKED | PASS | 433.1 | 396.62 | 3 | -8.4% | -7.3 | OPEN |
| 2026-07-22 | TPR | BLOCKED | PASS | 143.73 | 147.43 | 3 | +2.6% | +3.7 | OPEN |
| 2026-07-22 | URA | BLOCKED | DEEP-FAIL | 40.97 | 40.32 | 3 | -1.6% | -0.5 | OPEN |
| 2026-07-22 | USB | BLOCKED | PASS | 64.47 | 63.49 | 3 | -1.5% | -0.4 | OPEN |
| 2026-07-22 | VST | BLOCKED | REPAIR | 166.74 | 157.08 | 3 | -5.8% | -4.7 | OPEN |
| 2026-07-22 | VVV | BLOCKED | PASS | 39.03 | 39.56 | 3 | +1.4% | +2.5 | OPEN |
| 2026-07-22 | CTRE | PASSED | PASS | 42.38 | 42.96 | 3 | +1.4% | +2.5 | OPEN |
| 2026-07-22 | PFE | PASSED | REPAIR | 24.82 | 24.67 | 3 | -0.6% | +0.5 | OPEN |
| 2026-07-22 | TJX | PASSED | REPAIR | 155.41 | 156.38 | 3 | +0.6% | +1.7 | OPEN |
| 2026-07-22 | TXNM | PASSED | REPAIR | 58.3 | 58.16 | 3 | -0.2% | +0.9 | OPEN |
| 2026-07-22 | VZ | PASSED | REPAIR | 44.29 | 47.32 | 3 | +6.8% | +8.0 | OPEN |
| 2026-07-23 | ACTG | BLOCKED | REPAIR | 4.62 | 4.63 | 2 | +0.2% | +0.1 | OPEN |
| 2026-07-23 | ALSN | BLOCKED | PASS | 119.64 | 121.91 | 2 | +1.9% | +1.8 | OPEN |
| 2026-07-23 | AVT | BLOCKED | PASS | 89.92 | 88.38 | 2 | -1.7% | -1.8 | OPEN |
| 2026-07-23 | BUD | BLOCKED | REPAIR | 80.48 | 80.87 | 2 | +0.5% | +0.4 | OPEN |
| 2026-07-23 | COST | BLOCKED | REPAIR | 926.06 | 951.58 | 2 | +2.8% | +2.6 | OPEN |
| 2026-07-23 | CRCL | BLOCKED | DEEP-FAIL | 62.18 | 65.67 | 2 | +5.6% | +5.5 | OPEN |
| 2026-07-23 | DELL | BLOCKED | PASS | 439.34 | 426.91 | 2 | -2.8% | -3.0 | OPEN |
| 2026-07-23 | DGX | BLOCKED | PASS | 227.9 | 231.84 | 2 | +1.7% | +1.6 | OPEN |
| 2026-07-23 | F | BLOCKED | REPAIR | 14.15 | 14.68 | 2 | +3.8% | +3.6 | OPEN |
| 2026-07-23 | FCX | BLOCKED | REPAIR | 63.5 | 62.72 | 2 | -1.2% | -1.4 | OPEN |
| 2026-07-23 | FLG | BLOCKED | PASS | 14.71 | 13.76 | 2 | -6.5% | -6.6 | OPEN |
| 2026-07-23 | FNB | BLOCKED | PASS | 18.87 | 18.84 | 2 | -0.2% | -0.3 | OPEN |
| 2026-07-23 | FUTU | BLOCKED | DEEP-FAIL | 98.96 | 104.27 | 2 | +5.4% | +5.2 | OPEN |
| 2026-07-23 | GDX | BLOCKED | DEEP-FAIL | 75.02 | 75.73 | 2 | +0.9% | +0.8 | OPEN |
| 2026-07-23 | GLD | BLOCKED | REPAIR | 371.52 | 374.63 | 2 | +0.8% | +0.7 | OPEN |
| 2026-07-23 | GM | BLOCKED | PASS | 80.67 | 87.04 | 2 | +7.9% | +7.8 | OPEN |
| 2026-07-23 | HON | BLOCKED | PASS | 246.27 | 245.75 | 2 | -0.2% | -0.3 | OPEN |
| 2026-07-23 | IRM | BLOCKED | REPAIR | 124.55 | 126.99 | 2 | +2.0% | +1.8 | OPEN |
| 2026-07-23 | LCID | BLOCKED | DEEP-FAIL | 6.45 | 6.5 | 2 | +0.8% | +0.7 | OPEN |
| 2026-07-23 | LSTR | BLOCKED | PASS | 207.97 | 191.63 | 2 | -7.9% | -8.0 | OPEN |
| 2026-07-23 | M | BLOCKED | PASS | 23.33 | 24.96 | 2 | +7.0% | +6.9 | OPEN |
| 2026-07-23 | MAC | BLOCKED | PASS | 25.3 | 26.13 | 2 | +3.3% | +3.2 | OPEN |
| 2026-07-23 | NEM | BLOCKED | REPAIR | 94.72 | 93.47 | 2 | -1.3% | -1.4 | OPEN |
| 2026-07-23 | PLD | BLOCKED | PASS | 145.12 | 147.26 | 2 | +1.5% | +1.4 | OPEN |
| 2026-07-23 | PRLB | BLOCKED | PASS | 78.62 | 77.64 | 2 | -1.2% | -1.4 | OPEN |
| 2026-07-23 | RHP | BLOCKED | PASS | 128.89 | 134.94 | 2 | +4.7% | +4.6 | OPEN |
| 2026-07-23 | SMCI | BLOCKED | REPAIR | 31.2 | 29.81 | 2 | -4.5% | -4.6 | OPEN |
| 2026-07-23 | SON | BLOCKED | PASS | 56.32 | 58.68 | 2 | +4.2% | +4.1 | OPEN |
| 2026-07-23 | SPG | BLOCKED | PASS | 225.2 | 231.67 | 2 | +2.9% | +2.8 | OPEN |
| 2026-07-23 | TDY | BLOCKED | PASS | 651.22 | 651.65 | 2 | +0.1% | -0.1 | OPEN |
| 2026-07-23 | URA | BLOCKED | DEEP-FAIL | 41.13 | 40.32 | 2 | -2.0% | -2.1 | OPEN |
| 2026-07-23 | URI | BLOCKED | PASS | 1139.71 | 1127.91 | 2 | -1.0% | -1.2 | OPEN |
| 2026-07-23 | VST | BLOCKED | REPAIR | 168.98 | 157.08 | 2 | -7.0% | -7.2 | OPEN |
| 2026-07-23 | VVV | BLOCKED | PASS | 38.31 | 39.56 | 2 | +3.3% | +3.1 | OPEN |
| 2026-07-23 | ECVT | PASSED | PASS | 12.89 | 12.24 | 2 | -5.0% | -5.2 | OPEN |
| 2026-07-23 | FRT | PASSED | PASS | 124.83 | 127.13 | 2 | +1.8% | +1.7 | OPEN |
| 2026-07-23 | HAS | PASSED | PASS | 87.35 | 90.61 | 2 | +3.7% | +3.6 | OPEN |
| 2026-07-23 | LHX | PASSED | REPAIR | 299.67 | 303.48 | 2 | +1.3% | +1.1 | OPEN |
| 2026-07-23 | MLI | PASSED | REPAIR | 63.13 | 64.17 | 2 | +1.6% | +1.5 | OPEN |
| 2026-07-23 | PFE | PASSED | REPAIR | 25.01 | 24.67 | 2 | -1.4% | -1.5 | OPEN |
| 2026-07-23 | SJM | PASSED | PASS | 115.71 | 121.05 | 2 | +4.6% | +4.5 | OPEN |
| 2026-07-23 | VZ | PASSED | REPAIR | 43.82 | 47.32 | 2 | +8.0% | +7.9 | OPEN |
| 2026-07-24 | ALSN | BLOCKED | PASS | 122.34 | 121.91 | 1 | -0.3% | -0.4 | OPEN |
| 2026-07-24 | AVT | BLOCKED | PASS | 89.42 | 88.38 | 1 | -1.2% | -1.2 | OPEN |
| 2026-07-24 | BUD | BLOCKED | REPAIR | 81.66 | 80.87 | 1 | -1.0% | -1.0 | OPEN |
| 2026-07-24 | CB | BLOCKED | PASS | 359.75 | 358.91 | 1 | -0.2% | -0.3 | OPEN |
| 2026-07-24 | CNP | BLOCKED | PASS | 44.56 | 44.01 | 1 | -1.2% | -1.3 | OPEN |
| 2026-07-24 | COST | BLOCKED | REPAIR | 935.03 | 951.58 | 1 | +1.8% | +1.8 | OPEN |
| 2026-07-24 | CRCL | BLOCKED | DEEP-FAIL | 62.36 | 65.67 | 1 | +5.3% | +5.3 | OPEN |
| 2026-07-24 | DE | BLOCKED | PASS | 628.16 | 625.02 | 1 | -0.5% | -0.5 | OPEN |
| 2026-07-24 | DGX | BLOCKED | PASS | 227.86 | 231.84 | 1 | +1.8% | +1.7 | OPEN |
| 2026-07-24 | DLR | BLOCKED | PASS | 199.08 | 195.76 | 1 | -1.7% | -1.7 | OPEN |
| 2026-07-24 | EGBN | BLOCKED | PASS | 28.44 | 28.15 | 1 | -1.0% | -1.0 | OPEN |
| 2026-07-24 | F | BLOCKED | REPAIR | 14.37 | 14.68 | 1 | +2.2% | +2.1 | OPEN |
| 2026-07-24 | FCX | BLOCKED | REPAIR | 62.6 | 62.72 | 1 | +0.2% | +0.2 | OPEN |
| 2026-07-24 | FUTU | BLOCKED | DEEP-FAIL | 99.36 | 104.27 | 1 | +4.9% | +4.9 | OPEN |
| 2026-07-24 | GDX | BLOCKED | DEEP-FAIL | 75.23 | 75.73 | 1 | +0.7% | +0.6 | OPEN |
| 2026-07-24 | GE | BLOCKED | PASS | 353.73 | 361.61 | 1 | +2.2% | +2.2 | OPEN |
| 2026-07-24 | GLD | BLOCKED | REPAIR | 371.9 | 374.63 | 1 | +0.7% | +0.7 | OPEN |
| 2026-07-24 | GM | BLOCKED | PASS | 82.64 | 87.04 | 1 | +5.3% | +5.3 | OPEN |
| 2026-07-24 | HON | BLOCKED | PASS | 243.15 | 245.75 | 1 | +1.1% | +1.1 | OPEN |
| 2026-07-24 | IRM | BLOCKED | PASS | 128.31 | 126.99 | 1 | -1.0% | -1.1 | OPEN |
| 2026-07-24 | JNJ | BLOCKED | PASS | 263.4 | 265.95 | 1 | +1.0% | +0.9 | OPEN |
| 2026-07-24 | LCID | BLOCKED | DEEP-FAIL | 6.3 | 6.5 | 1 | +3.2% | +3.1 | OPEN |
| 2026-07-24 | LDOS | BLOCKED | DEEP-FAIL | 112.14 | 114.95 | 1 | +2.5% | +2.5 | OPEN |
| 2026-07-24 | LIND | BLOCKED | PASS | 26.85 | 28.09 | 1 | +4.6% | +4.6 | OPEN |
| 2026-07-24 | M | BLOCKED | PASS | 23.38 | 24.96 | 1 | +6.8% | +6.7 | OPEN |
| 2026-07-24 | NEM | BLOCKED | REPAIR | 93.19 | 93.47 | 1 | +0.3% | +0.3 | OPEN |
| 2026-07-24 | ORKA | BLOCKED | PASS | 92.16 | 90.2 | 1 | -2.1% | -2.1 | OPEN |
| 2026-07-24 | PH | BLOCKED | PASS | 987.54 | 987.31 | 1 | -0.0% | -0.0 | OPEN |
| 2026-07-24 | PRLB | BLOCKED | PASS | 78.24 | 77.64 | 1 | -0.8% | -0.8 | OPEN |
| 2026-07-24 | ROP | BLOCKED | REPAIR | 367.34 | 375.02 | 1 | +2.1% | +2.1 | OPEN |
| 2026-07-24 | RSPU | BLOCKED | PASS | 82.33 | 81.24 | 1 | -1.3% | -1.4 | OPEN |
| 2026-07-24 | SMCI | BLOCKED | REPAIR | 30.1 | 29.81 | 1 | -1.0% | -1.0 | OPEN |
| 2026-07-24 | SON | BLOCKED | PASS | 58.23 | 58.68 | 1 | +0.8% | +0.8 | OPEN |
| 2026-07-24 | SPG | BLOCKED | PASS | 229.78 | 231.67 | 1 | +0.8% | +0.8 | OPEN |
| 2026-07-24 | TDY | BLOCKED | PASS | 655.35 | 651.65 | 1 | -0.6% | -0.6 | OPEN |
| 2026-07-24 | URA | BLOCKED | DEEP-FAIL | 39.89 | 40.32 | 1 | +1.1% | +1.1 | OPEN |
| 2026-07-24 | URI | BLOCKED | PASS | 1141.59 | 1127.91 | 1 | -1.2% | -1.2 | OPEN |
| 2026-07-24 | VST | BLOCKED | REPAIR | 163.38 | 157.08 | 1 | -3.9% | -3.9 | OPEN |
| 2026-07-24 | XLI | BLOCKED | PASS | 182.66 | 183.2 | 1 | +0.3% | +0.3 | OPEN |
| 2026-07-24 | ACTG | PASSED | PASS | 4.66 | 4.63 | 1 | -0.6% | -0.7 | OPEN |
| 2026-07-24 | DELL | PASSED | PASS | 437.5 | 426.91 | 1 | -2.4% | -2.4 | OPEN |
| 2026-07-24 | EQIX | PASSED | PASS | 1084.24 | 1046.79 | 1 | -3.5% | -3.5 | OPEN |
| 2026-07-24 | LHX | PASSED | REPAIR | 300.21 | 303.48 | 1 | +1.1% | +1.1 | OPEN |
| 2026-07-24 | MLI | PASSED | REPAIR | 63.91 | 64.17 | 1 | +0.4% | +0.4 | OPEN |
| 2026-07-24 | MRK | PASSED | PASS | 131.07 | 130.76 | 1 | -0.2% | -0.3 | OPEN |
| 2026-07-24 | RHP | PASSED | PASS | 133.09 | 134.94 | 1 | +1.4% | +1.4 | OPEN |
| 2026-07-24 | SJM | PASSED | PASS | 118.32 | 121.05 | 1 | +2.3% | +2.3 | OPEN |
| 2026-07-24 | VZ | PASSED | REPAIR | 46.38 | 47.32 | 1 | +2.0% | +2.0 | OPEN |

Open marks are not results. This file exists so that the cull the scan performs every night is measured instead of assumed.
