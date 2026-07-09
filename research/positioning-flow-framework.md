# Positioning & Flow Framework (Gap 3)

**Purpose:** the institutional "who is offside?" layer. Price + fundamentals tell you *what*; positioning tells you *how crowded the trade already is* and where a violent unwind hides. Crowded one-sided positioning is a contrarian flag; clean positioning lets a trend run.

**Sourcing:** verified/official only. Prices web-approx; authoritative = live TV feed.

## The five reads

### 1. Futures positioning — CFTC Commitments of Traders  ✅ FREE
- **Socrata API:** `https://publicreporting.cftc.gov/resource/6dca-aqww.json` (disaggregated/legacy futures-only). Filter by `contract_market_name`, order by `report_date_as_yyyy_mm_dd DESC`.
- Weekly: data as of **Tuesday**, released **Friday** (~4-day lag — bake that in).
- Read **Managed Money / Non-Commercial NET** (large specs) + **week-over-week change**. Crowded long at a range extreme + still building = contrarian caution; soft/bleeding = no spec tailwind.
- Markets that matter to our book: **WTI crude** (MPC, BKR, PSX, VLO), **gold** (GLD/GOLD), nat-gas, copper, indices.

### 2. Equity options / vol  (partly free)
- **IV rank/percentile, term structure, skew, expected move** into a catalyst. Front-month IV ≫ back months = event premium → **IV-crush risk** after the print (favors short-vol structures, not buying the straddle).
- **Call/put OI & volume skew** = directional crowding. Heavy call-crowding → a miss is punished harder than a beat is rewarded.
- Free-ish via verified snippets (MarketChameleon/Saxo/Barron's); clean numerics on most single names are **paid** (label, don't guess).

### 3. Short interest / squeeze  ✅ FREE (lagged)
- SI % of float + **days-to-cover**, from Nasdaq/FINRA bi-monthly settlement data (~2-wk lag — **re-pull each cycle; stored levels go stale fast**).
- Squeeze candidate = high SI % float **and** high days-to-cover **and** a forward catalyst. Rank by all three.

### 4. Sentiment — CBOE put/call  ✅ FREE
- **CBOE Total & Equity Put/Call**, daily. Low equity P/C (~0.5) = call-heavy/complacent/froth → fade chasing. High = fear/possible washout bottom.

### 5. Dealer gamma / dark pool  💲 PAID (blind spot)
- Dealer GEX (SpotGamma/Menthor) and dark-pool DIX (SqueezeMetrics) need a paid feed. FINRA ATS volume is free but weeks-lagged. **Acknowledge this as an open blind spot** rather than estimating.

## Output in a brief
A short "Positioning & Flow" block: the 2–4 reads that bear on the book, each with a one-line trading implication. Always state the data's as-of date (COT lag, SI lag).

## FREE vs PAID inventory (for automation)
- **✅ FREE / daily-automatable:** CFTC COT, CBOE total & equity put/call, short interest % float & days-to-cover, partial earnings IV/expected-move via search.
- **💲 PAID / gated:** real-time equity options flow & unusual activity, single-name IV-rank at scale, dealer gamma/GEX, intraday dark-pool DIX.

## Worked example
See `research/examples/2026-06-24-positioning-snapshot.md` — gold specs crowded long (caution), crude soft (no energy tailwind), MU an IV-crush setup into its print, and the squeeze board rotated (CHTR ~26% SI now top; NTAP/ANF retired).
