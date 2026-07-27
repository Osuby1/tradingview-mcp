# Fresh-Ignition "A" grade backtest — results

Run 2026-07-26 against `research/fresh-ignition-preregistration.md` (committed
first). 1,136 usable names of the scanner's own 1,200-name universe, the
scanner's own rules replayed daily, 2021–2025. **1,512 A-grade Fresh Ignition
entries.** All numbers are vs SPY over each trade's own window, 10 bp costs.

---

## Verdict: the middle band fires — "looks good recently" was recency

Pre-registered pass bar: mean excess ≥ +2.0 pt AND median > 0 AND both
alphabetical halves agree.

| Omar's rule (buy A-grade Fresh Ignition, sell on Cooling) | |
|---|---|
| Entries | 1,512 |
| **Mean excess vs SPY** | **−1.31 pt** (odd half −2.10, even −0.63) |
| Median excess | +2.29 pt |
| Trades beating SPY | **69.7%** |
| Average hold | 58 days |

Mean fails the bar by a wide margin; both halves are negative. The
pre-committed conclusion applies: *the A-grade Fresh Ignition cohort is
ordinary once five years are counted. No change to anything.*

## Why it LOOKED strong — the shape that fooled the eye

Seven of ten of these trades beat the market, and the median trade wins by
+2.3 points. Watching recent recommendations, that is exactly what one sees:
mostly winners. The mean is negative anyway because of what the rule does at
the two ends:

- **It sells winners the moment they get hot.** "Cooling" means RSI above 70
  or a 30% run — the exit fires ON strength, harvesting many small wins.
  This tripped the pre-registered tripwire: Omar's exit underperformed a
  plain 60-day hold by more than a point (−1.31 vs −0.15), the same
  sell-the-tail defect as the retired 2:1 target, at a different address.
- **It holds losers with no floor.** A name that never "cools" — because it
  drifts down instead of up — sits in the book up to 250 days. The rare big
  losers erase all the small wins. High hit rate, negative mean: the
  seductive combination.

## The controls — each claim tested

| Cohort | n | Fwd-60d mean vs SPY | Beat SPY |
|---|---|---|---|
| A-grade Fresh Ignition (plain 60d hold) | 1,512 | −0.15 pt | 45.8% |
| B-grade Fresh Ignition | 5,656 | −0.92 pt | 44.3% |
| A+ Fresh Ignition | 10 | +1.30 pt | too rare to matter |
| **COOLING names** | 16,261 | **+0.39 pt** | 44.6% |
| **COILED names** | 31,546 | **−0.63 pt** | 45.0% |

- The A-vs-B ordering points the right way but is small — the grade carries
  a whisper, not a signal.
- **"Cooling = dismiss" is backwards:** Cooling names went on to do mildly
  BETTER than the fresh A-grades. Stocks that just ran hard keep drifting up
  slightly — the same momentum-continuation reality that killed the 2:1
  target and the rotation radar's inverted ladder.
- **"Coiled = dismiss" roughly holds:** mildly negative, nothing there.
- Exit alternatives on the same entries: exit-on-any-status-loss lasts 2 days
  (LEADER status is that fleeting) and earns nothing; the current live exit
  (5% stop + ratchet) also fails to make this cohort beat SPY (−0.66).

## Honest caveats

Survivor universe (today's list — flatters every cohort; the failure is
conservative). Weekly indicators lag up to 4 days (declared; applied
identically everywhere). One run, no changes after registration.

## What this changes

1. **Nothing goes live and nothing is promoted.** The origination scanner
   remains a watchlist feeder; its tabs and grades are labels, not signals —
   now measured at the tab × grade level, not just the logbook level.
2. **The sell-on-Cooling idea is retired before it cost money** — it is the
   2:1 target wearing different clothes, and it also removes the downside
   floor. If any exit governs, it stays the measured one: stop + ratchet.
3. The one whisper worth remembering: A beat B by ~0.8 pt forward — too weak
   to trade, consistent with the grade ordering being real but tiny.
