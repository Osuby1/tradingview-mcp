# Exit redesign — results

Run 2026-07-25 against `research/exit-redesign-preregistration.md`, committed
before the code existed. **12,230 signals** — the identical entry set as the
sector study (Semiconductors alone reproduced its 1,000 signals exactly) — 12
sectors, 2021–2025, entries frozen, only the exit varied. Fills at real prices.
Zero signals skipped for missing stop/ATR.

---

## Verdict: all three challengers FAIL the pre-registered bar

| Rule | Mean | Median | Hit | Mean worst DD | Worst trade | Days held |
|---|---|---|---|---|---|---|
| **A — live (stop + 2:1 target)** | **+0.82%** | −1.70 | 45.9% | −3.37% | −12.0% | 13 |
| B — same stop, no target | +2.06% | −3.93 | 26.0% | −4.66% | −12.0% | 47 |
| C — Chandelier trail (22, 3) | +0.99% | −2.24 | 40.5% | −4.15% | −46.0% | 28 |
| D — 20% ratchet | +4.14% | +2.18 | 54.4% | −9.35% | −46.0% | 94 |
| P21 — pure 21-day hold | +1.28% | +1.06 | 55.5% | −5.16% | −44.9% | 21 |
| **P120 — pure 120-day hold** | **+5.89%** | +4.51 | 60.7% | −12.01% | −67.5% | 114 |

Criteria (declared in advance): B fails 3 of 4. C fails 3 of 4. D fails 3 of 4
(it clears only "beat the live rule by ≥2 pt", at +3.32). Both robustness gates
fail for all three. The dedup cut (3,773 non-overlapping signals) and the
odd/even split give the same ordering with near-identical numbers.

**The pre-committed conclusion therefore stands, verbatim:**

> *No tested exit rule improves on holding across a full cycle. The live stop +
> 2:1 target is retired as a claimed edge; exits in this system are drawdown
> control only, and the passive-core default from the earnings-surprise verdict
> stands unchanged.*

---

## The ordering is the finding

Sort the rules from tightest management to loosest and the means sort
themselves: A (+0.82) → C (+0.99) → B (+2.06) → D (+4.14) → P120 (+5.89).

This is now the **fourth independent measurement** of the same monotonic law in
this system — after the Jan–Jun 2026 replay (−1.18 pt), the ZLSMA sweep (rising
to the grid edge), and the live hand-registered calls. The less the exit
touches the position, the more money is left. There is no clever middle: even
the textbook Chandelier(22, 3) — the classic trend-following exit at classic
settings — trailed out of **97.3% of positions** and kept almost none of the
tail (+0.99%, barely above the live rule).

Why: the return distribution is a lottery (sector study: top 5% of signals =
241% of the excess). Any rule that reacts to a pullback sells the tail's
pullbacks, and the tail IS the profit. The 2:1 target is the worst offender by
construction — it *guarantees* no trade ever pays more than 2R while the losers
still arrive — but the data says every price-reactive exit tested shares the
defect in proportion to its tightness.

## 2022 is the result that kills the idea properly

The whole case for an exit rule is "it saves you in the down year." It did not.

| 2022 (n=1,438) | A | B | C | D | P21 | P120 |
|---|---|---|---|---|---|---|
| Mean | 0.00% | −2.05% | −0.69% | −1.73% | +0.58% | **+0.76%** |

**Every exit rule did worse than doing nothing, in the bear year.** The
protection the exit was supposed to provide had already been provided upstream:
the entry gates cut 2022 signal count by half (1,438 vs 2,702 in 2021) and the
signals that did fire held roughly flat through a −19% SPY year. That is the
regime gate doing its measured job — risk control at ENTRY. The exit then only
added whipsaw: sell the chop, miss the recovery.

This closes the gap the ZLSMA study declared ("exits only tested in a strong
uptrend"). Tested in a real bear market, the exits still lost to holding.

## What exits actually buy, priced honestly

Exits are not worthless — they are *expensive insurance*, and now the premium
is measured:

- **Live rule A:** gives up **5.1 pt of mean return** (+0.82 vs +5.89) to cut
  the average worst-drawdown from −12.0% to −3.4% and cap the worst single
  trade at −12% instead of −67%.
- **Rule D (20% ratchet):** gives up 1.75 pt to cut mean drawdown by 2.7 pt and
  the worst trade to −46%.

Per unit of drawdown avoided, none of it passes the bar set in advance
(≥3 pt drawdown relief while staying within 1 pt of the hold's return). On this
sample the cheapest risk control remains the one already measured elsewhere:
the entry gates plus small position sizing — not per-trade price exits.

---

## Honest caveats

- **Stop fills are optimistic for A and B** — fills assumed exactly at the stop
  price, no gap-through. Real fills would make the tight-stop rules *worse*,
  which strengthens, not weakens, the verdict.
- Drawdowns are close-based; intraday troughs are deeper for every rule alike.
- Survivor universe, hand-picked names, 10 bp costs — shared by all rules, so
  the rule-vs-rule comparison largely cancels them; the absolute levels remain
  flattered.
- Overlapping signals — addressed by the dedup cut, same conclusion.
- One run. No parameter was changed after the registration; D's 20% and C's
  (22, 3) were frozen before any number was seen.

## What this changes

1. **The 2:1 target and the CE(1,2) tight stop are dead as claimed edges.**
   Retired per the pre-committed conclusion. (Rule freeze through 2026-08-31
   still applies to the live pipeline; the claim dies today, the plumbing
   changes only after the freeze, deliberately.)
2. **"Exit skill" is not where the fix is.** Three attempts, three failures, in
   both a trend year and a bear year. Per-trade price exits are a drawdown
   dial, not a return source — present them as exactly that in every plan.
3. **The load-bearing risk controls are the entry gates and position size.**
   Both already exist and both measured well. Sizing (Gap-1 in the frameworks
   doc) is now the only untested lever left in the risk chain.
4. Recorded as hypotheses for possible future registrations, NOT conclusions:
   portfolio-level exits (position-count caps, capital recycling after N days)
   and thesis-break exits (catalyst failed) — neither is testable in this
   price-only harness.
