# Pre-registration: Do "EXTENDED — don't chase" runners keep paying?

**Registered:** 2026-07-30, before any data is computed. Prompted by PBF (+14.8%
on earnings day AFTER the extension flag; a hypothetical rule-breaking $70 Aug
call would have doubled overnight) and CORT (+30% single day after its flag).
Two lottery hits are NOT evidence — this study is the honest version of the
question. Run at the Friday 2026-07-31 hard-stats review or the next one after.

## Question

When the live-picks radar flips one of OUR OWN recommendations to
"EXTENDED — don't chase," what actually happens next — and would a
rules-compliant long-options expression entered AT the flag have positive
expectancy?

## Sample (fixed before looking)

EVERY extended-flag transition ever emitted by `scripts/live_picks_radar.py`
since the radar started — reconstructed from its state/ledger files and, where
gaps exist, recomputed by replaying the radar's own extended-threshold rule over
daily bars from each pick's reco date. **No exclusions.** PBF and CORT enter the
sample on the same terms as every flag that died quietly. If the total sample is
under 15 flags, the verdict is auto-downgraded to "insufficient data — keep the
don't-chase rule" regardless of the numbers.

## Measurements per flag

1. Underlying forward total return at +5, +10, +21 trading sessions from the
   first close after the flag; same windows for SPY (benchmark).
2. Max adverse excursion (worst drawdown from flag price) inside 21 sessions.
3. Simulated rules-compliant option: the call closest to delta 0.65 (Black-
   Scholes via `scripts/options_analysis.py` machinery), 45-90 DTE at flag
   date, priced with IV = max(realized-20d, realized-60d) x 1.1 as the honest
   synthetic proxy (LABEL: synthetic pricing, not real quotes). Skip (and count
   as "blocked") any flag with earnings inside the option's hold window — the
   overlay's blackout rule applies to the simulation too. Exit per live overlay
   policy A: +100% take, -50% cut, 21-days-to-expiry time exit, 21-session cap.

## Pre-registered verdict lines (written before results)

- **Stock layer:** extended flags "keep paying" only if median +10-session
  return beats SPY's AND the hit rate (positive +10s return) is >= 55%.
- **Options layer:** the compliant-option simulation must show positive
  expectancy per trade net of the -100% losers, with >= 15 tradeable
  (non-blocked) flags.
- **Action mapping:** BOTH pass -> design a paper-only "extension continuation"
  entry for the options overlay, itself pre-registered, minimum 30 paper trades
  before any real money. Either fails -> the don't-chase rule STANDS and the
  PBF/CORT anecdotes are formally closed as survivorship noise. No middle
  outcome may be argued from the same data after the fact.
- These thresholds change only via an explained commit BEFORE the study runs.
