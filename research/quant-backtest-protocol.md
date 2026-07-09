# Quant Backtest Protocol — Walk-Forward & Out-of-Sample (Gap 4)

**Purpose:** stop trusting single full-history backtest numbers (they overfit). Before any strategy is deployed or sized up, it must clear this protocol. A strategy that looks great in-sample but collapses out-of-sample is noise, not edge.

**Where this runs:** LOCAL only — the live TradingView desktop via MCP (Strategy Tester). Not a daily cloud-brief item; it's a per-strategy validation **gate** run on demand.

## Hard rules (institutional discipline)
1. **Normal candles, never Heikin-Ashi.** HA charts inflate backtests massively (known finding). Confirm chart type before testing.
2. **Costs ON.** Commission + slippage must be modeled. If the strategy runs 0 commission, results are *gross/optimistic* — flag it explicitly and haircut.
3. **Out-of-sample split.** Evaluate over ≥2 non-overlapping windows:
   - **In-Sample (IS):** older period for "did it ever work."
   - **Out-of-Sample (OOS):** recent period it was *not* tuned on — the real test.
   - Use `chart_set_visible_range` (unix ts) or `chart_scroll_to_date` to scope windows; if the tester won't re-scope to the window, report full-period + a clear caveat.
4. **Significance.** Need a meaningful trade count (**>~30**, ideally per window). A 0.9 profit factor on 12 trades proves nothing.
5. **Benchmark.** Compare to **buy-and-hold** of the same symbol over the same period. A strategy that underperforms B&H net of costs is not worth the risk/effort.

## Metrics to capture per window
Net P&L %, **Profit Factor**, Total trades, % Profitable, **Max Drawdown**, (expectancy if available). Tabulate **IS vs OOS vs Buy&Hold**.

## Verdict gates (all must pass to deploy)
- [ ] OOS holds up vs IS (no collapse) — *the overfit test*
- [ ] Trade count > ~30 per window — *significance*
- [ ] Beats buy-and-hold net of costs — *worth doing*
- [ ] Profit Factor > ~1.3 **net of costs** — *real edge margin*

Fail any → **do not deploy**: re-tune (looser params / higher timeframe / add a regime filter) or shelve. Known prior result: the Chandelier+ZLSMA strategy with default params is a net loser on daily equities (whipsaw) — the *regime filter* (200SMA + ADX), not the indicator, is the edge.

## ⚠️ Do not clobber live indicator slots
Attaching/saving a strategy uses the Pine editor's **single bound script slot**. On 2026-06-24 a backtest saved "HQ Swing v2" into the **Early Ignition** slot and overwrote it (recovered via TV Version history). RULE: before backtesting, **Make-a-copy into a throwaway slot** (or use a dedicated strategy script) — never `pine_save` into one of Omar's live indicator slots (Early Ignition, Lift-Off Detector, Chandelier, HQ Swing v1). Sources backed up under repo `pine/`.

## MCP execution notes
- Attach a strategy: `ui_open_panel pine-editor open` → `pine_open "<name>"` → `ui_find_element "Add to chart"` then `ui_mouse_click` its coords (ui_click by text/aria-label does NOT match this button). `pine_smart_compile` only SAVES; it does not add to chart. Once attached it re-runs on symbol/timeframe/range change.
- Read results: `ui_open_panel strategy-tester open`, then prefer `data_get_strategy_results`; it OFTEN returns metric_count:0, so fall back to `ui_evaluate` scanning divs for "Total P&L … Max equity drawdown … Total trades … Percent profitable … Profit factor".

## Worked example
See `research/examples/2026-06-24-backtest-SMH.md` — walk-forward read on SMH daily (IS vs OOS vs B&H) with the verdict against each gate and the tooling limitations hit.
