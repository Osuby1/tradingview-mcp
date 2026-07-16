# Daily Regime Scan State

Rolling state file for the local live-feed regime scan (price vs 200SMA, ADX-14, Chandelier Exit 22/3, RSbeat, Early Ignition / Lift-Off flags). Refresh daily; diff against the prior snapshot for the morning brief.

Scan stack (chart method): HQ Swing v1 - Regime Breakout, ADX 14 + 20 Threshold, Chandelier Exit, Early Ignition, Lift-Off Detector.
**METHOD CHANGE 2026-07-06:** `layout_switch` to the HQ Swing v1 layout is broken (silent no-op) and `chart_manage_indicator` can't add the custom scripts. This scan was computed **in-page via `ui_evaluate`** directly from the chart's main-series bars (same live feed), replicating the exact formulas: SMA200, `ta.dmi(14,14)` ADX, Chandelier 22/3 (close-extremum variant — matches prior recorded stop values), RSbeat = 126d return > SPY 126d return (+9.56% this run), Early-Ignition Tier-1/Tier-2 conditions from `pine/early_ignition.pine`. Lift-Off Detector NOT evaluated (source not in repo). **ADX re-baselined** — computed values run higher than the old chart-study column (e.g. DTE 17.6 → 29.0 same week); do not diff ADX levels across the method change, only the >20 verdict.

**METHOD NOTE 2026-07-08:** `TradingViewApi.activeChart().exportData()` now returns "Data export is not supported" — bars are read instead via the MCP server's own internal path (`window.TradingViewApi._activeChartWidgetWV.value()._chartWidget.model().mainSeries().bars()`, `valueAt()` loop — same live feed, synchronous). Intraday runs drop today's partial bar; indicator values = last COMPLETED close, with the live price reported separately. "Close" column is the chart-feed close (Cboe One can miss the closing auction — e.g. DTE chart 153.53 vs official 154.28 on 7/7).

## Latest — 2026-07-16 ~17:15 ET (values = 2026-07-16 daily close, live feed via ui_evaluate; RS base = SPY 126d +8.21%)

| Symbol | Close 7/16 | 200SMA | % vs 200d | ADX | Chandelier | RSbeat | Flags | Verdict |
|--------|-----------|--------|-----------|-----|------------|--------|-------|---------|
| CB | 343.70 | 314.65 | +9.2% | 23.4 ↓ | **SHORT 345.71** | 1 | — | **⚠ FLIPPED SELL — first Tier-1 casualty (359.87 on 7/8 → 343.70)** |
| DTE | 148.91 | 141.32 | +5.4% | 14.6 ↓ | LONG 146.75 | 1 | — | PASS but tight (+1.5% over stop); ADX collapsed 30→15 |
| AMGN | 371.58 | 339.19 | +9.5% | 13.6 ↓ | LONG 349.57 | 1 | — | PASS |
| KRE | 77.92 | 67.19 | +16.0% | 30.1 | LONG 73.89 | 1 | RVOL 1.4 | **PASS strong — best on board; radar WATCH + sweep Finance-LOADED convergence** |
| XLI | 180.15 | 165.84 | +8.6% | 13.1 ↓ | LONG 176.39 | 1 | — | PASS, trendless |
| JNJ | 249.97 | 222.56 | +12.3% | 28.8 ↓ | LONG 249.76 | 1 | — | **21 CENTS above stop — post-earnings slide from 266 record; flip-watch** |
| KO | 84.92 | 75.09 | +13.1% | 18.1 ↑ | LONG 80.05 | 1 | — | PASS |
| DAL | 86.70 | 69.38 | +25.0% | 30.8 ↓ | LONG 85.46 | 1 | — | PASS but tight (+1.4%), still deteriorating |
| NEE | 89.35 | 87.27 | +2.4% | 15.2 | **LONG 84.57** | 1 | — | **CE FLIPPED LONG + RSbeat 1 = full PASS (was FAIL→improving). Flip ratcheted in BELOW the 90.10 alert — that alert is now a stale proxy** |
| HOPE | 13.98 | 11.71 | +19.4% | 25.0 | LONG 13.12 | 1 | RVOL 1.37 | PASS strong (⚠ earnings 7/21 — no full size) |
| SPY | 750.72 | 696.29 | +7.8% | 17.8 ↓ | **LONG 730.73** | — | — | CE repaired from the 7/8 SHORT 758.52 |
| QQQ | 705.94 | 640.36 | +10.2% | 16.3 ↓ | LONG 705.21 | 1 | — | **0.1% above the flip line — one red day = two-flip character change (SMH already SHORT)** |
| IWM | 295.59 | 263.17 | +12.3% | 11.3 ⚠ | LONG 285.81 | 1 | — | PASS (trendless chop) |
| SMH | 568.92 | 438.55 | +29.7% | 17.7 ↑ | SHORT 651.30 | 1 | — | short regime confirmed (−4.0% on 7/16, TSMC sell-the-news) |
| NET | 272.46 | 210.43 | +29.5% | 23.3 ↑ | LONG 241.24 | 1 | — | PASS, base intact, no chase |
| TXN† | 291.22 | 220.92 | +31.8% | 13.9 | SHORT 320.88 | 1 | — | paper P2 is counter-CE by design (unfilled-call test) |
| IBKR† | 92.21 | 74.86 | +23.2% | 18.8 ↑ | LONG 86.95 | 1 | — | PASS; −4.8% day, paper stop 91.50 sits above the CE line (low 91.58 = 8-cent survival) |
| ECO† | 56.77 | 43.71 | +29.9% | 14.8 ↑ | LONG 49.97 | 1 | — | PASS |

† paper-book adds (vacation-week book). No Quality/Spec-Ignition fires on scanned names (max RVOL = KRE 1.4).

### Deltas vs 2026-07-08 snapshot
- **CB Chandelier FLIPPED SELL** — first Tier-1 regime casualty; insurance leg of the financials split. The 6/30 entry-zone fire was never confirmed as a fill; the 323 stop alert is moot/stale either way.
- **NEE Chandelier FLIPPED LONG** (short stop ratcheted down through ~89.5 and the 7/14 close crossed it) → NEE = full PASS. **The 90.10 "CE-flip" alert never fired and now sits ABOVE the actual flip — stale proxy; paper C4 add-condition treated as NOT met.**
- **SPY CE repaired to LONG 730.73** (7/8 snapshot had it SHORT 758.52 — that short died in the CPI rally).
- **Two flip-watches for Fri 7/17: QQQ < 705.21 and JNJ < 249.76 daily closes.** JNJ's slide is the earnings reaction (266 → 250 in 6 sessions); if it flips, the 245 dip alert = knife signal, not entry.
- DTE ADX collapsed 30.1 → 14.6 (trend died; 154-gate saga closed). DAL still bleeding inside a PASS.
- ADX column is method-sensitive vs the 7/8 run — trust flips and the >20 verdict, not level diffs.

## Prior — 2026-07-08 ~10:05 ET (indicators = 2026-07-07 completed close; Live = ~10:00 ET print)

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

(7/6 snapshot table removed 7/16 — two generations old. Its lasting lessons, preserved: **(1)** the 7/2 "SMH Chandelier SELL flip @ 592.29" was FALSE — contaminated reads; SMH's real first flip was 7/7. **(2)** Index chart feeds (DJ_DLY:DJI, SP:SPX) are ~15-min DELAYED right after the bell — use the symbol-details pane / official quote for closes pulled within ~20 min of the close. **(3)** BMNR CE flip line computed 17.29 vs the 16.93 alert wired at entry — alerts drift from ratcheting CE lines; recompute before trusting an old flip alert (same failure mode as NEE 90.10 on 7/16).)
