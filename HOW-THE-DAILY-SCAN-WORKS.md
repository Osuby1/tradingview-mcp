# How the daily scan works

*Plain-English reference. Written 2026-07-22. "Run the universe" = the daily/EOD scan; same thing.*

---

## In one line

Sweep every stock you follow through the O.G Chandelier signal, keep only the ones
that also pass the HQ Swing v1 trend filter and the risk gates, and hand you a
ranked, gated, plain-English workbook — plus a scorecard that grades what we said
against what actually happened.

---

## 1. What stocks it runs against (the universe)

Built fresh each run from **repo files, combined and de-duplicated** — about **480
names**. It is the union of:

| Source | ~count |
|---|---|
| Main watchlist (`watchlists/main-watchlist.md`) | 179 |
| HQ Swing watchlist (`watchlists/hq-swing.md`) | 94 |
| Sector Themes watchlist (`watchlists/sector-themes.md`) | 37 |
| Origination scanner tabs — Buy Zone + Fresh Ignitions + Coiled | 210 |
| **Tracked names** — anything with a live/recently-fired alert or a recent plan | rescues ~40 |

Built by `scripts/build_extended_universe.py` (+ `tracked_symbols.py`).

**Two hard rules:**
- **Never** use the live TradingView watchlist reader — it silently returns only
  ~1/3 of the list (this is why SMCI was missed). Always build from the repo files.
- **Always read on HEIKIN ASHI** (Omar's standing decision 2026-07-23, which
  reversed the earlier candles-only rule). Chart type matters a lot — HA vs candles
  changes the buy/sell answer on ~22% of names and the flip date on ~72% — so never
  mix the two in one run, and note that HA runs are not comparable to the pre-7/23
  candle history. (Backtests are the one exception: those still use normal candles,
  because HA inflates backtests — see `research/quant-backtest-protocol.md`.)

---

## 2. What each stock is compared against — TWO layers

**Layer 1 — the O.G Chandelier stack (the SIGNAL: "a buy just fired"):**
- **Chandelier Exit** — the buy/sell flip
- **ZLSMA** — the trend line (price must be above it)
- **Magical (overbought / oversold)** — 20-period CCI, ±100 bands

**Layer 2 — HQ Swing v1 (the FILTER: "is this a real trend"):** now a mandatory
gate every candidate must clear, and also run as its own three-way lens.

A name only becomes a real candidate when **Layer 1 fires AND Layer 2 passes.**
That pairing is what correctly killed the GDX trade (Chandelier said buy, HQ Swing
said no).

---

## 3. The full gate stack (a candidate must pass ALL) — `scripts/gate_stack.py`

1. **Regime** — above a rising 200-day average and the 50-day *(HQ Swing core)*.
   More than 10% below the 200-day = no trade, ever.
2. **Trend** — ADX ≥ 20 *(HQ Swing)*.
3. **Direction** — buyers in control, +DI over −DI *(HQ Swing)*.
4. **Structure** — price above the ZLSMA *(Chandelier's own test)*.
5. **ATR floor** — stop is 1–4× the average daily range (not inside the noise, not
   so wide the position is a token).
6. **Stop cap** — stop no more than ~12% away (so 2:1 is reachable).
7. **Liquidity** — the position is a small slice of a day's dollar volume.

The gates **fail closed**: if the data to check a gate is missing, the name is
blocked, never passed. This is the scan's real strength — knowing what *not* to buy.

---

## 4. What comes out — the workbook (`reports/universe_<date>.xlsx`)

11–12 tabs, every column with a plain-English tooltip:
1. Market & Rotation · 2. Fresh Buys (ranked, ≤5-bar flips) · 2b. Gated Longs (ALL
ages — every BUY name that clears the full gate stack, ranked least-extended first,
so established uptrends like DVN/PBR surface too) · 3. Plans (sized) · 4. Blocked
(worst-first) · 5. Sell Mode · 6. Tracker Broken · 7. Notes & Decisions · 8. Market
Movers · 9. Track Record · 10. Data Quality (read the red BLOCKERS first) · 11. Run
Summary. Plus the EOD brief and the HQ Swing three-bucket lens.

---

## 5. How to run it (the pipeline)

1. `build_extended_universe.py` → today's ~480-name universe
2. `og_sweep_runner.js` (in the live TradingView chart) → reads Chandelier / ZLSMA /
   Magical + computes regime, ADX, DI, ATR, dollar-volume — **on Heikin Ashi**
   (it refuses any other style unless forced)
3. `build_universe_results.py` → applies the gate stack (`gate_stack.py`)
4. `hq_swing_lens.py` → the three-way Chandelier-vs-HQ-Swing comparison
5. `rotation_radar.py` + `ignition_sweep.py` → sector rotation + market-wide ignitions
6. `compile_universe_report_v2.py` → the workbook (auto-verified by
   `verify_eod_output.py`)
7. Scorecard: `dump_call_prices.py` → `outcome_tracker.py` → grades every call vs SPY

---

## 6. Honest caveats (do not skip)

- The **ranking of survivors is UNPROVEN** — measured 2026-07-22, it does not
  forecast returns. Use the order as "look at these first," never as "these will go
  up." The ranking is a sort, not a forecast.
- **The gates are unproven too — corrected 2026-07-25.** This document used to say
  "the gates (rejections) are what work." That was an assertion, never a
  measurement. `scripts/gate_outcomes.py` now grades the cull forward: it buckets
  every fresh signal into PASSED vs BLOCKED and compares their returns. First run
  showed a spread of **−0.11 percentage points** — i.e. no detectable edge — but
  **nothing has matured yet**, so there is no verdict in either direction. Read
  `research/gate-outcomes.md` before repeating any claim about what the gates buy
  you. If the spread stays flat as the sample grows, the stack is costing
  opportunities without buying safety.
- The sweep needs the **live TradingView chart open** to read the indicators. This
  is the system's single biggest fragility — it is what broke the nightly run on
  7/21 and 7/24. `scripts/og_shadow.py` is the chart-free lane that would remove
  the dependency; as of 2026-07-25 it matches the chart on 85.8% of names, which is
  not good enough to promote (Omar's call after 8/31).
- The fully-automated evening run (`run_eod_chain.bat`, Windows Task Scheduler task
  "EOD Universe Chain", weekdays 15:15 CT) is **ENABLED and runs the FULL pipeline**:
  gate-stack unit tests (step 0 — a failing gate refuses the whole run), origination
  scan, extended ~480-name universe, Heikin Ashi sweep + gate stack, then the
  deterministic Python analysis (rotation radar, ignition sweep, HQ Swing lens,
  track record, outcome tracker, gate outcomes, shadow grade), then the full 12-tab
  workbook, then a commit. It **fails closed** — a failed scan or verify stops the
  compile and the task exits non-zero with "EOD CHAIN FAILED" in
  `reports\eod_chain.log`, so it can never ship a stale report as today's.
- **The sweep is driven by a plain Node process, not a headless LLM** (fixed
  2026-07-25). `scripts/og_sweep_cdp.mjs` connects over CDP and runs the loop
  itself, so it cannot run out of turn or credit budget — the failure that killed
  the 7/21 and 7/24 nightlies. Soak-tested on the full 494-name universe 2026-07-25.

---

## 7. The rule that ties it together

Every recommendation is **pre-registered and graded** against what actually happened
and against just buying SPY (`calls-ledger.json` → `outcome_tracker.py`). We measure
ourselves, so the pretty-but-false signals get caught instead of believed.
