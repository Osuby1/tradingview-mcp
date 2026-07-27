# Fresh-Ignition exit search — results

Run 2026-07-26 against `research/fi-exit-preregistration.md` (committed
first). Same 1,512 A-grade Fresh Ignition entries; eight exits compared; all
numbers are mean excess vs SPY over each trade's own window.

---

## Verdict: no candidate passes — the pre-committed conclusion stands

| Exit | Mean | Median | Beat SPY | Worst trade | Days |
|---|---|---|---|---|---|
| Hold 250 days | **+2.81** | −4.81 | 44% | −102 | 228 |
| E1 trend-break (ride until Stage-2 dies) | +1.91 | −9.43 | 33% | −93 | 110 |
| E2 close below scanner's support shelf | −0.13 | −4.44 | 31% | −59 | 32 |
| Hold 60 days | −0.15 | −1.89 | 46% | −99 | 59 |
| E3 Omar's rule + floor | −0.50 | +0.91 | 55% | −52 | 10 |
| Live stop + ratchet | −0.67 | −4.58 | 21% | −53 | 33 |
| Hold 120 days | −0.70 | −3.69 | 44% | −100 | 114 |
| R1 Omar's sell-on-Cooling | −1.31 | +2.29 | 70% | −102 | 58 |

All three candidates FAIL the pre-registered criteria (E1 fails all three;
E2/E3 clear only the beat-R1 test). The pre-committed conclusion, verbatim:

> *There is no clever exit hiding in this cohort. The tab machinery adds
> nothing to exit timing; if the cohort is traded at all, use the measured
> default and accept that the entry, not the exit, is the constraint.*

## The sixth measurement of the same law

Sort the table and it is the familiar staircase: the two loosest rules sit on
top, the tightest harvest rules at the bottom, with Omar's original
sell-on-Cooling last. Looser beats tighter, holding beats managing — now
observed in six independent tests across two different signal systems.

## Why even the "winners" are not real

The two positive rules fall apart under the splits declared in advance:

| | Odd half | Even half | 2021 | 2022 |
|---|---|---|---|---|
| Hold 250d | **−1.51** | +6.54 | −5.62 | +6.48 |
| E1 trend-break | **−2.40** | +5.65 | −4.20 | +2.17 |

The entire positive mean lives in one random half of the alphabet and
flips sign in the other. A rule whose profit depends on which half of the
alphabet you trade is noise wearing a trend coat. This is exactly the
fragility the registration was built to catch, and it caught it.

## What was learned that is real

1. **The harvest instinct is now dead twice over.** Sell-on-Cooling (−1.31)
   is the worst exit of eight; adding a floor (E3) helps but still loses to
   doing nothing. Selling into strength costs money in every configuration
   tested this week.
2. **The entry is the constraint.** With no alpha at entry (60-day hold
   ≈ −0.15), no exit can rescue the cohort — exits redistribute the same
   nothing. Improving stock picking means improving what gets BOUGHT, and
   this scanner's tabs and grades, now fully measured, do not do that.
3. The scanner's support shelf (E2) is at least benign — it matched the
   60-day hold with smaller worst-case losses (−59 vs −99). As a RISK tool
   (not a return tool) on discretionary trades, it is not crazy. Label it
   exactly that.

One run, no changes after registration. Hypothesis-grade context only;
nothing is promoted, nothing goes live.
