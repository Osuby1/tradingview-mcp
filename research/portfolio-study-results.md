# Portfolio study (firehose + sizing) — results

Run 2026-07-26 against `research/portfolio-study-preregistration.md` (committed
first). 12,230 signals, 1,261 trading days, 18 configs, entries/gates/exits as
frozen. Benchmark: SPY bought with the same committed capital and held.

---

## Verdict: pre-committed conclusion 1 fires

| | Primary book (N8 / FIFO / FLAT, $800k) | SPY, same $800k |
|---|---|---|
| Total return 2021–2025 | **+66.8%** ($1.334M) | **+88.2%** |
| CAGR | +10.8% | ~+13.4% |
| Max drawdown | **−11.7%** | −25.4% |
| 2022 (bear year) | **+5.9%** | ~−19% |
| Win rate | 27.5% | — |

Every one of the 18 configs underperformed SPY on total return (best:
N4/EXT/FLAT at +82.4%, still short). The pre-committed conclusion, verbatim:

> *The firehose adds nothing at the account level. The passive-core default
> stands; the satellite book is optionality priced as entertainment, and its
> capital allocation should be sized accordingly.*

With the survivor-universe bias flattering the satellite and not SPY, this is
the conservative direction: reality would be worse.

## The honest full picture: it's a defensive vehicle, not an engine

The book earned two-thirds of SPY's return with **less than half the pain**
(−11.7% vs −25.4% max drawdown) and was **positive in 2022** (+5.9% while SPY
fell 19%) — the entry gates halved the signal flow, the 5% stops cut losers,
and the cash buffer did the rest. Return over max-drawdown: 5.7 vs SPY's 3.5.
That is now the FOURTH independent account of the same identity: this system
is a risk-management machine, not an alpha machine. Anyone wanting
SPY-or-better returns should own SPY; anyone wanting equity exposure with
half the drawdown has, on this sample, a measured instrument.

## The capacity finding nobody had measured

At N=8 slots the book could take **209 of 11,498 offered signals — 1.8%**.
Every per-signal statistic of the past week described a fantasy account that
takes everything; a real account samples the firehose at 2% and its results
are dominated by WHICH 2% arrive when slots happen to be free. This is why
per-signal expectancy (+$1,709) never compounds into index-beating returns.

## Slot selection: no skill found — the blind rule won the primary

| N=8 | Total | | N=4 | Total | | N=16 | Total |
|---|---|---|---|---|---|---|---|
| FIFO (alphabetical) | **+66.8%** | | EXT | **+82.4%** | | LIQ | **+64.0%** |
| LIQ | +49.3% | | LIQ/FIFO | +67/+55% | | FIFO | +54.3% |
| EXT | +40.3% | | — | | | EXT | +41.7% |

The spread between rules is large (>26 pt at N=8) but the ORDERING flips at
every slot count — least-extended is best at N=4 and worst at N=8; liquidity
is worst at N=8 and best at N=16. No rule wins consistently, and the
deliberately skill-free alphabetical baseline won the pre-registered primary.
Consistent with every scoring test this week: there is no measurable
picking skill here, only variance. Take signals in arrival order.

## Sizing (Gap-1): second-order, as the band predicted

FLAT +66.8% vs VOL-SCALED +59.7% at the primary config — a 7.1 pt gap, below
the pre-registered 10%-of-SPY threshold. Conclusion 5 fires: **sizing formula
is second-order; the risk contract (how much per trade, how much total heat)
is the decision that matters, not the scaling math.** Vol-scaling did cut
drawdown at N=4 (−14.4% vs −22.8%) — worth remembering if a small-slot book
is ever run — but it is not a return lever.

## Caveats

Survivor universe (flatters the book — strengthens the verdict). The 5% stop
was tuned on this same data (declared in advance); slot/sizing comparisons
are unaffected. Cash earns 0% — a real book would hold T-bills, adding
roughly +15-20 pt over five years at 2021-25 rates on ~30% average idle cash;
that narrows but does not close the SPY gap, and helps every config equally.
One run, no config changes.

## What this changes

1. **The passive-core question is now priced:** the scan-driven satellite,
   run realistically, returns SPY-minus-21-points with half the drawdown.
   Core capital belongs in the index; the satellite's honest pitch is
   drawdown control and 2022-style resilience, never outperformance.
2. **Stop optimizing slot selection and scoring.** Third strike: no picking
   skill exists at any layer measured. Arrival order is fine.
3. **Sizing debates end:** enforce the risk contract; the formula is noise.
4. Nothing live changes (freeze through 8/31); this informs allocation, which
   is Omar's call, not a pipeline rule.
