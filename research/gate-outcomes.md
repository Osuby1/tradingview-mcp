# Gate stack forward grade

Does THE GATE STACK earn its keep? Every fresh Chandelier signal is graded forward from the CLOSE of its signal date over 21 trading sessions, bucketed by what the stack decided. The number that matters is the SPREAD.

- Signal events found: 894  |  priced: 788  |  unique symbol-cohort pairs (headline sample): 319
- Skipped (pre-2026-07-22 hand-written verdicts, not machine-comparable): 20

## Headline - all signals, deduped to first appearance

| Cohort | n | Win% | Mean | Median | Mean vs SPY | Mean worst drawdown |
|---|---|---|---|---|---|---|
| PASSED | 71 | 51% | +1.56% | +0.04% | -1.33% | -4.72% |
| BLOCKED | 248 | 58% | +1.19% | +0.93% | -1.72% | -5.83% |

**Spread (PASSED minus BLOCKED): +0.37 percentage points.**

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
| ADX FLOOR | 75 | 64% | +2.13% | +1.90% | -0.89% |
| ATR GEOMETRY | 13 | 69% | +3.51% | +1.29% | -0.02% |
| DIRECTION | 19 | 53% | -2.17% | +0.46% | -4.69% |
| LIQUIDITY | 1 | 0% | -9.33% | -9.33% | -12.32% |
| OTHER | 30 | 33% | -2.80% | -1.81% | -6.05% |
| REGIME | 34 | 59% | +2.53% | +1.62% | -0.03% |
| VOLATILITY CAP (ex 2:1) | 19 | 68% | +2.19% | +1.16% | +0.81% |
| ZLSMA | 57 | 60% | +1.71% | +0.92% | -1.58% |

## Shadow cohorts - the forbidden retro-tune, run forward instead

Would lowering the ADX floor to 18, or softening DEEP-FAIL, have helped? The replay's missed monsters make that tempting; answering it by re-running history is curve-fitting. These cohorts answer it FORWARD: sole-failure near-misses graded nightly against the PASSED cohort. Promotion bar (pre-registered): >=30 MATURED signals AND mean above PASSED's - then it goes to a Friday review, not before.

| Shadow cohort | n | Win% | Mean | Median | Mean vs SPY | PASSED mean (ref) |
|---|---|---|---|---|---|---|
| ADX 18-20, all else passed | 11 | 64% | +0.35% | +0.78% | -2.61% | +1.56% |
| DEEP-FAIL, all else passed | 2 | 50% | +5.08% | +5.08% | +0.91% | +1.56% |

## Every graded signal

| Date | Sym | Cohort | Regime | Entry | Mark | Days | Return | vs SPY | Status |
|---|---|---|---|---|---|---|---|---|---|
| 2026-07-20 | BG | BLOCKED | n/a | 120.49 | 106.62 | 12 | -11.5% | -15.2 | OPEN |
| 2026-07-20 | CHRD | BLOCKED | n/a | 128.8 | 129.95 | 12 | +0.9% | -2.8 | OPEN |
| 2026-07-20 | CNOB | BLOCKED | n/a | 33.46 | 33.42 | 12 | -0.1% | -3.9 | OPEN |
| 2026-07-20 | COCO | BLOCKED | PASS | 73.87 | 64.84 | 12 | -12.2% | -16.0 | OPEN |
| 2026-07-20 | CVNA | BLOCKED | DEEP-FAIL | 64.14 | 69.48 | 12 | +8.3% | +4.6 | OPEN |
| 2026-07-20 | FLG | BLOCKED | n/a | 14.84 | 14.3 | 12 | -3.6% | -7.4 | OPEN |
| 2026-07-20 | FNB | BLOCKED | n/a | 18.75 | 19.21 | 12 | +2.5% | -1.3 | OPEN |
| 2026-07-20 | HAS | BLOCKED | REPAIR | 81.59 | 91.16 | 12 | +11.7% | +8.0 | OPEN |
| 2026-07-20 | HLX | BLOCKED | n/a | 9.43 | 9.32 | 12 | -1.2% | -4.9 | OPEN |
| 2026-07-20 | LCID | BLOCKED | n/a | 7.11 | 6.7 | 12 | -5.8% | -9.5 | OPEN |
| 2026-07-20 | M | BLOCKED | REPAIR | 23.31 | 25.51 | 12 | +9.4% | +5.7 | OPEN |
| 2026-07-20 | NOV | BLOCKED | REPAIR | 19.55 | 19.5 | 12 | -0.3% | -4.0 | OPEN |
| 2026-07-20 | ODFL | BLOCKED | PASS | 231.76 | 215.45 | 12 | -7.0% | -10.8 | OPEN |
| 2026-07-20 | RYZ | BLOCKED | n/a | 29.07 | 27.64 | 12 | -4.9% | -8.7 | OPEN |
| 2026-07-20 | SHAK | BLOCKED | DEEP-FAIL | 56.97 | 74.33 | 12 | +30.5% | +26.7 | OPEN |
| 2026-07-20 | SPG | BLOCKED | PASS | 228.19 | 224.81 | 12 | -1.5% | -5.2 | OPEN |
| 2026-07-20 | TRNS | BLOCKED | n/a | 86.09 | 93.75 | 12 | +8.9% | +5.2 | OPEN |
| 2026-07-20 | VVV | BLOCKED | PASS | 39.54 | 36.98 | 12 | -6.5% | -10.2 | OPEN |
| 2026-07-20 | VZ | BLOCKED | REPAIR | 43.5 | 46.47 | 12 | +6.8% | +3.1 | OPEN |
| 2026-07-20 | WPC | BLOCKED | REPAIR | 75.17 | 72.18 | 12 | -4.0% | -7.7 | OPEN |
| 2026-07-21 | ALKS | BLOCKED | TAPE OK | 52.85 | 49.61 | 11 | -6.1% | -9.0 | OPEN |
| 2026-07-21 | ATLC | BLOCKED | TAPE OK | 96.37 | 111.31 | 11 | +15.5% | +12.6 | OPEN |
| 2026-07-21 | BRKR | BLOCKED | TAPE OK | 60.43 | 52.47 | 11 | -13.2% | -16.1 | OPEN |
| 2026-07-21 | CB | BLOCKED | TAPE OK | 354.8 | 352.54 | 11 | -0.6% | -3.5 | OPEN |
| 2026-07-21 | CBL | BLOCKED | TAPE OK | 55.53 | 56.67 | 11 | +2.0% | -0.8 | OPEN |
| 2026-07-21 | CNOB | BLOCKED | TAPE OK | 33.41 | 33.42 | 11 | +0.0% | -2.8 | OPEN |
| 2026-07-21 | COCO | BLOCKED | TAPE OK | 75.89 | 64.84 | 11 | -14.6% | -17.4 | OPEN |
| 2026-07-21 | CTRE | BLOCKED | TAPE OK | 43.4 | 41.14 | 11 | -5.2% | -8.1 | OPEN |
| 2026-07-21 | ESQ | BLOCKED | TAPE OK | 122.83 | 132.2 | 11 | +7.6% | +4.8 | OPEN |
| 2026-07-21 | EXTR | BLOCKED | TAPE OK | 30.44 | 26.19 | 11 | -14.0% | -16.8 | OPEN |
| 2026-07-21 | FFIV | BLOCKED | TAPE OK | 408.74 | 411.32 | 11 | +0.6% | -2.2 | OPEN |
| 2026-07-21 | FRT | BLOCKED | TAPE OK | 125.59 | 121.83 | 11 | -3.0% | -5.9 | OPEN |
| 2026-07-21 | HCSG | BLOCKED | TAPE OK | 24.8 | 22.84 | 11 | -7.9% | -10.8 | OPEN |
| 2026-07-21 | HELE | BLOCKED | TAPE OK | 27.28 | 29.56 | 11 | +8.4% | +5.5 | OPEN |
| 2026-07-21 | HOMB | BLOCKED | TAPE OK | 30.42 | 31.21 | 11 | +2.6% | -0.3 | OPEN |
| 2026-07-21 | LQDA | BLOCKED | TAPE OK | 80.89 | 89.12 | 11 | +10.2% | +7.3 | OPEN |
| 2026-07-21 | NVRI | BLOCKED | TAPE OK | 21.87 | 23.01 | 11 | +5.2% | +2.3 | OPEN |
| 2026-07-21 | NWPX | BLOCKED | TAPE OK | 135.41 | 124.24 | 11 | -8.2% | -11.1 | OPEN |
| 2026-07-21 | OSCR | BLOCKED | TAPE OK | 30.77 | 30.11 | 11 | -2.1% | -5.0 | OPEN |
| 2026-07-21 | PNC | BLOCKED | TAPE OK | 250.38 | 255.37 | 11 | +2.0% | -0.9 | OPEN |
| 2026-07-21 | SION | BLOCKED | TAPE OK | 47.21 | 47.34 | 11 | +0.3% | -2.6 | OPEN |
| 2026-07-21 | TBLA | BLOCKED | TAPE OK | 5.11 | 3.84 | 11 | -24.9% | -27.8 | OPEN |
| 2026-07-21 | TFIN | BLOCKED | TAPE OK | 79.19 | 78.11 | 11 | -1.4% | -4.2 | OPEN |
| 2026-07-21 | TGTX | BLOCKED | TAPE OK | 53.95 | 49.88 | 11 | -7.5% | -10.4 | OPEN |
| 2026-07-21 | TVTX | BLOCKED | TAPE OK | 56.58 | 62.76 | 11 | +10.9% | +8.1 | OPEN |
| 2026-07-21 | VCYT | BLOCKED | TAPE OK | 59.53 | 46.15 | 11 | -22.5% | -25.4 | OPEN |
| 2026-07-21 | ZD | BLOCKED | TAPE OK | 52.39 | 52.72 | 11 | +0.6% | -2.2 | OPEN |
| 2026-07-21 | CYRX | PASSED | TAPE OK | 16.24 | 15.25 | 11 | -6.1% | -9.0 | OPEN |
| 2026-07-21 | FLEX | PASSED | TAPE OK | 127.39 | 121.88 | 11 | -4.3% | -7.2 | OPEN |
| 2026-07-21 | GDX | PASSED | TAPE OK | 74.19 | 83.68 | 11 | +12.8% | +9.9 | OPEN |
| 2026-07-21 | HON | PASSED | TAPE OK | 229.86 | 248.12 | 11 | +7.9% | +5.1 | OPEN |
| 2026-07-21 | KWEB | PASSED | TAPE OK | 27.02 | 28.54 | 11 | +5.6% | +2.8 | OPEN |
| 2026-07-21 | MSFT | PASSED | TAPE OK | 397.75 | 487.46 | 11 | +22.6% | +19.7 | OPEN |
| 2026-07-21 | MU | PASSED | TAPE OK | 970.82 | 893.19 | 11 | -8.0% | -10.9 | OPEN |
| 2026-07-21 | NKE | PASSED | TAPE OK | 42.96 | 42.45 | 11 | -1.2% | -4.1 | OPEN |
| 2026-07-21 | PM | PASSED | TAPE OK | 188.04 | 188.93 | 11 | +0.5% | -2.4 | OPEN |
| 2026-07-21 | SKYY | PASSED | TAPE OK | 136.02 | 153.48 | 11 | +12.8% | +10.0 | OPEN |
| 2026-07-21 | SNOW | PASSED | TAPE OK | 271.73 | 316.84 | 11 | +16.6% | +13.7 | OPEN |
| 2026-07-22 | ACTG | BLOCKED | REPAIR | 4.57 | 4.54 | 10 | -0.7% | -3.6 | OPEN |
| 2026-07-22 | AMCR | BLOCKED | PASS | 43.21 | 47.75 | 10 | +10.5% | +7.5 | OPEN |
| 2026-07-22 | AMGN | BLOCKED | PASS | 366.05 | 407.83 | 10 | +11.4% | +8.4 | OPEN |
| 2026-07-22 | ASB | BLOCKED | PASS | 30.7 | 31.53 | 10 | +2.7% | -0.3 | OPEN |
| 2026-07-22 | BCBP | BLOCKED | REPAIR | 10.29 | 8.76 | 10 | -14.9% | -17.9 | OPEN |
| 2026-07-22 | BHP | BLOCKED | REPAIR | 84.54 | 89.38 | 10 | +5.7% | +2.7 | OPEN |
| 2026-07-22 | BHRB | BLOCKED | PASS | 71.01 | 74.12 | 10 | +4.4% | +1.4 | OPEN |
| 2026-07-22 | BX | BLOCKED | REPAIR | 122.82 | 136.03 | 10 | +10.8% | +7.8 | OPEN |
| 2026-07-22 | BY | BLOCKED | PASS | 37.75 | 39.52 | 10 | +4.7% | +1.7 | OPEN |
| 2026-07-22 | CBSH | BLOCKED | PASS | 58.7 | 59.66 | 10 | +1.6% | -1.4 | OPEN |
| 2026-07-22 | CCJ | BLOCKED | DEEP-FAIL | 90.37 | 94.27 | 10 | +4.3% | +1.3 | OPEN |
| 2026-07-22 | CMP | BLOCKED | REPAIR | 30.14 | 30.03 | 10 | -0.4% | -3.4 | OPEN |
| 2026-07-22 | CNOB | BLOCKED | PASS | 33.0 | 33.42 | 10 | +1.3% | -1.7 | OPEN |
| 2026-07-22 | COKE | BLOCKED | PASS | 184.36 | 184.74 | 10 | +0.2% | -2.8 | OPEN |
| 2026-07-22 | COLB | BLOCKED | PASS | 32.63 | 31.35 | 10 | -3.9% | -6.9 | OPEN |
| 2026-07-22 | COST | BLOCKED | REPAIR | 927.31 | 941.99 | 10 | +1.6% | -1.4 | OPEN |
| 2026-07-22 | CRCL | BLOCKED | DEEP-FAIL | 66.16 | 63.28 | 10 | -4.3% | -7.3 | OPEN |
| 2026-07-22 | DE | BLOCKED | PASS | 607.33 | 612.0 | 10 | +0.8% | -2.2 | OPEN |
| 2026-07-22 | DELL | BLOCKED | PASS | 441.8 | 462.7 | 10 | +4.7% | +1.7 | OPEN |
| 2026-07-22 | DIS | BLOCKED | REPAIR | 95.87 | 101.76 | 10 | +6.1% | +3.1 | OPEN |
| 2026-07-22 | EQR | BLOCKED | PASS | 68.29 | 67.74 | 10 | -0.8% | -3.8 | OPEN |
| 2026-07-22 | F | BLOCKED | PASS | 14.42 | 14.13 | 10 | -2.0% | -5.0 | OPEN |
| 2026-07-22 | FCX | BLOCKED | PASS | 65.0 | 69.39 | 10 | +6.8% | +3.8 | OPEN |
| 2026-07-22 | FHB | BLOCKED | PASS | 28.81 | 27.77 | 10 | -3.6% | -6.6 | OPEN |
| 2026-07-22 | FITB | BLOCKED | PASS | 57.67 | 57.6 | 10 | -0.1% | -3.1 | OPEN |
| 2026-07-22 | FLEX | BLOCKED | REPAIR | 127.0 | 121.88 | 10 | -4.0% | -7.0 | OPEN |
| 2026-07-22 | FLG | BLOCKED | PASS | 14.88 | 14.3 | 10 | -3.9% | -6.9 | OPEN |
| 2026-07-22 | FNB | BLOCKED | PASS | 18.86 | 19.21 | 10 | +1.9% | -1.1 | OPEN |
| 2026-07-22 | FRT | BLOCKED | PASS | 125.05 | 121.83 | 10 | -2.6% | -5.6 | OPEN |
| 2026-07-22 | GBCI | BLOCKED | PASS | 51.17 | 50.0 | 10 | -2.3% | -5.3 | OPEN |
| 2026-07-22 | GDX | BLOCKED | DEEP-FAIL | 76.68 | 83.68 | 10 | +9.1% | +6.1 | OPEN |
| 2026-07-22 | GLD | BLOCKED | REPAIR | 379.12 | 389.64 | 10 | +2.8% | -0.2 | OPEN |
| 2026-07-22 | GM | BLOCKED | PASS | 82.13 | 89.16 | 10 | +8.6% | +5.6 | OPEN |
| 2026-07-22 | HBNC | BLOCKED | PASS | 20.21 | 20.65 | 10 | +2.2% | -0.8 | OPEN |
| 2026-07-22 | HON | BLOCKED | PASS | 232.99 | 248.12 | 10 | +6.5% | +3.5 | OPEN |
| 2026-07-22 | HOPE | BLOCKED | PASS | 13.54 | 14.27 | 10 | +5.4% | +2.4 | OPEN |
| 2026-07-22 | HSIC | BLOCKED | PASS | 84.81 | 89.59 | 10 | +5.6% | +2.6 | OPEN |
| 2026-07-22 | HTZ | BLOCKED | DEEP-FAIL | 1.93 | 1.56 | 10 | -19.2% | -22.2 | OPEN |
| 2026-07-22 | KRE | BLOCKED | PASS | 75.6 | 77.34 | 10 | +2.3% | -0.7 | OPEN |
| 2026-07-22 | LCID | BLOCKED | DEEP-FAIL | 6.78 | 6.7 | 10 | -1.2% | -4.2 | OPEN |
| 2026-07-22 | LZB | BLOCKED | PASS | 39.3 | 41.45 | 10 | +5.5% | +2.5 | OPEN |
| 2026-07-22 | M | BLOCKED | PASS | 24.33 | 25.51 | 10 | +4.8% | +1.9 | OPEN |
| 2026-07-22 | MFA | BLOCKED | REPAIR | 9.29 | 9.06 | 10 | -2.5% | -5.5 | OPEN |
| 2026-07-22 | MU | BLOCKED | PASS | 959.48 | 893.19 | 10 | -6.9% | -9.9 | OPEN |
| 2026-07-22 | NEE | BLOCKED | PASS | 89.41 | 85.91 | 10 | -3.9% | -6.9 | OPEN |
| 2026-07-22 | NEM | BLOCKED | REPAIR | 95.75 | 104.29 | 10 | +8.9% | +5.9 | OPEN |
| 2026-07-22 | OCFC | BLOCKED | PASS | 19.67 | 19.87 | 10 | +1.0% | -2.0 | OPEN |
| 2026-07-22 | PANW | BLOCKED | PASS | 335.28 | 362.66 | 10 | +8.2% | +5.2 | OPEN |
| 2026-07-22 | PB | BLOCKED | PASS | 73.06 | 74.62 | 10 | +2.1% | -0.9 | OPEN |
| 2026-07-22 | PM | BLOCKED | PASS | 194.3 | 188.93 | 10 | -2.8% | -5.8 | OPEN |
| 2026-07-22 | POWL | BLOCKED | REPAIR | 240.68 | 208.33 | 10 | -13.4% | -16.4 | OPEN |
| 2026-07-22 | PRLB | BLOCKED | PASS | 79.73 | 90.31 | 10 | +13.3% | +10.3 | OPEN |
| 2026-07-22 | RACE | BLOCKED | REPAIR | 371.61 | 406.8 | 10 | +9.5% | +6.5 | OPEN |
| 2026-07-22 | RCL | BLOCKED | REPAIR | 285.85 | 327.42 | 10 | +14.5% | +11.6 | OPEN |
| 2026-07-22 | RSPU | BLOCKED | PASS | 81.85 | 77.56 | 10 | -5.2% | -8.2 | OPEN |
| 2026-07-22 | SAIC | BLOCKED | PASS | 115.95 | 120.3 | 10 | +3.8% | +0.8 | OPEN |
| 2026-07-22 | SJM | BLOCKED | PASS | 118.05 | 119.21 | 10 | +1.0% | -2.0 | OPEN |
| 2026-07-22 | SKK | BLOCKED | PASS | 5.22 | 4.73 | 10 | -9.3% | -12.3 | OPEN |
| 2026-07-22 | SMCI | BLOCKED | REPAIR | 30.56 | 30.32 | 10 | -0.8% | -3.8 | OPEN |
| 2026-07-22 | SON | BLOCKED | PASS | 55.15 | 58.46 | 10 | +6.0% | +3.0 | OPEN |
| 2026-07-22 | SPG | BLOCKED | PASS | 226.22 | 224.81 | 10 | -0.6% | -3.6 | OPEN |
| 2026-07-22 | SSB | BLOCKED | PASS | 102.19 | 109.19 | 10 | +6.8% | +3.9 | OPEN |
| 2026-07-22 | STRL | BLOCKED | REPAIR | 719.34 | 536.03 | 10 | -25.5% | -28.5 | OPEN |
| 2026-07-22 | STX | BLOCKED | PASS | 908.1 | 837.66 | 10 | -7.8% | -10.8 | OPEN |
| 2026-07-22 | TDY | BLOCKED | PASS | 650.5 | 683.73 | 10 | +5.1% | +2.1 | OPEN |
| 2026-07-22 | TPL | BLOCKED | PASS | 433.1 | 381.88 | 10 | -11.8% | -14.8 | OPEN |
| 2026-07-22 | TPR | BLOCKED | PASS | 143.73 | 159.16 | 10 | +10.7% | +7.7 | OPEN |
| 2026-07-22 | URA | BLOCKED | DEEP-FAIL | 40.97 | 42.89 | 10 | +4.7% | +1.7 | OPEN |
| 2026-07-22 | USB | BLOCKED | PASS | 64.47 | 64.21 | 10 | -0.4% | -3.4 | OPEN |
| 2026-07-22 | VST | BLOCKED | REPAIR | 166.74 | 140.58 | 10 | -15.7% | -18.7 | OPEN |
| 2026-07-22 | VVV | BLOCKED | PASS | 39.03 | 36.98 | 10 | -5.2% | -8.2 | OPEN |
| 2026-07-22 | CTRE | PASSED | PASS | 42.38 | 41.14 | 10 | -2.9% | -5.9 | OPEN |
| 2026-07-22 | PFE | PASSED | REPAIR | 24.82 | 25.81 | 10 | +4.0% | +1.0 | OPEN |
| 2026-07-22 | TJX | PASSED | REPAIR | 155.41 | 159.92 | 10 | +2.9% | -0.1 | OPEN |
| 2026-07-22 | TXNM | PASSED | REPAIR | 58.3 | 57.36 | 10 | -1.6% | -4.6 | OPEN |
| 2026-07-22 | VZ | PASSED | REPAIR | 44.29 | 46.47 | 10 | +4.9% | +1.9 | OPEN |
| 2026-07-23 | ACTG | BLOCKED | REPAIR | 4.62 | 4.54 | 9 | -1.7% | -6.0 | OPEN |
| 2026-07-23 | ALSN | BLOCKED | PASS | 119.64 | 118.13 | 9 | -1.3% | -5.5 | OPEN |
| 2026-07-23 | AVT | BLOCKED | PASS | 89.92 | 97.22 | 9 | +8.1% | +3.8 | OPEN |
| 2026-07-23 | BUD | BLOCKED | REPAIR | 80.48 | 85.18 | 9 | +5.8% | +1.6 | OPEN |
| 2026-07-23 | COST | BLOCKED | REPAIR | 926.06 | 941.99 | 9 | +1.7% | -2.6 | OPEN |
| 2026-07-23 | CRCL | BLOCKED | DEEP-FAIL | 62.18 | 63.28 | 9 | +1.8% | -2.5 | OPEN |
| 2026-07-23 | DELL | BLOCKED | PASS | 439.34 | 462.7 | 9 | +5.3% | +1.0 | OPEN |
| 2026-07-23 | DGX | BLOCKED | PASS | 227.9 | 235.84 | 9 | +3.5% | -0.8 | OPEN |
| 2026-07-23 | F | BLOCKED | REPAIR | 14.15 | 14.13 | 9 | -0.1% | -4.4 | OPEN |
| 2026-07-23 | FCX | BLOCKED | REPAIR | 63.5 | 69.39 | 9 | +9.3% | +5.0 | OPEN |
| 2026-07-23 | FLG | BLOCKED | PASS | 14.71 | 14.3 | 9 | -2.8% | -7.1 | OPEN |
| 2026-07-23 | FNB | BLOCKED | PASS | 18.87 | 19.21 | 9 | +1.8% | -2.5 | OPEN |
| 2026-07-23 | FUTU | BLOCKED | DEEP-FAIL | 98.96 | 110.22 | 9 | +11.4% | +7.1 | OPEN |
| 2026-07-23 | GDX | BLOCKED | DEEP-FAIL | 75.02 | 83.68 | 9 | +11.5% | +7.3 | OPEN |
| 2026-07-23 | GLD | BLOCKED | REPAIR | 371.52 | 389.64 | 9 | +4.9% | +0.6 | OPEN |
| 2026-07-23 | GM | BLOCKED | PASS | 80.67 | 89.16 | 9 | +10.5% | +6.2 | OPEN |
| 2026-07-23 | HON | BLOCKED | PASS | 246.27 | 248.12 | 9 | +0.8% | -3.5 | OPEN |
| 2026-07-23 | IRM | BLOCKED | REPAIR | 124.55 | 127.13 | 9 | +2.1% | -2.2 | OPEN |
| 2026-07-23 | LCID | BLOCKED | DEEP-FAIL | 6.45 | 6.7 | 9 | +3.9% | -0.4 | OPEN |
| 2026-07-23 | LSTR | BLOCKED | PASS | 207.97 | 179.35 | 9 | -13.8% | -18.0 | OPEN |
| 2026-07-23 | M | BLOCKED | PASS | 23.33 | 25.51 | 9 | +9.3% | +5.1 | OPEN |
| 2026-07-23 | MAC | BLOCKED | PASS | 25.3 | 25.39 | 9 | +0.4% | -3.9 | OPEN |
| 2026-07-23 | NEM | BLOCKED | REPAIR | 94.72 | 104.29 | 9 | +10.1% | +5.8 | OPEN |
| 2026-07-23 | PLD | BLOCKED | PASS | 145.12 | 140.76 | 9 | -3.0% | -7.3 | OPEN |
| 2026-07-23 | PRLB | BLOCKED | PASS | 78.62 | 90.31 | 9 | +14.9% | +10.6 | OPEN |
| 2026-07-23 | RHP | BLOCKED | PASS | 128.89 | 127.62 | 9 | -1.0% | -5.3 | OPEN |
| 2026-07-23 | SMCI | BLOCKED | REPAIR | 31.2 | 30.32 | 9 | -2.8% | -7.1 | OPEN |
| 2026-07-23 | SON | BLOCKED | PASS | 56.32 | 58.46 | 9 | +3.8% | -0.5 | OPEN |
| 2026-07-23 | SPG | BLOCKED | PASS | 225.2 | 224.81 | 9 | -0.2% | -4.5 | OPEN |
| 2026-07-23 | TDY | BLOCKED | PASS | 651.22 | 683.73 | 9 | +5.0% | +0.7 | OPEN |
| 2026-07-23 | URA | BLOCKED | DEEP-FAIL | 41.13 | 42.89 | 9 | +4.3% | -0.0 | OPEN |
| 2026-07-23 | URI | BLOCKED | PASS | 1139.71 | 1162.04 | 9 | +2.0% | -2.3 | OPEN |
| 2026-07-23 | VST | BLOCKED | REPAIR | 168.98 | 140.58 | 9 | -16.8% | -21.1 | OPEN |
| 2026-07-23 | VVV | BLOCKED | PASS | 38.31 | 36.98 | 9 | -3.5% | -7.8 | OPEN |
| 2026-07-23 | ECVT | PASSED | PASS | 12.89 | 11.45 | 9 | -11.2% | -15.4 | OPEN |
| 2026-07-23 | FRT | PASSED | PASS | 124.83 | 121.83 | 9 | -2.4% | -6.7 | OPEN |
| 2026-07-23 | HAS | PASSED | PASS | 87.35 | 91.16 | 9 | +4.4% | +0.1 | OPEN |
| 2026-07-23 | LHX | PASSED | REPAIR | 299.67 | 286.12 | 9 | -4.5% | -8.8 | OPEN |
| 2026-07-23 | MLI | PASSED | REPAIR | 63.13 | 69.26 | 9 | +9.7% | +5.4 | OPEN |
| 2026-07-23 | PFE | PASSED | REPAIR | 25.01 | 25.81 | 9 | +3.2% | -1.1 | OPEN |
| 2026-07-23 | SJM | PASSED | PASS | 115.71 | 119.21 | 9 | +3.0% | -1.3 | OPEN |
| 2026-07-23 | VZ | PASSED | REPAIR | 43.82 | 46.47 | 9 | +6.0% | +1.8 | OPEN |
| 2026-07-24 | ALSN | BLOCKED | PASS | 122.34 | 118.13 | 8 | -3.4% | -7.6 | OPEN |
| 2026-07-24 | AVT | BLOCKED | PASS | 89.42 | 97.22 | 8 | +8.7% | +4.5 | OPEN |
| 2026-07-24 | BUD | BLOCKED | REPAIR | 81.66 | 85.18 | 8 | +4.3% | +0.1 | OPEN |
| 2026-07-24 | CB | BLOCKED | PASS | 359.75 | 352.54 | 8 | -2.0% | -6.2 | OPEN |
| 2026-07-24 | CNP | BLOCKED | PASS | 44.56 | 40.65 | 8 | -8.8% | -12.9 | OPEN |
| 2026-07-24 | COST | BLOCKED | REPAIR | 935.03 | 941.99 | 8 | +0.7% | -3.4 | OPEN |
| 2026-07-24 | CRCL | BLOCKED | DEEP-FAIL | 62.36 | 63.28 | 8 | +1.5% | -2.7 | OPEN |
| 2026-07-24 | DE | BLOCKED | PASS | 628.16 | 612.0 | 8 | -2.6% | -6.8 | OPEN |
| 2026-07-24 | DGX | BLOCKED | PASS | 227.86 | 235.84 | 8 | +3.5% | -0.7 | OPEN |
| 2026-07-24 | DLR | BLOCKED | PASS | 199.08 | 194.93 | 8 | -2.1% | -6.3 | OPEN |
| 2026-07-24 | EGBN | BLOCKED | PASS | 28.44 | 28.25 | 8 | -0.7% | -4.8 | OPEN |
| 2026-07-24 | F | BLOCKED | REPAIR | 14.37 | 14.13 | 8 | -1.7% | -5.8 | OPEN |
| 2026-07-24 | FCX | BLOCKED | REPAIR | 62.6 | 69.39 | 8 | +10.8% | +6.7 | OPEN |
| 2026-07-24 | FUTU | BLOCKED | DEEP-FAIL | 99.36 | 110.22 | 8 | +10.9% | +6.8 | OPEN |
| 2026-07-24 | GDX | BLOCKED | DEEP-FAIL | 75.23 | 83.68 | 8 | +11.2% | +7.1 | OPEN |
| 2026-07-24 | GE | BLOCKED | PASS | 353.73 | 381.22 | 8 | +7.8% | +3.6 | OPEN |
| 2026-07-24 | GLD | BLOCKED | REPAIR | 371.9 | 389.64 | 8 | +4.8% | +0.6 | OPEN |
| 2026-07-24 | GM | BLOCKED | PASS | 82.64 | 89.16 | 8 | +7.9% | +3.7 | OPEN |
| 2026-07-24 | HON | BLOCKED | PASS | 243.15 | 248.12 | 8 | +2.0% | -2.1 | OPEN |
| 2026-07-24 | IRM | BLOCKED | PASS | 128.31 | 127.13 | 8 | -0.9% | -5.1 | OPEN |
| 2026-07-24 | JNJ | BLOCKED | PASS | 263.4 | 257.59 | 8 | -2.2% | -6.4 | OPEN |
| 2026-07-24 | LCID | BLOCKED | DEEP-FAIL | 6.3 | 6.7 | 8 | +6.3% | +2.2 | OPEN |
| 2026-07-24 | LDOS | BLOCKED | DEEP-FAIL | 112.14 | 126.85 | 8 | +13.1% | +8.9 | OPEN |
| 2026-07-24 | LIND | BLOCKED | PASS | 26.85 | 34.11 | 8 | +27.0% | +22.9 | OPEN |
| 2026-07-24 | M | BLOCKED | PASS | 23.38 | 25.51 | 8 | +9.1% | +4.9 | OPEN |
| 2026-07-24 | NEM | BLOCKED | REPAIR | 93.19 | 104.29 | 8 | +11.9% | +7.7 | OPEN |
| 2026-07-24 | ORKA | BLOCKED | PASS | 92.16 | 97.19 | 8 | +5.5% | +1.3 | OPEN |
| 2026-07-24 | PH | BLOCKED | PASS | 987.54 | 996.9 | 8 | +0.9% | -3.2 | OPEN |
| 2026-07-24 | PRLB | BLOCKED | PASS | 78.24 | 90.31 | 8 | +15.4% | +11.2 | OPEN |
| 2026-07-24 | ROP | BLOCKED | REPAIR | 367.34 | 394.53 | 8 | +7.4% | +3.2 | OPEN |
| 2026-07-24 | RSPU | BLOCKED | PASS | 82.33 | 77.56 | 8 | -5.8% | -10.0 | OPEN |
| 2026-07-24 | SMCI | BLOCKED | REPAIR | 30.1 | 30.32 | 8 | +0.7% | -3.5 | OPEN |
| 2026-07-24 | SON | BLOCKED | PASS | 58.23 | 58.46 | 8 | +0.4% | -3.8 | OPEN |
| 2026-07-24 | SPG | BLOCKED | PASS | 229.78 | 224.81 | 8 | -2.2% | -6.3 | OPEN |
| 2026-07-24 | TDY | BLOCKED | PASS | 655.35 | 683.73 | 8 | +4.3% | +0.1 | OPEN |
| 2026-07-24 | URA | BLOCKED | DEEP-FAIL | 39.89 | 42.89 | 8 | +7.5% | +3.3 | OPEN |
| 2026-07-24 | URI | BLOCKED | PASS | 1141.59 | 1162.04 | 8 | +1.8% | -2.4 | OPEN |
| 2026-07-24 | VST | BLOCKED | REPAIR | 163.38 | 140.58 | 8 | -14.0% | -18.1 | OPEN |
| 2026-07-24 | XLI | BLOCKED | PASS | 182.66 | 186.35 | 8 | +2.0% | -2.2 | OPEN |
| 2026-07-24 | ACTG | PASSED | PASS | 4.66 | 4.54 | 8 | -2.6% | -6.8 | OPEN |
| 2026-07-24 | DELL | PASSED | PASS | 437.5 | 462.7 | 8 | +5.8% | +1.6 | OPEN |
| 2026-07-24 | EQIX | PASSED | PASS | 1084.24 | 1056.2 | 8 | -2.6% | -6.8 | OPEN |
| 2026-07-24 | LHX | PASSED | REPAIR | 300.21 | 286.12 | 8 | -4.7% | -8.9 | OPEN |
| 2026-07-24 | MLI | PASSED | REPAIR | 63.91 | 69.26 | 8 | +8.4% | +4.2 | OPEN |
| 2026-07-24 | MRK | PASSED | PASS | 131.07 | 128.33 | 8 | -2.1% | -6.3 | OPEN |
| 2026-07-24 | RHP | PASSED | PASS | 133.09 | 127.62 | 8 | -4.1% | -8.3 | OPEN |
| 2026-07-24 | SJM | PASSED | PASS | 118.32 | 119.21 | 8 | +0.8% | -3.4 | OPEN |
| 2026-07-24 | VZ | PASSED | REPAIR | 46.38 | 46.47 | 8 | +0.2% | -4.0 | OPEN |
| 2026-07-27 | ACGL | BLOCKED | PASS | 103.88 | 99.09 | 7 | -4.6% | -8.8 | OPEN |
| 2026-07-27 | ALSN | BLOCKED | PASS | 121.91 | 118.13 | 7 | -3.1% | -7.2 | OPEN |
| 2026-07-27 | AVT | BLOCKED | PASS | 88.38 | 97.22 | 7 | +10.0% | +5.8 | OPEN |
| 2026-07-27 | BUD | BLOCKED | REPAIR | 80.87 | 85.18 | 7 | +5.3% | +1.2 | OPEN |
| 2026-07-27 | CB | BLOCKED | PASS | 358.91 | 352.54 | 7 | -1.8% | -5.9 | OPEN |
| 2026-07-27 | CPRT | BLOCKED | DEEP-FAIL | 29.79 | 28.91 | 7 | -3.0% | -7.1 | OPEN |
| 2026-07-27 | CRCL | BLOCKED | DEEP-FAIL | 65.67 | 63.28 | 7 | -3.6% | -7.8 | OPEN |
| 2026-07-27 | DE | BLOCKED | PASS | 625.02 | 612.0 | 7 | -2.1% | -6.2 | OPEN |
| 2026-07-27 | DLR | BLOCKED | PASS | 195.76 | 194.93 | 7 | -0.4% | -4.6 | OPEN |
| 2026-07-27 | EGBN | BLOCKED | PASS | 28.15 | 28.25 | 7 | +0.4% | -3.8 | OPEN |
| 2026-07-27 | F | BLOCKED | PASS | 14.68 | 14.13 | 7 | -3.8% | -7.9 | OPEN |
| 2026-07-27 | FCX | BLOCKED | REPAIR | 62.72 | 69.39 | 7 | +10.6% | +6.5 | OPEN |
| 2026-07-27 | FUTU | BLOCKED | DEEP-FAIL | 104.27 | 110.22 | 7 | +5.7% | +1.6 | OPEN |
| 2026-07-27 | GDX | BLOCKED | DEEP-FAIL | 75.73 | 83.68 | 7 | +10.5% | +6.3 | OPEN |
| 2026-07-27 | GLD | BLOCKED | REPAIR | 374.63 | 389.64 | 7 | +4.0% | -0.1 | OPEN |
| 2026-07-27 | GM | BLOCKED | PASS | 87.04 | 89.16 | 7 | +2.4% | -1.7 | OPEN |
| 2026-07-27 | HON | BLOCKED | PASS | 245.75 | 248.12 | 7 | +1.0% | -3.2 | OPEN |
| 2026-07-27 | IRM | BLOCKED | PASS | 126.99 | 127.13 | 7 | +0.1% | -4.0 | OPEN |
| 2026-07-27 | LDOS | BLOCKED | DEEP-FAIL | 114.95 | 126.85 | 7 | +10.3% | +6.2 | OPEN |
| 2026-07-27 | LIND | BLOCKED | PASS | 28.09 | 34.11 | 7 | +21.4% | +17.3 | OPEN |
| 2026-07-27 | MAR | BLOCKED | PASS | 383.06 | 361.31 | 7 | -5.7% | -9.8 | OPEN |
| 2026-07-27 | NEM | BLOCKED | REPAIR | 93.47 | 104.29 | 7 | +11.6% | +7.4 | OPEN |
| 2026-07-27 | ORKA | BLOCKED | PASS | 90.2 | 97.19 | 7 | +7.8% | +3.6 | OPEN |
| 2026-07-27 | PGR | BLOCKED | REPAIR | 215.76 | 212.76 | 7 | -1.4% | -5.5 | OPEN |
| 2026-07-27 | PH | BLOCKED | PASS | 987.31 | 996.9 | 7 | +1.0% | -3.2 | OPEN |
| 2026-07-27 | PRLB | BLOCKED | PASS | 77.64 | 90.31 | 7 | +16.3% | +12.2 | OPEN |
| 2026-07-27 | RCL | BLOCKED | REPAIR | 305.04 | 327.42 | 7 | +7.3% | +3.2 | OPEN |
| 2026-07-27 | ROP | BLOCKED | REPAIR | 375.02 | 394.53 | 7 | +5.2% | +1.1 | OPEN |
| 2026-07-27 | RSPU | BLOCKED | PASS | 81.24 | 77.56 | 7 | -4.5% | -8.7 | OPEN |
| 2026-07-27 | SLB | BLOCKED | PASS | 51.53 | 49.91 | 7 | -3.1% | -7.3 | OPEN |
| 2026-07-27 | SMCI | BLOCKED | DEEP-FAIL | 29.81 | 30.32 | 7 | +1.7% | -2.4 | OPEN |
| 2026-07-27 | SON | BLOCKED | PASS | 58.68 | 58.46 | 7 | -0.4% | -4.5 | OPEN |
| 2026-07-27 | TDY | BLOCKED | PASS | 651.65 | 683.73 | 7 | +4.9% | +0.8 | OPEN |
| 2026-07-27 | TJX | BLOCKED | REPAIR | 156.38 | 159.92 | 7 | +2.3% | -1.9 | OPEN |
| 2026-07-27 | URA | BLOCKED | DEEP-FAIL | 40.32 | 42.89 | 7 | +6.4% | +2.2 | OPEN |
| 2026-07-27 | VRSN | BLOCKED | REPAIR | 274.82 | 293.41 | 7 | +6.8% | +2.6 | OPEN |
| 2026-07-27 | VST | BLOCKED | REPAIR | 157.08 | 140.58 | 7 | -10.5% | -14.7 | OPEN |
| 2026-07-27 | WWD | BLOCKED | PASS | 419.76 | 373.28 | 7 | -11.1% | -15.2 | OPEN |
| 2026-07-27 | XLI | BLOCKED | PASS | 183.2 | 186.35 | 7 | +1.7% | -2.4 | OPEN |
| 2026-07-27 | ACTG | PASSED | PASS | 4.63 | 4.54 | 7 | -1.9% | -6.1 | OPEN |
| 2026-07-27 | DELL | PASSED | PASS | 426.91 | 462.7 | 7 | +8.4% | +4.2 | OPEN |
| 2026-07-27 | DGX | PASSED | PASS | 231.84 | 235.84 | 7 | +1.7% | -2.4 | OPEN |
| 2026-07-27 | EQIX | PASSED | PASS | 1046.79 | 1056.2 | 7 | +0.9% | -3.2 | OPEN |
| 2026-07-27 | GE | PASSED | PASS | 361.61 | 381.22 | 7 | +5.4% | +1.3 | OPEN |
| 2026-07-27 | JNJ | PASSED | PASS | 265.95 | 257.59 | 7 | -3.1% | -7.3 | OPEN |
| 2026-07-27 | LHX | PASSED | REPAIR | 303.48 | 286.12 | 7 | -5.7% | -9.9 | OPEN |
| 2026-07-27 | MLI | PASSED | PASS | 64.17 | 69.26 | 7 | +7.9% | +3.8 | OPEN |
| 2026-07-27 | MRK | PASSED | PASS | 130.76 | 128.33 | 7 | -1.9% | -6.0 | OPEN |
| 2026-07-27 | RHP | PASSED | PASS | 134.94 | 127.62 | 7 | -5.4% | -9.6 | OPEN |
| 2026-07-27 | SJM | PASSED | PASS | 121.05 | 119.21 | 7 | -1.5% | -5.7 | OPEN |
| 2026-07-27 | URI | PASSED | PASS | 1127.91 | 1162.04 | 7 | +3.0% | -1.1 | OPEN |
| 2026-07-28 | ACGL | BLOCKED | PASS | 106.48 | 99.09 | 6 | -6.9% | -10.8 | OPEN |
| 2026-07-28 | AGNC | BLOCKED | PASS | 11.07 | 10.67 | 6 | -3.6% | -7.5 | OPEN |
| 2026-07-28 | AI | BLOCKED | DEEP-FAIL | 8.9 | 9.91 | 6 | +11.3% | +7.4 | OPEN |
| 2026-07-28 | AJG | BLOCKED | REPAIR | 265.31 | 251.03 | 6 | -5.4% | -9.3 | OPEN |
| 2026-07-28 | ALSN | BLOCKED | PASS | 121.11 | 118.13 | 6 | -2.5% | -6.4 | OPEN |
| 2026-07-28 | AVT | BLOCKED | REPAIR | 86.22 | 97.22 | 6 | +12.8% | +8.8 | OPEN |
| 2026-07-28 | AXON | BLOCKED | REPAIR | 547.65 | 609.49 | 6 | +11.3% | +7.4 | OPEN |
| 2026-07-28 | BUD | BLOCKED | PASS | 83.2 | 85.18 | 6 | +2.4% | -1.5 | OPEN |
| 2026-07-28 | CB | BLOCKED | PASS | 363.5 | 352.54 | 6 | -3.0% | -6.9 | OPEN |
| 2026-07-28 | CCL | BLOCKED | REPAIR | 28.23 | 29.67 | 6 | +5.1% | +1.2 | OPEN |
| 2026-07-28 | CHTR | BLOCKED | DEEP-FAIL | 139.97 | 153.17 | 6 | +9.4% | +5.5 | OPEN |
| 2026-07-28 | CLX | BLOCKED | REPAIR | 100.32 | 105.84 | 6 | +5.5% | +1.6 | OPEN |
| 2026-07-28 | CNP | BLOCKED | PASS | 44.1 | 40.65 | 6 | -7.8% | -11.7 | OPEN |
| 2026-07-28 | COKE | BLOCKED | PASS | 195.0 | 184.74 | 6 | -5.3% | -9.2 | OPEN |
| 2026-07-28 | CPRT | BLOCKED | DEEP-FAIL | 30.69 | 28.91 | 6 | -5.8% | -9.7 | OPEN |
| 2026-07-28 | CRCL | BLOCKED | DEEP-FAIL | 64.32 | 63.28 | 6 | -1.6% | -5.5 | OPEN |
| 2026-07-28 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.79 | 6 | +11.0% | +7.1 | OPEN |
| 2026-07-28 | DASH | BLOCKED | REPAIR | 195.52 | 207.27 | 6 | +6.0% | +2.1 | OPEN |
| 2026-07-28 | DUOL | BLOCKED | REPAIR | 140.73 | 135.32 | 6 | -3.8% | -7.8 | OPEN |
| 2026-07-28 | EGBN | BLOCKED | PASS | 28.39 | 28.25 | 6 | -0.5% | -4.4 | OPEN |
| 2026-07-28 | ERIE | BLOCKED | REPAIR | 242.43 | 250.79 | 6 | +3.5% | -0.5 | OPEN |
| 2026-07-28 | F | BLOCKED | PASS | 14.96 | 14.13 | 6 | -5.5% | -9.4 | OPEN |
| 2026-07-28 | FCX | BLOCKED | REPAIR | 61.64 | 69.39 | 6 | +12.6% | +8.7 | OPEN |
| 2026-07-28 | FUTU | BLOCKED | DEEP-FAIL | 101.84 | 110.22 | 6 | +8.2% | +4.3 | OPEN |
| 2026-07-28 | GDX | BLOCKED | DEEP-FAIL | 74.21 | 83.68 | 6 | +12.8% | +8.9 | OPEN |
| 2026-07-28 | GLD | BLOCKED | DEEP-FAIL | 369.37 | 389.64 | 6 | +5.5% | +1.6 | OPEN |
| 2026-07-28 | GM | BLOCKED | PASS | 90.3 | 89.16 | 6 | -1.3% | -5.2 | OPEN |
| 2026-07-28 | HD | BLOCKED | REPAIR | 344.47 | 353.14 | 6 | +2.5% | -1.4 | OPEN |
| 2026-07-28 | JETS | BLOCKED | PASS | 31.86 | 33.53 | 6 | +5.2% | +1.3 | OPEN |
| 2026-07-28 | LDOS | BLOCKED | DEEP-FAIL | 118.36 | 126.85 | 6 | +7.2% | +3.3 | OPEN |
| 2026-07-28 | LOW | BLOCKED | REPAIR | 218.24 | 219.94 | 6 | +0.8% | -3.1 | OPEN |
| 2026-07-28 | LZB | BLOCKED | PASS | 41.3 | 41.45 | 6 | +0.4% | -3.5 | OPEN |
| 2026-07-28 | MAR | BLOCKED | PASS | 383.52 | 361.31 | 6 | -5.8% | -9.7 | OPEN |
| 2026-07-28 | MCD | BLOCKED | REPAIR | 273.02 | 274.0 | 6 | +0.4% | -3.5 | OPEN |
| 2026-07-28 | MDT | BLOCKED | REPAIR | 86.88 | 85.99 | 6 | -1.0% | -4.9 | OPEN |
| 2026-07-28 | NCLH | BLOCKED | REPAIR | 21.22 | 20.3 | 6 | -4.3% | -8.2 | OPEN |
| 2026-07-28 | NEM | BLOCKED | DEEP-FAIL | 91.52 | 104.29 | 6 | +13.9% | +10.1 | OPEN |
| 2026-07-28 | NFLX | BLOCKED | DEEP-FAIL | 72.39 | 74.2 | 6 | +2.5% | -1.4 | OPEN |
| 2026-07-28 | NOW | BLOCKED | DEEP-FAIL | 110.62 | 117.22 | 6 | +6.0% | +2.1 | OPEN |
| 2026-07-28 | PGR | BLOCKED | REPAIR | 219.52 | 212.76 | 6 | -3.1% | -7.0 | OPEN |
| 2026-07-28 | PH | BLOCKED | PASS | 990.96 | 996.9 | 6 | +0.6% | -3.3 | OPEN |
| 2026-07-28 | RACE | BLOCKED | REPAIR | 390.14 | 406.8 | 6 | +4.3% | +0.4 | OPEN |
| 2026-07-28 | RCL | BLOCKED | REPAIR | 322.5 | 327.42 | 6 | +1.5% | -2.4 | OPEN |
| 2026-07-28 | RMD | BLOCKED | DEEP-FAIL | 208.96 | 224.03 | 6 | +7.2% | +3.3 | OPEN |
| 2026-07-28 | ROP | BLOCKED | REPAIR | 390.92 | 394.53 | 6 | +0.9% | -3.0 | OPEN |
| 2026-07-28 | RSPU | BLOCKED | PASS | 81.03 | 77.56 | 6 | -4.3% | -8.2 | OPEN |
| 2026-07-28 | SHAK | BLOCKED | DEEP-FAIL | 63.2 | 74.33 | 6 | +17.6% | +13.7 | OPEN |
| 2026-07-28 | SHW | BLOCKED | REPAIR | 354.27 | 369.68 | 6 | +4.3% | +0.4 | OPEN |
| 2026-07-28 | SMCI | BLOCKED | DEEP-FAIL | 28.45 | 30.32 | 6 | +6.6% | +2.7 | OPEN |
| 2026-07-28 | SON | BLOCKED | PASS | 60.56 | 58.46 | 6 | -3.5% | -7.4 | OPEN |
| 2026-07-28 | STGW | BLOCKED | PASS | 7.97 | 8.85 | 6 | +11.0% | +7.1 | OPEN |
| 2026-07-28 | TDY | BLOCKED | PASS | 649.67 | 683.73 | 6 | +5.2% | +1.3 | OPEN |
| 2026-07-28 | TOST | BLOCKED | REPAIR | 32.34 | 34.8 | 6 | +7.6% | +3.7 | OPEN |
| 2026-07-28 | TPR | BLOCKED | PASS | 150.9 | 159.16 | 6 | +5.5% | +1.6 | OPEN |
| 2026-07-28 | TYL | BLOCKED | DEEP-FAIL | 333.35 | 306.58 | 6 | -8.0% | -11.9 | OPEN |
| 2026-07-28 | URA | BLOCKED | DEEP-FAIL | 38.95 | 42.89 | 6 | +10.1% | +6.2 | OPEN |
| 2026-07-28 | URI | BLOCKED | PASS | 1091.26 | 1162.04 | 6 | +6.5% | +2.6 | OPEN |
| 2026-07-28 | VRSN | BLOCKED | REPAIR | 281.15 | 293.41 | 6 | +4.4% | +0.5 | OPEN |
| 2026-07-28 | WWD | BLOCKED | PASS | 410.55 | 373.28 | 6 | -9.1% | -13.0 | OPEN |
| 2026-07-28 | XLI | BLOCKED | PASS | 182.49 | 186.35 | 6 | +2.1% | -1.8 | OPEN |
| 2026-07-28 | ZTS | BLOCKED | DEEP-FAIL | 77.51 | 74.39 | 6 | -4.0% | -7.9 | OPEN |
| 2026-07-28 | ACTG | PASSED | PASS | 4.63 | 4.54 | 6 | -1.9% | -5.8 | OPEN |
| 2026-07-28 | CTS | PASSED | PASS | 64.82 | 66.78 | 6 | +3.0% | -0.9 | OPEN |
| 2026-07-28 | DAL | PASSED | PASS | 89.37 | 93.14 | 6 | +4.2% | +0.3 | OPEN |
| 2026-07-28 | DE | PASSED | PASS | 639.84 | 612.0 | 6 | -4.3% | -8.3 | OPEN |
| 2026-07-28 | DGX | PASSED | PASS | 235.94 | 235.84 | 6 | -0.0% | -4.0 | OPEN |
| 2026-07-28 | DLR | PASSED | PASS | 193.18 | 194.93 | 6 | +0.9% | -3.0 | OPEN |
| 2026-07-28 | EQIX | PASSED | REPAIR | 1034.86 | 1056.2 | 6 | +2.1% | -1.8 | OPEN |
| 2026-07-28 | GE | PASSED | PASS | 363.59 | 381.22 | 6 | +4.8% | +0.9 | OPEN |
| 2026-07-28 | HON | PASSED | PASS | 247.05 | 248.12 | 6 | +0.4% | -3.5 | OPEN |
| 2026-07-28 | JNJ | PASSED | PASS | 266.73 | 257.59 | 6 | -3.4% | -7.3 | OPEN |
| 2026-07-28 | LHX | PASSED | REPAIR | 305.2 | 286.12 | 6 | -6.2% | -10.2 | OPEN |
| 2026-07-28 | LLY | PASSED | PASS | 1220.66 | 1169.86 | 6 | -4.2% | -8.1 | OPEN |
| 2026-07-28 | MLI | PASSED | PASS | 66.49 | 69.26 | 6 | +4.2% | +0.3 | OPEN |
| 2026-07-28 | MNST | PASSED | PASS | 97.74 | 94.46 | 6 | -3.4% | -7.3 | OPEN |
| 2026-07-28 | MRK | PASSED | PASS | 131.82 | 128.33 | 6 | -2.6% | -6.5 | OPEN |
| 2026-07-28 | PEP | PASSED | REPAIR | 142.86 | 138.78 | 6 | -2.9% | -6.8 | OPEN |
| 2026-07-28 | SLB | PASSED | REPAIR | 49.98 | 49.91 | 6 | -0.1% | -4.0 | OPEN |
| 2026-07-28 | SSD | PASSED | PASS | 198.28 | 197.35 | 6 | -0.5% | -4.4 | OPEN |
| 2026-07-28 | TJX | PASSED | PASS | 160.8 | 159.92 | 6 | -0.6% | -4.5 | OPEN |
| 2026-07-29 | ABNB | BLOCKED | PASS | 153.01 | 152.49 | 5 | -0.3% | -5.9 | OPEN |
| 2026-07-29 | ACGL | BLOCKED | PASS | 104.55 | 99.09 | 5 | -5.2% | -10.8 | OPEN |
| 2026-07-29 | AGNC | BLOCKED | PASS | 10.9 | 10.67 | 5 | -2.1% | -7.6 | OPEN |
| 2026-07-29 | AI | BLOCKED | DEEP-FAIL | 8.85 | 9.91 | 5 | +12.0% | +6.5 | OPEN |
| 2026-07-29 | AJG | BLOCKED | REPAIR | 268.91 | 251.03 | 5 | -6.7% | -12.2 | OPEN |
| 2026-07-29 | AXON | BLOCKED | REPAIR | 531.2 | 609.49 | 5 | +14.7% | +9.2 | OPEN |
| 2026-07-29 | BFC | BLOCKED | PASS | 151.78 | 156.31 | 5 | +3.0% | -2.5 | OPEN |
| 2026-07-29 | CB | BLOCKED | PASS | 361.9 | 352.54 | 5 | -2.6% | -8.1 | OPEN |
| 2026-07-29 | CHTR | BLOCKED | DEEP-FAIL | 145.2 | 153.17 | 5 | +5.5% | -0.0 | OPEN |
| 2026-07-29 | CLX | BLOCKED | REPAIR | 99.63 | 105.84 | 5 | +6.2% | +0.7 | OPEN |
| 2026-07-29 | CMG | BLOCKED | REPAIR | 34.24 | 34.5 | 5 | +0.8% | -4.8 | OPEN |
| 2026-07-29 | CNP | BLOCKED | PASS | 42.93 | 40.65 | 5 | -5.3% | -10.8 | OPEN |
| 2026-07-29 | COKE | BLOCKED | PASS | 192.39 | 184.74 | 5 | -4.0% | -9.5 | OPEN |
| 2026-07-29 | CPRT | BLOCKED | DEEP-FAIL | 30.82 | 28.91 | 5 | -6.2% | -11.7 | OPEN |
| 2026-07-29 | CTM | BLOCKED | DEEP-FAIL | 0.66 | 0.79 | 5 | +18.4% | +12.9 | OPEN |
| 2026-07-29 | DASH | BLOCKED | REPAIR | 193.53 | 207.27 | 5 | +7.1% | +1.6 | OPEN |
| 2026-07-29 | DE | BLOCKED | PASS | 610.95 | 612.0 | 5 | +0.2% | -5.4 | OPEN |
| 2026-07-29 | DUOL | BLOCKED | REPAIR | 140.17 | 135.32 | 5 | -3.5% | -9.0 | OPEN |
| 2026-07-29 | EGBN | BLOCKED | PASS | 27.89 | 28.25 | 5 | +1.3% | -4.2 | OPEN |
| 2026-07-29 | EQIX | BLOCKED | REPAIR | 1008.02 | 1056.2 | 5 | +4.8% | -0.8 | OPEN |
| 2026-07-29 | ERIE | BLOCKED | REPAIR | 248.55 | 250.79 | 5 | +0.9% | -4.6 | OPEN |
| 2026-07-29 | ESQ | BLOCKED | PASS | 131.89 | 132.2 | 5 | +0.2% | -5.3 | OPEN |
| 2026-07-29 | FCX | BLOCKED | REPAIR | 59.99 | 69.39 | 5 | +15.7% | +10.1 | OPEN |
| 2026-07-29 | GDX | BLOCKED | DEEP-FAIL | 73.57 | 83.68 | 5 | +13.7% | +8.2 | OPEN |
| 2026-07-29 | GME | BLOCKED | REPAIR | 21.84 | 19.01 | 5 | -13.0% | -18.5 | OPEN |
| 2026-07-29 | GRND | BLOCKED | PASS | 17.21 | 17.78 | 5 | +3.3% | -2.2 | OPEN |
| 2026-07-29 | HD | BLOCKED | REPAIR | 338.27 | 353.14 | 5 | +4.4% | -1.1 | OPEN |
| 2026-07-29 | IBM | BLOCKED | DEEP-FAIL | 226.44 | 235.92 | 5 | +4.2% | -1.3 | OPEN |
| 2026-07-29 | JBLU | BLOCKED | PASS | 5.72 | 6.36 | 5 | +11.2% | +5.7 | OPEN |
| 2026-07-29 | JETS | BLOCKED | PASS | 30.97 | 33.53 | 5 | +8.3% | +2.7 | OPEN |
| 2026-07-29 | KWEB | BLOCKED | DEEP-FAIL | 27.8 | 28.54 | 5 | +2.7% | -2.9 | OPEN |
| 2026-07-29 | LDOS | BLOCKED | DEEP-FAIL | 114.37 | 126.85 | 5 | +10.9% | +5.4 | OPEN |
| 2026-07-29 | LOW | BLOCKED | REPAIR | 215.68 | 219.94 | 5 | +2.0% | -3.5 | OPEN |
| 2026-07-29 | LZB | BLOCKED | PASS | 40.93 | 41.45 | 5 | +1.3% | -4.3 | OPEN |
| 2026-07-29 | MAR | BLOCKED | PASS | 381.12 | 361.31 | 5 | -5.2% | -10.7 | OPEN |
| 2026-07-29 | MCD | BLOCKED | REPAIR | 271.52 | 274.0 | 5 | +0.9% | -4.6 | OPEN |
| 2026-07-29 | NCLH | BLOCKED | REPAIR | 20.75 | 20.3 | 5 | -2.2% | -7.7 | OPEN |
| 2026-07-29 | NEM | BLOCKED | DEEP-FAIL | 91.34 | 104.29 | 5 | +14.2% | +8.7 | OPEN |
| 2026-07-29 | NEO | BLOCKED | PASS | 15.27 | 15.73 | 5 | +3.0% | -2.5 | OPEN |
| 2026-07-29 | NFLX | BLOCKED | DEEP-FAIL | 73.63 | 74.2 | 5 | +0.8% | -4.8 | OPEN |
| 2026-07-29 | NIO | BLOCKED | DEEP-FAIL | 4.76 | 4.65 | 5 | -2.3% | -7.8 | OPEN |
| 2026-07-29 | NOW | BLOCKED | REPAIR | 115.76 | 117.22 | 5 | +1.3% | -4.3 | OPEN |
| 2026-07-29 | NVST | BLOCKED | PASS | 28.37 | 28.63 | 5 | +0.9% | -4.6 | OPEN |
| 2026-07-29 | PGR | BLOCKED | REPAIR | 219.99 | 212.76 | 5 | -3.3% | -8.8 | OPEN |
| 2026-07-29 | PH | BLOCKED | PASS | 951.07 | 996.9 | 5 | +4.8% | -0.7 | OPEN |
| 2026-07-29 | RCL | BLOCKED | REPAIR | 323.58 | 327.42 | 5 | +1.2% | -4.3 | OPEN |
| 2026-07-29 | RMD | BLOCKED | REPAIR | 214.29 | 224.03 | 5 | +4.5% | -1.0 | OPEN |
| 2026-07-29 | ROKU | BLOCKED | PASS | 145.33 | 146.96 | 5 | +1.1% | -4.4 | OPEN |
| 2026-07-29 | ROP | BLOCKED | REPAIR | 408.07 | 394.53 | 5 | -3.3% | -8.8 | OPEN |
| 2026-07-29 | RSPU | BLOCKED | PASS | 79.85 | 77.56 | 5 | -2.9% | -8.4 | OPEN |
| 2026-07-29 | SHAK | BLOCKED | DEEP-FAIL | 63.05 | 74.33 | 5 | +17.9% | +12.4 | OPEN |
| 2026-07-29 | SHW | BLOCKED | REPAIR | 343.88 | 369.68 | 5 | +7.5% | +2.0 | OPEN |
| 2026-07-29 | SKYY | BLOCKED | PASS | 138.56 | 153.48 | 5 | +10.8% | +5.2 | OPEN |
| 2026-07-29 | SMCI | BLOCKED | DEEP-FAIL | 25.7 | 30.32 | 5 | +18.0% | +12.4 | OPEN |
| 2026-07-29 | STGW | BLOCKED | PASS | 8.08 | 8.85 | 5 | +9.5% | +4.0 | OPEN |
| 2026-07-29 | TDY | BLOCKED | PASS | 631.35 | 683.73 | 5 | +8.3% | +2.8 | OPEN |
| 2026-07-29 | TOST | BLOCKED | REPAIR | 32.6 | 34.8 | 5 | +6.8% | +1.2 | OPEN |
| 2026-07-29 | TPR | BLOCKED | PASS | 150.11 | 159.16 | 5 | +6.0% | +0.5 | OPEN |
| 2026-07-29 | TYL | BLOCKED | DEEP-FAIL | 333.5 | 306.58 | 5 | -8.1% | -13.6 | OPEN |
| 2026-07-29 | URI | BLOCKED | PASS | 1055.11 | 1162.04 | 5 | +10.1% | +4.6 | OPEN |
| 2026-07-29 | VRSN | BLOCKED | REPAIR | 290.92 | 293.41 | 5 | +0.9% | -4.7 | OPEN |
| 2026-07-29 | WWD | BLOCKED | PASS | 385.42 | 373.28 | 5 | -3.1% | -8.7 | OPEN |
| 2026-07-29 | ZTS | BLOCKED | DEEP-FAIL | 77.93 | 74.39 | 5 | -4.5% | -10.1 | OPEN |
| 2026-07-29 | CCL | PASSED | REPAIR | 27.81 | 29.67 | 5 | +6.7% | +1.2 | OPEN |
| 2026-07-29 | CPT | PASSED | PASS | 116.37 | 111.91 | 5 | -3.8% | -9.4 | OPEN |
| 2026-07-29 | CTS | PASSED | PASS | 61.53 | 66.78 | 5 | +8.5% | +3.0 | OPEN |
| 2026-07-29 | DAL | PASSED | PASS | 86.25 | 93.14 | 5 | +8.0% | +2.5 | OPEN |
| 2026-07-29 | DGX | PASSED | PASS | 235.22 | 235.84 | 5 | +0.3% | -5.3 | OPEN |
| 2026-07-29 | DLR | PASSED | PASS | 188.18 | 194.93 | 5 | +3.6% | -1.9 | OPEN |
| 2026-07-29 | GE | PASSED | PASS | 350.63 | 381.22 | 5 | +8.7% | +3.2 | OPEN |
| 2026-07-29 | HON | PASSED | PASS | 241.12 | 248.12 | 5 | +2.9% | -2.6 | OPEN |
| 2026-07-29 | JNJ | PASSED | PASS | 265.53 | 257.59 | 5 | -3.0% | -8.5 | OPEN |
| 2026-07-29 | KDP | PASSED | PASS | 31.45 | 30.75 | 5 | -2.2% | -7.8 | OPEN |
| 2026-07-29 | LHX | PASSED | REPAIR | 297.53 | 286.12 | 5 | -3.8% | -9.4 | OPEN |
| 2026-07-29 | LLY | PASSED | PASS | 1210.02 | 1169.86 | 5 | -3.3% | -8.8 | OPEN |
| 2026-07-29 | MDT | PASSED | REPAIR | 87.54 | 85.99 | 5 | -1.8% | -7.3 | OPEN |
| 2026-07-29 | MNST | PASSED | PASS | 97.23 | 94.46 | 5 | -2.9% | -8.4 | OPEN |
| 2026-07-29 | MRK | PASSED | PASS | 130.36 | 128.33 | 5 | -1.6% | -7.1 | OPEN |
| 2026-07-29 | PEP | PASSED | REPAIR | 143.5 | 138.78 | 5 | -3.3% | -8.8 | OPEN |
| 2026-07-29 | RACE | PASSED | REPAIR | 385.69 | 406.8 | 5 | +5.5% | -0.1 | OPEN |
| 2026-07-29 | SLB | PASSED | REPAIR | 48.96 | 49.91 | 5 | +1.9% | -3.6 | OPEN |
| 2026-07-29 | SSD | PASSED | REPAIR | 189.48 | 197.35 | 5 | +4.2% | -1.4 | OPEN |
| 2026-07-29 | TJX | PASSED | PASS | 161.63 | 159.92 | 5 | -1.1% | -6.6 | OPEN |
| 2026-07-30 | ABNB | BLOCKED | PASS | 152.08 | 152.49 | 4 | +0.3% | -3.5 | OPEN |
| 2026-07-30 | ACGL | BLOCKED | PASS | 101.14 | 99.09 | 4 | -2.0% | -5.8 | OPEN |
| 2026-07-30 | AGNC | BLOCKED | PASS | 10.92 | 10.67 | 4 | -2.3% | -6.1 | OPEN |
| 2026-07-30 | AI | BLOCKED | DEEP-FAIL | 9.07 | 9.91 | 4 | +9.3% | +5.5 | OPEN |
| 2026-07-30 | AJG | BLOCKED | REPAIR | 256.46 | 251.03 | 4 | -2.1% | -5.9 | OPEN |
| 2026-07-30 | APD | BLOCKED | PASS | 300.2 | 295.09 | 4 | -1.7% | -5.5 | OPEN |
| 2026-07-30 | AXON | BLOCKED | REPAIR | 525.3 | 609.49 | 4 | +16.0% | +12.2 | OPEN |
| 2026-07-30 | CB | BLOCKED | PASS | 350.15 | 352.54 | 4 | +0.7% | -3.1 | OPEN |
| 2026-07-30 | CHTR | BLOCKED | DEEP-FAIL | 142.0 | 153.17 | 4 | +7.9% | +4.1 | OPEN |
| 2026-07-30 | CLX | BLOCKED | REPAIR | 96.73 | 105.84 | 4 | +9.4% | +5.6 | OPEN |
| 2026-07-30 | CMG | BLOCKED | REPAIR | 38.52 | 34.5 | 4 | -10.4% | -14.2 | OPEN |
| 2026-07-30 | CNP | BLOCKED | REPAIR | 42.15 | 40.65 | 4 | -3.6% | -7.3 | OPEN |
| 2026-07-30 | COKE | BLOCKED | PASS | 189.83 | 184.74 | 4 | -2.7% | -6.5 | OPEN |
| 2026-07-30 | CPRT | BLOCKED | DEEP-FAIL | 29.57 | 28.91 | 4 | -2.2% | -6.0 | OPEN |
| 2026-07-30 | CTM | BLOCKED | DEEP-FAIL | 0.71 | 0.79 | 4 | +10.4% | +6.6 | OPEN |
| 2026-07-30 | DASH | BLOCKED | REPAIR | 197.53 | 207.27 | 4 | +4.9% | +1.1 | OPEN |
| 2026-07-30 | DE | BLOCKED | PASS | 599.47 | 612.0 | 4 | +2.1% | -1.7 | OPEN |
| 2026-07-30 | DUOL | BLOCKED | REPAIR | 133.6 | 135.32 | 4 | +1.3% | -2.5 | OPEN |
| 2026-07-30 | EGBN | BLOCKED | PASS | 27.49 | 28.25 | 4 | +2.8% | -1.0 | OPEN |
| 2026-07-30 | GME | BLOCKED | REPAIR | 21.88 | 19.01 | 4 | -13.1% | -16.9 | OPEN |
| 2026-07-30 | HD | BLOCKED | REPAIR | 333.35 | 353.14 | 4 | +5.9% | +2.1 | OPEN |
| 2026-07-30 | IBM | BLOCKED | DEEP-FAIL | 221.74 | 235.92 | 4 | +6.4% | +2.6 | OPEN |
| 2026-07-30 | JBLU | BLOCKED | PASS | 6.07 | 6.36 | 4 | +4.8% | +1.0 | OPEN |
| 2026-07-30 | KWEB | BLOCKED | DEEP-FAIL | 28.06 | 28.54 | 4 | +1.7% | -2.1 | OPEN |
| 2026-07-30 | LDOS | BLOCKED | DEEP-FAIL | 112.41 | 126.85 | 4 | +12.8% | +9.1 | OPEN |
| 2026-07-30 | LLY | BLOCKED | PASS | 1154.97 | 1169.86 | 4 | +1.3% | -2.5 | OPEN |
| 2026-07-30 | LOW | BLOCKED | DEEP-FAIL | 210.08 | 219.94 | 4 | +4.7% | +0.9 | OPEN |
| 2026-07-30 | LYV | BLOCKED | PASS | 183.56 | 183.52 | 4 | -0.0% | -3.8 | OPEN |
| 2026-07-30 | LZB | BLOCKED | PASS | 40.13 | 41.45 | 4 | +3.3% | -0.5 | OPEN |
| 2026-07-30 | MAR | BLOCKED | REPAIR | 375.48 | 361.31 | 4 | -3.8% | -7.6 | OPEN |
| 2026-07-30 | MCD | BLOCKED | DEEP-FAIL | 268.44 | 274.0 | 4 | +2.1% | -1.7 | OPEN |
| 2026-07-30 | MIDD | BLOCKED | PASS | 133.32 | 135.34 | 4 | +1.5% | -2.3 | OPEN |
| 2026-07-30 | MRK | BLOCKED | PASS | 129.79 | 128.33 | 4 | -1.1% | -4.9 | OPEN |
| 2026-07-30 | MSFT | BLOCKED | REPAIR | 451.1 | 487.46 | 4 | +8.1% | +4.3 | OPEN |
| 2026-07-30 | NCLH | BLOCKED | REPAIR | 18.72 | 20.3 | 4 | +8.4% | +4.7 | OPEN |
| 2026-07-30 | NFLX | BLOCKED | DEEP-FAIL | 73.17 | 74.2 | 4 | +1.4% | -2.4 | OPEN |
| 2026-07-30 | NIO | BLOCKED | DEEP-FAIL | 4.84 | 4.65 | 4 | -3.9% | -7.7 | OPEN |
| 2026-07-30 | NOW | BLOCKED | DEEP-FAIL | 110.07 | 117.22 | 4 | +6.5% | +2.7 | OPEN |
| 2026-07-30 | NVST | BLOCKED | PASS | 27.78 | 28.63 | 4 | +3.1% | -0.7 | OPEN |
| 2026-07-30 | PB | BLOCKED | PASS | 74.82 | 74.62 | 4 | -0.3% | -4.1 | OPEN |
| 2026-07-30 | PGR | BLOCKED | REPAIR | 213.28 | 212.76 | 4 | -0.2% | -4.0 | OPEN |
| 2026-07-30 | PH | BLOCKED | PASS | 962.79 | 996.9 | 4 | +3.5% | -0.2 | OPEN |
| 2026-07-30 | RCL | BLOCKED | REPAIR | 321.94 | 327.42 | 4 | +1.7% | -2.1 | OPEN |
| 2026-07-30 | RMD | BLOCKED | REPAIR | 208.56 | 224.03 | 4 | +7.4% | +3.6 | OPEN |
| 2026-07-30 | ROKU | BLOCKED | PASS | 145.09 | 146.96 | 4 | +1.3% | -2.5 | OPEN |
| 2026-07-30 | RSPU | BLOCKED | REPAIR | 79.51 | 77.56 | 4 | -2.5% | -6.2 | OPEN |
| 2026-07-30 | SFM | BLOCKED | REPAIR | 86.85 | 85.12 | 4 | -2.0% | -5.8 | OPEN |
| 2026-07-30 | SHAK | BLOCKED | DEEP-FAIL | 63.07 | 74.33 | 4 | +17.9% | +14.1 | OPEN |
| 2026-07-30 | SHW | BLOCKED | REPAIR | 344.84 | 369.68 | 4 | +7.2% | +3.4 | OPEN |
| 2026-07-30 | SKYY | BLOCKED | PASS | 140.03 | 153.48 | 4 | +9.6% | +5.8 | OPEN |
| 2026-07-30 | SSD | BLOCKED | REPAIR | 186.67 | 197.35 | 4 | +5.7% | +1.9 | OPEN |
| 2026-07-30 | STGW | BLOCKED | PASS | 8.49 | 8.85 | 4 | +4.2% | +0.5 | OPEN |
| 2026-07-30 | TDY | BLOCKED | PASS | 649.18 | 683.73 | 4 | +5.3% | +1.5 | OPEN |
| 2026-07-30 | TOST | BLOCKED | REPAIR | 32.85 | 34.8 | 4 | +5.9% | +2.1 | OPEN |
| 2026-07-30 | TPR | BLOCKED | PASS | 152.58 | 159.16 | 4 | +4.3% | +0.5 | OPEN |
| 2026-07-30 | TYL | BLOCKED | DEEP-FAIL | 323.31 | 306.58 | 4 | -5.2% | -9.0 | OPEN |
| 2026-07-30 | URI | BLOCKED | PASS | 1068.63 | 1162.04 | 4 | +8.7% | +5.0 | OPEN |
| 2026-07-30 | ZTS | BLOCKED | DEEP-FAIL | 76.03 | 74.39 | 4 | -2.2% | -6.0 | OPEN |
| 2026-07-30 | CCL | PASSED | REPAIR | 27.77 | 29.67 | 4 | +6.8% | +3.0 | OPEN |
| 2026-07-30 | CPT | PASSED | PASS | 113.29 | 111.91 | 4 | -1.2% | -5.0 | OPEN |
| 2026-07-30 | CTS | PASSED | REPAIR | 62.7 | 66.78 | 4 | +6.5% | +2.7 | OPEN |
| 2026-07-30 | DAL | PASSED | PASS | 88.59 | 93.14 | 4 | +5.1% | +1.4 | OPEN |
| 2026-07-30 | DGX | PASSED | PASS | 234.3 | 235.84 | 4 | +0.7% | -3.1 | OPEN |
| 2026-07-30 | EQIX | PASSED | PASS | 1047.53 | 1056.2 | 4 | +0.8% | -3.0 | OPEN |
| 2026-07-30 | ERIE | PASSED | REPAIR | 233.67 | 250.79 | 4 | +7.3% | +3.5 | OPEN |
| 2026-07-30 | GE | PASSED | PASS | 355.04 | 381.22 | 4 | +7.4% | +3.6 | OPEN |
| 2026-07-30 | JETS | PASSED | PASS | 31.68 | 33.53 | 4 | +5.8% | +2.0 | OPEN |
| 2026-07-30 | KDP | PASSED | PASS | 31.57 | 30.75 | 4 | -2.6% | -6.4 | OPEN |
| 2026-07-30 | MDT | PASSED | REPAIR | 85.71 | 85.99 | 4 | +0.3% | -3.5 | OPEN |
| 2026-07-30 | MNST | PASSED | PASS | 97.65 | 94.46 | 4 | -3.3% | -7.1 | OPEN |
| 2026-07-30 | PEP | PASSED | REPAIR | 140.2 | 138.78 | 4 | -1.0% | -4.8 | OPEN |
| 2026-07-30 | RACE | PASSED | REPAIR | 397.73 | 406.8 | 4 | +2.3% | -1.5 | OPEN |
| 2026-07-30 | ROP | PASSED | REPAIR | 389.25 | 394.53 | 4 | +1.4% | -2.4 | OPEN |
| 2026-07-30 | ST | PASSED | PASS | 47.99 | 47.59 | 4 | -0.8% | -4.6 | OPEN |
| 2026-07-30 | TJX | PASSED | PASS | 159.26 | 159.92 | 4 | +0.4% | -3.4 | OPEN |
| 2026-07-30 | VRSN | PASSED | REPAIR | 286.58 | 293.41 | 4 | +2.4% | -1.4 | OPEN |
| 2026-07-31 | ABNB | BLOCKED | PASS | 151.52 | 152.49 | 3 | +0.6% | -2.4 | OPEN |
| 2026-07-31 | ACGL | BLOCKED | PASS | 100.53 | 99.09 | 3 | -1.4% | -4.5 | OPEN |
| 2026-07-31 | AGNC | BLOCKED | PASS | 10.66 | 10.67 | 3 | +0.1% | -3.0 | OPEN |
| 2026-07-31 | AI | BLOCKED | DEEP-FAIL | 9.18 | 9.91 | 3 | +8.0% | +4.9 | OPEN |
| 2026-07-31 | AJG | BLOCKED | REPAIR | 249.42 | 251.03 | 3 | +0.7% | -2.4 | OPEN |
| 2026-07-31 | AMZN | BLOCKED | PASS | 271.58 | 272.65 | 3 | +0.4% | -2.6 | OPEN |
| 2026-07-31 | APD | BLOCKED | PASS | 294.89 | 295.09 | 3 | +0.1% | -3.0 | OPEN |
| 2026-07-31 | APH | BLOCKED | PASS | 160.7 | 172.24 | 3 | +7.2% | +4.1 | OPEN |
| 2026-07-31 | AXON | BLOCKED | REPAIR | 527.76 | 609.49 | 3 | +15.5% | +12.4 | OPEN |
| 2026-07-31 | BABA | BLOCKED | DEEP-FAIL | 122.25 | 128.53 | 3 | +5.1% | +2.1 | OPEN |
| 2026-07-31 | CB | BLOCKED | PASS | 350.68 | 352.54 | 3 | +0.5% | -2.5 | OPEN |
| 2026-07-31 | CCL | BLOCKED | REPAIR | 27.81 | 29.67 | 3 | +6.7% | +3.6 | OPEN |
| 2026-07-31 | CHTR | BLOCKED | DEEP-FAIL | 144.98 | 153.17 | 3 | +5.7% | +2.6 | OPEN |
| 2026-07-31 | CLX | BLOCKED | REPAIR | 95.53 | 105.84 | 3 | +10.8% | +7.8 | OPEN |
| 2026-07-31 | CMG | BLOCKED | REPAIR | 37.22 | 34.5 | 3 | -7.3% | -10.3 | OPEN |
| 2026-07-31 | COKE | BLOCKED | PASS | 187.9 | 184.74 | 3 | -1.7% | -4.7 | OPEN |
| 2026-07-31 | CPRT | BLOCKED | DEEP-FAIL | 29.12 | 28.91 | 3 | -0.7% | -3.8 | OPEN |
| 2026-07-31 | CPT | BLOCKED | REPAIR | 110.81 | 111.91 | 3 | +1.0% | -2.0 | OPEN |
| 2026-07-31 | CTM | BLOCKED | DEEP-FAIL | 0.72 | 0.79 | 3 | +9.5% | +6.4 | OPEN |
| 2026-07-31 | DAL | BLOCKED | PASS | 87.44 | 93.14 | 3 | +6.5% | +3.5 | OPEN |
| 2026-07-31 | DASH | BLOCKED | REPAIR | 196.16 | 207.27 | 3 | +5.7% | +2.6 | OPEN |
| 2026-07-31 | DE | BLOCKED | PASS | 592.67 | 612.0 | 3 | +3.3% | +0.2 | OPEN |
| 2026-07-31 | DUOL | BLOCKED | REPAIR | 134.81 | 135.32 | 3 | +0.4% | -2.7 | OPEN |
| 2026-07-31 | EGBN | BLOCKED | PASS | 27.75 | 28.25 | 3 | +1.8% | -1.2 | OPEN |
| 2026-07-31 | EME | BLOCKED | PASS | 797.43 | 822.16 | 3 | +3.1% | +0.1 | OPEN |
| 2026-07-31 | EQIX | BLOCKED | REPAIR | 1019.28 | 1056.2 | 3 | +3.6% | +0.6 | OPEN |
| 2026-07-31 | ERIE | BLOCKED | REPAIR | 242.04 | 250.79 | 3 | +3.6% | +0.6 | OPEN |
| 2026-07-31 | GH | BLOCKED | PASS | 161.99 | 163.18 | 3 | +0.7% | -2.3 | OPEN |
| 2026-07-31 | GME | BLOCKED | REPAIR | 21.72 | 19.01 | 3 | -12.5% | -15.5 | OPEN |
| 2026-07-31 | GOOG | BLOCKED | REPAIR | 356.65 | 360.13 | 3 | +1.0% | -2.1 | OPEN |
| 2026-07-31 | GRND | BLOCKED | PASS | 17.34 | 17.78 | 3 | +2.5% | -0.5 | OPEN |
| 2026-07-31 | HD | BLOCKED | REPAIR | 331.96 | 353.14 | 3 | +6.4% | +3.3 | OPEN |
| 2026-07-31 | IBM | BLOCKED | DEEP-FAIL | 223.65 | 235.92 | 3 | +5.5% | +2.4 | OPEN |
| 2026-07-31 | IGV | BLOCKED | REPAIR | 94.58 | 101.31 | 3 | +7.1% | +4.1 | OPEN |
| 2026-07-31 | JBLU | BLOCKED | PASS | 6.03 | 6.36 | 3 | +5.5% | +2.4 | OPEN |
| 2026-07-31 | JETS | BLOCKED | PASS | 31.28 | 33.53 | 3 | +7.2% | +4.2 | OPEN |
| 2026-07-31 | KWEB | BLOCKED | DEEP-FAIL | 28.49 | 28.54 | 3 | +0.2% | -2.9 | OPEN |
| 2026-07-31 | LDOS | BLOCKED | DEEP-FAIL | 115.6 | 126.85 | 3 | +9.7% | +6.7 | OPEN |
| 2026-07-31 | LOW | BLOCKED | DEEP-FAIL | 207.81 | 219.94 | 3 | +5.8% | +2.8 | OPEN |
| 2026-07-31 | LYV | BLOCKED | PASS | 174.13 | 183.52 | 3 | +5.4% | +2.4 | OPEN |
| 2026-07-31 | LZB | BLOCKED | PASS | 39.38 | 41.45 | 3 | +5.3% | +2.2 | OPEN |
| 2026-07-31 | MAR | BLOCKED | REPAIR | 372.83 | 361.31 | 3 | -3.1% | -6.1 | OPEN |
| 2026-07-31 | MCD | BLOCKED | DEEP-FAIL | 270.64 | 274.0 | 3 | +1.2% | -1.8 | OPEN |
| 2026-07-31 | MDT | BLOCKED | REPAIR | 85.39 | 85.99 | 3 | +0.7% | -2.3 | OPEN |
| 2026-07-31 | MIDD | BLOCKED | PASS | 133.58 | 135.34 | 3 | +1.3% | -1.7 | OPEN |
| 2026-07-31 | MRK | BLOCKED | PASS | 130.2 | 128.33 | 3 | -1.4% | -4.5 | OPEN |
| 2026-07-31 | MSFT | BLOCKED | REPAIR | 464.72 | 487.46 | 3 | +4.9% | +1.9 | OPEN |
| 2026-07-31 | NCLH | BLOCKED | REPAIR | 18.53 | 20.3 | 3 | +9.6% | +6.5 | OPEN |
| 2026-07-31 | NFLX | BLOCKED | DEEP-FAIL | 71.71 | 74.2 | 3 | +3.5% | +0.4 | OPEN |
| 2026-07-31 | NIO | BLOCKED | DEEP-FAIL | 4.88 | 4.65 | 3 | -4.7% | -7.8 | OPEN |
| 2026-07-31 | NOW | BLOCKED | DEEP-FAIL | 111.23 | 117.22 | 3 | +5.4% | +2.3 | OPEN |
| 2026-07-31 | PEP | BLOCKED | REPAIR | 139.56 | 138.78 | 3 | -0.6% | -3.6 | OPEN |
| 2026-07-31 | PGR | BLOCKED | REPAIR | 211.42 | 212.76 | 3 | +0.6% | -2.4 | OPEN |
| 2026-07-31 | PH | BLOCKED | PASS | 976.53 | 996.9 | 3 | +2.1% | -1.0 | OPEN |
| 2026-07-31 | PLPC | BLOCKED | PASS | 356.98 | 471.29 | 3 | +32.0% | +29.0 | OPEN |
| 2026-07-31 | PWR | BLOCKED | REPAIR | 667.36 | 682.99 | 3 | +2.3% | -0.7 | OPEN |
| 2026-07-31 | RCL | BLOCKED | REPAIR | 318.3 | 327.42 | 3 | +2.9% | -0.2 | OPEN |
| 2026-07-31 | RMD | BLOCKED | DEEP-FAIL | 210.98 | 224.03 | 3 | +6.2% | +3.1 | OPEN |
| 2026-07-31 | ROKU | BLOCKED | PASS | 145.01 | 146.96 | 3 | +1.3% | -1.7 | OPEN |
| 2026-07-31 | ROP | BLOCKED | REPAIR | 391.97 | 394.53 | 3 | +0.7% | -2.4 | OPEN |
| 2026-07-31 | SFM | BLOCKED | REPAIR | 87.16 | 85.12 | 3 | -2.3% | -5.4 | OPEN |
| 2026-07-31 | SHAK | BLOCKED | DEEP-FAIL | 62.75 | 74.33 | 3 | +18.4% | +15.4 | OPEN |
| 2026-07-31 | SHW | BLOCKED | REPAIR | 340.85 | 369.68 | 3 | +8.5% | +5.4 | OPEN |
| 2026-07-31 | SKYY | BLOCKED | PASS | 143.0 | 153.48 | 3 | +7.3% | +4.3 | OPEN |
| 2026-07-31 | SSD | BLOCKED | REPAIR | 187.74 | 197.35 | 3 | +5.1% | +2.1 | OPEN |
| 2026-07-31 | TOST | BLOCKED | REPAIR | 32.27 | 34.8 | 3 | +7.8% | +4.8 | OPEN |
| 2026-07-31 | TPR | BLOCKED | PASS | 152.37 | 159.16 | 3 | +4.5% | +1.4 | OPEN |
| 2026-07-31 | TYL | BLOCKED | DEEP-FAIL | 309.6 | 306.58 | 3 | -1.0% | -4.0 | OPEN |
| 2026-07-31 | XLY | BLOCKED | REPAIR | 116.09 | 118.64 | 3 | +2.2% | -0.8 | OPEN |
| 2026-07-31 | ZTS | BLOCKED | DEEP-FAIL | 77.29 | 74.39 | 3 | -3.8% | -6.8 | OPEN |
| 2026-07-31 | CTS | PASSED | PASS | 64.12 | 66.78 | 3 | +4.2% | +1.1 | OPEN |
| 2026-07-31 | FIVN | PASSED | PASS | 27.51 | 29.6 | 3 | +7.6% | +4.5 | OPEN |
| 2026-07-31 | GE | PASSED | PASS | 360.07 | 381.22 | 3 | +5.9% | +2.8 | OPEN |
| 2026-07-31 | KDP | PASSED | PASS | 31.12 | 30.75 | 3 | -1.2% | -4.2 | OPEN |
| 2026-07-31 | RACE | PASSED | REPAIR | 393.87 | 406.8 | 3 | +3.3% | +0.2 | OPEN |
| 2026-07-31 | ST | PASSED | REPAIR | 46.29 | 47.59 | 3 | +2.8% | -0.2 | OPEN |
| 2026-07-31 | TJX | PASSED | PASS | 157.34 | 159.92 | 3 | +1.6% | -1.4 | OPEN |
| 2026-07-31 | VRSN | PASSED | REPAIR | 290.02 | 293.41 | 3 | +1.2% | -1.9 | OPEN |
| 2026-08-03 | ABNB | BLOCKED | PASS | 150.64 | 152.49 | 2 | +1.2% | -0.4 | OPEN |
| 2026-08-03 | ACGL | BLOCKED | PASS | 101.12 | 99.09 | 2 | -2.0% | -3.6 | OPEN |
| 2026-08-03 | AGNC | BLOCKED | REPAIR | 10.64 | 10.67 | 2 | +0.3% | -1.3 | OPEN |
| 2026-08-03 | AI | BLOCKED | DEEP-FAIL | 9.73 | 9.91 | 2 | +1.9% | +0.2 | OPEN |
| 2026-08-03 | AJG | BLOCKED | REPAIR | 247.79 | 251.03 | 2 | +1.3% | -0.3 | OPEN |
| 2026-08-03 | AMZN | BLOCKED | PASS | 284.02 | 272.65 | 2 | -4.0% | -5.6 | OPEN |
| 2026-08-03 | APD | BLOCKED | PASS | 292.94 | 295.09 | 2 | +0.7% | -0.9 | OPEN |
| 2026-08-03 | APH | BLOCKED | PASS | 163.34 | 172.24 | 2 | +5.5% | +3.9 | OPEN |
| 2026-08-03 | AXON | BLOCKED | REPAIR | 575.88 | 609.49 | 2 | +5.8% | +4.2 | OPEN |
| 2026-08-03 | BABA | BLOCKED | REPAIR | 127.3 | 128.53 | 2 | +1.0% | -0.6 | OPEN |
| 2026-08-03 | CHTR | BLOCKED | DEEP-FAIL | 144.1 | 153.17 | 2 | +6.3% | +4.7 | OPEN |
| 2026-08-03 | CLX | BLOCKED | REPAIR | 98.26 | 105.84 | 2 | +7.7% | +6.1 | OPEN |
| 2026-08-03 | COKE | BLOCKED | PASS | 180.76 | 184.74 | 2 | +2.2% | +0.6 | OPEN |
| 2026-08-03 | CPRT | BLOCKED | DEEP-FAIL | 29.35 | 28.91 | 2 | -1.5% | -3.1 | OPEN |
| 2026-08-03 | CRWD | BLOCKED | PASS | 202.54 | 209.86 | 2 | +3.6% | +2.0 | OPEN |
| 2026-08-03 | CTM | BLOCKED | DEEP-FAIL | 0.74 | 0.79 | 2 | +7.0% | +5.3 | OPEN |
| 2026-08-03 | DASH | BLOCKED | REPAIR | 200.5 | 207.27 | 2 | +3.4% | +1.8 | OPEN |
| 2026-08-03 | DGII | BLOCKED | PASS | 70.4 | 72.75 | 2 | +3.3% | +1.7 | OPEN |
| 2026-08-03 | DOW | BLOCKED | PASS | 29.89 | 29.67 | 2 | -0.7% | -2.3 | OPEN |
| 2026-08-03 | EME | BLOCKED | REPAIR | 817.42 | 822.16 | 2 | +0.6% | -1.0 | OPEN |
| 2026-08-03 | EMN | BLOCKED | PASS | 71.98 | 73.35 | 2 | +1.9% | +0.3 | OPEN |
| 2026-08-03 | ERIE | BLOCKED | REPAIR | 236.86 | 250.79 | 2 | +5.9% | +4.3 | OPEN |
| 2026-08-03 | ETN | BLOCKED | PASS | 438.23 | 447.28 | 2 | +2.1% | +0.5 | OPEN |
| 2026-08-03 | FIVN | BLOCKED | PASS | 28.95 | 29.6 | 2 | +2.2% | +0.7 | OPEN |
| 2026-08-03 | FSLR | BLOCKED | REPAIR | 232.73 | 236.8 | 2 | +1.8% | +0.1 | OPEN |
| 2026-08-03 | GOOG | BLOCKED | PASS | 372.47 | 360.13 | 2 | -3.3% | -4.9 | OPEN |
| 2026-08-03 | GRND | BLOCKED | PASS | 17.9 | 17.78 | 2 | -0.7% | -2.3 | OPEN |
| 2026-08-03 | HD | BLOCKED | REPAIR | 340.02 | 353.14 | 2 | +3.9% | +2.3 | OPEN |
| 2026-08-03 | IBM | BLOCKED | DEEP-FAIL | 226.31 | 235.92 | 2 | +4.2% | +2.6 | OPEN |
| 2026-08-03 | IGV | BLOCKED | REPAIR | 97.42 | 101.31 | 2 | +4.0% | +2.4 | OPEN |
| 2026-08-03 | JBLU | BLOCKED | PASS | 6.23 | 6.36 | 2 | +2.1% | +0.5 | OPEN |
| 2026-08-03 | KWEB | BLOCKED | REPAIR | 28.74 | 28.54 | 2 | -0.7% | -2.3 | OPEN |
| 2026-08-03 | LOW | BLOCKED | DEEP-FAIL | 212.06 | 219.94 | 2 | +3.7% | +2.1 | OPEN |
| 2026-08-03 | LYV | BLOCKED | PASS | 181.69 | 183.52 | 2 | +1.0% | -0.6 | OPEN |
| 2026-08-03 | LZB | BLOCKED | PASS | 41.0 | 41.45 | 2 | +1.1% | -0.5 | OPEN |
| 2026-08-03 | MAMA | BLOCKED | PASS | 18.89 | 18.25 | 2 | -3.4% | -5.0 | OPEN |
| 2026-08-03 | MCD | BLOCKED | REPAIR | 265.23 | 274.0 | 2 | +3.3% | +1.7 | OPEN |
| 2026-08-03 | MLAB | BLOCKED | PASS | 104.43 | 102.62 | 2 | -1.7% | -3.3 | OPEN |
| 2026-08-03 | MSFT | BLOCKED | REPAIR | 487.65 | 487.46 | 2 | -0.0% | -1.6 | OPEN |
| 2026-08-03 | NCLH | BLOCKED | REPAIR | 19.76 | 20.3 | 2 | +2.7% | +1.1 | OPEN |
| 2026-08-03 | NFLX | BLOCKED | DEEP-FAIL | 73.33 | 74.2 | 2 | +1.2% | -0.4 | OPEN |
| 2026-08-03 | NIO | BLOCKED | DEEP-FAIL | 4.81 | 4.65 | 2 | -3.3% | -4.9 | OPEN |
| 2026-08-03 | NOW | BLOCKED | REPAIR | 114.19 | 117.22 | 2 | +2.6% | +1.1 | OPEN |
| 2026-08-03 | ORCL | BLOCKED | DEEP-FAIL | 141.85 | 144.39 | 2 | +1.8% | +0.2 | OPEN |
| 2026-08-03 | PEP | BLOCKED | REPAIR | 139.63 | 138.78 | 2 | -0.6% | -2.2 | OPEN |
| 2026-08-03 | PGR | BLOCKED | REPAIR | 210.46 | 212.76 | 2 | +1.1% | -0.5 | OPEN |
| 2026-08-03 | PWR | BLOCKED | REPAIR | 680.2 | 682.99 | 2 | +0.4% | -1.2 | OPEN |
| 2026-08-03 | RMD | BLOCKED | REPAIR | 215.19 | 224.03 | 2 | +4.1% | +2.5 | OPEN |
| 2026-08-03 | ROKU | BLOCKED | PASS | 145.84 | 146.96 | 2 | +0.8% | -0.8 | OPEN |
| 2026-08-03 | S | BLOCKED | PASS | 20.05 | 21.0 | 2 | +4.7% | +3.1 | OPEN |
| 2026-08-03 | SFM | BLOCKED | REPAIR | 88.81 | 85.12 | 2 | -4.2% | -5.8 | OPEN |
| 2026-08-03 | SHAK | BLOCKED | DEEP-FAIL | 64.78 | 74.33 | 2 | +14.7% | +13.1 | OPEN |
| 2026-08-03 | SKYY | BLOCKED | PASS | 147.98 | 153.48 | 2 | +3.7% | +2.1 | OPEN |
| 2026-08-03 | SPXL | BLOCKED | PASS | 279.68 | 292.85 | 2 | +4.7% | +3.1 | OPEN |
| 2026-08-03 | SYM | BLOCKED | DEEP-FAIL | 45.85 | 46.52 | 2 | +1.5% | -0.1 | OPEN |
| 2026-08-03 | TOST | BLOCKED | REPAIR | 32.79 | 34.8 | 2 | +6.1% | +4.5 | OPEN |
| 2026-08-03 | TPR | BLOCKED | PASS | 155.63 | 159.16 | 2 | +2.3% | +0.7 | OPEN |
| 2026-08-03 | TYL | BLOCKED | DEEP-FAIL | 305.54 | 306.58 | 2 | +0.3% | -1.3 | OPEN |
| 2026-08-03 | WRBY | BLOCKED | PASS | 28.28 | 29.27 | 2 | +3.5% | +1.9 | OPEN |
| 2026-08-03 | XLY | BLOCKED | REPAIR | 118.21 | 118.64 | 2 | +0.4% | -1.2 | OPEN |
| 2026-08-03 | ZTS | BLOCKED | DEEP-FAIL | 77.1 | 74.39 | 2 | -3.5% | -5.1 | OPEN |
| 2026-08-03 | AMG | PASSED | PASS | 380.89 | 375.62 | 2 | -1.4% | -3.0 | OPEN |
| 2026-08-03 | CCL | PASSED | REPAIR | 28.74 | 29.67 | 2 | +3.2% | +1.6 | OPEN |
| 2026-08-03 | CMG | PASSED | REPAIR | 37.46 | 34.5 | 2 | -7.9% | -9.5 | OPEN |
| 2026-08-03 | CTS | PASSED | PASS | 65.23 | 66.78 | 2 | +2.4% | +0.8 | OPEN |
| 2026-08-03 | DAL | PASSED | PASS | 91.59 | 93.14 | 2 | +1.7% | +0.1 | OPEN |
| 2026-08-03 | DUOL | PASSED | REPAIR | 135.8 | 135.32 | 2 | -0.3% | -1.9 | OPEN |
| 2026-08-03 | JETS | PASSED | PASS | 32.67 | 33.53 | 2 | +2.6% | +1.0 | OPEN |
| 2026-08-03 | KDP | PASSED | PASS | 30.91 | 30.75 | 2 | -0.5% | -2.1 | OPEN |
| 2026-08-03 | MDT | PASSED | REPAIR | 86.68 | 85.99 | 2 | -0.8% | -2.4 | OPEN |
| 2026-08-03 | MIDD | PASSED | PASS | 135.81 | 135.34 | 2 | -0.3% | -1.9 | OPEN |
| 2026-08-03 | PLPC | PASSED | REPAIR | 358.15 | 471.29 | 2 | +31.6% | +30.0 | OPEN |
| 2026-08-03 | RACE | PASSED | REPAIR | 401.28 | 406.8 | 2 | +1.4% | -0.2 | OPEN |
| 2026-08-03 | RCL | PASSED | REPAIR | 324.0 | 327.42 | 2 | +1.1% | -0.5 | OPEN |
| 2026-08-03 | SHW | PASSED | REPAIR | 354.22 | 369.68 | 2 | +4.4% | +2.8 | OPEN |
| 2026-08-03 | SSD | PASSED | REPAIR | 192.17 | 197.35 | 2 | +2.7% | +1.1 | OPEN |
| 2026-08-03 | ST | PASSED | REPAIR | 46.82 | 47.59 | 2 | +1.6% | +0.0 | OPEN |
| 2026-08-03 | TJX | PASSED | PASS | 157.5 | 159.92 | 2 | +1.5% | -0.1 | OPEN |
| 2026-08-03 | UAL | PASSED | PASS | 128.39 | 132.76 | 2 | +3.4% | +1.8 | OPEN |
| 2026-08-03 | VRSN | PASSED | REPAIR | 298.89 | 293.41 | 2 | -1.8% | -3.4 | OPEN |
| 2026-08-04 | AAL | BLOCKED | PASS | 16.56 | 16.58 | 1 | +0.1% | +0.3 | OPEN |
| 2026-08-04 | ABNB | BLOCKED | PASS | 149.92 | 152.49 | 1 | +1.7% | +1.9 | OPEN |
| 2026-08-04 | AGNC | BLOCKED | REPAIR | 10.64 | 10.67 | 1 | +0.3% | +0.5 | OPEN |
| 2026-08-04 | AI | BLOCKED | DEEP-FAIL | 10.05 | 9.91 | 1 | -1.4% | -1.2 | OPEN |
| 2026-08-04 | AJG | BLOCKED | REPAIR | 248.06 | 251.03 | 1 | +1.2% | +1.4 | OPEN |
| 2026-08-04 | APD | BLOCKED | PASS | 294.71 | 295.09 | 1 | +0.1% | +0.3 | OPEN |
| 2026-08-04 | APEI | BLOCKED | REPAIR | 53.42 | 53.82 | 1 | +0.8% | +0.9 | OPEN |
| 2026-08-04 | APH | BLOCKED | PASS | 171.33 | 172.24 | 1 | +0.5% | +0.7 | OPEN |
| 2026-08-04 | ASB | BLOCKED | PASS | 31.75 | 31.53 | 1 | -0.7% | -0.5 | OPEN |
| 2026-08-04 | ASTS | BLOCKED | DEEP-FAIL | 70.31 | 68.38 | 1 | -2.7% | -2.5 | OPEN |
| 2026-08-04 | AXON | BLOCKED | REPAIR | 607.2 | 609.49 | 1 | +0.4% | +0.6 | OPEN |
| 2026-08-04 | BA | BLOCKED | PASS | 237.16 | 240.19 | 1 | +1.3% | +1.5 | OPEN |
| 2026-08-04 | BABA | BLOCKED | REPAIR | 128.99 | 128.53 | 1 | -0.4% | -0.2 | OPEN |
| 2026-08-04 | BLMN | BLOCKED | PASS | 8.92 | 11.85 | 1 | +32.9% | +33.0 | OPEN |
| 2026-08-04 | BOTZ | BLOCKED | REPAIR | 37.09 | 37.3 | 1 | +0.6% | +0.8 | OPEN |
| 2026-08-04 | CAT | BLOCKED | REPAIR | 876.54 | 871.08 | 1 | -0.6% | -0.4 | OPEN |
| 2026-08-04 | CCJ | BLOCKED | DEEP-FAIL | 93.09 | 94.27 | 1 | +1.3% | +1.5 | OPEN |
| 2026-08-04 | CENX | BLOCKED | REPAIR | 47.12 | 46.9 | 1 | -0.5% | -0.3 | OPEN |
| 2026-08-04 | CHTR | BLOCKED | DEEP-FAIL | 153.07 | 153.17 | 1 | +0.1% | +0.3 | OPEN |
| 2026-08-04 | CLX | BLOCKED | REPAIR | 104.67 | 105.84 | 1 | +1.1% | +1.3 | OPEN |
| 2026-08-04 | CMG | BLOCKED | REPAIR | 33.82 | 34.5 | 1 | +2.0% | +2.2 | OPEN |
| 2026-08-04 | COKE | BLOCKED | REPAIR | 181.0 | 184.74 | 1 | +2.1% | +2.3 | OPEN |
| 2026-08-04 | CRWD | BLOCKED | PASS | 211.22 | 209.86 | 1 | -0.6% | -0.4 | OPEN |
| 2026-08-04 | CRWV | BLOCKED | REPAIR | 91.9 | 89.89 | 1 | -2.2% | -2.0 | OPEN |
| 2026-08-04 | CTM | BLOCKED | DEEP-FAIL | 0.79 | 0.79 | 1 | -0.6% | -0.4 | OPEN |
| 2026-08-04 | CVNA | BLOCKED | REPAIR | 68.03 | 69.48 | 1 | +2.1% | +2.3 | OPEN |
| 2026-08-04 | DASH | BLOCKED | REPAIR | 202.37 | 207.27 | 1 | +2.4% | +2.6 | OPEN |
| 2026-08-04 | DAVE | BLOCKED | PASS | 429.26 | 430.16 | 1 | +0.2% | +0.4 | OPEN |
| 2026-08-04 | DGII | BLOCKED | PASS | 72.14 | 72.75 | 1 | +0.8% | +1.1 | OPEN |
| 2026-08-04 | DOW | BLOCKED | PASS | 30.33 | 29.67 | 1 | -2.2% | -2.0 | OPEN |
| 2026-08-04 | DUOL | BLOCKED | REPAIR | 137.75 | 135.32 | 1 | -1.8% | -1.6 | OPEN |
| 2026-08-04 | EMN | BLOCKED | PASS | 73.9 | 73.35 | 1 | -0.7% | -0.5 | OPEN |
| 2026-08-04 | ETN | BLOCKED | PASS | 444.77 | 447.28 | 1 | +0.6% | +0.8 | OPEN |
| 2026-08-04 | FFIV | BLOCKED | PASS | 412.25 | 411.32 | 1 | -0.2% | -0.0 | OPEN |
| 2026-08-04 | FSLR | BLOCKED | REPAIR | 243.63 | 236.8 | 1 | -2.8% | -2.6 | OPEN |
| 2026-08-04 | FTDR | BLOCKED | PASS | 76.75 | 76.38 | 1 | -0.5% | -0.3 | OPEN |
| 2026-08-04 | GOOG | BLOCKED | PASS | 375.35 | 360.13 | 1 | -4.0% | -3.9 | OPEN |
| 2026-08-04 | HD | BLOCKED | REPAIR | 348.24 | 353.14 | 1 | +1.4% | +1.6 | OPEN |
| 2026-08-04 | HIMX | BLOCKED | REPAIR | 14.18 | 13.35 | 1 | -5.8% | -5.7 | OPEN |
| 2026-08-04 | IBM | BLOCKED | DEEP-FAIL | 235.15 | 235.92 | 1 | +0.3% | +0.5 | OPEN |
| 2026-08-04 | IGV | BLOCKED | REPAIR | 102.0 | 101.31 | 1 | -0.7% | -0.5 | OPEN |
| 2026-08-04 | INOD | BLOCKED | REPAIR | 70.21 | 69.37 | 1 | -1.2% | -1.0 | OPEN |
| 2026-08-04 | JBLU | BLOCKED | PASS | 6.41 | 6.36 | 1 | -0.8% | -0.6 | OPEN |
| 2026-08-04 | KDP | BLOCKED | REPAIR | 31.1 | 30.75 | 1 | -1.1% | -0.9 | OPEN |
| 2026-08-04 | KWEB | BLOCKED | REPAIR | 28.89 | 28.54 | 1 | -1.2% | -1.0 | OPEN |
| 2026-08-04 | LAES | BLOCKED | DEEP-FAIL | 2.54 | 2.46 | 1 | -3.1% | -3.0 | OPEN |
| 2026-08-04 | LOW | BLOCKED | DEEP-FAIL | 218.08 | 219.94 | 1 | +0.8% | +1.1 | OPEN |
| 2026-08-04 | LUNR | BLOCKED | DEEP-FAIL | 13.96 | 13.99 | 1 | +0.2% | +0.4 | OPEN |
| 2026-08-04 | LYV | BLOCKED | PASS | 183.7 | 183.52 | 1 | -0.1% | +0.1 | OPEN |
| 2026-08-04 | MCD | BLOCKED | DEEP-FAIL | 268.34 | 274.0 | 1 | +2.1% | +2.3 | OPEN |
| 2026-08-04 | MDT | BLOCKED | REPAIR | 86.2 | 85.99 | 1 | -0.2% | -0.0 | OPEN |
| 2026-08-04 | MLAB | BLOCKED | PASS | 101.14 | 102.62 | 1 | +1.5% | +1.7 | OPEN |
| 2026-08-04 | MP | BLOCKED | DEEP-FAIL | 47.47 | 47.91 | 1 | +0.9% | +1.1 | OPEN |
| 2026-08-04 | MSFT | BLOCKED | REPAIR | 492.81 | 487.46 | 1 | -1.1% | -0.9 | OPEN |
| 2026-08-04 | MTCH | BLOCKED | PASS | 41.24 | 38.15 | 1 | -7.5% | -7.3 | OPEN |
| 2026-08-04 | NCLH | BLOCKED | REPAIR | 20.07 | 20.3 | 1 | +1.1% | +1.4 | OPEN |
| 2026-08-04 | NFLX | BLOCKED | DEEP-FAIL | 73.57 | 74.2 | 1 | +0.9% | +1.1 | OPEN |
| 2026-08-04 | NIO | BLOCKED | DEEP-FAIL | 4.76 | 4.65 | 1 | -2.3% | -2.1 | OPEN |
| 2026-08-04 | NOVT | BLOCKED | PASS | 159.49 | 153.12 | 1 | -4.0% | -3.8 | OPEN |
| 2026-08-04 | NOW | BLOCKED | REPAIR | 118.14 | 117.22 | 1 | -0.8% | -0.6 | OPEN |
| 2026-08-04 | NVDA | BLOCKED | PASS | 211.94 | 219.22 | 1 | +3.4% | +3.6 | OPEN |
| 2026-08-04 | OPY | BLOCKED | PASS | 116.91 | 115.92 | 1 | -0.8% | -0.7 | OPEN |
| 2026-08-04 | ORCL | BLOCKED | DEEP-FAIL | 145.74 | 144.39 | 1 | -0.9% | -0.7 | OPEN |
| 2026-08-04 | PANW | BLOCKED | PASS | 366.34 | 362.66 | 1 | -1.0% | -0.8 | OPEN |
| 2026-08-04 | PEP | BLOCKED | REPAIR | 139.1 | 138.78 | 1 | -0.2% | -0.0 | OPEN |
| 2026-08-04 | PL | BLOCKED | DEEP-FAIL | 22.83 | 22.35 | 1 | -2.1% | -1.9 | OPEN |
| 2026-08-04 | PLPC | BLOCKED | PASS | 423.6 | 471.29 | 1 | +11.3% | +11.5 | OPEN |
| 2026-08-04 | PLTR | BLOCKED | REPAIR | 162.66 | 158.43 | 1 | -2.6% | -2.4 | OPEN |
| 2026-08-04 | PWR | BLOCKED | PASS | 693.0 | 682.99 | 1 | -1.4% | -1.2 | OPEN |
| 2026-08-04 | RGTI | BLOCKED | DEEP-FAIL | 17.45 | 16.78 | 1 | -3.8% | -3.6 | OPEN |
| 2026-08-04 | RKLB | BLOCKED | REPAIR | 74.48 | 74.82 | 1 | +0.5% | +0.7 | OPEN |
| 2026-08-04 | ROKU | BLOCKED | PASS | 147.33 | 146.96 | 1 | -0.2% | -0.1 | OPEN |
| 2026-08-04 | SE | BLOCKED | REPAIR | 111.44 | 114.91 | 1 | +3.1% | +3.3 | OPEN |
| 2026-08-04 | SEZL | BLOCKED | PASS | 177.23 | 174.4 | 1 | -1.6% | -1.4 | OPEN |
| 2026-08-04 | SHAK | BLOCKED | DEEP-FAIL | 66.22 | 74.33 | 1 | +12.2% | +12.4 | OPEN |
| 2026-08-04 | SMR | BLOCKED | DEEP-FAIL | 9.49 | 9.38 | 1 | -1.2% | -1.0 | OPEN |
| 2026-08-04 | SOFI | BLOCKED | DEEP-FAIL | 18.7 | 18.25 | 1 | -2.4% | -2.2 | OPEN |
| 2026-08-04 | SPXL | BLOCKED | PASS | 294.56 | 292.85 | 1 | -0.6% | -0.4 | OPEN |
| 2026-08-04 | SXI | BLOCKED | PASS | 322.72 | 326.45 | 1 | +1.2% | +1.4 | OPEN |
| 2026-08-04 | SYM | BLOCKED | DEEP-FAIL | 47.46 | 46.52 | 1 | -2.0% | -1.8 | OPEN |
| 2026-08-04 | TOST | BLOCKED | REPAIR | 33.81 | 34.8 | 1 | +2.9% | +3.1 | OPEN |
| 2026-08-04 | TPR | BLOCKED | PASS | 155.97 | 159.16 | 1 | +2.0% | +2.2 | OPEN |
| 2026-08-04 | TSLA | BLOCKED | DEEP-FAIL | 327.35 | 321.55 | 1 | -1.8% | -1.6 | OPEN |
| 2026-08-04 | TWST | BLOCKED | PASS | 99.45 | 115.01 | 1 | +15.7% | +15.8 | OPEN |
| 2026-08-04 | TYL | BLOCKED | DEEP-FAIL | 313.33 | 306.58 | 1 | -2.1% | -1.9 | OPEN |
| 2026-08-04 | VISN | BLOCKED | DEEP-FAIL | 12.49 | 12.35 | 1 | -1.1% | -0.9 | OPEN |
| 2026-08-04 | VSAT | BLOCKED | PASS | 86.16 | 81.03 | 1 | -6.0% | -5.8 | OPEN |
| 2026-08-04 | VSEC | BLOCKED | PASS | 214.23 | 215.75 | 1 | +0.7% | +0.9 | OPEN |
| 2026-08-04 | WMS | BLOCKED | PASS | 149.75 | 149.59 | 1 | -0.1% | +0.1 | OPEN |
| 2026-08-04 | WRBY | BLOCKED | PASS | 29.92 | 29.27 | 1 | -2.2% | -2.0 | OPEN |
| 2026-08-04 | XLI | BLOCKED | PASS | 186.4 | 186.35 | 1 | -0.0% | +0.2 | OPEN |
| 2026-08-04 | XLY | BLOCKED | REPAIR | 118.29 | 118.64 | 1 | +0.3% | +0.5 | OPEN |
| 2026-08-04 | ZTS | BLOCKED | DEEP-FAIL | 76.04 | 74.39 | 1 | -2.2% | -2.0 | OPEN |
| 2026-08-04 | AMG | PASSED | PASS | 383.42 | 375.62 | 1 | -2.0% | -1.8 | OPEN |
| 2026-08-04 | AMZN | PASSED | PASS | 277.42 | 272.65 | 1 | -1.7% | -1.5 | OPEN |
| 2026-08-04 | CCL | PASSED | REPAIR | 29.59 | 29.67 | 1 | +0.3% | +0.5 | OPEN |
| 2026-08-04 | CSCO | PASSED | PASS | 121.74 | 121.5 | 1 | -0.2% | +0.0 | OPEN |
| 2026-08-04 | CTS | PASSED | PASS | 67.26 | 66.78 | 1 | -0.7% | -0.5 | OPEN |
| 2026-08-04 | DAL | PASSED | PASS | 92.77 | 93.14 | 1 | +0.4% | +0.6 | OPEN |
| 2026-08-04 | EME | PASSED | PASS | 819.88 | 822.16 | 1 | +0.3% | +0.5 | OPEN |
| 2026-08-04 | ERIE | PASSED | REPAIR | 244.53 | 250.79 | 1 | +2.6% | +2.8 | OPEN |
| 2026-08-04 | HSIC | PASSED | PASS | 89.11 | 89.59 | 1 | +0.5% | +0.7 | OPEN |
| 2026-08-04 | IWM | PASSED | PASS | 301.71 | 299.77 | 1 | -0.6% | -0.4 | OPEN |
| 2026-08-04 | JETS | PASSED | PASS | 33.4 | 33.53 | 1 | +0.4% | +0.6 | OPEN |
| 2026-08-04 | LUV | PASSED | PASS | 48.7 | 48.79 | 1 | +0.2% | +0.4 | OPEN |
| 2026-08-04 | MATX | PASSED | PASS | 213.44 | 205.51 | 1 | -3.7% | -3.5 | OPEN |
| 2026-08-04 | QQQ | PASSED | PASS | 723.85 | 717.3 | 1 | -0.9% | -0.7 | OPEN |
| 2026-08-04 | RACE | PASSED | REPAIR | 402.79 | 406.8 | 1 | +1.0% | +1.2 | OPEN |
| 2026-08-04 | RMD | PASSED | REPAIR | 223.14 | 224.03 | 1 | +0.4% | +0.6 | OPEN |
| 2026-08-04 | ROBO | PASSED | PASS | 84.34 | 84.37 | 1 | +0.0% | +0.2 | OPEN |
| 2026-08-04 | SFM | PASSED | REPAIR | 86.07 | 85.12 | 1 | -1.1% | -0.9 | OPEN |
| 2026-08-04 | SHW | PASSED | REPAIR | 361.57 | 369.68 | 1 | +2.2% | +2.4 | OPEN |
| 2026-08-04 | SKYY | PASSED | PASS | 153.43 | 153.48 | 1 | +0.0% | +0.2 | OPEN |
| 2026-08-04 | ST | PASSED | PASS | 48.66 | 47.59 | 1 | -2.2% | -2.0 | OPEN |
| 2026-08-04 | UAL | PASSED | PASS | 132.62 | 132.76 | 1 | +0.1% | +0.3 | OPEN |
| 2026-08-04 | XLK | PASSED | PASS | 186.9 | 185.91 | 1 | -0.5% | -0.3 | OPEN |

Open marks are not results. This file exists so that the cull the scan performs every night is measured instead of assumed.
