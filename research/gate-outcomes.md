# Gate stack forward grade

Does THE GATE STACK earn its keep? Every fresh Chandelier signal is graded forward from the CLOSE of its signal date over 21 trading sessions, bucketed by what the stack decided. The number that matters is the SPREAD.

- Signal events found: 514  |  priced: 438  |  unique symbol-cohort pairs (headline sample): 222
- Skipped (pre-2026-07-22 hand-written verdicts, not machine-comparable): 20

## Headline - all signals, deduped to first appearance

| Cohort | n | Win% | Mean | Median | Mean vs SPY | Mean worst drawdown |
|---|---|---|---|---|---|---|
| PASSED | 45 | 40% | -0.76% | -0.87% | -0.80% | -5.00% |
| BLOCKED | 177 | 44% | -0.68% | -0.67% | -0.49% | -5.53% |

**Spread (PASSED minus BLOCKED): -0.08 percentage points.**

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
| ADX FLOOR | 55 | 47% | -0.09% | -0.20% | +0.08% |
| ATR GEOMETRY | 7 | 29% | -2.77% | -2.96% | -3.16% |
| DIRECTION | 11 | 9% | -5.06% | -2.40% | -4.60% |
| LIQUIDITY | 1 | 0% | -10.92% | -10.92% | -10.15% |
| OTHER | 30 | 40% | +0.08% | -0.98% | +0.61% |
| REGIME | 21 | 48% | -0.57% | -0.19% | -0.72% |
| VOLATILITY CAP (ex 2:1) | 5 | 20% | -2.43% | -3.61% | -2.37% |
| ZLSMA | 47 | 53% | -0.15% | +0.37% | +0.02% |

## Shadow cohorts - the forbidden retro-tune, run forward instead

Would lowering the ADX floor to 18, or softening DEEP-FAIL, have helped? The replay's missed monsters make that tempting; answering it by re-running history is curve-fitting. These cohorts answer it FORWARD: sole-failure near-misses graded nightly against the PASSED cohort. Promotion bar (pre-registered): >=30 MATURED signals AND mean above PASSED's - then it goes to a Friday review, not before.

| Shadow cohort | n | Win% | Mean | Median | Mean vs SPY | PASSED mean (ref) |
|---|---|---|---|---|---|---|
| ADX 18-20, all else passed | 5 | 20% | -1.38% | -1.68% | -1.59% | -0.76% |
| DEEP-FAIL, all else passed | 2 | 50% | -0.26% | -0.26% | -0.62% | -0.76% |

## Every graded signal

| Date | Sym | Cohort | Regime | Entry | Mark | Days | Return | vs SPY | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | BG | BLOCKED | n/a | 120.49 | 105.07 | 8 | -12.8% | -12.7 | OPEN |
| 2026-07-20 | CHRD | BLOCKED | n/a | 128.8 | 138.25 | 8 | +7.3% | +7.4 | OPEN |
| 2026-07-20 | CNOB | BLOCKED | n/a | 33.46 | 32.95 | 8 | -1.5% | -1.5 | OPEN |
| 2026-07-20 | COCO | BLOCKED | PASS | 73.87 | 66.95 | 8 | -9.4% | -9.3 | OPEN |
| 2026-07-20 | CVNA | BLOCKED | DEEP-FAIL | 64.14 | 61.44 | 8 | -4.2% | -4.2 | OPEN |
| 2026-07-20 | FLG | BLOCKED | n/a | 14.84 | 14.25 | 8 | -4.0% | -3.9 | OPEN |
| 2026-07-20 | FNB | BLOCKED | n/a | 18.75 | 18.99 | 8 | +1.3% | +1.3 | OPEN |
| 2026-07-20 | HAS | BLOCKED | REPAIR | 81.59 | 94.53 | 8 | +15.9% | +15.9 | OPEN |
| 2026-07-20 | HLX | BLOCKED | n/a | 9.43 | 9.2 | 8 | -2.4% | -2.4 | OPEN |
| 2026-07-20 | LCID | BLOCKED | n/a | 7.11 | 8.12 | 8 | +14.2% | +14.3 | OPEN |
| 2026-07-20 | M | BLOCKED | REPAIR | 23.31 | 24.93 | 8 | +7.0% | +7.0 | OPEN |
| 2026-07-20 | NOV | BLOCKED | REPAIR | 19.55 | 19.3 | 8 | -1.3% | -1.2 | OPEN |
| 2026-07-20 | ODFL | BLOCKED | PASS | 231.76 | 212.47 | 8 | -8.3% | -8.3 | OPEN |
| 2026-07-20 | RYZ | BLOCKED | n/a | 29.07 | 26.81 | 8 | -7.8% | -7.7 | OPEN |
| 2026-07-20 | SHAK | BLOCKED | DEEP-FAIL | 56.97 | 63.07 | 8 | +10.7% | +10.8 | OPEN |
| 2026-07-20 | SPG | BLOCKED | PASS | 228.19 | 230.44 | 8 | +1.0% | +1.0 | OPEN |
| 2026-07-20 | TRNS | BLOCKED | n/a | 86.09 | 83.34 | 8 | -3.2% | -3.1 | OPEN |
| 2026-07-20 | VVV | BLOCKED | PASS | 39.54 | 38.39 | 8 | -2.9% | -2.9 | OPEN |
| 2026-07-20 | VZ | BLOCKED | REPAIR | 43.5 | 46.11 | 8 | +6.0% | +6.0 | OPEN |
| 2026-07-20 | WPC | BLOCKED | REPAIR | 75.17 | 74.08 | 8 | -1.4% | -1.4 | OPEN |
| 2026-07-21 | ALKS | BLOCKED | TAPE OK | 52.85 | 50.03 | 7 | -5.3% | -4.5 | OPEN |
| 2026-07-21 | ATLC | BLOCKED | TAPE OK | 96.37 | 106.05 | 7 | +10.0% | +10.9 | OPEN |
| 2026-07-21 | BRKR | BLOCKED | TAPE OK | 60.43 | 64.34 | 7 | +6.5% | +7.3 | OPEN |
| 2026-07-21 | CB | BLOCKED | TAPE OK | 354.8 | 350.15 | 7 | -1.3% | -0.4 | OPEN |
| 2026-07-21 | CBL | BLOCKED | TAPE OK | 55.53 | 58.28 | 7 | +5.0% | +5.8 | OPEN |
| 2026-07-21 | CNOB | BLOCKED | TAPE OK | 33.41 | 32.95 | 7 | -1.4% | -0.5 | OPEN |
| 2026-07-21 | COCO | BLOCKED | TAPE OK | 75.89 | 66.95 | 7 | -11.8% | -10.9 | OPEN |
| 2026-07-21 | CTRE | BLOCKED | TAPE OK | 43.4 | 41.64 | 7 | -4.1% | -3.2 | OPEN |
| 2026-07-21 | ESQ | BLOCKED | TAPE OK | 122.83 | 129.62 | 7 | +5.5% | +6.4 | OPEN |
| 2026-07-21 | EXTR | BLOCKED | TAPE OK | 30.44 | 29.84 | 7 | -2.0% | -1.1 | OPEN |
| 2026-07-21 | FFIV | BLOCKED | TAPE OK | 408.74 | 388.75 | 7 | -4.9% | -4.0 | OPEN |
| 2026-07-21 | FRT | BLOCKED | TAPE OK | 125.59 | 124.09 | 7 | -1.2% | -0.3 | OPEN |
| 2026-07-21 | HCSG | BLOCKED | TAPE OK | 24.8 | 23.08 | 7 | -6.9% | -6.0 | OPEN |
| 2026-07-21 | HELE | BLOCKED | TAPE OK | 27.28 | 27.88 | 7 | +2.2% | +3.1 | OPEN |
| 2026-07-21 | HOMB | BLOCKED | TAPE OK | 30.42 | 31.16 | 7 | +2.4% | +3.3 | OPEN |
| 2026-07-21 | LQDA | BLOCKED | TAPE OK | 80.89 | 86.8 | 7 | +7.3% | +8.2 | OPEN |
| 2026-07-21 | NVRI | BLOCKED | TAPE OK | 21.87 | 22.21 | 7 | +1.6% | +2.4 | OPEN |
| 2026-07-21 | NWPX | BLOCKED | TAPE OK | 135.41 | 126.87 | 7 | -6.3% | -5.4 | OPEN |
| 2026-07-21 | OSCR | BLOCKED | TAPE OK | 30.77 | 31.23 | 7 | +1.5% | +2.4 | OPEN |
| 2026-07-21 | PNC | BLOCKED | TAPE OK | 250.38 | 248.71 | 7 | -0.7% | +0.2 | OPEN |
| 2026-07-21 | SION | BLOCKED | TAPE OK | 47.21 | 46.78 | 7 | -0.9% | -0.0 | OPEN |
| 2026-07-21 | TBLA | BLOCKED | TAPE OK | 5.11 | 5.1 | 7 | -0.2% | +0.7 | OPEN |
| 2026-07-21 | TFIN | BLOCKED | TAPE OK | 79.19 | 73.83 | 7 | -6.8% | -5.9 | OPEN |
| 2026-07-21 | TGTX | BLOCKED | TAPE OK | 53.95 | 53.53 | 7 | -0.8% | +0.1 | OPEN |
| 2026-07-21 | TVTX | BLOCKED | TAPE OK | 56.58 | 57.28 | 7 | +1.2% | +2.1 | OPEN |
| 2026-07-21 | VCYT | BLOCKED | TAPE OK | 59.53 | 59.78 | 7 | +0.4% | +1.3 | OPEN |
| 2026-07-21 | ZD | BLOCKED | TAPE OK | 52.39 | 52.61 | 7 | +0.4% | +1.3 | OPEN |
| 2026-07-21 | CYRX | PASSED | TAPE OK | 16.24 | 15.33 | 7 | -5.6% | -4.7 | OPEN |
| 2026-07-21 | FLEX | PASSED | TAPE OK | 127.39 | 111.91 | 7 | -12.2% | -11.3 | OPEN |
| 2026-07-21 | GDX | PASSED | TAPE OK | 74.19 | 76.78 | 7 | +3.5% | +4.4 | OPEN |
| 2026-07-21 | HON | PASSED | TAPE OK | 229.86 | 241.91 | 7 | +5.2% | +6.1 | OPEN |
| 2026-07-21 | KWEB | PASSED | TAPE OK | 27.02 | 28.06 | 7 | +3.9% | +4.7 | OPEN |
| 2026-07-21 | MSFT | PASSED | TAPE OK | 397.75 | 451.1 | 7 | +13.4% | +14.3 | OPEN |
| 2026-07-21 | MU | PASSED | TAPE OK | 970.82 | 874.66 | 7 | -9.9% | -9.0 | OPEN |
| 2026-07-21 | NKE | PASSED | TAPE OK | 42.96 | 42.29 | 7 | -1.6% | -0.7 | OPEN |
| 2026-07-21 | PM | PASSED | TAPE OK | 188.04 | 192.0 | 7 | +2.1% | +3.0 | OPEN |
| 2026-07-21 | SKYY | PASSED | TAPE OK | 136.02 | 140.03 | 7 | +3.0% | +3.8 | OPEN |
| 2026-07-21 | SNOW | PASSED | TAPE OK | 271.73 | 298.1 | 7 | +9.7% | +10.6 | OPEN |
| 2026-07-22 | ACTG | BLOCKED | REPAIR | 4.57 | 4.41 | 6 | -3.5% | -2.7 | OPEN |
| 2026-07-22 | AMCR | BLOCKED | PASS | 43.21 | 45.15 | 6 | +4.5% | +5.3 | OPEN |
| 2026-07-22 | AMGN | BLOCKED | PASS | 366.05 | 387.64 | 6 | +5.9% | +6.7 | OPEN |
| 2026-07-22 | ASB | BLOCKED | PASS | 30.7 | 30.76 | 6 | +0.2% | +1.0 | OPEN |
| 2026-07-22 | BCBP | BLOCKED | REPAIR | 10.29 | 10.21 | 6 | -0.8% | -0.0 | OPEN |
| 2026-07-22 | BHP | BLOCKED | REPAIR | 84.54 | 85.9 | 6 | +1.6% | +2.4 | OPEN |
| 2026-07-22 | BHRB | BLOCKED | PASS | 71.01 | 73.02 | 6 | +2.8% | +3.6 | OPEN |
| 2026-07-22 | BX | BLOCKED | REPAIR | 122.82 | 128.07 | 6 | +4.3% | +5.0 | OPEN |
| 2026-07-22 | BY | BLOCKED | PASS | 37.75 | 39.22 | 6 | +3.9% | +4.7 | OPEN |
| 2026-07-22 | CBSH | BLOCKED | PASS | 58.7 | 59.44 | 6 | +1.3% | +2.0 | OPEN |
| 2026-07-22 | CCJ | BLOCKED | DEEP-FAIL | 90.37 | 88.23 | 6 | -2.4% | -1.6 | OPEN |
| 2026-07-22 | CMP | BLOCKED | REPAIR | 30.14 | 29.78 | 6 | -1.2% | -0.4 | OPEN |
| 2026-07-22 | CNOB | BLOCKED | PASS | 33.0 | 32.95 | 6 | -0.1% | +0.6 | OPEN |
| 2026-07-22 | COKE | BLOCKED | PASS | 184.36 | 189.83 | 6 | +3.0% | +3.7 | OPEN |
| 2026-07-22 | COLB | BLOCKED | PASS | 32.63 | 31.25 | 6 | -4.2% | -3.5 | OPEN |
| 2026-07-22 | COST | BLOCKED | REPAIR | 927.31 | 954.17 | 6 | +2.9% | +3.7 | OPEN |
| 2026-07-22 | CRCL | BLOCKED | DEEP-FAIL | 66.16 | 64.24 | 6 | -2.9% | -2.1 | OPEN |
| 2026-07-22 | DE | BLOCKED | PASS | 607.33 | 599.47 | 6 | -1.3% | -0.5 | OPEN |
| 2026-07-22 | DELL | BLOCKED | PASS | 441.8 | 404.81 | 6 | -8.4% | -7.6 | OPEN |
| 2026-07-22 | DIS | BLOCKED | REPAIR | 95.87 | 96.16 | 6 | +0.3% | +1.1 | OPEN |
| 2026-07-22 | EQR | BLOCKED | PASS | 68.29 | 67.12 | 6 | -1.7% | -0.9 | OPEN |
| 2026-07-22 | F | BLOCKED | PASS | 14.42 | 14.86 | 6 | +3.0% | +3.8 | OPEN |
| 2026-07-22 | FCX | BLOCKED | PASS | 65.0 | 63.44 | 6 | -2.4% | -1.6 | OPEN |
| 2026-07-22 | FHB | BLOCKED | PASS | 28.81 | 27.92 | 6 | -3.1% | -2.3 | OPEN |
| 2026-07-22 | FITB | BLOCKED | PASS | 57.67 | 56.59 | 6 | -1.9% | -1.1 | OPEN |
| 2026-07-22 | FLEX | BLOCKED | REPAIR | 127.0 | 111.91 | 6 | -11.9% | -11.1 | OPEN |
| 2026-07-22 | FLG | BLOCKED | PASS | 14.88 | 14.25 | 6 | -4.2% | -3.5 | OPEN |
| 2026-07-22 | FNB | BLOCKED | PASS | 18.86 | 18.99 | 6 | +0.7% | +1.4 | OPEN |
| 2026-07-22 | FRT | BLOCKED | PASS | 125.05 | 124.09 | 6 | -0.8% | -0.0 | OPEN |
| 2026-07-22 | GBCI | BLOCKED | PASS | 51.17 | 48.97 | 6 | -4.3% | -3.5 | OPEN |
| 2026-07-22 | GDX | BLOCKED | DEEP-FAIL | 76.68 | 76.78 | 6 | +0.1% | +0.9 | OPEN |
| 2026-07-22 | GLD | BLOCKED | REPAIR | 379.12 | 377.16 | 6 | -0.5% | +0.2 | OPEN |
| 2026-07-22 | GM | BLOCKED | PASS | 82.13 | 88.4 | 6 | +7.6% | +8.4 | OPEN |
| 2026-07-22 | HBNC | BLOCKED | PASS | 20.21 | 20.58 | 6 | +1.8% | +2.6 | OPEN |
| 2026-07-22 | HON | BLOCKED | PASS | 232.99 | 241.91 | 6 | +3.8% | +4.6 | OPEN |
| 2026-07-22 | HOPE | BLOCKED | PASS | 13.54 | 14.03 | 6 | +3.6% | +4.4 | OPEN |
| 2026-07-22 | HSIC | BLOCKED | PASS | 84.81 | 85.17 | 6 | +0.4% | +1.2 | OPEN |
| 2026-07-22 | HTZ | BLOCKED | DEEP-FAIL | 1.93 | 1.65 | 6 | -14.2% | -13.5 | OPEN |
| 2026-07-22 | KRE | BLOCKED | PASS | 75.6 | 75.9 | 6 | +0.4% | +1.2 | OPEN |
| 2026-07-22 | LCID | BLOCKED | DEEP-FAIL | 6.78 | 8.12 | 6 | +19.8% | +20.5 | OPEN |
| 2026-07-22 | LZB | BLOCKED | PASS | 39.3 | 40.13 | 6 | +2.1% | +2.9 | OPEN |
| 2026-07-22 | M | BLOCKED | PASS | 24.33 | 24.93 | 6 | +2.5% | +3.2 | OPEN |
| 2026-07-22 | MFA | BLOCKED | REPAIR | 9.29 | 9.2 | 6 | -1.0% | -0.2 | OPEN |
| 2026-07-22 | MU | BLOCKED | PASS | 959.48 | 874.66 | 6 | -8.8% | -8.1 | OPEN |
| 2026-07-22 | NEE | BLOCKED | PASS | 89.41 | 87.93 | 6 | -1.7% | -0.9 | OPEN |
| 2026-07-22 | NEM | BLOCKED | REPAIR | 95.75 | 95.76 | 6 | +0.0% | +0.8 | OPEN |
| 2026-07-22 | OCFC | BLOCKED | PASS | 19.67 | 19.64 | 6 | -0.1% | +0.6 | OPEN |
| 2026-07-22 | PANW | BLOCKED | PASS | 335.28 | 325.68 | 6 | -2.9% | -2.1 | OPEN |
| 2026-07-22 | PB | BLOCKED | PASS | 73.06 | 74.82 | 6 | +2.4% | +3.2 | OPEN |
| 2026-07-22 | PM | BLOCKED | PASS | 194.3 | 192.0 | 6 | -1.2% | -0.4 | OPEN |
| 2026-07-22 | POWL | BLOCKED | REPAIR | 240.68 | 209.3 | 6 | -13.0% | -12.3 | OPEN |
| 2026-07-22 | PRLB | BLOCKED | PASS | 79.73 | 75.14 | 6 | -5.8% | -5.0 | OPEN |
| 2026-07-22 | RACE | BLOCKED | REPAIR | 371.61 | 397.73 | 6 | +7.0% | +7.8 | OPEN |
| 2026-07-22 | RCL | BLOCKED | REPAIR | 285.85 | 321.94 | 6 | +12.6% | +13.4 | OPEN |
| 2026-07-22 | RSPU | BLOCKED | PASS | 81.85 | 79.51 | 6 | -2.9% | -2.1 | OPEN |
| 2026-07-22 | SAIC | BLOCKED | PASS | 115.95 | 115.72 | 6 | -0.2% | +0.6 | OPEN |
| 2026-07-22 | SJM | BLOCKED | PASS | 118.05 | 122.21 | 6 | +3.5% | +4.3 | OPEN |
| 2026-07-22 | SKK | BLOCKED | PASS | 5.22 | 4.65 | 6 | -10.9% | -10.2 | OPEN |
| 2026-07-22 | SMCI | BLOCKED | REPAIR | 30.56 | 27.73 | 6 | -9.3% | -8.5 | OPEN |
| 2026-07-22 | SON | BLOCKED | PASS | 55.15 | 56.82 | 6 | +3.0% | +3.8 | OPEN |
| 2026-07-22 | SPG | BLOCKED | PASS | 226.22 | 230.44 | 6 | +1.9% | +2.6 | OPEN |
| 2026-07-22 | SSB | BLOCKED | PASS | 102.19 | 105.26 | 6 | +3.0% | +3.8 | OPEN |
| 2026-07-22 | STRL | BLOCKED | REPAIR | 719.34 | 580.73 | 6 | -19.3% | -18.5 | OPEN |
| 2026-07-22 | STX | BLOCKED | PASS | 908.1 | 851.68 | 6 | -6.2% | -5.5 | OPEN |
| 2026-07-22 | TDY | BLOCKED | PASS | 650.5 | 649.18 | 6 | -0.2% | +0.6 | OPEN |
| 2026-07-22 | TPL | BLOCKED | PASS | 433.1 | 394.25 | 6 | -9.0% | -8.2 | OPEN |
| 2026-07-22 | TPR | BLOCKED | PASS | 143.73 | 152.58 | 6 | +6.2% | +6.9 | OPEN |
| 2026-07-22 | URA | BLOCKED | DEEP-FAIL | 40.97 | 39.72 | 6 | -3.0% | -2.3 | OPEN |
| 2026-07-22 | USB | BLOCKED | PASS | 64.47 | 62.9 | 6 | -2.4% | -1.7 | OPEN |
| 2026-07-22 | VST | BLOCKED | REPAIR | 166.74 | 148.62 | 6 | -10.9% | -10.1 | OPEN |
| 2026-07-22 | VVV | BLOCKED | PASS | 39.03 | 38.39 | 6 | -1.6% | -0.9 | OPEN |
| 2026-07-22 | CTRE | PASSED | PASS | 42.38 | 41.64 | 6 | -1.8% | -1.0 | OPEN |
| 2026-07-22 | PFE | PASSED | REPAIR | 24.82 | 24.91 | 6 | +0.4% | +1.1 | OPEN |
| 2026-07-22 | TJX | PASSED | REPAIR | 155.41 | 159.26 | 6 | +2.5% | +3.2 | OPEN |
| 2026-07-22 | TXNM | PASSED | REPAIR | 58.3 | 57.97 | 6 | -0.6% | +0.2 | OPEN |
| 2026-07-22 | VZ | PASSED | REPAIR | 44.29 | 46.11 | 6 | +4.1% | +4.9 | OPEN |
| 2026-07-23 | ACTG | BLOCKED | REPAIR | 4.62 | 4.41 | 5 | -4.5% | -5.0 | OPEN |
| 2026-07-23 | ALSN | BLOCKED | PASS | 119.64 | 115.44 | 5 | -3.5% | -4.0 | OPEN |
| 2026-07-23 | AVT | BLOCKED | PASS | 89.92 | 86.8 | 5 | -3.5% | -4.0 | OPEN |
| 2026-07-23 | BUD | BLOCKED | REPAIR | 80.48 | 86.14 | 5 | +7.0% | +6.6 | OPEN |
| 2026-07-23 | COST | BLOCKED | REPAIR | 926.06 | 954.17 | 5 | +3.0% | +2.6 | OPEN |
| 2026-07-23 | CRCL | BLOCKED | DEEP-FAIL | 62.18 | 64.24 | 5 | +3.3% | +2.8 | OPEN |
| 2026-07-23 | DELL | BLOCKED | PASS | 439.34 | 404.81 | 5 | -7.9% | -8.3 | OPEN |
| 2026-07-23 | DGX | BLOCKED | PASS | 227.9 | 234.3 | 5 | +2.8% | +2.3 | OPEN |
| 2026-07-23 | F | BLOCKED | REPAIR | 14.15 | 14.86 | 5 | +5.0% | +4.5 | OPEN |
| 2026-07-23 | FCX | BLOCKED | REPAIR | 63.5 | 63.44 | 5 | -0.1% | -0.6 | OPEN |
| 2026-07-23 | FLG | BLOCKED | PASS | 14.71 | 14.25 | 5 | -3.1% | -3.6 | OPEN |
| 2026-07-23 | FNB | BLOCKED | PASS | 18.87 | 18.99 | 5 | +0.6% | +0.2 | OPEN |
| 2026-07-23 | FUTU | BLOCKED | DEEP-FAIL | 98.96 | 103.42 | 5 | +4.5% | +4.0 | OPEN |
| 2026-07-23 | GDX | BLOCKED | DEEP-FAIL | 75.02 | 76.78 | 5 | +2.4% | +1.9 | OPEN |
| 2026-07-23 | GLD | BLOCKED | REPAIR | 371.52 | 377.16 | 5 | +1.5% | +1.0 | OPEN |
| 2026-07-23 | GM | BLOCKED | PASS | 80.67 | 88.4 | 5 | +9.6% | +9.1 | OPEN |
| 2026-07-23 | HON | BLOCKED | PASS | 246.27 | 241.91 | 5 | -1.8% | -2.2 | OPEN |
| 2026-07-23 | IRM | BLOCKED | REPAIR | 124.55 | 124.64 | 5 | +0.1% | -0.4 | OPEN |
| 2026-07-23 | LCID | BLOCKED | DEEP-FAIL | 6.45 | 8.12 | 5 | +25.9% | +25.4 | OPEN |
| 2026-07-23 | LSTR | BLOCKED | PASS | 207.97 | 169.34 | 5 | -18.6% | -19.1 | OPEN |
| 2026-07-23 | M | BLOCKED | PASS | 23.33 | 24.93 | 5 | +6.9% | +6.4 | OPEN |
| 2026-07-23 | MAC | BLOCKED | PASS | 25.3 | 25.47 | 5 | +0.7% | +0.2 | OPEN |
| 2026-07-23 | NEM | BLOCKED | REPAIR | 94.72 | 95.76 | 5 | +1.1% | +0.6 | OPEN |
| 2026-07-23 | PLD | BLOCKED | PASS | 145.12 | 146.19 | 5 | +0.7% | +0.3 | OPEN |
| 2026-07-23 | PRLB | BLOCKED | PASS | 78.62 | 75.14 | 5 | -4.4% | -4.9 | OPEN |
| 2026-07-23 | RHP | BLOCKED | PASS | 128.89 | 133.25 | 5 | +3.4% | +2.9 | OPEN |
| 2026-07-23 | SMCI | BLOCKED | REPAIR | 31.2 | 27.73 | 5 | -11.1% | -11.6 | OPEN |
| 2026-07-23 | SON | BLOCKED | PASS | 56.32 | 56.82 | 5 | +0.9% | +0.4 | OPEN |
| 2026-07-23 | SPG | BLOCKED | PASS | 225.2 | 230.44 | 5 | +2.3% | +1.9 | OPEN |
| 2026-07-23 | TDY | BLOCKED | PASS | 651.22 | 649.18 | 5 | -0.3% | -0.8 | OPEN |
| 2026-07-23 | URA | BLOCKED | DEEP-FAIL | 41.13 | 39.72 | 5 | -3.4% | -3.9 | OPEN |
| 2026-07-23 | URI | BLOCKED | PASS | 1139.71 | 1068.63 | 5 | -6.2% | -6.7 | OPEN |
| 2026-07-23 | VST | BLOCKED | REPAIR | 168.98 | 148.62 | 5 | -12.1% | -12.5 | OPEN |
| 2026-07-23 | VVV | BLOCKED | PASS | 38.31 | 38.39 | 5 | +0.2% | -0.3 | OPEN |
| 2026-07-23 | ECVT | PASSED | PASS | 12.89 | 12.09 | 5 | -6.2% | -6.7 | OPEN |
| 2026-07-23 | FRT | PASSED | PASS | 124.83 | 124.09 | 5 | -0.6% | -1.1 | OPEN |
| 2026-07-23 | HAS | PASSED | PASS | 87.35 | 94.53 | 5 | +8.2% | +7.7 | OPEN |
| 2026-07-23 | LHX | PASSED | REPAIR | 299.67 | 271.9 | 5 | -9.3% | -9.7 | OPEN |
| 2026-07-23 | MLI | PASSED | REPAIR | 63.13 | 66.86 | 5 | +5.9% | +5.4 | OPEN |
| 2026-07-23 | PFE | PASSED | REPAIR | 25.01 | 24.91 | 5 | -0.4% | -0.9 | OPEN |
| 2026-07-23 | SJM | PASSED | PASS | 115.71 | 122.21 | 5 | +5.6% | +5.1 | OPEN |
| 2026-07-23 | VZ | PASSED | REPAIR | 43.82 | 46.11 | 5 | +5.2% | +4.8 | OPEN |
| 2026-07-24 | ALSN | BLOCKED | PASS | 122.34 | 115.44 | 4 | -5.6% | -6.0 | OPEN |
| 2026-07-24 | AVT | BLOCKED | PASS | 89.42 | 86.8 | 4 | -2.9% | -3.3 | OPEN |
| 2026-07-24 | BUD | BLOCKED | REPAIR | 81.66 | 86.14 | 4 | +5.5% | +5.1 | OPEN |
| 2026-07-24 | CB | BLOCKED | PASS | 359.75 | 350.15 | 4 | -2.7% | -3.0 | OPEN |
| 2026-07-24 | CNP | BLOCKED | PASS | 44.56 | 42.15 | 4 | -5.4% | -5.8 | OPEN |
| 2026-07-24 | COST | BLOCKED | REPAIR | 935.03 | 954.17 | 4 | +2.0% | +1.7 | OPEN |
| 2026-07-24 | CRCL | BLOCKED | DEEP-FAIL | 62.36 | 64.24 | 4 | +3.0% | +2.6 | OPEN |
| 2026-07-24 | DE | BLOCKED | PASS | 628.16 | 599.47 | 4 | -4.6% | -4.9 | OPEN |
| 2026-07-24 | DGX | BLOCKED | PASS | 227.86 | 234.3 | 4 | +2.8% | +2.5 | OPEN |
| 2026-07-24 | DLR | BLOCKED | PASS | 199.08 | 193.19 | 4 | -3.0% | -3.3 | OPEN |
| 2026-07-24 | EGBN | BLOCKED | PASS | 28.44 | 27.49 | 4 | -3.3% | -3.7 | OPEN |
| 2026-07-24 | F | BLOCKED | REPAIR | 14.37 | 14.86 | 4 | +3.4% | +3.0 | OPEN |
| 2026-07-24 | FCX | BLOCKED | REPAIR | 62.6 | 63.44 | 4 | +1.3% | +1.0 | OPEN |
| 2026-07-24 | FUTU | BLOCKED | DEEP-FAIL | 99.36 | 103.42 | 4 | +4.1% | +3.7 | OPEN |
| 2026-07-24 | GDX | BLOCKED | DEEP-FAIL | 75.23 | 76.78 | 4 | +2.1% | +1.7 | OPEN |
| 2026-07-24 | GE | BLOCKED | PASS | 353.73 | 355.04 | 4 | +0.4% | -0.0 | OPEN |
| 2026-07-24 | GLD | BLOCKED | REPAIR | 371.9 | 377.16 | 4 | +1.4% | +1.0 | OPEN |
| 2026-07-24 | GM | BLOCKED | PASS | 82.64 | 88.4 | 4 | +7.0% | +6.6 | OPEN |
| 2026-07-24 | HON | BLOCKED | PASS | 243.15 | 241.91 | 4 | -0.5% | -0.9 | OPEN |
| 2026-07-24 | IRM | BLOCKED | PASS | 128.31 | 124.64 | 4 | -2.9% | -3.2 | OPEN |
| 2026-07-24 | JNJ | BLOCKED | PASS | 263.4 | 255.82 | 4 | -2.9% | -3.2 | OPEN |
| 2026-07-24 | LCID | BLOCKED | DEEP-FAIL | 6.3 | 8.12 | 4 | +28.9% | +28.5 | OPEN |
| 2026-07-24 | LDOS | BLOCKED | DEEP-FAIL | 112.14 | 112.41 | 4 | +0.2% | -0.1 | OPEN |
| 2026-07-24 | LIND | BLOCKED | PASS | 26.85 | 29.79 | 4 | +10.9% | +10.6 | OPEN |
| 2026-07-24 | M | BLOCKED | PASS | 23.38 | 24.93 | 4 | +6.6% | +6.3 | OPEN |
| 2026-07-24 | NEM | BLOCKED | REPAIR | 93.19 | 95.76 | 4 | +2.8% | +2.4 | OPEN |
| 2026-07-24 | ORKA | BLOCKED | PASS | 92.16 | 97.86 | 4 | +6.2% | +5.8 | OPEN |
| 2026-07-24 | PH | BLOCKED | PASS | 987.54 | 962.79 | 4 | -2.5% | -2.9 | OPEN |
| 2026-07-24 | PRLB | BLOCKED | PASS | 78.24 | 75.14 | 4 | -4.0% | -4.3 | OPEN |
| 2026-07-24 | ROP | BLOCKED | REPAIR | 367.34 | 389.25 | 4 | +6.0% | +5.6 | OPEN |
| 2026-07-24 | RSPU | BLOCKED | PASS | 82.33 | 79.51 | 4 | -3.4% | -3.8 | OPEN |
| 2026-07-24 | SMCI | BLOCKED | REPAIR | 30.1 | 27.73 | 4 | -7.9% | -8.2 | OPEN |
| 2026-07-24 | SON | BLOCKED | PASS | 58.23 | 56.82 | 4 | -2.4% | -2.8 | OPEN |
| 2026-07-24 | SPG | BLOCKED | PASS | 229.78 | 230.44 | 4 | +0.3% | -0.1 | OPEN |
| 2026-07-24 | TDY | BLOCKED | PASS | 655.35 | 649.18 | 4 | -0.9% | -1.3 | OPEN |
| 2026-07-24 | URA | BLOCKED | DEEP-FAIL | 39.89 | 39.72 | 4 | -0.4% | -0.8 | OPEN |
| 2026-07-24 | URI | BLOCKED | PASS | 1141.59 | 1068.63 | 4 | -6.4% | -6.8 | OPEN |
| 2026-07-24 | VST | BLOCKED | REPAIR | 163.38 | 148.62 | 4 | -9.0% | -9.4 | OPEN |
| 2026-07-24 | XLI | BLOCKED | PASS | 182.66 | 178.39 | 4 | -2.3% | -2.7 | OPEN |
| 2026-07-24 | ACTG | PASSED | PASS | 4.66 | 4.41 | 4 | -5.4% | -5.7 | OPEN |
| 2026-07-24 | DELL | PASSED | PASS | 437.5 | 404.81 | 4 | -7.5% | -7.8 | OPEN |
| 2026-07-24 | EQIX | PASSED | PASS | 1084.24 | 1047.53 | 4 | -3.4% | -3.8 | OPEN |
| 2026-07-24 | LHX | PASSED | REPAIR | 300.21 | 271.9 | 4 | -9.4% | -9.8 | OPEN |
| 2026-07-24 | MLI | PASSED | REPAIR | 63.91 | 66.86 | 4 | +4.6% | +4.2 | OPEN |
| 2026-07-24 | MRK | PASSED | PASS | 131.07 | 129.79 | 4 | -1.0% | -1.4 | OPEN |
| 2026-07-24 | RHP | PASSED | PASS | 133.09 | 133.25 | 4 | +0.1% | -0.2 | OPEN |
| 2026-07-24 | SJM | PASSED | PASS | 118.32 | 122.21 | 4 | +3.3% | +2.9 | OPEN |
| 2026-07-24 | VZ | PASSED | REPAIR | 46.38 | 46.11 | 4 | -0.6% | -1.0 | OPEN |
| 2026-07-27 | ACGL | BLOCKED | PASS | 103.88 | 101.14 | 3 | -2.6% | -3.0 | OPEN |
| 2026-07-27 | ALSN | BLOCKED | PASS | 121.91 | 115.44 | 3 | -5.3% | -5.7 | OPEN |
| 2026-07-27 | AVT | BLOCKED | PASS | 88.38 | 86.8 | 3 | -1.8% | -2.1 | OPEN |
| 2026-07-27 | BUD | BLOCKED | REPAIR | 80.87 | 86.14 | 3 | +6.5% | +6.2 | OPEN |
| 2026-07-27 | CB | BLOCKED | PASS | 358.91 | 350.15 | 3 | -2.4% | -2.8 | OPEN |
| 2026-07-27 | CPRT | BLOCKED | DEEP-FAIL | 29.79 | 29.57 | 3 | -0.8% | -1.1 | OPEN |
| 2026-07-27 | CRCL | BLOCKED | DEEP-FAIL | 65.67 | 64.24 | 3 | -2.2% | -2.5 | OPEN |
| 2026-07-27 | DE | BLOCKED | PASS | 625.02 | 599.47 | 3 | -4.1% | -4.4 | OPEN |
| 2026-07-27 | DLR | BLOCKED | PASS | 195.76 | 193.19 | 3 | -1.3% | -1.7 | OPEN |
| 2026-07-27 | EGBN | BLOCKED | PASS | 28.15 | 27.49 | 3 | -2.3% | -2.7 | OPEN |
| 2026-07-27 | F | BLOCKED | PASS | 14.68 | 14.86 | 3 | +1.2% | +0.9 | OPEN |
| 2026-07-27 | FCX | BLOCKED | REPAIR | 62.72 | 63.44 | 3 | +1.1% | +0.8 | OPEN |
| 2026-07-27 | FUTU | BLOCKED | DEEP-FAIL | 104.27 | 103.42 | 3 | -0.8% | -1.2 | OPEN |
| 2026-07-27 | GDX | BLOCKED | DEEP-FAIL | 75.73 | 76.78 | 3 | +1.4% | +1.0 | OPEN |
| 2026-07-27 | GLD | BLOCKED | REPAIR | 374.63 | 377.16 | 3 | +0.7% | +0.3 | OPEN |
| 2026-07-27 | GM | BLOCKED | PASS | 87.04 | 88.4 | 3 | +1.6% | +1.2 | OPEN |
| 2026-07-27 | HON | BLOCKED | PASS | 245.75 | 241.91 | 3 | -1.6% | -1.9 | OPEN |
| 2026-07-27 | IRM | BLOCKED | PASS | 126.99 | 124.64 | 3 | -1.9% | -2.2 | OPEN |
| 2026-07-27 | LDOS | BLOCKED | DEEP-FAIL | 114.95 | 112.41 | 3 | -2.2% | -2.6 | OPEN |
| 2026-07-27 | LIND | BLOCKED | PASS | 28.09 | 29.79 | 3 | +6.0% | +5.7 | OPEN |
| 2026-07-27 | MAR | BLOCKED | PASS | 383.06 | 375.48 | 3 | -2.0% | -2.3 | OPEN |
| 2026-07-27 | NEM | BLOCKED | REPAIR | 93.47 | 95.76 | 3 | +2.5% | +2.1 | OPEN |
| 2026-07-27 | ORKA | BLOCKED | PASS | 90.2 | 97.86 | 3 | +8.5% | +8.1 | OPEN |
| 2026-07-27 | PGR | BLOCKED | REPAIR | 215.76 | 213.28 | 3 | -1.1% | -1.5 | OPEN |
| 2026-07-27 | PH | BLOCKED | PASS | 987.31 | 962.79 | 3 | -2.5% | -2.8 | OPEN |
| 2026-07-27 | PRLB | BLOCKED | PASS | 77.64 | 75.14 | 3 | -3.2% | -3.6 | OPEN |
| 2026-07-27 | RCL | BLOCKED | REPAIR | 305.04 | 321.94 | 3 | +5.5% | +5.2 | OPEN |
| 2026-07-27 | ROP | BLOCKED | REPAIR | 375.02 | 389.25 | 3 | +3.8% | +3.4 | OPEN |
| 2026-07-27 | RSPU | BLOCKED | PASS | 81.24 | 79.51 | 3 | -2.1% | -2.5 | OPEN |
| 2026-07-27 | SLB | BLOCKED | PASS | 51.53 | 48.91 | 3 | -5.1% | -5.4 | OPEN |
| 2026-07-27 | SMCI | BLOCKED | DEEP-FAIL | 29.81 | 27.73 | 3 | -7.0% | -7.3 | OPEN |
| 2026-07-27 | SON | BLOCKED | PASS | 58.68 | 56.82 | 3 | -3.2% | -3.5 | OPEN |
| 2026-07-27 | TDY | BLOCKED | PASS | 651.65 | 649.18 | 3 | -0.4% | -0.7 | OPEN |
| 2026-07-27 | TJX | BLOCKED | REPAIR | 156.38 | 159.26 | 3 | +1.8% | +1.5 | OPEN |
| 2026-07-27 | URA | BLOCKED | DEEP-FAIL | 40.32 | 39.72 | 3 | -1.5% | -1.8 | OPEN |
| 2026-07-27 | VRSN | BLOCKED | REPAIR | 274.82 | 286.58 | 3 | +4.3% | +3.9 | OPEN |
| 2026-07-27 | VST | BLOCKED | REPAIR | 157.08 | 148.62 | 3 | -5.4% | -5.7 | OPEN |
| 2026-07-27 | WWD | BLOCKED | PASS | 419.76 | 356.28 | 3 | -15.1% | -15.5 | OPEN |
| 2026-07-27 | XLI | BLOCKED | PASS | 183.2 | 178.39 | 3 | -2.6% | -3.0 | OPEN |
| 2026-07-27 | ACTG | PASSED | PASS | 4.63 | 4.41 | 3 | -4.8% | -5.1 | OPEN |
| 2026-07-27 | DELL | PASSED | PASS | 426.91 | 404.81 | 3 | -5.2% | -5.5 | OPEN |
| 2026-07-27 | DGX | PASSED | PASS | 231.84 | 234.3 | 3 | +1.1% | +0.7 | OPEN |
| 2026-07-27 | EQIX | PASSED | PASS | 1046.79 | 1047.53 | 3 | +0.1% | -0.3 | OPEN |
| 2026-07-27 | GE | PASSED | PASS | 361.61 | 355.04 | 3 | -1.8% | -2.2 | OPEN |
| 2026-07-27 | JNJ | PASSED | PASS | 265.95 | 255.82 | 3 | -3.8% | -4.2 | OPEN |
| 2026-07-27 | LHX | PASSED | REPAIR | 303.48 | 271.9 | 3 | -10.4% | -10.8 | OPEN |
| 2026-07-27 | MLI | PASSED | PASS | 64.17 | 66.86 | 3 | +4.2% | +3.8 | OPEN |
| 2026-07-27 | MRK | PASSED | PASS | 130.76 | 129.79 | 3 | -0.7% | -1.1 | OPEN |
| 2026-07-27 | RHP | PASSED | PASS | 134.94 | 133.25 | 3 | -1.2% | -1.6 | OPEN |
| 2026-07-27 | SJM | PASSED | PASS | 121.05 | 122.21 | 3 | +1.0% | +0.6 | OPEN |
| 2026-07-27 | URI | PASSED | PASS | 1127.91 | 1068.63 | 3 | -5.3% | -5.6 | OPEN |
| 2026-07-28 | ACGL | BLOCKED | PASS | 106.48 | 101.14 | 2 | -5.0% | -5.1 | OPEN |
| 2026-07-28 | AGNC | BLOCKED | PASS | 11.07 | 10.92 | 2 | -1.4% | -1.5 | OPEN |
| 2026-07-28 | AI | BLOCKED | DEEP-FAIL | 8.9 | 9.07 | 2 | +1.9% | +1.8 | OPEN |
| 2026-07-28 | AJG | BLOCKED | REPAIR | 265.31 | 256.46 | 2 | -3.3% | -3.5 | OPEN |
| 2026-07-28 | ALSN | BLOCKED | PASS | 121.11 | 115.44 | 2 | -4.7% | -4.8 | OPEN |
| 2026-07-28 | AVT | BLOCKED | REPAIR | 86.22 | 86.8 | 2 | +0.7% | +0.6 | OPEN |
| 2026-07-28 | AXON | BLOCKED | REPAIR | 547.65 | 525.3 | 2 | -4.1% | -4.2 | OPEN |
| 2026-07-28 | BUD | BLOCKED | PASS | 83.2 | 86.14 | 2 | +3.5% | +3.4 | OPEN |
| 2026-07-28 | CB | BLOCKED | PASS | 363.5 | 350.15 | 2 | -3.7% | -3.8 | OPEN |
| 2026-07-28 | CCL | BLOCKED | REPAIR | 28.23 | 27.77 | 2 | -1.6% | -1.7 | OPEN |
| 2026-07-28 | CHTR | BLOCKED | DEEP-FAIL | 139.97 | 142.0 | 2 | +1.4% | +1.3 | OPEN |
| 2026-07-28 | CLX | BLOCKED | REPAIR | 100.32 | 96.73 | 2 | -3.6% | -3.7 | OPEN |
| 2026-07-28 | CNP | BLOCKED | PASS | 44.1 | 42.15 | 2 | -4.4% | -4.5 | OPEN |
| 2026-07-28 | COKE | BLOCKED | PASS | 195.0 | 189.83 | 2 | -2.6% | -2.8 | OPEN |
| 2026-07-28 | CPRT | BLOCKED | DEEP-FAIL | 30.69 | 29.57 | 2 | -3.7% | -3.8 | OPEN |
| 2026-07-28 | CRCL | BLOCKED | DEEP-FAIL | 64.32 | 64.24 | 2 | -0.1% | -0.2 | OPEN |
| 2026-07-28 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.71 | 2 | +0.6% | +0.5 | OPEN |
| 2026-07-28 | DASH | BLOCKED | REPAIR | 195.52 | 197.53 | 2 | +1.0% | +0.9 | OPEN |
| 2026-07-28 | DUOL | BLOCKED | REPAIR | 140.73 | 133.6 | 2 | -5.1% | -5.2 | OPEN |
| 2026-07-28 | EGBN | BLOCKED | PASS | 28.39 | 27.49 | 2 | -3.2% | -3.3 | OPEN |
| 2026-07-28 | ERIE | BLOCKED | REPAIR | 242.43 | 233.67 | 2 | -3.6% | -3.7 | OPEN |
| 2026-07-28 | F | BLOCKED | PASS | 14.96 | 14.86 | 2 | -0.7% | -0.8 | OPEN |
| 2026-07-28 | FCX | BLOCKED | REPAIR | 61.64 | 63.44 | 2 | +2.9% | +2.8 | OPEN |
| 2026-07-28 | FUTU | BLOCKED | DEEP-FAIL | 101.84 | 103.42 | 2 | +1.6% | +1.4 | OPEN |
| 2026-07-28 | GDX | BLOCKED | DEEP-FAIL | 74.21 | 76.78 | 2 | +3.5% | +3.4 | OPEN |
| 2026-07-28 | GLD | BLOCKED | DEEP-FAIL | 369.37 | 377.16 | 2 | +2.1% | +2.0 | OPEN |
| 2026-07-28 | GM | BLOCKED | PASS | 90.3 | 88.4 | 2 | -2.1% | -2.2 | OPEN |
| 2026-07-28 | HD | BLOCKED | REPAIR | 344.47 | 333.35 | 2 | -3.2% | -3.3 | OPEN |
| 2026-07-28 | JETS | BLOCKED | PASS | 31.86 | 31.68 | 2 | -0.6% | -0.7 | OPEN |
| 2026-07-28 | LDOS | BLOCKED | DEEP-FAIL | 118.36 | 112.41 | 2 | -5.0% | -5.1 | OPEN |
| 2026-07-28 | LOW | BLOCKED | REPAIR | 218.24 | 210.08 | 2 | -3.7% | -3.9 | OPEN |
| 2026-07-28 | LZB | BLOCKED | PASS | 41.3 | 40.13 | 2 | -2.8% | -2.9 | OPEN |
| 2026-07-28 | MAR | BLOCKED | PASS | 383.52 | 375.48 | 2 | -2.1% | -2.2 | OPEN |
| 2026-07-28 | MCD | BLOCKED | REPAIR | 273.02 | 268.44 | 2 | -1.7% | -1.8 | OPEN |
| 2026-07-28 | MDT | BLOCKED | REPAIR | 86.88 | 85.71 | 2 | -1.4% | -1.5 | OPEN |
| 2026-07-28 | NCLH | BLOCKED | REPAIR | 21.22 | 18.72 | 2 | -11.8% | -11.9 | OPEN |
| 2026-07-28 | NEM | BLOCKED | DEEP-FAIL | 91.52 | 95.76 | 2 | +4.6% | +4.5 | OPEN |
| 2026-07-28 | NFLX | BLOCKED | DEEP-FAIL | 72.39 | 73.17 | 2 | +1.1% | +1.0 | OPEN |
| 2026-07-28 | NOW | BLOCKED | DEEP-FAIL | 110.62 | 110.07 | 2 | -0.5% | -0.6 | OPEN |
| 2026-07-28 | PGR | BLOCKED | REPAIR | 219.52 | 213.28 | 2 | -2.8% | -3.0 | OPEN |
| 2026-07-28 | PH | BLOCKED | PASS | 990.96 | 962.79 | 2 | -2.8% | -3.0 | OPEN |
| 2026-07-28 | RACE | BLOCKED | REPAIR | 390.14 | 397.73 | 2 | +1.9% | +1.8 | OPEN |
| 2026-07-28 | RCL | BLOCKED | REPAIR | 322.5 | 321.94 | 2 | -0.2% | -0.3 | OPEN |
| 2026-07-28 | RMD | BLOCKED | DEEP-FAIL | 208.96 | 208.56 | 2 | -0.2% | -0.3 | OPEN |
| 2026-07-28 | ROP | BLOCKED | REPAIR | 390.92 | 389.25 | 2 | -0.4% | -0.5 | OPEN |
| 2026-07-28 | RSPU | BLOCKED | PASS | 81.03 | 79.51 | 2 | -1.9% | -2.0 | OPEN |
| 2026-07-28 | SHAK | BLOCKED | DEEP-FAIL | 63.2 | 63.07 | 2 | -0.2% | -0.3 | OPEN |
| 2026-07-28 | SHW | BLOCKED | REPAIR | 354.27 | 344.84 | 2 | -2.7% | -2.8 | OPEN |
| 2026-07-28 | SMCI | BLOCKED | DEEP-FAIL | 28.45 | 27.73 | 2 | -2.5% | -2.6 | OPEN |
| 2026-07-28 | SON | BLOCKED | PASS | 60.56 | 56.82 | 2 | -6.2% | -6.3 | OPEN |
| 2026-07-28 | STGW | BLOCKED | PASS | 7.97 | 8.49 | 2 | +6.5% | +6.4 | OPEN |
| 2026-07-28 | TDY | BLOCKED | PASS | 649.67 | 649.18 | 2 | -0.1% | -0.2 | OPEN |
| 2026-07-28 | TOST | BLOCKED | REPAIR | 32.34 | 32.85 | 2 | +1.6% | +1.5 | OPEN |
| 2026-07-28 | TPR | BLOCKED | PASS | 150.9 | 152.58 | 2 | +1.1% | +1.0 | OPEN |
| 2026-07-28 | TYL | BLOCKED | DEEP-FAIL | 333.35 | 323.31 | 2 | -3.0% | -3.1 | OPEN |
| 2026-07-28 | URA | BLOCKED | DEEP-FAIL | 38.95 | 39.72 | 2 | +2.0% | +1.9 | OPEN |
| 2026-07-28 | URI | BLOCKED | PASS | 1091.26 | 1068.63 | 2 | -2.1% | -2.2 | OPEN |
| 2026-07-28 | VRSN | BLOCKED | REPAIR | 281.15 | 286.58 | 2 | +1.9% | +1.8 | OPEN |
| 2026-07-28 | WWD | BLOCKED | PASS | 410.55 | 356.28 | 2 | -13.2% | -13.3 | OPEN |
| 2026-07-28 | XLI | BLOCKED | PASS | 182.49 | 178.39 | 2 | -2.2% | -2.4 | OPEN |
| 2026-07-28 | ZTS | BLOCKED | DEEP-FAIL | 77.51 | 76.03 | 2 | -1.9% | -2.0 | OPEN |
| 2026-07-28 | ACTG | PASSED | PASS | 4.63 | 4.41 | 2 | -4.8% | -4.9 | OPEN |
| 2026-07-28 | CTS | PASSED | PASS | 64.82 | 62.7 | 2 | -3.3% | -3.4 | OPEN |
| 2026-07-28 | DAL | PASSED | PASS | 89.37 | 88.59 | 2 | -0.9% | -1.0 | OPEN |
| 2026-07-28 | DE | PASSED | PASS | 639.84 | 599.47 | 2 | -6.3% | -6.4 | OPEN |
| 2026-07-28 | DGX | PASSED | PASS | 235.94 | 234.3 | 2 | -0.7% | -0.8 | OPEN |
| 2026-07-28 | DLR | PASSED | PASS | 193.18 | 193.19 | 2 | +0.0% | -0.1 | OPEN |
| 2026-07-28 | EQIX | PASSED | REPAIR | 1034.86 | 1047.53 | 2 | +1.2% | +1.1 | OPEN |
| 2026-07-28 | GE | PASSED | PASS | 363.59 | 355.04 | 2 | -2.4% | -2.5 | OPEN |
| 2026-07-28 | HON | PASSED | PASS | 247.05 | 241.91 | 2 | -2.1% | -2.2 | OPEN |
| 2026-07-28 | JNJ | PASSED | PASS | 266.73 | 255.82 | 2 | -4.1% | -4.2 | OPEN |
| 2026-07-28 | LHX | PASSED | REPAIR | 305.2 | 271.9 | 2 | -10.9% | -11.0 | OPEN |
| 2026-07-28 | LLY | PASSED | PASS | 1220.66 | 1154.97 | 2 | -5.4% | -5.5 | OPEN |
| 2026-07-28 | MLI | PASSED | PASS | 66.49 | 66.86 | 2 | +0.6% | +0.4 | OPEN |
| 2026-07-28 | MNST | PASSED | PASS | 97.74 | 97.65 | 2 | -0.1% | -0.2 | OPEN |
| 2026-07-28 | MRK | PASSED | PASS | 131.82 | 129.79 | 2 | -1.5% | -1.6 | OPEN |
| 2026-07-28 | PEP | PASSED | REPAIR | 142.86 | 140.2 | 2 | -1.9% | -2.0 | OPEN |
| 2026-07-28 | SLB | PASSED | REPAIR | 49.98 | 48.91 | 2 | -2.1% | -2.2 | OPEN |
| 2026-07-28 | SSD | PASSED | PASS | 198.28 | 186.67 | 2 | -5.9% | -6.0 | OPEN |
| 2026-07-28 | TJX | PASSED | PASS | 160.8 | 159.26 | 2 | -1.0% | -1.1 | OPEN |
| 2026-07-29 | ABNB | BLOCKED | PASS | 153.01 | 152.08 | 1 | -0.6% | -2.3 | OPEN |
| 2026-07-29 | ACGL | BLOCKED | PASS | 104.55 | 101.14 | 1 | -3.3% | -4.9 | OPEN |
| 2026-07-29 | AGNC | BLOCKED | PASS | 10.9 | 10.92 | 1 | +0.2% | -1.5 | OPEN |
| 2026-07-29 | AI | BLOCKED | DEEP-FAIL | 8.85 | 9.07 | 1 | +2.5% | +0.8 | OPEN |
| 2026-07-29 | AJG | BLOCKED | REPAIR | 268.91 | 256.46 | 1 | -4.6% | -6.3 | OPEN |
| 2026-07-29 | AXON | BLOCKED | REPAIR | 531.2 | 525.3 | 1 | -1.1% | -2.8 | OPEN |
| 2026-07-29 | BFC | BLOCKED | PASS | 151.78 | 151.29 | 1 | -0.3% | -2.0 | OPEN |
| 2026-07-29 | CB | BLOCKED | PASS | 361.9 | 350.15 | 1 | -3.2% | -4.9 | OPEN |
| 2026-07-29 | CHTR | BLOCKED | DEEP-FAIL | 145.2 | 142.0 | 1 | -2.2% | -3.9 | OPEN |
| 2026-07-29 | CLX | BLOCKED | REPAIR | 99.63 | 96.73 | 1 | -2.9% | -4.6 | OPEN |
| 2026-07-29 | CMG | BLOCKED | REPAIR | 34.24 | 38.52 | 1 | +12.5% | +10.8 | OPEN |
| 2026-07-29 | CNP | BLOCKED | PASS | 42.93 | 42.15 | 1 | -1.8% | -3.5 | OPEN |
| 2026-07-29 | COKE | BLOCKED | PASS | 192.39 | 189.83 | 1 | -1.3% | -3.0 | OPEN |
| 2026-07-29 | CPRT | BLOCKED | DEEP-FAIL | 30.82 | 29.57 | 1 | -4.1% | -5.8 | OPEN |
| 2026-07-29 | CTM | BLOCKED | DEEP-FAIL | 0.66 | 0.71 | 1 | +7.3% | +5.6 | OPEN |
| 2026-07-29 | DASH | BLOCKED | REPAIR | 193.53 | 197.53 | 1 | +2.1% | +0.4 | OPEN |
| 2026-07-29 | DE | BLOCKED | PASS | 610.95 | 599.47 | 1 | -1.9% | -3.6 | OPEN |
| 2026-07-29 | DUOL | BLOCKED | REPAIR | 140.17 | 133.6 | 1 | -4.7% | -6.4 | OPEN |
| 2026-07-29 | EGBN | BLOCKED | PASS | 27.89 | 27.49 | 1 | -1.4% | -3.1 | OPEN |
| 2026-07-29 | EQIX | BLOCKED | REPAIR | 1008.02 | 1047.53 | 1 | +3.9% | +2.2 | OPEN |
| 2026-07-29 | ERIE | BLOCKED | REPAIR | 248.55 | 233.67 | 1 | -6.0% | -7.7 | OPEN |
| 2026-07-29 | ESQ | BLOCKED | PASS | 131.89 | 129.62 | 1 | -1.7% | -3.4 | OPEN |
| 2026-07-29 | FCX | BLOCKED | REPAIR | 59.99 | 63.44 | 1 | +5.8% | +4.1 | OPEN |
| 2026-07-29 | GDX | BLOCKED | DEEP-FAIL | 73.57 | 76.78 | 1 | +4.4% | +2.7 | OPEN |
| 2026-07-29 | GME | BLOCKED | REPAIR | 21.84 | 21.88 | 1 | +0.2% | -1.5 | OPEN |
| 2026-07-29 | GRND | BLOCKED | PASS | 17.21 | 16.95 | 1 | -1.5% | -3.2 | OPEN |
| 2026-07-29 | HD | BLOCKED | REPAIR | 338.27 | 333.35 | 1 | -1.4% | -3.1 | OPEN |
| 2026-07-29 | IBM | BLOCKED | DEEP-FAIL | 226.44 | 221.74 | 1 | -2.1% | -3.8 | OPEN |
| 2026-07-29 | JBLU | BLOCKED | PASS | 5.72 | 6.07 | 1 | +6.1% | +4.4 | OPEN |
| 2026-07-29 | JETS | BLOCKED | PASS | 30.97 | 31.68 | 1 | +2.3% | +0.6 | OPEN |
| 2026-07-29 | KWEB | BLOCKED | DEEP-FAIL | 27.8 | 28.06 | 1 | +0.9% | -0.7 | OPEN |
| 2026-07-29 | LDOS | BLOCKED | DEEP-FAIL | 114.37 | 112.41 | 1 | -1.7% | -3.4 | OPEN |
| 2026-07-29 | LOW | BLOCKED | REPAIR | 215.68 | 210.08 | 1 | -2.6% | -4.3 | OPEN |
| 2026-07-29 | LZB | BLOCKED | PASS | 40.93 | 40.13 | 1 | -1.9% | -3.6 | OPEN |
| 2026-07-29 | MAR | BLOCKED | PASS | 381.12 | 375.48 | 1 | -1.5% | -3.2 | OPEN |
| 2026-07-29 | MCD | BLOCKED | REPAIR | 271.52 | 268.44 | 1 | -1.1% | -2.8 | OPEN |
| 2026-07-29 | NCLH | BLOCKED | REPAIR | 20.75 | 18.72 | 1 | -9.8% | -11.5 | OPEN |
| 2026-07-29 | NEM | BLOCKED | DEEP-FAIL | 91.34 | 95.76 | 1 | +4.8% | +3.2 | OPEN |
| 2026-07-29 | NEO | BLOCKED | PASS | 15.27 | 15.88 | 1 | +4.0% | +2.3 | OPEN |
| 2026-07-29 | NFLX | BLOCKED | DEEP-FAIL | 73.63 | 73.17 | 1 | -0.6% | -2.3 | OPEN |
| 2026-07-29 | NIO | BLOCKED | DEEP-FAIL | 4.76 | 4.84 | 1 | +1.7% | +0.0 | OPEN |
| 2026-07-29 | NOW | BLOCKED | REPAIR | 115.76 | 110.07 | 1 | -4.9% | -6.6 | OPEN |
| 2026-07-29 | NVST | BLOCKED | PASS | 28.37 | 27.78 | 1 | -2.1% | -3.8 | OPEN |
| 2026-07-29 | PGR | BLOCKED | REPAIR | 219.99 | 213.28 | 1 | -3.0% | -4.7 | OPEN |
| 2026-07-29 | PH | BLOCKED | PASS | 951.07 | 962.79 | 1 | +1.2% | -0.4 | OPEN |
| 2026-07-29 | RCL | BLOCKED | REPAIR | 323.58 | 321.94 | 1 | -0.5% | -2.2 | OPEN |
| 2026-07-29 | RMD | BLOCKED | REPAIR | 214.29 | 208.56 | 1 | -2.7% | -4.3 | OPEN |
| 2026-07-29 | ROKU | BLOCKED | PASS | 145.33 | 145.09 | 1 | -0.2% | -1.8 | OPEN |
| 2026-07-29 | ROP | BLOCKED | REPAIR | 408.07 | 389.25 | 1 | -4.6% | -6.3 | OPEN |
| 2026-07-29 | RSPU | BLOCKED | PASS | 79.85 | 79.51 | 1 | -0.4% | -2.1 | OPEN |
| 2026-07-29 | SHAK | BLOCKED | DEEP-FAIL | 63.05 | 63.07 | 1 | +0.0% | -1.6 | OPEN |
| 2026-07-29 | SHW | BLOCKED | REPAIR | 343.88 | 344.84 | 1 | +0.3% | -1.4 | OPEN |
| 2026-07-29 | SKYY | BLOCKED | PASS | 138.56 | 140.03 | 1 | +1.1% | -0.6 | OPEN |
| 2026-07-29 | SMCI | BLOCKED | DEEP-FAIL | 25.7 | 27.73 | 1 | +7.9% | +6.2 | OPEN |
| 2026-07-29 | STGW | BLOCKED | PASS | 8.08 | 8.49 | 1 | +5.1% | +3.4 | OPEN |
| 2026-07-29 | TDY | BLOCKED | PASS | 631.35 | 649.18 | 1 | +2.8% | +1.1 | OPEN |
| 2026-07-29 | TOST | BLOCKED | REPAIR | 32.6 | 32.85 | 1 | +0.8% | -0.9 | OPEN |
| 2026-07-29 | TPR | BLOCKED | PASS | 150.11 | 152.58 | 1 | +1.6% | -0.0 | OPEN |
| 2026-07-29 | TYL | BLOCKED | DEEP-FAIL | 333.5 | 323.31 | 1 | -3.1% | -4.7 | OPEN |
| 2026-07-29 | URI | BLOCKED | PASS | 1055.11 | 1068.63 | 1 | +1.3% | -0.4 | OPEN |
| 2026-07-29 | VRSN | BLOCKED | REPAIR | 290.92 | 286.58 | 1 | -1.5% | -3.2 | OPEN |
| 2026-07-29 | WWD | BLOCKED | PASS | 385.42 | 356.28 | 1 | -7.6% | -9.2 | OPEN |
| 2026-07-29 | ZTS | BLOCKED | DEEP-FAIL | 77.93 | 76.03 | 1 | -2.4% | -4.1 | OPEN |
| 2026-07-29 | CCL | PASSED | REPAIR | 27.81 | 27.77 | 1 | -0.1% | -1.8 | OPEN |
| 2026-07-29 | CPT | PASSED | PASS | 116.37 | 113.29 | 1 | -2.6% | -4.3 | OPEN |
| 2026-07-29 | CTS | PASSED | PASS | 61.53 | 62.7 | 1 | +1.9% | +0.2 | OPEN |
| 2026-07-29 | DAL | PASSED | PASS | 86.25 | 88.59 | 1 | +2.7% | +1.0 | OPEN |
| 2026-07-29 | DGX | PASSED | PASS | 235.22 | 234.3 | 1 | -0.4% | -2.1 | OPEN |
| 2026-07-29 | DLR | PASSED | PASS | 188.18 | 193.19 | 1 | +2.7% | +1.0 | OPEN |
| 2026-07-29 | GE | PASSED | PASS | 350.63 | 355.04 | 1 | +1.3% | -0.4 | OPEN |
| 2026-07-29 | HON | PASSED | PASS | 241.12 | 241.91 | 1 | +0.3% | -1.4 | OPEN |
| 2026-07-29 | JNJ | PASSED | PASS | 265.53 | 255.82 | 1 | -3.7% | -5.3 | OPEN |
| 2026-07-29 | KDP | PASSED | PASS | 31.45 | 31.57 | 1 | +0.4% | -1.3 | OPEN |
| 2026-07-29 | LHX | PASSED | REPAIR | 297.53 | 271.9 | 1 | -8.6% | -10.3 | OPEN |
| 2026-07-29 | LLY | PASSED | PASS | 1210.02 | 1154.97 | 1 | -4.5% | -6.2 | OPEN |
| 2026-07-29 | MDT | PASSED | REPAIR | 87.54 | 85.71 | 1 | -2.1% | -3.8 | OPEN |
| 2026-07-29 | MNST | PASSED | PASS | 97.23 | 97.65 | 1 | +0.4% | -1.2 | OPEN |
| 2026-07-29 | MRK | PASSED | PASS | 130.36 | 129.79 | 1 | -0.4% | -2.1 | OPEN |
| 2026-07-29 | PEP | PASSED | REPAIR | 143.5 | 140.2 | 1 | -2.3% | -4.0 | OPEN |
| 2026-07-29 | RACE | PASSED | REPAIR | 385.69 | 397.73 | 1 | +3.1% | +1.4 | OPEN |
| 2026-07-29 | SLB | PASSED | REPAIR | 48.96 | 48.91 | 1 | -0.1% | -1.8 | OPEN |
| 2026-07-29 | SSD | PASSED | REPAIR | 189.48 | 186.67 | 1 | -1.5% | -3.2 | OPEN |
| 2026-07-29 | TJX | PASSED | PASS | 161.63 | 159.26 | 1 | -1.5% | -3.1 | OPEN |

Open marks are not results. This file exists so that the cull the scan performs every night is measured instead of assumed.
