# Gate stack forward grade

Does THE GATE STACK earn its keep? Every fresh Chandelier signal is graded forward from the CLOSE of its signal date over 21 trading sessions, bucketed by what the stack decided. The number that matters is the SPREAD.

- Signal events found: 355  |  priced: 275  |  unique symbol-cohort pairs (headline sample): 169
- Skipped (pre-2026-07-22 hand-written verdicts, not machine-comparable): 20

## Headline - all signals, deduped to first appearance

| Cohort | n | Win% | Mean | Median | Mean vs SPY | Mean worst drawdown |
|---|---|---|---|---|---|---|
| PASSED | 31 | 65% | +0.10% | +0.57% | +0.45% | -4.35% |
| BLOCKED | 138 | 57% | +0.42% | +1.04% | +0.96% | -4.81% |

**Spread (PASSED minus BLOCKED): -0.32 percentage points.**

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
| ADX FLOOR | 44 | 61% | +1.12% | +1.27% | +1.65% |
| ATR GEOMETRY | 5 | 20% | -2.72% | -3.01% | -2.79% |
| DIRECTION | 9 | 22% | -8.45% | -5.17% | -7.57% |
| LIQUIDITY | 1 | 0% | -8.81% | -8.81% | -7.94% |
| OTHER | 30 | 57% | +1.92% | +0.54% | +2.55% |
| REGIME | 10 | 50% | +0.22% | +0.07% | +0.60% |
| VOLATILITY CAP (ex 2:1) | 1 | 0% | -11.25% | -11.25% | -10.37% |
| ZLSMA | 38 | 68% | +1.52% | +1.62% | +2.03% |

## Shadow cohorts - the forbidden retro-tune, run forward instead

Would lowering the ADX floor to 18, or softening DEEP-FAIL, have helped? The replay's missed monsters make that tempting; answering it by re-running history is curve-fitting. These cohorts answer it FORWARD: sole-failure near-misses graded nightly against the PASSED cohort. Promotion bar (pre-registered): >=30 MATURED signals AND mean above PASSED's - then it goes to a Friday review, not before.

| Shadow cohort | n | Win% | Mean | Median | Mean vs SPY | PASSED mean (ref) |
|---|---|---|---|---|---|---|
| ADX 18-20, all else passed | 2 | 100% | +1.48% | +1.48% | +1.23% | +0.10% |
| DEEP-FAIL, all else passed | 2 | 100% | +4.29% | +4.29% | +4.04% | +0.10% |

## Every graded signal

| Date | Sym | Cohort | Regime | Entry | Mark | Days | Return | vs SPY | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | BG | BLOCKED | n/a | 120.49 | 117.37 | 6 | -2.6% | -2.4 | OPEN |
| 2026-07-20 | CHRD | BLOCKED | n/a | 128.8 | 128.8 | 6 | +0.0% | +0.2 | OPEN |
| 2026-07-20 | CNOB | BLOCKED | n/a | 33.46 | 33.1 | 6 | -1.1% | -0.9 | OPEN |
| 2026-07-20 | COCO | BLOCKED | PASS | 73.87 | 69.58 | 6 | -5.8% | -5.6 | OPEN |
| 2026-07-20 | CVNA | BLOCKED | DEEP-FAIL | 64.14 | 66.07 | 6 | +3.0% | +3.2 | OPEN |
| 2026-07-20 | FLG | BLOCKED | n/a | 14.84 | 13.98 | 6 | -5.8% | -5.6 | OPEN |
| 2026-07-20 | FNB | BLOCKED | n/a | 18.75 | 19.13 | 6 | +2.0% | +2.2 | OPEN |
| 2026-07-20 | HAS | BLOCKED | REPAIR | 81.59 | 96.34 | 6 | +18.1% | +18.2 | OPEN |
| 2026-07-20 | HLX | BLOCKED | n/a | 9.43 | 9.13 | 6 | -3.2% | -3.0 | OPEN |
| 2026-07-20 | LCID | BLOCKED | n/a | 7.11 | 7.9 | 6 | +11.1% | +11.3 | OPEN |
| 2026-07-20 | M | BLOCKED | REPAIR | 23.31 | 25.15 | 5 | +7.9% | +8.1 | OPEN |
| 2026-07-20 | NOV | BLOCKED | REPAIR | 19.55 | 19.82 | 6 | +1.4% | +1.6 | OPEN |
| 2026-07-20 | ODFL | BLOCKED | PASS | 231.76 | 226.28 | 6 | -2.4% | -2.2 | OPEN |
| 2026-07-20 | RYZ | BLOCKED | n/a | 29.07 | 31.03 | 6 | +6.7% | +6.9 | OPEN |
| 2026-07-20 | SHAK | BLOCKED | DEEP-FAIL | 56.97 | 63.2 | 6 | +10.9% | +11.1 | OPEN |
| 2026-07-20 | SPG | BLOCKED | PASS | 228.19 | 236.7 | 6 | +3.7% | +3.9 | OPEN |
| 2026-07-20 | TRNS | BLOCKED | n/a | 86.09 | 86.07 | 6 | -0.0% | +0.1 | OPEN |
| 2026-07-20 | VVV | BLOCKED | PASS | 39.54 | 40.2 | 6 | +1.7% | +1.8 | OPEN |
| 2026-07-20 | VZ | BLOCKED | REPAIR | 43.5 | 48.19 | 6 | +10.8% | +10.9 | OPEN |
| 2026-07-20 | WPC | BLOCKED | REPAIR | 75.17 | 75.61 | 6 | +0.6% | +0.8 | OPEN |
| 2026-07-21 | ALKS | BLOCKED | TAPE OK | 52.85 | 50.5 | 5 | -4.5% | -3.5 | OPEN |
| 2026-07-21 | ATLC | BLOCKED | TAPE OK | 96.37 | 104.82 | 5 | +8.8% | +9.8 | OPEN |
| 2026-07-21 | BRKR | BLOCKED | TAPE OK | 60.43 | 62.91 | 5 | +4.1% | +5.1 | OPEN |
| 2026-07-21 | CB | BLOCKED | TAPE OK | 354.8 | 363.5 | 5 | +2.5% | +3.4 | OPEN |
| 2026-07-21 | CBL | BLOCKED | TAPE OK | 55.53 | 60.05 | 5 | +8.1% | +9.1 | OPEN |
| 2026-07-21 | CNOB | BLOCKED | TAPE OK | 33.41 | 33.1 | 5 | -0.9% | +0.1 | OPEN |
| 2026-07-21 | COCO | BLOCKED | TAPE OK | 75.89 | 69.58 | 5 | -8.3% | -7.3 | OPEN |
| 2026-07-21 | CTRE | BLOCKED | TAPE OK | 43.4 | 42.73 | 5 | -1.5% | -0.6 | OPEN |
| 2026-07-21 | ESQ | BLOCKED | TAPE OK | 122.83 | 127.58 | 5 | +3.9% | +4.8 | OPEN |
| 2026-07-21 | EXTR | BLOCKED | TAPE OK | 30.44 | 29.99 | 5 | -1.5% | -0.5 | OPEN |
| 2026-07-21 | FFIV | BLOCKED | TAPE OK | 408.74 | 403.46 | 4 | -1.3% | -0.3 | OPEN |
| 2026-07-21 | FRT | BLOCKED | TAPE OK | 125.59 | 126.12 | 5 | +0.4% | +1.4 | OPEN |
| 2026-07-21 | HCSG | BLOCKED | TAPE OK | 24.8 | 23.75 | 5 | -4.2% | -3.2 | OPEN |
| 2026-07-21 | HELE | BLOCKED | TAPE OK | 27.28 | 28.85 | 5 | +5.8% | +6.8 | OPEN |
| 2026-07-21 | HOMB | BLOCKED | TAPE OK | 30.42 | 31.48 | 5 | +3.5% | +4.5 | OPEN |
| 2026-07-21 | LQDA | BLOCKED | TAPE OK | 80.89 | 86.82 | 4 | +7.3% | +8.3 | OPEN |
| 2026-07-21 | NVRI | BLOCKED | TAPE OK | 21.87 | 22.16 | 5 | +1.3% | +2.3 | OPEN |
| 2026-07-21 | NWPX | BLOCKED | TAPE OK | 135.41 | 126.25 | 5 | -6.8% | -5.8 | OPEN |
| 2026-07-21 | OSCR | BLOCKED | TAPE OK | 30.77 | 31.4 | 5 | +2.0% | +3.0 | OPEN |
| 2026-07-21 | PNC | BLOCKED | TAPE OK | 250.38 | 251.6 | 5 | +0.5% | +1.5 | OPEN |
| 2026-07-21 | SION | BLOCKED | TAPE OK | 47.21 | 46.55 | 4 | -1.4% | -0.4 | OPEN |
| 2026-07-21 | TBLA | BLOCKED | TAPE OK | 5.11 | 5.01 | 5 | -1.9% | -0.9 | OPEN |
| 2026-07-21 | TFIN | BLOCKED | TAPE OK | 79.19 | 77.08 | 4 | -2.7% | -1.7 | OPEN |
| 2026-07-21 | TGTX | BLOCKED | TAPE OK | 53.95 | 54.87 | 4 | +1.7% | +2.7 | OPEN |
| 2026-07-21 | TVTX | BLOCKED | TAPE OK | 56.58 | 55.91 | 5 | -1.2% | -0.2 | OPEN |
| 2026-07-21 | VCYT | BLOCKED | TAPE OK | 59.53 | 55.65 | 5 | -6.5% | -5.5 | OPEN |
| 2026-07-21 | ZD | BLOCKED | TAPE OK | 52.39 | 52.93 | 5 | +1.0% | +2.0 | OPEN |
| 2026-07-21 | CYRX | PASSED | TAPE OK | 16.24 | 15.17 | 5 | -6.6% | -5.6 | OPEN |
| 2026-07-21 | FLEX | PASSED | TAPE OK | 127.39 | 113.28 | 5 | -11.1% | -10.1 | OPEN |
| 2026-07-21 | GDX | PASSED | TAPE OK | 74.19 | 74.21 | 5 | +0.0% | +1.0 | OPEN |
| 2026-07-21 | HON | PASSED | TAPE OK | 229.86 | 247.05 | 4 | +7.5% | +8.5 | OPEN |
| 2026-07-21 | KWEB | PASSED | TAPE OK | 27.02 | 27.31 | 5 | +1.1% | +2.1 | OPEN |
| 2026-07-21 | MSFT | PASSED | TAPE OK | 397.75 | 393.35 | 5 | -1.1% | -0.1 | OPEN |
| 2026-07-21 | MU | PASSED | TAPE OK | 970.82 | 820.53 | 5 | -15.5% | -14.5 | OPEN |
| 2026-07-21 | NKE | PASSED | TAPE OK | 42.96 | 43.05 | 5 | +0.2% | +1.2 | OPEN |
| 2026-07-21 | PM | PASSED | TAPE OK | 188.04 | 200.17 | 5 | +6.5% | +7.4 | OPEN |
| 2026-07-21 | SKYY | PASSED | TAPE OK | 136.02 | 137.9 | 5 | +1.4% | +2.4 | OPEN |
| 2026-07-21 | SNOW | PASSED | TAPE OK | 271.73 | 270.36 | 5 | -0.5% | +0.5 | OPEN |
| 2026-07-22 | ACTG | BLOCKED | REPAIR | 4.57 | 4.63 | 4 | +1.3% | +2.2 | OPEN |
| 2026-07-22 | AMCR | BLOCKED | PASS | 43.21 | 46.69 | 4 | +8.1% | +8.9 | OPEN |
| 2026-07-22 | AMGN | BLOCKED | PASS | 366.05 | 393.1 | 4 | +7.4% | +8.3 | OPEN |
| 2026-07-22 | ASB | BLOCKED | PASS | 30.7 | 31.06 | 4 | +1.2% | +2.0 | OPEN |
| 2026-07-22 | BCBP | BLOCKED | REPAIR | 10.29 | 10.72 | 4 | +4.2% | +5.1 | OPEN |
| 2026-07-22 | BHP | BLOCKED | REPAIR | 84.54 | 83.79 | 3 | -0.9% | -0.0 | OPEN |
| 2026-07-22 | BHRB | BLOCKED | PASS | 71.01 | 74.08 | 4 | +4.3% | +5.2 | OPEN |
| 2026-07-22 | BX | BLOCKED | REPAIR | 122.82 | 133.9 | 4 | +9.0% | +9.9 | OPEN |
| 2026-07-22 | BY | BLOCKED | PASS | 37.75 | 39.2 | 4 | +3.8% | +4.7 | OPEN |
| 2026-07-22 | CBSH | BLOCKED | PASS | 58.7 | 60.01 | 4 | +2.2% | +3.1 | OPEN |
| 2026-07-22 | CCJ | BLOCKED | DEEP-FAIL | 90.37 | 86.96 | 4 | -3.8% | -2.9 | OPEN |
| 2026-07-22 | CMP | BLOCKED | REPAIR | 30.14 | 29.69 | 4 | -1.5% | -0.6 | OPEN |
| 2026-07-22 | CNOB | BLOCKED | PASS | 33.0 | 33.1 | 4 | +0.3% | +1.2 | OPEN |
| 2026-07-22 | COKE | BLOCKED | PASS | 184.36 | 195.0 | 4 | +5.8% | +6.7 | OPEN |
| 2026-07-22 | COLB | BLOCKED | PASS | 32.63 | 31.27 | 4 | -4.2% | -3.3 | OPEN |
| 2026-07-22 | COST | BLOCKED | REPAIR | 927.31 | 966.58 | 4 | +4.2% | +5.1 | OPEN |
| 2026-07-22 | CRCL | BLOCKED | DEEP-FAIL | 66.16 | 64.32 | 4 | -2.8% | -1.9 | OPEN |
| 2026-07-22 | DE | BLOCKED | PASS | 607.33 | 639.84 | 4 | +5.3% | +6.2 | OPEN |
| 2026-07-22 | DELL | BLOCKED | PASS | 441.8 | 392.1 | 4 | -11.2% | -10.4 | OPEN |
| 2026-07-22 | DIS | BLOCKED | REPAIR | 95.87 | 98.89 | 4 | +3.1% | +4.0 | OPEN |
| 2026-07-22 | EQR | BLOCKED | PASS | 68.29 | 68.09 | 3 | -0.3% | +0.6 | OPEN |
| 2026-07-22 | F | BLOCKED | PASS | 14.42 | 14.96 | 4 | +3.7% | +4.6 | OPEN |
| 2026-07-22 | FCX | BLOCKED | PASS | 65.0 | 61.64 | 4 | -5.2% | -4.3 | OPEN |
| 2026-07-22 | FHB | BLOCKED | PASS | 28.81 | 28.09 | 4 | -2.5% | -1.6 | OPEN |
| 2026-07-22 | FITB | BLOCKED | PASS | 57.67 | 57.8 | 3 | +0.2% | +1.1 | OPEN |
| 2026-07-22 | FLEX | BLOCKED | REPAIR | 127.0 | 113.28 | 4 | -10.8% | -9.9 | OPEN |
| 2026-07-22 | FLG | BLOCKED | PASS | 14.88 | 13.98 | 4 | -6.0% | -5.2 | OPEN |
| 2026-07-22 | FNB | BLOCKED | PASS | 18.86 | 19.13 | 4 | +1.4% | +2.3 | OPEN |
| 2026-07-22 | FRT | BLOCKED | PASS | 125.05 | 126.12 | 4 | +0.9% | +1.7 | OPEN |
| 2026-07-22 | GBCI | BLOCKED | PASS | 51.17 | 49.51 | 4 | -3.2% | -2.4 | OPEN |
| 2026-07-22 | GDX | BLOCKED | DEEP-FAIL | 76.68 | 74.21 | 4 | -3.2% | -2.3 | OPEN |
| 2026-07-22 | GLD | BLOCKED | REPAIR | 379.12 | 369.37 | 4 | -2.6% | -1.7 | OPEN |
| 2026-07-22 | GM | BLOCKED | PASS | 82.13 | 90.3 | 4 | +9.9% | +10.8 | OPEN |
| 2026-07-22 | HBNC | BLOCKED | PASS | 20.21 | 20.71 | 4 | +2.5% | +3.4 | OPEN |
| 2026-07-22 | HON | BLOCKED | PASS | 232.99 | 247.05 | 3 | +6.0% | +6.9 | OPEN |
| 2026-07-22 | HOPE | BLOCKED | PASS | 13.54 | 14.12 | 4 | +4.3% | +5.2 | OPEN |
| 2026-07-22 | HSIC | BLOCKED | PASS | 84.81 | 85.71 | 3 | +1.1% | +1.9 | OPEN |
| 2026-07-22 | HTZ | BLOCKED | DEEP-FAIL | 1.93 | 1.76 | 4 | -8.6% | -7.7 | OPEN |
| 2026-07-22 | KRE | BLOCKED | PASS | 75.6 | 76.79 | 4 | +1.6% | +2.5 | OPEN |
| 2026-07-22 | LCID | BLOCKED | DEEP-FAIL | 6.78 | 7.9 | 4 | +16.5% | +17.4 | OPEN |
| 2026-07-22 | LZB | BLOCKED | PASS | 39.3 | 41.3 | 4 | +5.1% | +6.0 | OPEN |
| 2026-07-22 | M | BLOCKED | PASS | 24.33 | 25.15 | 3 | +3.4% | +4.2 | OPEN |
| 2026-07-22 | MFA | BLOCKED | REPAIR | 9.29 | 9.2 | 4 | -1.0% | -0.1 | OPEN |
| 2026-07-22 | MU | BLOCKED | PASS | 959.48 | 820.53 | 4 | -14.5% | -13.6 | OPEN |
| 2026-07-22 | NEE | BLOCKED | PASS | 89.41 | 89.28 | 4 | -0.1% | +0.7 | OPEN |
| 2026-07-22 | NEM | BLOCKED | REPAIR | 95.75 | 91.52 | 4 | -4.4% | -3.5 | OPEN |
| 2026-07-22 | OCFC | BLOCKED | PASS | 19.67 | 20.04 | 4 | +1.9% | +2.8 | OPEN |
| 2026-07-22 | PANW | BLOCKED | PASS | 335.28 | 319.0 | 4 | -4.9% | -4.0 | OPEN |
| 2026-07-22 | PB | BLOCKED | PASS | 73.06 | 73.55 | 4 | +0.7% | +1.6 | OPEN |
| 2026-07-22 | PM | BLOCKED | PASS | 194.3 | 200.17 | 4 | +3.0% | +3.9 | OPEN |
| 2026-07-22 | POWL | BLOCKED | REPAIR | 240.68 | 201.0 | 4 | -16.5% | -15.6 | OPEN |
| 2026-07-22 | PRLB | BLOCKED | PASS | 79.73 | 74.88 | 4 | -6.1% | -5.2 | OPEN |
| 2026-07-22 | RACE | BLOCKED | REPAIR | 371.61 | 390.14 | 4 | +5.0% | +5.9 | OPEN |
| 2026-07-22 | RCL | BLOCKED | REPAIR | 285.85 | 322.5 | 4 | +12.8% | +13.7 | OPEN |
| 2026-07-22 | RSPU | BLOCKED | PASS | 81.85 | 81.03 | 3 | -1.0% | -0.1 | OPEN |
| 2026-07-22 | SAIC | BLOCKED | PASS | 115.95 | 121.59 | 4 | +4.9% | +5.7 | OPEN |
| 2026-07-22 | SJM | BLOCKED | PASS | 118.05 | 123.04 | 4 | +4.2% | +5.1 | OPEN |
| 2026-07-22 | SKK | BLOCKED | PASS | 5.22 | 4.76 | 4 | -8.8% | -7.9 | OPEN |
| 2026-07-22 | SMCI | BLOCKED | REPAIR | 30.56 | 28.45 | 4 | -6.9% | -6.0 | OPEN |
| 2026-07-22 | SON | BLOCKED | PASS | 55.15 | 60.56 | 3 | +9.8% | +10.7 | OPEN |
| 2026-07-22 | SPG | BLOCKED | PASS | 226.22 | 236.7 | 4 | +4.6% | +5.5 | OPEN |
| 2026-07-22 | SSB | BLOCKED | PASS | 102.19 | 106.6 | 3 | +4.3% | +5.2 | OPEN |
| 2026-07-22 | STRL | BLOCKED | REPAIR | 719.34 | 538.09 | 4 | -25.2% | -24.3 | OPEN |
| 2026-07-22 | STX | BLOCKED | PASS | 908.1 | 747.3 | 4 | -17.7% | -16.8 | OPEN |
| 2026-07-22 | TDY | BLOCKED | PASS | 650.5 | 649.67 | 4 | -0.1% | +0.8 | OPEN |
| 2026-07-22 | TPL | BLOCKED | PASS | 433.1 | 389.42 | 4 | -10.1% | -9.2 | OPEN |
| 2026-07-22 | TPR | BLOCKED | PASS | 143.73 | 150.9 | 4 | +5.0% | +5.9 | OPEN |
| 2026-07-22 | URA | BLOCKED | DEEP-FAIL | 40.97 | 38.95 | 4 | -4.9% | -4.0 | OPEN |
| 2026-07-22 | USB | BLOCKED | PASS | 64.47 | 64.43 | 4 | -0.1% | +0.8 | OPEN |
| 2026-07-22 | VST | BLOCKED | REPAIR | 166.74 | 148.64 | 4 | -10.9% | -10.0 | OPEN |
| 2026-07-22 | VVV | BLOCKED | PASS | 39.03 | 40.2 | 4 | +3.0% | +3.9 | OPEN |
| 2026-07-22 | CTRE | PASSED | PASS | 42.38 | 42.73 | 4 | +0.8% | +1.7 | OPEN |
| 2026-07-22 | PFE | PASSED | REPAIR | 24.82 | 25.25 | 4 | +1.7% | +2.6 | OPEN |
| 2026-07-22 | TJX | PASSED | REPAIR | 155.41 | 160.8 | 4 | +3.5% | +4.3 | OPEN |
| 2026-07-22 | TXNM | PASSED | REPAIR | 58.3 | 58.05 | 3 | -0.4% | +0.5 | OPEN |
| 2026-07-22 | VZ | PASSED | REPAIR | 44.29 | 48.19 | 4 | +8.8% | +9.7 | OPEN |
| 2026-07-23 | ACTG | BLOCKED | REPAIR | 4.62 | 4.63 | 3 | +0.2% | -0.1 | OPEN |
| 2026-07-23 | ALSN | BLOCKED | PASS | 119.64 | 121.11 | 3 | +1.2% | +0.9 | OPEN |
| 2026-07-23 | AVT | BLOCKED | PASS | 89.92 | 86.22 | 3 | -4.1% | -4.5 | OPEN |
| 2026-07-23 | BUD | BLOCKED | REPAIR | 80.48 | 83.2 | 3 | +3.4% | +3.0 | OPEN |
| 2026-07-23 | COST | BLOCKED | REPAIR | 926.06 | 966.58 | 3 | +4.4% | +4.0 | OPEN |
| 2026-07-23 | CRCL | BLOCKED | DEEP-FAIL | 62.18 | 64.32 | 3 | +3.4% | +3.1 | OPEN |
| 2026-07-23 | DELL | BLOCKED | PASS | 439.34 | 392.1 | 3 | -10.8% | -11.1 | OPEN |
| 2026-07-23 | DGX | BLOCKED | PASS | 227.9 | 235.94 | 3 | +3.5% | +3.2 | OPEN |
| 2026-07-23 | F | BLOCKED | REPAIR | 14.15 | 14.96 | 3 | +5.7% | +5.4 | OPEN |
| 2026-07-23 | FCX | BLOCKED | REPAIR | 63.5 | 61.64 | 3 | -2.9% | -3.3 | OPEN |
| 2026-07-23 | FLG | BLOCKED | PASS | 14.71 | 13.98 | 3 | -5.0% | -5.3 | OPEN |
| 2026-07-23 | FNB | BLOCKED | PASS | 18.87 | 19.13 | 3 | +1.4% | +1.0 | OPEN |
| 2026-07-23 | FUTU | BLOCKED | DEEP-FAIL | 98.96 | 101.84 | 3 | +2.9% | +2.5 | OPEN |
| 2026-07-23 | GDX | BLOCKED | DEEP-FAIL | 75.02 | 74.21 | 3 | -1.1% | -1.4 | OPEN |
| 2026-07-23 | GLD | BLOCKED | REPAIR | 371.52 | 369.37 | 3 | -0.6% | -0.9 | OPEN |
| 2026-07-23 | GM | BLOCKED | PASS | 80.67 | 90.3 | 3 | +11.9% | +11.6 | OPEN |
| 2026-07-23 | HON | BLOCKED | PASS | 246.27 | 247.05 | 2 | +0.3% | -0.1 | OPEN |
| 2026-07-23 | IRM | BLOCKED | REPAIR | 124.55 | 125.7 | 3 | +0.9% | +0.6 | OPEN |
| 2026-07-23 | LCID | BLOCKED | DEEP-FAIL | 6.45 | 7.9 | 3 | +22.5% | +22.1 | OPEN |
| 2026-07-23 | LSTR | BLOCKED | PASS | 207.97 | 185.32 | 3 | -10.9% | -11.2 | OPEN |
| 2026-07-23 | M | BLOCKED | PASS | 23.33 | 25.15 | 2 | +7.8% | +7.4 | OPEN |
| 2026-07-23 | MAC | BLOCKED | PASS | 25.3 | 26.51 | 3 | +4.8% | +4.4 | OPEN |
| 2026-07-23 | NEM | BLOCKED | REPAIR | 94.72 | 91.52 | 3 | -3.4% | -3.7 | OPEN |
| 2026-07-23 | PLD | BLOCKED | PASS | 145.12 | 147.12 | 2 | +1.4% | +1.0 | OPEN |
| 2026-07-23 | PRLB | BLOCKED | PASS | 78.62 | 74.88 | 3 | -4.8% | -5.1 | OPEN |
| 2026-07-23 | RHP | BLOCKED | PASS | 128.89 | 135.99 | 3 | +5.5% | +5.2 | OPEN |
| 2026-07-23 | SMCI | BLOCKED | REPAIR | 31.2 | 28.45 | 3 | -8.8% | -9.2 | OPEN |
| 2026-07-23 | SON | BLOCKED | PASS | 56.32 | 60.56 | 2 | +7.5% | +7.2 | OPEN |
| 2026-07-23 | SPG | BLOCKED | PASS | 225.2 | 236.7 | 3 | +5.1% | +4.7 | OPEN |
| 2026-07-23 | TDY | BLOCKED | PASS | 651.22 | 649.67 | 3 | -0.2% | -0.6 | OPEN |
| 2026-07-23 | URA | BLOCKED | DEEP-FAIL | 41.13 | 38.95 | 3 | -5.3% | -5.7 | OPEN |
| 2026-07-23 | URI | BLOCKED | PASS | 1139.71 | 1091.26 | 3 | -4.2% | -4.6 | OPEN |
| 2026-07-23 | VST | BLOCKED | REPAIR | 168.98 | 148.64 | 3 | -12.0% | -12.4 | OPEN |
| 2026-07-23 | VVV | BLOCKED | PASS | 38.31 | 40.2 | 3 | +4.9% | +4.6 | OPEN |
| 2026-07-23 | ECVT | PASSED | PASS | 12.89 | 12.32 | 2 | -4.4% | -4.8 | OPEN |
| 2026-07-23 | FRT | PASSED | PASS | 124.83 | 126.12 | 3 | +1.0% | +0.7 | OPEN |
| 2026-07-23 | HAS | PASSED | PASS | 87.35 | 96.34 | 3 | +10.3% | +9.9 | OPEN |
| 2026-07-23 | LHX | PASSED | REPAIR | 299.67 | 305.2 | 3 | +1.9% | +1.5 | OPEN |
| 2026-07-23 | MLI | PASSED | REPAIR | 63.13 | 66.49 | 3 | +5.3% | +5.0 | OPEN |
| 2026-07-23 | PFE | PASSED | REPAIR | 25.01 | 25.25 | 3 | +1.0% | +0.6 | OPEN |
| 2026-07-23 | SJM | PASSED | PASS | 115.71 | 123.04 | 3 | +6.3% | +6.0 | OPEN |
| 2026-07-23 | VZ | PASSED | REPAIR | 43.82 | 48.19 | 3 | +10.0% | +9.6 | OPEN |
| 2026-07-24 | ALSN | BLOCKED | PASS | 122.34 | 121.11 | 2 | -1.0% | -1.3 | OPEN |
| 2026-07-24 | AVT | BLOCKED | PASS | 89.42 | 86.22 | 2 | -3.6% | -3.8 | OPEN |
| 2026-07-24 | BUD | BLOCKED | REPAIR | 81.66 | 83.2 | 2 | +1.9% | +1.6 | OPEN |
| 2026-07-24 | CB | BLOCKED | PASS | 359.75 | 363.5 | 2 | +1.0% | +0.8 | OPEN |
| 2026-07-24 | CNP | BLOCKED | PASS | 44.56 | 44.1 | 2 | -1.0% | -1.3 | OPEN |
| 2026-07-24 | COST | BLOCKED | REPAIR | 935.03 | 966.58 | 2 | +3.4% | +3.1 | OPEN |
| 2026-07-24 | CRCL | BLOCKED | DEEP-FAIL | 62.36 | 64.32 | 2 | +3.1% | +2.9 | OPEN |
| 2026-07-24 | DE | BLOCKED | PASS | 628.16 | 639.84 | 2 | +1.9% | +1.6 | OPEN |
| 2026-07-24 | DGX | BLOCKED | PASS | 227.86 | 235.94 | 2 | +3.5% | +3.3 | OPEN |
| 2026-07-24 | DLR | BLOCKED | PASS | 199.08 | 193.18 | 2 | -3.0% | -3.2 | OPEN |
| 2026-07-24 | EGBN | BLOCKED | PASS | 28.44 | 28.39 | 2 | -0.2% | -0.4 | OPEN |
| 2026-07-24 | F | BLOCKED | REPAIR | 14.37 | 14.96 | 2 | +4.1% | +3.8 | OPEN |
| 2026-07-24 | FCX | BLOCKED | REPAIR | 62.6 | 61.64 | 2 | -1.5% | -1.8 | OPEN |
| 2026-07-24 | FUTU | BLOCKED | DEEP-FAIL | 99.36 | 101.84 | 2 | +2.5% | +2.2 | OPEN |
| 2026-07-24 | GDX | BLOCKED | DEEP-FAIL | 75.23 | 74.21 | 2 | -1.4% | -1.6 | OPEN |
| 2026-07-24 | GE | BLOCKED | PASS | 353.73 | 363.59 | 2 | +2.8% | +2.5 | OPEN |
| 2026-07-24 | GLD | BLOCKED | REPAIR | 371.9 | 369.37 | 2 | -0.7% | -0.9 | OPEN |
| 2026-07-24 | GM | BLOCKED | PASS | 82.64 | 90.3 | 2 | +9.3% | +9.0 | OPEN |
| 2026-07-24 | HON | BLOCKED | PASS | 245.75 | 247.05 | 1 | +0.5% | +0.3 | OPEN |
| 2026-07-24 | IRM | BLOCKED | PASS | 128.31 | 125.7 | 2 | -2.0% | -2.3 | OPEN |
| 2026-07-24 | JNJ | BLOCKED | PASS | 263.4 | 266.73 | 2 | +1.3% | +1.0 | OPEN |
| 2026-07-24 | LCID | BLOCKED | DEEP-FAIL | 6.3 | 7.9 | 2 | +25.4% | +25.1 | OPEN |
| 2026-07-24 | LDOS | BLOCKED | DEEP-FAIL | 112.14 | 118.36 | 2 | +5.5% | +5.3 | OPEN |
| 2026-07-24 | LIND | BLOCKED | PASS | 26.85 | 29.74 | 2 | +10.8% | +10.5 | OPEN |
| 2026-07-24 | M | BLOCKED | PASS | 24.96 | 25.15 | 1 | +0.8% | +0.5 | OPEN |
| 2026-07-24 | NEM | BLOCKED | REPAIR | 93.19 | 91.52 | 2 | -1.8% | -2.0 | OPEN |
| 2026-07-24 | ORKA | BLOCKED | PASS | 92.16 | 90.45 | 2 | -1.9% | -2.1 | OPEN |
| 2026-07-24 | PH | BLOCKED | PASS | 987.54 | 990.96 | 2 | +0.3% | +0.1 | OPEN |
| 2026-07-24 | PRLB | BLOCKED | PASS | 78.24 | 74.88 | 2 | -4.3% | -4.6 | OPEN |
| 2026-07-24 | ROP | BLOCKED | REPAIR | 375.02 | 390.92 | 1 | +4.2% | +4.0 | OPEN |
| 2026-07-24 | RSPU | BLOCKED | PASS | 81.24 | 81.03 | 1 | -0.3% | -0.5 | OPEN |
| 2026-07-24 | SMCI | BLOCKED | REPAIR | 30.1 | 28.45 | 2 | -5.5% | -5.7 | OPEN |
| 2026-07-24 | SON | BLOCKED | PASS | 58.68 | 60.56 | 1 | +3.2% | +2.9 | OPEN |
| 2026-07-24 | SPG | BLOCKED | PASS | 229.78 | 236.7 | 2 | +3.0% | +2.8 | OPEN |
| 2026-07-24 | TDY | BLOCKED | PASS | 655.35 | 649.67 | 2 | -0.9% | -1.1 | OPEN |
| 2026-07-24 | URA | BLOCKED | DEEP-FAIL | 39.89 | 38.95 | 2 | -2.4% | -2.6 | OPEN |
| 2026-07-24 | URI | BLOCKED | PASS | 1141.59 | 1091.26 | 2 | -4.4% | -4.7 | OPEN |
| 2026-07-24 | VST | BLOCKED | REPAIR | 163.38 | 148.64 | 2 | -9.0% | -9.3 | OPEN |
| 2026-07-24 | XLI | BLOCKED | PASS | 182.66 | 182.49 | 2 | -0.1% | -0.3 | OPEN |
| 2026-07-24 | ACTG | PASSED | PASS | 4.66 | 4.63 | 2 | -0.6% | -0.9 | OPEN |
| 2026-07-24 | DELL | PASSED | PASS | 437.5 | 392.1 | 2 | -10.4% | -10.6 | OPEN |
| 2026-07-24 | EQIX | PASSED | PASS | 1084.24 | 1034.86 | 2 | -4.5% | -4.8 | OPEN |
| 2026-07-24 | LHX | PASSED | REPAIR | 300.21 | 305.2 | 2 | +1.7% | +1.4 | OPEN |
| 2026-07-24 | MLI | PASSED | REPAIR | 63.91 | 66.49 | 2 | +4.0% | +3.8 | OPEN |
| 2026-07-24 | MRK | PASSED | PASS | 131.07 | 131.82 | 2 | +0.6% | +0.3 | OPEN |
| 2026-07-24 | RHP | PASSED | PASS | 133.09 | 135.99 | 2 | +2.2% | +1.9 | OPEN |
| 2026-07-24 | SJM | PASSED | PASS | 118.32 | 123.04 | 2 | +4.0% | +3.7 | OPEN |
| 2026-07-24 | VZ | PASSED | REPAIR | 46.38 | 48.19 | 2 | +3.9% | +3.6 | OPEN |
| 2026-07-27 | ACGL | BLOCKED | PASS | 103.88 | 106.48 | 1 | +2.5% | +2.3 | OPEN |
| 2026-07-27 | ALSN | BLOCKED | PASS | 121.91 | 121.11 | 1 | -0.7% | -0.9 | OPEN |
| 2026-07-27 | AVT | BLOCKED | PASS | 88.38 | 86.22 | 1 | -2.4% | -2.7 | OPEN |
| 2026-07-27 | BUD | BLOCKED | REPAIR | 80.87 | 83.2 | 1 | +2.9% | +2.6 | OPEN |
| 2026-07-27 | CB | BLOCKED | PASS | 358.91 | 363.5 | 1 | +1.3% | +1.0 | OPEN |
| 2026-07-27 | CPRT | BLOCKED | DEEP-FAIL | 29.79 | 30.69 | 1 | +3.0% | +2.8 | OPEN |
| 2026-07-27 | CRCL | BLOCKED | DEEP-FAIL | 65.67 | 64.32 | 1 | -2.1% | -2.3 | OPEN |
| 2026-07-27 | DE | BLOCKED | PASS | 625.02 | 639.84 | 1 | +2.4% | +2.1 | OPEN |
| 2026-07-27 | DLR | BLOCKED | PASS | 195.76 | 193.18 | 1 | -1.3% | -1.6 | OPEN |
| 2026-07-27 | EGBN | BLOCKED | PASS | 28.15 | 28.39 | 1 | +0.8% | +0.6 | OPEN |
| 2026-07-27 | F | BLOCKED | PASS | 14.68 | 14.96 | 1 | +1.9% | +1.7 | OPEN |
| 2026-07-27 | FCX | BLOCKED | REPAIR | 62.72 | 61.64 | 1 | -1.7% | -2.0 | OPEN |
| 2026-07-27 | FUTU | BLOCKED | DEEP-FAIL | 104.27 | 101.84 | 1 | -2.3% | -2.6 | OPEN |
| 2026-07-27 | GDX | BLOCKED | DEEP-FAIL | 75.73 | 74.21 | 1 | -2.0% | -2.2 | OPEN |
| 2026-07-27 | GLD | BLOCKED | REPAIR | 374.63 | 369.37 | 1 | -1.4% | -1.6 | OPEN |
| 2026-07-27 | GM | BLOCKED | PASS | 87.04 | 90.3 | 1 | +3.8% | +3.5 | OPEN |
| 2026-07-27 | HON | BLOCKED | PASS | 245.75 | 247.05 | 1 | +0.5% | +0.3 | OPEN |
| 2026-07-27 | IRM | BLOCKED | PASS | 126.99 | 125.7 | 1 | -1.0% | -1.3 | OPEN |
| 2026-07-27 | LDOS | BLOCKED | DEEP-FAIL | 114.95 | 118.36 | 1 | +3.0% | +2.7 | OPEN |
| 2026-07-27 | LIND | BLOCKED | PASS | 28.09 | 29.74 | 1 | +5.9% | +5.6 | OPEN |
| 2026-07-27 | MAR | BLOCKED | PASS | 383.06 | 383.52 | 1 | +0.1% | -0.1 | OPEN |
| 2026-07-27 | NEM | BLOCKED | REPAIR | 93.47 | 91.52 | 1 | -2.1% | -2.3 | OPEN |
| 2026-07-27 | ORKA | BLOCKED | PASS | 90.2 | 90.45 | 1 | +0.3% | +0.0 | OPEN |
| 2026-07-27 | PGR | BLOCKED | REPAIR | 215.76 | 219.52 | 1 | +1.7% | +1.5 | OPEN |
| 2026-07-27 | PH | BLOCKED | PASS | 987.31 | 990.96 | 1 | +0.4% | +0.1 | OPEN |
| 2026-07-27 | PRLB | BLOCKED | PASS | 77.64 | 74.88 | 1 | -3.5% | -3.8 | OPEN |
| 2026-07-27 | RCL | BLOCKED | REPAIR | 305.04 | 322.5 | 1 | +5.7% | +5.5 | OPEN |
| 2026-07-27 | ROP | BLOCKED | REPAIR | 375.02 | 390.92 | 1 | +4.2% | +4.0 | OPEN |
| 2026-07-27 | RSPU | BLOCKED | PASS | 81.24 | 81.03 | 1 | -0.3% | -0.5 | OPEN |
| 2026-07-27 | SLB | BLOCKED | PASS | 51.53 | 49.98 | 1 | -3.0% | -3.2 | OPEN |
| 2026-07-27 | SMCI | BLOCKED | DEEP-FAIL | 29.81 | 28.45 | 1 | -4.6% | -4.8 | OPEN |
| 2026-07-27 | SON | BLOCKED | PASS | 58.68 | 60.56 | 1 | +3.2% | +3.0 | OPEN |
| 2026-07-27 | TDY | BLOCKED | PASS | 651.65 | 649.67 | 1 | -0.3% | -0.5 | OPEN |
| 2026-07-27 | TJX | BLOCKED | REPAIR | 156.38 | 160.8 | 1 | +2.8% | +2.6 | OPEN |
| 2026-07-27 | URA | BLOCKED | DEEP-FAIL | 40.32 | 38.95 | 1 | -3.4% | -3.6 | OPEN |
| 2026-07-27 | VRSN | BLOCKED | REPAIR | 274.82 | 281.15 | 1 | +2.3% | +2.1 | OPEN |
| 2026-07-27 | VST | BLOCKED | REPAIR | 157.08 | 148.64 | 1 | -5.4% | -5.6 | OPEN |
| 2026-07-27 | WWD | BLOCKED | PASS | 419.76 | 410.55 | 1 | -2.2% | -2.4 | OPEN |
| 2026-07-27 | XLI | BLOCKED | PASS | 183.2 | 182.49 | 1 | -0.4% | -0.6 | OPEN |
| 2026-07-27 | ACTG | PASSED | PASS | 4.63 | 4.63 | 1 | +0.0% | -0.2 | OPEN |
| 2026-07-27 | DELL | PASSED | PASS | 426.91 | 392.1 | 1 | -8.2% | -8.4 | OPEN |
| 2026-07-27 | DGX | PASSED | PASS | 231.84 | 235.94 | 1 | +1.8% | +1.5 | OPEN |
| 2026-07-27 | EQIX | PASSED | PASS | 1046.79 | 1034.86 | 1 | -1.1% | -1.4 | OPEN |
| 2026-07-27 | GE | PASSED | PASS | 361.61 | 363.59 | 1 | +0.6% | +0.3 | OPEN |
| 2026-07-27 | JNJ | PASSED | PASS | 265.95 | 266.73 | 1 | +0.3% | +0.1 | OPEN |
| 2026-07-27 | LHX | PASSED | REPAIR | 303.48 | 305.2 | 1 | +0.6% | +0.3 | OPEN |
| 2026-07-27 | MLI | PASSED | PASS | 64.17 | 66.49 | 1 | +3.6% | +3.4 | OPEN |
| 2026-07-27 | MRK | PASSED | PASS | 130.76 | 131.82 | 1 | +0.8% | +0.6 | OPEN |
| 2026-07-27 | RHP | PASSED | PASS | 134.94 | 135.99 | 1 | +0.8% | +0.5 | OPEN |
| 2026-07-27 | SJM | PASSED | PASS | 121.05 | 123.04 | 1 | +1.6% | +1.4 | OPEN |
| 2026-07-27 | URI | PASSED | PASS | 1127.91 | 1091.26 | 1 | -3.2% | -3.5 | OPEN |

Open marks are not results. This file exists so that the cull the scan performs every night is measured instead of assumed.
