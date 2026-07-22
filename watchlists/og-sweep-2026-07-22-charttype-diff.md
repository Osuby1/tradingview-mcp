# Chart-type disagreement: candles vs Heikin Ashi

**Written at** 2026-07-22 10:30 local  
**Symbols compared** 155

## Headline

- BUY/SELL mode disagrees on **34/155** names (22%)
- flip DATE disagrees on **111/155** names (72%)
- Magical median absolute difference **14.0**, max **63.0**
- Magical alone flips the too-hot verdict on **3** names

## Mode disagreements (candles -> HA)

| Sym | Candles | Heikin Ashi |
|---|---|---|
| BCBP | BUY | SELL |
| CAR | BUY | SELL |
| CENX | BUY | SELL |
| CLX | BUY | SELL |
| CRWD | SELL | BUY |
| CRWV | BUY | SELL |
| CVNA | SELL | BUY |
| DE | BUY | SELL |
| DFDV | BUY | SELL |
| DIS | BUY | SELL |
| FHB | BUY | SELL |
| FLEX | BUY | SELL |
| GD | SELL | BUY |
| GOOG | SELL | BUY |
| GS | SELL | BUY |
| HTZ | BUY | SELL |
| IGV | SELL | BUY |
| IWM | SELL | BUY |
| KO | SELL | BUY |
| MBLY | SELL | BUY |
| MU | BUY | SELL |
| NEE | SELL | BUY |
| NMAX | SELL | BUY |
| NTRS | SELL | BUY |
| PANW | SELL | BUY |
| RGTI | BUY | SELL |
| RIVN | SELL | BUY |
| RSPU | BUY | SELL |
| SOFI | SELL | BUY |
| SOUN | BUY | SELL |
| SOXL | BUY | SELL |
| SPXL | SELL | BUY |
| TGTX | SELL | BUY |
| UBER | SELL | BUY |

## Flip-date disagreements (63 of 111 are HA reporting LATER)

| Sym | Candles flip | HA flip | Who lags | Bar delta |
|---|---|---|---|---|
| NTRS | 2026-07-22 | 2026-03-25 | candles later | +81 |
| PANW | 2026-07-22 | 2026-04-08 | candles later | +72 |
| HTZ | 2026-07-22 | 2026-05-18 | candles later | +44 |
| IWM | 2026-07-20 | 2026-05-26 | candles later | +37 |
| KRE | 2026-07-16 | 2026-05-22 | candles later | +36 |
| RGTI | 2026-07-22 | 2026-06-05 | candles later | +31 |
| TGTX | 2026-07-20 | 2026-06-04 | candles later | +30 |
| AMGN | 2026-07-16 | 2026-06-04 | candles later | +28 |
| CENX | 2026-07-22 | 2026-06-10 | candles later | +28 |
| SKK | 2026-07-20 | 2026-06-08 | candles later | +28 |
| QQQ | 2026-07-16 | 2026-06-05 | candles later | +27 |
| FUTU | 2026-06-15 | 2026-07-21 | HA later | -24 |
| AMCR | 2026-07-16 | 2026-06-11 | candles later | +23 |
| SOUN | 2026-07-06 | 2026-06-04 | candles later | +20 |
| CRWV | 2026-07-22 | 2026-06-24 | candles later | +19 |
| BCBP | 2026-07-16 | 2026-06-22 | candles later | +17 |
| UBER | 2026-07-22 | 2026-06-26 | candles later | +17 |
| CRWD | 2026-07-22 | 2026-06-29 | candles later | +16 |
| EVGO | 2026-07-17 | 2026-06-24 | candles later | +16 |
| IGV | 2026-07-22 | 2026-07-01 | candles later | +14 |
| KO | 2026-07-17 | 2026-06-26 | candles later | +14 |
| NMAX | 2026-07-22 | 2026-07-01 | candles later | +14 |
| SOFI | 2026-07-20 | 2026-06-29 | candles later | +14 |
| CLX | 2026-07-10 | 2026-06-22 | candles later | +13 |
| DFDV | 2026-06-29 | 2026-07-17 | HA later | -13 |
| SOXL | 2026-07-22 | 2026-07-02 | candles later | +13 |
| MU | 2026-07-21 | 2026-07-02 | candles later | +12 |
| DIS | 2026-07-16 | 2026-06-30 | candles later | +11 |
| LUNR | 2026-06-23 | 2026-06-05 | candles later | +11 |
| MBLY | 2026-07-16 | 2026-06-30 | candles later | +11 |
| MP | 2026-06-24 | 2026-06-08 | candles later | +11 |
| XLK | 2026-06-23 | 2026-06-05 | candles later | +11 |
| ARQT | 2026-05-26 | 2026-06-09 | HA later | -10 |
| FLEX | 2026-07-21 | 2026-07-07 | candles later | +10 |
| TSLA | 2026-07-02 | 2026-07-17 | HA later | -10 |
| DTE | 2026-07-01 | 2026-07-15 | HA later | -9 |
| GD | 2026-07-15 | 2026-07-01 | candles later | +9 |
| GOOG | 2026-07-17 | 2026-07-06 | candles later | +9 |
| INOD | 2026-06-09 | 2026-06-23 | HA later | -9 |
| SOXS | 2026-06-23 | 2026-07-07 | HA later | -9 |

## Names where Magical alone changes the gate verdict

| Sym | Magical candles | Magical HA |
|---|---|---|
| GDX | 104.6 | 70.9 |
| NVDA | 128.2 | 98.5 |
| SMCI | 147.2 | 84.2 |

## What this means

These are the SAME indicator on the SAME symbols at the SAME moment.
Every disagreement above is the chart-type setting alone. Whichever
type the system runs on must be fixed and recorded per run, and the
Magical thresholds must be recalibrated against THAT type - the two
are not interchangeable and mixing them invalidates the gate.
