# Fixing the cons — what the evidence actually supports

2026-07-25. Written after five hours of pre-registered tests tore the system
down, and after one more test (the exit redesign, run today) answered the
biggest remaining question. This is the con-by-con repair plan, in plain
English, with every claim tied to a measurement in this repo.

---

## The question, reframed

The question asked was: *"Fix the cons using the best technical analysis —
especially how to time trades, especially exits, and how to pick favored
sectors and stocks making huge runs, before the run."*

That question assumes the fix is a better indicator. Our own tests just spent a
week proving there isn't one: the rotation radar's states run backwards, stock
selection adds nothing over the sector ETF, every score has zero predictive
power, and earnings surprise failed all four of its requirements. Asking for
"the best technical analysis" after that is asking which brand of the thing
that just failed to buy next.

**The better question — the one the data can actually answer — is:**

> *"My returns are a lottery: the top 5% of trades carry all the profit. My
> detector already gets me into 79% of the big runs early, and my risk gates
> already kept me flat through 2022. The one measured leak is that my exits
> throw the winning tickets away. What keeps the tail — and what do I stop
> pretending works?"*

Everything below is the answer to that question.

---

## Con by con

### 1. "Exits destroy value" — MEASURED, and the fix is subtraction, not addition

Three studies now agree (Jan–Jun 2026 replay, ZLSMA sweep, and today's
exit-redesign test across 12,230 signals, 2021–2025, bear year included):

- The live rule — Chandelier stop + 2:1 target — turned a +5.89% average hold
  into +0.82%. The target caps every winner at 2R in a system whose entire
  profit is a handful of +100% tails. It is mathematically the wrong tool for
  this distribution.
- **No exit rule tested beats holding — including in 2022.** The bear-year
  protection everyone assumes an exit provides was already provided by the
  entry gates, which halved the signal count in 2022 and kept what fired flat
  while SPY fell 19%. The exit only added whipsaw on top.
- Exits are not free risk control; they are expensive insurance. The live rule
  pays 5.1 points of return to cap the worst trade at −12% instead of −67%.
  That price is now known, so it can be chosen deliberately instead of paid
  blindly.

**The fix:** stop using price targets, full stop. Hold winners longer — the
tested horizon that worked is measured in months, not 21 days. Take risk
control from the two things that measured well: the entry gates, and small
fixed-risk position sizes ($5k risk per trade already does this). If a
drawdown cap is emotionally necessary, the 20% ratchet was the least-bad
managed rule (+4.14% vs +0.82%) — but it is a comfort purchase costing ~1.75
points, and it must be labelled that, never "edge."

Nothing changes in the live pipeline before the 2026-08-31 rule freeze ends;
the *claims* change today.

### 2. "Time my entries better" — NOT BROKEN, do not touch

The replay showed the detector flagged 109 of 138 stocks that ran 50%+ — before
the peak, often months early (SNDK +755%: first signal March 13). Entry timing
is the one part of the machine that works. Every hour spent "improving" it is
an hour spent on the wrong component, with a real risk of breaking the only
thing that measured well.

### 3. "Pick the sector before the huge run" — NOT FIXABLE WITH PRICE DATA, and we proved it ourselves

The rotation radar's IGNITING sectors went on to do the *worst* (+1.14% vs
ROLLING's +4.51% at 60 days — the ladder is perfectly inverted). Acceleration
correlates *negatively* with forward returns at 2–6 months. This is not a
flawed formula — plain momentum scored the same — it is the premise. At the
horizon you trade, "just started accelerating" is closer to a fade signal than
a buy signal, and no indicator setting escapes that.

**The honest replacement for "before the run": be early IN the run and stay
in.** The detector already provides early; the exit fix (con #1) provides
stay-in. That combination — caught SNDK in March, held for months instead of
21 days with a 2R cap — is the entire realistic version of "catch huge runs."
The radar survives as a notice board ("energy is moving, go look"), never as
an allocator.

### 4. "Stock selection adds nothing over the ETF" — ACCEPT IT, restructure around it

+0.71 pt excess at a 48.9% hit rate with a negative median, nothing at all in
the last three years, and the whole positive mean living in the top 5% of
trades. The defensible structure is the one pre-committed in the PEAD verdict:
**a passive core** (broad index / sector ETFs) as the default home for
capital, with the scan-driven trades as a small, fixed-risk satellite whose
job is to be present for tails. The satellite is entertainment-plus-optionality
until a pre-registered test says otherwise — size it like that.

### 5. "88 signals a day is a firehose" — OPEN, and it is a portfolio question, not a scoring question

Every attempt to rank the firehose (BUY SCORE, origination score, grades) has
zero predictive power, so shortlisting by score is decoration. The unexplored
lever is portfolio construction: how many concurrent positions, first-come vs
rotation, capital recycling after N flat days. That is a separate pre-ratified
test to design — it is the only remaining place a real improvement could live,
alongside sizing (Gap-1), which is still the one untested link in the risk
chain.

### 6. The scores — LABELS, forever, until one passes a test

BUY SCORE, origination score, radar states: all measured, all ~zero. They may
appear in reports as descriptive labels only, never as numbers implying
forecast, never as a sort order presented as conviction.

---

## What survives, said plainly

Two components earned their place with data, and the repair plan is built on
them:

1. **Detection** — 79% of big movers flagged before their peaks. It is a
   watchlist generator and it is good at it.
2. **Risk control at entry** — the gate stack halved exposure in 2022 and cut
   stop-out rates; picks held flat while sectors fell. It is not a stock
   picker and never was; described honestly, it is seatbelts.

Plus the discipline itself: pre-registration caught every one of these
illusions before money kept leaking into them. That process is the single most
valuable thing built this week and it now applies to any future change,
including the ones proposed here.

## What to actually watch, and when

- **Now → 2026-08-31 (rule freeze):** nothing changes live. The paper book
  keeps grading the live rule so the freeze period doubles as baseline data.
- **After the freeze:** the one change with three measurements behind it —
  drop the 2:1 target, extend the holding window, keep entries and gates
  untouched — goes to the paper book first, graded weekly against the old rule.
- **Friday reviews:** the outcome tracker keeps score. If the held-longer book
  does not show its expected advantage within a quarter, that too gets written
  down and acted on.
- **Do not act on:** any urge to lower the ADX floor to 18 because TWST/HIMX/HUT
  missed by a point — that instinct is curve-fitting wearing a helpful face,
  and the replay registration already quarantined it.
