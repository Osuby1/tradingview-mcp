# Fresh-Ignition exit search — pre-registration

Committed 2026-07-26, BEFORE any study code exists.

## Honesty header — what kind of test this is

This is a SECOND-stage search on the same 2021–2025 data that just graded the
A-grade Fresh Ignition cohort (mean −1.3 pt vs SPY under Omar's rule). Any
search produces a "best" cell by chance, so: the candidate set is THREE rules
chosen for mechanism and frozen here; no parameter sweeps; and any winner is
HYPOTHESIS-GRADE ONLY — eligible for the shadow lane, never live from this
test. Known context that shapes expectations, declared: five prior
measurements all found looser-beats-tighter, holding beats managing, and this
entry cohort has no alpha to protect (60d hold ≈ −0.15 pt vs SPY).

## Frozen design

Entries: the identical 1,512 A-grade Fresh Ignition episodes (same code path,
same universe, same approximations as `fresh_ignition_backtest.py`). 10 bp
costs. All exits capped at 250 trading days.

**Candidates (mechanism stated, no knobs):**
- **E1 — Trend-break:** hold through anything (including Cooling) until the
  scanner's own Stage-2 test fails (close below 200-day SMA, or 50-day below
  200-day, or 200-day falling vs 21 days ago). Exit at that day's close.
  Mechanism: Cooling names drift UP (+0.39 fwd); heat is not the enemy,
  trend death is.
- **E2 — Structure:** exit on the first close below the scanner's own
  pullback-zone floor (min of 20-day EMA and 50-day SMA), computed daily.
  Mechanism: the scanner defines where a healthy pullback holds; closing
  through it means the pullback failed.
- **E3 — Omar's rule + floor:** exit on the first COOLING day OR the first
  close below the E2 floor, whichever comes first. Mechanism: repairs the
  one measured defect of the original rule (no downside floor) while keeping
  its harvest behavior, so the comparison isolates what the floor is worth.

**Baselines:** pure holds at 60, 120 and 250 days; the live 5%-stop +
20%-ratchet rule; and Omar's original sell-on-Cooling (R1) for continuity.

**Metric:** mean excess vs SPY over each trade's own window; median, hit
rate, mean days, worst trade; per-year with 2022 always shown; odd/even
alphabetical halves.

## Selection rule — declared now

A candidate is named "the exit" ONLY if ALL hold:
1. Full-sample mean excess beats the BEST pure hold by ≥ +1.0 pt.
2. Mean excess is higher than R1's in BOTH odd and even halves.
3. Its 2022 mean excess is not more than 2 pt below the best pure hold's 2022.

If no candidate clears all three, the pre-committed conclusion is: **"There is
no clever exit hiding in this cohort. The tab machinery adds nothing to exit
timing; if the cohort is traded at all, use the measured default (hold long /
stop + ratchet) and accept that the entry, not the exit, is the constraint."**

Three candidates = three chances; margins above are set so a lucky ranking
cannot clear them. One run. No additions after this commit.
