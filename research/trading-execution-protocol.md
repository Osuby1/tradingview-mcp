# Trading Execution Protocol (permanent — mirrored from Claude memory 2026-07-13)

The stock-picker/risk-manager contract. Applies to every idea, entry, fill, and brief.

## Sizing & risk (Omar, 2026-07-10 → 07-13)
- **Account $1M · max loss per trade $5,000 (0.5%) · typical order $100k (10% position)**
- Position size = min($100k, $5,000 / structure-stop-distance%) — the stop NEVER tightens to fit the size
- Halves: $50k at the level + $50k on confirmation (first tranche risks ≤$2.5k)
- Spec/biotech: $300-risk half-units, 2–3 names max
- **Weekly circuit breaker: −$10k realized (1%) = flat until next Monday**; warn at −$5k week-to-date
- Concentration flags: single position >$150k; >60% of open notional in one radar group; combined open risk >$10k

## Entry rules
1. Limit orders AT the plan level, set in advance — never market after the level is gone
2. Stops at STRUCTURE with an **ATR floor** (≥1.5–2x daily ATR from entry; if 2x ATR > structure distance, the entry is too far from structure — wait)
3. **Reward:risk ≥2:1** measured to the next structure level, or no entry
4. **Volume gates on breakouts:** alert fire = LOOK; projected RVOL ≥1.5–2x = BUY
5. No resting stop-markets on full size — alert → decide → limit into the bounce
6. Binary gates: earnings date VERIFIED before every entry; no fresh entries the day before a print; trim before earnings; no fresh full size into long weekends; crypto re-entry requires a DAILY CLOSE through the level
7. No chasing day-one war/news spikes
8. **ZLSMA gate** (from `pine/zlsma_chandelier_strategy.pine`): longs want close > ZLSMA(50) AND rising; a FAIL is disclosed on the idea, never silent
9. **Chart-verify before entry:** symbol on the live TV chart (daily TF confirmed), read the actual HQ Swing v1 / OG Chandelier OB-OS values — Python/Yahoo ports are approximations, the chart is ground truth
10. **O.G CHANDELIER HARD VETO (Omar-approved 2026-07-17, from Week-1 review):** NO buy of any kind — door fire, leftover call, add, re-entry — while the O.G Chandelier on the chart shows SELL mode on the daily. No exceptions, no "counter-regime tests" (the TXN experiment answered that: gapped through its stop for the week's worst loss). The read comes from the CHART INSTANCE per rule 9, never from a recomputed approximation — the 7/17 review proved recomputed defaults miss the chart's actual signals (IBKR). If the chart can't be read, the entry waits.

## GOVERNANCE — rule freeze & shadow lane (Omar-approved 2026-07-20)
**No new live rules until measured — this is itself a codified rule.**
1. **FREEZE:** the live rule set as of 2026-07-20 (rules 1–10 above + the O.G veto, HQ Swing regime gate, run-watch/exit-watch layers, universe-command phases, sizing/breakers) is FROZEN through **2026-08-31**. Nothing new goes live; no thresholds move. Permitted exceptions, each logged as such in the commit: (a) bug fixes — code not doing what the written rule says; (b) data-integrity fixes (wrong ticker/exchange/feed reads); (c) Omar's explicit override, recorded as an override.
2. **SHADOW LANE:** every new idea (VCP detector, new gates, tweaks) is built as a SHADOW detector: the nightly chain logs its signals + would-be plans in the results JSON under `shadow` with ZERO effect on live plans, alerts, or sizing. Shadow signals are pre-registered and graded on the same +1w/+1m scorecards as live calls.
3. **PROMOTION:** a shadow idea goes live only after ≥20–30 graded out-of-sample signals AND demonstrably better expectancy than the incumbent it would replace or augment — decided at a Friday review, logged with the numbers. No promotion by narrative.
4. **ATTRIBUTION:** every results JSON and plans file carries `system_version` = the git short-hash of the rules in force, so Friday stats segment performance by rule-era and "did that change help?" is answered by a table.
**Why (Omar, 2026-07-20):** six rules were added in the 72 hours after Week-1 with zero graded trades behind them — plausible-rule stacking without measurement is how systems quietly rot. The scorecard earns changes; changes don't earn themselves.

## Claude's enforcement duties (unprompted)
Grade every fill vs plan price (flag chases >0.5%) · wire stop+context alerts on every position, entry-ladder alerts on every plan · delete stale alerts on exits · log deliberate SKIPs with reference prices · quote $ risk on every idea · raise sizing/pain flags at entry, not after · every idea ships complete (level, halves, stop, $ risk, verified earnings, catalyst, ZLSMA verdict, wired alert)

## Detection stack (daily)
Rotation Radar (groups, AM+EOD, `scripts/rotation_radar.py`) → Ignition Sweep (names, market-wide, EOD, `scripts/ignition_sweep.py`) → convergence rule (LOADED name in WATCH/IGNITING group = top candidate) → volume-gated trigger alerts → ledger/tracker scorecard. Sector+rotation commentary in all three daily briefs.
