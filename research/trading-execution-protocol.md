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

## Claude's enforcement duties (unprompted)
Grade every fill vs plan price (flag chases >0.5%) · wire stop+context alerts on every position, entry-ladder alerts on every plan · delete stale alerts on exits · log deliberate SKIPs with reference prices · quote $ risk on every idea · raise sizing/pain flags at entry, not after · every idea ships complete (level, halves, stop, $ risk, verified earnings, catalyst, ZLSMA verdict, wired alert)

## Detection stack (daily)
Rotation Radar (groups, AM+EOD, `scripts/rotation_radar.py`) → Ignition Sweep (names, market-wide, EOD, `scripts/ignition_sweep.py`) → convergence rule (LOADED name in WATCH/IGNITING group = top candidate) → volume-gated trigger alerts → ledger/tracker scorecard. Sector+rotation commentary in all three daily briefs.
