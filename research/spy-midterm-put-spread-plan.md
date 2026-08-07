# SPY Midterm-Correction Put Spread — Trade Plan (authored 2026-07-06)

Omar's H2-2026 correction expression. Reminder routine fires Mon 2026-07-27 ~9:00 ET (tranche-1 entry week).

## Thesis
- Midterm election years: avg intra-year drawdown ~17–19%; ≥10% correction in 12 of 17 midterm years (~70%) since 1957; weakness clusters Apr–Oct; **low forms late October almost without exception**, then the strongest rally of the 4-year cycle (avg +15% next 12m).
- Distribution matters: 2022 −25%, 1990 −20%, 1970 −26%, 1962 −27%, 2002 −33% — the 14–20%+ zone has real precedent, hence the wide spread.
- Supporting tape (as of 7/6): records with narrow leadership, SMH Chandelier SELL flip 7/2, crypto bearish regime, Polymarket 77.7% zero-2026-cuts (hawkish Warsh Fed), VIX 16.06 complacent, SPY 749.63.
- Counter-case: second-term-president midterms run milder (+8.8% avg, Carson); Street constructive. This is a positive-expectancy seasonal bet, NOT a certainty → size small.

## Structure — SPY Nov 20 2026 vertical put spread 710/600 (~$1,420 debit, est. @ 7/6 vol)
- BUY Nov 20 710 put (~$19.5) / SELL Nov 20 600 put (~$5.3). One order, net debit. Max loss = debit.
- Why 710/600 over 710/645: short-leg premium decays fast below −14% ($10 @645, $5.3 @600, $2.2 @525); the extra $445 buys $4,500 more payout in the 14–20% zone (real midterm precedent). Beyond −20/25% coverage, just buy the naked 710 put instead (525 short leg saves pennies).
- Payoff per spread @ expiry: −8% +$580 · −10% +$2,080 · −14% +$5,080 · ≤−20% +$9,580 max (6.7x). Breakeven ≈ 696 (−7.2%). Flat/up = −$1,420 (−100%).
- Wider spread also holds delta better through the planned early-exit zone (gains don't cap out at −10/−12% like the 645 version).
- Size: ONE spread ≈ 2.3× the ~$600 risk unit. Premium is 100% at risk.

## Entry plan
- **Tranche 1 (half): week of Jul 27–31, before FOMC Jul 28–29.**
- Tranche 2: Aug 10–21 into strength; ideally on a VIX print <15 (cheaper long leg as the seasonal window opens).
- ABORT ENTRY if the correction already started (SPX below trend supports / VIX >20 / SPY well under ~735) — don't chase weakness with fresh puts; re-underwrite instead.
- July = strongest Q3 month; buying earlier just donates theta.

## Exit plan (matters more than entry)
- Scale out INTO the panic: VIX >28–30 or SPY −10 to −12% → start selling.
- **Flat by early November no matter what** (midterms Nov 3; post-midterm rally vaporizes put value). Never hold for the full 20%.
- Close both legs together; never hold deep-ITM legs into expiry Friday.
- The bigger prize: cash + Tier-1 buy list ready at the October low (12m post-midterm-low avg ≈ 2× normal returns). The spread payoff funds those fills.

## Status log
- 2026-07-06: plan authored; NOT entered. Cloud reminder set for 7/27. No position.
- **2026-07-27: TRANCHE 1 DECLINED by Omar. No position.** Quoted debit **$1,214**
  (vs $1,420 modelled) → max loss $1,214, max gain $9,786, breakeven SPY 697.86
  (−5.4%), best case ~8.1x. **No abort clause had fired:** VIX 19.33 (line 20,
  intraday high 19.93), SPY 737.60 (line ~735, intraday low 735.87), SPY below its
  20d 746.58 and 50d 744.97 but +5.5% over its 200d 698.89 and only −2.9% off its
  highest close. So this was a discretionary decline against a live plan, not an
  abort. Logged as a graded skip: `research/calls-ledger.json`
  → `2026-07-27-SPY-putspread-skip`. Grades at SPY levels through Nov 20 2026 —
  below 697.86 the skip cost money, flat/up it saved $1,214.
- **2026-07-27 process note:** the 7/27 reminder was a CLOUD routine and never
  reached the local session. Nothing in the nightly chain or the morning brief reads
  this file, so its own dated entry week passed unflagged until Omar asked. Tranche 2
  (Aug 10–21) has the same exposure. See "commitments due today" TODO.


## EXECUTION RECORD - Tranche 1 (2026-07-31)
FILLED as LONG 710 PUT ONLY (structure deviation, documented in calls-ledger id
2026-07-31-SPY-put-tranche1): cash account could not margin the spread (short
leg demanded $60k cash-secured; rejected order 1292217286 on the record).
1 SPY Nov 20 2026 710P @ $14.87 = $1,487, TS acct 12075036, order 1292226101,
10:29 CT, final day of the entry window with entry conditions back in
compliance (VIX 17.4, SPY 742.55). Exits per plan unchanged; flat by early Nov.
Tranche 2 (Aug 10-21, VIX <15): use margin/main broker if the spread is wanted.

## Amendment 2026-08-04 (Omar, pre-decided 3 days ahead): tranche-2 evaluation
moved UP from Mon 8/10 to FRIDAY 8/7 IMMEDIATELY AFTER the jobs data.
Decision framework, frozen now so Friday is execution not improvisation:
- Jobs WEAK + VIX spiking (>18): NO add — that's chasing insurance into
  panic; tranche 1 is the payer, exit ladder (VIX>28 = sell into fear) takes
  over. Adding into a spike violates the plan's own buy-it-cheap principle.
- Jobs benign/strong + VIX <15: original window condition met one day early
  WITH the catalyst answered -> ADD tranche 2 (prefer the 710/600 spread if
  margin/main-broker is ready; long-put fallback documented like tranche 1).
- Muddle (VIX 15-16.5, mixed print): present live pricing + both cases,
  Omar decides same-day.
Prep still open before Friday: enable margin on TS or confirm main-broker
routing so the SPREAD structure is actually placeable (7/31 rejection).

### STRUCTURE DECIDED 2026-08-06 (Omar, pre-jobs): LONG PUT ONLY — no spread.
Omar's call, made the evening before the tranche-2 decision so Friday is
execution not improvisation. Consequences, all deliberate:
- The margin/main-broker prep item above is CLOSED — not needed, no action.
  The 7/31 spread rejection can no longer delay or reshape a tranche-2 fill.
- Structure = 1x SPY Nov 20 2026 710 PUT, same contract as tranche 1
  (14.87 fill). Plan line 13 already documents the naked 710 put as the
  sanctioned structure when >20-25% coverage is wanted, so this is a
  documented variant, not a deviation.
- Payoff differs from the spread: no short leg means no $9,580 cap and no
  premium offset — full premium at risk, unlimited-to-zero payoff below 710.
  Cheaper to be wrong about timing, more expensive to be wrong about
  direction.
- Live pricing at the 8/6 close: Nov 710P mid 8.86 (bid 8.85 / ask 8.88,
  OI 2,735) = ~$886, i.e. 40% CHEAPER than tranche 1's $1,487 six sessions
  ago. VIX 15.31 (-21.7% on the week, below its 20d 17.18). The plan's
  "buy it cheap on a VIX print <15" condition is essentially met — the
  jobs print is the only open variable.
- UNRESOLVED TENSION to settle Friday, flagged now: the hedge-board alert
  spec says VIX 15 + SPY >760 = "thesis delayed, consider cutting half",
  and VIX 14 + SPY >765 = the pre-agreed CUT signal. SPY closed 768.86,
  already past 765. So the same rulebook can order an ADD and a CUT off
  the same tape. Jobs is the tiebreaker; do not resolve it by preference.
- **DIRECT CONTRADICTION SURFACED 2026-08-06 PM — resolve it Friday, do not
  let both run by default.** The A-List's first live run carded SPXL (3x long
  S&P, readiness 56) the same evening. Omar's stated intent: "we may get a good
  jobs report and SPY may continue to rally, in which case we would want to
  switch into SPXL and out of the SPY put." That is the OPPOSITE of the
  tranche-2 rule frozen on 8/4, which says a benign/strong print with VIX <15
  = ADD a second put because insurance got cheap. Same print, same branch, two
  opposite actions. Both are defensible on their own terms — the frozen rule
  expresses the multi-month midterm-correction thesis (Oct low), the SPXL
  instinct expresses a tactical momentum view — but running both means paying
  for insurance while simultaneously levering long, which nets to noise and
  costs two premiums. Friday must pick ONE of: add tranche 2 / rotate to SPXL /
  do neither. Whichever Omar picks, the OTHER one is logged as a graded skip.
### OMAR'S THESIS + EXIT PLAN, pre-registered 2026-08-06 PM (grade in Sept/Oct)
Stated in his words: SPX may see a steep correction **mid-Aug to mid-Sept**;
he entered tranche 1 on the yen/USD carry unwind plus an expected bad jobs
print; **if tomorrow's print beats, he EXITS the put** rather than let it decay,
and **re-enters around the Sept FOMC (Sept 15-16, with dot plot)** as the next
catalyst.
- Reconciliation with the original plan: NOT a contradiction. Plan line 6 says
  the midterm low forms late October; Omar's window is when the decline gets
  STEEP. A correction that turns down mid-Aug and bottoms late Oct satisfies
  both, and the Nov 20 expiry covers both.
- Hindsight claim logged for honest grading: he says he should have skipped the
  7/31 entry and bought today instead. TRUE in outcome - 14.87 then vs 8.75 now,
  41% cheaper. But the premium fell BECAUSE the risk receded (VIX 17.4 -> 15.3);
  insurance is always cheaper after the scare. The generalizable fix is a
  volatility CONDITION on tranche entries, which tranche 2 already has ("ideally
  on a VIX print <15") and tranche 1 lacked (time-boxed only). Fix the design,
  don't grade the outcome. (Minor factual: the fill was Fri 7/31 10:29 CT, not
  Monday.)
- THE FLAW TO WEIGH, stated plainly: exiting now and re-entering 9/16 means
  being UNINSURED through the first half of his own stated danger window, and
  the re-entry price is asymmetric - cheap only if nothing happens, expensive
  exactly when it's needed. Modelled Nov 710P at 9/16 (65d left, IV held 18.3):
  SPY flat -> 3.76 (re-entry saves ~$500) | SPY -5% -> 11.76 (costs 34% MORE to
  re-enter, and +$301 of gain forgone) | SPY -8% -> 20.70 (2.4x, +$1,195
  forgone). **The exit plan is only profitable if his own thesis is wrong about
  timing.** Desk recommendation if the print beats: cut HALF, not all - theta is
  5.9%/week (~$52), which is not an emergency worth vacating the window for.
- Thesis leg still alive as of 8/6: USDJPY 158.45, **-3.0% on the week**, broken
  below its 50d (161.18) and sitting ON its 200d (158.02). The carry-unwind leg
  has NOT been invalidated; a break of 158 is the confirmation to watch.
- Process guard (this plan was missed once already — see 7/27 process note):
  one-shot cloud reminder trig_016kjtth2eemMP6JpneoWiiy fires 7:45 CT
  Fri 8/7, ~15 min after the print. Local session also owes it in the
  Friday brief. Two independent paths, because the cloud one failed before.

## Companion pre-decision 2026-08-04 (Omar): GE REAL CALL EXITS THURSDAY 8/6
Pre-jobs de-risk, decided 2 days ahead: the real GE Sep 350 call (entry
28.00) is SOLD on Thursday 8/6, worked as a limit into strength (never
market into the wide spread), position flat by Thursday's close regardless
of price. Rationale logged: banks the most coil-extended winner before the
jobs binary, keeps the younger UAL call + the SPY put into Friday - put
holds with banked profit behind it. Earlier triggers SUPERSEDE if they fire
first (target 56 / thesis-break 342 / checkpoint-380 judgment). UAL call is
explicitly NOT part of this - it runs on its own plan.

## EXECUTION RECORD - Tranche 1 CLOSED (2026-08-07)
SOLD 1 SPY Nov 20 710P @ 8.52 (~08:5x CT, Omar-reported). P&L -$635 (-42.7%,
7 days). Jobs missed (57k vs ~83k) but the tape rallied and VIX fell - Omar:
"no meaningful hurdles for market to react negatively to." Tranche 2 = NOT
ADDED (same logic). The 8/6 "one decision" resolved as: EXIT the put, no SPXL
rotation decided yet. BOOK IS NOW UNHEDGED.
RE-ENTRY (pre-registered 8/6, stands): around the Sept 15-16 FOMC as the next
catalyst - or EARLIER if the hedge board fires (VIX 20 up-cross + SPY <735
breadth break = thesis working without us; re-underwrite, don't chase).
The VIX 15/14 hedge-board alerts now read as RE-ENTRY timing signals, not
cut signals - no position to cut.
