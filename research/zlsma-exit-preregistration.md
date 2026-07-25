# Pre-registration: ZLSMA scale-out study — semiconductors, 2025

Registered 2026-07-25 **before writing the code**, because this is explicitly an
optimisation ("study the optimum distance below the ZLSMA") and an optimisation
run without rules in place is a curve-fitting exercise by construction.

## The question (Omar's, restated)

Price is above the ZLSMA. When it dips below, take **50% off**. Then either
**reload** if it recovers, or **exit the rest** at some distance below the line.
What is that distance, and does the whole rule beat what we do today?

## What is fixed before running

- **Universe:** US-listed semiconductor + semi-equipment names, liquid, defined
  by ticker list in the script and printed in the results. Chosen before any
  returns were looked at.
- **Period:** 2025-01-01 → 2025-12-31, with 2024 history for indicator warm-up.
- **Entries are held CONSTANT.** Same fresh Chandelier BUY + full gate stack the
  live system uses. This study varies the EXIT only — otherwise a change in
  results cannot be attributed to the exit rule.
- **ZLSMA computed on Heikin Ashi**, matching the live chart Omar reads.
- **Entries and exits fill at REAL closes**, never Heikin-Ashi values.
- **Max hold 120 trading days** or the end of the data, whichever comes first.

## The rules being compared

| | Rule |
|---|---|
| **A** | Today's live rule: Chandelier stop + 2:1 target, 21-day cap |
| **B** | Pure 21-day hold, no management |
| **C** | Pure 120-day hold |
| **D(x)** | 50% off on first close below ZLSMA; remainder on close below ZLSMA×(1−x) |
| **E(x)** | As D(x), but RELOAD to full if the close recovers above ZLSMA first |
| **F** | Sector benchmark: buy and hold SOXX over the same windows |

x is swept from 0% to 15%.

## Rules that protect the answer

1. **The whole curve gets reported, not the peak.** A sharp spike at one value of
   x is evidence of overfitting; a broad plateau is evidence of a real effect.
   The shape is the finding, not the maximum.
2. **Split-sample, both ways.** The optimum is found on one half and then tested
   on the other, split (a) by calendar — H1 2025 vs H2 2025 — and (b) by name —
   alphabetical odd vs even. An optimum that does not survive both splits is
   declared **NOT REAL**, whatever the headline number says.
3. **The peak value of x is reported as IN-SAMPLE and may not be quoted as an
   expected return.** Only the held-out number may be.
4. **Nothing here changes the live system.** Whatever comes out is a candidate
   for a separate forward test, per the rule freeze through 2026-08-31.

## The bar for "worth switching to"

The ZLSMA rule must beat rule A (today's live exit) by **≥ 1.5 percentage points
on the HELD-OUT half**, in both splits. Anything less is noise given the sample.

## Known limits, stated in advance

- **One sector, one year.** Semiconductors in 2025 were a strong trend. A
  trend-following exit will flatter itself in a trending market, and this cannot
  tell us how the rule behaves in a chop or a bear phase.
- **Small sample.** A single sector yields far fewer signals than the full
  universe; the confidence interval will be wide and will be reported.
- **Survivorship.** Delisted names are absent from the price source.
- **I have already seen the Jan–Jun 2026 replay results**, which showed the
  current exits cost 1.18pt. So I am not a blank slate. The protections above
  and the pre-set bar are what stand in for that.
