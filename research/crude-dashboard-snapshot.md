# Crude Fundamental Dashboard - snapshot for the morning-brief writer
Source workbook: Crude_Fundamental_Dashboard (2).xlsx | model as-of: 2026-07-20
This is Omar's own fair-value model (weekly refresh). The daily brief
re-sources these metrics fresh each morning and reports where the
MARKET has moved vs this baseline. Stale vs fresh must be labeled.

## Fair-value signals (Dashboard tab)
| Instrument | Market | Fair Value | Mispricing | Signal | Threshold |
|---|--:|--:|--:|---|--:|
| WTI Front Month vs Second Month (M1-M2) | 0.68 | 6.65 | -5.97 | LONG spread (cheap) | 0.25 |
| Brent Front Month vs Second Month (M1-M2) | 0.9 | 3.5 | -2.6 | LONG spread (cheap) | 0.3 |
| WTI minus Brent (inter-grade) | -5.42 | -16.55 | 11.13 | SHORT spread (rich) | 0.5 |

### Key model drivers
- Cushing Z-score (52-week): **-2** (Below -1 = tight; above +1 = oversupplied)
- Cushing capacity utilization: **0.26** (Above 85% = tank tops squeeze contango wider; below 35% = squeeze risk)
- OECD commercial inventory Z-score: **-4.4** (Below -1 = global tightness)
- OPEC+ effective spare capacity (MMbpd): **1.5** (Below 2.5 = stressed; normal is 4-5)
- Full carry cost (WTI): **0.7** (Contango ceiling — sets the floor on M1-M2 spread)
- WTI backwardation depth (M1-M12): **8.28** (Structural tightness signal)
- Brent backwardation depth (M1-M12): **10.2** (Global structural tightness)

## Heavy-light differentials (fair value vs market)
| Grade | Market | FV | Mispricing | Signal |
|---|--:|--:|--:|---|
| ASCI (Argus Sour Crude Index) | -3.4 | 0.55 | -3.95 | LONG diff (cheap) |
| WCS (Western Canadian Select) | -13 | -8.4 | -4.6 | LONG diff (cheap) |
| Maya (Mexican heavy crude) | -8 | -4.43 | -3.57 | LONG diff (cheap) |
| Mars (USGC medium sour) | 2.5 | 0.53 | 1.97 | SHORT diff (rich) |
| SGC (Southern Green Canyon — Gulf medium) | -3.8 | 0.15 | -3.95 | LONG diff (cheap) |

## East-West arb
- Brent minus Dubai EFS (Exchange of Futures for Swaps): **2.2** (FV 1.94, FAIR)
- Dubai geopolitical premium: **4.2** (Hormuz / Mideast risk lever)
- Aramco Official Selling Price signal (Asia diff): **1.2** (Positive = aggressive Aramco; negative = competing for share)

## Crack spreads (market vs FV)
| Crack | Market | FV | Mispricing | Signal | Region |
|---|--:|--:|--:|---|---|
| USGC 3-2-1 (gasoline + diesel from crude) | 41.89 | 20.69 | 21.19 | FAT (rich) | USGC |
| NWE 3-2-1 (Northwest Europe) | 33.73 | 12.1 | 21.63 | FAT (rich) | NWE |
| Singapore Gasoil minus Dubai | 16.8 | 14.38 | 2.42 | FAT (rich) | Asia |
| Singapore Complex Margin (refiner basket) | -10.92 | 6.18 | -17.1 | THIN (cheap) | Asia |

## Inventory tracker (WPSR week in model)
- US crude C+C: level 409,700 | WoW -1,600 | note: In line
- Cushing: level 20,040 | WoW 430 | note: Tank bottoms — BACKWARDATION
- US gasoline: level 222,000 | WoW -8,500 | note: BULLISH surprise
- US distillate: level 108,200 | WoW 4,560 | note: BEARISH surprise
- US SPR: level 316,500 | WoW -2,980 | note: Drawing
- Days of US cover: level 20.08 | WoW days | note: n/a

### Floating storage by origin (kbbl)
- Iran: 72,000 (WoW 4,000, vs 5yr 22,000) VERY HIGH — major overhang
- Russia: 18,000 (WoW -1,500, vs 5yr -4,000) Below avg
- China: 12,000 (WoW 500, vs 5yr —) —
- Other: 35,000 (WoW 500, vs 5yr —) —

## Demand engine composites (triangulated)
| Data point | Composite | Confidence |
|---|--:|---|
| China total refinery throughput (kbpd) | 14,435 | HIGH |
| China crude imports (kbpd) | 11,252.5 | MEDIUM |
| India crude imports (kbpd) | 5,293.5 | HIGH |
| China Shandong teapot run rate (%) | 61.7 | HIGH |
| OPEC total crude production (MMbpd) | 27.61 | MEDIUM |
| Saudi Arabia crude production (MMbpd) | 9.03 | MEDIUM |
| Iran crude exports (kbpd) | 1,670 | MEDIUM |
| Russia crude exports (post-sanctions) (kbpd) | 4,867.5 | HIGH |
| Global jet fuel demand (MMbpd) | 7.18 | MEDIUM |
| Global floating storage (crude) (MMbbl) | 88.45 | HIGH |
| US gasoline demand (MMbpd) | 9.04 | HIGH |

## Aramco OSP model
- Arab Light: current 1.65 -> predicted 2.14 (RAISE expected, conviction MEDIUM)
- Arab Medium: current 1.1 -> predicted 1.47 (RAISE expected, conviction MEDIUM)
- Arab Heavy: current 0.5 -> predicted 0.66 (Modest raise, conviction LOW)

## Trade signal thresholds (Methodology tab)
WTI M1-M2 +/-$0.25 | Brent M1-M2 +/-$0.30 | WTI-Brent +/-$0.50 -
mispricing outside the band = model sees an edge; inside = no edge.

## Triangulation discipline (carry into the brief)
Source tiers: T1 satellite/AIS (Kpler, Vortexa, Kayrros, Cirium, TSA)
> T2 official aggregations (IEA, IATA, PPAC, EIA STEO) > T3 surveys
(JLC teapots, OPEC MOMR secondary) > T4 cross-check only (China NBS).
When sources diverge materially, confidence is LOW - the dashboard's
rule is DO NOT TRADE on LOW-confidence data points; the brief should
flag them the same way.
