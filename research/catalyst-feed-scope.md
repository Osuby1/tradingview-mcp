# Catalyst Feed (ALL SECTORS) — Scope

*Written 2026-07-23. Supersedes the biopharma-only draft. Purpose: a forward calendar
of scheduled, high-impact, binary-ish events across the WHOLE market, mapped to tickers,
so we are positioned/aware instead of blindsided. Origin: 3 of the 10 biggest US gainers
since June (CRNX, MBX, COAG) were on no tab — but the blind spot generalizes past
biopharma to any catalyst our momentum/leader scanners can't originate. Omar 2026-07-23:
build it for ALL sectors, not just biopharma.*

## 1. What it is
A cross-sector **event calendar mapped to tickers**. It gives WHERE the catalysts are and
WHEN — not which way they resolve (except earnings, where we have a measured PEAD/SUE edge).

## 2. Event taxonomy (all sectors)
| Event | Sectors | Schedulable? | Have an edge? |
|---|---|---|---|
| **Earnings** | ALL | Yes (quarterly, dated) | **YES — measured PEAD/SUE, esp. small/mid** |
| Biopharma binary (PDUFA / trial readout / AdCom) | Health | Yes / window | No (pure binary) |
| Regulatory & legal (court, FTC/DOJ/FCC/FERC/FAA/EPA) | Telecom, utilities, airlines, tech | Some scheduled | No |
| Corporate events (investor/analyst days, product launches — GTC, CES, Apple) | Tech, consumer, auto | Date known | No |
| Index add/rebalance (S&P/Nasdaq) | ALL | Yes | Small, mechanical |
| Conference data drops (ASCO, GTC, OPEC) | Sector-specific | Conf date known | No |
| M&A / buyout | ALL | **NO** | (uncatchable) |

## 3. Data sources — feasibility verified 2026-07-23
**Backbone (free, confirmed):**
- **TradingView scanner earnings fields** — `earnings_release_next_date` (unix),
  `earnings_per_share_forecast_next_fq`, plus `sector` — market-wide, one request. ✅ probed,
  works. This is the **ALL-SECTOR earnings calendar** and the highest-value layer (edge).
- **ClinicalTrials.gov API v2** — Phase 2/3 INDUSTRY trials + primary-completion dates =
  biopharma readout windows. ✅ probed.
- **FDA AdCom calendar** (fda.gov) — scheduled advisory meetings. ✅ reachable.
- **SEC EDGAR** — `company_tickers.json` for the sponsor/name→ticker map; 8-K full-text for
  event filings; our existing `edgar_sue_backtest.py` for the SUE overlay.

**Paid / optional (later):**
- **Wall Street Horizon** — the standard corporate-event calendar (investor days, product
  events, conferences, splits) across sectors. This is what fills the non-earnings,
  non-biopharma gap cleanly. ~$$.
- **BioPharmaCatalyst** — clean PDUFA dates (~$100–300/mo).

**News verification (verified outlets only, per [[data-sourcing-standards]]):** for
confirming individual events — Reuters, Bloomberg, sector trades (Fierce Biotech, Endpoints
for health; the majors for the rest). No forums.

## 4. Architecture (daily pipeline)
1. **Collectors:** TV scanner earnings (all sectors, backbone) + ClinicalTrials + FDA AdCom
   + EDGAR 8-K + (later) Wall Street Horizon / conference calendars.
2. **Normalize** → `{ticker, company, sector, event_type, date_or_window, detail,
   est_eps / SUE, source, confidence}`.
3. **Ticker-map** (SEC company_tickers + alias table); public US, drop private/academic.
4. **Loose liquidity filter** (price>$5, cap>~$300M) — looser than the momentum scanners so
   fresh IPOs / small names qualify (that was the miss).
5. **Overlays:** earnings names get the **PEAD/SUE overlay** (our one measured edge, via the
   EDGAR SUE pipeline); biopharma get a BINARY-risk label.
6. **Output — INTEGRATED INTO THE DAILY SCAN (Omar 2026-07-23), not a standalone tab:**
   `research/catalyst-calendar.json` is JOINED by ticker onto the per-ticker workbook tabs
   (Fresh Buys, Plans, Blocked, Sell Mode, Market Movers…) as **two columns on each row** —
   **"Catalyst"** (event type + date, e.g. "Earnings 7/28", "PDUFA ~8/15") and
   **"Catalyst View"** (plain-English what-it-is + how-it-may-play-out + **ALWAYS a suggested
   action** — trim into / do NOT hold full size through / spec-size for total loss /
   defined-risk options / post-confirmation entry / awareness-only — matched to the event type
   per [[trading-execution-protocol]]: SUE/PEAD lens for earnings, BINARY defined-risk for
   biopharma, context for the rest; say "awareness-only, no edge" where we genuinely have none
   rather than inventing a call). Blank where a ticker has no near catalyst. PLUS a
   **compact list of catalyst names NOT in the scanned universe** so the blind-spot names
   (the CRNX-type misses this whole thing exists to catch) still surface. A one-line catalyst
   note goes in the brief; convergence with ignition/origination is flagged.
7. **Daily wiring:** `scripts/run_eod_chain.bat` rebuilds `catalyst-calendar.json` BEFORE the
   workbook compile, so the columns are fresh every day — the catalyst feed is part of the
   nightly universe scan, not a separate manual run.

## 5. Trading model — by event type (honest)
- **Earnings (the actionable layer):** we have a MEASURED short-horizon edge (PEAD/SUE,
  strongest in small/mid). Act on fresh high-SUE names (extends `pead_live_signal.py`); and
  never hold a momentum long blindly INTO an unflagged earnings date. Pre-register all.
- **Biopharma binary:** awareness-first; defined-risk spec only (size for total loss / options);
  no directional edge — CRNX went +99% but the same setup gaps −60% on failure.
- **Regulatory / product / index:** awareness/context; case-by-case; no assumed edge.
- Everything pre-registered in the outcome tracker ([[outcome-tracker]],
  [[anti-sycophancy-validation-mandate]]) — measure, don't narrate.

## 6. Honest limitations
- Scanner earnings dates are estimates — companies move them; verify near-term ones.
- Non-earnings / non-biopharma events (regulatory, product) are the hardest to source for
  free — the MVP is THIN there until Wall Street Horizon (paid) is added. Say so.
- M&A pops remain uncatchable (unscheduled).
- Name→ticker mapping imperfect (subsidiaries, ex-US parents).
- Only earnings carries a real statistical edge; the rest is awareness, not alpha.

## 7. Phased build (effort / cost)
- **MVP (free, tonight):** all-sector earnings calendar (TV scanner) + biopharma binary layer
  (ClinicalTrials + FDA AdCom) + SEC ticker map → `research/catalyst-calendar.json` +
  Catalyst Watch tab + brief block, SUE overlay on earnings where available, loose liquidity
  floor, convergence flag vs ignition/origination.
- **v1 (free):** + EDGAR 8-K event filings + conference calendars + richer AdCom detail.
- **v2 (paid):** Wall Street Horizon corporate events + BioPharmaCatalyst PDUFA.

## 8. Recommendation
Build the all-sector MVP: earnings backbone (universal + the PEAD/SUE edge) + the biopharma
binary layer, all free. It closes the "didn't know a catalyst was coming" gap across the
whole market, with the edge concentrated where we've actually measured one (earnings), and
awareness everywhere else. Prove it against the outcome tracker before paying for WSH/BPC.

Related: [[forecasting-improvement-findings]], [[outcome-tracker]],
[[early-ignition-multibagger-system]], [[analysis-capability-frameworks]], [[data-sourcing-standards]].
