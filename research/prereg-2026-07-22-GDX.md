# Pre-registered trade call: GDX long

**Registered:** 2026-07-22, ~2:20pm CT (intraday, before entry)
**Approved by Omar:** yes, 2026-07-22 ("yes GDX tomorrow")
**Account state at registration:** FLAT (confirmed by Omar)
**Status: VETOED 2026-07-22 ~2:50pm CT. DO NOT ENTER.**

> ## VETO - HQ Swing v1 regime filter FAILS, decisively
>
> Omar asked that HQ Swing v1 be consulted. It kills this trade. Measured off the
> live GDX chart (300 daily bars, candles):
>
> | Regime test | Value | Verdict |
> |---|---|---|
> | Price vs 200-day | 76.57 vs **87.54** = **-12.5%** | **DEEP-FAIL** |
> | 200-day rising? | 87.54 vs 87.22 (20d ago) | rising, but barely |
> | Price vs 50-day | 76.57 vs **81.20** | BELOW |
> | ADX(14) | **17.5** | below 20 = **no trend** |
> | +DI vs -DI | 30.9 vs 29.4 | effectively tied, no edge |
>
> Two independent kills:
>
> 1. **Omar's own regime ladder** says DEEP-FAIL = more than 10% below the
>    200-day = **watch only, no size**. GDX is 12.5% below. It is not a REPAIR
>    starter, it is a no-trade.
> 2. **ADX 17.5 with +DI and -DI tied** means there is no trend to ride. Memory
>    ([[hq-swing-regime-breakout]]) records the finding that the regime filter
>    (200SMA + ADX) IS the edge of this system - not the entry signal. This is
>    precisely the condition it exists to filter out.
>
> What this exposes: the O.G Chandelier flip and the ZLSMA check both PASSED.
> GDX looked like the best setup on the board. The Chandelier stack has no
> long-term regime awareness - it happily fires buy signals inside a
> 12%-below-200-day downtrend. **The regime filter is not redundant with the
> Chandelier gates; it catches a failure mode they are blind to.**
>
> Recommendation: run every O.G Chandelier candidate through the regime filter
> before sizing, not after. Today that would have been a one-line check.
>
> The rest of this document is preserved unedited as the pre-registered
> reasoning that turned out to be insufficient.

**Original status (superseded):** NOT YET ENTERED. Entry was planned for 2026-07-23.

This document exists so the call cannot be re-described after the outcome is
known. Per [[anti-sycophancy-validation-mandate]], every call is pre-registered
with its reasoning, its entry conditions, and the conditions that would make it
wrong, BEFORE any money moves.

---

## The trade

| Field | Value |
|---|---|
| Symbol | AMEX:GDX (VanEck Gold Miners ETF) |
| Direction | LONG |
| Entry | 76.50 or better |
| Stop | 68.70 (Chandelier Exit level) |
| Risk per share | 7.80 (**10.2%** of entry) |
| Position size | **$50,000** (~654 shares) |
| Dollar risk | **~$5,100** (0.51% of the $1M account) |
| First target | 84.00 |
| Reward:risk | 0.96 : 1 at T1... **see the problem below** |

## PROBLEM WITH MY OWN NUMBERS - read before entering

At the brief I quoted "target 84 for 2:1". **That was wrong arithmetic.**
Entry 76.50, stop 68.70 = 7.80 of risk. A 2:1 target requires
76.50 + 15.60 = **92.10**, not 84.00. At 84.00 the reward is 7.50 against 7.80
of risk, i.e. **0.96:1 - it FAILS the 2:1 gate outright.**

So one of two things has to change before this is a legal trade under the
execution protocol:

- **Option A - raise the target.** 92.10 is ~20% above entry. GDX would need a
  substantial extension of the current gold move. Possible but not a base case
  off one headline-driven session.
- **Option B - tighten the stop.** A stop at 72.50 (under today's low of 75.92
  is too tight; under the 7/17 consolidation shelf) gives 4.00 of risk, needs
  84.50 for 2:1, and allows a $125k position - capped to $100k by the order
  limit. But 4.00 is only ~1.07x ATR (ATR14 = 2.86, 3.75%), which is at the
  ATR floor, not comfortably above it.

**Recommendation: Option B with a stop at 72.00** (4.50 risk = 1.57x ATR,
clears the floor), size $100k cap -> ~1,307 shares -> $5,880 risk. That is
slightly over the $5k unit, so trim to **$85,000 (~1,111 shares) = $5,000 risk**,
2:1 target **85.50**.

Do NOT enter on the original numbers.

## Conditions required before entry (all must hold)

1. GDX **closes 2026-07-22 above 76.00**. It was 76.36 at 2:10pm CT, 2.1% off
   its high of 77.99, so this is not assured.
2. Gold holds its bid overnight. This move is driven by Iran headlines
   (Brent >$92, 11th consecutive night of US strikes) and reverses on a headline.
3. Entry only in the first 90 minutes of 7/23, at 76.50 or better. If it gaps
   above 77.50, **stand down** - chasing a gap on a headline move is the exact
   mistake this system exists to prevent.

## Why this trade

- Chandelier Exit flipped BUY on 2026-07-21 (1 bar old - fresh).
- Price 76.36 is above ZLSMA 71.52 by 6.7% - trend structure intact, not extended.
- Magical (CCI-20) 60.9, inside the +/-100 band. NOTE: measured 2026-07-22 across
  1,725 signals, this gate does not predict returns - it is context only.
- Strongest group on the tape today: +2.87% since the 7/21 close while SPY was flat.
- ETF, so no single-name earnings risk.

## What would make this wrong

- **Volume is not confirming.** GDX traded **0.57x** normal volume today. A
  leadership move on 57% of typical volume is not accumulation. This is the
  single biggest argument against the trade and it is why size is reduced.
- **NEM, a top GDX holding, reports earnings 2026-07-23 after the close.** The
  ETF carries indirect single-name event risk on day one of the position.
- **The broad tape is in sell mode.** SPY, QQQ, IWM, XLK and SMH all show
  Chandelier SELL. This is a long into a hostile backdrop.
- It faded 2.1% off its high today, the same intraday shape that made me reject
  PM.

## Grading

Grade at 21 trading days (2026-08-20) against:
- SPY over the identical window
- The origination TRACKER's A/B calls over the same window

Record: fill price vs planned entry, max favorable/adverse excursion, whether the
stop was hit, and whether the entry conditions above were actually met or
overridden.
