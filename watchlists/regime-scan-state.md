# Daily Regime Scan State

Rolling state file for the local live-feed regime scan (price vs 200SMA, ADX-14, Chandelier Exit 22/3, RSbeat, Early Ignition / Lift-Off flags). Refresh daily; diff against the prior snapshot for the morning brief.

Scan stack (chart method): HQ Swing v1 - Regime Breakout, ADX 14 + 20 Threshold, Chandelier Exit, Early Ignition, Lift-Off Detector.
**METHOD CHANGE 2026-07-06:** `layout_switch` to the HQ Swing v1 layout is broken (silent no-op) and `chart_manage_indicator` can't add the custom scripts. This scan was computed **in-page via `ui_evaluate`** directly from the chart's main-series bars (same live feed), replicating the exact formulas: SMA200, `ta.dmi(14,14)` ADX, Chandelier 22/3 (close-extremum variant — matches prior recorded stop values), RSbeat = 126d return > SPY 126d return (+9.56% this run), Early-Ignition Tier-1/Tier-2 conditions from `pine/early_ignition.pine`. Lift-Off Detector NOT evaluated (source not in repo). **ADX re-baselined** — computed values run higher than the old chart-study column (e.g. DTE 17.6 → 29.0 same week); do not diff ADX levels across the method change, only the >20 verdict.

**METHOD NOTE 2026-07-08:** `TradingViewApi.activeChart().exportData()` now returns "Data export is not supported" — bars are read instead via the MCP server's own internal path (`window.TradingViewApi._activeChartWidgetWV.value()._chartWidget.model().mainSeries().bars()`, `valueAt()` loop — same live feed, synchronous). Intraday runs drop today's partial bar; indicator values = last COMPLETED close, with the live price reported separately. "Close" column is the chart-feed close (Cboe One can miss the closing auction — e.g. DTE chart 153.53 vs official 154.28 on 7/7).

## Latest — 2026-07-08 ~10:05 ET (indicators = 2026-07-07 completed close; Live = ~10:00 ET print)

| Symbol | Close 7/7 | Live | 200SMA | % vs 200d | ADX | Chandelier | RSbeat | Flags | Verdict |
|--------|-----------|------|--------|-----------|-----|------------|--------|-------|---------|
| CB | 359.87 | 358.42 | 312.04 | +15.3% | 27.5 ↑ | LONG 334.74 | 1 | — | PASS strong |
| DTE | 153.53† | 153.02 | 140.95 | +8.9% | 30.1 ↑ | LONG 145.01 | 1 | — | PASS strong († official 7/7 close 154.28 = gate hit; back under 154 this AM) |
| AMGN | 371.00 | 365.93 | 336.06 | +10.4% | 21.6 ↑ | LONG 340.90 | 1 | — | PASS |
| KRE | 75.45 | 74.23 | 66.81 | +12.9% | 35.7 ↑ | LONG 71.23 | 1 | — | PASS strong (74.00 dip alert fired 7/8 AM) |
| XLI | 183.12 | 180.22 | 164.85 | +11.1% | 23.7 ↑ | LONG 175.20 | 1 | — | PASS (live only +2.9% above CE stop) |
| JNJ | 266.40 | 267.54 | 219.57 | +21.3% | 35.7 ↑ | LONG 245.20 | 1 | — | PASS strongest (record high; earnings 7/15 ⚠) |
| KO | 84.49 | 84.25 | 74.48 | +13.4% | 25.4 ↑ | LONG 78.88 | 1 | — | PASS strong |
| DAL | 90.12 | 86.23 | 68.39 | +31.8% | 52.0 ↑ | LONG 83.44 | 1 | — | PASS but DETERIORATING fast (IATA cut; live only +3.3% above CE 83.44; $85 stop alert sits above the line = fires early ✓; earnings Fri 7/10) |
| NEE | 88.46 | 88.15 | 86.73 | +2.0% | 21.8 ↓ | SHORT 90.06 | **1** | — | FAIL→improving (RSbeat flipped 0→1; flip line 90.06, alert 89.10 just under) |
| HOPE | 13.45 | 13.15 | 11.61 | +15.8% | 33.4 ↑ | LONG 12.83 | 1 | — | PASS strong (earnings 7/21) |
| SPY* | 748.53 | 743.72 | 693.05 | +8.0% | 22.3 ↓ | **SHORT 758.52** | — | — | *new row — CE flipped short during the July pullback |
| QQQ | 711.21 | 704.27 | 636.01 | +11.8% | 23.1 ↓ | LONG 697.43 | 1 | — | PASS — **FLIP WATCH: live just +1.0% above the 697.43 line** |
| IWM | 297.63 | 292.63 | 261.24 | +13.9% | 13.7 ⚠ | LONG 283.21 | 1 | — | PASS (trendless chop) |
| SMH | 578.57 | 580.07 | 428.61 | +35.0% | 23.9 ↓ | **SHORT 649.25** | 1 | — | **FLIPPED SELL 7/7** (first flip in ~3 months; short stop will ratchet down) |
| NET* | 264.00 | 264.31 | 208.51 | +26.6% | 19.9 ↑ | LONG 219.66 | 1 | — | *new row — PASS (day 2 of base >260; rvol 1.46; ADX 19.9 knocking on 20) |
| BMNR | — | — | — | — | — | — | — | — | NOT SCANNED — feed returned an empty series for BMNR this session (quote_get also failing); book flat, watch only |

No Quality-Ignition / Spec-Ignition conditions met on any scanned name (max RVOL = NET 1.46x).

### Deltas vs 2026-07-06 snapshot
- **SMH Chandelier FLIPPED SELL** (LONG 585.98 → SHORT) — the real flip, confirmed in this method at the 7/7 close (official 576.19). This is what the 7/2 phantom falsely previewed.
- **SPY (added) computes CE SHORT** — flipped during the July pullback week. With SMH short, **QQQ is the two-flip character-change tell: a daily close < 697.43 confirms**. Watch into/after today's 2 PM Fed minutes.
- **NEE RSbeat flipped 0→1** (126d +9.9% vs SPY +9.5%) — second consecutive improvement (200d cross 7/6, RS 7/7). Still CE SHORT; flip line 90.06.
- **DAL deteriorating inside a PASS**: −3.0% on 7/7 (IATA halved 2026 airline profits on doubled jet fuel) and another −4.3% live 7/8; from +11% above its CE stop (7/6) to +3.3% live. ADX 52 = blow-off trend rolling over. Earnings Fri 7/10.
- **JNJ new record** (266.40, live 267.5; +3.4% on 7/7 on PT raises + MEMBRANE data) — strongest name on the board. Earnings Wed 7/15 → position-window flag from ~7/11.
- Stop-alert staleness (CE lines ratcheted again): **CB alert 323 vs CE 334.74 — worst on the board, −3.3% of protection given up**; AMGN 336 vs 340.90 stale-low; **JNJ 243 vs 245.20 — newly stale-low** (line crossed above the alert since 7/6); XLI 174.50 vs 175.20 marginal; KRE 71.30 vs 71.23 aligned; DTE 146.50 / KO 79 / DAL 85 sit at-or-above their lines (fire early — conservative, OK).
- ADX firming across defensives (CB 27.5, KO 25.4, JNJ/KRE 35.7 — all rising); IWM still trendless (13.7).

## Prior — 2026-07-06 ~16:45 ET (values = 2026-07-06 daily close, live feed via ui_evaluate)

| Symbol | Close | 200SMA | % vs 200d | ADX | Chandelier | RSbeat | Flags | Verdict |
|--------|-------|--------|-----------|-----|------------|--------|-------|---------|
| CB | 357.43 | 311.61 | +14.7% | 24.9 | LONG 332.75 | 1 | — | PASS strong |
| DTE | 152.69 | 140.86 | +8.4% | 29.0 | LONG 145.01 | 1 | — | PASS strong (probed 154.41 intraday) |
| AMGN | 367.90 | 335.58 | +9.6% | 20.2 | LONG 339.73 | 1 | — | PASS |
| KRE | 75.23 | 66.75 | +12.7% | 34.0 | LONG 71.14 | 1 | — | PASS strong |
| XLI | 185.35 | 164.69 | +12.5% | 24.4 | LONG 175.20 | 1 | — | PASS strong |
| JNJ | 259.22 | 219.13 | +18.3% | 33.0 | LONG 238.68 | 1 | — | PASS strong |
| KO | 83.48 | 74.39 | +12.2% | 23.4 | LONG 78.03 | 1 | — | PASS strong |
| DAL | 92.91 | 68.24 | +36.2% | 52.9 | LONG 83.44 | 1 | — | PASS strongest (extended) |
| NEE | 87.83 | 86.64 | **+1.4%** | 22.7 | SHORT 90.10 | 0 | — | **FAIL→improving: crossed ABOVE 200d** |
| HOPE | 13.54 | 11.60 | +16.8% | 33.0 | LONG 12.83 | 1 | — | PASS strong (earnings 7/21) |
| QQQ | 721.82 | 635.40 | +13.6% | 22.9 | LONG 697.43 | 1 | — | PASS (ROC-21 −3.1%, still cooling) |
| IWM | 298.67 | 260.95 | +14.5% | 14.7 ⚠ | LONG 283.08 | 1 | — | PASS (trendless chop) |
| SMH | 608.40 | 427.25 | +42.4% | 23.8 | **LONG 585.98** | 1 | — | PASS — see correction below |
| BMNR† | 15.08 | 29.21 | −48.4% | 30.9 | SHORT **17.29** | 0 | — | FAIL regime (open book position — counter-trend ETH proxy) |

† BMNR added 7/6 (Omar's 7,500 @ 15.75 position). CE flip line per this method = 17.29, slightly above the 16.93 alert wired at entry.

No Quality-Ignition / Spec-Ignition conditions met on any scanned name. No Chandelier flips today.

### ⚠ CORRECTION — the 7/2 "SMH Chandelier SELL flip" was FALSE (bad data)
The 7/2 EOD addendum recorded SMH 655.89 (6/30) → 620.46 (7/1) → 592.29 (7/2, "flip SELL"). The real NASDAQ series (verified 7/6 on-chart legend: 7/6 close 608.40 **+0.35%**) is **646.57 → 628.33 → 606.29 → 608.40**. The −9.7%/two-day crash never happened (real two-day was −6.2%) and the 22/3 Chandelier **never flipped — SMH has been LONG throughout** (stop now 585.98, last flip ~3 months ago). The 7/2 session's own warning about contaminated `data_get_study_values` applied to the screenshot reads too. Consequences: the SOXS tactical was armed on a phantom signal (correctly never taken — now stood down); the "QQQ second-flip = character change" watch is moot. Index chart feeds (DJ_DLY:DJI, SP:SPX) are DELAYED — their "last" lags the official close by ~15 min right after the bell (7/6: chart DJI 52,898 vs official close 53,055.91). Use the symbol-details pane / official quote for closes pulled within ~20 min of the bell.

### Deltas vs 2026-07-02 snapshot
- **NEE crossed ABOVE its 200SMA** (−0.1% → +1.4%) — first regime improvement since it went FAIL. Chandelier still SHORT; computed flip ≈ 90.10, so Omar's NEE 89.10 breakout-confirmation alert sits just UNDER the flip line (fires slightly early — fine).
- All Tier-1 names still PASS; no flips; broad up-day (KO/JNJ/CB/AMGN defensives strong).
- Chandelier stops ratcheted up again — stop-alert staleness check: **CB alert 323 vs CE 332.75 (very stale-low, worst on the board)**, AMGN 336 vs 339.73 (stale-low), XLI 174.50 vs 175.20 (marginal), KRE 71.30 vs 71.14 (now aligned), DTE 146.50 / JNJ 243 / KO 79 / DAL 85 all sit at-or-above their CE lines (fire early — conservative, OK).
- ADX column re-baselined (see method note) — treat 7/6 as the new baseline for trend-strength diffs.

(7/2 snapshot table removed 7/8 — two generations old; its lasting lesson lives in the correction note above.)
