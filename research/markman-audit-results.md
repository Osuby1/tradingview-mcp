# Markman "Tactical Options" Newsletter Audit — Results

**Run:** 2026-07-31, per the standing order in `session-pending-tasks.md` (MARKMAN NEWSLETTER AUDIT + MARKMAN AUDIT UPDATE).
**Dataset:** all 31 `.eml` letters in `research/markman-history/` (Markman Capital Insight, Jan 7 – Mar 11, 2021). **This is the complete dataset — no more emails exist.**
**Companion file:** `research/markman-ledger.json` — every recommendation with source citations, prices, gate math, and labels.

---

## The bounded frame — read this first

This audit covers **ten weeks of the raging early-2021 bull market**. Almost anything you bought a call on in that stretch went up. That means:

- We CAN grade these specific picks, and we CAN test whether our gates would have separated the winners from the losers **in this sample**.
- We CANNOT clear or condemn a re-subscription for bear markets or choppy markets. The steady losing stretch Omar remembers is **not in this data** — those letters don't exist anymore, so that period is simply unknowable.
- The honest decidable question is gate separation, not absolute edge.

---

## Bottom line

**The newsletter's picks made money in this window — but our rulebook would have taken zero of these trades.** Every single recommendation fails our 45-to-90-day time rule (they trade 1-to-6-week options; median about 18 days to expiry). So "gate-passers vs gate-failers" — the question we set out to decide — is degenerate: there are **no full passers to compare**. The only individual gate that separated winners from losers here was the **earnings blackout** (the two trades holding through an earnings date averaged a 29% loss; the clean ones averaged a 22% gain — but that is only 2 trades, and the big one, First Majestic, died of the silver-squeeze unwind, not the earnings print). The delta band and the 200-day trend filter did NOT separate winners from losers in this sample.

**What that means in money terms:** if you had followed every filled recommendation with our standard $2,500 per trade, the ten weeks netted about **+$6,500** (17 positions, average +15.4% each, 12 winners, 5 losers). The S&P 500 did +3.8% in the same window. Good result — earned in the easiest options tape of the decade, with a style our discipline rules exist specifically to block.

---

## 1. Their record, reconstructed (the part they don't headline)

31 letters produced **44 distinct recommendation events**. Of those: **17 actually filled and became trades**, 15 never filled (stated or safely inferred), 6 have unknowable fates (follow-up letters missing or the dataset ends), and 4 are known only as passing mentions with no contract details (LYV, AAPL, HD, and a GM attempt), plus 2 pre-dataset positions (TSM, and MS/DD mentions) excluded from stats.

**The 17 filled trades: 12 wins, 5 losses (71% win rate). Average +15.4% per position. Median +18.9%.**

- Winners averaged **+36%**. Losers averaged **−34%**.
- Biggest win: Costco March calls, **+62%** in two days.
- Biggest loss: First Majestic Silver calls, **−74% in one day** (bought into the silver-squeeze spike Feb 1, stopped out Feb 2). The letters' own money-management line — never more than 20% of capital in one trade — is what kept that from being fatal.

### Honesty findings against their own claims

1. **Two "overall gain" claims are double the real number.** When a trade exited in halves with one half losing, they reported the SUM of the two half-returns instead of the average: BTBT claimed "+17.5% overall" — the true position return is **+8.8%**. SunPower claimed "+14% overall" — truth is **+7.3%**. When both halves won (Cigna), the arithmetic was suddenly done correctly. The error only ever flattered them.
2. **The AMD loss simply vanishes.** Bought Feb 10 at $4.70, last seen Feb 16 trading at $3.85 with a $3.55 stop, and the portfolio is "flat" by Feb 18. No letter ever states the loss (~−24%, our reconstruction). Fairness note: the Feb 17 letter is missing from the dataset, so we can't prove it was never disclosed — but no *surviving* letter admits it, while every winner gets a headline banner.
3. **Wins get banners, losses get buried mid-paragraph.** "Sold TSM calls for 99% gain" is the headline; the −73% AG disaster is admitted in body text ("that will happen occasionally"). To their credit, losses ARE disclosed — CCL, AG, AAL, GM all get stated loss numbers — they're just never the headline.
4. Small stuff: the CCL loss was claimed as −18% (actual −16.4%, they rounded against themselves), entry dates have typos ("Fri Jan 5" for Feb 5, "Jan 17" for Jan 27), and the Feb 4 Deere alert had the wrong strike, expiry AND price — corrected the same day (we use the corrected contract).

---

## 2. The full per-trade table (17 filled positions)

"Their #s" are the newsletter's own claimed fills/exits. Anything reconstructed is labeled. Gate columns are from OUR rulebook applied retroactively at the alert date (synthetic Black-Scholes delta with vol = max(20d, 60d realized) × 1.2 — LABELED synthetic throughout).

| ID | Alert | Contract | Entry | Exit(s) | Position P&L | Gates failed (of 6 checkable) |
|----|-------|----------|-------|---------|-------------|-------------------------------|
| R01 | Jan 7 | CCL Jan-15 $15 C | $5.80 | stopped $4.85 Jan 11 | **−16.4%** | delta 0.96, DTE 8 |
| R04 | Jan 11 | BLNK Feb $65 C | $4.90 | half $6.50; half "at market" ~$5.15 (estimate) | **+18.9%** | delta 0.52, DTE 39 |
| R08 | ~Jan 19* | XPEV Feb $60 C | $4.60 | half $6.10; 2nd half SYNTHETIC: target $7.50 hit | **+47.8%** (part synthetic) | delta 0.53, DTE 31 |
| R12 | ~Jan 25* | FUBO Feb $40 C | $7.10 | halves $10.30 / $12.40 | **+59.9%** | DTE 25 |
| R14 | Jan 28 | BTBT Feb $17.5 C | $5.70 | half $7.90; half stopped $4.50 | **+8.8%** (they claimed +17.5%) | DTE 22 |
| R15 | Feb 1 | AG Feb $17 C | $6.10 | stopped $1.60 Feb 2 | **−73.8%** | delta 0.83, DTE 18, earnings 2/18 in window |
| R19 | Feb 5 | XOM Feb $45 C | $5.00 | half $6.50; half $5.40 | **+19.0%** | delta 0.87, DTE 14 |
| R20 | Feb 5 | CAT Feb $190 C | $5.14 | half $7.15; 2nd half INFERRED at $8.00 stop (exit letter missing; conservative) | **+47.4%** | DTE 14 |
| R22 | Feb 9 | SPWR Feb $48 C | $5.50 | half $6.90; half stopped $4.90 | **+7.3%** (they claimed +14%) | gates uncheckable — SPWR delisted, no free data |
| R23 | ~Feb 10* | AMD Mar $95 C | $4.70 | INFERRED stop $3.55 ~Feb 17 (loss never stated) | **−24.5%** (inferred) | delta 0.45, DTE 37 |
| R27 | ~Feb 19* | CI Mar $210 C | $5.90 | halves $8.10 / $9.75 | **+51.3%** | delta 0.42, DTE 28 |
| R28 | ~Feb 19* | ORCL Mar $60 C | $5.15 | half $6.55; half $5.30 | **+15.0%** | DTE 28, ORCL earnings 3/10 in window |
| R33 | Mar 1 | AAL Mar $23 **PUT** | $2.40 | stopped $1.75 Mar 3 | **−27.1%** | DTE 18, regime (shorting above its 200-day) |
| R36 | Mar 3 | GM Mar $50 C | $4.10 | stopped $2.90 Mar 4 | **−29.3%** | DTE 16 |
| R40 | Mar 9 | GM Mar $50 C | $5.00 | half $6.50; 2nd half SYNTHETIC: target $8.50 hit (dataset ends 3/11) | **+50.0%** (part synthetic) | delta 0.85, DTE 10 |
| R41 | Mar 9 | MSFT Mar $232.5 C | $5.00 | halves $6.50 / $8.00 | **+45.0%** | delta 0.55, DTE 10 |
| R42 | Mar 10 | COST Mar $322.5 C | $5.50 | halves $8.45 / $9.35 | **+61.8%** | delta 0.55, DTE 9, regime (COST below its 200-day) |

\* = the original alert letter is NOT in the 31-file dataset (those days' letters are missing); the trade is reconstructed from follow-up letters. Every such case is flagged in the ledger.

**Never filled (15):** TSM Jan 8 weekly (1-day option!), MCD, OXY?, DG?, LYV, TDOC?, DDOG?, AAPL, WDAY, CAT 185, CRM, DE (the corrected 310 strike), AMAT, PTON, HD, MMM, BA, WW, SBUX, DKNG, GM (Mar 2 attempt), DY, MSFT 230, DKS, BBBY. (Question-marked names plus COST/FCX April: fate unknowable — follow-up letters missing or dataset ends. Hypothetical if-filled reconstructions for those six live in the ledger, all labeled.)

**Flagged tickers:** BBBY is delisted — yfinance's surviving series failed our sanity check against real 2021 prices (~2x off) and was REJECTED; its gate audit is marked unreliable. SPWR and WW have no free daily data at all (delisted/restructured) — SPWR's P&L uses their claimed exits only; gates uncheckable. FUBO's series carried a post-2021 reverse-split distortion (10x) — detected and corrected against its verified real $49.18 close on Jan 25, 2021.

---

## 3. The retroactive gate audit — the decidable verdict

Our six checkable gates, applied at each alert date (OI and bid/ask spread gates are **NOT reconstructable** from free historical data — that is the known hole in this audit; nothing can be said about them):

| Gate | Result across the sample |
|------|--------------------------|
| **45–90 days to expiry** | **ALL 40 recs with known contracts FAIL.** Range 1–42 days, median ~18. This is a different sport from ours. |
| Delta 0.60–0.75 (synthetic) | 26 of 40 outside the band — they mix lottery-ish (MMM 0.06, PTON 0.29) with near-stock (CCL 0.96, FUBO ~1 pre-correction). On filled trades: in-band averaged +12.4%, out-of-band +17.9% — **no separation, if anything inverted**. Tiny sample. |
| Monthly (3rd-Friday) expiry | Passes everywhere except the Jan 8 TSM weekly (1 day to expiry — never filled, thankfully). |
| **Earnings blackout** | **The only gate with teeth here.** Two filled trades held through an in-window earnings date (AG, ORCL): average **−29.4%**. The 14 clean trades: average **+22.3%**. Caveat honestly: n=2, and AG's wipeout was the silver-squeeze unwind, not its Feb 18 print. Among never-filled recs it also flagged MCD, DDOG, DE, AMAT, DKS — the DKS call was recommended the afternoon before its earnings morning. |
| Breakeven vs expected move | Passes almost everywhere (their entries were near- or in-the-money; synthetic vol in that tape was huge). Only MMM failed. No separation power in this sample. |
| Price vs 200-day average (regime) | Only 2 filled trades failed it — and they split: AAL puts (−27%) failed it and lost; COST calls below the 200-day made +62%. **No separation in this sample.** |

**Verdict on the pre-registered question ("do gate-passers beat gate-failers?"): NOT DECIDABLE AS POSED — there are zero full gate-passers among 44 recommendations.** The stack rejects the entire newsletter. The per-gate evidence says: earnings blackout helped (weakly, n=2), delta band and regime filter showed nothing in ten bull-market weeks, and the DTE rule never got a test because it vetoed everything.

Equally important: **gate-failure count did not predict P&L** (3-gate failers include both the worst trade, AG −74%, and the best, COST +62%).

---

## 4. What this means for re-subscribing

**This audit cannot clear or damn the subscription.** Ten weeks of one-directional bull tape, 17 filled trades, and the losing period Omar actually remembers isn't in the data. A 71% win rate with +15% a trade in THAT tape is consistent with skill AND with a rising tide — indistinguishable at this sample size.

What the audit DOES establish:

1. **Structural incompatibility.** Their product is 2–5 week momentum options. Our rulebook (45–90 days, 0.60–0.75 delta, earnings blackout, $2,500 cap) would have taken **zero** of their 44 recommendations as-is. Subscribing and then filtering through our gates = paying for a service we'd never act on.
2. **Their accounting flatters them.** Two doubled "overall gain" claims and one vanished loss in just ten weeks. Any live trial must mark THEIR trades with OUR arithmetic.
3. **Risk profile:** the one-day −74% shows what the style can do; their own 20%-of-capital ceiling and hard stops are real and were honored in the letters.

**Recommendation — trial framing only (per the standing anti-sycophancy mandate):** if Omar re-subscribes, treat it as an UNPROVEN detector: log the **first 30 live alerts** in a pre-registered ledger (same format as `markman-ledger.json`) before a single dollar follows one — entry, exits, our-arithmetic P&L, and our gate stamps at alert time. Decide continuation on that live sample, which will include whatever regime shows up, not on ten weeks of 2021 sunshine. If any real-money expression is ever considered, it would have to be a RE-ENGINEERED version of their signal (their name selection, our contract selection at 45–90 days / 0.60–0.75 delta) — and that variant is untested; it is NOT what this audit graded.

---

## Method notes and labels (for reproducibility)

- Bodies parsed from HTML with Python's `email` module; every price/date cross-read against the stripped text. The Feb 4 correction letter supersedes the original Deere alert.
- "Claimed" = the newsletter's own stated fill/exit — taken verbatim, never independently verified (no historical options tape available for free).
- "SYNTHETIC" = Black-Scholes reconstruction: vol = max(20-day, 60-day realized) × 1.2, risk-free ~0.1%, close-to-close walk; open second-halves exit at their stated target/stop when the synthetic value crosses it, else intrinsic at expiry. Two trades (XPEV, GM #2) have one synthetic leg each; both synthetic legs hit TARGETS, so if anything the reconstruction may flatter them — flagged.
- "Inferred" = the exit letter is missing but the position provably closed between two surviving letters; the conservative bound is used (CAT second half at the $8.00 stop, not the $9.45 target; AMD at its stop).
- Earnings dates from yfinance historical earnings (available for all tickers used; fetched with retries). OI/spread gates: not reconstructable — known hole. SPWR/WW/BBBY data limits flagged above.
- Sample regime: SPY +3.8% over the window; Nasdaq/small-caps far hotter. Every conclusion above is bounded to this sample.
