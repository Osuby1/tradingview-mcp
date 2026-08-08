# Winner Score v1 — pre-registration (2026-08-07, committed BEFORE any backtest runs)

Omar's go, with the explicit order: avoid overfitting. These are the structural
guards, then the frozen score, then the frozen pass bars. Nothing below changes
after this commit. If v1 fails, it FAILS — a v2 would need a fresh
pre-registration and fresh data, never a tweak-until-it-passes loop.

## Anti-overfitting guards (the design, not a promise)
1. **Inputs restricted to traits ALREADY validated independently** (8/7 traits
   scan + detector study). No new features may be added because they "help."
2. **No fitted weights.** Simple a-priori point scheme below — no optimizer, no
   parameter search, no iteration. One score, one shot per dataset.
3. **Threshold provenance declared:** the cut levels come from the July traits
   scan, which makes the July hold-out only weakly out-of-sample for them. The
   REAL out-of-sample tests are (a) the two-year replay across three separate
   regime windows the thresholds never saw, and (b) forward shadow on live
   cards. A win only on July data counts as NOTHING.
4. **Regime-split consistency required** — pooled significance alone can be one
   lucky window; the score must work in at least 2 of 3 disjoint windows.
5. **Survivorship acknowledged:** the replay universe is today's ~470-name
   universe, i.e. names that survived to be on today's lists. This inflates
   absolute returns; it inflates ALL RANKERS EQUALLY, so the comparison (score
   vs incumbents, top vs bottom bucket) remains fair. Absolute numbers from the
   replay are never quoted as expected returns.
6. **Few comparisons:** exactly one composite tested against two incumbents.
   No feature scan, no threshold grid.

## The frozen score
**WS-traits (0–6), computable on any flag, any era:**
- Trend strength: ADX ≥ 27 → +1; ≥ 35 → +2
- Buyer margin: (DI+ − DI−) ≥ 10 → +1; ≥ 18 → +2
- Established trend: ≥ +10% above the 200-day → +1
- Size: 20-day dollar volume between $20M (hard floor) and $200M → +1

**WS-full = WS-traits + detector source** (live lane only; replay has no tabs):
orig-COILED +2 · FRESH IGNITION +1 · sweep-CE +1 · BUY ZONE +0 · COOLING = excluded (veto).

## The frozen tests
- **T1 July hold-out:** score all first-recommendations 7/1–7/25, grade forward
  returns of 7/26–8/7 flags top-half vs bottom-half. Directional check only.
- **T2 Replay (the real test):** simulate Chandelier BUY flips over ~2 years on
  the current universe; score each flip day with WS-traits (no look-ahead);
  measure +10/+21-session returns vs SPY by score tercile across three windows:
  W1 = Aug 2024–Feb 2025, W2 = Mar 2025–Sep 2025, W3 = Oct 2025–Aug 2026.
- **T3 Race:** on identical historical pools, WS ranking vs readiness ranking
  vs Buy Score ranking (wherever incumbents' stored values exist) — nightly
  top-3 forward returns.
- **T4 Stop-width (the holding half of selection):** on replayed flips, stop at
  the 10-day low vs the same stop one ATR wider; count flags reaching +15%
  before the stop under each; expectancy normalized to $5k risk per trade.

## The frozen pass bars (ALL required before shadow → promotion)
1. T2: top-tercile beats bottom-tercile on +21 excess-vs-SPY in ≥2 of 3
   windows AND the pooled difference's bootstrap 95% CI excludes zero.
2. T1: direction agrees (top ≥ bottom). Weak evidence, necessary not sufficient.
3. T3: WS top-3 ≥ readiness top-3 on forward returns over the comparable pools.
4. THEN: 2–3 weeks forward shadow on live cards (separate script, zero touch of
   the live pipeline), agreement with backtest direction.
5. THEN: presented to Omar as a decision. Nothing auto-promotes. A failure at
   any bar is reported as loudly as a pass.
