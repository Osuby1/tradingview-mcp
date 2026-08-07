# Winner-DNA score — pre-registration (SHADOW LANE per the rule freeze)
Registered 2026-08-06 (git timestamp = proof). Purpose: Omar's ask — "know
from past setups that ran with similar characteristics that we have a
compelling stock." Quantify what our OWN winning flags shared at flag time.

## Question
Which measurable flag-day traits separate flags that ran >= +15% within
1 month from flags that went nowhere or died?

## Sample (AMENDED 2026-08-06 pre-data, Omar's design: skipped-runner attributes drive selection)
WINNER COHORT: the workbook's SKIPPED RUNNERS block (certified >=10%
runners with rec-day snapshots) PLUS acted-on winners (GE, MLI, ...) —
winners are winners regardless of whether we rode them.
CONTROL COHORT (the part that keeps this from being astrology): all
same-period flags that did NOT run (< +5% at +1m) from the same logs.
A trait only counts if it SEPARATES the cohorts — traits shared with the
duds are noise, however impressive they look on the winners alone.
Rec-day attribute sources: recommendations_log CSVs (2026-07-22 onward),
rec-day-dmi-cache.json, og-sweep raws. Pre-7/22 flags included only
where sweeps carry their flag-day row; exclusions listed, not hidden.
HONEST LIMITS: ~3 months, one regime (melt-up), winner n ~10-25 —
label UNCALIBRATED until out-of-sample.

## Candidate traits (frozen list — no additions after first grading)
band-width percentile at flag · RVOL at flag · % of 52wk high · ADX ·
+DI minus -DI margin · % vs 200-day · sector-radar state of its group ·
short interest % float (where known) · flag source (coil vs breakout vs
squeeze) · dollar-volume decile.

## Output
A 0-10 similarity-to-past-winners score printed on every A-List card as
SHADOW context ("resembles winners: X/10 [uncalibrated]"). It influences
NOTHING live until promotion.

## Promotion gate (per governance)
>= 20-30 out-of-sample A-List cards graded (+1w/+1m); promoted only if
top-DNA-tercile cards beat bottom-tercile by a margin that survives the
Friday-review red team; otherwise it dies and we say so.

## Grading joins the standing Friday review alongside the funnel metrics
(flags -> A-List -> doors -> fires -> fills -> P&L per stage).

---

# FIRST CUT — BAND WIDTH — run 2026-08-06 PM (`scripts/winner_dna_bandwidth.py`)

**VERDICT: the lead hypothesis is NOT supported so far, and the test is badly
underpowered. Nothing here earns the coil story a place in any brief yet.**

Method: band width = (upper-lower)/mid, 20d Bollinger 2sd; percentile ranked in
the trailing 120 sessions ENDING ON THE FLAG DATE (no look-ahead). Sample = every
fresh Chandelier BUY in the sweep archive, first flag per symbol.

### Results

| Bucket | +5 sessions | +10 sessions |
|---|---|---|
| COILED (0-25th) | n=96, mean **+0.16%**, MFE 4.09% | n=67, mean **+0.18%**, median +1.50%, MFE 5.63% |
| MIDDLE (26-59th) | n=83, mean **-0.25%**, MFE 4.17% | n=52, mean **+3.08%**, median +1.90%, MFE 7.43% |
| EXPANDED (60th+) | n=29, mean **-2.25%**, MFE 4.34% | n=20, mean **-2.09%**, median -0.71%, MFE 6.77% |

- Runners (>= +15%): **0 at +5 sessions, 2 at +10** (MSFT 40th pctile, SNOW 44th)
  — both MIDDLE, neither coiled. **0 of 67 coiled flags reached +15% in 10 days.**
- Coiled beats middle at 5 sessions and LOSES to it at 10. That inconsistency is
  what noise looks like.
- The ONE effect consistent across both horizons: **EXPANDED is the worst bucket**
  (-2.2% and -2.1%). The usable rule so far is "don't chase the 60th+ percentile",
  NOT "prefer the coil."

### Named cases, measured (too recent to grade, but the traits are real)

| Sym | Flag | Band width | Tag | Stock since flag |
|---|---|--:|---|--:|
| GE | 7/31 | **2nd** | COILED | +4.02% (the CALL paid +32%) |
| UAL | 8/3 | 9th | COILED | +0.57% |
| HSIC | 8/5 | 12th | COILED | -1.52% |
| LUV | 8/5 | 14th | COILED | -3.79% |
| ROBO | 8/4 | 19th | COILED | -1.51% |
| DAL | 7/29 | 20th | COILED | +6.64% |
| AMG | 8/4 | 39th | middle | -2.93% |
| **MLI** | 7/23 | **62nd** | **EXPANDED** | **+10.03%** (best position in the book) |
| BA | 8/5 | **78th** | EXPANDED | -3.33% |

### What this CONFIRMS and what it OVERTURNS
- **CONFIRMED:** GE really was 2nd percentile and BA really was 78th. The
  GE-vs-BA post-mortem stands: readiness ranked BA (70) above GE (60) and the
  compressed one was the one that paid.
- **OVERTURNED — my own 12:34 claim.** I said all three of that night's cards
  were post-breakout and "not one is a coil." Measured: LUV 14th and HSIC 12th
  were both COILED. Only BA was expanded. That claim came from the buggy
  structure tag (driver-string parsing) and I over-corrected on it. The narrower
  BA statement was right; the sweeping one was wrong.
- **COUNTER-EVIDENCE worth keeping in front of us:** MLI, the book's biggest
  winner, was flagged EXPANDED at the 62nd percentile.

### Why this is not yet a verdict
1. Pre-registered horizon is **+1 month; nothing in the archive has it.** The
   sweep starts 7/18. This cut used +5 and +10 sessions as a deviation, labelled.
2. The winner-vs-dud contrast the design requires is untestable with 0-2 runners.
3. **Every hypothesis-generating case is excluded** for insufficient forward data
   (GE, BA, LUV, UAL, DAL, ROBO, AMG, BLMN, TWST).
4. CDNA/EAT/IOVA/AMLX never appear in the sweep `hits` at all — they came from
   other detectors, so this archive does not cover them. Widening the flag source
   is required before the sample represents "our flags."

### Standing consequence until the September cut
Band-width percentile keeps being **printed** on every card (it is a measured
fact) but is **not** described as predictive, and no card is framed as compelling
because it is coiled. Re-run: 2026-09-04, at the true +1m horizon, alongside the
squeeze study.
