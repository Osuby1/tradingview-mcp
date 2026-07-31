# Gate stack forward grade

Does THE GATE STACK earn its keep? Every fresh Chandelier signal is graded forward from the CLOSE of its signal date over 21 trading sessions, bucketed by what the stack decided. The number that matters is the SPREAD.

- Signal events found: 592  |  priced: 514  |  unique symbol-cohort pairs (headline sample): 235
- Skipped (pre-2026-07-22 hand-written verdicts, not machine-comparable): 20

## Headline - all signals, deduped to first appearance

| Cohort | n | Win% | Mean | Median | Mean vs SPY | Mean worst drawdown |
|---|---|---|---|---|---|---|
| PASSED | 50 | 36% | -0.94% | -0.91% | -1.70% | -4.95% |
| BLOCKED | 185 | 43% | -1.04% | -0.94% | -1.58% | -5.70% |

**Spread (PASSED minus BLOCKED): +0.10 percentage points.**

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
| ADX FLOOR | 57 | 46% | -0.45% | -0.87% | -1.01% |
| ATR GEOMETRY | 9 | 33% | -2.56% | -3.76% | -3.58% |
| DIRECTION | 11 | 9% | -5.58% | -3.54% | -5.83% |
| LIQUIDITY | 1 | 0% | -11.30% | -11.30% | -11.25% |
| OTHER | 30 | 40% | -0.85% | -0.92% | -1.04% |
| REGIME | 21 | 48% | -0.77% | -0.28% | -1.64% |
| VOLATILITY CAP (ex 2:1) | 5 | 20% | -1.62% | -1.49% | -2.27% |
| ZLSMA | 51 | 51% | -0.40% | +0.20% | -0.98% |

## Shadow cohorts - the forbidden retro-tune, run forward instead

Would lowering the ADX floor to 18, or softening DEEP-FAIL, have helped? The replay's missed monsters make that tempting; answering it by re-running history is curve-fitting. These cohorts answer it FORWARD: sole-failure near-misses graded nightly against the PASSED cohort. Promotion bar (pre-registered): >=30 MATURED signals AND mean above PASSED's - then it goes to a Friday review, not before.

| Shadow cohort | n | Win% | Mean | Median | Mean vs SPY | PASSED mean (ref) |
|---|---|---|---|---|---|---|
| ADX 18-20, all else passed | 5 | 20% | -1.89% | -1.72% | -2.81% | -0.94% |
| DEEP-FAIL, all else passed | 2 | 50% | +0.42% | +0.42% | -0.66% | -0.94% |

## Every graded signal

| Date | Sym | Cohort | Regime | Entry | Mark | Days | Return | vs SPY | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | BG | BLOCKED | n/a | 120.49 | 106.23 | 9 | -11.8% | -12.5 | OPEN |
| 2026-07-20 | CHRD | BLOCKED | n/a | 128.8 | 140.38 | 9 | +9.0% | +8.3 | OPEN |
| 2026-07-20 | CNOB | BLOCKED | n/a | 33.46 | 32.94 | 9 | -1.6% | -2.2 | OPEN |
| 2026-07-20 | COCO | BLOCKED | PASS | 73.87 | 65.94 | 9 | -10.7% | -11.4 | OPEN |
| 2026-07-20 | CVNA | BLOCKED | DEEP-FAIL | 64.14 | 62.36 | 9 | -2.8% | -3.4 | OPEN |
| 2026-07-20 | FLG | BLOCKED | n/a | 14.84 | 14.22 | 9 | -4.2% | -4.8 | OPEN |
| 2026-07-20 | FNB | BLOCKED | n/a | 18.75 | 18.9 | 9 | +0.8% | +0.1 | OPEN |
| 2026-07-20 | HAS | BLOCKED | REPAIR | 81.59 | 93.94 | 9 | +15.1% | +14.5 | OPEN |
| 2026-07-20 | HLX | BLOCKED | n/a | 9.43 | 9.51 | 9 | +0.8% | +0.2 | OPEN |
| 2026-07-20 | LCID | BLOCKED | n/a | 7.11 | 7.38 | 9 | +3.8% | +3.1 | OPEN |
| 2026-07-20 | M | BLOCKED | REPAIR | 23.31 | 24.82 | 9 | +6.5% | +5.8 | OPEN |
| 2026-07-20 | NOV | BLOCKED | REPAIR | 19.55 | 19.43 | 9 | -0.6% | -1.3 | OPEN |
| 2026-07-20 | ODFL | BLOCKED | PASS | 231.76 | 212.14 | 9 | -8.5% | -9.1 | OPEN |
| 2026-07-20 | RYZ | BLOCKED | n/a | 29.07 | 27.79 | 9 | -4.4% | -5.1 | OPEN |
| 2026-07-20 | SHAK | BLOCKED | DEEP-FAIL | 56.97 | 62.75 | 9 | +10.2% | +9.5 | OPEN |
| 2026-07-20 | SPG | BLOCKED | PASS | 228.19 | 229.37 | 9 | +0.5% | -0.1 | OPEN |
| 2026-07-20 | TRNS | BLOCKED | n/a | 86.09 | 85.37 | 9 | -0.8% | -1.5 | OPEN |
| 2026-07-20 | VVV | BLOCKED | PASS | 39.54 | 38.41 | 9 | -2.9% | -3.5 | OPEN |
| 2026-07-20 | VZ | BLOCKED | REPAIR | 43.5 | 46.81 | 9 | +7.6% | +6.9 | OPEN |
| 2026-07-20 | WPC | BLOCKED | REPAIR | 75.17 | 73.6 | 9 | -2.1% | -2.8 | OPEN |
| 2026-07-21 | ALKS | BLOCKED | TAPE OK | 52.85 | 48.99 | 8 | -7.3% | -7.1 | OPEN |
| 2026-07-21 | ATLC | BLOCKED | TAPE OK | 96.37 | 105.49 | 8 | +9.5% | +9.6 | OPEN |
| 2026-07-21 | BRKR | BLOCKED | TAPE OK | 60.43 | 62.84 | 8 | +4.0% | +4.2 | OPEN |
| 2026-07-21 | CB | BLOCKED | TAPE OK | 354.8 | 350.68 | 8 | -1.2% | -1.0 | OPEN |
| 2026-07-21 | CBL | BLOCKED | TAPE OK | 55.53 | 58.71 | 8 | +5.7% | +5.9 | OPEN |
| 2026-07-21 | CNOB | BLOCKED | TAPE OK | 33.41 | 32.94 | 8 | -1.4% | -1.2 | OPEN |
| 2026-07-21 | COCO | BLOCKED | TAPE OK | 75.89 | 65.94 | 8 | -13.1% | -12.9 | OPEN |
| 2026-07-21 | CTRE | BLOCKED | TAPE OK | 43.4 | 41.94 | 8 | -3.4% | -3.2 | OPEN |
| 2026-07-21 | ESQ | BLOCKED | TAPE OK | 122.83 | 129.22 | 8 | +5.2% | +5.4 | OPEN |
| 2026-07-21 | EXTR | BLOCKED | TAPE OK | 30.44 | 30.14 | 8 | -1.0% | -0.8 | OPEN |
| 2026-07-21 | FFIV | BLOCKED | TAPE OK | 408.74 | 402.57 | 8 | -1.5% | -1.3 | OPEN |
| 2026-07-21 | FRT | BLOCKED | TAPE OK | 125.59 | 124.09 | 8 | -1.2% | -1.0 | OPEN |
| 2026-07-21 | HCSG | BLOCKED | TAPE OK | 24.8 | 23.3 | 8 | -6.0% | -5.9 | OPEN |
| 2026-07-21 | HELE | BLOCKED | TAPE OK | 27.28 | 27.63 | 8 | +1.3% | +1.4 | OPEN |
| 2026-07-21 | HOMB | BLOCKED | TAPE OK | 30.42 | 31.07 | 8 | +2.1% | +2.3 | OPEN |
| 2026-07-21 | LQDA | BLOCKED | TAPE OK | 80.89 | 84.11 | 8 | +4.0% | +4.2 | OPEN |
| 2026-07-21 | NVRI | BLOCKED | TAPE OK | 21.87 | 22.18 | 8 | +1.4% | +1.6 | OPEN |
| 2026-07-21 | NWPX | BLOCKED | TAPE OK | 135.41 | 123.08 | 8 | -9.1% | -8.9 | OPEN |
| 2026-07-21 | OSCR | BLOCKED | TAPE OK | 30.77 | 31.22 | 8 | +1.5% | +1.6 | OPEN |
| 2026-07-21 | PNC | BLOCKED | TAPE OK | 250.38 | 249.87 | 8 | -0.2% | -0.0 | OPEN |
| 2026-07-21 | SION | BLOCKED | TAPE OK | 47.21 | 47.13 | 8 | -0.2% | -0.0 | OPEN |
| 2026-07-21 | TBLA | BLOCKED | TAPE OK | 5.11 | 5.01 | 8 | -2.0% | -1.8 | OPEN |
| 2026-07-21 | TFIN | BLOCKED | TAPE OK | 79.19 | 75.93 | 8 | -4.1% | -4.0 | OPEN |
| 2026-07-21 | TGTX | BLOCKED | TAPE OK | 53.95 | 52.03 | 8 | -3.6% | -3.4 | OPEN |
| 2026-07-21 | TVTX | BLOCKED | TAPE OK | 56.58 | 55.89 | 8 | -1.2% | -1.1 | OPEN |
| 2026-07-21 | VCYT | BLOCKED | TAPE OK | 59.53 | 46.32 | 8 | -22.2% | -22.0 | OPEN |
| 2026-07-21 | ZD | BLOCKED | TAPE OK | 52.39 | 53.08 | 8 | +1.3% | +1.5 | OPEN |
| 2026-07-21 | CYRX | PASSED | TAPE OK | 16.24 | 15.09 | 8 | -7.1% | -6.9 | OPEN |
| 2026-07-21 | FLEX | PASSED | TAPE OK | 127.39 | 113.75 | 8 | -10.7% | -10.5 | OPEN |
| 2026-07-21 | GDX | PASSED | TAPE OK | 74.19 | 74.1 | 8 | -0.1% | +0.1 | OPEN |
| 2026-07-21 | HON | PASSED | TAPE OK | 229.86 | 243.05 | 8 | +5.7% | +5.9 | OPEN |
| 2026-07-21 | KWEB | PASSED | TAPE OK | 27.02 | 28.49 | 8 | +5.4% | +5.6 | OPEN |
| 2026-07-21 | MSFT | PASSED | TAPE OK | 397.75 | 464.72 | 8 | +16.8% | +17.0 | OPEN |
| 2026-07-21 | MU | PASSED | TAPE OK | 970.82 | 823.03 | 8 | -15.2% | -15.1 | OPEN |
| 2026-07-21 | NKE | PASSED | TAPE OK | 42.96 | 41.71 | 8 | -2.9% | -2.7 | OPEN |
| 2026-07-21 | PM | PASSED | TAPE OK | 188.04 | 190.82 | 8 | +1.5% | +1.6 | OPEN |
| 2026-07-21 | SKYY | PASSED | TAPE OK | 136.02 | 143.0 | 8 | +5.1% | +5.3 | OPEN |
| 2026-07-21 | SNOW | PASSED | TAPE OK | 271.73 | 293.28 | 8 | +7.9% | +8.1 | OPEN |
| 2026-07-22 | ACTG | BLOCKED | REPAIR | 4.57 | 4.43 | 7 | -3.1% | -3.0 | OPEN |
| 2026-07-22 | AMCR | BLOCKED | PASS | 43.21 | 44.88 | 7 | +3.9% | +3.9 | OPEN |
| 2026-07-22 | AMGN | BLOCKED | PASS | 366.05 | 385.16 | 7 | +5.2% | +5.3 | OPEN |
| 2026-07-22 | ASB | BLOCKED | PASS | 30.7 | 30.88 | 7 | +0.6% | +0.6 | OPEN |
| 2026-07-22 | BCBP | BLOCKED | REPAIR | 10.29 | 9.99 | 7 | -2.9% | -2.9 | OPEN |
| 2026-07-22 | BHP | BLOCKED | REPAIR | 84.54 | 84.49 | 7 | -0.1% | -0.0 | OPEN |
| 2026-07-22 | BHRB | BLOCKED | PASS | 71.01 | 73.25 | 7 | +3.1% | +3.2 | OPEN |
| 2026-07-22 | BX | BLOCKED | REPAIR | 122.82 | 127.75 | 7 | +4.0% | +4.1 | OPEN |
| 2026-07-22 | BY | BLOCKED | PASS | 37.75 | 39.27 | 7 | +4.0% | +4.1 | OPEN |
| 2026-07-22 | CBSH | BLOCKED | PASS | 58.7 | 59.27 | 7 | +1.0% | +1.0 | OPEN |
| 2026-07-22 | CCJ | BLOCKED | DEEP-FAIL | 90.37 | 86.38 | 7 | -4.4% | -4.4 | OPEN |
| 2026-07-22 | CMP | BLOCKED | REPAIR | 30.14 | 29.34 | 7 | -2.6% | -2.6 | OPEN |
| 2026-07-22 | CNOB | BLOCKED | PASS | 33.0 | 32.94 | 7 | -0.2% | -0.1 | OPEN |
| 2026-07-22 | COKE | BLOCKED | PASS | 184.36 | 187.9 | 7 | +1.9% | +2.0 | OPEN |
| 2026-07-22 | COLB | BLOCKED | PASS | 32.63 | 31.27 | 7 | -4.2% | -4.1 | OPEN |
| 2026-07-22 | COST | BLOCKED | REPAIR | 927.31 | 951.89 | 7 | +2.6% | +2.7 | OPEN |
| 2026-07-22 | CRCL | BLOCKED | DEEP-FAIL | 66.16 | 62.61 | 7 | -5.4% | -5.3 | OPEN |
| 2026-07-22 | DE | BLOCKED | PASS | 607.33 | 592.67 | 7 | -2.4% | -2.4 | OPEN |
| 2026-07-22 | DELL | BLOCKED | PASS | 441.8 | 405.37 | 7 | -8.2% | -8.2 | OPEN |
| 2026-07-22 | DIS | BLOCKED | REPAIR | 95.87 | 96.19 | 7 | +0.3% | +0.4 | OPEN |
| 2026-07-22 | EQR | BLOCKED | PASS | 68.29 | 66.45 | 7 | -2.7% | -2.6 | OPEN |
| 2026-07-22 | F | BLOCKED | PASS | 14.42 | 14.68 | 7 | +1.8% | +1.9 | OPEN |
| 2026-07-22 | FCX | BLOCKED | PASS | 65.0 | 62.63 | 7 | -3.6% | -3.6 | OPEN |
| 2026-07-22 | FHB | BLOCKED | PASS | 28.81 | 27.79 | 7 | -3.5% | -3.5 | OPEN |
| 2026-07-22 | FITB | BLOCKED | PASS | 57.67 | 56.5 | 7 | -2.0% | -2.0 | OPEN |
| 2026-07-22 | FLEX | BLOCKED | REPAIR | 127.0 | 113.75 | 7 | -10.4% | -10.4 | OPEN |
| 2026-07-22 | FLG | BLOCKED | PASS | 14.88 | 14.22 | 7 | -4.4% | -4.4 | OPEN |
| 2026-07-22 | FNB | BLOCKED | PASS | 18.86 | 18.9 | 7 | +0.2% | +0.3 | OPEN |
| 2026-07-22 | FRT | BLOCKED | PASS | 125.05 | 124.09 | 7 | -0.8% | -0.7 | OPEN |
| 2026-07-22 | GBCI | BLOCKED | PASS | 51.17 | 49.29 | 7 | -3.7% | -3.6 | OPEN |
| 2026-07-22 | GDX | BLOCKED | DEEP-FAIL | 76.68 | 74.1 | 7 | -3.4% | -3.3 | OPEN |
| 2026-07-22 | GLD | BLOCKED | REPAIR | 379.12 | 371.54 | 7 | -2.0% | -1.9 | OPEN |
| 2026-07-22 | GM | BLOCKED | PASS | 82.13 | 88.86 | 7 | +8.2% | +8.2 | OPEN |
| 2026-07-22 | HBNC | BLOCKED | PASS | 20.21 | 20.45 | 7 | +1.2% | +1.2 | OPEN |
| 2026-07-22 | HON | BLOCKED | PASS | 232.99 | 243.05 | 7 | +4.3% | +4.4 | OPEN |
| 2026-07-22 | HOPE | BLOCKED | PASS | 13.54 | 14.01 | 7 | +3.5% | +3.5 | OPEN |
| 2026-07-22 | HSIC | BLOCKED | PASS | 84.81 | 85.75 | 7 | +1.1% | +1.2 | OPEN |
| 2026-07-22 | HTZ | BLOCKED | DEEP-FAIL | 1.93 | 1.59 | 7 | -17.9% | -17.8 | OPEN |
| 2026-07-22 | KRE | BLOCKED | PASS | 75.6 | 76.06 | 7 | +0.6% | +0.7 | OPEN |
| 2026-07-22 | LCID | BLOCKED | DEEP-FAIL | 6.78 | 7.38 | 7 | +8.8% | +8.9 | OPEN |
| 2026-07-22 | LZB | BLOCKED | PASS | 39.3 | 39.38 | 7 | +0.2% | +0.2 | OPEN |
| 2026-07-22 | M | BLOCKED | PASS | 24.33 | 24.82 | 7 | +2.0% | +2.1 | OPEN |
| 2026-07-22 | MFA | BLOCKED | REPAIR | 9.29 | 9.11 | 7 | -1.9% | -1.9 | OPEN |
| 2026-07-22 | MU | BLOCKED | PASS | 959.48 | 823.03 | 7 | -14.2% | -14.2 | OPEN |
| 2026-07-22 | NEE | BLOCKED | PASS | 89.41 | 86.92 | 7 | -2.8% | -2.7 | OPEN |
| 2026-07-22 | NEM | BLOCKED | REPAIR | 95.75 | 93.71 | 7 | -2.1% | -2.1 | OPEN |
| 2026-07-22 | OCFC | BLOCKED | PASS | 19.67 | 19.31 | 7 | -1.8% | -1.8 | OPEN |
| 2026-07-22 | PANW | BLOCKED | PASS | 335.28 | 331.83 | 7 | -1.0% | -1.0 | OPEN |
| 2026-07-22 | PB | BLOCKED | PASS | 73.06 | 74.87 | 7 | +2.5% | +2.5 | OPEN |
| 2026-07-22 | PM | BLOCKED | PASS | 194.3 | 190.82 | 7 | -1.8% | -1.7 | OPEN |
| 2026-07-22 | POWL | BLOCKED | REPAIR | 240.68 | 208.68 | 7 | -13.3% | -13.2 | OPEN |
| 2026-07-22 | PRLB | BLOCKED | PASS | 79.73 | 75.05 | 7 | -5.9% | -5.8 | OPEN |
| 2026-07-22 | RACE | BLOCKED | REPAIR | 371.61 | 393.87 | 7 | +6.0% | +6.0 | OPEN |
| 2026-07-22 | RCL | BLOCKED | REPAIR | 285.85 | 318.3 | 7 | +11.3% | +11.4 | OPEN |
| 2026-07-22 | RSPU | BLOCKED | PASS | 81.85 | 78.89 | 7 | -3.6% | -3.6 | OPEN |
| 2026-07-22 | SAIC | BLOCKED | PASS | 115.95 | 117.13 | 7 | +1.0% | +1.1 | OPEN |
| 2026-07-22 | SJM | BLOCKED | PASS | 118.05 | 119.26 | 7 | +1.0% | +1.1 | OPEN |
| 2026-07-22 | SKK | BLOCKED | PASS | 5.22 | 4.63 | 7 | -11.3% | -11.2 | OPEN |
| 2026-07-22 | SMCI | BLOCKED | REPAIR | 30.56 | 28.4 | 7 | -7.1% | -7.0 | OPEN |
| 2026-07-22 | SON | BLOCKED | PASS | 55.15 | 56.36 | 7 | +2.2% | +2.2 | OPEN |
| 2026-07-22 | SPG | BLOCKED | PASS | 226.22 | 229.37 | 7 | +1.4% | +1.4 | OPEN |
| 2026-07-22 | SSB | BLOCKED | PASS | 102.19 | 105.09 | 7 | +2.8% | +2.9 | OPEN |
| 2026-07-22 | STRL | BLOCKED | REPAIR | 719.34 | 596.77 | 7 | -17.0% | -17.0 | OPEN |
| 2026-07-22 | STX | BLOCKED | PASS | 908.1 | 856.13 | 7 | -5.7% | -5.7 | OPEN |
| 2026-07-22 | TDY | BLOCKED | PASS | 650.5 | 655.57 | 7 | +0.8% | +0.8 | OPEN |
| 2026-07-22 | TPL | BLOCKED | PASS | 433.1 | 402.58 | 7 | -7.0% | -7.0 | OPEN |
| 2026-07-22 | TPR | BLOCKED | PASS | 143.73 | 152.37 | 7 | +6.0% | +6.1 | OPEN |
| 2026-07-22 | URA | BLOCKED | DEEP-FAIL | 40.97 | 39.07 | 7 | -4.6% | -4.6 | OPEN |
| 2026-07-22 | USB | BLOCKED | PASS | 64.47 | 63.01 | 7 | -2.3% | -2.2 | OPEN |
| 2026-07-22 | VST | BLOCKED | REPAIR | 166.74 | 148.19 | 7 | -11.1% | -11.1 | OPEN |
| 2026-07-22 | VVV | BLOCKED | PASS | 39.03 | 38.41 | 7 | -1.6% | -1.5 | OPEN |
| 2026-07-22 | CTRE | PASSED | PASS | 42.38 | 41.94 | 7 | -1.0% | -1.0 | OPEN |
| 2026-07-22 | PFE | PASSED | REPAIR | 24.82 | 25.01 | 7 | +0.8% | +0.8 | OPEN |
| 2026-07-22 | TJX | PASSED | REPAIR | 155.41 | 157.34 | 7 | +1.2% | +1.3 | OPEN |
| 2026-07-22 | TXNM | PASSED | REPAIR | 58.3 | 57.92 | 7 | -0.7% | -0.6 | OPEN |
| 2026-07-22 | VZ | PASSED | REPAIR | 44.29 | 46.81 | 7 | +5.7% | +5.7 | OPEN |
| 2026-07-23 | ACTG | BLOCKED | REPAIR | 4.62 | 4.43 | 6 | -4.1% | -5.3 | OPEN |
| 2026-07-23 | ALSN | BLOCKED | PASS | 119.64 | 114.54 | 6 | -4.3% | -5.5 | OPEN |
| 2026-07-23 | AVT | BLOCKED | PASS | 89.92 | 88.84 | 6 | -1.2% | -2.4 | OPEN |
| 2026-07-23 | BUD | BLOCKED | REPAIR | 80.48 | 86.48 | 6 | +7.5% | +6.3 | OPEN |
| 2026-07-23 | COST | BLOCKED | REPAIR | 926.06 | 951.89 | 6 | +2.8% | +1.6 | OPEN |
| 2026-07-23 | CRCL | BLOCKED | DEEP-FAIL | 62.18 | 62.61 | 6 | +0.7% | -0.5 | OPEN |
| 2026-07-23 | DELL | BLOCKED | PASS | 439.34 | 405.37 | 6 | -7.7% | -8.9 | OPEN |
| 2026-07-23 | DGX | BLOCKED | PASS | 227.9 | 233.01 | 6 | +2.2% | +1.0 | OPEN |
| 2026-07-23 | F | BLOCKED | REPAIR | 14.15 | 14.68 | 6 | +3.8% | +2.5 | OPEN |
| 2026-07-23 | FCX | BLOCKED | REPAIR | 63.5 | 62.63 | 6 | -1.4% | -2.6 | OPEN |
| 2026-07-23 | FLG | BLOCKED | PASS | 14.71 | 14.22 | 6 | -3.3% | -4.5 | OPEN |
| 2026-07-23 | FNB | BLOCKED | PASS | 18.87 | 18.9 | 6 | +0.2% | -1.0 | OPEN |
| 2026-07-23 | FUTU | BLOCKED | DEEP-FAIL | 98.96 | 105.12 | 6 | +6.2% | +5.0 | OPEN |
| 2026-07-23 | GDX | BLOCKED | DEEP-FAIL | 75.02 | 74.1 | 6 | -1.2% | -2.4 | OPEN |
| 2026-07-23 | GLD | BLOCKED | REPAIR | 371.52 | 371.54 | 6 | +0.0% | -1.2 | OPEN |
| 2026-07-23 | GM | BLOCKED | PASS | 80.67 | 88.86 | 6 | +10.2% | +8.9 | OPEN |
| 2026-07-23 | HON | BLOCKED | PASS | 246.27 | 243.05 | 6 | -1.3% | -2.5 | OPEN |
| 2026-07-23 | IRM | BLOCKED | REPAIR | 124.55 | 122.32 | 6 | -1.8% | -3.0 | OPEN |
| 2026-07-23 | LCID | BLOCKED | DEEP-FAIL | 6.45 | 7.38 | 6 | +14.4% | +13.2 | OPEN |
| 2026-07-23 | LSTR | BLOCKED | PASS | 207.97 | 174.77 | 6 | -16.0% | -17.2 | OPEN |
| 2026-07-23 | M | BLOCKED | PASS | 23.33 | 24.82 | 6 | +6.4% | +5.2 | OPEN |
| 2026-07-23 | MAC | BLOCKED | PASS | 25.3 | 25.84 | 6 | +2.1% | +0.9 | OPEN |
| 2026-07-23 | NEM | BLOCKED | REPAIR | 94.72 | 93.71 | 6 | -1.1% | -2.3 | OPEN |
| 2026-07-23 | PLD | BLOCKED | PASS | 145.12 | 144.61 | 6 | -0.3% | -1.6 | OPEN |
| 2026-07-23 | PRLB | BLOCKED | PASS | 78.62 | 75.05 | 6 | -4.5% | -5.7 | OPEN |
| 2026-07-23 | RHP | BLOCKED | PASS | 128.89 | 133.65 | 6 | +3.7% | +2.5 | OPEN |
| 2026-07-23 | SMCI | BLOCKED | REPAIR | 31.2 | 28.4 | 6 | -9.0% | -10.2 | OPEN |
| 2026-07-23 | SON | BLOCKED | PASS | 56.32 | 56.36 | 6 | +0.1% | -1.1 | OPEN |
| 2026-07-23 | SPG | BLOCKED | PASS | 225.2 | 229.37 | 6 | +1.9% | +0.7 | OPEN |
| 2026-07-23 | TDY | BLOCKED | PASS | 651.22 | 655.57 | 6 | +0.7% | -0.5 | OPEN |
| 2026-07-23 | URA | BLOCKED | DEEP-FAIL | 41.13 | 39.07 | 6 | -5.0% | -6.2 | OPEN |
| 2026-07-23 | URI | BLOCKED | PASS | 1139.71 | 1079.26 | 6 | -5.3% | -6.5 | OPEN |
| 2026-07-23 | VST | BLOCKED | REPAIR | 168.98 | 148.19 | 6 | -12.3% | -13.5 | OPEN |
| 2026-07-23 | VVV | BLOCKED | PASS | 38.31 | 38.41 | 6 | +0.3% | -0.9 | OPEN |
| 2026-07-23 | ECVT | PASSED | PASS | 12.89 | 12.06 | 6 | -6.4% | -7.6 | OPEN |
| 2026-07-23 | FRT | PASSED | PASS | 124.83 | 124.09 | 6 | -0.6% | -1.8 | OPEN |
| 2026-07-23 | HAS | PASSED | PASS | 87.35 | 93.94 | 6 | +7.5% | +6.3 | OPEN |
| 2026-07-23 | LHX | PASSED | REPAIR | 299.67 | 277.06 | 6 | -7.5% | -8.7 | OPEN |
| 2026-07-23 | MLI | PASSED | REPAIR | 63.13 | 66.41 | 6 | +5.2% | +4.0 | OPEN |
| 2026-07-23 | PFE | PASSED | REPAIR | 25.01 | 25.01 | 6 | +0.0% | -1.2 | OPEN |
| 2026-07-23 | SJM | PASSED | PASS | 115.71 | 119.26 | 6 | +3.1% | +1.9 | OPEN |
| 2026-07-23 | VZ | PASSED | REPAIR | 43.82 | 46.81 | 6 | +6.8% | +5.6 | OPEN |
| 2026-07-24 | ALSN | BLOCKED | PASS | 122.34 | 114.54 | 5 | -6.4% | -7.5 | OPEN |
| 2026-07-24 | AVT | BLOCKED | PASS | 89.42 | 88.84 | 5 | -0.7% | -1.7 | OPEN |
| 2026-07-24 | BUD | BLOCKED | REPAIR | 81.66 | 86.48 | 5 | +5.9% | +4.8 | OPEN |
| 2026-07-24 | CB | BLOCKED | PASS | 359.75 | 350.68 | 5 | -2.5% | -3.6 | OPEN |
| 2026-07-24 | CNP | BLOCKED | PASS | 44.56 | 42.04 | 5 | -5.7% | -6.8 | OPEN |
| 2026-07-24 | COST | BLOCKED | REPAIR | 935.03 | 951.89 | 5 | +1.8% | +0.7 | OPEN |
| 2026-07-24 | CRCL | BLOCKED | DEEP-FAIL | 62.36 | 62.61 | 5 | +0.4% | -0.7 | OPEN |
| 2026-07-24 | DE | BLOCKED | PASS | 628.16 | 592.67 | 5 | -5.7% | -6.8 | OPEN |
| 2026-07-24 | DGX | BLOCKED | PASS | 227.86 | 233.01 | 5 | +2.3% | +1.2 | OPEN |
| 2026-07-24 | DLR | BLOCKED | PASS | 199.08 | 188.52 | 5 | -5.3% | -6.4 | OPEN |
| 2026-07-24 | EGBN | BLOCKED | PASS | 28.44 | 27.75 | 5 | -2.4% | -3.5 | OPEN |
| 2026-07-24 | F | BLOCKED | REPAIR | 14.37 | 14.68 | 5 | +2.2% | +1.1 | OPEN |
| 2026-07-24 | FCX | BLOCKED | REPAIR | 62.6 | 62.63 | 5 | +0.1% | -1.1 | OPEN |
| 2026-07-24 | FUTU | BLOCKED | DEEP-FAIL | 99.36 | 105.12 | 5 | +5.8% | +4.7 | OPEN |
| 2026-07-24 | GDX | BLOCKED | DEEP-FAIL | 75.23 | 74.1 | 5 | -1.5% | -2.6 | OPEN |
| 2026-07-24 | GE | BLOCKED | PASS | 353.73 | 360.07 | 5 | +1.8% | +0.7 | OPEN |
| 2026-07-24 | GLD | BLOCKED | REPAIR | 371.9 | 371.54 | 5 | -0.1% | -1.2 | OPEN |
| 2026-07-24 | GM | BLOCKED | PASS | 82.64 | 88.86 | 5 | +7.5% | +6.4 | OPEN |
| 2026-07-24 | HON | BLOCKED | PASS | 243.15 | 243.05 | 5 | -0.0% | -1.1 | OPEN |
| 2026-07-24 | IRM | BLOCKED | PASS | 128.31 | 122.32 | 5 | -4.7% | -5.8 | OPEN |
| 2026-07-24 | JNJ | BLOCKED | PASS | 263.4 | 256.35 | 5 | -2.7% | -3.8 | OPEN |
| 2026-07-24 | LCID | BLOCKED | DEEP-FAIL | 6.3 | 7.38 | 5 | +17.1% | +16.1 | OPEN |
| 2026-07-24 | LDOS | BLOCKED | DEEP-FAIL | 112.14 | 115.6 | 5 | +3.1% | +2.0 | OPEN |
| 2026-07-24 | LIND | BLOCKED | PASS | 26.85 | 29.58 | 5 | +10.2% | +9.1 | OPEN |
| 2026-07-24 | M | BLOCKED | PASS | 23.38 | 24.82 | 5 | +6.2% | +5.1 | OPEN |
| 2026-07-24 | NEM | BLOCKED | REPAIR | 93.19 | 93.71 | 5 | +0.6% | -0.5 | OPEN |
| 2026-07-24 | ORKA | BLOCKED | PASS | 92.16 | 96.51 | 5 | +4.7% | +3.6 | OPEN |
| 2026-07-24 | PH | BLOCKED | PASS | 987.54 | 976.53 | 5 | -1.1% | -2.2 | OPEN |
| 2026-07-24 | PRLB | BLOCKED | PASS | 78.24 | 75.05 | 5 | -4.1% | -5.2 | OPEN |
| 2026-07-24 | ROP | BLOCKED | REPAIR | 367.34 | 391.97 | 5 | +6.7% | +5.6 | OPEN |
| 2026-07-24 | RSPU | BLOCKED | PASS | 82.33 | 78.89 | 5 | -4.2% | -5.3 | OPEN |
| 2026-07-24 | SMCI | BLOCKED | REPAIR | 30.1 | 28.4 | 5 | -5.7% | -6.7 | OPEN |
| 2026-07-24 | SON | BLOCKED | PASS | 58.23 | 56.36 | 5 | -3.2% | -4.3 | OPEN |
| 2026-07-24 | SPG | BLOCKED | PASS | 229.78 | 229.37 | 5 | -0.2% | -1.3 | OPEN |
| 2026-07-24 | TDY | BLOCKED | PASS | 655.35 | 655.57 | 5 | +0.0% | -1.1 | OPEN |
| 2026-07-24 | URA | BLOCKED | DEEP-FAIL | 39.89 | 39.07 | 5 | -2.1% | -3.1 | OPEN |
| 2026-07-24 | URI | BLOCKED | PASS | 1141.59 | 1079.26 | 5 | -5.5% | -6.6 | OPEN |
| 2026-07-24 | VST | BLOCKED | REPAIR | 163.38 | 148.19 | 5 | -9.3% | -10.4 | OPEN |
| 2026-07-24 | XLI | BLOCKED | PASS | 182.66 | 179.84 | 5 | -1.5% | -2.6 | OPEN |
| 2026-07-24 | ACTG | PASSED | PASS | 4.66 | 4.43 | 5 | -4.9% | -6.0 | OPEN |
| 2026-07-24 | DELL | PASSED | PASS | 437.5 | 405.37 | 5 | -7.3% | -8.4 | OPEN |
| 2026-07-24 | EQIX | PASSED | PASS | 1084.24 | 1019.28 | 5 | -6.0% | -7.1 | OPEN |
| 2026-07-24 | LHX | PASSED | REPAIR | 300.21 | 277.06 | 5 | -7.7% | -8.8 | OPEN |
| 2026-07-24 | MLI | PASSED | REPAIR | 63.91 | 66.41 | 5 | +3.9% | +2.8 | OPEN |
| 2026-07-24 | MRK | PASSED | PASS | 131.07 | 130.2 | 5 | -0.7% | -1.8 | OPEN |
| 2026-07-24 | RHP | PASSED | PASS | 133.09 | 133.65 | 5 | +0.4% | -0.7 | OPEN |
| 2026-07-24 | SJM | PASSED | PASS | 118.32 | 119.26 | 5 | +0.8% | -0.3 | OPEN |
| 2026-07-24 | VZ | PASSED | REPAIR | 46.38 | 46.81 | 5 | +0.9% | -0.2 | OPEN |
| 2026-07-27 | ACGL | BLOCKED | PASS | 103.88 | 100.53 | 4 | -3.2% | -4.3 | OPEN |
| 2026-07-27 | ALSN | BLOCKED | PASS | 121.91 | 114.54 | 4 | -6.0% | -7.1 | OPEN |
| 2026-07-27 | AVT | BLOCKED | PASS | 88.38 | 88.84 | 4 | +0.5% | -0.6 | OPEN |
| 2026-07-27 | BUD | BLOCKED | REPAIR | 80.87 | 86.48 | 4 | +6.9% | +5.9 | OPEN |
| 2026-07-27 | CB | BLOCKED | PASS | 358.91 | 350.68 | 4 | -2.3% | -3.4 | OPEN |
| 2026-07-27 | CPRT | BLOCKED | DEEP-FAIL | 29.79 | 29.12 | 4 | -2.2% | -3.3 | OPEN |
| 2026-07-27 | CRCL | BLOCKED | DEEP-FAIL | 65.67 | 62.61 | 4 | -4.7% | -5.7 | OPEN |
| 2026-07-27 | DE | BLOCKED | PASS | 625.02 | 592.67 | 4 | -5.2% | -6.2 | OPEN |
| 2026-07-27 | DLR | BLOCKED | PASS | 195.76 | 188.52 | 4 | -3.7% | -4.8 | OPEN |
| 2026-07-27 | EGBN | BLOCKED | PASS | 28.15 | 27.75 | 4 | -1.4% | -2.5 | OPEN |
| 2026-07-27 | F | BLOCKED | PASS | 14.68 | 14.68 | 4 | +0.0% | -1.1 | OPEN |
| 2026-07-27 | FCX | BLOCKED | REPAIR | 62.72 | 62.63 | 4 | -0.1% | -1.2 | OPEN |
| 2026-07-27 | FUTU | BLOCKED | DEEP-FAIL | 104.27 | 105.12 | 4 | +0.8% | -0.3 | OPEN |
| 2026-07-27 | GDX | BLOCKED | DEEP-FAIL | 75.73 | 74.1 | 4 | -2.1% | -3.2 | OPEN |
| 2026-07-27 | GLD | BLOCKED | REPAIR | 374.63 | 371.54 | 4 | -0.8% | -1.9 | OPEN |
| 2026-07-27 | GM | BLOCKED | PASS | 87.04 | 88.86 | 4 | +2.1% | +1.0 | OPEN |
| 2026-07-27 | HON | BLOCKED | PASS | 245.75 | 243.05 | 4 | -1.1% | -2.2 | OPEN |
| 2026-07-27 | IRM | BLOCKED | PASS | 126.99 | 122.32 | 4 | -3.7% | -4.8 | OPEN |
| 2026-07-27 | LDOS | BLOCKED | DEEP-FAIL | 114.95 | 115.6 | 4 | +0.6% | -0.5 | OPEN |
| 2026-07-27 | LIND | BLOCKED | PASS | 28.09 | 29.58 | 4 | +5.3% | +4.2 | OPEN |
| 2026-07-27 | MAR | BLOCKED | PASS | 383.06 | 372.83 | 4 | -2.7% | -3.7 | OPEN |
| 2026-07-27 | NEM | BLOCKED | REPAIR | 93.47 | 93.71 | 4 | +0.3% | -0.8 | OPEN |
| 2026-07-27 | ORKA | BLOCKED | PASS | 90.2 | 96.51 | 4 | +7.0% | +5.9 | OPEN |
| 2026-07-27 | PGR | BLOCKED | REPAIR | 215.76 | 211.42 | 4 | -2.0% | -3.1 | OPEN |
| 2026-07-27 | PH | BLOCKED | PASS | 987.31 | 976.53 | 4 | -1.1% | -2.2 | OPEN |
| 2026-07-27 | PRLB | BLOCKED | PASS | 77.64 | 75.05 | 4 | -3.3% | -4.4 | OPEN |
| 2026-07-27 | RCL | BLOCKED | REPAIR | 305.04 | 318.3 | 4 | +4.3% | +3.3 | OPEN |
| 2026-07-27 | ROP | BLOCKED | REPAIR | 375.02 | 391.97 | 4 | +4.5% | +3.5 | OPEN |
| 2026-07-27 | RSPU | BLOCKED | PASS | 81.24 | 78.89 | 4 | -2.9% | -4.0 | OPEN |
| 2026-07-27 | SLB | BLOCKED | PASS | 51.53 | 49.59 | 4 | -3.8% | -4.8 | OPEN |
| 2026-07-27 | SMCI | BLOCKED | DEEP-FAIL | 29.81 | 28.4 | 4 | -4.7% | -5.8 | OPEN |
| 2026-07-27 | SON | BLOCKED | PASS | 58.68 | 56.36 | 4 | -4.0% | -5.0 | OPEN |
| 2026-07-27 | TDY | BLOCKED | PASS | 651.65 | 655.57 | 4 | +0.6% | -0.5 | OPEN |
| 2026-07-27 | TJX | BLOCKED | REPAIR | 156.38 | 157.34 | 4 | +0.6% | -0.5 | OPEN |
| 2026-07-27 | URA | BLOCKED | DEEP-FAIL | 40.32 | 39.07 | 4 | -3.1% | -4.2 | OPEN |
| 2026-07-27 | VRSN | BLOCKED | REPAIR | 274.82 | 290.02 | 4 | +5.5% | +4.5 | OPEN |
| 2026-07-27 | VST | BLOCKED | REPAIR | 157.08 | 148.19 | 4 | -5.7% | -6.7 | OPEN |
| 2026-07-27 | WWD | BLOCKED | PASS | 419.76 | 360.75 | 4 | -14.1% | -15.1 | OPEN |
| 2026-07-27 | XLI | BLOCKED | PASS | 183.2 | 179.84 | 4 | -1.8% | -2.9 | OPEN |
| 2026-07-27 | ACTG | PASSED | PASS | 4.63 | 4.43 | 4 | -4.3% | -5.4 | OPEN |
| 2026-07-27 | DELL | PASSED | PASS | 426.91 | 405.37 | 4 | -5.0% | -6.1 | OPEN |
| 2026-07-27 | DGX | PASSED | PASS | 231.84 | 233.01 | 4 | +0.5% | -0.6 | OPEN |
| 2026-07-27 | EQIX | PASSED | PASS | 1046.79 | 1019.28 | 4 | -2.6% | -3.7 | OPEN |
| 2026-07-27 | GE | PASSED | PASS | 361.61 | 360.07 | 4 | -0.4% | -1.5 | OPEN |
| 2026-07-27 | JNJ | PASSED | PASS | 265.95 | 256.35 | 4 | -3.6% | -4.7 | OPEN |
| 2026-07-27 | LHX | PASSED | REPAIR | 303.48 | 277.06 | 4 | -8.7% | -9.8 | OPEN |
| 2026-07-27 | MLI | PASSED | PASS | 64.17 | 66.41 | 4 | +3.5% | +2.4 | OPEN |
| 2026-07-27 | MRK | PASSED | PASS | 130.76 | 130.2 | 4 | -0.4% | -1.5 | OPEN |
| 2026-07-27 | RHP | PASSED | PASS | 134.94 | 133.65 | 4 | -1.0% | -2.0 | OPEN |
| 2026-07-27 | SJM | PASSED | PASS | 121.05 | 119.26 | 4 | -1.5% | -2.5 | OPEN |
| 2026-07-27 | URI | PASSED | PASS | 1127.91 | 1079.26 | 4 | -4.3% | -5.4 | OPEN |
| 2026-07-28 | ACGL | BLOCKED | PASS | 106.48 | 100.53 | 3 | -5.6% | -6.4 | OPEN |
| 2026-07-28 | AGNC | BLOCKED | PASS | 11.07 | 10.66 | 3 | -3.7% | -4.5 | OPEN |
| 2026-07-28 | AI | BLOCKED | DEEP-FAIL | 8.9 | 9.18 | 3 | +3.1% | +2.3 | OPEN |
| 2026-07-28 | AJG | BLOCKED | REPAIR | 265.31 | 249.42 | 3 | -6.0% | -6.8 | OPEN |
| 2026-07-28 | ALSN | BLOCKED | PASS | 121.11 | 114.54 | 3 | -5.4% | -6.3 | OPEN |
| 2026-07-28 | AVT | BLOCKED | REPAIR | 86.22 | 88.84 | 3 | +3.0% | +2.2 | OPEN |
| 2026-07-28 | AXON | BLOCKED | REPAIR | 547.65 | 527.76 | 3 | -3.6% | -4.5 | OPEN |
| 2026-07-28 | BUD | BLOCKED | PASS | 83.2 | 86.48 | 3 | +3.9% | +3.1 | OPEN |
| 2026-07-28 | CB | BLOCKED | PASS | 363.5 | 350.68 | 3 | -3.5% | -4.4 | OPEN |
| 2026-07-28 | CCL | BLOCKED | REPAIR | 28.23 | 27.81 | 3 | -1.5% | -2.3 | OPEN |
| 2026-07-28 | CHTR | BLOCKED | DEEP-FAIL | 139.97 | 144.98 | 3 | +3.6% | +2.8 | OPEN |
| 2026-07-28 | CLX | BLOCKED | REPAIR | 100.32 | 95.53 | 3 | -4.8% | -5.6 | OPEN |
| 2026-07-28 | CNP | BLOCKED | PASS | 44.1 | 42.04 | 3 | -4.7% | -5.5 | OPEN |
| 2026-07-28 | COKE | BLOCKED | PASS | 195.0 | 187.9 | 3 | -3.6% | -4.5 | OPEN |
| 2026-07-28 | CPRT | BLOCKED | DEEP-FAIL | 30.69 | 29.12 | 3 | -5.1% | -6.0 | OPEN |
| 2026-07-28 | CRCL | BLOCKED | DEEP-FAIL | 64.32 | 62.61 | 3 | -2.7% | -3.5 | OPEN |
| 2026-07-28 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.72 | 3 | +1.4% | +0.5 | OPEN |
| 2026-07-28 | DASH | BLOCKED | REPAIR | 195.52 | 196.16 | 3 | +0.3% | -0.5 | OPEN |
| 2026-07-28 | DUOL | BLOCKED | REPAIR | 140.73 | 134.81 | 3 | -4.2% | -5.0 | OPEN |
| 2026-07-28 | EGBN | BLOCKED | PASS | 28.39 | 27.75 | 3 | -2.2% | -3.1 | OPEN |
| 2026-07-28 | ERIE | BLOCKED | REPAIR | 242.43 | 242.04 | 3 | -0.2% | -1.0 | OPEN |
| 2026-07-28 | F | BLOCKED | PASS | 14.96 | 14.68 | 3 | -1.9% | -2.7 | OPEN |
| 2026-07-28 | FCX | BLOCKED | REPAIR | 61.64 | 62.63 | 3 | +1.6% | +0.8 | OPEN |
| 2026-07-28 | FUTU | BLOCKED | DEEP-FAIL | 101.84 | 105.12 | 3 | +3.2% | +2.4 | OPEN |
| 2026-07-28 | GDX | BLOCKED | DEEP-FAIL | 74.21 | 74.1 | 3 | -0.1% | -1.0 | OPEN |
| 2026-07-28 | GLD | BLOCKED | DEEP-FAIL | 369.37 | 371.54 | 3 | +0.6% | -0.2 | OPEN |
| 2026-07-28 | GM | BLOCKED | PASS | 90.3 | 88.86 | 3 | -1.6% | -2.4 | OPEN |
| 2026-07-28 | HD | BLOCKED | REPAIR | 344.47 | 331.96 | 3 | -3.6% | -4.5 | OPEN |
| 2026-07-28 | JETS | BLOCKED | PASS | 31.86 | 31.28 | 3 | -1.8% | -2.6 | OPEN |
| 2026-07-28 | LDOS | BLOCKED | DEEP-FAIL | 118.36 | 115.6 | 3 | -2.3% | -3.2 | OPEN |
| 2026-07-28 | LOW | BLOCKED | REPAIR | 218.24 | 207.81 | 3 | -4.8% | -5.6 | OPEN |
| 2026-07-28 | LZB | BLOCKED | PASS | 41.3 | 39.38 | 3 | -4.7% | -5.5 | OPEN |
| 2026-07-28 | MAR | BLOCKED | PASS | 383.52 | 372.83 | 3 | -2.8% | -3.6 | OPEN |
| 2026-07-28 | MCD | BLOCKED | REPAIR | 273.02 | 270.64 | 3 | -0.9% | -1.7 | OPEN |
| 2026-07-28 | MDT | BLOCKED | REPAIR | 86.88 | 85.39 | 3 | -1.7% | -2.5 | OPEN |
| 2026-07-28 | NCLH | BLOCKED | REPAIR | 21.22 | 18.53 | 3 | -12.7% | -13.5 | OPEN |
| 2026-07-28 | NEM | BLOCKED | DEEP-FAIL | 91.52 | 93.71 | 3 | +2.4% | +1.6 | OPEN |
| 2026-07-28 | NFLX | BLOCKED | DEEP-FAIL | 72.39 | 71.71 | 3 | -0.9% | -1.8 | OPEN |
| 2026-07-28 | NOW | BLOCKED | DEEP-FAIL | 110.62 | 111.23 | 3 | +0.6% | -0.3 | OPEN |
| 2026-07-28 | PGR | BLOCKED | REPAIR | 219.52 | 211.42 | 3 | -3.7% | -4.5 | OPEN |
| 2026-07-28 | PH | BLOCKED | PASS | 990.96 | 976.53 | 3 | -1.5% | -2.3 | OPEN |
| 2026-07-28 | RACE | BLOCKED | REPAIR | 390.14 | 393.87 | 3 | +1.0% | +0.1 | OPEN |
| 2026-07-28 | RCL | BLOCKED | REPAIR | 322.5 | 318.3 | 3 | -1.3% | -2.1 | OPEN |
| 2026-07-28 | RMD | BLOCKED | DEEP-FAIL | 208.96 | 210.98 | 3 | +1.0% | +0.1 | OPEN |
| 2026-07-28 | ROP | BLOCKED | REPAIR | 390.92 | 391.97 | 3 | +0.3% | -0.6 | OPEN |
| 2026-07-28 | RSPU | BLOCKED | PASS | 81.03 | 78.89 | 3 | -2.6% | -3.5 | OPEN |
| 2026-07-28 | SHAK | BLOCKED | DEEP-FAIL | 63.2 | 62.75 | 3 | -0.7% | -1.5 | OPEN |
| 2026-07-28 | SHW | BLOCKED | REPAIR | 354.27 | 340.85 | 3 | -3.8% | -4.6 | OPEN |
| 2026-07-28 | SMCI | BLOCKED | DEEP-FAIL | 28.45 | 28.4 | 3 | -0.2% | -1.0 | OPEN |
| 2026-07-28 | SON | BLOCKED | PASS | 60.56 | 56.36 | 3 | -6.9% | -7.8 | OPEN |
| 2026-07-28 | STGW | BLOCKED | PASS | 7.97 | 8.45 | 3 | +6.0% | +5.2 | OPEN |
| 2026-07-28 | TDY | BLOCKED | PASS | 649.67 | 655.57 | 3 | +0.9% | +0.1 | OPEN |
| 2026-07-28 | TOST | BLOCKED | REPAIR | 32.34 | 32.27 | 3 | -0.2% | -1.1 | OPEN |
| 2026-07-28 | TPR | BLOCKED | PASS | 150.9 | 152.37 | 3 | +1.0% | +0.1 | OPEN |
| 2026-07-28 | TYL | BLOCKED | DEEP-FAIL | 333.35 | 309.6 | 3 | -7.1% | -8.0 | OPEN |
| 2026-07-28 | URA | BLOCKED | DEEP-FAIL | 38.95 | 39.07 | 3 | +0.3% | -0.5 | OPEN |
| 2026-07-28 | URI | BLOCKED | PASS | 1091.26 | 1079.26 | 3 | -1.1% | -1.9 | OPEN |
| 2026-07-28 | VRSN | BLOCKED | REPAIR | 281.15 | 290.02 | 3 | +3.1% | +2.3 | OPEN |
| 2026-07-28 | WWD | BLOCKED | PASS | 410.55 | 360.75 | 3 | -12.1% | -13.0 | OPEN |
| 2026-07-28 | XLI | BLOCKED | PASS | 182.49 | 179.84 | 3 | -1.4% | -2.3 | OPEN |
| 2026-07-28 | ZTS | BLOCKED | DEEP-FAIL | 77.51 | 77.29 | 3 | -0.3% | -1.1 | OPEN |
| 2026-07-28 | ACTG | PASSED | PASS | 4.63 | 4.43 | 3 | -4.3% | -5.2 | OPEN |
| 2026-07-28 | CTS | PASSED | PASS | 64.82 | 64.12 | 3 | -1.1% | -1.9 | OPEN |
| 2026-07-28 | DAL | PASSED | PASS | 89.37 | 87.44 | 3 | -2.2% | -3.0 | OPEN |
| 2026-07-28 | DE | PASSED | PASS | 639.84 | 592.67 | 3 | -7.4% | -8.2 | OPEN |
| 2026-07-28 | DGX | PASSED | PASS | 235.94 | 233.01 | 3 | -1.2% | -2.1 | OPEN |
| 2026-07-28 | DLR | PASSED | PASS | 193.18 | 188.52 | 3 | -2.4% | -3.2 | OPEN |
| 2026-07-28 | EQIX | PASSED | REPAIR | 1034.86 | 1019.28 | 3 | -1.5% | -2.3 | OPEN |
| 2026-07-28 | GE | PASSED | PASS | 363.59 | 360.07 | 3 | -1.0% | -1.8 | OPEN |
| 2026-07-28 | HON | PASSED | PASS | 247.05 | 243.05 | 3 | -1.6% | -2.5 | OPEN |
| 2026-07-28 | JNJ | PASSED | PASS | 266.73 | 256.35 | 3 | -3.9% | -4.7 | OPEN |
| 2026-07-28 | LHX | PASSED | REPAIR | 305.2 | 277.06 | 3 | -9.2% | -10.1 | OPEN |
| 2026-07-28 | LLY | PASSED | PASS | 1220.66 | 1148.84 | 3 | -5.9% | -6.7 | OPEN |
| 2026-07-28 | MLI | PASSED | PASS | 66.49 | 66.41 | 3 | -0.1% | -0.9 | OPEN |
| 2026-07-28 | MNST | PASSED | PASS | 97.74 | 96.38 | 3 | -1.4% | -2.2 | OPEN |
| 2026-07-28 | MRK | PASSED | PASS | 131.82 | 130.2 | 3 | -1.2% | -2.1 | OPEN |
| 2026-07-28 | PEP | PASSED | REPAIR | 142.86 | 139.56 | 3 | -2.3% | -3.1 | OPEN |
| 2026-07-28 | SLB | PASSED | REPAIR | 49.98 | 49.59 | 3 | -0.8% | -1.6 | OPEN |
| 2026-07-28 | SSD | PASSED | PASS | 198.28 | 187.74 | 3 | -5.3% | -6.2 | OPEN |
| 2026-07-28 | TJX | PASSED | PASS | 160.8 | 157.34 | 3 | -2.1% | -3.0 | OPEN |
| 2026-07-29 | ABNB | BLOCKED | PASS | 153.01 | 151.52 | 2 | -1.0% | -3.4 | OPEN |
| 2026-07-29 | ACGL | BLOCKED | PASS | 104.55 | 100.53 | 2 | -3.9% | -6.2 | OPEN |
| 2026-07-29 | AGNC | BLOCKED | PASS | 10.9 | 10.66 | 2 | -2.2% | -4.6 | OPEN |
| 2026-07-29 | AI | BLOCKED | DEEP-FAIL | 8.85 | 9.18 | 2 | +3.7% | +1.3 | OPEN |
| 2026-07-29 | AJG | BLOCKED | REPAIR | 268.91 | 249.42 | 2 | -7.2% | -9.7 | OPEN |
| 2026-07-29 | AXON | BLOCKED | REPAIR | 531.2 | 527.76 | 2 | -0.7% | -3.1 | OPEN |
| 2026-07-29 | BFC | BLOCKED | PASS | 151.78 | 152.74 | 2 | +0.6% | -1.8 | OPEN |
| 2026-07-29 | CB | BLOCKED | PASS | 361.9 | 350.68 | 2 | -3.1% | -5.5 | OPEN |
| 2026-07-29 | CHTR | BLOCKED | DEEP-FAIL | 145.2 | 144.98 | 2 | -0.1% | -2.6 | OPEN |
| 2026-07-29 | CLX | BLOCKED | REPAIR | 99.63 | 95.53 | 2 | -4.1% | -6.5 | OPEN |
| 2026-07-29 | CMG | BLOCKED | REPAIR | 34.24 | 37.22 | 2 | +8.7% | +6.3 | OPEN |
| 2026-07-29 | CNP | BLOCKED | PASS | 42.93 | 42.04 | 2 | -2.1% | -4.5 | OPEN |
| 2026-07-29 | COKE | BLOCKED | PASS | 192.39 | 187.9 | 2 | -2.3% | -4.7 | OPEN |
| 2026-07-29 | CPRT | BLOCKED | DEEP-FAIL | 30.82 | 29.12 | 2 | -5.5% | -7.9 | OPEN |
| 2026-07-29 | CTM | BLOCKED | DEEP-FAIL | 0.66 | 0.72 | 2 | +8.1% | +5.7 | OPEN |
| 2026-07-29 | DASH | BLOCKED | REPAIR | 193.53 | 196.16 | 2 | +1.4% | -1.1 | OPEN |
| 2026-07-29 | DE | BLOCKED | PASS | 610.95 | 592.67 | 2 | -3.0% | -5.4 | OPEN |
| 2026-07-29 | DUOL | BLOCKED | REPAIR | 140.17 | 134.81 | 2 | -3.8% | -6.2 | OPEN |
| 2026-07-29 | EGBN | BLOCKED | PASS | 27.89 | 27.75 | 2 | -0.5% | -2.9 | OPEN |
| 2026-07-29 | EQIX | BLOCKED | REPAIR | 1008.02 | 1019.28 | 2 | +1.1% | -1.3 | OPEN |
| 2026-07-29 | ERIE | BLOCKED | REPAIR | 248.55 | 242.04 | 2 | -2.6% | -5.0 | OPEN |
| 2026-07-29 | ESQ | BLOCKED | PASS | 131.89 | 129.22 | 2 | -2.0% | -4.4 | OPEN |
| 2026-07-29 | FCX | BLOCKED | REPAIR | 59.99 | 62.63 | 2 | +4.4% | +2.0 | OPEN |
| 2026-07-29 | GDX | BLOCKED | DEEP-FAIL | 73.57 | 74.1 | 2 | +0.7% | -1.7 | OPEN |
| 2026-07-29 | GME | BLOCKED | REPAIR | 21.84 | 21.72 | 2 | -0.6% | -3.0 | OPEN |
| 2026-07-29 | GRND | BLOCKED | PASS | 17.21 | 17.34 | 2 | +0.8% | -1.6 | OPEN |
| 2026-07-29 | HD | BLOCKED | REPAIR | 338.27 | 331.96 | 2 | -1.9% | -4.3 | OPEN |
| 2026-07-29 | IBM | BLOCKED | DEEP-FAIL | 226.44 | 223.65 | 2 | -1.2% | -3.6 | OPEN |
| 2026-07-29 | JBLU | BLOCKED | PASS | 5.72 | 6.03 | 2 | +5.4% | +3.0 | OPEN |
| 2026-07-29 | JETS | BLOCKED | PASS | 30.97 | 31.28 | 2 | +1.0% | -1.4 | OPEN |
| 2026-07-29 | KWEB | BLOCKED | DEEP-FAIL | 27.8 | 28.49 | 2 | +2.5% | +0.1 | OPEN |
| 2026-07-29 | LDOS | BLOCKED | DEEP-FAIL | 114.37 | 115.6 | 2 | +1.1% | -1.3 | OPEN |
| 2026-07-29 | LOW | BLOCKED | REPAIR | 215.68 | 207.81 | 2 | -3.6% | -6.1 | OPEN |
| 2026-07-29 | LZB | BLOCKED | PASS | 40.93 | 39.38 | 2 | -3.8% | -6.2 | OPEN |
| 2026-07-29 | MAR | BLOCKED | PASS | 381.12 | 372.83 | 2 | -2.2% | -4.6 | OPEN |
| 2026-07-29 | MCD | BLOCKED | REPAIR | 271.52 | 270.64 | 2 | -0.3% | -2.7 | OPEN |
| 2026-07-29 | NCLH | BLOCKED | REPAIR | 20.75 | 18.53 | 2 | -10.7% | -13.1 | OPEN |
| 2026-07-29 | NEM | BLOCKED | DEEP-FAIL | 91.34 | 93.71 | 2 | +2.6% | +0.2 | OPEN |
| 2026-07-29 | NEO | BLOCKED | PASS | 15.27 | 15.29 | 2 | +0.1% | -2.3 | OPEN |
| 2026-07-29 | NFLX | BLOCKED | DEEP-FAIL | 73.63 | 71.71 | 2 | -2.6% | -5.0 | OPEN |
| 2026-07-29 | NIO | BLOCKED | DEEP-FAIL | 4.76 | 4.88 | 2 | +2.5% | +0.1 | OPEN |
| 2026-07-29 | NOW | BLOCKED | REPAIR | 115.76 | 111.23 | 2 | -3.9% | -6.3 | OPEN |
| 2026-07-29 | NVST | BLOCKED | PASS | 28.37 | 27.31 | 2 | -3.7% | -6.1 | OPEN |
| 2026-07-29 | PGR | BLOCKED | REPAIR | 219.99 | 211.42 | 2 | -3.9% | -6.3 | OPEN |
| 2026-07-29 | PH | BLOCKED | PASS | 951.07 | 976.53 | 2 | +2.7% | +0.3 | OPEN |
| 2026-07-29 | RCL | BLOCKED | REPAIR | 323.58 | 318.3 | 2 | -1.6% | -4.0 | OPEN |
| 2026-07-29 | RMD | BLOCKED | REPAIR | 214.29 | 210.98 | 2 | -1.5% | -4.0 | OPEN |
| 2026-07-29 | ROKU | BLOCKED | PASS | 145.33 | 145.01 | 2 | -0.2% | -2.6 | OPEN |
| 2026-07-29 | ROP | BLOCKED | REPAIR | 408.07 | 391.97 | 2 | -4.0% | -6.3 | OPEN |
| 2026-07-29 | RSPU | BLOCKED | PASS | 79.85 | 78.89 | 2 | -1.2% | -3.6 | OPEN |
| 2026-07-29 | SHAK | BLOCKED | DEEP-FAIL | 63.05 | 62.75 | 2 | -0.5% | -2.9 | OPEN |
| 2026-07-29 | SHW | BLOCKED | REPAIR | 343.88 | 340.85 | 2 | -0.9% | -3.3 | OPEN |
| 2026-07-29 | SKYY | BLOCKED | PASS | 138.56 | 143.0 | 2 | +3.2% | +0.8 | OPEN |
| 2026-07-29 | SMCI | BLOCKED | DEEP-FAIL | 25.7 | 28.4 | 2 | +10.5% | +8.1 | OPEN |
| 2026-07-29 | STGW | BLOCKED | PASS | 8.08 | 8.45 | 2 | +4.6% | +2.2 | OPEN |
| 2026-07-29 | TDY | BLOCKED | PASS | 631.35 | 655.57 | 2 | +3.8% | +1.4 | OPEN |
| 2026-07-29 | TOST | BLOCKED | REPAIR | 32.6 | 32.27 | 2 | -1.0% | -3.4 | OPEN |
| 2026-07-29 | TPR | BLOCKED | PASS | 150.11 | 152.37 | 2 | +1.5% | -0.9 | OPEN |
| 2026-07-29 | TYL | BLOCKED | DEEP-FAIL | 333.5 | 309.6 | 2 | -7.2% | -9.6 | OPEN |
| 2026-07-29 | URI | BLOCKED | PASS | 1055.11 | 1079.26 | 2 | +2.3% | -0.1 | OPEN |
| 2026-07-29 | VRSN | BLOCKED | REPAIR | 290.92 | 290.02 | 2 | -0.3% | -2.7 | OPEN |
| 2026-07-29 | WWD | BLOCKED | PASS | 385.42 | 360.75 | 2 | -6.4% | -8.8 | OPEN |
| 2026-07-29 | ZTS | BLOCKED | DEEP-FAIL | 77.93 | 77.29 | 2 | -0.8% | -3.2 | OPEN |
| 2026-07-29 | CCL | PASSED | REPAIR | 27.81 | 27.81 | 2 | +0.0% | -2.4 | OPEN |
| 2026-07-29 | CPT | PASSED | PASS | 116.37 | 110.81 | 2 | -4.8% | -7.2 | OPEN |
| 2026-07-29 | CTS | PASSED | PASS | 61.53 | 64.12 | 2 | +4.2% | +1.8 | OPEN |
| 2026-07-29 | DAL | PASSED | PASS | 86.25 | 87.44 | 2 | +1.4% | -1.0 | OPEN |
| 2026-07-29 | DGX | PASSED | PASS | 235.22 | 233.01 | 2 | -0.9% | -3.4 | OPEN |
| 2026-07-29 | DLR | PASSED | PASS | 188.18 | 188.52 | 2 | +0.2% | -2.2 | OPEN |
| 2026-07-29 | GE | PASSED | PASS | 350.63 | 360.07 | 2 | +2.7% | +0.3 | OPEN |
| 2026-07-29 | HON | PASSED | PASS | 241.12 | 243.05 | 2 | +0.8% | -1.6 | OPEN |
| 2026-07-29 | JNJ | PASSED | PASS | 265.53 | 256.35 | 2 | -3.5% | -5.9 | OPEN |
| 2026-07-29 | KDP | PASSED | PASS | 31.45 | 31.12 | 2 | -1.1% | -3.5 | OPEN |
| 2026-07-29 | LHX | PASSED | REPAIR | 297.53 | 277.06 | 2 | -6.9% | -9.3 | OPEN |
| 2026-07-29 | LLY | PASSED | PASS | 1210.02 | 1148.84 | 2 | -5.1% | -7.5 | OPEN |
| 2026-07-29 | MDT | PASSED | REPAIR | 87.54 | 85.39 | 2 | -2.5% | -4.9 | OPEN |
| 2026-07-29 | MNST | PASSED | PASS | 97.23 | 96.38 | 2 | -0.9% | -3.3 | OPEN |
| 2026-07-29 | MRK | PASSED | PASS | 130.36 | 130.2 | 2 | -0.1% | -2.5 | OPEN |
| 2026-07-29 | PEP | PASSED | REPAIR | 143.5 | 139.56 | 2 | -2.8% | -5.2 | OPEN |
| 2026-07-29 | RACE | PASSED | REPAIR | 385.69 | 393.87 | 2 | +2.1% | -0.3 | OPEN |
| 2026-07-29 | SLB | PASSED | REPAIR | 48.96 | 49.59 | 2 | +1.3% | -1.1 | OPEN |
| 2026-07-29 | SSD | PASSED | REPAIR | 189.48 | 187.74 | 2 | -0.9% | -3.3 | OPEN |
| 2026-07-29 | TJX | PASSED | PASS | 161.63 | 157.34 | 2 | -2.6% | -5.1 | OPEN |
| 2026-07-30 | ABNB | BLOCKED | PASS | 152.08 | 151.52 | 1 | -0.4% | -1.1 | OPEN |
| 2026-07-30 | ACGL | BLOCKED | PASS | 101.14 | 100.53 | 1 | -0.6% | -1.3 | OPEN |
| 2026-07-30 | AGNC | BLOCKED | PASS | 10.92 | 10.66 | 1 | -2.4% | -3.1 | OPEN |
| 2026-07-30 | AI | BLOCKED | DEEP-FAIL | 9.07 | 9.18 | 1 | +1.2% | +0.5 | OPEN |
| 2026-07-30 | AJG | BLOCKED | REPAIR | 256.46 | 249.42 | 1 | -2.8% | -3.5 | OPEN |
| 2026-07-30 | APD | BLOCKED | PASS | 300.2 | 294.89 | 1 | -1.8% | -2.5 | OPEN |
| 2026-07-30 | AXON | BLOCKED | REPAIR | 525.3 | 527.76 | 1 | +0.5% | -0.2 | OPEN |
| 2026-07-30 | CB | BLOCKED | PASS | 350.15 | 350.68 | 1 | +0.1% | -0.6 | OPEN |
| 2026-07-30 | CHTR | BLOCKED | DEEP-FAIL | 142.0 | 144.98 | 1 | +2.1% | +1.4 | OPEN |
| 2026-07-30 | CLX | BLOCKED | REPAIR | 96.73 | 95.53 | 1 | -1.2% | -2.0 | OPEN |
| 2026-07-30 | CMG | BLOCKED | REPAIR | 38.52 | 37.22 | 1 | -3.4% | -4.1 | OPEN |
| 2026-07-30 | CNP | BLOCKED | REPAIR | 42.15 | 42.04 | 1 | -0.3% | -1.0 | OPEN |
| 2026-07-30 | COKE | BLOCKED | PASS | 189.83 | 187.9 | 1 | -1.0% | -1.7 | OPEN |
| 2026-07-30 | CPRT | BLOCKED | DEEP-FAIL | 29.57 | 29.12 | 1 | -1.5% | -2.2 | OPEN |
| 2026-07-30 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.72 | 1 | +0.8% | +0.1 | OPEN |
| 2026-07-30 | DASH | BLOCKED | REPAIR | 197.53 | 196.16 | 1 | -0.7% | -1.4 | OPEN |
| 2026-07-30 | DE | BLOCKED | PASS | 599.47 | 592.67 | 1 | -1.1% | -1.9 | OPEN |
| 2026-07-30 | DUOL | BLOCKED | REPAIR | 133.6 | 134.81 | 1 | +0.9% | +0.2 | OPEN |
| 2026-07-30 | EGBN | BLOCKED | PASS | 27.49 | 27.75 | 1 | +0.9% | +0.2 | OPEN |
| 2026-07-30 | GME | BLOCKED | REPAIR | 21.88 | 21.72 | 1 | -0.7% | -1.4 | OPEN |
| 2026-07-30 | HD | BLOCKED | REPAIR | 333.35 | 331.96 | 1 | -0.4% | -1.1 | OPEN |
| 2026-07-30 | IBM | BLOCKED | DEEP-FAIL | 221.74 | 223.65 | 1 | +0.9% | +0.1 | OPEN |
| 2026-07-30 | JBLU | BLOCKED | PASS | 6.07 | 6.03 | 1 | -0.7% | -1.4 | OPEN |
| 2026-07-30 | KWEB | BLOCKED | DEEP-FAIL | 28.06 | 28.49 | 1 | +1.5% | +0.8 | OPEN |
| 2026-07-30 | LDOS | BLOCKED | DEEP-FAIL | 112.41 | 115.6 | 1 | +2.8% | +2.1 | OPEN |
| 2026-07-30 | LLY | BLOCKED | PASS | 1154.97 | 1148.84 | 1 | -0.5% | -1.2 | OPEN |
| 2026-07-30 | LOW | BLOCKED | DEEP-FAIL | 210.08 | 207.81 | 1 | -1.1% | -1.8 | OPEN |
| 2026-07-30 | LYV | BLOCKED | PASS | 183.56 | 174.13 | 1 | -5.1% | -5.9 | OPEN |
| 2026-07-30 | LZB | BLOCKED | PASS | 40.13 | 39.38 | 1 | -1.9% | -2.6 | OPEN |
| 2026-07-30 | MAR | BLOCKED | REPAIR | 375.48 | 372.83 | 1 | -0.7% | -1.4 | OPEN |
| 2026-07-30 | MCD | BLOCKED | DEEP-FAIL | 268.44 | 270.64 | 1 | +0.8% | +0.1 | OPEN |
| 2026-07-30 | MIDD | BLOCKED | PASS | 133.32 | 133.58 | 1 | +0.2% | -0.5 | OPEN |
| 2026-07-30 | MRK | BLOCKED | PASS | 129.79 | 130.2 | 1 | +0.3% | -0.4 | OPEN |
| 2026-07-30 | MSFT | BLOCKED | REPAIR | 451.1 | 464.72 | 1 | +3.0% | +2.3 | OPEN |
| 2026-07-30 | NCLH | BLOCKED | REPAIR | 18.72 | 18.53 | 1 | -1.0% | -1.7 | OPEN |
| 2026-07-30 | NFLX | BLOCKED | DEEP-FAIL | 73.17 | 71.71 | 1 | -2.0% | -2.7 | OPEN |
| 2026-07-30 | NIO | BLOCKED | DEEP-FAIL | 4.84 | 4.88 | 1 | +0.8% | +0.1 | OPEN |
| 2026-07-30 | NOW | BLOCKED | DEEP-FAIL | 110.07 | 111.23 | 1 | +1.1% | +0.3 | OPEN |
| 2026-07-30 | NVST | BLOCKED | PASS | 27.78 | 27.31 | 1 | -1.7% | -2.4 | OPEN |
| 2026-07-30 | PB | BLOCKED | PASS | 74.82 | 74.87 | 1 | +0.1% | -0.7 | OPEN |
| 2026-07-30 | PGR | BLOCKED | REPAIR | 213.28 | 211.42 | 1 | -0.9% | -1.6 | OPEN |
| 2026-07-30 | PH | BLOCKED | PASS | 962.79 | 976.53 | 1 | +1.4% | +0.7 | OPEN |
| 2026-07-30 | RCL | BLOCKED | REPAIR | 321.94 | 318.3 | 1 | -1.1% | -1.9 | OPEN |
| 2026-07-30 | RMD | BLOCKED | REPAIR | 208.56 | 210.98 | 1 | +1.2% | +0.4 | OPEN |
| 2026-07-30 | ROKU | BLOCKED | PASS | 145.09 | 145.01 | 1 | -0.1% | -0.8 | OPEN |
| 2026-07-30 | RSPU | BLOCKED | REPAIR | 79.51 | 78.89 | 1 | -0.8% | -1.5 | OPEN |
| 2026-07-30 | SFM | BLOCKED | REPAIR | 86.85 | 87.16 | 1 | +0.4% | -0.4 | OPEN |
| 2026-07-30 | SHAK | BLOCKED | DEEP-FAIL | 63.07 | 62.75 | 1 | -0.5% | -1.2 | OPEN |
| 2026-07-30 | SHW | BLOCKED | REPAIR | 344.84 | 340.85 | 1 | -1.2% | -1.9 | OPEN |
| 2026-07-30 | SKYY | BLOCKED | PASS | 140.03 | 143.0 | 1 | +2.1% | +1.4 | OPEN |
| 2026-07-30 | SSD | BLOCKED | REPAIR | 186.67 | 187.74 | 1 | +0.6% | -0.1 | OPEN |
| 2026-07-30 | STGW | BLOCKED | PASS | 8.49 | 8.45 | 1 | -0.5% | -1.2 | OPEN |
| 2026-07-30 | TDY | BLOCKED | PASS | 649.18 | 655.57 | 1 | +1.0% | +0.3 | OPEN |
| 2026-07-30 | TOST | BLOCKED | REPAIR | 32.85 | 32.27 | 1 | -1.8% | -2.5 | OPEN |
| 2026-07-30 | TPR | BLOCKED | PASS | 152.58 | 152.37 | 1 | -0.1% | -0.9 | OPEN |
| 2026-07-30 | TYL | BLOCKED | DEEP-FAIL | 323.31 | 309.6 | 1 | -4.2% | -5.0 | OPEN |
| 2026-07-30 | URI | BLOCKED | PASS | 1068.63 | 1079.26 | 1 | +1.0% | +0.3 | OPEN |
| 2026-07-30 | ZTS | BLOCKED | DEEP-FAIL | 76.03 | 77.29 | 1 | +1.7% | +0.9 | OPEN |
| 2026-07-30 | CCL | PASSED | REPAIR | 27.77 | 27.81 | 1 | +0.1% | -0.6 | OPEN |
| 2026-07-30 | CPT | PASSED | PASS | 113.29 | 110.81 | 1 | -2.2% | -2.9 | OPEN |
| 2026-07-30 | CTS | PASSED | REPAIR | 62.7 | 64.12 | 1 | +2.3% | +1.5 | OPEN |
| 2026-07-30 | DAL | PASSED | PASS | 88.59 | 87.44 | 1 | -1.3% | -2.0 | OPEN |
| 2026-07-30 | DGX | PASSED | PASS | 234.3 | 233.01 | 1 | -0.6% | -1.3 | OPEN |
| 2026-07-30 | EQIX | PASSED | PASS | 1047.53 | 1019.28 | 1 | -2.7% | -3.4 | OPEN |
| 2026-07-30 | ERIE | PASSED | REPAIR | 233.67 | 242.04 | 1 | +3.6% | +2.9 | OPEN |
| 2026-07-30 | GE | PASSED | PASS | 355.04 | 360.07 | 1 | +1.4% | +0.7 | OPEN |
| 2026-07-30 | JETS | PASSED | PASS | 31.68 | 31.28 | 1 | -1.3% | -2.0 | OPEN |
| 2026-07-30 | KDP | PASSED | PASS | 31.57 | 31.12 | 1 | -1.4% | -2.1 | OPEN |
| 2026-07-30 | MDT | PASSED | REPAIR | 85.71 | 85.39 | 1 | -0.4% | -1.1 | OPEN |
| 2026-07-30 | MNST | PASSED | PASS | 97.65 | 96.38 | 1 | -1.3% | -2.0 | OPEN |
| 2026-07-30 | PEP | PASSED | REPAIR | 140.2 | 139.56 | 1 | -0.5% | -1.2 | OPEN |
| 2026-07-30 | RACE | PASSED | REPAIR | 397.73 | 393.87 | 1 | -1.0% | -1.7 | OPEN |
| 2026-07-30 | ROP | PASSED | REPAIR | 389.25 | 391.97 | 1 | +0.7% | -0.0 | OPEN |
| 2026-07-30 | ST | PASSED | PASS | 47.99 | 46.29 | 1 | -3.5% | -4.3 | OPEN |
| 2026-07-30 | TJX | PASSED | PASS | 159.26 | 157.34 | 1 | -1.2% | -1.9 | OPEN |
| 2026-07-30 | VRSN | PASSED | REPAIR | 286.58 | 290.02 | 1 | +1.2% | +0.5 | OPEN |

Open marks are not results. This file exists so that the cull the scan performs every night is measured instead of assumed.
