# Portfolio study (firehose + sizing) — pre-registration

Committed 2026-07-26, BEFORE any study code exists. Omar approved items 2+3 of
the repair plan: the scan fires ~50-90 signals a day and nothing has ever
measured what taking them EARNS AT THE ACCOUNT LEVEL under real constraints —
slots, capital, one position per name. Every prior number was per-signal
expectancy, which no account can actually collect. This is the test that
prices the firehose in dollars, and the first test of position sizing (Gap-1).

## The question

Run the satellite book the way it would really be run — N slots, capital
budget, signals competing for free slots — over 2021–2025. Does it beat
parking the same capital in SPY? Does slot-selection skill matter? Does
sizing method matter?

## Frozen design

**Entries:** the same frozen harvest as every study this week (12 sector
baskets, 2021–2025, gate stack unchanged, fresh gate-passing BUYs, entry at
the signal-day real close).

**Exit rule:** the intended forward rule — initial stop 5% below entry
(gap-through fills at the open), 20% close-based ratchet once 0.8 × highest
close clears the stop, 120-trading-day cap, 10 bp round trip. HONESTY NOTE,
declared: the 5% stop was itself chosen on this same 2021–2025 data
(stop-sweep, 7/26), so the absolute account numbers are partly in-sample to
that one choice; the SLOT and SIZING comparisons are unaffected (all configs
share the exit).

**Book mechanics:** one position per symbol at a time; no adds; no re-entry
while held; a signal is taken only if a slot AND budget are free that day;
committed capital = N × $100k, held as cash when not deployed (cash earns 0).
Daily mark-to-market equity curve from real closes.

**The grid (all 18 configs run, NONE added later):**
- Slots N: 4, 8, 16
- Slot selection when signals exceed free slots:
  FIFO (alphabetical — the deliberately skill-free baseline),
  MOST-LIQUID (highest avg dollar volume),
  LEAST-EXTENDED (smallest % above the 200-day)
- Sizing: FLAT ($100k per position) vs VOL-SCALED ($100k × 2.5% / ATR%,
  capped $50k–$150k, skipped if free budget < $25k)

**Primary read, declared now: N=8, FIFO, FLAT.** The no-skill default. All
other configs are sensitivity, reported in full, never promoted to headline
because they scored better.

**Benchmark:** SPY bought with the same committed capital on the first sim
day and held. Metrics per config: total $ P&L, CAGR on committed capital,
max drawdown of the equity curve, win rate, trades taken vs signals offered,
average exposure, per-year table (2022 always shown).

## Pre-committed conclusions

1. **Primary config total return < SPY's** → "The firehose adds nothing at
   the account level. The passive-core default stands; the satellite book is
   optionality priced as entertainment, and its capital allocation should be
   sized accordingly."
2. **Primary ≥ SPY but max drawdown > 1.5× SPY's** → "The satellite earns its
   return by taking materially more pain than the index — a leverage
   substitute, not an edge."
3. **Primary ≥ SPY with drawdown ≤ 1.5× SPY's** → "The account-level book
   clears the bar ON THIS SAMPLE — subject to the in-sample caveat above, and
   promotable only via the shadow lane like everything else."
4. **Selection rules:** if the spread between best and worst selection rule is
   < 10% of SPY's total return, the conclusion is "slot selection does not
   matter — take signals in arrival order and stop looking for picking skill
   here" (consistent with every scoring test this week).
5. **Sizing:** if |VOL-SCALED − FLAT| < 10% of SPY's total return at the
   primary config, "sizing method is second-order; the risk contract, not the
   formula, is the decision." Otherwise report which way and by how much.

## Biases, stated in advance

Survivor universe and hand-picked baskets (flatter the satellite, not SPY —
they make this test EASIER for the firehose, so conclusion 1, if it fires, is
conservative). The exit rule's in-sample tilt (above). No slippage beyond
gap-opens and 10 bp. One run, no config changes after this commit.
