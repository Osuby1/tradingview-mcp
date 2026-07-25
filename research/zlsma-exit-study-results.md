# ZLSMA scale-out study — semiconductors, 2025

Run 2026-07-25 against `research/zlsma-exit-preregistration.md`, committed before
the code existed. 386 gate-passing fresh BUY signals across 53 US semiconductor
and semi-equipment names, 1 Jan – 31 Dec 2025. Entries held constant (same gate
stack the live system runs); only the exit varies.

---

## Headline: there is no optimum distance

The sweep does not have a peak. It rises **monotonically** from 0% to 15% below
the ZLSMA and is still rising when it hits the edge of the search range:

| Distance below ZLSMA | Scale-out, no reload | With reload |
|---|---|---|
| 0.0% | +0.29% | +0.22% |
| 2.5% | +0.11% | +0.22% |
| 5.0% | +0.92% | +1.64% |
| 7.5% | +1.21% | +1.92% |
| 10.0% | +3.10% | +4.71% |
| 12.5% | +5.05% | +7.38% |
| **15.0%** | **+6.52%** | **+9.39%** |

A parameter that improves all the way to the boundary is not an optimum — it is
the arithmetic telling us the rule wants to be switched off. "Exit further and
further away" converges on "do not exit."

And the baselines confirm exactly that:

| Rule | Mean per signal |
|---|---|
| **A** — live rule (Chandelier stop + 2:1 target) | **+0.12%** |
| **B** — pure 21-day hold | +1.14% |
| **C** — pure 120-day hold, no management at all | **+16.40%** |

Doing nothing beat every managed rule tested, by a wide margin.

---

## The control that matters: none of it beat buying the sector

SOXX returned **+38.9%** in 2025 against the S&P's +16.6%. Measured over the
*same 120-day windows* as each signal:

| | Mean return | vs just owning SOXX |
|---|---|---|
| **Buy and hold SOXX** | **+16.95%** | — |
| Pure 120-day hold of our signals | +16.40% | **−0.55 pt** |
| ZLSMA scale-out at 14% (best in sweep) | +9.41% | **−7.54 pt** |
| Live rule (stop + 2:1) | +0.12% | **−16.83 pt** |

**Only 163 of 386 signals — 42% — beat simply owning the sector ETF.**

So the stock selection added nothing over buying SOXX, and every exit rule we
tested subtracted from it. The live rule subtracted almost seventeen points.

---

## My pre-registered bar was met, and it was the wrong bar

The registration said the ZLSMA rule must beat rule A by ≥1.5 pt on the held-out
half of both splits. It did, comfortably:

| Split | Trained on | Best x | Held-out result | vs rule A |
|---|---|---|---|---|
| Calendar | H1 2025 | 14.0% | +8.24% | **+7.64 pt** |
| Calendar (reload) | H1 2025 | 14.5% | +11.62% | **+11.02 pt** |
| By name | odd | 14.5% | +7.07% | **+6.96 pt** |
| By name (reload) | odd | 14.0% | +10.43% | **+10.32 pt** |

**That pass is hollow and I am not going to present it as a success.** The
mechanism is not "14% is the right distance." It is "any exit looser than the
current one does better, and none of them beat not exiting." Both chosen values
sit at the edge of the grid, which is the same monotonic story.

The design fault is mine: I set the bar against **rule A**, the current live
exit, when the honest comparison was against *doing nothing* and against *buying
the sector*. A bar measured off a bad baseline can be cleared while the idea
underneath is still wrong.

---

## What holding actually costs

"Just hold" is not free, and the mean return hides it:

- Mean worst drawdown while holding: **−15.79%**
- Worst single drawdown: **−60.51%**

So the honest description of rule C is: it matched the sector ETF's return while
taking single-name risk, including one position that went 60% against it. That is
worse than the ETF on a risk-adjusted basis even though the mean looks similar.

---

## The caveat that limits all of this

**2025 semiconductors was one of the strongest sector trends available.** In a
year like that, "never sell" wins by construction and every exit rule looks
destructive. This study says nothing about how a ZLSMA exit behaves in a choppy
or falling market — which is precisely where an exit rule earns its keep.

A trend-following exit tested only in a trend is a test the rule cannot fail on
its merits, and cannot pass on them either.

---

## Answers to what was asked

**"What is the optimum distance below the ZLSMA to cut?"**
There isn't one in this data. The curve runs to the boundary. Cutting at any
distance cost money relative to not cutting.

**"Take 50% off on the dip below, then reload or exit?"**
Reloading beat not reloading at every distance tested (+9.39% vs +6.52% at 15%),
which is consistent with the same story — the scale-out was premature, and
putting the position back on recovered part of what it cost.

**"Do I have a better chance of making money this way?"**
On this sample: better than the current stop-and-target rule, yes, by a wide
margin. Better than simply buying SOXX and leaving it alone, no.

---

## What this does and does not change

- **Nothing live changes.** Rule freeze through 2026-08-31.
- It is the second independent finding that the current exit rule is the most
  damaging component in the system — −16.83 pt here, −1.18 pt in the Jan–Jun 2026
  replay.
- The obvious next question is not "which exit distance" but **"does the stock
  selection beat the sector ETF at all?"** On this sample it did not, and that is
  a bigger question than the exit.
- Before any of this informs real money it needs testing in a **flat or falling**
  market. Everything above is one sector in one very good year.
