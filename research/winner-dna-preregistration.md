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

---

# SECOND CUT — ALL DETECTORS + HISTORY ARM — 2026-08-06 PM
`scripts/winner_dna_bandwidth_v2.py` (Omar: "widen the flag source... and use a
wider data set if useful")

**VERDICT: band-width compression is DEAD as a predictor. Not underpowered —
answered. And the study found a replacement lead variable that is roughly eight
times larger: WHICH DETECTOR flagged it.**

Sources merged: sweep-CE 313 (7/18+), orig-COILED 225, orig-COOLING 250,
orig-FRESH IGNITION 90, orig-BUY ZONE 42 (7/1+). **920 flag records, 566 symbols,
719 gradeable.** Plus a history arm of **41,347 observations** over ~2 years on
the same 564 names — the power the flag archive cannot supply this year.

### ARM 2 — history, 41,347 observations, forward 21 sessions
| Band width at observation | n | mean fwd21 | >= +15% |
|---|--:|--:|--:|
| 0-10th (extreme coil) | 4,578 | +2.92% | 14.4% |
| 11-25th (coiled) | 4,968 | +2.96% | 14.3% |
| 26-59th (middle) | 12,972 | +3.03% | 14.6% |
| 60-89th (expanded) | 11,670 | +3.50% | 15.9% |
| 90-100th (blown out) | 5,212 | **+3.98%** | **16.8%** |
| baseline | 41,347 | +3.27% | 15.2% |

Monotonic — and pointing the WRONG WAY. The most blown-out names beat the most
compressed ones. The spread is small (about 1 point over 21 sessions) but it is
consistent across 41k observations and it is the opposite of the hypothesis.
**Compression does not predict direction. It never did; we never checked.**

### ARM 1 — our own flags, all detectors
| Horizon | COILED | MIDDLE | EXPANDED |
|---|---|---|---|
| +5 (n=719) | -0.11% (n=231) | -1.24% (n=245) | -1.51% (n=243) |
| +10 (n=556) | -0.45% (n=165) | -0.69% (n=180) | -2.82% (n=211) |
| +21 (n=186) | +0.59% (n=35) | +0.41% (n=43) | **-3.91%** (n=108) |

**The single cleanest number in the whole study: at +21 sessions the median
RUNNER (>= +15%) had a band width of 72nd percentile — and the median DUD had a
band width of 72nd percentile. Identical. Zero separation.**

v1's "avoid expanded" rule ALSO does not survive as stated: expanded flags have
the worst mean (-3.91%) but produce MORE big winners (12/108 = 11%) than coiled
(3/35 = 9%). Expansion is a fat-tailed state, not a bad one — more of both. The
honest reframe: our detectors catch expansion LATE (the history arm shows
expanded states are fine in general; only OUR expanded flags underperform), which
is a chasing problem in the detectors, not a property of expanded stocks.

### THE FINDING THAT MATTERS — detector source, +21 sessions
| Source | mean fwd21 | n |
|---|--:|--:|
| **orig-COILED tab** | **+4.03%** | 36 |
| orig-FRESH IGNITION | -0.87% | 31 |
| **orig-COOLING tab** | **-4.24%** | 112 |

An **8-point spread between detector tabs**, versus roughly 1 point for band
width across 41k observations. Which detector fires is worth far more than any
trait measured afterwards.

And the twist that kills the trait outright: **inside the origination COILED tab
— the best-performing source — my band-width buckets rank BACKWARDS** (its
"expanded" names returned +8.08%, its coiled +4.18%). Whatever that tab is
capturing, it is demonstrably NOT band-width compression.

Sample honesty: the +21 arm has only 186 flags and the per-detector cells are
n=31-112. These are suggestive, not settled. COOLING at -4.24% on n=112 is the
sturdiest of them and the one most worth acting on early.

### Consequences, effective now
1. **Band-width percentile is DEMOTED from lead hypothesis.** It stays printed on
   cards as a description. It is never again offered as a reason to buy, and the
   phrase "GE-type compression" is retired from briefs.
2. **The GE-vs-BA story loses its explanation.** GE (2nd pctile) paid and BA (78th)
   did not, but with runners and duds sharing an identical median band width, that
   pair was an anecdote, not a mechanism. Something else drove GE.
3. **New lead hypothesis: detector source / tab.** The Winner-DNA score's first
   input becomes which detector fired, not what the chart looked like.
4. **COOLING tab flagged for review** at -4.24% over 112 flags — the largest
   negative cell in the study.

---

# THIRD CUT — DETECTOR SOURCE AS LEAD VARIABLE — 2026-08-06 PM
`scripts/winner_dna_detector.py`. Everything market-adjusted (raw returns confound
the detector with WHEN it fired), bootstrap 95% intervals on every cell, split-half
stability, and source overlap reported.

**VERDICT: detector source is a REAL variable — the first thing in this study to
produce an interval that excludes zero. Two findings survive every control, and
one of them is about our whole operation, not a tab.**

### +21 sessions, excess over IWM (the right benchmark — our flags are not S&P names)
| Source | n | mean vs IWM | 95% CI | beat IWM | split-half |
|---|--:|--:|---|--:|---|
| **orig-COILED** | 36 | **+2.72%** | **[+0.66, +5.14]** | 56% | consistent (+1.32 / +0.21) |
| orig-FRESH IGNITION | 31 | +0.38% | [-4.06, +5.22] | 48% | too few |
| orig-BUY ZONE | 7 | -5.34% | [-15.92, +5.68] | 43% | too few |
| **orig-COOLING** | 112 | **-5.52%** | **[-8.63, -2.32]** | 31% | consistent (-6.66 / -9.63) |
| **ALL FLAGS POOLED** | 186 | **-2.94%** | — | **39%** | — |

Versus SPY the same cells read COILED +1.04%, COOLING **-7.22%** [-10.43, -4.03],
pooled **-4.75%** with 34% beating.

### The three things that survive
1. **The COILED tab has a credible edge: +2.72% over small caps in a month, the
   interval excludes zero, 56% beat rate, and the sign holds in both halves of the
   sample.** Note the irony: the tab is named for compression and the previous cut
   proved its edge is NOT compression. We have found a source that works and we do
   not know why. That is the next question.
2. **The COOLING tab is credibly harmful: -5.52% vs IWM, -7.22% vs SPY, over 112
   flags, negative in both halves, only 31% beating.** The largest and sturdiest
   negative cell anywhere in this study. CAVEAT BEFORE ACTING: confirm with Omar
   what that tab is FOR — "cooling" may be a watch state, not a buy list, in which
   case this is a labelling problem, not a broken detector. It is also 94%
   overlapped with BUY ZONE, so those two are nearly the same population.
3. **Grade A underperformed grade B: -7.17% vs -4.23% excess over SPY, both
   credibly negative.** The scanner's own conviction ranking is inverted over this
   sample. That deserves its own investigation.

### The uncomfortable headline
**Pooled across every detector, our flags returned -2.94% versus small caps over
the following month, and only 39% of them beat the index.** Detection is not
merely running ahead of capture — over this window the flags themselves did not
beat buying the index. This is the first hard measurement of that claim and it
belongs in the Friday review at the top, not in a footnote.

### Limits, stated not buried
- The +21 sample is 186 flags and **sweep-CE contributes ZERO of them** (the sweep
  archive starts 7/18, so nothing has a full month). Every +21 conclusion is about
  the ORIGINATION scanner, not our Chandelier sweep. The sweep's own +21 verdict
  arrives in September.
- Five weeks of flag dates, one regime.
- Sources overlap heavily (BUY ZONE is 94% inside COOLING; COILED and FRESH
  IGNITION share 70%), so these are not five independent detectors.
- At +10, sweep-CE is **-1.89% excess [CI excludes 0] despite a +0.93% RAW mean** —
  the clearest demonstration in the study of why raw returns mislead. Our flags
  went up; the market went up more.

---

# CORRECTION + THE ACTUAL DEFECT — 2026-08-06 PM (Omar: "the cooling tab is
# 'this already ran, wait for it to settle'... it is not a buy list")

**My third-cut headline was WRONG and is withdrawn.** I pooled a watch state in
with buy recommendations and called the result "our flags."

### Recomputed, excess over IWM, buy-intent sources only
| Cut | +5 | +10 | +21 |
|---|---|---|---|
| BUY-INTENT only (COILED, FRESH IGNITION, BUY ZONE, sweep-CE) | -0.74% (n=498) | -0.74% (n=364) | **+0.98% (n=74), CI [-1.38, +3.55]** |
| ...also excluding BUY ZONE | -0.59% | -0.51% | **+1.64% (n=67), CI [-0.72, +4.06]** |
| COOLING (watch state) | -1.57% | -3.09% | **-5.52% (n=112), CI excludes 0** |
| what I wrongly reported as "our flags" | -0.99% | -1.55% | -2.94% |

**Correct statement: at one month our buy-intent flags are roughly INDEX-MATCHING —
the interval spans zero, so they are not proven better or worse than the index.**
Not "they failed to beat it." The -2.94% was manufactured by including a list whose
entire purpose is to identify names that will lag next.

**COOLING is fully exonerated and PROMOTED to a validated negative signal:** -5.52%
vs IWM at 21 sessions, 31% beat rate, interval excludes zero, negative in both
halves. It does exactly what Omar says it does. It belongs in the Winner-DNA score
as a VETO input, not as a candidate source.

### THE DEFECT THIS EXPOSED — the watch state is being served to Omar as picks
- Across all live-picks files, **`origination:Cooling` is the LARGEST single source:
  1,952 entries.** 180 of the 403 tickers ever surfaced as a live pick (45%) came
  from it. Today: 129 of 347 active picks.
- **6 of the 20 runners in tonight's EOD brief came from COOLING** — IOVA, EAT,
  ALNT, BLFS, MNPR, CHE — every one printed as "confirming - enter/add per plan."
- The 9:00 and 11:45 phone pushes carry the same mapping: the radar's CONFIRMING
  tag is rendered as "enter/add per plan". CONFIRMING describes PRICE ACTION (the
  name is still running); it says nothing about buy intent. Fusing the two turns
  "this already ran, wait" into "buy it."
- The cost is now measured, not theoretical: **5.5 points of underperformance
  versus small caps over the following month.**

### Proposed fix (needs Omar's go — it changes what the radar says, not just how it computes)
1. live-picks carries the source tab on every row and NEVER renders a
   COOLING-sourced name as "enter/add per plan" — it reads "already ran, wait to
   settle" per the tab's own definition.
2. The runners table in all three briefs marks COOLING-sourced rows explicitly.
3. Winner-DNA score: COILED tab positive weight, COOLING tab a veto.

### Standing consequence until the September cut
Band-width percentile keeps being **printed** on every card (it is a measured
fact) but is **not** described as predictive, and no card is framed as compelling
because it is coiled. Re-run: 2026-09-04, at the true +1m horizon, alongside the
squeeze study.

---

# RUNNER RECALL BACKTEST — 2026-08-06 PM (Omar: "would it have caught the
# stocks on the Runners list?")
`research/runner-backtest-eligibility.json`. Readiness recomputed AS OF each
runner's recommendation date (history truncated at that date, no look-ahead),
then run through the live A-List floors: readiness >= 55, $20M dollar volume,
plus tonight's COOLING veto.

**ANSWER: 2 of 20. The methodology that produced ROKU/ECO/PH would have caught
HALO and PH, and missed the other eighteen.**

| Outcome | n | Names |
|---|--:|---|
| PASS (carded-eligible) | **2** | HALO (r67), PH (r92) |
| Blocked by the COOLING veto | **10** | IOVA, FTDR, ALNT, BLFS, DGII, MNPR, UHAL, CHE, RELY, PTGX |
| Failed the readiness / liquidity floor | **8** | AMLX, STGW, EAT, VSXY, PRAX, SAIC, GDX, MLI |

### The floor is set above the median runner
**Runners' readiness at recommendation: median 48, mean 48, range 10-92. Our
A-List floor is 55 — 14 of the 20 scored BELOW it.** Five were under 30: AMLX
(r20, went +35%), DGII (r10, +15%), VSXY (r25, +20%), PRAX (r20, +11%), SAIC
(r24, +9%). **AMLX at readiness 20 is the single most damaging observation for
readiness as a ranker anywhere in this study.**

### The COOLING veto is the other half of the loss
It blocked ten runners, four of them with readiness 70 and ample liquidity —
**PTGX, BLFS, CHE and IOVA** — i.e. genuinely card-worthy by every other test.
Removing the veto lifts recall from 2/20 to 6/20.

**This does NOT mean the veto is wrong.** The runners list is survivorship: it
shows the Cooling names that ran and hides the ones that didn't, while the
detector study measured all 112 and found -5.52% vs IWM with the interval
excluding zero. Both facts are true. The unresolved question is whether Cooling
is a wide-but-real distribution (fat tails: a few big runners paying for many
laggards) or a genuinely negative one. THAT is now the highest-value open
question in the whole programme, because it decides whether we keep or drop half
our historical winners.

### Also confirmed here
The compression component scored ZERO for 12 of the 20 runners — a third
independent confirmation that band width does not mark our winners.

### What this does NOT prove
Recall only. It says nothing about precision — how many NON-runners also cleared
the floors. A selector that carded everything would score 20/20 here. Precision
comes from the eligible-cohort grading in September.

### Consequence
The readiness floor of 55 and the COOLING veto are BOTH now open questions with
measured costs attached, not settled parameters. Neither should be treated as
validated until September grades selected-vs-rejected.

---

# COOLING DISTRIBUTION TEST — 2026-08-06 PM (`scripts/cooling_distribution.py`)
Omar: "test the cooling distribution across all 112 flags."

**VERDICT: COOLING is BROADLY NEGATIVE, not fat-tailed-positive. The veto stands.
But the test surfaced a bigger problem than COOLING — the scanner's STOPS.**

### Test 1+2 — full distribution, buy and hold 21 sessions
| | COOLING (n=112) | BUY-INTENT control (n=67) |
|---|---|---|
| mean | **-5.41%** | +1.03% |
| median | -3.81% | +1.03% |
| win rate | 31% | 58% |
| deciles | -73 -24 -19 -11 -8 -4 -2 +0 +6 +13 | -32 -13 -6 -3 -0 +1 +2 +4 +7 +14 |
| >= +15% | 9 (8%) | 4 (6%) |
| <= -15% | **25 (22%)** | 3 (4%) |
| best / worst | +56.6% / -73.4% | +41.4% / -32.0% |

**Only 2 of COOLING's 10 deciles are positive**, and there are nearly three times
as many -15% disasters (25) as +15% winners (9).

**Tail arithmetic settles it:** COOLING's top decile contributes +2.49 points of
the mean while the other 90% contribute **-7.91** points. The tail is real but
nowhere near large enough to fund the body. Strip the top decile and the mean is
-8.86%.

**This also EXPLAINS the runners-list tension.** 8% of COOLING flags really do
reach +15%, and the best returned +56.6% — the ten COOLING names on the runners
list are that visible 8%. They exist; buying all of them still loses money. The
runners list was survivorship, exactly as suspected.

### Test 3 — the way we actually trade (scanner entry, SCANNER'S OWN STOP, 21-day cap)
| | COOLING | BUY-INTENT |
|---|---|---|
| buy & hold mean | -5.41% | **+1.03%** |
| **with the scanner's stop** | -4.21% | **-0.78%** |
| stop-out rate | **84%** (94 of 112) | 36% (24 of 67) |
| win rate after stops | 15% | 39% |

**THE BIGGER FINDING: the scanner's stops destroy the buy-intent edge.** They turn
a +1.03% mean into -0.78% — the only positive expectancy in the whole study,
erased by its own risk management. The stops are too tight to survive normal
noise over a 21-session hold: one in three buy-intent trades is stopped out, and
in COOLING names five in six are.

**IMMEDIATE CONSEQUENCE — tonight's cards.** The dual-feed A-List I wired hours
ago takes entry AND STOP straight from the scanner. ROKU's stop is 2.2% away.
Those cards inherit the exact stops measured here to destroy expectancy. Before
any origination card is actionable its stop must be replaced with a structure or
ATR-based level per our own execution protocol, sized off that instead.

### Third confirmation of a standing theme
The buy-intent group's entire +1.03% is its top decile too — without it, -1.45%.
Every edge we have is tail-carried, which is exactly what the exit-redesign study
concluded for stocks. Anything that amputates tails (a tight stop, a fixed target)
is more expensive than it looks.

### Limits
Exits modelled AT the stop price (optimistic - gaps are not simulated); 21-session
cap; n=67 on the buy-intent control because fewer flags have a full month; one
regime.
