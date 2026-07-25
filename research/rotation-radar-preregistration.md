# Pre-registration: does the rotation radar predict anything?

Registered 2026-07-25 **before writing the code**. This is the last major
unmeasured component in the system, and the sector-vs-stock-picking result
(aad9be3) makes it the one that matters most: if the sector call is where the
value lives, the answer is "buy the ETF." If the sector call is also noise, there
is no top-down edge either.

## What is being tested

`scripts/rotation_radar.py` scores 29 sector ETFs with:

    accel = Perf.1M − (Perf.6M / 6)

and assigns a state with these thresholds, **used unchanged**:

| State | Rule |
|---|---|
| IGNITING | accel ≥ +8 **and** beating SPY on 1M **and** week > −2 |
| WATCH | accel ≥ +4 |
| ROLLING | accel ≤ −6 **and** 6M performance ≥ +10 |
| NEUTRAL | everything else |

## Fixed now

- **Universe:** the radar's own 29 ETFs, unchanged. SPY is the benchmark, not a
  candidate.
- **Period:** 2021-01-01 → 2025-12-31, five years, reported year by year,
  including 2022.
- **Reconstruction:** Perf.W / 1M / 6M rebuilt from daily closes as 5 / 21 / 126
  trading days. **Validated against the live radar output for 2026-07-24 before
  any forward return is computed** — if the reconstruction does not reproduce the
  live accel values and states, the test is not run.
- **Horizons:** 21, 60, 120 trading days. **60 is the primary**, declared now.
- **Sampling:** **weekly (every 5th trading day) is primary.** Daily observations
  overlap almost completely and would overstate the sample size by ~5x. Daily is
  reported as robustness only.
- No parameter is tuned. The thresholds above are the live ones.

## The measures

1. **IGNITING forward return vs SPY**, same windows.
2. **IGNITING minus ROLLING** — does the state ranking separate anything?
3. **IGNITING vs an equal-weight basket of all 29 ETFs** — the honest "just own
   everything" alternative.
4. **Rank correlation (IC) between accel and forward return**, across sectors at
   each date.
5. **Control: does accel beat plain 1-month momentum?** If ranking by Perf.1M
   alone does as well, the acceleration formula adds nothing and the radar is a
   momentum screen with extra steps.

## Pre-committed conclusions (primary = 60 days, weekly sampling)

| Result | Conclusion |
|---|---|
| IGNITING beats SPY by **≥ +2pt** AND beats ROLLING by **≥ +2pt** | The radar predicts. Sector selection is a real edge and is where to build. |
| Both between **−2 and +2pt** | The radar does not predict. It describes what has already moved. Stop using it to allocate. |
| IGNITING **≤ −2pt** vs SPY | The radar is actively harmful — it is buying tops. Stop using it entirely. |

Plus, independent of the above: **if accel does not beat plain 1M momentum, the
acceleration formula itself is not earning its keep**, whatever the states do.

## Anti-force-fit rules

1. Every state, every sector, every year reported — nothing dropped.
2. No threshold moved. No horizon promoted after the fact.
3. The reconstruction is validated against live output *first*; a failed
   validation stops the test rather than being patched until it agrees.
4. One run. A genuine bug means a disclosed re-run showing the pre-fix numbers.

## Known limits

- **Survivorship-free but backfill-prone:** these ETFs all existed throughout, so
  no survivorship issue, but ETF returns include their own internal turnover.
- **Overlapping windows** remain even at weekly sampling; confidence intervals
  are wider than the raw n suggests and will be described that way.
- Five years is one broad regime cycle, not many.
