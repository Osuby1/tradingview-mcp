# Markman history calibration — 8.5 months of their own archive (2026-08-03)

**What this is.** The subscription unlocked their full daily archive: 160
issues from November 24, 2025 through August 3, 2026. This study rebuilds
every options trade in it and tests the DRAFT skip rules in
`research/markman-trial-preregistration.md` against their own history —
so the rules can be fixed BEFORE the pre-registration freezes. Companion
data file: `research/markman-history-trades.json` (every trade, every leg,
every flag, machine-readable).

**How it was built.** Their letters carry a running "CURRENT POSITIONS"
ledger, so entries, partial sells and exits could be reconstructed
contract by contract across issues. Prices for every underlying were
pulled from Yahoo (dividend-adjusted series for trend math, unadjusted for
strike math) and every entry was sanity-checked against the letter's own
narrative — no split glitches found this time. Where they never stated an
exit price (that happens a lot — see the honesty section) the exit was
estimated from the stock price and flagged. Nothing estimated is ever
presented as reported.

---

## The headline numbers

- **39 option trades reconstructed** (34 closed, 5 still open at the
  archive's end), 1 stock trade, and roughly **35 more buy orders that
  never filled** (their day-order limits often miss).
- **Closed record: 22 wins, 11 losses, 1 breakeven. Average about +8% per
  trade, median +23%.** Wins average about +49%; losses average about
  −73% — when they lose, the contract usually goes to nearly zero.
- **Their own claimed model account went from about $19,900 to about
  $22,100 over the whole 8.5 months — up 11%. Just buying the S&P over
  the same window made 14%.** And their curve swung from a $26,200 peak
  (early March) to under $19,000 — a one-quarter drawdown on the way.
  So even taking every claim at face value, the letter did not beat the
  index, with far more pain. That is the money takeaway.
- The five open positions will make the final record worse, not better:
  their MDB call marks at roughly −95%, and the remaining DELL half is a
  "winner that became a loser" by their own admission.

**Fine print on the record.** The 22-11-1 uses computed math on their own
stated prices plus estimates for the exits they never quantified. The
subset where every leg was actually reported: 21W-6L-1P, average +19%.
The subset with estimated legs: 1W-5L, average −42%. Read that again —
**the unreported exits are almost all the disasters.**

## Performance by tape

They traded through a real stress test: the S&P slipped below its 200-day
in mid-March and dropped ~13% peak-to-trough, then a second air pocket hit
in early June.

| Entry cohort | Record | Avg |
|---|---|---|
| Nov–Jan (bull tape) | 10W-3L-1P | ~+22% |
| Feb–Mar (correction) | 4W-2L | ~+3% |
| April (recovery buys) | 2W-3L | **−30%** |
| May–Jul | 6W-2L | ~+20% |

Only ONE entry was made with the S&P actually below its 200-day (USO
puts — a total loss). They largely stopped initiating during the worst
weeks; the damage came from **holding** broken contracts through the
selloff and the June air pocket (HOOD, XEL, META, RTX, USO all died
there). So the 2026 tape still cannot tell us how their *entries* perform
in a confirmed down-regime — the sample is one trade.

Calls went 19W-10L-1P (avg +9%); puts 3W-1L (avg +2%, the USO wipeout
eats the three wins).

---

## The draft skip rules, tested on their own trades

**1. Liquidity reality check — UNTESTABLE historically.** No chain
history exists for these dates. Keep it as a live-screen rule. One flag:
the premiums they report on far-out-of-the-money DELL/MDB/TSLA calls imply
implied vols near 90% — plausible in that tape but unverifiable, so their
stated fills should be treated with suspicion until we see live alerts.

**2. Earnings inside the hold window — KEEP. Strongest gate observed.**
- Earnings inside the hold: **1W-4L, average −74%** (CVX −100, OKLO −100,
  RTX-May −100, HOOD −90; AMZN +18 the lone win).
- No earnings inside: **21W-7L-1P, average +22%.**
- Chance of that split being luck: about 3% (exact test). n=5, so still
  a small sample — but it now points the same way as the 2021 audit's n=2.
- Honest nuance: only HOOD was killed *by* the report itself (−13% gap).
  CVX/OKLO/RTX were already nearly dead when their reports hit — earnings
  in-window correlates with their worst habit, riding broken contracts to
  expiry. The gate keeps us out of 4 of their 8 worst losses either way.

**3. Stock more than 10% below its 200-day — KEEP, but call it what it
is: unvalidated.** It fired exactly once in 39 trades (HOOD, 15% below)
and that trade lost 90%. Right direction, n=1. It costs nothing to keep.

**4. Must have a compliant 45–90-day, 0.60–0.75-delta translation —
KEEP, and here is the new evidence it needs teeth.** Estimated delta at
entry (from their own stated premiums) is the best separator in the whole
sample:

| Their contract's delta | Record | Avg |
|---|---|---|
| 0.45 or higher (near/in the money) | 14W-3L-1P (n=18) | **~+38%** |
| Under 0.45 (out of the money) | 8W-8L (n=16) | **~−25%** |

Chance of luck ~4%. The 0.30–0.45 band alone went 2W-6L, −57% average.
Contracts 10%+ out of the money: 4W-5L with a *median* of −89%. **Every
single ~total loss in the book was an out-of-the-money contract.** Our
delta floor isn't just a style preference — in their own history it is
the line between a winning book and a losing one.

**DTE — update the prior.** The 2021 audit found ~18-day contracts; that
habit is gone. 2026 range is 25–67 days, median ~45, none under 21. The
21–45 bucket went 13W-5L-1P (+22% avg); over-45 went 9W-6L (−10% avg) —
but that's the OTM-lotto contamination again, not time itself.

**A warning on the translation, from simulation.** Replaying all 34
closed signals in a synthetic 67-day, 0.675-delta contract with their
exact entry/exit dates: 19W-14L, average about −2%, versus +8% for their
literal contracts. **Their realized edge comes from fast partial
profit-taking on convex contracts, not from directional stock-picking.**
If we translate their signal but hold like tourists, we lose the thing
that made it work. The trial's dual-cohort design plus our own exit rules
(+100%/−50%/21-days) are load-bearing, not decoration.

---

## Honesty audit (they had priors)

The 2021 audit caught two ~2x-inflated claims and one vanished loss. The
2026 archive is better, but not clean:

- **One inflated claim confirmed:** AMD calls — claimed +31.49%; their own
  stated prices (in 4.70, out 5.50) make it **+17.0%**.
- **One understated loss in the ledger:** RXRX stock — running ledger says
  −34%; the actual math (5.03 → 2.85) is **−43%**, which their own body
  text admitted once ("loss of 43%... umph") while the ledger kept saying 34.
- **Two understated *gains*** (RTX Dec claimed +18.5%, actual +26.4%;
  C calls claimed +51.6%, actual +57.1%) — so the arithmetic is sloppy in
  both directions, not a pure pump. But note the asymmetry below.
- **The real pattern: losses go unquantified.** Nine exits were never
  given a price or percentage — USO (~−100%), RTX May (~−100%), the TSLA
  re-entry (~−100%), the CCJ re-entry's back half (~−87%), ABBV's last
  third (~−90%), the "tracked" BIDU half that silently expired worthless,
  OKLO's expiry (noted, never percentaged), MO Aug ("small profit," no
  price — and the stock math makes even that claim doubtful), and SBUX
  (exit never confirmed at all). **Winning legs always get a number;
  6 of the 8 worst losing legs never did.**
- **Ledger sloppiness:** UAL entry line contradicts their own buy order
  and exit math; a WMT entry mis-dated by a month; sale dates on weekends;
  "April 31st"; ticker typo AMZM. The ledger cannot be taken at face
  value without cross-checking the order flow — which is what this file did.
- **Equity curve:** roughly internally consistent this time (realized
  claims ≈ +$6.6k on $2k sizing vs +$2.2k equity change, gap explained by
  open-position marks, mostly MDB's ~−$1.9k). No 2021-style 2x inflation
  found. It just doesn't beat SPY.

## What to change before the freeze

1. **Keep the earnings gate** (criterion 2). Now supported at n=5 plus
   2021's n=2, ~3% luck-probability. Extend it to known binary event
   dates (TSLA delivery day cost their re-entry a −7.5% day).
2. **Keep the deep-fail regime gate** (criterion 3), labeled unvalidated
   (n=1, directionally right).
3. **Keep the liquidity check** (criterion 1) — live-only, untestable
   here; treat their stated OTM fills as unverified.
4. **Sharpen criterion 4 into an explicit delta floor:** skip any alert
   whose recommended contract sits under ~0.45 delta / more than ~10% out
   of the money unless our compliant 0.60–0.75-delta translation exists.
   This is the strongest separator in their own 8.5-month record
   (+38% vs −25%, ~4% luck-probability).
5. **Add nothing about SPY regime** — one entry below the 200-day is not
   evidence; leave macro to our own hedging framework.
6. **Keep the kill criterion and the dual-cohort tracking exactly as
   drafted.** The simulation says the translation cohort may underperform
   their literal contracts unless our exits mimic their trim speed — that
   is precisely what the trial exists to measure.

## Caveats, stated plainly

34 closed trades is a small sample; every bucket above is single-digit to
low-double-digit. The two "significant" splits (earnings ~3%, delta ~4%)
were found while looking at several cuts, so the true false-positive odds
are higher than the raw numbers suggest — they justify *screening rules
in a paper trial*, not real-money confidence. Six trades carry estimated
exit values (all flagged); deltas are Black-Scholes estimates from their
own stated premiums; earnings dates from Yahoo. The down-regime question
is unanswered (n=1). And the record above is *their claims* where
reported — the honest version of their year is: **roughly +11% claimed on
the model account, behind the S&P's +14%, with a 25% drawdown, before
subscription costs.**

*Built 2026-08-03 from `research/markman-archive/markman-archive-2026-08-03.json`.
Prior audit: `research/markman-ledger.json` (commit 23be6c7).*

## Portfolio-page verification (2026-08-03 PM, Omar-requested)

Checked app.markmancapital.net/portfolios/digital-leverage ("Million Dollar
Portfolio" embed) row-by-row vs the newsletter reconstruction:
- Arithmetic: every row's Total Chg % computes correctly from its own
  Entry/Last (~15 spot-checks, all pass).
- Losers ARE listed (unlike the newsletters' silence): IONQ/FCX/OKLO/USO/
  RTX-May -100%, TOL -96%, CCJ -94%, HOOD/XEL -90%, TSLA back-half -97%,
  ABBV third -98.28%, open MDB -97% and DELL third -93% shown.
- ~25 of 28 comparable closed trades match our reconstruction exactly or as
  half-averages (MAR 144, MO-Jan 53.05, PG 7.14, MP, WMT x2, ON, CCJ, INTC,
  BA, APLD, TTWO, META, AMZN, DELL, MRNA, SBUX 0.0, BIDU-Dec 38.03).
- THREE PROBLEMS: (1) AMD Feb: portfolio books exit 6.18 (+31.49%) but the
  1/20 newsletter told subscribers "Sell at $5.50" (+17.0%) - the exit is
  booked 12% better than the price subscribers were alerted to take, and
  the same issue bragged "31% gain" same day. (2) MO Aug 70C: booked +38%
  (exit 6.90) vs newsletter's only statement "closed MO for a small
  profit" - no subscriber-visible exit price exists; unverifiable and
  incongruent. (3) The worthless-expired BIDU tracked half (123.82 close
  vs 130 strike) is absent from the table entirely. Also watch: today's
  UAL half listed at exit 8.27 vs the morning alert "sell at 7.70" - same
  better-than-alerted-fill pattern as AMD.
- RTX-Dec listed LOWER than our reconstruction (+18.5 vs +26.4) -
  errors run both directions on small stuff; the directional pattern is in
  the exits they brag about.
- Pre-archive rows (Jun-Nov 2025) arithmetic-checked only - no newsletters
  held to verify against.
