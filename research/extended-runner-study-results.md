# Extended-runner study — RESULTS (2026-07-31)

This is the pre-registered study from
`research/extended-runner-options-study-preregistration.md`, run exactly as
written, thresholds untouched. The question: when our own radar stamps a pick
"EXTENDED — don't chase" (up 25% or more from the price where we first
recommended it), does the stock keep paying — and would buying a
rules-compliant call option at that moment have made money?

## The verdict, stated bluntly

**Both layers: INSUFFICIENT DATA — the don't-chase rule STANDS.** The
pre-registration said in advance: fewer than 15 flags means the verdict is
automatically "insufficient data" no matter what the numbers look like. We
found exactly 7 flags. That is half the required sample, so no conclusion may
be drawn in either direction, and the PBF/CORT stories stay open until a real
sample exists. The rule that prompted this study — don't chase — remains in
force unchanged.

Two things the small sample DID surface, reported honestly but carrying no
verdict weight:

1. **The early stock numbers lean against chasing, not for it.** Only 2 of the
   7 flags are old enough to have a full 10-session look. Their median
   10-session return was about -2.7% while the market (SPY) lost about -1.3%
   over the same windows — the chased names did worse than the market, and
   only 1 of the 2 was positive at all (50% hit rate; the bar was 55%). Every
   single flag also took a quick hit after flagging: worst drawdowns ranged
   from about -3% (CAKE) to -13% (CDNA) within days.

2. **The PBF lottery ticket that started this study was never a legal trade.**
   PBF's +15% earnings-day moonshot happened on 2026-07-30 — and 7/30 sits
   inside the option's hold window, so the overlay's own earnings blackout
   blocks the trade. Same for 4 more of the 7 flags (BJRI, CDNA, DK, ETON all
   had earnings inside the window). The "rule-breaking call that doubled" was
   rule-breaking twice over: chasing AND holding through earnings. Of the 2
   flags a compliant option could actually be bought on, the synthetic marks
   so far are CAKE roughly flat and CORT about -11%.

## Every flag (no exclusions — this is the whole sample)

Returns are total return from the first close at/after the flag; SPY over the
identical windows in parentheses. "Worst hit" is the deepest intraday drawdown
from the flag close within 21 sessions (or however many exist so far).
Blank = window hasn't finished yet (most flags are days old).

| Ticker | Reco date @ price | Flag date @ close (gain at flag) | Radar emitted | +5 sess (SPY) | +10 sess (SPY) | +21 sess | Worst hit | Option sim (SYNTHETIC) |
|---|---|---|---|---|---|---|---|---|
| PBF  | 07-02 @ 48.04 | 07-14 @ 60.89 (+27%) | 07-23 | +8.5% (-0.5%) | +0.2% (-1.5%) | — | -7% in 13 sess | **BLOCKED** — earnings 07-30 in window |
| CDNA | 07-07 @ 29.06 | 07-16 @ 40.34 (+39%) | 07-23 | -6.8% (-1.7%) | -5.6% (-1.2%) | — | -13% in 11 sess | **BLOCKED** — earnings 07-30 in window |
| DK   | 07-02 @ 53.14 | 07-21 @ 67.19 (+26%) | 07-30 | -6.5% (-1.0%) | — | — | -11% in 8 sess | **BLOCKED** — earnings 08-05 in window |
| CAKE | 07-07 @ 76.89 | 07-29 @ 101.14 (+32%) | 07-29 | — | — | — | -3% in 2 sess | Sep 95 call @ 12.50, now ~12.51 (**+0.1%**, open 2 sess) |
| ETON | 07-07 @ 38.02 | 07-29 @ 48.13 (+27%) | 07-29 | — | — | — | -4% in 2 sess | **BLOCKED** — earnings 08-06 in window |
| CORT | 07-07 @ 91.61 | 07-30 @ 118.32 (+29%) | 07-30 | — | — | — | -6% in 1 sess | Sep 110 call @ 23.12, now ~20.49 (**-11.4%**, open 1 sess) |
| BJRI | 07-07 @ 59.19 | 07-30 @ 74.26 (+25%) | 07-30 | — | — | — | -9% in 1 sess | **BLOCKED** — earnings 07-30 (after that close) in window |

Flag dates are the replay of the radar's own rule (first daily close 25%+
above the reco price) run from each pick's reco date — this backdates PBF,
CDNA and DK to before the radar existed (it launched 07-23) or before it
re-noticed them, which is the unbiased way to date the transitions. The
radar's actual notification dates are shown alongside.

## How the sample was built (no cherry-picking)

All 391 picks the radar has ever watched — every OPEN row across every dated
recommendations log, every long call in the calls ledger, every gate-passing
universe candidate — were replayed through the radar's exact extended rule
(close at 25%+ above reco price) from each pick's reco date using daily bars.
Exactly 7 ever crossed. The 7 match the radar's own state file one for one,
so nothing was emitted that the replay missed, and nothing was quietly
dropped.

## Option simulation fine print (all labeled, none of it real quotes)

Call nearest a 0.65 delta, first monthly expiry 45–90 days out (all landed on
Sep 18), priced with Black-Scholes from `scripts/options_analysis.py` using a
SYNTHETIC volatility = 1.1 x the larger of 20- and 60-day realized volatility.
Model fills at daily closes, no bid-ask spread or slippage — real fills would
be worse. Exits per live overlay policy A: +100% take, -50% cut, 21 days to
expiry, 21-session cap. Neither tradeable position has hit an exit yet; their
numbers are marks, not banked results.

## Honest limitations

- 7 flags, most under a week old. Five of seven forward windows are unfinished.
- The 2 completed 10-session windows landed in a falling tape (SPY negative in
  every measured window), which flatters nothing but also proves nothing.
- Synthetic option pricing at constant volatility understates what earnings-
  and squeeze-driven IV swings would do to real premiums, in both directions.
- Earnings blackout treated a report dated the entry day (BJRI, after the
  close) as inside the hold window — BJRI gapped -9% the next session, so the
  block was the right call, but the convention is noted.

## What happens next (pre-registered action mapping)

Insufficient data = the don't-chase rule stands and nothing changes. No
"extension continuation" overlay entry gets designed. Re-run this exact study
— same thresholds, same file — once the radar has emitted 15 or more flags and
their 10-session windows have matured; the CAKE and CORT synthetic positions
keep running inside `research/extended-runner-study-results.json` until their
exits trigger. The PBF/CORT anecdotes may not be cited as evidence for
chasing until that re-run passes both pre-registered bars.

Raw numbers: `research/extended-runner-study-results.json`.
