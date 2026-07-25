# Does stock picking beat buying the sector? — results

Run 2026-07-25 against `research/sector-vs-stockpicking-preregistration.md`,
committed to git before the code existed. **12,230 gate-passing BUY signals**,
12 sectors, 244 stocks, 2021–2025. Pure hold, no exit rule. Fills at real closes.

---

## Verdict: **selection adds nothing** — the pre-registered middle band

Primary horizon, declared in advance as 60 trading days:

| | |
|---|---|
| Stock picks | **+2.90%** |
| Their sector ETF, same days, same holding period | **+2.19%** |
| **Excess** | **+0.71 pt** |
| **Hit rate** | **48.9%** |

The registration set three bands. This lands in the middle one:

> *Mean excess between −2 and +2pt, hit rate 45–55%* → **"Selection adds nothing.
> The sector is doing the work — buy the ETF instead and save the single-name
> risk."**

That is the conclusion, and it was written before the number was known.

Note the shape: the mean is **positive** while the hit rate is **below 50%** and
the **median is −0.28 pt**. More than half of all picks did worse than simply
owning their sector. The positive average comes from a small number of large
winners, not from being right more often.

---

## All horizons (context — 60d was pre-declared as the headline)

| Horizon | Excess | Hit rate | Stock | Sector ETF |
|---|---|---|---|---|
| 21 days | +0.24 pt | 49.8% | +1.28% | +1.03% |
| **60 days** | **+0.71 pt** | **48.9%** | **+2.90%** | **+2.19%** |
| 120 days | +1.50 pt | 49.7% | +5.89% | +4.39% |

The excess grows with holding period while the hit rate stays pinned near 50% at
every horizon. That is the same tail story: holding longer captures more of the
few big winners, it does not make the picks more often right.

---

## Every sector, including the bad ones

| Sector | n | Excess | Hit rate |
|---|---|---|---|
| Biotech | 760 | **+4.45 pt** | 53.6% |
| Retail | 853 | **+3.36 pt** | 55.6% |
| Materials | 1036 | +0.88 pt | 47.7% |
| Healthcare | 1127 | +0.70 pt | 50.5% |
| Energy | 987 | +0.51 pt | 44.0% |
| Financials | 1065 | +0.46 pt | 53.9% |
| Semiconductors | 1000 | +0.26 pt | 46.4% |
| Discretionary | 1136 | +0.11 pt | 50.7% |
| Homebuilders | 1002 | +0.03 pt | 46.8% |
| Industrials | 1169 | **−0.11 pt** | 44.4% |
| Software | 987 | **−0.22 pt** | 47.4% |
| Utilities | 1108 | **−0.30 pt** | 48.0% |

Ten of twelve sectors sit between −0.30 and +0.88. Two — Biotech and Retail —
carry almost the whole result.

---

## Every year, including 2022

| Year | n | Excess | Hit rate | Stock | Sector ETF |
|---|---|---|---|---|---|
| 2021 | 2702 | **+2.56 pt** | 55.8% | +5.53% | +2.97% |
| 2022 | 1438 | **+1.30 pt** | 48.4% | +0.06% | −1.24% |
| 2023 | 2493 | −0.07 pt | 46.2% | +4.21% | +4.28% |
| 2024 | 3180 | −0.25 pt | 48.0% | +1.67% | +1.92% |
| 2025 | 2417 | +0.36 pt | 45.5% | +1.91% | +1.56% |

**2021 is the only year that would have cleared the bar.** It is also the only
year with a hit rate above 55%. Since then the edge has been flat or slightly
negative three years out of four.

**2022 is the one genuinely encouraging line.** In the bear market the picks were
roughly flat (+0.06%) while their sectors fell (−1.24%). That is the gate stack
behaving exactly as a risk control should — the first evidence for it from a
falling market, which nothing in this repo had before today.

---

## Robustness — disclosure, not a new headline

The headline stays **+0.71 pt**. These cuts are reported because hiding them
would be the force-fitting Omar asked me to avoid.

| Cut | n | Mean | Median | Hit rate |
|---|---|---|---|---|
| **Headline (all)** | 12,230 | **+0.71 pt** | −0.28 pt | 48.9% |
| Excluding Biotech + Retail | 10,617 | +0.23 pt | −0.45 pt | 48.0% |
| Last three years only (2023–25) | 8,090 | **−0.01 pt** | −0.71 pt | 46.7% |
| 2021 alone | 2,702 | +2.56 pt | +1.29 pt | 55.8% |

And the concentration is extreme:

- The **top 5% of signals account for 241% of the total excess return.**
- Remove them and the mean is **−1.05 pt**.

So the entire positive result rests on roughly 600 trades out of 12,230. That is
not a robust edge; it is a lottery-ticket distribution that happens to have a
positive expectation on this sample.

---

## Which way the biases ran

All three, stated in advance, favour stock picking:

1. **Survivorship** — the baskets contain companies that still exist and are
   still liquid. The ones that went to zero are absent. The ETF returns are real
   and include their own losers and turnover.
2. **I chose the names**, knowing which are well-known today.
3. **No trading costs**, against a strategy that trades vastly more than buying
   one ETF and holding it.

With all three tilted in its favour, stock picking produced +0.71 pt at a 48.9%
hit rate, a negative median, and nothing at all over the last three years.

---

## What it means

**Buying the sector ETF was as good as picking stocks inside it**, for far less
work, far less single-name risk, and far fewer transactions. Once realistic costs
are applied, the +0.71 pt almost certainly disappears.

**One real thing did show up: 2022.** The picks held flat while their sectors
fell. That is a defensive property, and it is consistent with every other
measurement this week saying the gate stack is a risk control rather than a
selector. It is the first evidence of it from a down market.

**The edge, such as it was, lived in 2021 and has not been seen since.**

## What this does NOT answer

Whether the *sector choice* is any good. This test always compares a stock with
its own sector, so it says nothing about picking which sector to be in. The
rotation radar remains ungraded, and it is now the single most important
unmeasured component — because if the sector call is where the value is, this
result says buy the ETF and stop there.
