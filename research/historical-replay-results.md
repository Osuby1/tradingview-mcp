# Historical replay results — Jan–Jul 2026

Run 2026-07-25 against `research/historical-replay-preregistration.md`, which was
committed to git **before** any of this code existed. Nothing below was tuned
after the numbers were seen.

---

## VERDICT: **FAIL** on both pre-registered criteria

Primary window **2026-01-02 → 2026-06-30** (out-of-sample: the gate stack was
built 20–22 July). Primary measure as pre-registered — 21-day hold, exiting early
on the Chandelier stop or the 2:1 target.

| Criterion | Required | Actual | |
|---|---|---|---|
| **C1** — PASSED beats SPY | ≥ +2.0 pt | **−0.56 pt** | **FAIL** |
| **C2** — PASSED beats BLOCKED | ≥ +2.0 pt | **+0.44 pt** | **FAIL** |
| Sample | ≥ 30 | 2,472 PASSED / 8,726 BLOCKED | sufficient |

Net of the assumed 10bp round trip, C1 becomes −0.66 pt. C2 is unchanged, since
both cohorts pay the same cost.

**Pre-committed conclusion for "both fail", quoted from the registration:**

> *The scan as constructed does not beat buying SPY. Given the biases, this is
> close to decisive and would justify stopping work on price-based signals
> entirely, consistent with the momentum-IC and BUY-SCORE findings.*

That stands. Every one of the six known biases flattered the system and it still
failed.

---

## But the diagnostic says the detection is not the problem

Omar's original question was whether the scan would have caught the stocks that
ran. **It would have.**

Of the **138 names that rose 50%+ at some point in Jan–Jun**, the scan produced a
gate-clearing BUY signal before the peak on **109 of them — 79%**.

| Mover | Peak gain | Outcome |
|---|---|---|
| SNDK | +755% | **CAUGHT** — 3 signals, first 2026-03-13 |
| NVTS | +308% | **CAUGHT** — first 2026-01-09 |
| STX | +298% | **CAUGHT** — first 2026-03-16 |
| MU | +298% | **CAUGHT** — first 2026-03-18 |
| ARM | +295% | **CAUGHT** — first 2026-02-11 |
| DELL | +267% | **CAUGHT** — first 2026-02-10 |
| INTC | +262% | **CAUGHT** — first 2026-01-06 |
| AMAT | +175% | **CAUGHT** — 10 signals, first 2026-01-07 |

The memory complex — SanDisk, Micron, Seagate, Western Digital — was caught, and
caught early. **The signal engine finds the moves.**

---

## So where does the edge go? Two places.

### 1. The exit rules are net-negative, and by a lot

This is the single most important number in the whole exercise.

| Cohort | Pure 21-day hold | With stop + 2:1 target | Cost of managing |
|---|---|---|---|
| PASSED | **+2.63%** | **+1.45%** | **−1.18 pt** |
| BLOCKED | +3.31% | +1.01% | −2.30 pt |

Win rate collapses the same way: PASSED goes from **57.4%** on a pure hold to
**48.1%** once the stop and target are applied.

**44% of PASSED signals get stopped out. Only 28% reach the target.** Roughly
three quarters of trades exit before the window closes.

The stops are placed too close to the signal's own volatility and the 2:1 target
caps the winners that pay for everything else. This is the same defect the 14
live hand-registered calls hinted at on 2026-07-25 — ECVT reaching +7.5% and
giving back to +0.9%, SMH +5.6% down to +1.4% — now confirmed on 11,198 signals
over 125 trading days.

**This does NOT mean trade without stops.** It means *these* stop and target
levels are miscalibrated. Removing risk control entirely would change the
drawdown profile completely and is not what the data supports.

### 2. The signal is a firehose, not a screen

**12,378 signals over 140 trading days** — about 88 a day, 2,472 of which cleared
every gate in the primary window alone. The big winners are genuinely in there.
So is everything else. A screen that fires this often cannot function as a
shortlist.

---

## The gate stack picks slightly WORSE stocks, and helps only via risk

On a pure 21-day hold, the names the gates **rejected** beat the names they
**passed**: +3.31% vs +2.63%, a spread of **−0.68 pt**.

The gates only turn positive once stops are applied (+0.44 pt) — and the reason
is mechanical: the ATR-floor and max-stop-percent gates select for names whose
stops sit in a sensible place, so fewer of them get stopped out (44% vs 51%).

**That is a risk-control function, not stock selection.** This is now the third
independent measurement pointing the same way, after the 7/25 drawdown comparison
(−3.1% vs −3.8%) and the live gate-outcomes tracker.

The honest description of the gate stack is: *it does not find better stocks, it
finds stocks you are less likely to be shaken out of.*

---

## Out-of-sample vs in-sample — why the window split mattered

| Window | PASSED vs SPY | PASSED − BLOCKED |
|---|---|---|
| **Jan–Jun (out-of-sample)** | **−0.56 pt** | **+0.44 pt** |
| Jul (in-sample, no pass/fail weight) | +1.28 pt | +0.73 pt |

The rules look meaningfully better on the three weeks of data that shaped them
than on the six months that did not. That is the textbook signature of fitting,
and it is exactly why the registration split the windows before any result was
seen. Had July been included in the headline, the failure would have looked far
milder than it is.

---

## Robustness

Deduplicated to one signal per name per ~30 calendar days, so a name that stays
fresh for a week is not counted five times:

| Cohort | n | Managed | Pure | vs SPY |
|---|---|---|---|---|
| PASSED | 806 | +1.86% | +2.92% | −0.14 pt |
| BLOCKED | 1,635 | +1.50% | +2.84% | −0.07 pt |

Spread +0.36 pt. Same conclusion — the verdict is not an artefact of overlapping
signals.

---

## What blocked the big misses — observation only, NOT a tuning instruction

Of the 29 movers the scan missed, the blocking reasons cluster:

| Mover | Peak | Blocked by |
|---|---|---|
| CAR | +561% | regime DEEP-FAIL (−11.9% vs 200-day) |
| SOXL | +539% | stop 14.1% away (max-stop cap is 12%) |
| SKK | +523% | regime DEEP-FAIL (−43.8%) |
| TWST | +222% | ADX **19.15** (floor is 20) |
| STRL | +215% | −DI ≥ +DI |
| HIMX | +194% | ADX **19.66** |
| HUT | +175% | ADX **19.47** |
| SEZL | +167% | regime DEEP-FAIL (−20.6%) |
| FLEX | +162% | ADX 15.47 |

Three of these missed the ADX floor by less than a point (19.15, 19.47, 19.66
against a threshold of 20).

**This must not be acted on.** The registration explicitly forbids changing a
parameter and re-running, and "lower ADX to 18 and we would have caught three
more monsters" is the precise shape of curve fitting — chosen after seeing which
names ran. Recorded here as a hypothesis for a **separate, forward-tested**
question, never as a change.

The same applies to the DEEP-FAIL blocks: names 20–44% below their 200-day that
then ran hundreds of percent are, by construction, the highest-risk trades in the
universe. The regime gate exists to refuse exactly those. Whether that refusal is
worth its cost is a real question — but it is not answered by looking at the ones
that worked.

---

## What this changes

1. **Stop claiming the scan has a demonstrated edge.** It does not, on six months
   of out-of-sample data with every bias in its favour.
2. **The exit rules are now the top priority, ahead of any new signal work.**
   They cost 1.18 points on the PASSED cohort. That is the largest measured,
   fixable number in the system — and unlike the signal question, it is a
   calibration problem rather than a search for alpha.
3. **The gate stack keeps its job, under an honest description** — risk control,
   not selection. Its measured contribution is a lower stop-out rate.
4. **The detection layer is not the weak link and should not be rebuilt.** 79% of
   the big movers were flagged before their peak.

---

## Method notes

- Indicator port validated against the live 2026-07-24 sweep across 492 names:
  ADX within **0.009%**, ATR **0.005%**, DI **0.007%**, regime string match
  **99.6%**. The replay runs the real rules, not an approximation.
- `gate_stack.evaluate()` imported unchanged, never re-implemented.
- Empirically settled during validation: the live sweep computes the **entire**
  gate stack on Heikin-Ashi bars, not raw prices (raw-OHLC error was 18% on ADX,
  29% on DI). The replay matches that so it tests the live system.
- **Entries and exits are graded at REAL closing prices**, not Heikin-Ashi ones,
  so the returns above are achievable rather than notional.
- Five symbols excluded — BHP, COCO, DTE, EQR, SFL — which the live sweep
  resolves to foreign listings of different companies. Reported separately as a
  live data-quality defect.
- One run. No parameter changed, no gate added or removed, no outliers excluded.
