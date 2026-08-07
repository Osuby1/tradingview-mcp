# Cooling-arrival put study — pre-registration (2026-08-07, Omar decision #5)

The tab-lifecycle study found fresh COOLING arrivals underperform the small-cap
index at every horizon (-0.7% next day to -3.2% at ten sessions, n=245, every
CI excluding zero). This registers the PAPER-ONLY trading test of that signal
BEFORE any data is peeked at.

## Frozen design
- SIGNAL: a ticker's FIRST appearance on the COOLING tab in the daily
  origination log (same event definition as the study).
- PAPER ENTRY: next session's OPEN, synthetic Black-Scholes ATM PUT, ~30-45
  DTE monthly, IV = 1.2x realized-20 (LABELED SYNTHETIC); real-chain pricing
  used instead whenever the name has a chain passing the standard gates
  (OI>=100, spread<=15%).
- EXIT: +5 sessions at the close, or -50% premium stop, whichever first.
- SIZE: $500 notional premium per signal, paper only.
- VERDICT (after >=30 signals): positive mean expectancy AND >=50% win rate ->
  present for promotion discussion. Either bar missed -> the signal stays a
  brief annotation and the study closes. NO REAL DOLLAR before the verdict.
- Grading joins the Friday reviews; first read after ~2 weeks of signals.

Runs mechanically off the nightly log from Monday 2026-08-10.
