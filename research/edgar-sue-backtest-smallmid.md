# EDGAR SUE / PEAD backtest - hard facts

155 US names, **4420 earnings events** with a point-in-time SUE and a full 60-day forward window. Surprise measured from EDGAR filing dates (no look-ahead); drift from the day AFTER filing.

## Does the earnings surprise forecast drift? (the whole question)
- IC = Spearman(SUE, +20d return) = **+0.067**  (n=4420)
- IC = Spearman(SUE, +60d return) = **+0.030**  (n=4420)

  Compare: momentum IC was -0.006, the technical BUY SCORE +0.065. IC >= |0.03| is a usable signal; PEAD in the literature runs ~0.05-0.10.

## High-SUE vs low-SUE quintiles
- **+20d:** low-SUE +4.29%  high-SUE +1.85%  spread -2.44pt
    vs SPY: low +3.07%  high +0.93%  high-SUE excess +0.93%
- **+60d:** low-SUE +8.29%  high-SUE +8.35%  spread +0.06pt
    vs SPY: low +5.65%  high +6.04%  high-SUE excess +6.04%

## Verdict (corrected - the auto-text was too generous)

**Hypothesis CONFIRMED that PEAD is stronger in small/mid caps, but it is NOT a
clean tradeable signal as built.** Two facts that must be read together:

- **IC roughly DOUBLED vs large caps:** +0.067 at 20d / +0.030 at 60d, vs the
  large-cap +0.029 / +0.005. IC +0.067 is genuinely usable (>0.03) and matches the
  low end of the published PEAD range. This is the strongest CLEAN, point-in-time
  forecasting number we have measured. The theory held: the drift lives in smaller,
  less-covered names.
- **BUT the top-vs-bottom quintile does NOT sort:** at 20d low-SUE (+4.29%) BEAT
  high-SUE (+1.85%) - spread -2.44pt, backwards; at 60d it is flat (+0.06pt). So a
  naive long-high-SUE / short-low-SUE quintile trade would NOT have worked. The
  positive IC is coming from the middle of the distribution, not the extremes.

The contradiction (positive IC, non-monotonic / backwards quintiles) means the raw
seasonal-SUE relationship in small caps is real but MESSY - dominated by huge
idiosyncratic small-cap volatility and non-linear at the extremes (biggest
surprises over-react then revert). It is a lead, not a finished edge.

Also: the vs-SPY excesses (+6% at 60d) are mostly SMALL-CAP BETA in a strong-small-
cap July window, NOT PEAD - both high AND low SUE beat SPY by ~5-6%. Do not read
those as alpha.

## What this actually justifies

- Keep going - this is the first clean signal with a real IC AND a known reason to
  strengthen further. The refinements that the literature says sharpen PEAD:
  1. **Analyst-surprise instead of seasonal-SUE** (the Phase-2 paid data) - "beat
     vs Street" reacts more cleanly than "vs year-ago".
  2. **Winsorize / neutralize** the extreme small-cap outliers so the quintiles are
     not dominated by a few 40% movers.
  3. **Mid-cap band** ($2-12B) rather than the smallest names, where idiosyncratic
     noise is lower but coverage is still thin.
- Forward-validate any refined version through the outcome tracker before trusting.

## Caveats
- Small/mid-cap SURVIVOR universe (from the 7/20 scanner run) - survivorship still
  inflates; delisted small caps are absent and that matters MORE for small caps.
- Seasonal-SUE, not analyst-surprise (free construction).
- Overlapping 60-day windows -> events not independent -> significance overstated.
- One strong-small-cap window; the vs-SPY numbers are mostly beta.
- Q4 quarterly EPS often absent from 10-Ks.
