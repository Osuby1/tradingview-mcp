# Pre-registration: historical walk-forward replay of the scan, Jan–Jul 2026

**Registered 2026-07-25, BEFORE writing the replay code or looking at any result.**
Committed to git first so that neither the method nor the success bar can move
after the answer is known.

Omar's question: *"if I look back at stocks that ran, would what we measure have
caught them?"* — asked explicitly with the concern *"I don't want a data-fitting
exercise."*

That concern is correct, and it is why this document exists.

---

## 1. Why the obvious version of the test is not being run

The intuitive test is: take the stocks that ran 50%+ (memory names, energy names)
and check whether our scan flagged them.

**That test cannot fail, so it cannot teach us anything.** Our rules buy things
in uptrends. SanDisk (+422% this year), Micron (+192%), Seagate (+218%) and
Western Digital (+177%) were in uptrends for most of 2026. So were a great many
stocks that went nowhere. Selecting the sample on the outcome removes the
denominator — you learn that the scan can flag a stock that went up, which is
already known, and nothing about whether following it made money.

So the winners are **not** the test. They are the diagnostic, in section 6, run
only after an unbiased result exists.

---

## 2. What will actually be run — fixed now

A day-by-day forward replay, using only data available on each decision date.

**Signal engine.** The `og_shadow.py` port (Heikin-Ashi Chandelier Exit 1/2,
ZLSMA-50, CCI-20 as the Magical proxy), extended to evaluate every historical bar
instead of only the latest. Measured agreement with the live chart: **85.8%** on
2026-07-24.

**Gate engine.** `gate_stack.evaluate()` **imported unchanged**, never
re-implemented inline. Position size stays at the `DEFAULT_POSITION` of $85,000
so the liquidity gate behaves exactly as it does live.

**Procedure.** For each trading day D, for each symbol in the universe:
- compute indicators from bars **up to and including D only**
- if the Chandelier flipped to BUY within the previous 5 bars, it is a *fresh
  signal*
- run the gate stack on it and record the verdict as **PASSED** (CANDIDATE or
  STARTER ONLY) or **BLOCKED**
- entry is the **close of day D**. No intraday fills, no better price assumed.

**Grading.** Primary measure mirrors `outcome_tracker.py`: hold 21 trading days,
but exit early if the Chandelier stop or the 2:1 target is hit first. A pure
21-day hold with no stop or target is recorded alongside, so that signal quality
and exit-rule quality can be separated — exits were identified on 2026-07-25 as
the system's weakest link, and this is the chance to measure them.

**Benchmark.** SPY over the identical calendar window for every signal.

**Universe.** The current ~494-name list. See bias 1 below.

---

## 3. The windows

| Window | Dates | Status |
|---|---|---|
| **Primary** | 2026-01-02 → 2026-06-30 | **Out-of-sample. This is the test.** |
| Secondary | 2026-07-01 → 2026-07-24 | In-sample. Reported, but carries no pass/fail weight. |

The split is not cosmetic. The gate stack was built on **20–22 July 2026**, in
direct response to specific July events — the GDX regime veto, the SKK liquidity
miss, the FRT stop-inside-noise case, the DELL wide-stop case. Judging those rules
on July data is marking my own homework. January to June is roughly 125 trading
days during which neither the rules nor the observations behind them existed.

---

## 4. Success criteria — pre-specified, on the PRIMARY window only

Reported on **gross** returns. Net of an assumed 10bp round-trip cost is reported
beside it, and flagged loudly if the cost changes the verdict.

**Minimum sample.** If fewer than **30** PASSED signals occur in the primary
window, the result is declared **NO VERDICT — INSUFFICIENT SAMPLE**, and no
conclusion is drawn in either direction.

The test **PASSES** only if **both** hold:

- **C1 — beats the index.** Mean 21-day return of PASSED signals exceeds the mean
  SPY return over the same windows by **≥ +2.0 percentage points**.
- **C2 — the gates earn their keep.** Mean 21-day return of PASSED signals exceeds
  that of BLOCKED signals by **≥ +2.0 percentage points**.

**C3 — hit rate above 50%** is recorded as descriptive only. A strategy can be
profitable at a 40% hit rate and unprofitable at 60%; making it a gate would risk
a false negative on an otherwise sound result.

C2 is the criterion that matters most. It is the only one that isolates what the
gate stack itself contributes, as opposed to what the market did.

---

## 5. What each outcome will be taken to mean — committed now

| Result | Pre-committed conclusion |
|---|---|
| **C1 and C2 both pass** | The scan showed a real edge over this window. Given every bias below runs in its favour, this is **suggestive, not proven** — the response is forward validation, not more size. |
| **C2 fails** | The gate stack is a **risk control, not a source of return.** Stop describing it as the system's strength. Its measured benefit becomes the drawdown reduction already observed (−3.1% vs −3.8%), and loosening it becomes a legitimate thing to consider. |
| **C1 fails, C2 passes** | The gates help relative to our own signals, but the whole system still fails to beat simply owning the index. The **Chandelier entry signal** is then the weak link, not the gates. |
| **Both fail** | The scan as constructed does not beat buying SPY. Given the biases, this is close to **decisive** and would justify stopping work on price-based signals entirely, consistent with the momentum-IC and BUY-SCORE findings. |

---

## 6. The diagnostic — secondary, and explicitly not pass/fail

Only after the above is computed and recorded:

For every name that rose **≥50% at any point** within the window, report whether
it ever produced a PASSED signal before the bulk of its move, and for the misses,
**which specific gate blocked it**. Memory and energy names are called out by name
since that is what prompted the question.

This answers Omar's original question and is the most *interesting* output. It is
also the part most vulnerable to storytelling, so it is quarantined here and
cannot influence the verdict.

---

## 7. Known biases — all of them push the same way

1. **Curated universe.** The 494-name list is what Omar watches *today*, shaped by
   what he noticed running this year. Using it for a January replay imports
   hindsight.
2. **Survivorship.** Delisted and bankrupt names are absent from the price source,
   so losers are systematically under-represented.
3. **Reconstruction error.** The signal port agrees with the live chart 85.8% of
   the time, not 100%.
4. **Partial in-sample.** Mitigated by the window split, not eliminated.
5. **No slippage or market impact** beyond the existing liquidity gate.
6. **Clean-data assumption.** Entry at the official close, always filled.

**Every one of these flatters the system.** That asymmetry is the single most
useful property of this test:

> A **failure** is close to decisive, because the deck was stacked in favour.
> A **pass** is only suggestive, and the margin should be assumed inflated.

---

## 8. What will NOT happen

- No parameter will be changed and the test re-run. Not the ADX floor, not the
  5-bar freshness window, not the 21-day hold, not the $85k size.
- No gate will be added or removed after seeing results.
- The universe will not be changed after seeing results.
- No "outliers" will be excluded.
- **One run.** If a genuine bug is found, it will be fixed and re-run — and the
  fact that it was re-run, and why, will be stated in the results with the
  pre-fix numbers shown.

This is the same discipline applied to the PEAD refinement on 2026-07-22, which
then **failed its own bar and was recorded as a failure** rather than retuned.
The precedent is the point.

---

## 9. Deliverables

- `scripts/historical_replay.py` — the replay, importing `gate_stack` unchanged
- `research/historical-replay-results.md` — every number above, verdict first
- `research/historical-replay-signals.json` — every signal, for independent re-checking

**Registered before any code was written or any result seen.**
