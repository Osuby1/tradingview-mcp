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
