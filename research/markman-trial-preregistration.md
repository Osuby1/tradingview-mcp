# Markman 30-alert trial — pre-registration (DRAFT 2026-08-03)

**Status: DRAFT.** Omar is subscribing (announced 2026-08-03). This freezes
into a binding pre-registration — a dated FROZEN section added below — BEFORE
the first live alert is acted on. If the subscription unlocks historical
recommendations, that data may refine the draft criteria BEFORE the freeze,
never after. Origin: the 7/31 newsletter audit (research/markman-ledger.json,
commit 23be6c7) — their record was real (12W-5L, +15.4%/position in a 2021
bull tape) but 0/44 recs passed our structure rules (they trade ~18-DTE
options; we require 45-90), two overall-gain claims were inflated ~2x, and
one loss vanished. Verdict then: "take their ideas, never their contracts."

## The trial

- **Scope: the first 30 live Markman options alerts** after subscription.
- Every alert is screened within the day by `scripts/markman_screener.py`
  and logged to `research/markman-trial-ledger.json` — takes AND skips.
- **Both cohorts are paper-tracked in BOTH forms:** (a) their literal
  contract at their stated/first-available price, (b) OUR translation
  (same ticker+direction, 45-90 DTE, delta .60-.75, $2.5k sizing).
  Nothing real-money during the trial (options overlay paper-only rule
  applies on top).

## DRAFT take/skip line (subject to refinement until freeze)

SKIP if ANY of:
1. Their contract fails the live-chain reality check (no bid / crossed or
   stale book / OI and spread outside standards).
2. **Earnings inside the hold window** — the one gate with observed teeth
   in the audit (in-window trades -29% vs +22% clean, n=2 = a hint).
3. Stock regime DEEP-FAIL (>10% below its 200-day).
4. No compliant our-translation contract exists.
Otherwise TAKE (as our translation, paper).

## Outcomes and verdict (to be FROZEN)

- Grade each alert at their stated exit, or at our exit rules for the
  translation cohort (+100% / -50% / 21-days-to-expiry), whichever applies
  to that cohort.
- **Primary question: do TAKES beat SKIPS by a real margin?** Secondary:
  does OUR translation beat their literal contract on the same signals?
- **Kill criterion (draft): if takes do not beat skips after 30 alerts,
  the screener adds nothing to their feed — cancel the subscription with
  evidence.** Cost of a clean kill: a month or two of fees, zero real dollars.
- No verdict before 30 alerts resolve; interim Friday reports are
  counts-only, no conclusions.

## Standing cautions

- The 2021 audit sample cannot validate ANY classifier (10 sunny weeks,
  17 filled trades). Historical data, if unlocked, informs design only.
- The screener's card is fact (live chain, earnings, posture); its
  take/skip LINE is hypothesis until this trial grades it.

## FROZEN 2026-08-03 (authority: Omar's order to operationalize the filter)

The take/skip line is now BINDING for the 30-alert trial. SKIP if ANY of:
1. Their contract fails the live-chain reality check (no bid / crossed or
   stale book / OI+spread outside standards).
2. Earnings or a known binary event inside the hold window.
   [calibration: 1W-4L avg −74% in-window vs +22% clean, p≈.03]
3. Stock regime DEEP-FAIL (>10% below its 200-day).
   [n=1 historically, kept unvalidated]
4. **Entry delta < 0.45 OR strike >10% out of the money.** [THE EMPHASIS
   finding: ≥0.45 went 14W-3L-1P ~+38%; below went 8W-8L ~−25%; every
   near-total loss was OTM]
5. No compliant 45-90 DTE delta .60-.75 translation exists.
Otherwise TAKE. Verdict quotes their contract; translation cohort uses OUR
exits (+100%/−50%/21-days), which the calibration showed are load-bearing.
No edits to these five lines until the 30-alert verdict. Kill criterion
unchanged: takes must beat skips or the subscription is cancelled with
evidence. p-values above are multiple-comparison-flattered; the trial is
the test, this filter is the hypothesis.
