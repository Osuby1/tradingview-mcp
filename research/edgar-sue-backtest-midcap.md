# EDGAR SUE / PEAD backtest - hard facts
*(forward returns winsorized at 2.5/97.5 pct)*

103 US names, **2954 earnings events** with a point-in-time SUE and a full 60-day forward window. Surprise measured from EDGAR filing dates (no look-ahead); drift from the day AFTER filing.

## Does the earnings surprise forecast drift? (the whole question)
- IC = Spearman(SUE, +20d return) = **+0.051**  (n=2954)
- IC = Spearman(SUE, +60d return) = **-0.002**  (n=2954)

  Compare: momentum IC was -0.006, the technical BUY SCORE +0.065. IC >= |0.03| is a usable signal; PEAD in the literature runs ~0.05-0.10.

## High-SUE vs low-SUE quintiles
- **+20d:** low-SUE +0.35%  high-SUE +1.50%  spread +1.15pt
    vs SPY: low -1.05%  high +0.49%  high-SUE excess +0.49%
- **+60d:** low-SUE +8.15%  high-SUE +7.58%  spread -0.57pt
    vs SPY: low +5.22%  high +5.16%  high-SUE excess +5.16%

## Verdict vs the PRE-REGISTERED criterion

Pre-registered bar (research/pead-refinement-preregistration.md, set BEFORE the run):
"quintile spread turns POSITIVE at BOTH 20d and 60d." Result:

- 20d spread: **-2.44pt (baseline) -> +1.15pt (POSITIVE)**  PASS
- 60d spread: **-0.57pt (still negative)**  FAIL

**=> FAILS the pre-registered test** (required BOTH horizons). Honoring the
pre-registration: this is a FAIL, and per the plan we STOP free refining.

## But the honest partial finding (not spin - stated as failing the strict bar)

The winsorize + mid-cap refinement genuinely FIXED the 20-DAY picture: the quintile
spread flipped from -2.44 to **+1.15pt**, IC 20d = **+0.051**, high-SUE mid-caps
returned +1.50% vs low-SUE +0.35% over 20 days (+0.49% vs SPY). That is a real,
clean, short-horizon PEAD effect.

The problem is PERSISTENCE: by 60 days the signal is dead (IC -0.002, spread -0.57).
The drift plays out in ~1 month then reverts/decays - consistent with PEAD being
partly arbitraged in names this size. So there IS a signal, but it is SHORT-HORIZON
only, and it did not clear the two-horizon bar we set to avoid fooling ourselves.

## Decision (as agreed: act and stop)

Free refinement is exhausted - this was the last one. Two real options:
1. **Act on the 20-day signal as-is**: a ~1-month hold of high-SUE mid-caps has a
   genuine clean edge (+1.15pt/+0.49% vs SPY, IC +0.051). Modest, short, but real
   and free. Forward-validate via the outcome tracker before sizing.
2. **Pay for analyst-surprise data** (~$59/mo FMP): "beat vs Street" reacts faster
   and may give a cleaner, more persistent signal than seasonal-SUE. This is the
   Phase-2 decision the scoping doc flagged.

No more free-parameter tinkering - that would be overfitting.

## Caveats
- Mid-cap $2-12B SURVIVOR universe (from the 7/20 scanner mcaps); survivorship
  inflates and matters more for smaller names.
- Seasonal-SUE, not analyst-surprise (free construction).
- Winsorized at 2.5/97.5 (pre-registered); overlapping 60-day windows -> events not
  independent -> significance overstated. One strong-tape window.
- Q4 quarterly EPS often absent from 10-Ks.
