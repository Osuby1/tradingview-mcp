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
- **Always read on plain CANDLES**, never Heikin Ashi (HA changes the buy/sell
  answer on ~22% of names).

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
1. Market & Rotation · 2. Fresh Buys (ranked) · 3. Plans (sized) · 4. Blocked
(worst-first) · 5. Sell Mode · 6. Tracker Broken · 7. Notes & Decisions · 8. Market
Movers · 9. Track Record · 10. Data Quality (read the red BLOCKERS first) · 11. Run
Summary. Plus the EOD brief and the HQ Swing three-bucket lens.

---

## 5. How to run it (the pipeline)

1. `build_extended_universe.py` → today's ~480-name universe
2. `og_sweep_runner.js` (in the live TradingView chart) → reads Chandelier / ZLSMA /
   Magical + computes regime, ADX, DI, ATR, dollar-volume — **on candles**
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
  up." The gates (rejections) are what work; the ranking is a sort.
- The sweep needs the **live TradingView chart open** to read the indicators.
- The fully-automated evening run (`run_eod_chain.bat`, Windows Task Scheduler) is
  **currently DISABLED** — switched off 2026-07-22 to fix a bug where it shipped
  yesterday's report labeled as today's. It is fixed and now fails loudly instead;
  re-enable in Task Scheduler when you want it unattended.

---

## 7. The rule that ties it together

Every recommendation is **pre-registered and graded** against what actually happened
and against just buying SPY (`calls-ledger.json` → `outcome_tracker.py`). We measure
ourselves, so the pretty-but-false signals get caught instead of believed.
