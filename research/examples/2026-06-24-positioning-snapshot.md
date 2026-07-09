# POSITIONING & FLOW SNAPSHOT — 2026-06-24
Worked example of the [Positioning & Flow framework](../positioning-flow-framework.md) (Gap 3). Institutional "who's offside?" view.

## A) Futures positioning — CFTC COT (FREE; data as-of 2026-06-16, released 6/19)
Source: CFTC Socrata `6dca-aqww`. NYMEX/COMEX main contracts.

| Market | Large-Spec (Non-Comm) NET | Long | Short | W/W Δ | OI |
|---|---|---|---|---|---|
| **WTI Crude** | **+124,483** | 361,004 | 236,521 | **−5,818** | 2.01M |
| **Gold** | **+180,220** | 211,127 | 30,907 | **+6,383** | 339K |

- **WTI:** net long but **middling, bleeding two weeks** (−25,573 then −5,818). De-risking tape, no crowded blow-off → no strong contrarian signal; **no spec tailwind for energy** (MPC/BKR/PSX/VLO).
- **Gold:** **crowded net long** (longs 6.8x shorts; 62% of OI), still building → **contrarian caution** on GLD/GOLD; a flush is the surprise.

## B) Equity options / vol
**MU (reports tonight):** IV rank 100 (front weekly ~155%, ATM ~160%); expected move **±11% (±$132)**; term structure 155%→108%→102% = huge **event premium / IV-crush risk**; call OI ~2.7x put, call volume bias 1.6x = **bullish crowding** → a miss punished harder than a beat rewarded. **Edge is short-vol / IV-crush, not long-premium.**
**Energy (MPC/VLO):** clean free IV-rank source **not available** (Barchart/OptionCharts gated). Needs paid feed or manual screen — flagged, not estimated.

## C) Short interest / squeeze — RANKED (board has rotated since prior notes)
| Rank | Ticker | SI % Float | Days-to-Cover | vs prior note |
|---|---|---|---|---|
| **1** | **CHTR** | **~26%** ⚠️ | 6.7–11.6 | was 12.8% — **now ~double** |
| 2 | POWL | ~mid-teens–24% (small float) | ~5.6 | ≈ prior 9.5% |
| 3 | SFM | ~11–12% | ~5.0 | matches |
| 4 | NTAP | **~4%** ⚠️ | ~2.3–3.5 | was 10.9% — **collapsed** |
| 5 | ANF | **~8%** ⚠️ | ~1.6 | was 19.7% — **covered out** |

→ **Re-rank squeeze watch: CHTR > POWL > SFM. Retire NTAP & ANF** (data no longer supports). CHTR = top candidate to pair with a catalyst.

## D) Dealer gamma / dark pool
- **CBOE Total P/C 0.86 (6/17); Equity P/C 0.56 (6/23)** = call-heavy / **complacent-froth** → fade chasing into strength.
- Dealer GEX (SpotGamma/Menthor) and dark-pool DIX (SqueezeMetrics) = **PAID** — open blind spot.

## FREE vs PAID inventory
- **✅ FREE / daily-automatable:** CFTC COT (Socrata, weekly), CBOE total & equity put/call (daily), short interest % float & days-to-cover (Nasdaq/FINRA, ~2-wk lag — re-pull each cycle), partial earnings IV via search.
- **💲 PAID:** real-time options flow & unusual activity, single-name IV-rank at scale, dealer gamma/GEX, intraday dark-pool DIX.

**Bottom line:** Gold longs crowded (caution GLD/GOLD); crude soft (no energy tailwind); MU = IV-crush setup tonight; squeeze leadership → **CHTR** top, NTAP/ANF retired; sentiment complacent (equity P/C 0.56) → fade chasing.

*Caveats: COT 4-day lag; short interest ~2-wk settlement lag, varies by source — directional. Energy IV-rank and dealer-gamma/dark-pool require paid feeds (labeled, not estimated).*
