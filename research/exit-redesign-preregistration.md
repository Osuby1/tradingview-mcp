# Exit redesign — pre-registration

Committed 2026-07-25, BEFORE any study code exists. Same contract as every test
this week: the rules, the universe, the metrics, the success bar and the
conclusion for every possible outcome are frozen here. Nothing may be tuned
after a number is seen.

---

## Why this test, and why now

Two independent measurements this week said the same thing:

1. **Jan–Jun 2026 replay** (11,198 signals): the live stop + 2:1 target cost the
   PASSED cohort **−1.18 pt** vs a pure 21-day hold. 44% stopped out, only 28%
   reached the target. Win rate fell from 57.4% to 48.1%.
2. **ZLSMA study** (386 semi signals, 2025): the live rule returned **+0.12%**
   per signal while doing nothing returned +16.40%. Every managed exit tested
   lost to not exiting, monotonically to the edge of the grid.

And the return distribution is a lottery: in the sector study the **top 5% of
signals carried 241% of the total excess**. A system whose entire profit lives
in the tails cannot use an exit that caps the tails — the 2:1 target does
exactly that, by construction.

The declared gap in the ZLSMA study was: *exits were only tested in a strong
uptrend, where "never sell" wins by construction.* This test closes that gap by
running 2021–2025 across 12 sectors — **including 2022, a real bear market**,
which is where an exit rule must earn its keep.

## The question

**Is there an exit rule that keeps the tail winners (which are all of the
profit) while still cutting losses — and does it survive a down year?**

This test holds ENTRIES constant (the same gate-passing fresh BUY signals as
`sector_vs_stockpicking.py`, unchanged) and varies ONLY the exit.

---

## Frozen design

**Universe & entries** — identical to `research/sector-vs-stockpicking-preregistration.md`:
the same 12 sector baskets (frozen symbol lists imported from
`scripts/sector_vs_stockpicking.py`), 2021-01-01 → 2025-12-31, fresh BUY =
Chandelier flip to BUY within 5 bars, gate stack imported and applied unchanged,
signal dates where gate verdict is not BLOCKED. Entry at the REAL close of the
signal day. All exits graded at REAL prices. Round-trip cost 10 bp reported on
every rule (one round trip each; no rule reloads).

**Rules under test** — four rules, two controls. No parameter sweeps anywhere;
each challenger is a single frozen specification. This is pass/fail, not a search.

| Rule | Specification |
|---|---|
| **A — live baseline** | Exactly as measured in the Jan–Jun replay: static stop at the entry-day Chandelier distance (HA-derived, converted to real-price %), target at 2× the stop distance, intraday fills, max 21 trading days. |
| **B — keep the stop, kill the target** | Same static entry stop, intraday fill. **No target.** Max 120 trading days. Isolates the cost of the target alone. |
| **C — classic Chandelier trail (22, 3)** | Trailing stop = highest real close since entry − 3 × ATR(22) on raw OHLC (22-day simple mean of true range, prior completed bars). Ratchets up, never down. Exit at the day's CLOSE when close < the trail level established through the previous day. No target. Max 120 trading days. The textbook trend-following exit, at textbook settings — deliberately NOT the live CE(1, 2.0), whose 1-bar lookback makes it hyper-tight. |
| **D — 20% ratchet** | Trailing stop = 0.80 × highest real close since entry. Same close-based mechanics as C. No target. Max 120 trading days. A single frozen "let it breathe" level between the ZLSMA study's boundary hint (15%) and the classic 25% position-trading trail. Chosen without any sweep. |
| **Control P21** | Pure hold, exit at close of day 21. (Comparator for A.) |
| **Control P120** | Pure hold, exit at close of day 120. (Comparator for B, C, D.) |

**Metrics per rule** — mean %, median %, hit rate (return > 0), mean days held,
exit-type breakdown, **mean worst drawdown from entry while the position is open**
(close-based trough vs entry), worst single trade, per-year table with 2022
reported no matter what, and a deduplicated robustness cut (first signal per
name per 30 calendar days) — headline stays on the full set, matching the
sector study's convention.

---

## Success bar — all four required, declared now

A challenger (B, C or D) **passes** only if, on the full 2021–2025 sample:

1. **Keeps the tail:** mean return ≥ P120 mean − 1.0 pt.
2. **Earns its keep as risk control:** mean worst-drawdown-while-held is at
   least 3.0 pt shallower than P120's.
3. **Protects in the down year:** 2022 mean ≥ P120's 2022 mean + 1.0 pt.
4. **Beats the incumbent:** mean ≥ rule A mean + 2.0 pt.

**Robustness gate:** criteria 1 and 3 must also hold in BOTH halves of an
odd/even split by alphabetical symbol index. A pass on the full sample that
fails either half is reported as **FRAGILE** and does not count.

**Multiplicity rule, declared now:** three challengers get three chances, so a
lucky pass is possible. If more than one passes, adopt the one with the LARGER
margin on criterion 2 (drawdown improvement) — the risk-control criterion — not
the higher mean return. If exactly one passes, that is the candidate.

## Pre-committed conclusions

- **No challenger passes all four →** "No tested exit rule improves on holding
  across a full cycle. The live stop + 2:1 target is retired as a claimed edge;
  exits in this system are drawdown control only, and the passive-core default
  from the earnings-surprise verdict stands unchanged."
- **A challenger passes →** it does NOT go live. It becomes the paper-book exit
  rule, forward-tested against rule A on live signals from the next trading day,
  graded weekly, through at least 2026-08-31 (the standing rule freeze). Only a
  forward-test win can change the live rule. The pass is described as "survived
  one backtest" — nothing stronger.
- **A challenger passes on returns but fails the 2022 criterion →** reported as
  "trend-year artefact, same shape as the ZLSMA result" and not adopted.

## Biases, stated in advance

Survivor-listed baskets, no slippage beyond 10 bp, and hand-picked well-known
names — all flatter every rule equally. Because every comparison here is
rule-vs-rule on identical entries, these biases mostly cancel; they do NOT
cancel for the drawdown numbers, which are optimistic in absolute terms.
One run. No parameter changes after this commit.
