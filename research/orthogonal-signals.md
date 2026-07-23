# Orthogonal (non-price) signal layer

55 names scored. Blend of revenue/EPS growth + analyst rating + target upside. NOTE: earnings-surprise/PEAD (the best component) came back empty from yfinance for 55/55 names - that piece needs a better data source and is NOT in these scores yet.

## Is it actually orthogonal to price? (the whole point)
- **Spearman(fundamental score, 12-1 price momentum) = +0.008** (n=55)
- Near ZERO = it carries genuinely DIFFERENT information than the price/technical signals. Only 4 of the top-10 fundamental names are also top-15 momentum. Despite the top list LOOKING like mega-cap tech, the rank ordering is independent of price.
- This is the necessary condition for combining signals to help: a second data family that does not just restate the first.

## Top 15 by fundamental score
| Sym | Score | RevGrow | EPS-Q | Analyst(1=SB) | Target Upside |
|---|---|---|---|---|---|
| NVDA | 96.3 | +85% | +211% | 1.3 | +43% |
| META | 95.6 | +33% | +61% | 1.35 | +32% |
| MP | 95.4 | +119% | - | 1.28 | +72% |
| MU | 94.7 | +346% | +1398% | 1.42 | +57% |
| PLTR | 89.1 | +85% | +307% | 1.88 | +47% |
| GOOG | 84.3 | +22% | +81% | 1.43 | +26% |
| AMZN | 82.9 | +17% | +77% | 1.33 | +28% |
| DELL | 76.5 | +88% | +256% | 1.78 | +13% |
| MSFT | 75.6 | +18% | +23% | 1.33 | +43% |
| LLY | 73.2 | +56% | +168% | 1.76 | +9% |
| SNOW | 71.1 | +34% | - | 1.49 | +11% |
| AMD | 68.9 | +38% | +95% | 1.49 | -2% |
| COST | 68.9 | +22% | +46% | 2.0 | +16% |
| C | 67.2 | +14% | +45% | 1.71 | +17% |
| JPM | 65.5 | +30% | +41% | 2.17 | +6% |

## Honest verdict
- **Orthogonal: YES** (corr +0.008 with momentum). It is real independent info.
- **Predictive: UNPROVEN.** This is a CURRENT snapshot, not backtested - yfinance fundamentals are not point-in-time, so a historical test leaks look-ahead. It will be FORWARD-graded by the outcome tracker.
- **Incomplete:** the single most valuable orthogonal signal - earnings surprise / post-earnings drift (PEAD) - is MISSING (yfinance earnings_dates returned empty). Getting PEAD + estimate revisions from a real source is the highest-value next step; this growth/analyst blend is the weaker cousin.

## What both builds together actually say
- Momentum backtest: IC ~0 (survivorship+beta made the compounded number look great; the real forecasting metric was zero).
- Orthogonal layer: genuinely independent of price, but forecasting power unproven and missing its best component.
- Net: the THESIS holds (non-price data is independent and could help), but neither piece has DEMONSTRATED an edge yet. 'Hugely better forecasting' is not a switch we flipped today - it is a data-acquisition project (real PEAD + revisions) plus patient forward validation. No shortcut, no self-deception.
