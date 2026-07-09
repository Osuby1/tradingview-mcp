# WALK-FORWARD BACKTEST — SMH (Daily, Candles) — 2026-06-24
Worked example of the [Quant Backtest Protocol](../quant-backtest-protocol.md) (Gap 4).

**Symbol:** SMH (VanEck Semis ETF), Daily, normal candles (verified chartType=1, not Heikin-Ashi).
**Strategy:** "HQ Swing v2 - Regime+Vol+Risk" — 200MA + ADX>20 + 20-bar breakout + SPY>200MA regime filter + volume confirm + ATR trailing stop. **Costs modeled:** 0.05% commission/trade + 1-tick slippage, $10k initial, 100% equity. Metrics below are NET of costs.

## Per-window metrics
| Metric | In-Sample (from 2015-01) | Out-of-Sample (from 2023-07) | Buy & Hold SMH |
|---|---|---|---|
| Net P&L % | +1.54% | +0.32% | hundreds of % (5Y ~+382%) |
| Profit Factor | 1.191 | 1.257 | n/a |
| Total trades | **16** | **4** | 1 |
| % Profitable | 50% | 50% | — |
| Max Drawdown | 3.26% | 1.11% | far larger |
| Sharpe | −0.328 | −0.599 | — |

## Verdict vs gates
- **(a) OOS holds vs IS?** Marginally yes (PF 1.19→1.26, tiny DD) — but meaningless given sample size.
- **(b) Trades >~30?** **FAIL badly** — 16 in 11y, only 4 OOS. Filters so restrictive it almost never fires.
- **(c) Beats buy-and-hold?** **FAIL catastrophically** — sits in cash ~99% of the time on a structural-bull ETF; B&H wins by orders of magnitude.
- **(d) PF >~1.3 net?** **FAIL (borderline)** — 1.19 / 1.26, and on 4–16 trades PF is noise.

## Tooling limitations hit
1. **`chart_set_visible_range` does NOT re-scope the Strategy Tester** — true window-splitting had to use the strategy's own `startDate` input, not chart zoom.
2. Chart had only ~300 daily bars loaded locally — older-window local OHLCV math not possible (server-side tester still computes full history).
3. **`data_get_strategy_results` returned metric_count:0** (confirmed broken) — metrics scraped via `ui_evaluate` DOM workaround.
4. Strategy exposes only a START date (no END) → could only do early-start vs recent-start; OOS is a recency subset, not a fully isolated partition (weakens walk-forward purity).
5. TV's buy-&-hold benchmark is a chart, not a labeled value; dollar figure distorted by SMH's ~2000 inception price — directional only.
6. Pine-editor single-script binding: attaching v2 consumed the editor's bound study slot (replaced the "Early Ignition" entity 8dAQhO). **NOTE for next local regime scan: re-add Early Ignition / re-verify the study set.**

## Conclusion
**Not deployable — and not properly testable on SMH as-is.** So heavily filtered it produced 16 trades in 11 years (4 in the last ~3) — far below significance. Where it trades it's barely profitable net of costs (PF ~1.2, negative Sharpe, CAGR ~0) while forgoing nearly all of SMH's trend; loses to buy-and-hold by orders of magnitude. Not overfit (OOS≈IS) and DD trivial — but there's no edge to overfit. To make it testable: (1) loosen filters to >30 trades/window, (2) run on a basket / longer history for sample size, (3) add an explicit end-date input for true non-overlapping walk-forward windows. **This is exactly the protocol working as intended — it killed a strategy that a single full-history number might have flattered.**
