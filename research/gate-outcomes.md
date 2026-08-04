# Gate stack forward grade

Does THE GATE STACK earn its keep? Every fresh Chandelier signal is graded forward from the CLOSE of its signal date over 21 trading sessions, bucketed by what the stack decided. The number that matters is the SPREAD.

- Signal events found: 788  |  priced: 672  |  unique symbol-cohort pairs (headline sample): 271
- Skipped (pre-2026-07-22 hand-written verdicts, not machine-comparable): 20

## Headline - all signals, deduped to first appearance

| Cohort | n | Win% | Mean | Median | Mean vs SPY | Mean worst drawdown |
|---|---|---|---|---|---|---|
| PASSED | 59 | 59% | +1.70% | +1.38% | -2.02% | -5.02% |
| BLOCKED | 212 | 63% | +1.57% | +2.06% | -2.07% | -5.88% |

**Spread (PASSED minus BLOCKED): +0.13 percentage points.**

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
| ADX FLOOR | 68 | 65% | +1.69% | +1.97% | -1.87% |
| ATR GEOMETRY | 12 | 67% | +2.88% | +2.10% | -1.17% |
| DIRECTION | 15 | 53% | -2.13% | +0.17% | -5.57% |
| LIQUIDITY | 1 | 0% | -9.48% | -9.48% | -12.68% |
| OTHER | 30 | 53% | -0.64% | +0.83% | -4.09% |
| REGIME | 24 | 75% | +3.78% | +3.78% | -0.14% |
| VOLATILITY CAP (ex 2:1) | 10 | 80% | +3.75% | +4.46% | +0.74% |
| ZLSMA | 52 | 62% | +2.24% | +2.51% | -1.60% |

## Shadow cohorts - the forbidden retro-tune, run forward instead

Would lowering the ADX floor to 18, or softening DEEP-FAIL, have helped? The replay's missed monsters make that tempting; answering it by re-running history is curve-fitting. These cohorts answer it FORWARD: sole-failure near-misses graded nightly against the PASSED cohort. Promotion bar (pre-registered): >=30 MATURED signals AND mean above PASSED's - then it goes to a Friday review, not before.

| Shadow cohort | n | Win% | Mean | Median | Mean vs SPY | PASSED mean (ref) |
|---|---|---|---|---|---|---|
| ADX 18-20, all else passed | 11 | 55% | +0.41% | +0.75% | -2.75% | +1.70% |
| DEEP-FAIL, all else passed | 2 | 50% | +7.58% | +7.58% | +3.21% | +1.70% |

## Every graded signal

| Date | Sym | Cohort | Regime | Entry | Mark | Days | Return | vs SPY | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | BG | BLOCKED | n/a | 120.49 | 106.73 | 11 | -11.4% | -15.4 | OPEN |
| 2026-07-20 | CHRD | BLOCKED | n/a | 128.8 | 136.89 | 11 | +6.3% | +2.3 | OPEN |
| 2026-07-20 | CNOB | BLOCKED | n/a | 33.46 | 33.65 | 11 | +0.6% | -3.4 | OPEN |
| 2026-07-20 | COCO | BLOCKED | PASS | 73.87 | 64.38 | 11 | -12.8% | -16.8 | OPEN |
| 2026-07-20 | CVNA | BLOCKED | DEEP-FAIL | 64.14 | 68.03 | 11 | +6.1% | +2.1 | OPEN |
| 2026-07-20 | FLG | BLOCKED | n/a | 14.84 | 14.26 | 11 | -3.9% | -7.8 | OPEN |
| 2026-07-20 | FNB | BLOCKED | n/a | 18.75 | 19.38 | 11 | +3.4% | -0.6 | OPEN |
| 2026-07-20 | HAS | BLOCKED | REPAIR | 81.59 | 91.51 | 11 | +12.2% | +8.2 | OPEN |
| 2026-07-20 | HLX | BLOCKED | n/a | 9.43 | 9.6 | 11 | +1.8% | -2.1 | OPEN |
| 2026-07-20 | LCID | BLOCKED | n/a | 7.11 | 7.78 | 11 | +9.4% | +5.5 | OPEN |
| 2026-07-20 | M | BLOCKED | REPAIR | 23.31 | 26.21 | 11 | +12.4% | +8.5 | OPEN |
| 2026-07-20 | NOV | BLOCKED | REPAIR | 19.55 | 19.99 | 11 | +2.2% | -1.7 | OPEN |
| 2026-07-20 | ODFL | BLOCKED | PASS | 231.76 | 219.32 | 11 | -5.4% | -9.3 | OPEN |
| 2026-07-20 | RYZ | BLOCKED | n/a | 29.07 | 26.97 | 11 | -7.2% | -11.2 | OPEN |
| 2026-07-20 | SHAK | BLOCKED | DEEP-FAIL | 56.97 | 66.22 | 11 | +16.2% | +12.3 | OPEN |
| 2026-07-20 | SPG | BLOCKED | PASS | 228.19 | 225.9 | 11 | -1.0% | -4.9 | OPEN |
| 2026-07-20 | TRNS | BLOCKED | n/a | 86.09 | 91.89 | 11 | +6.7% | +2.8 | OPEN |
| 2026-07-20 | VVV | BLOCKED | PASS | 39.54 | 39.28 | 11 | -0.7% | -4.6 | OPEN |
| 2026-07-20 | VZ | BLOCKED | REPAIR | 43.5 | 46.88 | 11 | +7.8% | +3.8 | OPEN |
| 2026-07-20 | WPC | BLOCKED | REPAIR | 75.17 | 72.32 | 11 | -3.8% | -7.7 | OPEN |
| 2026-07-21 | ALKS | BLOCKED | TAPE OK | 52.85 | 49.67 | 10 | -6.0% | -9.1 | OPEN |
| 2026-07-21 | ATLC | BLOCKED | TAPE OK | 96.37 | 110.32 | 10 | +14.5% | +11.4 | OPEN |
| 2026-07-21 | BRKR | BLOCKED | TAPE OK | 60.43 | 50.3 | 10 | -16.8% | -19.8 | OPEN |
| 2026-07-21 | CB | BLOCKED | TAPE OK | 354.8 | 348.3 | 10 | -1.8% | -4.9 | OPEN |
| 2026-07-21 | CBL | BLOCKED | TAPE OK | 55.53 | 56.56 | 10 | +1.9% | -1.2 | OPEN |
| 2026-07-21 | CNOB | BLOCKED | TAPE OK | 33.41 | 33.65 | 10 | +0.7% | -2.4 | OPEN |
| 2026-07-21 | COCO | BLOCKED | TAPE OK | 75.89 | 64.38 | 10 | -15.2% | -18.2 | OPEN |
| 2026-07-21 | CTRE | BLOCKED | TAPE OK | 43.4 | 40.84 | 10 | -5.9% | -9.0 | OPEN |
| 2026-07-21 | ESQ | BLOCKED | TAPE OK | 122.83 | 130.31 | 10 | +6.1% | +3.0 | OPEN |
| 2026-07-21 | EXTR | BLOCKED | TAPE OK | 30.44 | 32.34 | 10 | +6.2% | +3.2 | OPEN |
| 2026-07-21 | FFIV | BLOCKED | TAPE OK | 408.74 | 412.25 | 10 | +0.9% | -2.2 | OPEN |
| 2026-07-21 | FRT | BLOCKED | TAPE OK | 125.59 | 122.82 | 10 | -2.2% | -5.3 | OPEN |
| 2026-07-21 | HCSG | BLOCKED | TAPE OK | 24.8 | 23.15 | 10 | -6.7% | -9.7 | OPEN |
| 2026-07-21 | HELE | BLOCKED | TAPE OK | 27.28 | 28.24 | 10 | +3.5% | +0.4 | OPEN |
| 2026-07-21 | HOMB | BLOCKED | TAPE OK | 30.42 | 31.41 | 10 | +3.2% | +0.2 | OPEN |
| 2026-07-21 | LQDA | BLOCKED | TAPE OK | 80.89 | 88.38 | 10 | +9.3% | +6.2 | OPEN |
| 2026-07-21 | NVRI | BLOCKED | TAPE OK | 21.87 | 23.86 | 10 | +9.1% | +6.0 | OPEN |
| 2026-07-21 | NWPX | BLOCKED | TAPE OK | 135.41 | 126.89 | 10 | -6.3% | -9.4 | OPEN |
| 2026-07-21 | OSCR | BLOCKED | TAPE OK | 30.77 | 30.38 | 10 | -1.3% | -4.3 | OPEN |
| 2026-07-21 | PNC | BLOCKED | TAPE OK | 250.38 | 254.14 | 10 | +1.5% | -1.6 | OPEN |
| 2026-07-21 | SION | BLOCKED | TAPE OK | 47.21 | 49.94 | 10 | +5.8% | +2.7 | OPEN |
| 2026-07-21 | TBLA | BLOCKED | TAPE OK | 5.11 | 5.29 | 10 | +3.5% | +0.4 | OPEN |
| 2026-07-21 | TFIN | BLOCKED | TAPE OK | 79.19 | 79.83 | 10 | +0.8% | -2.3 | OPEN |
| 2026-07-21 | TGTX | BLOCKED | TAPE OK | 53.95 | 48.74 | 10 | -9.7% | -12.8 | OPEN |
| 2026-07-21 | TVTX | BLOCKED | TAPE OK | 56.58 | 56.02 | 10 | -1.0% | -4.1 | OPEN |
| 2026-07-21 | VCYT | BLOCKED | TAPE OK | 59.53 | 46.41 | 10 | -22.0% | -25.1 | OPEN |
| 2026-07-21 | ZD | BLOCKED | TAPE OK | 52.39 | 55.38 | 10 | +5.7% | +2.6 | OPEN |
| 2026-07-21 | CYRX | PASSED | TAPE OK | 16.24 | 15.22 | 10 | -6.3% | -9.4 | OPEN |
| 2026-07-21 | FLEX | PASSED | TAPE OK | 127.39 | 126.71 | 10 | -0.5% | -3.6 | OPEN |
| 2026-07-21 | GDX | PASSED | TAPE OK | 74.19 | 77.92 | 10 | +5.0% | +1.9 | OPEN |
| 2026-07-21 | HON | PASSED | TAPE OK | 229.86 | 248.79 | 10 | +8.2% | +5.2 | OPEN |
| 2026-07-21 | KWEB | PASSED | TAPE OK | 27.02 | 28.89 | 10 | +6.9% | +3.8 | OPEN |
| 2026-07-21 | MSFT | PASSED | TAPE OK | 397.75 | 492.81 | 10 | +23.9% | +20.8 | OPEN |
| 2026-07-21 | MU | PASSED | TAPE OK | 970.82 | 892.67 | 10 | -8.1% | -11.1 | OPEN |
| 2026-07-21 | NKE | PASSED | TAPE OK | 42.96 | 41.53 | 10 | -3.3% | -6.4 | OPEN |
| 2026-07-21 | PM | PASSED | TAPE OK | 188.04 | 186.91 | 10 | -0.6% | -3.7 | OPEN |
| 2026-07-21 | SKYY | PASSED | TAPE OK | 136.02 | 153.43 | 10 | +12.8% | +9.7 | OPEN |
| 2026-07-21 | SNOW | PASSED | TAPE OK | 271.73 | 316.77 | 10 | +16.6% | +13.5 | OPEN |
| 2026-07-22 | ACTG | BLOCKED | REPAIR | 4.57 | 4.61 | 9 | +0.9% | -2.3 | OPEN |
| 2026-07-22 | AMCR | BLOCKED | PASS | 43.21 | 47.14 | 9 | +9.1% | +5.9 | OPEN |
| 2026-07-22 | AMGN | BLOCKED | PASS | 366.05 | 390.02 | 9 | +6.5% | +3.4 | OPEN |
| 2026-07-22 | ASB | BLOCKED | PASS | 30.7 | 31.75 | 9 | +3.4% | +0.2 | OPEN |
| 2026-07-22 | BCBP | BLOCKED | REPAIR | 10.29 | 9.16 | 9 | -11.0% | -14.2 | OPEN |
| 2026-07-22 | BHP | BLOCKED | REPAIR | 84.54 | 87.46 | 9 | +3.5% | +0.2 | OPEN |
| 2026-07-22 | BHRB | BLOCKED | PASS | 71.01 | 74.64 | 9 | +5.1% | +1.9 | OPEN |
| 2026-07-22 | BX | BLOCKED | REPAIR | 122.82 | 137.2 | 9 | +11.7% | +8.5 | OPEN |
| 2026-07-22 | BY | BLOCKED | PASS | 37.75 | 39.75 | 9 | +5.3% | +2.1 | OPEN |
| 2026-07-22 | CBSH | BLOCKED | PASS | 58.7 | 59.93 | 9 | +2.1% | -1.1 | OPEN |
| 2026-07-22 | CCJ | BLOCKED | DEEP-FAIL | 90.37 | 93.09 | 9 | +3.0% | -0.2 | OPEN |
| 2026-07-22 | CMP | BLOCKED | REPAIR | 30.14 | 29.81 | 9 | -1.1% | -4.3 | OPEN |
| 2026-07-22 | CNOB | BLOCKED | PASS | 33.0 | 33.65 | 9 | +2.0% | -1.2 | OPEN |
| 2026-07-22 | COKE | BLOCKED | PASS | 184.36 | 181.0 | 9 | -1.8% | -5.0 | OPEN |
| 2026-07-22 | COLB | BLOCKED | PASS | 32.63 | 31.78 | 9 | -2.6% | -5.8 | OPEN |
| 2026-07-22 | COST | BLOCKED | REPAIR | 927.31 | 947.85 | 9 | +2.2% | -1.0 | OPEN |
| 2026-07-22 | CRCL | BLOCKED | DEEP-FAIL | 66.16 | 63.25 | 9 | -4.4% | -7.6 | OPEN |
| 2026-07-22 | DE | BLOCKED | PASS | 607.33 | 617.37 | 9 | +1.6% | -1.6 | OPEN |
| 2026-07-22 | DELL | BLOCKED | PASS | 441.8 | 467.27 | 9 | +5.8% | +2.6 | OPEN |
| 2026-07-22 | DIS | BLOCKED | REPAIR | 95.87 | 98.18 | 9 | +2.4% | -0.8 | OPEN |
| 2026-07-22 | EQR | BLOCKED | PASS | 68.29 | 67.69 | 9 | -0.9% | -4.1 | OPEN |
| 2026-07-22 | F | BLOCKED | PASS | 14.42 | 14.24 | 9 | -1.2% | -4.5 | OPEN |
| 2026-07-22 | FCX | BLOCKED | PASS | 65.0 | 67.3 | 9 | +3.5% | +0.3 | OPEN |
| 2026-07-22 | FHB | BLOCKED | PASS | 28.81 | 28.25 | 9 | -1.9% | -5.1 | OPEN |
| 2026-07-22 | FITB | BLOCKED | PASS | 57.67 | 57.77 | 9 | +0.2% | -3.0 | OPEN |
| 2026-07-22 | FLEX | BLOCKED | REPAIR | 127.0 | 126.71 | 9 | -0.2% | -3.4 | OPEN |
| 2026-07-22 | FLG | BLOCKED | PASS | 14.88 | 14.26 | 9 | -4.2% | -7.4 | OPEN |
| 2026-07-22 | FNB | BLOCKED | PASS | 18.86 | 19.38 | 9 | +2.8% | -0.4 | OPEN |
| 2026-07-22 | FRT | BLOCKED | PASS | 125.05 | 122.82 | 9 | -1.8% | -5.0 | OPEN |
| 2026-07-22 | GBCI | BLOCKED | PASS | 51.17 | 50.95 | 9 | -0.4% | -3.6 | OPEN |
| 2026-07-22 | GDX | BLOCKED | DEEP-FAIL | 76.68 | 77.92 | 9 | +1.6% | -1.6 | OPEN |
| 2026-07-22 | GLD | BLOCKED | REPAIR | 379.12 | 374.16 | 9 | -1.3% | -4.5 | OPEN |
| 2026-07-22 | GM | BLOCKED | PASS | 82.13 | 88.31 | 9 | +7.5% | +4.3 | OPEN |
| 2026-07-22 | HBNC | BLOCKED | PASS | 20.21 | 20.8 | 9 | +2.9% | -0.3 | OPEN |
| 2026-07-22 | HON | BLOCKED | PASS | 232.99 | 248.79 | 9 | +6.8% | +3.6 | OPEN |
| 2026-07-22 | HOPE | BLOCKED | PASS | 13.54 | 14.36 | 9 | +6.1% | +2.9 | OPEN |
| 2026-07-22 | HSIC | BLOCKED | PASS | 84.81 | 89.11 | 9 | +5.1% | +1.9 | OPEN |
| 2026-07-22 | HTZ | BLOCKED | DEEP-FAIL | 1.93 | 1.51 | 9 | -21.8% | -25.0 | OPEN |
| 2026-07-22 | KRE | BLOCKED | PASS | 75.6 | 77.84 | 9 | +3.0% | -0.2 | OPEN |
| 2026-07-22 | LCID | BLOCKED | DEEP-FAIL | 6.78 | 7.78 | 9 | +14.8% | +11.6 | OPEN |
| 2026-07-22 | LZB | BLOCKED | PASS | 39.3 | 41.73 | 9 | +6.2% | +3.0 | OPEN |
| 2026-07-22 | M | BLOCKED | PASS | 24.33 | 26.21 | 9 | +7.7% | +4.5 | OPEN |
| 2026-07-22 | MFA | BLOCKED | REPAIR | 9.29 | 9.09 | 9 | -2.1% | -5.3 | OPEN |
| 2026-07-22 | MU | BLOCKED | PASS | 959.48 | 892.67 | 9 | -7.0% | -10.2 | OPEN |
| 2026-07-22 | NEE | BLOCKED | PASS | 89.41 | 87.2 | 9 | -2.5% | -5.7 | OPEN |
| 2026-07-22 | NEM | BLOCKED | REPAIR | 95.75 | 97.73 | 9 | +2.1% | -1.1 | OPEN |
| 2026-07-22 | OCFC | BLOCKED | PASS | 19.67 | 19.81 | 9 | +0.7% | -2.5 | OPEN |
| 2026-07-22 | PANW | BLOCKED | PASS | 335.28 | 366.34 | 9 | +9.3% | +6.1 | OPEN |
| 2026-07-22 | PB | BLOCKED | PASS | 73.06 | 74.89 | 9 | +2.5% | -0.7 | OPEN |
| 2026-07-22 | PM | BLOCKED | PASS | 194.3 | 186.91 | 9 | -3.8% | -7.0 | OPEN |
| 2026-07-22 | POWL | BLOCKED | REPAIR | 240.68 | 211.38 | 9 | -12.2% | -15.4 | OPEN |
| 2026-07-22 | PRLB | BLOCKED | PASS | 79.73 | 88.4 | 9 | +10.9% | +7.7 | OPEN |
| 2026-07-22 | RACE | BLOCKED | REPAIR | 371.61 | 402.79 | 9 | +8.4% | +5.2 | OPEN |
| 2026-07-22 | RCL | BLOCKED | REPAIR | 285.85 | 325.74 | 9 | +13.9% | +10.8 | OPEN |
| 2026-07-22 | RSPU | BLOCKED | PASS | 81.85 | 78.27 | 9 | -4.4% | -7.6 | OPEN |
| 2026-07-22 | SAIC | BLOCKED | PASS | 115.95 | 120.37 | 9 | +3.8% | +0.6 | OPEN |
| 2026-07-22 | SJM | BLOCKED | PASS | 118.05 | 119.17 | 9 | +0.9% | -2.2 | OPEN |
| 2026-07-22 | SKK | BLOCKED | PASS | 5.22 | 4.72 | 9 | -9.5% | -12.7 | OPEN |
| 2026-07-22 | SMCI | BLOCKED | REPAIR | 30.56 | 31.69 | 9 | +3.7% | +0.5 | OPEN |
| 2026-07-22 | SON | BLOCKED | PASS | 55.15 | 58.62 | 9 | +6.3% | +3.1 | OPEN |
| 2026-07-22 | SPG | BLOCKED | PASS | 226.22 | 225.9 | 9 | -0.1% | -3.3 | OPEN |
| 2026-07-22 | SSB | BLOCKED | PASS | 102.19 | 109.43 | 9 | +7.1% | +3.9 | OPEN |
| 2026-07-22 | STRL | BLOCKED | REPAIR | 719.34 | 541.62 | 9 | -24.7% | -27.9 | OPEN |
| 2026-07-22 | STX | BLOCKED | PASS | 908.1 | 845.35 | 9 | -6.9% | -10.1 | OPEN |
| 2026-07-22 | TDY | BLOCKED | PASS | 650.5 | 684.76 | 9 | +5.3% | +2.1 | OPEN |
| 2026-07-22 | TPL | BLOCKED | PASS | 433.1 | 395.52 | 9 | -8.7% | -11.9 | OPEN |
| 2026-07-22 | TPR | BLOCKED | PASS | 143.73 | 155.97 | 9 | +8.5% | +5.3 | OPEN |
| 2026-07-22 | URA | BLOCKED | DEEP-FAIL | 40.97 | 42.49 | 9 | +3.7% | +0.5 | OPEN |
| 2026-07-22 | USB | BLOCKED | PASS | 64.47 | 64.23 | 9 | -0.4% | -3.6 | OPEN |
| 2026-07-22 | VST | BLOCKED | REPAIR | 166.74 | 143.23 | 9 | -14.1% | -17.3 | OPEN |
| 2026-07-22 | VVV | BLOCKED | PASS | 39.03 | 39.28 | 9 | +0.6% | -2.6 | OPEN |
| 2026-07-22 | CTRE | PASSED | PASS | 42.38 | 40.84 | 9 | -3.6% | -6.8 | OPEN |
| 2026-07-22 | PFE | PASSED | REPAIR | 24.82 | 25.41 | 9 | +2.4% | -0.8 | OPEN |
| 2026-07-22 | TJX | PASSED | REPAIR | 155.41 | 157.55 | 9 | +1.4% | -1.8 | OPEN |
| 2026-07-22 | TXNM | PASSED | REPAIR | 58.3 | 57.6 | 9 | -1.2% | -4.4 | OPEN |
| 2026-07-22 | VZ | PASSED | REPAIR | 44.29 | 46.88 | 9 | +5.8% | +2.6 | OPEN |
| 2026-07-23 | ACTG | BLOCKED | REPAIR | 4.62 | 4.61 | 8 | -0.2% | -4.7 | OPEN |
| 2026-07-23 | ALSN | BLOCKED | PASS | 119.64 | 122.62 | 8 | +2.5% | -2.0 | OPEN |
| 2026-07-23 | AVT | BLOCKED | PASS | 89.92 | 92.53 | 8 | +2.9% | -1.6 | OPEN |
| 2026-07-23 | BUD | BLOCKED | REPAIR | 80.48 | 84.59 | 8 | +5.1% | +0.6 | OPEN |
| 2026-07-23 | COST | BLOCKED | REPAIR | 926.06 | 947.85 | 8 | +2.4% | -2.1 | OPEN |
| 2026-07-23 | CRCL | BLOCKED | DEEP-FAIL | 62.18 | 63.25 | 8 | +1.7% | -2.8 | OPEN |
| 2026-07-23 | DELL | BLOCKED | PASS | 439.34 | 467.27 | 8 | +6.4% | +1.9 | OPEN |
| 2026-07-23 | DGX | BLOCKED | PASS | 227.9 | 233.72 | 8 | +2.5% | -1.9 | OPEN |
| 2026-07-23 | F | BLOCKED | REPAIR | 14.15 | 14.24 | 8 | +0.6% | -3.9 | OPEN |
| 2026-07-23 | FCX | BLOCKED | REPAIR | 63.5 | 67.3 | 8 | +6.0% | +1.5 | OPEN |
| 2026-07-23 | FLG | BLOCKED | PASS | 14.71 | 14.26 | 8 | -3.1% | -7.5 | OPEN |
| 2026-07-23 | FNB | BLOCKED | PASS | 18.87 | 19.38 | 8 | +2.7% | -1.8 | OPEN |
| 2026-07-23 | FUTU | BLOCKED | DEEP-FAIL | 98.96 | 109.0 | 8 | +10.2% | +5.7 | OPEN |
| 2026-07-23 | GDX | BLOCKED | DEEP-FAIL | 75.02 | 77.92 | 8 | +3.9% | -0.6 | OPEN |
| 2026-07-23 | GLD | BLOCKED | REPAIR | 371.52 | 374.16 | 8 | +0.7% | -3.8 | OPEN |
| 2026-07-23 | GM | BLOCKED | PASS | 80.67 | 88.31 | 8 | +9.5% | +5.0 | OPEN |
| 2026-07-23 | HON | BLOCKED | PASS | 246.27 | 248.79 | 8 | +1.0% | -3.5 | OPEN |
| 2026-07-23 | IRM | BLOCKED | REPAIR | 124.55 | 125.51 | 8 | +0.8% | -3.7 | OPEN |
| 2026-07-23 | LCID | BLOCKED | DEEP-FAIL | 6.45 | 7.78 | 8 | +20.6% | +16.1 | OPEN |
| 2026-07-23 | LSTR | BLOCKED | PASS | 207.97 | 181.62 | 8 | -12.7% | -17.2 | OPEN |
| 2026-07-23 | M | BLOCKED | PASS | 23.33 | 26.21 | 8 | +12.3% | +7.8 | OPEN |
| 2026-07-23 | MAC | BLOCKED | PASS | 25.3 | 25.62 | 8 | +1.3% | -3.2 | OPEN |
| 2026-07-23 | NEM | BLOCKED | REPAIR | 94.72 | 97.73 | 8 | +3.2% | -1.3 | OPEN |
| 2026-07-23 | PLD | BLOCKED | PASS | 145.12 | 139.05 | 8 | -4.2% | -8.7 | OPEN |
| 2026-07-23 | PRLB | BLOCKED | PASS | 78.62 | 88.4 | 8 | +12.4% | +8.0 | OPEN |
| 2026-07-23 | RHP | BLOCKED | PASS | 128.89 | 128.2 | 8 | -0.5% | -5.0 | OPEN |
| 2026-07-23 | SMCI | BLOCKED | REPAIR | 31.2 | 31.69 | 8 | +1.6% | -2.9 | OPEN |
| 2026-07-23 | SON | BLOCKED | PASS | 56.32 | 58.62 | 8 | +4.1% | -0.4 | OPEN |
| 2026-07-23 | SPG | BLOCKED | PASS | 225.2 | 225.9 | 8 | +0.3% | -4.2 | OPEN |
| 2026-07-23 | TDY | BLOCKED | PASS | 651.22 | 684.76 | 8 | +5.2% | +0.7 | OPEN |
| 2026-07-23 | URA | BLOCKED | DEEP-FAIL | 41.13 | 42.49 | 8 | +3.3% | -1.2 | OPEN |
| 2026-07-23 | URI | BLOCKED | PASS | 1139.71 | 1150.13 | 8 | +0.9% | -3.6 | OPEN |
| 2026-07-23 | VST | BLOCKED | REPAIR | 168.98 | 143.23 | 8 | -15.2% | -19.7 | OPEN |
| 2026-07-23 | VVV | BLOCKED | PASS | 38.31 | 39.28 | 8 | +2.5% | -2.0 | OPEN |
| 2026-07-23 | ECVT | PASSED | PASS | 12.89 | 12.11 | 8 | -6.0% | -10.5 | OPEN |
| 2026-07-23 | FRT | PASSED | PASS | 124.83 | 122.82 | 8 | -1.6% | -6.1 | OPEN |
| 2026-07-23 | HAS | PASSED | PASS | 87.35 | 91.51 | 8 | +4.8% | +0.3 | OPEN |
| 2026-07-23 | LHX | PASSED | REPAIR | 299.67 | 285.3 | 8 | -4.8% | -9.3 | OPEN |
| 2026-07-23 | MLI | PASSED | REPAIR | 63.13 | 68.35 | 8 | +8.3% | +3.8 | OPEN |
| 2026-07-23 | PFE | PASSED | REPAIR | 25.01 | 25.41 | 8 | +1.6% | -2.9 | OPEN |
| 2026-07-23 | SJM | PASSED | PASS | 115.71 | 119.17 | 8 | +3.0% | -1.5 | OPEN |
| 2026-07-23 | VZ | PASSED | REPAIR | 43.82 | 46.88 | 8 | +7.0% | +2.5 | OPEN |
| 2026-07-24 | ALSN | BLOCKED | PASS | 122.34 | 122.62 | 7 | +0.2% | -4.2 | OPEN |
| 2026-07-24 | AVT | BLOCKED | PASS | 89.42 | 92.53 | 7 | +3.5% | -0.9 | OPEN |
| 2026-07-24 | BUD | BLOCKED | REPAIR | 81.66 | 84.59 | 7 | +3.6% | -0.8 | OPEN |
| 2026-07-24 | CB | BLOCKED | PASS | 359.75 | 348.3 | 7 | -3.2% | -7.6 | OPEN |
| 2026-07-24 | CNP | BLOCKED | PASS | 44.56 | 41.58 | 7 | -6.7% | -11.1 | OPEN |
| 2026-07-24 | COST | BLOCKED | REPAIR | 935.03 | 947.85 | 7 | +1.4% | -3.0 | OPEN |
| 2026-07-24 | CRCL | BLOCKED | DEEP-FAIL | 62.36 | 63.25 | 7 | +1.4% | -3.0 | OPEN |
| 2026-07-24 | DE | BLOCKED | PASS | 628.16 | 617.37 | 7 | -1.7% | -6.1 | OPEN |
| 2026-07-24 | DGX | BLOCKED | PASS | 227.86 | 233.72 | 7 | +2.6% | -1.8 | OPEN |
| 2026-07-24 | DLR | BLOCKED | PASS | 199.08 | 193.89 | 7 | -2.6% | -7.0 | OPEN |
| 2026-07-24 | EGBN | BLOCKED | PASS | 28.44 | 28.36 | 7 | -0.3% | -4.7 | OPEN |
| 2026-07-24 | F | BLOCKED | REPAIR | 14.37 | 14.24 | 7 | -0.9% | -5.3 | OPEN |
| 2026-07-24 | FCX | BLOCKED | REPAIR | 62.6 | 67.3 | 7 | +7.5% | +3.1 | OPEN |
| 2026-07-24 | FUTU | BLOCKED | DEEP-FAIL | 99.36 | 109.0 | 7 | +9.7% | +5.3 | OPEN |
| 2026-07-24 | GDX | BLOCKED | DEEP-FAIL | 75.23 | 77.92 | 7 | +3.6% | -0.8 | OPEN |
| 2026-07-24 | GE | BLOCKED | PASS | 353.73 | 377.28 | 7 | +6.7% | +2.3 | OPEN |
| 2026-07-24 | GLD | BLOCKED | REPAIR | 371.9 | 374.16 | 7 | +0.6% | -3.8 | OPEN |
| 2026-07-24 | GM | BLOCKED | PASS | 82.64 | 88.31 | 7 | +6.9% | +2.5 | OPEN |
| 2026-07-24 | HON | BLOCKED | PASS | 243.15 | 248.79 | 7 | +2.3% | -2.1 | OPEN |
| 2026-07-24 | IRM | BLOCKED | PASS | 128.31 | 125.51 | 7 | -2.2% | -6.6 | OPEN |
| 2026-07-24 | JNJ | BLOCKED | PASS | 263.4 | 254.93 | 7 | -3.2% | -7.6 | OPEN |
| 2026-07-24 | LCID | BLOCKED | DEEP-FAIL | 6.3 | 7.78 | 7 | +23.5% | +19.1 | OPEN |
| 2026-07-24 | LDOS | BLOCKED | DEEP-FAIL | 112.14 | 130.6 | 7 | +16.5% | +12.1 | OPEN |
| 2026-07-24 | LIND | BLOCKED | PASS | 26.85 | 34.09 | 7 | +27.0% | +22.6 | OPEN |
| 2026-07-24 | M | BLOCKED | PASS | 23.38 | 26.21 | 7 | +12.1% | +7.7 | OPEN |
| 2026-07-24 | NEM | BLOCKED | REPAIR | 93.19 | 97.73 | 7 | +4.9% | +0.5 | OPEN |
| 2026-07-24 | ORKA | BLOCKED | PASS | 92.16 | 98.13 | 7 | +6.5% | +2.1 | OPEN |
| 2026-07-24 | PH | BLOCKED | PASS | 987.54 | 992.65 | 7 | +0.5% | -3.9 | OPEN |
| 2026-07-24 | PRLB | BLOCKED | PASS | 78.24 | 88.4 | 7 | +13.0% | +8.6 | OPEN |
| 2026-07-24 | ROP | BLOCKED | REPAIR | 367.34 | 392.76 | 7 | +6.9% | +2.5 | OPEN |
| 2026-07-24 | RSPU | BLOCKED | PASS | 82.33 | 78.27 | 7 | -4.9% | -9.3 | OPEN |
| 2026-07-24 | SMCI | BLOCKED | REPAIR | 30.1 | 31.69 | 7 | +5.3% | +0.9 | OPEN |
| 2026-07-24 | SON | BLOCKED | PASS | 58.23 | 58.62 | 7 | +0.7% | -3.7 | OPEN |
| 2026-07-24 | SPG | BLOCKED | PASS | 229.78 | 225.9 | 7 | -1.7% | -6.1 | OPEN |
| 2026-07-24 | TDY | BLOCKED | PASS | 655.35 | 684.76 | 7 | +4.5% | +0.1 | OPEN |
| 2026-07-24 | URA | BLOCKED | DEEP-FAIL | 39.89 | 42.49 | 7 | +6.5% | +2.1 | OPEN |
| 2026-07-24 | URI | BLOCKED | PASS | 1141.59 | 1150.13 | 7 | +0.8% | -3.6 | OPEN |
| 2026-07-24 | VST | BLOCKED | REPAIR | 163.38 | 143.23 | 7 | -12.3% | -16.7 | OPEN |
| 2026-07-24 | XLI | BLOCKED | PASS | 182.66 | 186.4 | 7 | +2.0% | -2.3 | OPEN |
| 2026-07-24 | ACTG | PASSED | PASS | 4.66 | 4.61 | 7 | -1.1% | -5.5 | OPEN |
| 2026-07-24 | DELL | PASSED | PASS | 437.5 | 467.27 | 7 | +6.8% | +2.4 | OPEN |
| 2026-07-24 | EQIX | PASSED | PASS | 1084.24 | 1051.53 | 7 | -3.0% | -7.4 | OPEN |
| 2026-07-24 | LHX | PASSED | REPAIR | 300.21 | 285.3 | 7 | -5.0% | -9.3 | OPEN |
| 2026-07-24 | MLI | PASSED | REPAIR | 63.91 | 68.35 | 7 | +7.0% | +2.6 | OPEN |
| 2026-07-24 | MRK | PASSED | PASS | 131.07 | 128.0 | 7 | -2.3% | -6.7 | OPEN |
| 2026-07-24 | RHP | PASSED | PASS | 133.09 | 128.2 | 7 | -3.7% | -8.1 | OPEN |
| 2026-07-24 | SJM | PASSED | PASS | 118.32 | 119.17 | 7 | +0.7% | -3.7 | OPEN |
| 2026-07-24 | VZ | PASSED | REPAIR | 46.38 | 46.88 | 7 | +1.1% | -3.3 | OPEN |
| 2026-07-27 | ACGL | BLOCKED | PASS | 103.88 | 99.52 | 6 | -4.2% | -8.6 | OPEN |
| 2026-07-27 | ALSN | BLOCKED | PASS | 121.91 | 122.62 | 6 | +0.6% | -3.8 | OPEN |
| 2026-07-27 | AVT | BLOCKED | PASS | 88.38 | 92.53 | 6 | +4.7% | +0.3 | OPEN |
| 2026-07-27 | BUD | BLOCKED | REPAIR | 80.87 | 84.59 | 6 | +4.6% | +0.2 | OPEN |
| 2026-07-27 | CB | BLOCKED | PASS | 358.91 | 348.3 | 6 | -3.0% | -7.3 | OPEN |
| 2026-07-27 | CPRT | BLOCKED | DEEP-FAIL | 29.79 | 29.4 | 6 | -1.3% | -5.7 | OPEN |
| 2026-07-27 | CRCL | BLOCKED | DEEP-FAIL | 65.67 | 63.25 | 6 | -3.7% | -8.1 | OPEN |
| 2026-07-27 | DE | BLOCKED | PASS | 625.02 | 617.37 | 6 | -1.2% | -5.6 | OPEN |
| 2026-07-27 | DLR | BLOCKED | PASS | 195.76 | 193.89 | 6 | -1.0% | -5.3 | OPEN |
| 2026-07-27 | EGBN | BLOCKED | PASS | 28.15 | 28.36 | 6 | +0.8% | -3.6 | OPEN |
| 2026-07-27 | F | BLOCKED | PASS | 14.68 | 14.24 | 6 | -3.0% | -7.4 | OPEN |
| 2026-07-27 | FCX | BLOCKED | REPAIR | 62.72 | 67.3 | 6 | +7.3% | +2.9 | OPEN |
| 2026-07-27 | FUTU | BLOCKED | DEEP-FAIL | 104.27 | 109.0 | 6 | +4.5% | +0.2 | OPEN |
| 2026-07-27 | GDX | BLOCKED | DEEP-FAIL | 75.73 | 77.92 | 6 | +2.9% | -1.5 | OPEN |
| 2026-07-27 | GLD | BLOCKED | REPAIR | 374.63 | 374.16 | 6 | -0.1% | -4.5 | OPEN |
| 2026-07-27 | GM | BLOCKED | PASS | 87.04 | 88.31 | 6 | +1.5% | -2.9 | OPEN |
| 2026-07-27 | HON | BLOCKED | PASS | 245.75 | 248.79 | 6 | +1.2% | -3.1 | OPEN |
| 2026-07-27 | IRM | BLOCKED | PASS | 126.99 | 125.51 | 6 | -1.2% | -5.5 | OPEN |
| 2026-07-27 | LDOS | BLOCKED | DEEP-FAIL | 114.95 | 130.6 | 6 | +13.6% | +9.2 | OPEN |
| 2026-07-27 | LIND | BLOCKED | PASS | 28.09 | 34.09 | 6 | +21.4% | +17.0 | OPEN |
| 2026-07-27 | MAR | BLOCKED | PASS | 383.06 | 345.2 | 6 | -9.9% | -14.2 | OPEN |
| 2026-07-27 | NEM | BLOCKED | REPAIR | 93.47 | 97.73 | 6 | +4.6% | +0.2 | OPEN |
| 2026-07-27 | ORKA | BLOCKED | PASS | 90.2 | 98.13 | 6 | +8.8% | +4.4 | OPEN |
| 2026-07-27 | PGR | BLOCKED | REPAIR | 215.76 | 210.75 | 6 | -2.3% | -6.7 | OPEN |
| 2026-07-27 | PH | BLOCKED | PASS | 987.31 | 992.65 | 6 | +0.5% | -3.8 | OPEN |
| 2026-07-27 | PRLB | BLOCKED | PASS | 77.64 | 88.4 | 6 | +13.9% | +9.5 | OPEN |
| 2026-07-27 | RCL | BLOCKED | REPAIR | 305.04 | 325.74 | 6 | +6.8% | +2.4 | OPEN |
| 2026-07-27 | ROP | BLOCKED | REPAIR | 375.02 | 392.76 | 6 | +4.7% | +0.4 | OPEN |
| 2026-07-27 | RSPU | BLOCKED | PASS | 81.24 | 78.27 | 6 | -3.7% | -8.0 | OPEN |
| 2026-07-27 | SLB | BLOCKED | PASS | 51.53 | 50.81 | 6 | -1.4% | -5.8 | OPEN |
| 2026-07-27 | SMCI | BLOCKED | DEEP-FAIL | 29.81 | 31.69 | 6 | +6.3% | +1.9 | OPEN |
| 2026-07-27 | SON | BLOCKED | PASS | 58.68 | 58.62 | 6 | -0.1% | -4.5 | OPEN |
| 2026-07-27 | TDY | BLOCKED | PASS | 651.65 | 684.76 | 6 | +5.1% | +0.7 | OPEN |
| 2026-07-27 | TJX | BLOCKED | REPAIR | 156.38 | 157.55 | 6 | +0.8% | -3.6 | OPEN |
| 2026-07-27 | URA | BLOCKED | DEEP-FAIL | 40.32 | 42.49 | 6 | +5.4% | +1.0 | OPEN |
| 2026-07-27 | VRSN | BLOCKED | REPAIR | 274.82 | 299.2 | 6 | +8.9% | +4.5 | OPEN |
| 2026-07-27 | VST | BLOCKED | REPAIR | 157.08 | 143.23 | 6 | -8.8% | -13.2 | OPEN |
| 2026-07-27 | WWD | BLOCKED | PASS | 419.76 | 373.67 | 6 | -11.0% | -15.3 | OPEN |
| 2026-07-27 | XLI | BLOCKED | PASS | 183.2 | 186.4 | 6 | +1.8% | -2.6 | OPEN |
| 2026-07-27 | ACTG | PASSED | PASS | 4.63 | 4.61 | 6 | -0.4% | -4.8 | OPEN |
| 2026-07-27 | DELL | PASSED | PASS | 426.91 | 467.27 | 6 | +9.4% | +5.1 | OPEN |
| 2026-07-27 | DGX | PASSED | PASS | 231.84 | 233.72 | 6 | +0.8% | -3.5 | OPEN |
| 2026-07-27 | EQIX | PASSED | PASS | 1046.79 | 1051.53 | 6 | +0.5% | -3.9 | OPEN |
| 2026-07-27 | GE | PASSED | PASS | 361.61 | 377.28 | 6 | +4.3% | -0.0 | OPEN |
| 2026-07-27 | JNJ | PASSED | PASS | 265.95 | 254.93 | 6 | -4.1% | -8.5 | OPEN |
| 2026-07-27 | LHX | PASSED | REPAIR | 303.48 | 285.3 | 6 | -6.0% | -10.3 | OPEN |
| 2026-07-27 | MLI | PASSED | PASS | 64.17 | 68.35 | 6 | +6.5% | +2.1 | OPEN |
| 2026-07-27 | MRK | PASSED | PASS | 130.76 | 128.0 | 6 | -2.1% | -6.5 | OPEN |
| 2026-07-27 | RHP | PASSED | PASS | 134.94 | 128.2 | 6 | -5.0% | -9.4 | OPEN |
| 2026-07-27 | SJM | PASSED | PASS | 121.05 | 119.17 | 6 | -1.6% | -5.9 | OPEN |
| 2026-07-27 | URI | PASSED | PASS | 1127.91 | 1150.13 | 6 | +2.0% | -2.4 | OPEN |
| 2026-07-28 | ACGL | BLOCKED | PASS | 106.48 | 99.52 | 5 | -6.5% | -10.7 | OPEN |
| 2026-07-28 | AGNC | BLOCKED | PASS | 11.07 | 10.64 | 5 | -3.9% | -8.0 | OPEN |
| 2026-07-28 | AI | BLOCKED | DEEP-FAIL | 8.9 | 10.05 | 5 | +12.9% | +8.8 | OPEN |
| 2026-07-28 | AJG | BLOCKED | REPAIR | 265.31 | 248.06 | 5 | -6.5% | -10.6 | OPEN |
| 2026-07-28 | ALSN | BLOCKED | PASS | 121.11 | 122.62 | 5 | +1.2% | -2.9 | OPEN |
| 2026-07-28 | AVT | BLOCKED | REPAIR | 86.22 | 92.53 | 5 | +7.3% | +3.2 | OPEN |
| 2026-07-28 | AXON | BLOCKED | REPAIR | 547.65 | 607.2 | 5 | +10.9% | +6.8 | OPEN |
| 2026-07-28 | BUD | BLOCKED | PASS | 83.2 | 84.59 | 5 | +1.7% | -2.4 | OPEN |
| 2026-07-28 | CB | BLOCKED | PASS | 363.5 | 348.3 | 5 | -4.2% | -8.3 | OPEN |
| 2026-07-28 | CCL | BLOCKED | REPAIR | 28.23 | 29.59 | 5 | +4.8% | +0.7 | OPEN |
| 2026-07-28 | CHTR | BLOCKED | DEEP-FAIL | 139.97 | 153.07 | 5 | +9.4% | +5.2 | OPEN |
| 2026-07-28 | CLX | BLOCKED | REPAIR | 100.32 | 104.67 | 5 | +4.3% | +0.2 | OPEN |
| 2026-07-28 | CNP | BLOCKED | PASS | 44.1 | 41.58 | 5 | -5.7% | -9.8 | OPEN |
| 2026-07-28 | COKE | BLOCKED | PASS | 195.0 | 181.0 | 5 | -7.2% | -11.3 | OPEN |
| 2026-07-28 | CPRT | BLOCKED | DEEP-FAIL | 30.69 | 29.4 | 5 | -4.2% | -8.3 | OPEN |
| 2026-07-28 | CRCL | BLOCKED | DEEP-FAIL | 64.32 | 63.25 | 5 | -1.7% | -5.8 | OPEN |
| 2026-07-28 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.79 | 5 | +11.7% | +7.6 | OPEN |
| 2026-07-28 | DASH | BLOCKED | REPAIR | 195.52 | 202.37 | 5 | +3.5% | -0.6 | OPEN |
| 2026-07-28 | DUOL | BLOCKED | REPAIR | 140.73 | 137.75 | 5 | -2.1% | -6.2 | OPEN |
| 2026-07-28 | EGBN | BLOCKED | PASS | 28.39 | 28.36 | 5 | -0.1% | -4.2 | OPEN |
| 2026-07-28 | ERIE | BLOCKED | REPAIR | 242.43 | 244.53 | 5 | +0.9% | -3.2 | OPEN |
| 2026-07-28 | F | BLOCKED | PASS | 14.96 | 14.24 | 5 | -4.8% | -8.9 | OPEN |
| 2026-07-28 | FCX | BLOCKED | REPAIR | 61.64 | 67.3 | 5 | +9.2% | +5.1 | OPEN |
| 2026-07-28 | FUTU | BLOCKED | DEEP-FAIL | 101.84 | 109.0 | 5 | +7.0% | +2.9 | OPEN |
| 2026-07-28 | GDX | BLOCKED | DEEP-FAIL | 74.21 | 77.92 | 5 | +5.0% | +0.9 | OPEN |
| 2026-07-28 | GLD | BLOCKED | DEEP-FAIL | 369.37 | 374.16 | 5 | +1.3% | -2.8 | OPEN |
| 2026-07-28 | GM | BLOCKED | PASS | 90.3 | 88.31 | 5 | -2.2% | -6.3 | OPEN |
| 2026-07-28 | HD | BLOCKED | REPAIR | 344.47 | 348.24 | 5 | +1.1% | -3.0 | OPEN |
| 2026-07-28 | JETS | BLOCKED | PASS | 31.86 | 33.4 | 5 | +4.8% | +0.7 | OPEN |
| 2026-07-28 | LDOS | BLOCKED | DEEP-FAIL | 118.36 | 130.6 | 5 | +10.3% | +6.2 | OPEN |
| 2026-07-28 | LOW | BLOCKED | REPAIR | 218.24 | 218.08 | 5 | -0.1% | -4.2 | OPEN |
| 2026-07-28 | LZB | BLOCKED | PASS | 41.3 | 41.73 | 5 | +1.0% | -3.1 | OPEN |
| 2026-07-28 | MAR | BLOCKED | PASS | 383.52 | 345.2 | 5 | -10.0% | -14.1 | OPEN |
| 2026-07-28 | MCD | BLOCKED | REPAIR | 273.02 | 268.34 | 5 | -1.7% | -5.8 | OPEN |
| 2026-07-28 | MDT | BLOCKED | REPAIR | 86.88 | 86.2 | 5 | -0.8% | -4.9 | OPEN |
| 2026-07-28 | NCLH | BLOCKED | REPAIR | 21.22 | 20.07 | 5 | -5.4% | -9.5 | OPEN |
| 2026-07-28 | NEM | BLOCKED | DEEP-FAIL | 91.52 | 97.73 | 5 | +6.8% | +2.7 | OPEN |
| 2026-07-28 | NFLX | BLOCKED | DEEP-FAIL | 72.39 | 73.57 | 5 | +1.6% | -2.5 | OPEN |
| 2026-07-28 | NOW | BLOCKED | DEEP-FAIL | 110.62 | 118.14 | 5 | +6.8% | +2.7 | OPEN |
| 2026-07-28 | PGR | BLOCKED | REPAIR | 219.52 | 210.75 | 5 | -4.0% | -8.1 | OPEN |
| 2026-07-28 | PH | BLOCKED | PASS | 990.96 | 992.65 | 5 | +0.2% | -3.9 | OPEN |
| 2026-07-28 | RACE | BLOCKED | REPAIR | 390.14 | 402.79 | 5 | +3.2% | -0.9 | OPEN |
| 2026-07-28 | RCL | BLOCKED | REPAIR | 322.5 | 325.74 | 5 | +1.0% | -3.1 | OPEN |
| 2026-07-28 | RMD | BLOCKED | DEEP-FAIL | 208.96 | 223.14 | 5 | +6.8% | +2.7 | OPEN |
| 2026-07-28 | ROP | BLOCKED | REPAIR | 390.92 | 392.76 | 5 | +0.5% | -3.6 | OPEN |
| 2026-07-28 | RSPU | BLOCKED | PASS | 81.03 | 78.27 | 5 | -3.4% | -7.5 | OPEN |
| 2026-07-28 | SHAK | BLOCKED | DEEP-FAIL | 63.2 | 66.22 | 5 | +4.8% | +0.7 | OPEN |
| 2026-07-28 | SHW | BLOCKED | REPAIR | 354.27 | 361.57 | 5 | +2.1% | -2.0 | OPEN |
| 2026-07-28 | SMCI | BLOCKED | DEEP-FAIL | 28.45 | 31.69 | 5 | +11.4% | +7.3 | OPEN |
| 2026-07-28 | SON | BLOCKED | PASS | 60.56 | 58.62 | 5 | -3.2% | -7.3 | OPEN |
| 2026-07-28 | STGW | BLOCKED | PASS | 7.97 | 9.01 | 5 | +13.1% | +8.9 | OPEN |
| 2026-07-28 | TDY | BLOCKED | PASS | 649.67 | 684.76 | 5 | +5.4% | +1.3 | OPEN |
| 2026-07-28 | TOST | BLOCKED | REPAIR | 32.34 | 33.81 | 5 | +4.5% | +0.4 | OPEN |
| 2026-07-28 | TPR | BLOCKED | PASS | 150.9 | 155.97 | 5 | +3.4% | -0.8 | OPEN |
| 2026-07-28 | TYL | BLOCKED | DEEP-FAIL | 333.35 | 313.33 | 5 | -6.0% | -10.1 | OPEN |
| 2026-07-28 | URA | BLOCKED | DEEP-FAIL | 38.95 | 42.49 | 5 | +9.1% | +5.0 | OPEN |
| 2026-07-28 | URI | BLOCKED | PASS | 1091.26 | 1150.13 | 5 | +5.4% | +1.3 | OPEN |
| 2026-07-28 | VRSN | BLOCKED | REPAIR | 281.15 | 299.2 | 5 | +6.4% | +2.3 | OPEN |
| 2026-07-28 | WWD | BLOCKED | PASS | 410.55 | 373.67 | 5 | -9.0% | -13.1 | OPEN |
| 2026-07-28 | XLI | BLOCKED | PASS | 182.49 | 186.4 | 5 | +2.1% | -2.0 | OPEN |
| 2026-07-28 | ZTS | BLOCKED | DEEP-FAIL | 77.51 | 76.04 | 5 | -1.9% | -6.0 | OPEN |
| 2026-07-28 | ACTG | PASSED | PASS | 4.63 | 4.61 | 5 | -0.4% | -4.5 | OPEN |
| 2026-07-28 | CTS | PASSED | PASS | 64.82 | 67.26 | 5 | +3.8% | -0.3 | OPEN |
| 2026-07-28 | DAL | PASSED | PASS | 89.37 | 92.77 | 5 | +3.8% | -0.3 | OPEN |
| 2026-07-28 | DE | PASSED | PASS | 639.84 | 617.37 | 5 | -3.5% | -7.6 | OPEN |
| 2026-07-28 | DGX | PASSED | PASS | 235.94 | 233.72 | 5 | -0.9% | -5.0 | OPEN |
| 2026-07-28 | DLR | PASSED | PASS | 193.18 | 193.89 | 5 | +0.4% | -3.8 | OPEN |
| 2026-07-28 | EQIX | PASSED | REPAIR | 1034.86 | 1051.53 | 5 | +1.6% | -2.5 | OPEN |
| 2026-07-28 | GE | PASSED | PASS | 363.59 | 377.28 | 5 | +3.8% | -0.3 | OPEN |
| 2026-07-28 | HON | PASSED | PASS | 247.05 | 248.79 | 5 | +0.7% | -3.4 | OPEN |
| 2026-07-28 | JNJ | PASSED | PASS | 266.73 | 254.93 | 5 | -4.4% | -8.5 | OPEN |
| 2026-07-28 | LHX | PASSED | REPAIR | 305.2 | 285.3 | 5 | -6.5% | -10.6 | OPEN |
| 2026-07-28 | LLY | PASSED | PASS | 1220.66 | 1115.68 | 5 | -8.6% | -12.7 | OPEN |
| 2026-07-28 | MLI | PASSED | PASS | 66.49 | 68.35 | 5 | +2.8% | -1.3 | OPEN |
| 2026-07-28 | MNST | PASSED | PASS | 97.74 | 94.18 | 5 | -3.6% | -7.8 | OPEN |
| 2026-07-28 | MRK | PASSED | PASS | 131.82 | 128.0 | 5 | -2.9% | -7.0 | OPEN |
| 2026-07-28 | PEP | PASSED | REPAIR | 142.86 | 139.1 | 5 | -2.6% | -6.7 | OPEN |
| 2026-07-28 | SLB | PASSED | REPAIR | 49.98 | 50.81 | 5 | +1.7% | -2.5 | OPEN |
| 2026-07-28 | SSD | PASSED | PASS | 198.28 | 196.48 | 5 | -0.9% | -5.0 | OPEN |
| 2026-07-28 | TJX | PASSED | PASS | 160.8 | 157.55 | 5 | -2.0% | -6.1 | OPEN |
| 2026-07-29 | ABNB | BLOCKED | PASS | 153.01 | 149.92 | 4 | -2.0% | -7.8 | OPEN |
| 2026-07-29 | ACGL | BLOCKED | PASS | 104.55 | 99.52 | 4 | -4.8% | -10.6 | OPEN |
| 2026-07-29 | AGNC | BLOCKED | PASS | 10.9 | 10.64 | 4 | -2.4% | -8.1 | OPEN |
| 2026-07-29 | AI | BLOCKED | DEEP-FAIL | 8.85 | 10.05 | 4 | +13.6% | +7.8 | OPEN |
| 2026-07-29 | AJG | BLOCKED | REPAIR | 268.91 | 248.06 | 4 | -7.8% | -13.5 | OPEN |
| 2026-07-29 | AXON | BLOCKED | REPAIR | 531.2 | 607.2 | 4 | +14.3% | +8.6 | OPEN |
| 2026-07-29 | BFC | BLOCKED | PASS | 151.78 | 156.08 | 4 | +2.8% | -2.9 | OPEN |
| 2026-07-29 | CB | BLOCKED | PASS | 361.9 | 348.3 | 4 | -3.8% | -9.5 | OPEN |
| 2026-07-29 | CHTR | BLOCKED | DEEP-FAIL | 145.2 | 153.07 | 4 | +5.4% | -0.3 | OPEN |
| 2026-07-29 | CLX | BLOCKED | REPAIR | 99.63 | 104.67 | 4 | +5.1% | -0.7 | OPEN |
| 2026-07-29 | CMG | BLOCKED | REPAIR | 34.24 | 33.82 | 4 | -1.2% | -7.0 | OPEN |
| 2026-07-29 | CNP | BLOCKED | PASS | 42.93 | 41.58 | 4 | -3.1% | -8.9 | OPEN |
| 2026-07-29 | COKE | BLOCKED | PASS | 192.39 | 181.0 | 4 | -5.9% | -11.7 | OPEN |
| 2026-07-29 | CPRT | BLOCKED | DEEP-FAIL | 30.82 | 29.4 | 4 | -4.6% | -10.3 | OPEN |
| 2026-07-29 | CTM | BLOCKED | DEEP-FAIL | 0.66 | 0.79 | 4 | +19.1% | +13.4 | OPEN |
| 2026-07-29 | DASH | BLOCKED | REPAIR | 193.53 | 202.37 | 4 | +4.6% | -1.2 | OPEN |
| 2026-07-29 | DE | BLOCKED | PASS | 610.95 | 617.37 | 4 | +1.1% | -4.7 | OPEN |
| 2026-07-29 | DUOL | BLOCKED | REPAIR | 140.17 | 137.75 | 4 | -1.7% | -7.5 | OPEN |
| 2026-07-29 | EGBN | BLOCKED | PASS | 27.89 | 28.36 | 4 | +1.7% | -4.0 | OPEN |
| 2026-07-29 | EQIX | BLOCKED | REPAIR | 1008.02 | 1051.53 | 4 | +4.3% | -1.4 | OPEN |
| 2026-07-29 | ERIE | BLOCKED | REPAIR | 248.55 | 244.53 | 4 | -1.6% | -7.4 | OPEN |
| 2026-07-29 | ESQ | BLOCKED | PASS | 131.89 | 130.31 | 4 | -1.2% | -6.9 | OPEN |
| 2026-07-29 | FCX | BLOCKED | REPAIR | 59.99 | 67.3 | 4 | +12.2% | +6.5 | OPEN |
| 2026-07-29 | GDX | BLOCKED | DEEP-FAIL | 73.57 | 77.92 | 4 | +5.9% | +0.2 | OPEN |
| 2026-07-29 | GME | BLOCKED | REPAIR | 21.84 | 19.21 | 4 | -12.0% | -17.8 | OPEN |
| 2026-07-29 | GRND | BLOCKED | PASS | 17.21 | 17.94 | 4 | +4.2% | -1.5 | OPEN |
| 2026-07-29 | HD | BLOCKED | REPAIR | 338.27 | 348.24 | 4 | +3.0% | -2.8 | OPEN |
| 2026-07-29 | IBM | BLOCKED | DEEP-FAIL | 226.44 | 235.15 | 4 | +3.9% | -1.9 | OPEN |
| 2026-07-29 | JBLU | BLOCKED | PASS | 5.72 | 6.41 | 4 | +12.1% | +6.3 | OPEN |
| 2026-07-29 | JETS | BLOCKED | PASS | 30.97 | 33.4 | 4 | +7.8% | +2.1 | OPEN |
| 2026-07-29 | KWEB | BLOCKED | DEEP-FAIL | 27.8 | 28.89 | 4 | +3.9% | -1.8 | OPEN |
| 2026-07-29 | LDOS | BLOCKED | DEEP-FAIL | 114.37 | 130.6 | 4 | +14.2% | +8.4 | OPEN |
| 2026-07-29 | LOW | BLOCKED | REPAIR | 215.68 | 218.08 | 4 | +1.1% | -4.6 | OPEN |
| 2026-07-29 | LZB | BLOCKED | PASS | 40.93 | 41.73 | 4 | +1.9% | -3.8 | OPEN |
| 2026-07-29 | MAR | BLOCKED | PASS | 381.12 | 345.2 | 4 | -9.4% | -15.2 | OPEN |
| 2026-07-29 | MCD | BLOCKED | REPAIR | 271.52 | 268.34 | 4 | -1.2% | -6.9 | OPEN |
| 2026-07-29 | NCLH | BLOCKED | REPAIR | 20.75 | 20.07 | 4 | -3.3% | -9.0 | OPEN |
| 2026-07-29 | NEM | BLOCKED | DEEP-FAIL | 91.34 | 97.73 | 4 | +7.0% | +1.3 | OPEN |
| 2026-07-29 | NEO | BLOCKED | PASS | 15.27 | 16.29 | 4 | +6.7% | +0.9 | OPEN |
| 2026-07-29 | NFLX | BLOCKED | DEEP-FAIL | 73.63 | 73.57 | 4 | -0.1% | -5.8 | OPEN |
| 2026-07-29 | NIO | BLOCKED | DEEP-FAIL | 4.76 | 4.76 | 4 | +0.0% | -5.7 | OPEN |
| 2026-07-29 | NOW | BLOCKED | REPAIR | 115.76 | 118.14 | 4 | +2.1% | -3.7 | OPEN |
| 2026-07-29 | NVST | BLOCKED | PASS | 28.37 | 27.96 | 4 | -1.4% | -7.2 | OPEN |
| 2026-07-29 | PGR | BLOCKED | REPAIR | 219.99 | 210.75 | 4 | -4.2% | -9.9 | OPEN |
| 2026-07-29 | PH | BLOCKED | PASS | 951.07 | 992.65 | 4 | +4.4% | -1.4 | OPEN |
| 2026-07-29 | RCL | BLOCKED | REPAIR | 323.58 | 325.74 | 4 | +0.7% | -5.1 | OPEN |
| 2026-07-29 | RMD | BLOCKED | REPAIR | 214.29 | 223.14 | 4 | +4.1% | -1.6 | OPEN |
| 2026-07-29 | ROKU | BLOCKED | PASS | 145.33 | 147.33 | 4 | +1.4% | -4.4 | OPEN |
| 2026-07-29 | ROP | BLOCKED | REPAIR | 408.07 | 392.76 | 4 | -3.8% | -9.5 | OPEN |
| 2026-07-29 | RSPU | BLOCKED | PASS | 79.85 | 78.27 | 4 | -2.0% | -7.7 | OPEN |
| 2026-07-29 | SHAK | BLOCKED | DEEP-FAIL | 63.05 | 66.22 | 4 | +5.0% | -0.7 | OPEN |
| 2026-07-29 | SHW | BLOCKED | REPAIR | 343.88 | 361.57 | 4 | +5.1% | -0.6 | OPEN |
| 2026-07-29 | SKYY | BLOCKED | PASS | 138.56 | 153.43 | 4 | +10.7% | +5.0 | OPEN |
| 2026-07-29 | SMCI | BLOCKED | DEEP-FAIL | 25.7 | 31.69 | 4 | +23.3% | +17.6 | OPEN |
| 2026-07-29 | STGW | BLOCKED | PASS | 8.08 | 9.01 | 4 | +11.5% | +5.8 | OPEN |
| 2026-07-29 | TDY | BLOCKED | PASS | 631.35 | 684.76 | 4 | +8.5% | +2.7 | OPEN |
| 2026-07-29 | TOST | BLOCKED | REPAIR | 32.6 | 33.81 | 4 | +3.7% | -2.0 | OPEN |
| 2026-07-29 | TPR | BLOCKED | PASS | 150.11 | 155.97 | 4 | +3.9% | -1.8 | OPEN |
| 2026-07-29 | TYL | BLOCKED | DEEP-FAIL | 333.5 | 313.33 | 4 | -6.0% | -11.8 | OPEN |
| 2026-07-29 | URI | BLOCKED | PASS | 1055.11 | 1150.13 | 4 | +9.0% | +3.3 | OPEN |
| 2026-07-29 | VRSN | BLOCKED | REPAIR | 290.92 | 299.2 | 4 | +2.9% | -2.9 | OPEN |
| 2026-07-29 | WWD | BLOCKED | PASS | 385.42 | 373.67 | 4 | -3.0% | -8.8 | OPEN |
| 2026-07-29 | ZTS | BLOCKED | DEEP-FAIL | 77.93 | 76.04 | 4 | -2.4% | -8.2 | OPEN |
| 2026-07-29 | CCL | PASSED | REPAIR | 27.81 | 29.59 | 4 | +6.4% | +0.7 | OPEN |
| 2026-07-29 | CPT | PASSED | PASS | 116.37 | 111.03 | 4 | -4.6% | -10.3 | OPEN |
| 2026-07-29 | CTS | PASSED | PASS | 61.53 | 67.26 | 4 | +9.3% | +3.6 | OPEN |
| 2026-07-29 | DAL | PASSED | PASS | 86.25 | 92.77 | 4 | +7.6% | +1.8 | OPEN |
| 2026-07-29 | DGX | PASSED | PASS | 235.22 | 233.72 | 4 | -0.6% | -6.4 | OPEN |
| 2026-07-29 | DLR | PASSED | PASS | 188.18 | 193.89 | 4 | +3.0% | -2.7 | OPEN |
| 2026-07-29 | GE | PASSED | PASS | 350.63 | 377.28 | 4 | +7.6% | +1.9 | OPEN |
| 2026-07-29 | HON | PASSED | PASS | 241.12 | 248.79 | 4 | +3.2% | -2.6 | OPEN |
| 2026-07-29 | JNJ | PASSED | PASS | 265.53 | 254.93 | 4 | -4.0% | -9.7 | OPEN |
| 2026-07-29 | KDP | PASSED | PASS | 31.45 | 31.1 | 4 | -1.1% | -6.8 | OPEN |
| 2026-07-29 | LHX | PASSED | REPAIR | 297.53 | 285.3 | 4 | -4.1% | -9.8 | OPEN |
| 2026-07-29 | LLY | PASSED | PASS | 1210.02 | 1115.68 | 4 | -7.8% | -13.5 | OPEN |
| 2026-07-29 | MDT | PASSED | REPAIR | 87.54 | 86.2 | 4 | -1.5% | -7.3 | OPEN |
| 2026-07-29 | MNST | PASSED | PASS | 97.23 | 94.18 | 4 | -3.1% | -8.9 | OPEN |
| 2026-07-29 | MRK | PASSED | PASS | 130.36 | 128.0 | 4 | -1.8% | -7.5 | OPEN |
| 2026-07-29 | PEP | PASSED | REPAIR | 143.5 | 139.1 | 4 | -3.1% | -8.8 | OPEN |
| 2026-07-29 | RACE | PASSED | REPAIR | 385.69 | 402.79 | 4 | +4.4% | -1.3 | OPEN |
| 2026-07-29 | SLB | PASSED | REPAIR | 48.96 | 50.81 | 4 | +3.8% | -2.0 | OPEN |
| 2026-07-29 | SSD | PASSED | REPAIR | 189.48 | 196.48 | 4 | +3.7% | -2.0 | OPEN |
| 2026-07-29 | TJX | PASSED | PASS | 161.63 | 157.55 | 4 | -2.5% | -8.3 | OPEN |
| 2026-07-30 | ABNB | BLOCKED | PASS | 152.08 | 149.92 | 3 | -1.4% | -5.4 | OPEN |
| 2026-07-30 | ACGL | BLOCKED | PASS | 101.14 | 99.52 | 3 | -1.6% | -5.6 | OPEN |
| 2026-07-30 | AGNC | BLOCKED | PASS | 10.92 | 10.64 | 3 | -2.6% | -6.6 | OPEN |
| 2026-07-30 | AI | BLOCKED | DEEP-FAIL | 9.07 | 10.05 | 3 | +10.8% | +6.8 | OPEN |
| 2026-07-30 | AJG | BLOCKED | REPAIR | 256.46 | 248.06 | 3 | -3.3% | -7.3 | OPEN |
| 2026-07-30 | APD | BLOCKED | PASS | 300.2 | 294.71 | 3 | -1.8% | -5.8 | OPEN |
| 2026-07-30 | AXON | BLOCKED | REPAIR | 525.3 | 607.2 | 3 | +15.6% | +11.6 | OPEN |
| 2026-07-30 | CB | BLOCKED | PASS | 350.15 | 348.3 | 3 | -0.5% | -4.5 | OPEN |
| 2026-07-30 | CHTR | BLOCKED | DEEP-FAIL | 142.0 | 153.07 | 3 | +7.8% | +3.8 | OPEN |
| 2026-07-30 | CLX | BLOCKED | REPAIR | 96.73 | 104.67 | 3 | +8.2% | +4.2 | OPEN |
| 2026-07-30 | CMG | BLOCKED | REPAIR | 38.52 | 33.82 | 3 | -12.2% | -16.2 | OPEN |
| 2026-07-30 | CNP | BLOCKED | REPAIR | 42.15 | 41.58 | 3 | -1.4% | -5.3 | OPEN |
| 2026-07-30 | COKE | BLOCKED | PASS | 189.83 | 181.0 | 3 | -4.7% | -8.7 | OPEN |
| 2026-07-30 | CPRT | BLOCKED | DEEP-FAIL | 29.57 | 29.4 | 3 | -0.6% | -4.6 | OPEN |
| 2026-07-30 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.79 | 3 | +11.1% | +7.1 | OPEN |
| 2026-07-30 | DASH | BLOCKED | REPAIR | 197.53 | 202.37 | 3 | +2.5% | -1.6 | OPEN |
| 2026-07-30 | DE | BLOCKED | PASS | 599.47 | 617.37 | 3 | +3.0% | -1.0 | OPEN |
| 2026-07-30 | DUOL | BLOCKED | REPAIR | 133.6 | 137.75 | 3 | +3.1% | -0.9 | OPEN |
| 2026-07-30 | EGBN | BLOCKED | PASS | 27.49 | 28.36 | 3 | +3.2% | -0.8 | OPEN |
| 2026-07-30 | GME | BLOCKED | REPAIR | 21.88 | 19.21 | 3 | -12.2% | -16.2 | OPEN |
| 2026-07-30 | HD | BLOCKED | REPAIR | 333.35 | 348.24 | 3 | +4.5% | +0.5 | OPEN |
| 2026-07-30 | IBM | BLOCKED | DEEP-FAIL | 221.74 | 235.15 | 3 | +6.0% | +2.0 | OPEN |
| 2026-07-30 | JBLU | BLOCKED | PASS | 6.07 | 6.41 | 3 | +5.6% | +1.6 | OPEN |
| 2026-07-30 | KWEB | BLOCKED | DEEP-FAIL | 28.06 | 28.89 | 3 | +3.0% | -1.0 | OPEN |
| 2026-07-30 | LDOS | BLOCKED | DEEP-FAIL | 112.41 | 130.6 | 3 | +16.2% | +12.2 | OPEN |
| 2026-07-30 | LLY | BLOCKED | PASS | 1154.97 | 1115.68 | 3 | -3.4% | -7.4 | OPEN |
| 2026-07-30 | LOW | BLOCKED | DEEP-FAIL | 210.08 | 218.08 | 3 | +3.8% | -0.2 | OPEN |
| 2026-07-30 | LYV | BLOCKED | PASS | 183.56 | 183.7 | 3 | +0.1% | -3.9 | OPEN |
| 2026-07-30 | LZB | BLOCKED | PASS | 40.13 | 41.73 | 3 | +4.0% | -0.0 | OPEN |
| 2026-07-30 | MAR | BLOCKED | REPAIR | 375.48 | 345.2 | 3 | -8.1% | -12.1 | OPEN |
| 2026-07-30 | MCD | BLOCKED | DEEP-FAIL | 268.44 | 268.34 | 3 | -0.0% | -4.0 | OPEN |
| 2026-07-30 | MIDD | BLOCKED | PASS | 133.32 | 138.78 | 3 | +4.1% | +0.1 | OPEN |
| 2026-07-30 | MRK | BLOCKED | PASS | 129.79 | 128.0 | 3 | -1.4% | -5.4 | OPEN |
| 2026-07-30 | MSFT | BLOCKED | REPAIR | 451.1 | 492.81 | 3 | +9.2% | +5.2 | OPEN |
| 2026-07-30 | NCLH | BLOCKED | REPAIR | 18.72 | 20.07 | 3 | +7.2% | +3.2 | OPEN |
| 2026-07-30 | NFLX | BLOCKED | DEEP-FAIL | 73.17 | 73.57 | 3 | +0.6% | -3.5 | OPEN |
| 2026-07-30 | NIO | BLOCKED | DEEP-FAIL | 4.84 | 4.76 | 3 | -1.6% | -5.7 | OPEN |
| 2026-07-30 | NOW | BLOCKED | DEEP-FAIL | 110.07 | 118.14 | 3 | +7.3% | +3.3 | OPEN |
| 2026-07-30 | NVST | BLOCKED | PASS | 27.78 | 27.96 | 3 | +0.7% | -3.4 | OPEN |
| 2026-07-30 | PB | BLOCKED | PASS | 74.82 | 74.89 | 3 | +0.1% | -3.9 | OPEN |
| 2026-07-30 | PGR | BLOCKED | REPAIR | 213.28 | 210.75 | 3 | -1.2% | -5.2 | OPEN |
| 2026-07-30 | PH | BLOCKED | PASS | 962.79 | 992.65 | 3 | +3.1% | -0.9 | OPEN |
| 2026-07-30 | RCL | BLOCKED | REPAIR | 321.94 | 325.74 | 3 | +1.2% | -2.8 | OPEN |
| 2026-07-30 | RMD | BLOCKED | REPAIR | 208.56 | 223.14 | 3 | +7.0% | +3.0 | OPEN |
| 2026-07-30 | ROKU | BLOCKED | PASS | 145.09 | 147.33 | 3 | +1.5% | -2.5 | OPEN |
| 2026-07-30 | RSPU | BLOCKED | REPAIR | 79.51 | 78.27 | 3 | -1.6% | -5.6 | OPEN |
| 2026-07-30 | SFM | BLOCKED | REPAIR | 86.85 | 86.07 | 3 | -0.9% | -4.9 | OPEN |
| 2026-07-30 | SHAK | BLOCKED | DEEP-FAIL | 63.07 | 66.22 | 3 | +5.0% | +1.0 | OPEN |
| 2026-07-30 | SHW | BLOCKED | REPAIR | 344.84 | 361.57 | 3 | +4.8% | +0.9 | OPEN |
| 2026-07-30 | SKYY | BLOCKED | PASS | 140.03 | 153.43 | 3 | +9.6% | +5.6 | OPEN |
| 2026-07-30 | SSD | BLOCKED | REPAIR | 186.67 | 196.48 | 3 | +5.3% | +1.3 | OPEN |
| 2026-07-30 | STGW | BLOCKED | PASS | 8.49 | 9.01 | 3 | +6.1% | +2.1 | OPEN |
| 2026-07-30 | TDY | BLOCKED | PASS | 649.18 | 684.76 | 3 | +5.5% | +1.5 | OPEN |
| 2026-07-30 | TOST | BLOCKED | REPAIR | 32.85 | 33.81 | 3 | +2.9% | -1.1 | OPEN |
| 2026-07-30 | TPR | BLOCKED | PASS | 152.58 | 155.97 | 3 | +2.2% | -1.8 | OPEN |
| 2026-07-30 | TYL | BLOCKED | DEEP-FAIL | 323.31 | 313.33 | 3 | -3.1% | -7.1 | OPEN |
| 2026-07-30 | URI | BLOCKED | PASS | 1068.63 | 1150.13 | 3 | +7.6% | +3.6 | OPEN |
| 2026-07-30 | ZTS | BLOCKED | DEEP-FAIL | 76.03 | 76.04 | 3 | +0.0% | -4.0 | OPEN |
| 2026-07-30 | CCL | PASSED | REPAIR | 27.77 | 29.59 | 3 | +6.5% | +2.6 | OPEN |
| 2026-07-30 | CPT | PASSED | PASS | 113.29 | 111.03 | 3 | -2.0% | -6.0 | OPEN |
| 2026-07-30 | CTS | PASSED | REPAIR | 62.7 | 67.26 | 3 | +7.3% | +3.3 | OPEN |
| 2026-07-30 | DAL | PASSED | PASS | 88.59 | 92.77 | 3 | +4.7% | +0.7 | OPEN |
| 2026-07-30 | DGX | PASSED | PASS | 234.3 | 233.72 | 3 | -0.2% | -4.2 | OPEN |
| 2026-07-30 | EQIX | PASSED | PASS | 1047.53 | 1051.53 | 3 | +0.4% | -3.6 | OPEN |
| 2026-07-30 | ERIE | PASSED | REPAIR | 233.67 | 244.53 | 3 | +4.7% | +0.7 | OPEN |
| 2026-07-30 | GE | PASSED | PASS | 355.04 | 377.28 | 3 | +6.3% | +2.3 | OPEN |
| 2026-07-30 | JETS | PASSED | PASS | 31.68 | 33.4 | 3 | +5.4% | +1.4 | OPEN |
| 2026-07-30 | KDP | PASSED | PASS | 31.57 | 31.1 | 3 | -1.5% | -5.5 | OPEN |
| 2026-07-30 | MDT | PASSED | REPAIR | 85.71 | 86.2 | 3 | +0.6% | -3.4 | OPEN |
| 2026-07-30 | MNST | PASSED | PASS | 97.65 | 94.18 | 3 | -3.5% | -7.5 | OPEN |
| 2026-07-30 | PEP | PASSED | REPAIR | 140.2 | 139.1 | 3 | -0.8% | -4.8 | OPEN |
| 2026-07-30 | RACE | PASSED | REPAIR | 397.73 | 402.79 | 3 | +1.3% | -2.7 | OPEN |
| 2026-07-30 | ROP | PASSED | REPAIR | 389.25 | 392.76 | 3 | +0.9% | -3.1 | OPEN |
| 2026-07-30 | ST | PASSED | PASS | 47.99 | 48.66 | 3 | +1.4% | -2.6 | OPEN |
| 2026-07-30 | TJX | PASSED | PASS | 159.26 | 157.55 | 3 | -1.1% | -5.1 | OPEN |
| 2026-07-30 | VRSN | PASSED | REPAIR | 286.58 | 299.2 | 3 | +4.4% | +0.4 | OPEN |
| 2026-07-31 | ABNB | BLOCKED | PASS | 151.52 | 149.92 | 2 | -1.1% | -4.3 | OPEN |
| 2026-07-31 | ACGL | BLOCKED | PASS | 100.53 | 99.52 | 2 | -1.0% | -4.3 | OPEN |
| 2026-07-31 | AGNC | BLOCKED | PASS | 10.66 | 10.64 | 2 | -0.2% | -3.4 | OPEN |
| 2026-07-31 | AI | BLOCKED | DEEP-FAIL | 9.18 | 10.05 | 2 | +9.5% | +6.2 | OPEN |
| 2026-07-31 | AJG | BLOCKED | REPAIR | 249.42 | 248.06 | 2 | -0.6% | -3.8 | OPEN |
| 2026-07-31 | AMZN | BLOCKED | PASS | 271.58 | 277.42 | 2 | +2.1% | -1.1 | OPEN |
| 2026-07-31 | APD | BLOCKED | PASS | 294.89 | 294.71 | 2 | -0.1% | -3.3 | OPEN |
| 2026-07-31 | APH | BLOCKED | PASS | 160.7 | 171.33 | 2 | +6.6% | +3.4 | OPEN |
| 2026-07-31 | AXON | BLOCKED | REPAIR | 527.76 | 607.2 | 2 | +15.1% | +11.8 | OPEN |
| 2026-07-31 | BABA | BLOCKED | DEEP-FAIL | 122.25 | 128.99 | 2 | +5.5% | +2.3 | OPEN |
| 2026-07-31 | CB | BLOCKED | PASS | 350.68 | 348.3 | 2 | -0.7% | -3.9 | OPEN |
| 2026-07-31 | CCL | BLOCKED | REPAIR | 27.81 | 29.59 | 2 | +6.4% | +3.1 | OPEN |
| 2026-07-31 | CHTR | BLOCKED | DEEP-FAIL | 144.98 | 153.07 | 2 | +5.6% | +2.3 | OPEN |
| 2026-07-31 | CLX | BLOCKED | REPAIR | 95.53 | 104.67 | 2 | +9.6% | +6.3 | OPEN |
| 2026-07-31 | CMG | BLOCKED | REPAIR | 37.22 | 33.82 | 2 | -9.1% | -12.4 | OPEN |
| 2026-07-31 | COKE | BLOCKED | PASS | 187.9 | 181.0 | 2 | -3.7% | -6.9 | OPEN |
| 2026-07-31 | CPRT | BLOCKED | DEEP-FAIL | 29.12 | 29.4 | 2 | +1.0% | -2.3 | OPEN |
| 2026-07-31 | CPT | BLOCKED | REPAIR | 110.81 | 111.03 | 2 | +0.2% | -3.0 | OPEN |
| 2026-07-31 | CTM | BLOCKED | DEEP-FAIL | 0.72 | 0.79 | 2 | +10.2% | +6.9 | OPEN |
| 2026-07-31 | DAL | BLOCKED | PASS | 87.44 | 92.77 | 2 | +6.1% | +2.8 | OPEN |
| 2026-07-31 | DASH | BLOCKED | REPAIR | 196.16 | 202.37 | 2 | +3.2% | -0.1 | OPEN |
| 2026-07-31 | DE | BLOCKED | PASS | 592.67 | 617.37 | 2 | +4.2% | +0.9 | OPEN |
| 2026-07-31 | DUOL | BLOCKED | REPAIR | 134.81 | 137.75 | 2 | +2.2% | -1.1 | OPEN |
| 2026-07-31 | EGBN | BLOCKED | PASS | 27.75 | 28.36 | 2 | +2.2% | -1.1 | OPEN |
| 2026-07-31 | EME | BLOCKED | PASS | 797.43 | 819.88 | 2 | +2.8% | -0.4 | OPEN |
| 2026-07-31 | EQIX | BLOCKED | REPAIR | 1019.28 | 1051.53 | 2 | +3.2% | -0.1 | OPEN |
| 2026-07-31 | ERIE | BLOCKED | REPAIR | 242.04 | 244.53 | 2 | +1.0% | -2.2 | OPEN |
| 2026-07-31 | GH | BLOCKED | PASS | 161.99 | 159.79 | 2 | -1.4% | -4.6 | OPEN |
| 2026-07-31 | GME | BLOCKED | REPAIR | 21.72 | 19.21 | 2 | -11.6% | -14.8 | OPEN |
| 2026-07-31 | GOOG | BLOCKED | REPAIR | 356.65 | 375.35 | 2 | +5.2% | +2.0 | OPEN |
| 2026-07-31 | GRND | BLOCKED | PASS | 17.34 | 17.94 | 2 | +3.5% | +0.2 | OPEN |
| 2026-07-31 | HD | BLOCKED | REPAIR | 331.96 | 348.24 | 2 | +4.9% | +1.6 | OPEN |
| 2026-07-31 | IBM | BLOCKED | DEEP-FAIL | 223.65 | 235.15 | 2 | +5.1% | +1.9 | OPEN |
| 2026-07-31 | IGV | BLOCKED | REPAIR | 94.58 | 102.0 | 2 | +7.8% | +4.6 | OPEN |
| 2026-07-31 | JBLU | BLOCKED | PASS | 6.03 | 6.41 | 2 | +6.3% | +3.0 | OPEN |
| 2026-07-31 | JETS | BLOCKED | PASS | 31.28 | 33.4 | 2 | +6.8% | +3.5 | OPEN |
| 2026-07-31 | KWEB | BLOCKED | DEEP-FAIL | 28.49 | 28.89 | 2 | +1.4% | -1.9 | OPEN |
| 2026-07-31 | LDOS | BLOCKED | DEEP-FAIL | 115.6 | 130.6 | 2 | +13.0% | +9.7 | OPEN |
| 2026-07-31 | LOW | BLOCKED | DEEP-FAIL | 207.81 | 218.08 | 2 | +4.9% | +1.7 | OPEN |
| 2026-07-31 | LYV | BLOCKED | PASS | 174.13 | 183.7 | 2 | +5.5% | +2.2 | OPEN |
| 2026-07-31 | LZB | BLOCKED | PASS | 39.38 | 41.73 | 2 | +6.0% | +2.7 | OPEN |
| 2026-07-31 | MAR | BLOCKED | REPAIR | 372.83 | 345.2 | 2 | -7.4% | -10.7 | OPEN |
| 2026-07-31 | MCD | BLOCKED | DEEP-FAIL | 270.64 | 268.34 | 2 | -0.8% | -4.1 | OPEN |
| 2026-07-31 | MDT | BLOCKED | REPAIR | 85.39 | 86.2 | 2 | +0.9% | -2.3 | OPEN |
| 2026-07-31 | MIDD | BLOCKED | PASS | 133.58 | 138.78 | 2 | +3.9% | +0.6 | OPEN |
| 2026-07-31 | MRK | BLOCKED | PASS | 130.2 | 128.0 | 2 | -1.7% | -4.9 | OPEN |
| 2026-07-31 | MSFT | BLOCKED | REPAIR | 464.72 | 492.81 | 2 | +6.0% | +2.8 | OPEN |
| 2026-07-31 | NCLH | BLOCKED | REPAIR | 18.53 | 20.07 | 2 | +8.3% | +5.1 | OPEN |
| 2026-07-31 | NFLX | BLOCKED | DEEP-FAIL | 71.71 | 73.57 | 2 | +2.6% | -0.7 | OPEN |
| 2026-07-31 | NIO | BLOCKED | DEEP-FAIL | 4.88 | 4.76 | 2 | -2.5% | -5.7 | OPEN |
| 2026-07-31 | NOW | BLOCKED | DEEP-FAIL | 111.23 | 118.14 | 2 | +6.2% | +3.0 | OPEN |
| 2026-07-31 | PEP | BLOCKED | REPAIR | 139.56 | 139.1 | 2 | -0.3% | -3.6 | OPEN |
| 2026-07-31 | PGR | BLOCKED | REPAIR | 211.42 | 210.75 | 2 | -0.3% | -3.6 | OPEN |
| 2026-07-31 | PH | BLOCKED | PASS | 976.53 | 992.65 | 2 | +1.6% | -1.6 | OPEN |
| 2026-07-31 | PLPC | BLOCKED | PASS | 356.98 | 423.6 | 2 | +18.7% | +15.4 | OPEN |
| 2026-07-31 | PWR | BLOCKED | REPAIR | 667.36 | 693.0 | 2 | +3.8% | +0.6 | OPEN |
| 2026-07-31 | RCL | BLOCKED | REPAIR | 318.3 | 325.74 | 2 | +2.3% | -0.9 | OPEN |
| 2026-07-31 | RMD | BLOCKED | DEEP-FAIL | 210.98 | 223.14 | 2 | +5.8% | +2.5 | OPEN |
| 2026-07-31 | ROKU | BLOCKED | PASS | 145.01 | 147.33 | 2 | +1.6% | -1.6 | OPEN |
| 2026-07-31 | ROP | BLOCKED | REPAIR | 391.97 | 392.76 | 2 | +0.2% | -3.0 | OPEN |
| 2026-07-31 | SFM | BLOCKED | REPAIR | 87.16 | 86.07 | 2 | -1.2% | -4.5 | OPEN |
| 2026-07-31 | SHAK | BLOCKED | DEEP-FAIL | 62.75 | 66.22 | 2 | +5.5% | +2.3 | OPEN |
| 2026-07-31 | SHW | BLOCKED | REPAIR | 340.85 | 361.57 | 2 | +6.1% | +2.8 | OPEN |
| 2026-07-31 | SKYY | BLOCKED | PASS | 143.0 | 153.43 | 2 | +7.3% | +4.0 | OPEN |
| 2026-07-31 | SSD | BLOCKED | REPAIR | 187.74 | 196.48 | 2 | +4.7% | +1.4 | OPEN |
| 2026-07-31 | TOST | BLOCKED | REPAIR | 32.27 | 33.81 | 2 | +4.8% | +1.5 | OPEN |
| 2026-07-31 | TPR | BLOCKED | PASS | 152.37 | 155.97 | 2 | +2.4% | -0.9 | OPEN |
| 2026-07-31 | TYL | BLOCKED | DEEP-FAIL | 309.6 | 313.33 | 2 | +1.2% | -2.0 | OPEN |
| 2026-07-31 | XLY | BLOCKED | REPAIR | 116.09 | 118.29 | 2 | +1.9% | -1.4 | OPEN |
| 2026-07-31 | ZTS | BLOCKED | DEEP-FAIL | 77.29 | 76.04 | 2 | -1.6% | -4.9 | OPEN |
| 2026-07-31 | CTS | PASSED | PASS | 64.12 | 67.26 | 2 | +4.9% | +1.6 | OPEN |
| 2026-07-31 | FIVN | PASSED | PASS | 27.51 | 29.79 | 2 | +8.3% | +5.0 | OPEN |
| 2026-07-31 | GE | PASSED | PASS | 360.07 | 377.28 | 2 | +4.8% | +1.5 | OPEN |
| 2026-07-31 | KDP | PASSED | PASS | 31.12 | 31.1 | 2 | -0.1% | -3.3 | OPEN |
| 2026-07-31 | RACE | PASSED | REPAIR | 393.87 | 402.79 | 2 | +2.3% | -1.0 | OPEN |
| 2026-07-31 | ST | PASSED | REPAIR | 46.29 | 48.66 | 2 | +5.1% | +1.9 | OPEN |
| 2026-07-31 | TJX | PASSED | PASS | 157.34 | 157.55 | 2 | +0.1% | -3.1 | OPEN |
| 2026-07-31 | VRSN | PASSED | REPAIR | 290.02 | 299.2 | 2 | +3.2% | -0.1 | OPEN |
| 2026-08-03 | ABNB | BLOCKED | PASS | 150.64 | 149.92 | 1 | -0.5% | -2.3 | OPEN |
| 2026-08-03 | ACGL | BLOCKED | PASS | 101.12 | 99.52 | 1 | -1.6% | -3.4 | OPEN |
| 2026-08-03 | AGNC | BLOCKED | REPAIR | 10.64 | 10.64 | 1 | +0.0% | -1.8 | OPEN |
| 2026-08-03 | AI | BLOCKED | DEEP-FAIL | 9.73 | 10.05 | 1 | +3.3% | +1.5 | OPEN |
| 2026-08-03 | AJG | BLOCKED | REPAIR | 247.79 | 248.06 | 1 | +0.1% | -1.7 | OPEN |
| 2026-08-03 | AMZN | BLOCKED | PASS | 284.02 | 277.42 | 1 | -2.3% | -4.1 | OPEN |
| 2026-08-03 | APD | BLOCKED | PASS | 292.94 | 294.71 | 1 | +0.6% | -1.2 | OPEN |
| 2026-08-03 | APH | BLOCKED | PASS | 163.34 | 171.33 | 1 | +4.9% | +3.1 | OPEN |
| 2026-08-03 | AXON | BLOCKED | REPAIR | 575.88 | 607.2 | 1 | +5.4% | +3.6 | OPEN |
| 2026-08-03 | BABA | BLOCKED | REPAIR | 127.3 | 128.99 | 1 | +1.3% | -0.5 | OPEN |
| 2026-08-03 | CHTR | BLOCKED | DEEP-FAIL | 144.1 | 153.07 | 1 | +6.2% | +4.4 | OPEN |
| 2026-08-03 | CLX | BLOCKED | REPAIR | 98.26 | 104.67 | 1 | +6.5% | +4.7 | OPEN |
| 2026-08-03 | COKE | BLOCKED | PASS | 180.76 | 181.0 | 1 | +0.1% | -1.7 | OPEN |
| 2026-08-03 | CPRT | BLOCKED | DEEP-FAIL | 29.35 | 29.4 | 1 | +0.2% | -1.6 | OPEN |
| 2026-08-03 | CRWD | BLOCKED | PASS | 202.54 | 211.22 | 1 | +4.3% | +2.5 | OPEN |
| 2026-08-03 | CTM | BLOCKED | DEEP-FAIL | 0.74 | 0.79 | 1 | +7.6% | +5.8 | OPEN |
| 2026-08-03 | DASH | BLOCKED | REPAIR | 200.5 | 202.37 | 1 | +0.9% | -0.9 | OPEN |
| 2026-08-03 | DGII | BLOCKED | PASS | 70.4 | 72.14 | 1 | +2.5% | +0.7 | OPEN |
| 2026-08-03 | DOW | BLOCKED | PASS | 29.89 | 30.33 | 1 | +1.5% | -0.3 | OPEN |
| 2026-08-03 | EME | BLOCKED | REPAIR | 817.42 | 819.88 | 1 | +0.3% | -1.5 | OPEN |
| 2026-08-03 | EMN | BLOCKED | PASS | 71.98 | 73.9 | 1 | +2.7% | +0.9 | OPEN |
| 2026-08-03 | ERIE | BLOCKED | REPAIR | 236.86 | 244.53 | 1 | +3.2% | +1.4 | OPEN |
| 2026-08-03 | ETN | BLOCKED | PASS | 438.23 | 444.77 | 1 | +1.5% | -0.3 | OPEN |
| 2026-08-03 | FIVN | BLOCKED | PASS | 28.95 | 29.79 | 1 | +2.9% | +1.1 | OPEN |
| 2026-08-03 | FSLR | BLOCKED | REPAIR | 232.73 | 243.63 | 1 | +4.7% | +2.9 | OPEN |
| 2026-08-03 | GOOG | BLOCKED | PASS | 372.47 | 375.35 | 1 | +0.8% | -1.0 | OPEN |
| 2026-08-03 | GRND | BLOCKED | PASS | 17.9 | 17.94 | 1 | +0.2% | -1.6 | OPEN |
| 2026-08-03 | HD | BLOCKED | REPAIR | 340.02 | 348.24 | 1 | +2.4% | +0.6 | OPEN |
| 2026-08-03 | IBM | BLOCKED | DEEP-FAIL | 226.31 | 235.15 | 1 | +3.9% | +2.1 | OPEN |
| 2026-08-03 | IGV | BLOCKED | REPAIR | 97.42 | 102.0 | 1 | +4.7% | +2.9 | OPEN |
| 2026-08-03 | JBLU | BLOCKED | PASS | 6.23 | 6.41 | 1 | +2.9% | +1.1 | OPEN |
| 2026-08-03 | KWEB | BLOCKED | REPAIR | 28.74 | 28.89 | 1 | +0.5% | -1.3 | OPEN |
| 2026-08-03 | LOW | BLOCKED | DEEP-FAIL | 212.06 | 218.08 | 1 | +2.8% | +1.0 | OPEN |
| 2026-08-03 | LYV | BLOCKED | PASS | 181.69 | 183.7 | 1 | +1.1% | -0.7 | OPEN |
| 2026-08-03 | LZB | BLOCKED | PASS | 41.0 | 41.73 | 1 | +1.8% | -0.0 | OPEN |
| 2026-08-03 | MAMA | BLOCKED | PASS | 18.89 | 18.86 | 1 | -0.2% | -2.0 | OPEN |
| 2026-08-03 | MCD | BLOCKED | REPAIR | 265.23 | 268.34 | 1 | +1.2% | -0.6 | OPEN |
| 2026-08-03 | MLAB | BLOCKED | PASS | 104.43 | 101.14 | 1 | -3.1% | -5.0 | OPEN |
| 2026-08-03 | MSFT | BLOCKED | REPAIR | 487.65 | 492.81 | 1 | +1.1% | -0.7 | OPEN |
| 2026-08-03 | NCLH | BLOCKED | REPAIR | 19.76 | 20.07 | 1 | +1.6% | -0.2 | OPEN |
| 2026-08-03 | NFLX | BLOCKED | DEEP-FAIL | 73.33 | 73.57 | 1 | +0.3% | -1.5 | OPEN |
| 2026-08-03 | NIO | BLOCKED | DEEP-FAIL | 4.81 | 4.76 | 1 | -1.0% | -2.8 | OPEN |
| 2026-08-03 | NOW | BLOCKED | REPAIR | 114.19 | 118.14 | 1 | +3.5% | +1.7 | OPEN |
| 2026-08-03 | ORCL | BLOCKED | DEEP-FAIL | 141.85 | 145.74 | 1 | +2.7% | +0.9 | OPEN |
| 2026-08-03 | PEP | BLOCKED | REPAIR | 139.63 | 139.1 | 1 | -0.4% | -2.2 | OPEN |
| 2026-08-03 | PGR | BLOCKED | REPAIR | 210.46 | 210.75 | 1 | +0.1% | -1.7 | OPEN |
| 2026-08-03 | PWR | BLOCKED | REPAIR | 680.2 | 693.0 | 1 | +1.9% | +0.1 | OPEN |
| 2026-08-03 | RMD | BLOCKED | REPAIR | 215.19 | 223.14 | 1 | +3.7% | +1.9 | OPEN |
| 2026-08-03 | ROKU | BLOCKED | PASS | 145.84 | 147.33 | 1 | +1.0% | -0.8 | OPEN |
| 2026-08-03 | S | BLOCKED | PASS | 20.05 | 20.98 | 1 | +4.6% | +2.8 | OPEN |
| 2026-08-03 | SFM | BLOCKED | REPAIR | 88.81 | 86.07 | 1 | -3.1% | -4.9 | OPEN |
| 2026-08-03 | SHAK | BLOCKED | DEEP-FAIL | 64.78 | 66.22 | 1 | +2.2% | +0.4 | OPEN |
| 2026-08-03 | SKYY | BLOCKED | PASS | 147.98 | 153.43 | 1 | +3.7% | +1.9 | OPEN |
| 2026-08-03 | SPXL | BLOCKED | PASS | 279.68 | 294.56 | 1 | +5.3% | +3.5 | OPEN |
| 2026-08-03 | SYM | BLOCKED | DEEP-FAIL | 45.85 | 47.46 | 1 | +3.5% | +1.7 | OPEN |
| 2026-08-03 | TOST | BLOCKED | REPAIR | 32.79 | 33.81 | 1 | +3.1% | +1.3 | OPEN |
| 2026-08-03 | TPR | BLOCKED | PASS | 155.63 | 155.97 | 1 | +0.2% | -1.6 | OPEN |
| 2026-08-03 | TYL | BLOCKED | DEEP-FAIL | 305.54 | 313.33 | 1 | +2.5% | +0.8 | OPEN |
| 2026-08-03 | WRBY | BLOCKED | PASS | 28.28 | 29.92 | 1 | +5.8% | +4.0 | OPEN |
| 2026-08-03 | XLY | BLOCKED | REPAIR | 118.21 | 118.29 | 1 | +0.1% | -1.7 | OPEN |
| 2026-08-03 | ZTS | BLOCKED | DEEP-FAIL | 77.1 | 76.04 | 1 | -1.4% | -3.2 | OPEN |
| 2026-08-03 | AMG | PASSED | PASS | 380.89 | 383.42 | 1 | +0.7% | -1.1 | OPEN |
| 2026-08-03 | CCL | PASSED | REPAIR | 28.74 | 29.59 | 1 | +3.0% | +1.1 | OPEN |
| 2026-08-03 | CMG | PASSED | REPAIR | 37.46 | 33.82 | 1 | -9.7% | -11.5 | OPEN |
| 2026-08-03 | CTS | PASSED | PASS | 65.23 | 67.26 | 1 | +3.1% | +1.3 | OPEN |
| 2026-08-03 | DAL | PASSED | PASS | 91.59 | 92.77 | 1 | +1.3% | -0.5 | OPEN |
| 2026-08-03 | DUOL | PASSED | REPAIR | 135.8 | 137.75 | 1 | +1.4% | -0.4 | OPEN |
| 2026-08-03 | JETS | PASSED | PASS | 32.67 | 33.4 | 1 | +2.2% | +0.4 | OPEN |
| 2026-08-03 | KDP | PASSED | PASS | 30.91 | 31.1 | 1 | +0.6% | -1.2 | OPEN |
| 2026-08-03 | MDT | PASSED | REPAIR | 86.68 | 86.2 | 1 | -0.6% | -2.4 | OPEN |
| 2026-08-03 | MIDD | PASSED | PASS | 135.81 | 138.78 | 1 | +2.2% | +0.4 | OPEN |
| 2026-08-03 | PLPC | PASSED | REPAIR | 358.15 | 423.6 | 1 | +18.3% | +16.5 | OPEN |
| 2026-08-03 | RACE | PASSED | REPAIR | 401.28 | 402.79 | 1 | +0.4% | -1.4 | OPEN |
| 2026-08-03 | RCL | PASSED | REPAIR | 324.0 | 325.74 | 1 | +0.5% | -1.3 | OPEN |
| 2026-08-03 | SHW | PASSED | REPAIR | 354.22 | 361.57 | 1 | +2.1% | +0.3 | OPEN |
| 2026-08-03 | SSD | PASSED | REPAIR | 192.17 | 196.48 | 1 | +2.2% | +0.4 | OPEN |
| 2026-08-03 | ST | PASSED | REPAIR | 46.82 | 48.66 | 1 | +3.9% | +2.1 | OPEN |
| 2026-08-03 | TJX | PASSED | PASS | 157.5 | 157.55 | 1 | +0.0% | -1.8 | OPEN |
| 2026-08-03 | UAL | PASSED | PASS | 128.39 | 132.62 | 1 | +3.3% | +1.5 | OPEN |
| 2026-08-03 | VRSN | PASSED | REPAIR | 298.89 | 299.2 | 1 | +0.1% | -1.7 | OPEN |

Open marks are not results. This file exists so that the cull the scan performs every night is measured instead of assumed.
