# Readiness score — first calibration look (2026-08-01, Saturday)

**Status: informal backward look, NOT the pre-registered forward calibration.
Logged because the result is a warning that must survive the weekend.**
Method: `readiness()` from `scripts/options_analysis.py` (math untouched),
history truncated to each pick date (same NY-timezone handling as
`readiness_batch.py`), long direction, Yahoo adjusted closes.

## Test: runners vs dead money, as of pick day

Same 2026-07-02..08 pick window, skipped picks only (nothing actioned).

| group | n | mean | median | range |
|---|---|---|---|---|
| top-10 skipped runners (+14% to +54%) | 10 | 47 | 49 | 16-95 |
| went-nowhere (|ret| <= 3% AND best-ever <= +6%) | 21 | 43 | 41 | 8-80 |

**Verdict: NO separation.** ~4 points of mean difference at these sample
sizes is noise. 60% of runners scored >=46 at pick — but so did 38% of the
dead-money group.

Instructive individual failures:
- PSA scored **80** at pick (2nd-pctile squeeze, at trigger, RS extreme) —
  never got 2.1% off the ground.
- PTGX scored **70** with the same momentum+RS signature as PBF/DK — flat.
- LEVI and EGBN had the formal TTM squeeze ON — neither moved.
- CAKE scored **16** and ran +30% (earnings gap); CDNA scored 30 (bands 91st
  pctile, move already underway) and ran +54% — the biggest runner.
- CORT was the one clean hit: 95 at pick -> ran +21.8% -> scored 40 by 7/31
  (spring released). One hit is an anecdote, not calibration.

## Interpretation (three candidate explanations, undecided)

1. The score genuinely has little timing power on our pool.
2. Restriction of range — every name already passed the scan's filters;
   candidate-vs-candidate is where any tool discriminates worst.
3. Three weeks of one regime (defensives dumped, AI/energy chased) is one
   tape's verdict, not a general one.

## Standing consequences (already applied)

- The "UNCALIBRATED - ranks, does not veto" label is load-bearing in BOTH
  directions: a low score can't kill a pick, a high score is NOT a green
  light. Confidence language in briefs dampened accordingly — a 60 is not
  claimed to be meaningfully better than a 40 inside the gated pool.
- The DGX anecdote (26 -> sideways) is downgraded from "score working" to
  "one good anecdote."
- The real test remains the pre-registered forward one: nightly scan now
  stamps readiness on every candidate (commit 14e4f34); Friday reviews grade
  score-vs-subsequent-move across regimes on hundreds of names.
- Extension idea if the forward test also shows nothing on the composite:
  test components separately — the runners' modal at-pick signature was
  momentum-turn + RS-extreme (PBF/DK/CORT), not the squeeze.

## Same-day snapshot: current readiness of the 19 skipped runners (7/31 close)

Still loaded: ECO 88 (0.7% from trigger, volume extreme, energy wind),
EAT 80 (at high, bands wide — hot not coiled), STGW 78, GKOS 70 (TTM squeeze
ON, 4th pctile, re-coiling 10% under high), PGEN 68, SNOW 66 (TTM squeeze ON).
Spent: CORT 40, GM 36, ETON 20, TXG 18, BJRI 10.
Action taken: GKOS/SNOW/ECO added to the Monday 8/3 gate check (fresh-pass
entries only; don't-chase stands). Monday 8:50 fill routine re-scores the
three staged options picks at the open (baselines GE 60 / AAPL-put 32 /
INTC-put 20).
