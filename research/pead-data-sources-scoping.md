# Scoping: clean data sources for a genuine PEAD signal

Written 2026-07-22. Question from Omar: what data source could give us a real,
backtestable Post-Earnings-Announcement-Drift signal - the orthogonal factor
yfinance could not deliver.

## What PEAD actually requires (the spec)

PEAD = stocks drift in the direction of an earnings surprise for weeks after the
print. To build it without fooling ourselves we need, per earnings event:

1. **A surprise measure.** Two valid constructions:
   - **SUE (Standardized Unexpected Earnings)** - actual EPS minus a MODEL
     expectation (usually same-quarter-last-year, i.e. a seasonal random walk),
     scaled by the volatility of past surprises. Bernard & Thomas (the canonical
     PEAD papers) used exactly this. **Needs only ACTUALS - no analyst estimates.**
   - **Analyst surprise** - actual minus the CONSENSUS estimate as it stood just
     before the print. Closer to how the market reacts, but needs point-in-time
     estimates.
2. **The exact announcement date AND time** (BMO vs AMC decides which session the
   drift starts).
3. **Historical depth** - 5+ years to backtest across regimes.
4. **Breadth** - the Russell universe we scan, survivorship-free ideally.

## The one trap that eliminates most cheap sources: POINT-IN-TIME

Verified in the research: "calculating an accurate historical surprise requires
capturing a valid consensus estimate at the exact time of earnings release;
extracting an estimate snapshot even one day late contaminates the tracking layer
with post-event analyst revisions." Earnings and estimates get RESTATED. If a
source stores today's restated actual, or the current estimate on an old date, a
backtest using it leaks the future - the same look-ahead bias that made the
yfinance fundamentals untrustworthy.

**So the first question for ANY source is not price - it is: are the historical
estimates/actuals stored as-of-the-event, or restated?** Most retail APIs do not
say, and several are known to serve restated numbers.

## The sources, tiered

### FREE, and genuinely point-in-time - SEC EDGAR XBRL `companyfacts`
- `data.sec.gov/api/xbrl/companyfacts/CIK{n}.json` - no key, 10 req/s, per company.
- Every fact carries a **`filed` date** = when it became public. That is REAL
  point-in-time for ACTUALS (EarningsPerShareDiluted, Revenues) with the filing
  timestamp. CIK map is free (`company_tickers.json`).
- **Gives:** actual quarterly EPS + revenue + exact filing date, clean, free, local.
- **Does NOT give:** analyst consensus. So you build **SUE (seasonal model)**, not
  analyst-surprise. That is a LEGITIMATE, publishable PEAD construction - it just
  measures "earnings momentum vs its own history", not "beat vs the Street".
- Fit: perfect for this setup - python, no cost, matches the Russell-wide infra
  the origination scanner already runs.

### LOW COST, adds analyst-surprise - Financial Modeling Prep / Finnhub
- **FMP Premium ~$59/mo (annual)**: earnings surprises + analyst estimates,
  up to 30y history, earnings calendar, bulk API. Ultimate $149/mo adds global +
  3000 calls/min + transcripts.
- **Finnhub**: `company_earnings()` (surprises) + `company_eps_estimates()`, free
  tier (limited) plus paid tiers (pricing page would not render - verify live).
- **Both add the "beat vs consensus" flavor** EDGAR cannot. BUT their historical
  estimate integrity is UNVERIFIED - must test point-in-time before trusting a
  backtest (see the verification test below). Do not assume they are clean.

### GOLD STANDARD, expensive - I/B/E/S (LSEG/Refinitiv), Zacks, FactSet
- Refinitiv I/B/E/S and Zacks are the academic-grade point-in-time consensus
  databases; Zacks powers the classic SUE/ESP research. Institutional pricing -
  overkill for a $1M personal book. Note only in case the cheap tier fails.

### AVOID for backtesting - yfinance, most scraped feeds
- Restated / not point-in-time, unreliable coverage (returned empty for us). Fine
  for a rough CURRENT read, useless for a clean historical test.

## Recommended path (cheapest-first, no self-deception)

**Phase 1 - FREE, build the real thing before paying a cent.**
Build a seasonal-SUE PEAD from EDGAR `companyfacts`: pull actual quarterly EPS +
filing dates for the Russell names, compute SUE = (EPS_q - EPS_q-4) / stdev(past
8 surprises), rank cross-sectionally, and backtest the 1-3 month drift vs SPY -
WALK-FORWARD, survivorship-flagged. This is genuinely point-in-time (filing dates),
zero cost, and tells us whether PEAD even works in our universe. If it does not
show an edge here, no paid feed will save it.

**Phase 2 - only if Phase 1 shows drift, pay for consensus.**
Add FMP or Finnhub analyst-surprise and A/B it against the free SUE. First run the
**point-in-time verification test**: pull a specific historical print (e.g. a 2024
NVDA quarter), and check the API's stored "estimate" against the pre-announcement
Street number from a contemporaneous news archive. If they match -> point-in-time,
trust it. If the API shows a suspiciously exact or restated figure -> reject it.

**Phase 3 - forward-validate live** through the outcome tracker regardless of
source, because even clean PEAD is a modest, regime-dependent edge.

## Effort / cost / risk summary

| Option | Cost | Point-in-time | Effort | Verdict |
|---|---|---|---|---|
| EDGAR companyfacts (seasonal SUE) | FREE | YES (filing dates) | ~1 day build | **START HERE** |
| FMP Premium | ~$59/mo | UNVERIFIED - test first | ~half day | Phase 2 if SUE works |
| Finnhub | free-to-paid | UNVERIFIED - test first | ~half day | Phase 2 alt |
| I/B/E/S / Zacks | $$$$ | YES | integration | overkill |
| yfinance | free | NO | - | not for backtest |

## The honest caveat
Even with clean PEAD data, the edge is modest (single-digit annualized, regime
dependent) and only pays with breadth + discipline + the forward validation we now
run. PEAD is real and one of the most durable anomalies - but it is an edge to be
harvested carefully, not a forecasting switch. Match expectations to that.

Sources: SEC EDGAR XBRL API docs; Financial Modeling Prep pricing + earnings
surprise/PEAD docs; Finnhub API; backtesting-bias / point-in-time literature
(hedgefundalpha, analystprep, starqube).
