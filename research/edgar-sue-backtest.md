# EDGAR SUE / PEAD backtest - hard facts

113 US names, **5497 earnings events** with a point-in-time SUE and a full 60-day forward window. Surprise measured from EDGAR filing dates (no look-ahead); drift from the day AFTER filing.

## Does the earnings surprise forecast drift? (the whole question)
- IC = Spearman(SUE, +20d return) = **+0.029**  (n=5497)
- IC = Spearman(SUE, +60d return) = **+0.005**  (n=5497)

  Compare: momentum IC was -0.006, the technical BUY SCORE +0.065. IC >= |0.03| is a usable signal; PEAD in the literature runs ~0.05-0.10.

## High-SUE vs low-SUE quintiles
- **+20d:** low-SUE +0.58%  high-SUE +1.12%  spread +0.54pt
    vs SPY: low -0.52%  high +0.10%  high-SUE excess +0.10%
- **+60d:** low-SUE +3.90%  high-SUE +3.32%  spread -0.59pt
    vs SPY: low +1.35%  high +0.94%  high-SUE excess +0.94%

## Verdict
**No usable PEAD here** (IC +0.005 at 60d). Either the seasonal-SUE construction is too crude for this liquid-mega-cap universe (PEAD is strongest in smaller, less-covered names) or the window is unfavorable.

## Caveats
- US large-cap SURVIVOR universe - and PEAD is KNOWN to be weaker in big, heavily-covered names (the drift is arbitraged faster). A small/mid-cap universe would be a fairer test of PEAD's real strength.
- Seasonal-SUE (vs year-ago), NOT analyst-surprise - the free construction. The 'beat vs Street' version may be stronger; that needs paid point-in-time estimates (Phase 2).
- No costs/slippage; overlapping 60-day windows mean events are not independent (inflates apparent significance).
- Q4 quarterly EPS often absent from 10-Ks, so Q4 events are under-sampled.
