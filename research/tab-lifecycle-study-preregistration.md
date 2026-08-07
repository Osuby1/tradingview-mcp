# Tab-lifecycle price-action study — pre-registration (2026-08-07, Omar-directed)

Omar's ask: analyze price action of names once they ARRIVE on and STAY on the
origination scanner's four tabs (FRESH IGNITION, COOLING, COILED, BUY ZONE) and
determine whether their behaviors offer a few-day options trade (pop or
selloff), short- or long-horizon. Registered BEFORE any data is computed;
event definitions and verdict bars frozen here.

## Data
Daily tab membership per (date, ticker) reconstructed from the dated
recommendations_log CSVs (research/, 2026-07-01 onward) + the master log.
Prices: daily OHLCV (auto-adjusted). Benchmark: IWM (small-cap universe).
~5 weeks, one regime — every verdict labeled PRELIMINARY regardless of result.

## Frozen event set (no additions after first compute)
1. **ARRIVAL**: first day a ticker appears on tab T → forward +1/+3/+5/+10
   session returns, excess over IWM. (The +21 version already exists in the
   detector study; this adds the short horizons Omar trades.)
2. **PERSISTENCE**: day-N-on-tab (N = 2, 3-5, 6+ consecutive) → same forward
   windows. Question: does a name COILED for 5+ days outperform day-1 arrivals
   (spring loading) or underperform (dead money)?
3. **TRANSITION — the scanner's own designed signal, never measured**:
   COOLING → BUY ZONE promotion day ("tomorrow's Buy Zone tab" per the
   source). Forward returns from the promotion close. Also COILED → FRESH
   IGNITION (coil fires).
4. **EXIT/DROP-OFF**: name leaves all tabs after ≥3 days on them → forward
   returns (short-side candidate: is drop-off a sell signal?).
5. **OPTION TRANSLATION**: for any event class that clears the bar, a
   synthetic Black-Scholes 5-session ATM call (or put, for short-side)
   expression at IV=1.2x realized, LABELED SYNTHETIC — real chains for the
   liquid subset only.

## Verdict bars (frozen)
- An event class is a CANDIDATE SIGNAL only if: n >= 15 events, mean excess
  vs IWM positive (negative for short-side) at the stated horizon, AND a
  2000-draw bootstrap 95% CI excluding zero.
- n < 15 = AUTO-INSUFFICIENT (reported, not spun).
- Any candidate signal goes to the SHADOW/PAPER lane with its own
  pre-registration before a dollar follows it. Nothing here trades live off
  this study alone.

## Delivery
Runs tonight with the 8/7 review batch; results in the Friday review document
with every other docket item.
