# Rotation radar test — results

Run 2026-07-25 against `research/rotation-radar-preregistration.md`, committed
before the code existed. 29 sector ETFs, 2021–2025, weekly sampling, **7,279
observations**. The radar's live formula and thresholds imported unchanged.

Reconstruction validated against the live 2026-07-24 radar first: median accel
error **0.88 pt**, state match **27/30 = 90%**.

---

## Verdict: the radar does not predict — and its states run backwards

Primary horizon, declared in advance as 60 trading days:

| State | n | Forward return | vs SPY | Beat SPY |
|---|---|---|---|---|
| **IGNITING** | 700 | **+1.14%** | **−1.12 pt** | 42.3% |
| WATCH | 1,062 | +1.42% | −0.56 pt | 45.7% |
| NEUTRAL | 4,987 | +3.00% | −0.18 pt | 46.2% |
| **ROLLING** | 530 | **+4.51%** | **+0.25 pt** | 45.5% |

**That ladder is perfectly inverted.** The four states line up in exactly the
wrong order, monotonically. The sectors the radar flags as igniting did worst;
the ones it flags as rolling over did best.

- **IGNITING minus ROLLING: −3.37 pt**
- **IGNITING minus just owning all 29 sectors equally: −1.56 pt**

By the pre-registered bands, IGNITING vs SPY at −1.12 pt sits in the middle:

> *"The radar does not predict. It describes what has already moved. Stop using
> it to allocate."*

But it sits at the pessimistic edge of that band, and the ROLLING comparison
actively contradicts the radar's own logic rather than merely failing to support
it.

---

## The correlation is negative

Rank correlation between acceleration and forward return, across sectors:

| Horizon | accel | plain 1-month momentum |
|---|---|---|
| 21 days | **+0.033** | +0.010 |
| 60 days | **−0.045** | −0.063 |
| 120 days | **−0.080** | −0.061 |

Higher acceleration predicted *slightly lower* forward returns at 60 and 120
days. At 3–6 months this is mean reversion, not momentum.

**The control matters:** plain 1-month momentum scores about the same, slightly
worse. So the acceleration formula is not the problem — it is marginally better
than raw momentum. **The premise is the problem.** Buying what has just
accelerated does not work at these horizons.

The only positive reading anywhere is **+0.033 at 21 days**, which is tiny and
should not be built on. It does hint that whatever effect exists is short-lived
and has inverted by two months.

---

## Every year, including the one that flatters it

| Year | n | IGNITING return | vs SPY |
|---|---|---|---|
| 2021 | 96 | −4.04% | **−7.58 pt** |
| 2022 | 214 | −2.73% | +0.63 pt |
| 2023 | 174 | +2.06% | −2.61 pt |
| 2024 | 90 | −0.48% | −3.71 pt |
| **2025** | 126 | **+11.57%** | **+4.72 pt** |

**2025 was excellent. The four years before it were not.**

This is worth sitting with, because it explains how the radar earned its
reputation. The most recent year is the one you have direct experience of, and in
that year it worked well. Across five years, four were negative or flat.

---

## What this means

**The rotation radar should not be used to decide where to put money at a 2–6
month horizon.** On this evidence it is a lagging description of what has already
moved, and at 60+ days what has already moved tends to give some back.

Combined with the previous test, the picture is now:

- Picking stocks inside a sector: **adds nothing** (+0.71 pt, negative median)
- Picking which sector to be in: **adds nothing, and points the wrong way**

So the "buy the sector instead" conclusion from the last test does not rescue the
system — because the sector call itself does not predict either.

---

## The honest caveats

- **Weekly sampling still overlaps.** A 60-day forward window sampled every 5
  days means each observation shares most of its window with its neighbours. The
  effective sample is far smaller than 7,279 and the confidence intervals are
  correspondingly wide.
- **Five years is one broad cycle.** Sector momentum is documented to work in
  some regimes; this covers a specific and unusual stretch.
- **The states are unbalanced** — only 700 IGNITING observations against 4,987
  NEUTRAL, so the IGNITING estimate is the least precise of the four.
- **This tests allocation, not alerting.** The radar may still be useful as a
  *notice board* — "energy is moving, go look" — even though allocating to it at
  60 days lost money. That is a different claim and is not tested here.

---

## What I would not conclude

That the radar is useless as a *monitor*. It flagged Energy and China internet
before Friday's move, and drawing attention is not the same as predicting excess
return. The finding is narrower and specific: **do not size positions off the
state, and do not treat IGNITING as a buy signal at a multi-month horizon.**
