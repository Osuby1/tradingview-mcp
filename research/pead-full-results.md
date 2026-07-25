# Earnings-surprise signal — full re-test results

Run 2026-07-25 against `research/pead-full-preregistration.md`, committed before
the re-run. 103 mid-cap names, **2,957 earnings events**, 2011–2026, surprise
measured from EDGAR filing dates with no look-ahead, drift from the day after
filing. Top-quintile SUE cohort, n=592.

---

## Verdict: fails all four requirements

Primary horizon, declared in advance as 20 trading days:

| # | Requirement | Needed | Actual | |
|---|---|---|---|---|
| 1 | Mean excess vs SPY | ≥ +1.00 pt | **−0.13 pt** | **FAIL** |
| 2 | Median excess | > 0 | **−0.68 pt** | **FAIL** |
| 3 | Hit rate | > 52% | **46.5%** | **FAIL** |
| 4 | Mean after deleting top 5% | > 0 | **−1.45 pt** | **FAIL** |

The pre-committed conclusion for "any of 1–3 fails":

> *"The earnings-surprise signal does not survive the standard applied to
> everything else. The system has no measured edge anywhere, and the honest
> answer is a passive core."*

That stands.

**Same lottery shape as everything else.** The top 5% of events contribute
+1.24 pt against an overall mean of −0.13 pt. Strip them and it is −1.45 pt.
This is the identical pattern that killed stock picking this morning.

---

## The 60-day number looks better and is not signal

| Cohort | 20d excess vs SPY | 60d excess vs SPY |
|---|---|---|
| Low-SUE (Q1) | −1.49 pt | **+3.45 pt** |
| High-SUE (Q5) | −0.13 pt | **+3.74 pt** |
| **Spread** | **+1.36 pt** | **+0.30 pt** |

At 60 days the high-SUE cohort beats SPY by 3.74 points — but so does the
**low**-SUE cohort, by 3.45. Both quintiles beat the index by roughly the same
amount because mid-caps beat SPY over that stretch. **That is beta, not
surprise.** The spread the signal actually produces is +0.30 pt, and the rank
correlation at 60 days is +0.000.

The genuine signal is the 20-day spread of +1.36 pt between the best and worst
surprises. Real, but it does not translate into beating the index, because the
whole quintile is still slightly behind SPY.

---

## Every year, nothing dropped

| Year | n | Mean | Median | Hit rate |
|---|---|---|---|---|
| 2011 | 16 | +4.92 | +1.87 | 62.5% |
| 2012 | 43 | −1.66 | −5.65 | 46.5% |
| 2013 | 30 | +0.66 | +0.35 | 50.0% |
| 2014 | 43 | −1.28 | −4.17 | 41.9% |
| 2015 | 34 | −1.94 | −4.91 | 32.4% |
| 2016 | 36 | −1.46 | −4.57 | 41.7% |
| 2017 | 42 | +0.69 | +1.61 | 52.4% |
| 2018 | 61 | +0.44 | −0.64 | 47.5% |
| 2019 | 32 | −1.94 | −3.31 | 43.8% |
| 2020 | 36 | −4.01 | −6.06 | 25.0% |
| 2021 | 68 | +1.18 | +0.41 | 51.5% |
| 2022 | 32 | −1.51 | −1.10 | 37.5% |
| 2023 | 34 | +0.36 | −2.42 | 41.2% |
| 2024 | 37 | **+3.95** | +3.44 | 67.6% |
| 2025 | 48 | +0.57 | +1.45 | 54.2% |

Eight of fifteen years have a negative mean. Nine have a negative median. The
two strong years — 2011 (n=16) and 2024 — are not enough to carry it.

---

## The result is not stable between runs

The 7/22 run of this same test reported IC **+0.051** and a 20-day high-SUE
excess of **+0.49%**. Today, three days later on essentially the same data:
IC **+0.041**, excess **−0.13%**.

Three additional events out of ~2,955 cannot move a quintile mean by 0.6 pt. The
difference comes from price-data revisions and the sensitivity of a
quintile-boundary cohort to small changes. **A signal that gives a materially
different answer on two runs three days apart is not robust enough to trade**,
independent of what any single run says.

That instability is itself a finding, and it is why the 7/22 "20 days works"
reading should not have been carried forward as confidently as it was.

---

## The caveat that survives — stated in advance

This is the **free** construction: surprise measured as this quarter's EPS versus
the same quarter a year ago, standardised by the company's own earnings
volatility. It is not "beat versus analyst expectations."

Real PEAD research uses analyst estimates. Those cost roughly $59/month for
point-in-time data. **This result does not rule out the paid version working** —
the published effect is built on analyst surprise, and the seasonal random walk
is a known-crude proxy.

What it does rule out is getting PEAD for free from SEC filings in this universe.

Also unchanged: survivor universe, no transaction costs, overlapping windows.
All three flatter the signal, and it still failed.

---

## Where this leaves the whole system

Every component has now been measured against a pre-registered bar:

| Component | Result |
|---|---|
| Origination score | No predictive power |
| BUY SCORE | No predictive power |
| Momentum | IC ≈ 0 |
| Gate stack as a selector | Failed both criteria |
| Exit rules | Actively harmful |
| Stock picking within sectors | Adds nothing, tail-driven |
| Rotation radar | States inverted |
| **Earnings surprise (free)** | **Fails all four** |

Two things survived measurement:

1. **Detection** — 79% of 50%+ movers flagged before their peak.
2. **Risk control** — flat while sectors fell in 2022; drawdowns cut by ~20%.

Neither is an edge. Both are useful.

The honest position is the one pre-committed above: **no measured edge anywhere,
and a passive core is the defensible default** — with the detector as a watchlist
generator and the gate stack as a risk overlay, described as exactly that.
