# Shadow detector pre-registration: WOC (Washed-Out Coil)

**Registered:** 2026-07-22
**Status:** SHADOW LANE — logging only. **NOT a live rule.**
**Governance:** rule freeze through 2026-08-31 (commit `2d673c6`). No new live rules
until measured. This document is the pre-registration; its git commit timestamp is
the proof the rule was fixed *before* the results were counted.

---

## Why this exists

On 2026-07-21 the origination scan looked at SMCI and threw it away. It landed on
the `Excluded — not screenable` tab: score 27.2, grade SKIP, trading at 38.2% of its
52-week high and 28% below its 50-day average. The next session it opened +4% and
ran +34% intraday.

Nothing in the live system could have caught it, and that is a structural fact, not
an accident:

- The **origination scan** is a Stage-2 *leader* screen. It hunts stocks starting
  healthy runs near their highs. A name 62% off its high fails the health gate by
  construction.
- The **O.G Chandelier universe run** is a trend-continuation read. SMCI was in
  `SELL` mode until 7/21.
- The **EOD ignition sweep** never flagged it either.

A washed-out name turning is a *different shape* from a leader continuing. The
system has no detector for it. This is that detector — in the shadow lane, where it
gets graded before anyone trades it.

The insight it exploits: the Excluded tab is ~900 rows a day of discarded data that
already contains every metric needed. SMCI's own discarded row on 7/21 said
`Coiled Spring = Y`, ADX 25 and rising, and carried a computed buy zone of
28.15–33.09 — which the next session's move ran straight through. The math was
already there. The health gate deleted the row before anyone could see it.

---

## The rule (frozen)

### Stage 1 — the "before photo" (`woc-v1`)
Read the `Excluded` tab of `reports/origination_scan_<date>.xlsx`. Flag a row when
**all five** hold:

| # | Condition | Threshold |
|---|---|---|
| 1 | Washed out | `% of 52-Wk High` ≤ 50% |
| 2 | Coiled | `Coiled Spring? = Y` |
| 3 | Not yet moved | `Volume vs Normal (today)` < 1.5 |
| 4 | Not in freefall | 25 ≤ `RSI Daily` ≤ 50 |
| 5 | Trend structure exists | `ADX` ≥ 20 |

Implementation: `scripts/shadow_woc_detector.py`

### Stage 2 — the ignition trigger (`woc-trigger-v1`)
A name triggers on day N when:

- it was on the stage-1 list on day **N-1**, **and**
- `Volume vs Normal (today)` ≥ **2.0** on day N, **and**
- it closed **higher** than day N-1.

Implementation: `scripts/shadow_woc_trigger.py`

**Five conditions, one threshold each, no weights, no score.** Anything more tuned
would be fitting to a single stock and would not survive out-of-sample.

---

## Measured signal rate — before any grading

Run across every origination workbook in `reports/`:

| Date | Stage-1 hits | Excluded rows scanned |
|---|---|---|
| 2026-07-18 (Sat) | 41 | 897 |
| 2026-07-19 (Sun) | 41 | 897 |
| 2026-07-20 | 41 | 897 |
| 2026-07-21 | 38 | 899 |

*(7/18 and 7/19 are byte-identical weekend copies — one trading session, not two.)*

**Stage 1 fires on ~40 names per day. That is a watch list, not a buy signal.**
Shipping stage 1 alone as a trigger would be dishonest — at 40 names/day you would
"catch" almost any mover and could claim credit for it afterwards.

Stage 2, applied 7/20 → 7/21, fired on **1 name**: ACHR, 4.44 → 5.31 (+19.6%) on
2.83x volume, at 36.3% of its 52-week high.

---

## The uncomfortable result — recorded before it can be forgotten

**SMCI does not trigger on 7/21.** It appears on the stage-1 watch list and nowhere
else.

> **CORRECTION 2026-07-22.** The first version of this document said "volume was
> 0.55x normal" on 7/21 and put the 7/21 close at $23.83. Both were wrong, because
> **the origination workbook runs one session behind its own filename** - the file
> named `2026-07-21` contains 7/20 data. Verified against the live TV feed:
>
> | Session | Close | Volume | RelVol (50d) |
> |---|---|---|---|
> | 7/20 | 23.83 | 24.9M | 0.45 |
> | 7/21 | **25.50** | 51.2M | **0.96** |
> | 7/22 | 30.93 | 131.9M | **2.48** |
>
> The conclusion survives - 0.96x is still far below the 2.0 trigger, so the
> detector still does not fire on 7/21 - but it survives on different numbers than
> originally claimed. SMCI's real 7/21 session (+7% on rising volume, before the
> after-hours announcement) was never visible to the scan at all.

The ignition bar came the *next* session, 7/22, at 2.48x volume. So a volume-confirmed
version of this detector would have bought SMCI on **7/22 near $30**, not on 7/21 at
$25.50.

That matters for how the original miss gets scored. The honest accounting:

- The coverage gap (SMCI absent from the scanned universe) was **real** and is worth fixing.
- But **no volume-confirmed system fires before the gap.** The missed entry was never
  $23.83. Any claim that this detector "would have caught the 34% move" is false, and
  this paragraph exists so that claim cannot be made later.

The detector's real value is the *watch list*: SMCI would have been one of ~40 names
under active observation going into 7/22, instead of invisible.

---

## Promotion criteria

Per the shadow-lane policy, WOC may **not** go live until:

1. **20–30 out-of-sample stage-2 signals** have been logged and graded, all dated
   after this commit.
2. Measured against the incumbent benchmark, defined here in advance:
   - **Benchmark A:** SPY over the identical holding window.
   - **Benchmark B:** the origination scan's own A/B-grade calls over the same window
     (the `TRACKER` tab / `recommendations_log.csv`).
3. Grading window: **21 trading days** per signal, matching the existing TRACKER
   convention so the numbers are comparable.
4. Recorded per signal: entry, 21-day return, max favorable/adverse excursion,
   stop-hit yes/no.

At ~1 stage-2 signal/day, that is roughly **4–6 weeks** of data. The freeze runs to
2026-08-31 regardless.

**If the hit rate does not beat both benchmarks, this detector gets deleted, not
loosened.** Widening thresholds to manufacture signals is the failure mode this
pre-registration exists to prevent.

---

## Known limitations

- **One session of real out-of-sample data** (7/20 → 7/21). Four workbooks exist but
  only two are distinct trading days. Everything above is provisional.
- **The input data lags one session.** Confirmed 2026-07-22: workbooks are named
  for the day they were generated but contain the PREVIOUS completed session. The
  stage-1 -> stage-2 comparison is still between consecutive sessions so the logic
  holds, but every date label in this document is one session ahead of the data
  behind it. Fix the generator or rename the files before grading starts, or the
  ledger will be permanently off by one.
- **Survivorship/selection:** the Excluded tab's composition depends on the
  origination scanner's own gates, which sit outside this repo
  (`Documents\Equities_Scanner\stage2_leader_scanner_v3.py`). If those gates change,
  this detector's input distribution changes silently.
- **No catalyst awareness.** A washed-out coil that ignites on news is
  indistinguishable here from one that ignites on flow.
- **Not tested through a hostile tape.** Every observation so far is from a single
  week.

---

## Files

| Path | Role |
|---|---|
| `scripts/shadow_woc_detector.py` | Stage 1 — watch list |
| `scripts/shadow_woc_trigger.py` | Stage 2 — ignition trigger |
| `research/shadow-woc-ledger.json` | Stage-1 output, all dates |
| `research/shadow-woc-trigger-<date>.json` | Stage-2 output per session |
