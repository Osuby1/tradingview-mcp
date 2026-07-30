# Gate stack forward grade

Does THE GATE STACK earn its keep? Every fresh Chandelier signal is graded forward from the CLOSE of its signal date over 21 trading sessions, bucketed by what the stack decided. The number that matters is the SPREAD.

- Signal events found: 438  |  priced: 355  |  unique symbol-cohort pairs (headline sample): 203
- Skipped (pre-2026-07-22 hand-written verdicts, not machine-comparable): 20

## Headline - all signals, deduped to first appearance

| Cohort | n | Win% | Mean | Median | Mean vs SPY | Mean worst drawdown |
|---|---|---|---|---|---|---|
| PASSED | 40 | 40% | -1.58% | -0.62% | +0.22% | -4.55% |
| BLOCKED | 163 | 48% | -1.02% | -0.55% | +0.97% | -5.31% |

**Spread (PASSED minus BLOCKED): -0.56 percentage points.**

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
| ADX FLOOR | 50 | 48% | -0.23% | -0.53% | +1.77% |
| ATR GEOMETRY | 6 | 17% | -5.58% | -5.24% | -4.10% |
| DIRECTION | 10 | 10% | -10.55% | -5.26% | -8.24% |
| LIQUIDITY | 1 | 0% | -9.96% | -9.96% | -7.56% |
| OTHER | 30 | 43% | +0.22% | -0.70% | +2.39% |
| REGIME | 18 | 61% | -0.59% | +1.12% | +1.16% |
| VOLATILITY CAP (ex 2:1) | 5 | 40% | -2.86% | -0.40% | -1.15% |
| ZLSMA | 43 | 63% | +0.28% | +0.77% | +2.25% |

## Shadow cohorts - the forbidden retro-tune, run forward instead

Would lowering the ADX floor to 18, or softening DEEP-FAIL, have helped? The replay's missed monsters make that tempting; answering it by re-running history is curve-fitting. These cohorts answer it FORWARD: sole-failure near-misses graded nightly against the PASSED cohort. Promotion bar (pre-registered): >=30 MATURED signals AND mean above PASSED's - then it goes to a Friday review, not before.

| Shadow cohort | n | Win% | Mean | Median | Mean vs SPY | PASSED mean (ref) |
|---|---|---|---|---|---|---|
| ADX 18-20, all else passed | 5 | 40% | +0.38% | -0.51% | +1.82% | -1.58% |
| DEEP-FAIL, all else passed | 2 | 100% | +2.73% | +2.73% | +4.01% | -1.58% |

## Every graded signal

| Date | Sym | Cohort | Regime | Entry | Mark | Days | Return | vs SPY | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | BG | BLOCKED | n/a | 120.49 | 107.78 | 7 | -10.6% | -8.8 | OPEN |
| 2026-07-20 | CHRD | BLOCKED | n/a | 128.8 | 136.47 | 7 | +6.0% | +7.7 | OPEN |
| 2026-07-20 | CNOB | BLOCKED | n/a | 33.46 | 32.79 | 7 | -2.0% | -0.3 | OPEN |
| 2026-07-20 | COCO | BLOCKED | PASS | 73.87 | 67.54 | 7 | -8.6% | -6.9 | OPEN |
| 2026-07-20 | CVNA | BLOCKED | DEEP-FAIL | 64.14 | 66.32 | 7 | +3.4% | +5.1 | OPEN |
| 2026-07-20 | FLG | BLOCKED | n/a | 14.84 | 14.08 | 7 | -5.1% | -3.4 | OPEN |
| 2026-07-20 | FNB | BLOCKED | n/a | 18.75 | 19.0 | 7 | +1.3% | +3.0 | OPEN |
| 2026-07-20 | HAS | BLOCKED | REPAIR | 81.59 | 95.17 | 7 | +16.6% | +18.4 | OPEN |
| 2026-07-20 | HLX | BLOCKED | n/a | 9.43 | 9.07 | 7 | -3.8% | -2.1 | OPEN |
| 2026-07-20 | LCID | BLOCKED | n/a | 7.11 | 7.96 | 7 | +11.9% | +13.7 | OPEN |
| 2026-07-20 | M | BLOCKED | REPAIR | 23.31 | 24.76 | 7 | +6.2% | +7.9 | OPEN |
| 2026-07-20 | NOV | BLOCKED | REPAIR | 19.55 | 19.06 | 7 | -2.5% | -0.8 | OPEN |
| 2026-07-20 | ODFL | BLOCKED | PASS | 231.76 | 222.79 | 7 | -3.9% | -2.2 | OPEN |
| 2026-07-20 | RYZ | BLOCKED | n/a | 29.07 | 28.79 | 7 | -1.0% | +0.7 | OPEN |
| 2026-07-20 | SHAK | BLOCKED | DEEP-FAIL | 56.97 | 63.05 | 7 | +10.7% | +12.4 | OPEN |
| 2026-07-20 | SPG | BLOCKED | PASS | 228.19 | 235.61 | 7 | +3.2% | +5.0 | OPEN |
| 2026-07-20 | TRNS | BLOCKED | n/a | 86.09 | 81.35 | 7 | -5.5% | -3.8 | OPEN |
| 2026-07-20 | VVV | BLOCKED | PASS | 39.54 | 39.65 | 7 | +0.3% | +2.0 | OPEN |
| 2026-07-20 | VZ | BLOCKED | REPAIR | 43.5 | 47.22 | 7 | +8.6% | +10.2 | OPEN |
| 2026-07-20 | WPC | BLOCKED | REPAIR | 75.17 | 74.71 | 7 | -0.6% | +1.1 | OPEN |
| 2026-07-21 | ALKS | BLOCKED | TAPE OK | 52.85 | 48.34 | 6 | -8.5% | -6.0 | OPEN |
| 2026-07-21 | ATLC | BLOCKED | TAPE OK | 96.37 | 104.13 | 6 | +8.1% | +10.6 | OPEN |
| 2026-07-21 | BRKR | BLOCKED | TAPE OK | 60.43 | 61.74 | 6 | +2.2% | +4.7 | OPEN |
| 2026-07-21 | CB | BLOCKED | TAPE OK | 354.8 | 361.9 | 6 | +2.0% | +4.5 | OPEN |
| 2026-07-21 | CBL | BLOCKED | TAPE OK | 55.53 | 59.32 | 6 | +6.8% | +9.3 | OPEN |
| 2026-07-21 | CNOB | BLOCKED | TAPE OK | 33.41 | 32.79 | 6 | -1.9% | +0.7 | OPEN |
| 2026-07-21 | COCO | BLOCKED | TAPE OK | 75.89 | 67.54 | 6 | -11.0% | -8.5 | OPEN |
| 2026-07-21 | CTRE | BLOCKED | TAPE OK | 43.4 | 42.34 | 6 | -2.4% | +0.1 | OPEN |
| 2026-07-21 | ESQ | BLOCKED | TAPE OK | 122.83 | 131.89 | 6 | +7.4% | +9.9 | OPEN |
| 2026-07-21 | EXTR | BLOCKED | TAPE OK | 30.44 | 29.07 | 6 | -4.5% | -2.0 | OPEN |
| 2026-07-21 | FFIV | BLOCKED | TAPE OK | 408.74 | 386.95 | 6 | -5.3% | -2.8 | OPEN |
| 2026-07-21 | FRT | BLOCKED | TAPE OK | 125.59 | 125.78 | 6 | +0.1% | +2.7 | OPEN |
| 2026-07-21 | HCSG | BLOCKED | TAPE OK | 24.8 | 23.43 | 6 | -5.5% | -3.0 | OPEN |
| 2026-07-21 | HELE | BLOCKED | TAPE OK | 27.28 | 28.15 | 6 | +3.2% | +5.7 | OPEN |
| 2026-07-21 | HOMB | BLOCKED | TAPE OK | 30.42 | 31.43 | 6 | +3.3% | +5.8 | OPEN |
| 2026-07-21 | LQDA | BLOCKED | TAPE OK | 80.89 | 86.82 | 6 | +7.3% | +9.8 | OPEN |
| 2026-07-21 | NVRI | BLOCKED | TAPE OK | 21.87 | 22.19 | 6 | +1.5% | +4.0 | OPEN |
| 2026-07-21 | NWPX | BLOCKED | TAPE OK | 135.41 | 123.21 | 6 | -9.0% | -6.5 | OPEN |
| 2026-07-21 | OSCR | BLOCKED | TAPE OK | 30.77 | 30.57 | 6 | -0.7% | +1.9 | OPEN |
| 2026-07-21 | PNC | BLOCKED | TAPE OK | 250.38 | 248.49 | 6 | -0.8% | +1.8 | OPEN |
| 2026-07-21 | SION | BLOCKED | TAPE OK | 47.21 | 44.81 | 6 | -5.1% | -2.6 | OPEN |
| 2026-07-21 | TBLA | BLOCKED | TAPE OK | 5.11 | 5.17 | 6 | +1.2% | +3.7 | OPEN |
| 2026-07-21 | TFIN | BLOCKED | TAPE OK | 79.19 | 75.89 | 6 | -4.2% | -1.6 | OPEN |
| 2026-07-21 | TGTX | BLOCKED | TAPE OK | 53.95 | 53.48 | 6 | -0.9% | +1.6 | OPEN |
| 2026-07-21 | TVTX | BLOCKED | TAPE OK | 56.58 | 55.56 | 6 | -1.8% | +0.7 | OPEN |
| 2026-07-21 | VCYT | BLOCKED | TAPE OK | 59.53 | 55.71 | 6 | -6.4% | -3.9 | OPEN |
| 2026-07-21 | ZD | BLOCKED | TAPE OK | 52.39 | 54.27 | 6 | +3.6% | +6.1 | OPEN |
| 2026-07-21 | CYRX | PASSED | TAPE OK | 16.24 | 14.93 | 6 | -8.1% | -5.5 | OPEN |
| 2026-07-21 | FLEX | PASSED | TAPE OK | 127.39 | 103.02 | 6 | -19.1% | -16.6 | OPEN |
| 2026-07-21 | GDX | PASSED | TAPE OK | 74.19 | 73.57 | 6 | -0.8% | +1.7 | OPEN |
| 2026-07-21 | HON | PASSED | TAPE OK | 229.86 | 241.12 | 6 | +4.9% | +7.4 | OPEN |
| 2026-07-21 | KWEB | PASSED | TAPE OK | 27.02 | 27.8 | 6 | +2.9% | +5.4 | OPEN |
| 2026-07-21 | MSFT | PASSED | TAPE OK | 397.75 | 390.54 | 6 | -1.8% | +0.7 | OPEN |
| 2026-07-21 | MU | PASSED | TAPE OK | 970.82 | 739.0 | 6 | -23.9% | -21.4 | OPEN |
| 2026-07-21 | NKE | PASSED | TAPE OK | 42.96 | 43.22 | 6 | +0.6% | +3.1 | OPEN |
| 2026-07-21 | PM | PASSED | TAPE OK | 188.04 | 198.44 | 6 | +5.5% | +8.1 | OPEN |
| 2026-07-21 | SKYY | PASSED | TAPE OK | 136.02 | 138.56 | 6 | +1.9% | +4.4 | OPEN |
| 2026-07-21 | SNOW | PASSED | TAPE OK | 271.73 | 282.9 | 6 | +4.1% | +6.6 | OPEN |
| 2026-07-22 | ACTG | BLOCKED | REPAIR | 4.57 | 4.52 | 5 | -1.1% | +1.3 | OPEN |
| 2026-07-22 | AMCR | BLOCKED | PASS | 43.21 | 45.84 | 5 | +6.1% | +8.5 | OPEN |
| 2026-07-22 | AMGN | BLOCKED | PASS | 366.05 | 387.64 | 5 | +5.9% | +8.3 | OPEN |
| 2026-07-22 | ASB | BLOCKED | PASS | 30.7 | 30.72 | 5 | +0.1% | +2.5 | OPEN |
| 2026-07-22 | BCBP | BLOCKED | REPAIR | 10.29 | 10.33 | 5 | +0.4% | +2.8 | OPEN |
| 2026-07-22 | BHP | BLOCKED | REPAIR | 84.54 | 83.11 | 5 | -1.7% | +0.7 | OPEN |
| 2026-07-22 | BHRB | BLOCKED | PASS | 71.01 | 73.63 | 5 | +3.7% | +6.1 | OPEN |
| 2026-07-22 | BX | BLOCKED | REPAIR | 122.82 | 129.4 | 5 | +5.4% | +7.8 | OPEN |
| 2026-07-22 | BY | BLOCKED | PASS | 37.75 | 39.15 | 5 | +3.7% | +6.1 | OPEN |
| 2026-07-22 | CBSH | BLOCKED | PASS | 58.7 | 60.33 | 5 | +2.8% | +5.2 | OPEN |
| 2026-07-22 | CCJ | BLOCKED | DEEP-FAIL | 90.37 | 84.57 | 5 | -6.4% | -4.0 | OPEN |
| 2026-07-22 | CMP | BLOCKED | REPAIR | 30.14 | 29.32 | 5 | -2.7% | -0.3 | OPEN |
| 2026-07-22 | CNOB | BLOCKED | PASS | 33.0 | 32.79 | 5 | -0.6% | +1.8 | OPEN |
| 2026-07-22 | COKE | BLOCKED | PASS | 184.36 | 192.39 | 5 | +4.4% | +6.8 | OPEN |
| 2026-07-22 | COLB | BLOCKED | PASS | 32.63 | 30.78 | 5 | -5.7% | -3.3 | OPEN |
| 2026-07-22 | COST | BLOCKED | REPAIR | 927.31 | 974.03 | 5 | +5.0% | +7.4 | OPEN |
| 2026-07-22 | CRCL | BLOCKED | DEEP-FAIL | 66.16 | 61.36 | 5 | -7.3% | -4.8 | OPEN |
| 2026-07-22 | DE | BLOCKED | PASS | 607.33 | 610.95 | 5 | +0.6% | +3.0 | OPEN |
| 2026-07-22 | DELL | BLOCKED | PASS | 441.8 | 369.64 | 5 | -16.3% | -13.9 | OPEN |
| 2026-07-22 | DIS | BLOCKED | REPAIR | 95.87 | 98.48 | 5 | +2.7% | +5.1 | OPEN |
| 2026-07-22 | EQR | BLOCKED | PASS | 68.29 | 68.85 | 5 | +0.8% | +3.2 | OPEN |
| 2026-07-22 | F | BLOCKED | PASS | 14.42 | 15.28 | 5 | +6.0% | +8.4 | OPEN |
| 2026-07-22 | FCX | BLOCKED | PASS | 65.0 | 59.99 | 5 | -7.7% | -5.3 | OPEN |
| 2026-07-22 | FHB | BLOCKED | PASS | 28.81 | 28.0 | 5 | -2.8% | -0.4 | OPEN |
| 2026-07-22 | FITB | BLOCKED | PASS | 57.67 | 56.57 | 5 | -1.9% | +0.5 | OPEN |
| 2026-07-22 | FLEX | BLOCKED | REPAIR | 127.0 | 103.02 | 5 | -18.9% | -16.5 | OPEN |
| 2026-07-22 | FLG | BLOCKED | PASS | 14.88 | 14.08 | 5 | -5.4% | -3.0 | OPEN |
| 2026-07-22 | FNB | BLOCKED | PASS | 18.86 | 19.0 | 5 | +0.7% | +3.1 | OPEN |
| 2026-07-22 | FRT | BLOCKED | PASS | 125.05 | 125.78 | 5 | +0.6% | +3.0 | OPEN |
| 2026-07-22 | GBCI | BLOCKED | PASS | 51.17 | 48.81 | 5 | -4.6% | -2.2 | OPEN |
| 2026-07-22 | GDX | BLOCKED | DEEP-FAIL | 76.68 | 73.57 | 5 | -4.1% | -1.6 | OPEN |
| 2026-07-22 | GLD | BLOCKED | REPAIR | 379.12 | 371.08 | 5 | -2.1% | +0.3 | OPEN |
| 2026-07-22 | GM | BLOCKED | PASS | 82.13 | 89.4 | 5 | +8.8% | +11.2 | OPEN |
| 2026-07-22 | HBNC | BLOCKED | PASS | 20.21 | 20.67 | 5 | +2.3% | +4.7 | OPEN |
| 2026-07-22 | HON | BLOCKED | PASS | 232.99 | 241.12 | 5 | +3.5% | +5.9 | OPEN |
| 2026-07-22 | HOPE | BLOCKED | PASS | 13.54 | 14.12 | 5 | +4.3% | +6.7 | OPEN |
| 2026-07-22 | HSIC | BLOCKED | PASS | 84.81 | 85.83 | 5 | +1.2% | +3.6 | OPEN |
| 2026-07-22 | HTZ | BLOCKED | DEEP-FAIL | 1.93 | 1.67 | 5 | -13.5% | -11.1 | OPEN |
| 2026-07-22 | KRE | BLOCKED | PASS | 75.6 | 76.18 | 5 | +0.8% | +3.2 | OPEN |
| 2026-07-22 | LCID | BLOCKED | DEEP-FAIL | 6.78 | 7.96 | 5 | +17.4% | +19.8 | OPEN |
| 2026-07-22 | LZB | BLOCKED | PASS | 39.3 | 40.93 | 5 | +4.2% | +6.5 | OPEN |
| 2026-07-22 | M | BLOCKED | PASS | 24.33 | 24.76 | 5 | +1.8% | +4.2 | OPEN |
| 2026-07-22 | MFA | BLOCKED | REPAIR | 9.29 | 9.17 | 5 | -1.3% | +1.1 | OPEN |
| 2026-07-22 | MU | BLOCKED | PASS | 959.48 | 739.0 | 5 | -23.0% | -20.6 | OPEN |
| 2026-07-22 | NEE | BLOCKED | PASS | 89.41 | 88.46 | 5 | -1.1% | +1.3 | OPEN |
| 2026-07-22 | NEM | BLOCKED | REPAIR | 95.75 | 91.34 | 5 | -4.6% | -2.2 | OPEN |
| 2026-07-22 | OCFC | BLOCKED | PASS | 19.67 | 19.73 | 5 | +0.3% | +2.7 | OPEN |
| 2026-07-22 | PANW | BLOCKED | PASS | 335.28 | 314.15 | 5 | -6.3% | -3.9 | OPEN |
| 2026-07-22 | PB | BLOCKED | PASS | 73.06 | 74.23 | 5 | +1.6% | +4.0 | OPEN |
| 2026-07-22 | PM | BLOCKED | PASS | 194.3 | 198.44 | 5 | +2.1% | +4.5 | OPEN |
| 2026-07-22 | POWL | BLOCKED | REPAIR | 240.68 | 186.39 | 5 | -22.6% | -20.2 | OPEN |
| 2026-07-22 | PRLB | BLOCKED | PASS | 79.73 | 71.35 | 5 | -10.5% | -8.1 | OPEN |
| 2026-07-22 | RACE | BLOCKED | REPAIR | 371.61 | 385.69 | 5 | +3.8% | +6.2 | OPEN |
| 2026-07-22 | RCL | BLOCKED | REPAIR | 285.85 | 323.58 | 5 | +13.2% | +15.6 | OPEN |
| 2026-07-22 | RSPU | BLOCKED | PASS | 81.85 | 79.85 | 5 | -2.5% | -0.1 | OPEN |
| 2026-07-22 | SAIC | BLOCKED | PASS | 115.95 | 117.01 | 5 | +0.9% | +3.3 | OPEN |
| 2026-07-22 | SJM | BLOCKED | PASS | 118.05 | 126.35 | 5 | +7.0% | +9.4 | OPEN |
| 2026-07-22 | SKK | BLOCKED | PASS | 5.22 | 4.7 | 5 | -10.0% | -7.6 | OPEN |
| 2026-07-22 | SMCI | BLOCKED | REPAIR | 30.56 | 25.7 | 5 | -15.9% | -13.5 | OPEN |
| 2026-07-22 | SON | BLOCKED | PASS | 55.15 | 58.98 | 5 | +6.9% | +9.3 | OPEN |
| 2026-07-22 | SPG | BLOCKED | PASS | 226.22 | 235.61 | 5 | +4.2% | +6.5 | OPEN |
| 2026-07-22 | SSB | BLOCKED | PASS | 102.19 | 105.71 | 5 | +3.4% | +5.8 | OPEN |
| 2026-07-22 | STRL | BLOCKED | REPAIR | 719.34 | 494.24 | 5 | -31.3% | -28.9 | OPEN |
| 2026-07-22 | STX | BLOCKED | PASS | 908.1 | 764.43 | 5 | -15.8% | -13.4 | OPEN |
| 2026-07-22 | TDY | BLOCKED | PASS | 650.5 | 631.35 | 5 | -2.9% | -0.5 | OPEN |
| 2026-07-22 | TPL | BLOCKED | PASS | 433.1 | 389.41 | 5 | -10.1% | -7.7 | OPEN |
| 2026-07-22 | TPR | BLOCKED | PASS | 143.73 | 150.11 | 5 | +4.4% | +6.8 | OPEN |
| 2026-07-22 | URA | BLOCKED | DEEP-FAIL | 40.97 | 37.52 | 5 | -8.4% | -6.0 | OPEN |
| 2026-07-22 | USB | BLOCKED | PASS | 64.47 | 62.82 | 5 | -2.6% | -0.2 | OPEN |
| 2026-07-22 | VST | BLOCKED | REPAIR | 166.74 | 142.81 | 5 | -14.3% | -11.9 | OPEN |
| 2026-07-22 | VVV | BLOCKED | PASS | 39.03 | 39.65 | 5 | +1.6% | +4.0 | OPEN |
| 2026-07-22 | CTRE | PASSED | PASS | 42.38 | 42.34 | 5 | -0.1% | +2.3 | OPEN |
| 2026-07-22 | PFE | PASSED | REPAIR | 24.82 | 25.15 | 5 | +1.3% | +3.7 | OPEN |
| 2026-07-22 | TJX | PASSED | REPAIR | 155.41 | 161.63 | 5 | +4.0% | +6.4 | OPEN |
| 2026-07-22 | TXNM | PASSED | REPAIR | 58.3 | 57.69 | 5 | -1.1% | +1.4 | OPEN |
| 2026-07-22 | VZ | PASSED | REPAIR | 44.29 | 47.22 | 5 | +6.6% | +9.0 | OPEN |
| 2026-07-23 | ACTG | BLOCKED | REPAIR | 4.62 | 4.52 | 4 | -2.2% | -1.0 | OPEN |
| 2026-07-23 | ALSN | BLOCKED | PASS | 119.64 | 114.66 | 4 | -4.2% | -3.0 | OPEN |
| 2026-07-23 | AVT | BLOCKED | PASS | 89.92 | 83.59 | 4 | -7.0% | -5.9 | OPEN |
| 2026-07-23 | BUD | BLOCKED | REPAIR | 80.48 | 84.87 | 4 | +5.5% | +6.6 | OPEN |
| 2026-07-23 | COST | BLOCKED | REPAIR | 926.06 | 974.03 | 4 | +5.2% | +6.4 | OPEN |
| 2026-07-23 | CRCL | BLOCKED | DEEP-FAIL | 62.18 | 61.36 | 4 | -1.3% | -0.1 | OPEN |
| 2026-07-23 | DELL | BLOCKED | PASS | 439.34 | 369.64 | 4 | -15.9% | -14.7 | OPEN |
| 2026-07-23 | DGX | BLOCKED | PASS | 227.9 | 235.22 | 4 | +3.2% | +4.4 | OPEN |
| 2026-07-23 | F | BLOCKED | REPAIR | 14.15 | 15.28 | 4 | +8.0% | +9.2 | OPEN |
| 2026-07-23 | FCX | BLOCKED | REPAIR | 63.5 | 59.99 | 4 | -5.5% | -4.3 | OPEN |
| 2026-07-23 | FLG | BLOCKED | PASS | 14.71 | 14.08 | 4 | -4.3% | -3.1 | OPEN |
| 2026-07-23 | FNB | BLOCKED | PASS | 18.87 | 19.0 | 4 | +0.7% | +1.9 | OPEN |
| 2026-07-23 | FUTU | BLOCKED | DEEP-FAIL | 98.96 | 101.88 | 4 | +3.0% | +4.1 | OPEN |
| 2026-07-23 | GDX | BLOCKED | DEEP-FAIL | 75.02 | 73.57 | 4 | -1.9% | -0.8 | OPEN |
| 2026-07-23 | GLD | BLOCKED | REPAIR | 371.52 | 371.08 | 4 | -0.1% | +1.1 | OPEN |
| 2026-07-23 | GM | BLOCKED | PASS | 80.67 | 89.4 | 4 | +10.8% | +12.0 | OPEN |
| 2026-07-23 | HON | BLOCKED | PASS | 246.27 | 241.12 | 4 | -2.1% | -0.9 | OPEN |
| 2026-07-23 | IRM | BLOCKED | REPAIR | 124.55 | 120.75 | 4 | -3.0% | -1.9 | OPEN |
| 2026-07-23 | LCID | BLOCKED | DEEP-FAIL | 6.45 | 7.96 | 4 | +23.4% | +24.6 | OPEN |
| 2026-07-23 | LSTR | BLOCKED | PASS | 207.97 | 177.83 | 4 | -14.5% | -13.3 | OPEN |
| 2026-07-23 | M | BLOCKED | PASS | 23.33 | 24.76 | 4 | +6.1% | +7.3 | OPEN |
| 2026-07-23 | MAC | BLOCKED | PASS | 25.3 | 26.09 | 4 | +3.1% | +4.3 | OPEN |
| 2026-07-23 | NEM | BLOCKED | REPAIR | 94.72 | 91.34 | 4 | -3.6% | -2.4 | OPEN |
| 2026-07-23 | PLD | BLOCKED | PASS | 145.12 | 145.47 | 4 | +0.2% | +1.4 | OPEN |
| 2026-07-23 | PRLB | BLOCKED | PASS | 78.62 | 71.35 | 4 | -9.2% | -8.1 | OPEN |
| 2026-07-23 | RHP | BLOCKED | PASS | 128.89 | 135.57 | 4 | +5.2% | +6.4 | OPEN |
| 2026-07-23 | SMCI | BLOCKED | REPAIR | 31.2 | 25.7 | 4 | -17.6% | -16.4 | OPEN |
| 2026-07-23 | SON | BLOCKED | PASS | 56.32 | 58.98 | 4 | +4.7% | +5.9 | OPEN |
| 2026-07-23 | SPG | BLOCKED | PASS | 225.2 | 235.61 | 4 | +4.6% | +5.8 | OPEN |
| 2026-07-23 | TDY | BLOCKED | PASS | 651.22 | 631.35 | 4 | -3.0% | -1.9 | OPEN |
| 2026-07-23 | URA | BLOCKED | DEEP-FAIL | 41.13 | 37.52 | 4 | -8.8% | -7.6 | OPEN |
| 2026-07-23 | URI | BLOCKED | PASS | 1139.71 | 1055.11 | 4 | -7.4% | -6.2 | OPEN |
| 2026-07-23 | VST | BLOCKED | REPAIR | 168.98 | 142.81 | 4 | -15.5% | -14.3 | OPEN |
| 2026-07-23 | VVV | BLOCKED | PASS | 38.31 | 39.65 | 4 | +3.5% | +4.7 | OPEN |
| 2026-07-23 | ECVT | PASSED | PASS | 12.89 | 12.03 | 4 | -6.7% | -5.5 | OPEN |
| 2026-07-23 | FRT | PASSED | PASS | 124.83 | 125.78 | 4 | +0.8% | +1.9 | OPEN |
| 2026-07-23 | HAS | PASSED | PASS | 87.35 | 95.17 | 4 | +8.9% | +10.1 | OPEN |
| 2026-07-23 | LHX | PASSED | REPAIR | 299.67 | 297.53 | 4 | -0.7% | +0.5 | OPEN |
| 2026-07-23 | MLI | PASSED | REPAIR | 63.13 | 65.4 | 4 | +3.6% | +4.8 | OPEN |
| 2026-07-23 | PFE | PASSED | REPAIR | 25.01 | 25.15 | 4 | +0.6% | +1.7 | OPEN |
| 2026-07-23 | SJM | PASSED | PASS | 115.71 | 126.35 | 4 | +9.2% | +10.4 | OPEN |
| 2026-07-23 | VZ | PASSED | REPAIR | 43.82 | 47.22 | 4 | +7.8% | +8.9 | OPEN |
| 2026-07-24 | ALSN | BLOCKED | PASS | 122.34 | 114.66 | 3 | -6.3% | -5.0 | OPEN |
| 2026-07-24 | AVT | BLOCKED | PASS | 89.42 | 83.59 | 3 | -6.5% | -5.2 | OPEN |
| 2026-07-24 | BUD | BLOCKED | REPAIR | 81.66 | 84.87 | 3 | +3.9% | +5.2 | OPEN |
| 2026-07-24 | CB | BLOCKED | PASS | 359.75 | 361.9 | 3 | +0.6% | +1.9 | OPEN |
| 2026-07-24 | CNP | BLOCKED | PASS | 44.56 | 42.93 | 3 | -3.7% | -2.4 | OPEN |
| 2026-07-24 | COST | BLOCKED | REPAIR | 935.03 | 974.03 | 3 | +4.2% | +5.5 | OPEN |
| 2026-07-24 | CRCL | BLOCKED | DEEP-FAIL | 62.36 | 61.36 | 3 | -1.6% | -0.3 | OPEN |
| 2026-07-24 | DE | BLOCKED | PASS | 628.16 | 610.95 | 3 | -2.7% | -1.5 | OPEN |
| 2026-07-24 | DGX | BLOCKED | PASS | 227.86 | 235.22 | 3 | +3.2% | +4.5 | OPEN |
| 2026-07-24 | DLR | BLOCKED | PASS | 199.08 | 188.18 | 3 | -5.5% | -4.2 | OPEN |
| 2026-07-24 | EGBN | BLOCKED | PASS | 28.44 | 27.89 | 3 | -1.9% | -0.7 | OPEN |
| 2026-07-24 | F | BLOCKED | REPAIR | 14.37 | 15.28 | 3 | +6.3% | +7.6 | OPEN |
| 2026-07-24 | FCX | BLOCKED | REPAIR | 62.6 | 59.99 | 3 | -4.2% | -2.9 | OPEN |
| 2026-07-24 | FUTU | BLOCKED | DEEP-FAIL | 99.36 | 101.88 | 3 | +2.5% | +3.8 | OPEN |
| 2026-07-24 | GDX | BLOCKED | DEEP-FAIL | 75.23 | 73.57 | 3 | -2.2% | -0.9 | OPEN |
| 2026-07-24 | GE | BLOCKED | PASS | 353.73 | 350.63 | 3 | -0.9% | +0.4 | OPEN |
| 2026-07-24 | GLD | BLOCKED | REPAIR | 371.9 | 371.08 | 3 | -0.2% | +1.1 | OPEN |
| 2026-07-24 | GM | BLOCKED | PASS | 82.64 | 89.4 | 3 | +8.2% | +9.5 | OPEN |
| 2026-07-24 | HON | BLOCKED | PASS | 243.15 | 241.12 | 3 | -0.8% | +0.5 | OPEN |
| 2026-07-24 | IRM | BLOCKED | PASS | 128.31 | 120.75 | 3 | -5.9% | -4.6 | OPEN |
| 2026-07-24 | JNJ | BLOCKED | PASS | 263.4 | 265.53 | 3 | +0.8% | +2.1 | OPEN |
| 2026-07-24 | LCID | BLOCKED | DEEP-FAIL | 6.3 | 7.96 | 3 | +26.4% | +27.6 | OPEN |
| 2026-07-24 | LDOS | BLOCKED | DEEP-FAIL | 112.14 | 114.37 | 3 | +2.0% | +3.3 | OPEN |
| 2026-07-24 | LIND | BLOCKED | PASS | 26.85 | 29.75 | 3 | +10.8% | +12.1 | OPEN |
| 2026-07-24 | M | BLOCKED | PASS | 23.38 | 24.76 | 3 | +5.9% | +7.2 | OPEN |
| 2026-07-24 | NEM | BLOCKED | REPAIR | 93.19 | 91.34 | 3 | -2.0% | -0.7 | OPEN |
| 2026-07-24 | ORKA | BLOCKED | PASS | 92.16 | 88.07 | 3 | -4.4% | -3.2 | OPEN |
| 2026-07-24 | PH | BLOCKED | PASS | 987.54 | 951.07 | 3 | -3.7% | -2.4 | OPEN |
| 2026-07-24 | PRLB | BLOCKED | PASS | 78.24 | 71.35 | 3 | -8.8% | -7.5 | OPEN |
| 2026-07-24 | ROP | BLOCKED | REPAIR | 367.34 | 408.07 | 3 | +11.1% | +12.4 | OPEN |
| 2026-07-24 | RSPU | BLOCKED | PASS | 82.33 | 79.85 | 3 | -3.0% | -1.7 | OPEN |
| 2026-07-24 | SMCI | BLOCKED | REPAIR | 30.1 | 25.7 | 3 | -14.6% | -13.3 | OPEN |
| 2026-07-24 | SON | BLOCKED | PASS | 58.23 | 58.98 | 3 | +1.3% | +2.6 | OPEN |
| 2026-07-24 | SPG | BLOCKED | PASS | 229.78 | 235.61 | 3 | +2.5% | +3.8 | OPEN |
| 2026-07-24 | TDY | BLOCKED | PASS | 655.35 | 631.35 | 3 | -3.7% | -2.4 | OPEN |
| 2026-07-24 | URA | BLOCKED | DEEP-FAIL | 39.89 | 37.52 | 3 | -5.9% | -4.7 | OPEN |
| 2026-07-24 | URI | BLOCKED | PASS | 1141.59 | 1055.11 | 3 | -7.6% | -6.3 | OPEN |
| 2026-07-24 | VST | BLOCKED | REPAIR | 163.38 | 142.81 | 3 | -12.6% | -11.3 | OPEN |
| 2026-07-24 | XLI | BLOCKED | PASS | 182.66 | 176.66 | 3 | -3.3% | -2.0 | OPEN |
| 2026-07-24 | ACTG | PASSED | PASS | 4.66 | 4.52 | 3 | -3.0% | -1.7 | OPEN |
| 2026-07-24 | DELL | PASSED | PASS | 437.5 | 369.64 | 3 | -15.5% | -14.2 | OPEN |
| 2026-07-24 | EQIX | PASSED | PASS | 1084.24 | 1008.02 | 3 | -7.0% | -5.8 | OPEN |
| 2026-07-24 | LHX | PASSED | REPAIR | 300.21 | 297.53 | 3 | -0.9% | +0.4 | OPEN |
| 2026-07-24 | MLI | PASSED | REPAIR | 63.91 | 65.4 | 3 | +2.3% | +3.6 | OPEN |
| 2026-07-24 | MRK | PASSED | PASS | 131.07 | 130.36 | 3 | -0.5% | +0.7 | OPEN |
| 2026-07-24 | RHP | PASSED | PASS | 133.09 | 135.57 | 3 | +1.9% | +3.1 | OPEN |
| 2026-07-24 | SJM | PASSED | PASS | 118.32 | 126.35 | 3 | +6.8% | +8.1 | OPEN |
| 2026-07-24 | VZ | PASSED | REPAIR | 46.38 | 47.22 | 3 | +1.8% | +3.1 | OPEN |
| 2026-07-27 | ACGL | BLOCKED | PASS | 103.88 | 104.55 | 2 | +0.6% | +1.9 | OPEN |
| 2026-07-27 | ALSN | BLOCKED | PASS | 121.91 | 114.66 | 2 | -6.0% | -4.6 | OPEN |
| 2026-07-27 | AVT | BLOCKED | PASS | 88.38 | 83.59 | 2 | -5.4% | -4.1 | OPEN |
| 2026-07-27 | BUD | BLOCKED | REPAIR | 80.87 | 84.87 | 2 | +5.0% | +6.2 | OPEN |
| 2026-07-27 | CB | BLOCKED | PASS | 358.91 | 361.9 | 2 | +0.8% | +2.1 | OPEN |
| 2026-07-27 | CPRT | BLOCKED | DEEP-FAIL | 29.79 | 30.82 | 2 | +3.5% | +4.8 | OPEN |
| 2026-07-27 | CRCL | BLOCKED | DEEP-FAIL | 65.67 | 61.36 | 2 | -6.6% | -5.3 | OPEN |
| 2026-07-27 | DE | BLOCKED | PASS | 625.02 | 610.95 | 2 | -2.2% | -0.9 | OPEN |
| 2026-07-27 | DLR | BLOCKED | PASS | 195.76 | 188.18 | 2 | -3.9% | -2.6 | OPEN |
| 2026-07-27 | EGBN | BLOCKED | PASS | 28.15 | 27.89 | 2 | -0.9% | +0.4 | OPEN |
| 2026-07-27 | F | BLOCKED | PASS | 14.68 | 15.28 | 2 | +4.1% | +5.4 | OPEN |
| 2026-07-27 | FCX | BLOCKED | REPAIR | 62.72 | 59.99 | 2 | -4.3% | -3.0 | OPEN |
| 2026-07-27 | FUTU | BLOCKED | DEEP-FAIL | 104.27 | 101.88 | 2 | -2.3% | -1.0 | OPEN |
| 2026-07-27 | GDX | BLOCKED | DEEP-FAIL | 75.73 | 73.57 | 2 | -2.9% | -1.6 | OPEN |
| 2026-07-27 | GLD | BLOCKED | REPAIR | 374.63 | 371.08 | 2 | -0.9% | +0.4 | OPEN |
| 2026-07-27 | GM | BLOCKED | PASS | 87.04 | 89.4 | 2 | +2.7% | +4.0 | OPEN |
| 2026-07-27 | HON | BLOCKED | PASS | 245.75 | 241.12 | 2 | -1.9% | -0.6 | OPEN |
| 2026-07-27 | IRM | BLOCKED | PASS | 126.99 | 120.75 | 2 | -4.9% | -3.6 | OPEN |
| 2026-07-27 | LDOS | BLOCKED | DEEP-FAIL | 114.95 | 114.37 | 2 | -0.5% | +0.8 | OPEN |
| 2026-07-27 | LIND | BLOCKED | PASS | 28.09 | 29.75 | 2 | +5.9% | +7.2 | OPEN |
| 2026-07-27 | MAR | BLOCKED | PASS | 383.06 | 381.12 | 2 | -0.5% | +0.8 | OPEN |
| 2026-07-27 | NEM | BLOCKED | REPAIR | 93.47 | 91.34 | 2 | -2.3% | -1.0 | OPEN |
| 2026-07-27 | ORKA | BLOCKED | PASS | 90.2 | 88.07 | 2 | -2.4% | -1.1 | OPEN |
| 2026-07-27 | PGR | BLOCKED | REPAIR | 215.76 | 219.99 | 2 | +2.0% | +3.3 | OPEN |
| 2026-07-27 | PH | BLOCKED | PASS | 987.31 | 951.07 | 2 | -3.7% | -2.4 | OPEN |
| 2026-07-27 | PRLB | BLOCKED | PASS | 77.64 | 71.35 | 2 | -8.1% | -6.8 | OPEN |
| 2026-07-27 | RCL | BLOCKED | REPAIR | 305.04 | 323.58 | 2 | +6.1% | +7.4 | OPEN |
| 2026-07-27 | ROP | BLOCKED | REPAIR | 375.02 | 408.07 | 2 | +8.8% | +10.1 | OPEN |
| 2026-07-27 | RSPU | BLOCKED | PASS | 81.24 | 79.85 | 2 | -1.7% | -0.4 | OPEN |
| 2026-07-27 | SLB | BLOCKED | PASS | 51.53 | 48.96 | 2 | -5.0% | -3.7 | OPEN |
| 2026-07-27 | SMCI | BLOCKED | DEEP-FAIL | 29.81 | 25.7 | 2 | -13.8% | -12.5 | OPEN |
| 2026-07-27 | SON | BLOCKED | PASS | 58.68 | 58.98 | 2 | +0.5% | +1.8 | OPEN |
| 2026-07-27 | TDY | BLOCKED | PASS | 651.65 | 631.35 | 2 | -3.1% | -1.8 | OPEN |
| 2026-07-27 | TJX | BLOCKED | REPAIR | 156.38 | 161.63 | 2 | +3.4% | +4.7 | OPEN |
| 2026-07-27 | URA | BLOCKED | DEEP-FAIL | 40.32 | 37.52 | 2 | -6.9% | -5.6 | OPEN |
| 2026-07-27 | VRSN | BLOCKED | REPAIR | 274.82 | 290.92 | 2 | +5.9% | +7.2 | OPEN |
| 2026-07-27 | VST | BLOCKED | REPAIR | 157.08 | 142.81 | 2 | -9.1% | -7.8 | OPEN |
| 2026-07-27 | WWD | BLOCKED | PASS | 419.76 | 385.42 | 2 | -8.2% | -6.9 | OPEN |
| 2026-07-27 | XLI | BLOCKED | PASS | 183.2 | 176.66 | 2 | -3.6% | -2.3 | OPEN |
| 2026-07-27 | ACTG | PASSED | PASS | 4.63 | 4.52 | 2 | -2.4% | -1.1 | OPEN |
| 2026-07-27 | DELL | PASSED | PASS | 426.91 | 369.64 | 2 | -13.4% | -12.1 | OPEN |
| 2026-07-27 | DGX | PASSED | PASS | 231.84 | 235.22 | 2 | +1.5% | +2.8 | OPEN |
| 2026-07-27 | EQIX | PASSED | PASS | 1046.79 | 1008.02 | 2 | -3.7% | -2.4 | OPEN |
| 2026-07-27 | GE | PASSED | PASS | 361.61 | 350.63 | 2 | -3.0% | -1.7 | OPEN |
| 2026-07-27 | JNJ | PASSED | PASS | 265.95 | 265.53 | 2 | -0.2% | +1.1 | OPEN |
| 2026-07-27 | LHX | PASSED | REPAIR | 303.48 | 297.53 | 2 | -2.0% | -0.7 | OPEN |
| 2026-07-27 | MLI | PASSED | PASS | 64.17 | 65.4 | 2 | +1.9% | +3.2 | OPEN |
| 2026-07-27 | MRK | PASSED | PASS | 130.76 | 130.36 | 2 | -0.3% | +1.0 | OPEN |
| 2026-07-27 | RHP | PASSED | PASS | 134.94 | 135.57 | 2 | +0.5% | +1.8 | OPEN |
| 2026-07-27 | SJM | PASSED | PASS | 121.05 | 126.35 | 2 | +4.4% | +5.7 | OPEN |
| 2026-07-27 | URI | PASSED | PASS | 1127.91 | 1055.11 | 2 | -6.5% | -5.2 | OPEN |
| 2026-07-28 | ACGL | BLOCKED | PASS | 106.48 | 104.55 | 1 | -1.8% | -0.3 | OPEN |
| 2026-07-28 | AGNC | BLOCKED | PASS | 11.07 | 10.9 | 1 | -1.5% | +0.0 | OPEN |
| 2026-07-28 | AI | BLOCKED | DEEP-FAIL | 8.9 | 8.85 | 1 | -0.6% | +1.0 | OPEN |
| 2026-07-28 | AJG | BLOCKED | REPAIR | 265.31 | 268.91 | 1 | +1.4% | +2.9 | OPEN |
| 2026-07-28 | ALSN | BLOCKED | PASS | 121.11 | 114.66 | 1 | -5.3% | -3.8 | OPEN |
| 2026-07-28 | AVT | BLOCKED | REPAIR | 86.22 | 83.59 | 1 | -3.0% | -1.5 | OPEN |
| 2026-07-28 | AXON | BLOCKED | REPAIR | 547.65 | 531.2 | 1 | -3.0% | -1.5 | OPEN |
| 2026-07-28 | BUD | BLOCKED | PASS | 83.2 | 84.87 | 1 | +2.0% | +3.5 | OPEN |
| 2026-07-28 | CB | BLOCKED | PASS | 363.5 | 361.9 | 1 | -0.4% | +1.1 | OPEN |
| 2026-07-28 | CCL | BLOCKED | REPAIR | 28.23 | 27.81 | 1 | -1.5% | +0.1 | OPEN |
| 2026-07-28 | CHTR | BLOCKED | DEEP-FAIL | 139.97 | 145.2 | 1 | +3.7% | +5.3 | OPEN |
| 2026-07-28 | CLX | BLOCKED | REPAIR | 100.32 | 99.63 | 1 | -0.7% | +0.8 | OPEN |
| 2026-07-28 | CNP | BLOCKED | PASS | 44.1 | 42.93 | 1 | -2.6% | -1.1 | OPEN |
| 2026-07-28 | COKE | BLOCKED | PASS | 195.0 | 192.39 | 1 | -1.3% | +0.2 | OPEN |
| 2026-07-28 | CPRT | BLOCKED | DEEP-FAIL | 30.69 | 30.82 | 1 | +0.4% | +2.0 | OPEN |
| 2026-07-28 | CRCL | BLOCKED | DEEP-FAIL | 64.32 | 61.36 | 1 | -4.6% | -3.1 | OPEN |
| 2026-07-28 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.66 | 1 | -6.2% | -4.7 | OPEN |
| 2026-07-28 | DASH | BLOCKED | REPAIR | 195.52 | 193.53 | 1 | -1.0% | +0.5 | OPEN |
| 2026-07-28 | DUOL | BLOCKED | REPAIR | 140.73 | 140.17 | 1 | -0.4% | +1.1 | OPEN |
| 2026-07-28 | EGBN | BLOCKED | PASS | 28.39 | 27.89 | 1 | -1.8% | -0.2 | OPEN |
| 2026-07-28 | ERIE | BLOCKED | REPAIR | 242.43 | 248.55 | 1 | +2.5% | +4.1 | OPEN |
| 2026-07-28 | F | BLOCKED | PASS | 14.96 | 15.28 | 1 | +2.1% | +3.7 | OPEN |
| 2026-07-28 | FCX | BLOCKED | REPAIR | 61.64 | 59.99 | 1 | -2.7% | -1.1 | OPEN |
| 2026-07-28 | FUTU | BLOCKED | DEEP-FAIL | 101.84 | 101.88 | 1 | +0.0% | +1.6 | OPEN |
| 2026-07-28 | GDX | BLOCKED | DEEP-FAIL | 74.21 | 73.57 | 1 | -0.9% | +0.7 | OPEN |
| 2026-07-28 | GLD | BLOCKED | DEEP-FAIL | 369.37 | 371.08 | 1 | +0.5% | +2.0 | OPEN |
| 2026-07-28 | GM | BLOCKED | PASS | 90.3 | 89.4 | 1 | -1.0% | +0.5 | OPEN |
| 2026-07-28 | HD | BLOCKED | REPAIR | 344.47 | 338.27 | 1 | -1.8% | -0.3 | OPEN |
| 2026-07-28 | JETS | BLOCKED | PASS | 31.86 | 30.97 | 1 | -2.8% | -1.2 | OPEN |
| 2026-07-28 | LDOS | BLOCKED | DEEP-FAIL | 118.36 | 114.37 | 1 | -3.4% | -1.8 | OPEN |
| 2026-07-28 | LOW | BLOCKED | REPAIR | 218.24 | 215.68 | 1 | -1.2% | +0.4 | OPEN |
| 2026-07-28 | LZB | BLOCKED | PASS | 41.3 | 40.93 | 1 | -0.9% | +0.6 | OPEN |
| 2026-07-28 | MAR | BLOCKED | PASS | 383.52 | 381.12 | 1 | -0.6% | +0.9 | OPEN |
| 2026-07-28 | MCD | BLOCKED | REPAIR | 273.02 | 271.52 | 1 | -0.6% | +1.0 | OPEN |
| 2026-07-28 | MDT | BLOCKED | REPAIR | 86.88 | 87.54 | 1 | +0.8% | +2.3 | OPEN |
| 2026-07-28 | NCLH | BLOCKED | REPAIR | 21.22 | 20.75 | 1 | -2.2% | -0.7 | OPEN |
| 2026-07-28 | NEM | BLOCKED | DEEP-FAIL | 91.52 | 91.34 | 1 | -0.2% | +1.3 | OPEN |
| 2026-07-28 | NFLX | BLOCKED | DEEP-FAIL | 72.39 | 73.63 | 1 | +1.7% | +3.2 | OPEN |
| 2026-07-28 | NOW | BLOCKED | DEEP-FAIL | 110.62 | 115.76 | 1 | +4.7% | +6.2 | OPEN |
| 2026-07-28 | PGR | BLOCKED | REPAIR | 219.52 | 219.99 | 1 | +0.2% | +1.8 | OPEN |
| 2026-07-28 | PH | BLOCKED | PASS | 990.96 | 951.07 | 1 | -4.0% | -2.5 | OPEN |
| 2026-07-28 | RACE | BLOCKED | REPAIR | 390.14 | 385.69 | 1 | -1.1% | +0.4 | OPEN |
| 2026-07-28 | RCL | BLOCKED | REPAIR | 322.5 | 323.58 | 1 | +0.3% | +1.9 | OPEN |
| 2026-07-28 | RMD | BLOCKED | DEEP-FAIL | 208.96 | 214.29 | 1 | +2.5% | +4.1 | OPEN |
| 2026-07-28 | ROP | BLOCKED | REPAIR | 390.92 | 408.07 | 1 | +4.4% | +5.9 | OPEN |
| 2026-07-28 | RSPU | BLOCKED | PASS | 81.03 | 79.85 | 1 | -1.5% | +0.1 | OPEN |
| 2026-07-28 | SHAK | BLOCKED | DEEP-FAIL | 63.2 | 63.05 | 1 | -0.2% | +1.3 | OPEN |
| 2026-07-28 | SHW | BLOCKED | REPAIR | 354.27 | 343.88 | 1 | -2.9% | -1.4 | OPEN |
| 2026-07-28 | SMCI | BLOCKED | DEEP-FAIL | 28.45 | 25.7 | 1 | -9.7% | -8.1 | OPEN |
| 2026-07-28 | SON | BLOCKED | PASS | 60.56 | 58.98 | 1 | -2.6% | -1.1 | OPEN |
| 2026-07-28 | STGW | BLOCKED | PASS | 7.97 | 8.08 | 1 | +1.4% | +2.9 | OPEN |
| 2026-07-28 | TDY | BLOCKED | PASS | 649.67 | 631.35 | 1 | -2.8% | -1.3 | OPEN |
| 2026-07-28 | TOST | BLOCKED | REPAIR | 32.34 | 32.6 | 1 | +0.8% | +2.3 | OPEN |
| 2026-07-28 | TPR | BLOCKED | PASS | 150.9 | 150.11 | 1 | -0.5% | +1.0 | OPEN |
| 2026-07-28 | TYL | BLOCKED | DEEP-FAIL | 333.35 | 333.5 | 1 | +0.0% | +1.6 | OPEN |
| 2026-07-28 | URA | BLOCKED | DEEP-FAIL | 38.95 | 37.52 | 1 | -3.7% | -2.1 | OPEN |
| 2026-07-28 | URI | BLOCKED | PASS | 1091.26 | 1055.11 | 1 | -3.3% | -1.8 | OPEN |
| 2026-07-28 | VRSN | BLOCKED | REPAIR | 281.15 | 290.92 | 1 | +3.5% | +5.0 | OPEN |
| 2026-07-28 | WWD | BLOCKED | PASS | 410.55 | 385.42 | 1 | -6.1% | -4.6 | OPEN |
| 2026-07-28 | XLI | BLOCKED | PASS | 182.49 | 176.66 | 1 | -3.2% | -1.7 | OPEN |
| 2026-07-28 | ZTS | BLOCKED | DEEP-FAIL | 77.51 | 77.93 | 1 | +0.5% | +2.1 | OPEN |
| 2026-07-28 | ACTG | PASSED | PASS | 4.63 | 4.52 | 1 | -2.4% | -0.8 | OPEN |
| 2026-07-28 | CTS | PASSED | PASS | 64.82 | 61.53 | 1 | -5.1% | -3.5 | OPEN |
| 2026-07-28 | DAL | PASSED | PASS | 89.37 | 86.25 | 1 | -3.5% | -1.9 | OPEN |
| 2026-07-28 | DE | PASSED | PASS | 639.84 | 610.95 | 1 | -4.5% | -3.0 | OPEN |
| 2026-07-28 | DGX | PASSED | PASS | 235.94 | 235.22 | 1 | -0.3% | +1.2 | OPEN |
| 2026-07-28 | DLR | PASSED | PASS | 193.18 | 188.18 | 1 | -2.6% | -1.1 | OPEN |
| 2026-07-28 | EQIX | PASSED | REPAIR | 1034.86 | 1008.02 | 1 | -2.6% | -1.1 | OPEN |
| 2026-07-28 | GE | PASSED | PASS | 363.59 | 350.63 | 1 | -3.6% | -2.0 | OPEN |
| 2026-07-28 | HON | PASSED | PASS | 247.05 | 241.12 | 1 | -2.4% | -0.9 | OPEN |
| 2026-07-28 | JNJ | PASSED | PASS | 266.73 | 265.53 | 1 | -0.5% | +1.1 | OPEN |
| 2026-07-28 | LHX | PASSED | REPAIR | 305.2 | 297.53 | 1 | -2.5% | -1.0 | OPEN |
| 2026-07-28 | LLY | PASSED | PASS | 1220.66 | 1210.02 | 1 | -0.9% | +0.7 | OPEN |
| 2026-07-28 | MLI | PASSED | PASS | 66.49 | 65.4 | 1 | -1.6% | -0.1 | OPEN |
| 2026-07-28 | MNST | PASSED | PASS | 97.74 | 97.23 | 1 | -0.5% | +1.0 | OPEN |
| 2026-07-28 | MRK | PASSED | PASS | 131.82 | 130.36 | 1 | -1.1% | +0.4 | OPEN |
| 2026-07-28 | PEP | PASSED | REPAIR | 142.86 | 143.5 | 1 | +0.5% | +2.0 | OPEN |
| 2026-07-28 | SLB | PASSED | REPAIR | 49.98 | 48.96 | 1 | -2.0% | -0.5 | OPEN |
| 2026-07-28 | SSD | PASSED | PASS | 198.28 | 189.48 | 1 | -4.4% | -2.9 | OPEN |
| 2026-07-28 | TJX | PASSED | PASS | 160.8 | 161.63 | 1 | +0.5% | +2.0 | OPEN |

Open marks are not results. This file exists so that the cull the scan performs every night is measured instead of assumed.
