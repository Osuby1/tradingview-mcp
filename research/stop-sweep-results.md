# Initial-stop sweep — results

Run 2026-07-26 against `research/stop-sweep-preregistration.md` (committed
first). Same 12,230 entries as the exit-redesign study, 2021–2025, live hybrid
rule (static stop → 20% ratchet once earned), 120-day cap, **gap-through fills
at the open**, every signal **sized by Omar's real formula:
notional = min($100k, $5k / stop-distance)**. One run, no grid changes.

---

## Headline table — dollars per signal under real sizing

| Stop | Mean $ | Median $ | Hit | Mean worst DD $ | Stopped | Mean days |
|---|---|---|---|---|---|---|
| 2% | +836 | −2,100 | 12.3% | −2,045 | 86.9% | 23 |
| 3% | +1,220 | −3,100 | 17.3% | −2,839 | 81.3% | 31 |
| 4% | +1,503 | −4,100 | 21.9% | −3,567 | 75.8% | 39 |
| **5%** | **+1,709** | −5,100 | 26.1% | −4,268 | 70.4% | 46 |
| 6% | +1,621 | −5,083 | 30.2% | −4,075 | 65.2% | 52 |
| 8% | +1,493 | −5,062 | 37.5% | −3,764 | 55.0% | 62 |
| 10% | +1,428 | −3,284 | 43.4% | −3,473 | 45.3% | 71 |
| 12% | +1,352 | −688 | 47.7% | −3,194 | 36.1% | 79 |
| 15% | +1,184 | +254 | 51.4% | −2,844 | 24.1% | 86 |
| 20% | +990 | +495 | 54.2% | −2,326 | 3.9% | 94 |
| **NOSTOP** (ratchet-only, $100k) | **+4,042** | +2,076 | 54.4% | **−9,348** | 0% | 94 |
| CE1x (pre-7/25 live stop) | +1,315 | −3,964 | 26.8% | −3,624 | 68.4% | 46 |

Pre-registered argmax stability: **NOSTOP wins the full sample AND both halves
of both splits** (odd/even names, 2021-23/2024-25). The dedup cut (3,773
non-overlapping signals) reproduces the ordering almost exactly.

## Three findings

### 1. The static-stop optimum is 5% — and it is pinned by the SIZING, not the market

For stops of 2–5%, $5k ÷ stop exceeds the $100k cap, so the position is $100k
regardless — and at constant notional, wider is strictly better (+$836 → +$1,709,
monotone). Above 5%, the formula shrinks the position faster than the wider
stop improves the trade, so dollars fall again. The peak sits **exactly at
risk ÷ cap = $5k / $100k = 5%** because that is the only point where the full
risk budget and the full notional budget deploy simultaneously.

That is a theorem about the sizing formula, confirmed empirically — the market
data merely fails to overturn it. By year the interior static peak wobbles
5–8% and inverts in 2022, so the "5" is structural, not a market constant.

### 2. On raw performance the curve still just wants looseness — 5th confirmation

Per-trade mean return rises monotonically from +0.94% (2% stop) to +4.14%
(no static stop). NOSTOP more than doubles the dollar expectancy of the best
static stop (+$4,042 vs +$1,709) — but it does so by risking ~4x more per
position (its mean worst drawdown is −$9,348, and it holds $100k with only the
20%-of-peak floor). It wins per SIGNAL by taking more risk per signal, which
Omar's $5k-per-trade contract and −$10k weekly breaker do not permit. It is
the right benchmark, not a usable rule.

Per dollar OF RISK, the ordering reverses: mean R falls monotonically from
0.47 (2%) to 0.20 (20%). Tight stops are the most risk-efficient and the most
psychologically brutal — 87% of them get stopped, median holding 23 days.

### 3. The old Chandelier stop loses to a flat 5% line

CE1x — the pre-7/25 live placement, median distance ~3–4% — made +$1,315 vs
+$1,709 for a plain 5% stop, with the same stop-out rate as 5% but a worse
median. Volatility-scaled placement at CE(1,2) settings is strictly dominated
on this sample by the dumb flat line that happens to match the sizing boundary.

## 2022, reported as promised

| Year | 2% | 5% | 20% | NOSTOP |
|---|---|---|---|---|
| 2022 mean $ | −889 | **−1,875** | −476 | −1,825 |

**No stop level made money in the bear year, and tighter was NOT safer** — 5%
was the worst static rule in 2022 (maximum whipsaw: wide enough to hold
through nothing, tight enough to catch every flush). The least-bad was the
loosest static (20%). The bear-year protection in this system remains where
every previous test located it: the entry gates halving the signal count, not
the stop.

## The psychological price of the correct stop — stated plainly

At the 5% optimum, the **median outcome is a full stop-out** (−$5,100) and only
26% of trades finish green. The entire expectancy is tails. Anyone running
this rule must expect to be wrong-feeling three trades out of four; tightening
to 2% to "lose less often" makes losing MORE frequent (88% stopped) and cuts
the dollars in half. The discomfort is load-bearing.

## Honest caveats

- Survivor universe, hand-picked names, overlapping signals (dedup cut agrees),
  slippage beyond the open unmodeled. Shared by all rules; comparisons mostly cancel.
- Re-entries are partially modeled: a stopped name that re-fires a fresh gated
  BUY re-enters the sample as a new signal.
- The grid did not test ATR-multiple stops other than CE1x, nor time stops.
- One run. The 5% peak's exact location is sizing-determined; the market
  evidence alone says only "looser is better, everywhere, again."

## What this changes

1. **For new plans (post-freeze, paper-first): initial stop = 5% below entry**
   (= the sizing boundary), replacing the CE-line placement, unless structure
   offers a level between 4–6%. Re-derive the boundary if the risk/cap
   parameters ever change: stop% = risk$ ÷ cap$.
2. **NOSTOP is the benchmark, not a rule** — it breaches the per-trade risk
   contract by ~4x.
3. **Open positions keep their registered stops** — widening a stop mid-trade
   adds risk the sizing never budgeted for.
4. Nothing live changes before 2026-08-31 (standing freeze); this goes through
   the paper book like the rest of the 7/25 exit rule.
