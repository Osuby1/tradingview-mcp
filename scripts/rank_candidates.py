"""Rank scan output so Omar knows what to do FIRST.

Requested 2026-07-22: rank buys strongest->weakest, blocked worst->best, and say
plainly whether sell-mode names are shortable.

HONESTY NOTE - READ THIS BEFORE TRUSTING A RANK
------------------------------------------------
These scores are **UNCALIBRATED**. They are a transparent weighting of things that
*ought* to matter, not a measured edge. Nothing here has been tested against
forward returns. Contrast the Magical gate, which looked sensible for months and
turned out to separate 21-day returns by 0.03 points across 1,725 signals.

So: use the rank to decide **what to look at first**, never as the reason to take
a trade. Every component is exposed in `components` so a rank can be argued with.
When ranking and judgement disagree, judgement wins.

Weights were chosen for one reason each, stated in RANK_RATIONALE below, so they
can be criticised individually rather than defended as a black box.
"""

ADX_MIN = 27.0  # raised from 20 (Omar decision 8/7): winner-traits scan found runners at ADX ~36 vs duds ~29; 20 was set below BOTH populations. PLTR counterexample logged; gate re-checker (also built 8/7) surfaces names that later clear 27.

RANK_RATIONALE = {
    "risk_quality": "How tight the stop is in ATR terms. Dominant weight because "
                    "stop distance decides position size, and size decides whether "
                    "a good call is worth anything.",
    "trend_strength": "ADX and the DI spread. A flip inside a real trend beats a "
                      "flip inside chop.",
    "regime": "Distance above the 200-day. The single filter that vetoed GDX.",
    "structure": "How far price sits above the ZLSMA. Just above = confirmed but "
                 "not chased; far above = extended.",
    "freshness": "Sessions since the flip. 1-3 is the sweet spot: settled enough "
                 "not to repaint, early enough to still be worth entering.",
    "liquidity": "Average daily dollar volume against the intended position.",
}


def _clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def score_long(r, position=85_000.0):
    """Strongest -> weakest buy. Returns (score 0-100, components, pros, cons)."""
    c, pros, cons = {}, [], []
    last, stop, zl = r.get("last"), r.get("long_stop"), r.get("zlsma")
    atr, adx = r.get("atr"), r.get("adx") or 0
    pdi, ndi = r.get("plus_di") or 0, r.get("minus_di") or 0
    regime, pct200 = r.get("regime"), r.get("pct_vs_200")
    adv, bars = r.get("avg_dollar_vol") or 0, r.get("bars_back")

    # --- risk quality (0-30) ------------------------------------------------
    if last and stop and last > stop:
        risk_pct = (last - stop) / last * 100
        x_atr = ((last - stop) / atr) if atr else None
        # best around 4-8% stop: tight enough to size, wide enough to survive noise
        if risk_pct <= 2:
            v, why = 0.35, (f"the stop is only {risk_pct:.1f}% below the price - "
                            "an ordinary quiet day could knock the trade out")
            cons.append(why)
        elif risk_pct <= 8:
            v = 1.0
            pros.append(f"the stop sits {risk_pct:.1f}% below the price - close "
                        "enough to buy a full-size position")
        elif risk_pct <= 12:
            v = 0.6
            cons.append(f"the stop is {risk_pct:.1f}% away, so the position has "
                        "to shrink to keep the dollar risk at $5k")
        else:
            v = 0.15
            cons.append(f"the stop is {risk_pct:.1f}% away - keeping risk at $5k "
                        "shrinks the position to a token")
        if x_atr is not None:
            if x_atr < 1.0:
                v *= 0.4
                cons.append(f"the stop sits {x_atr:.2f} normal daily swings below "
                            "the price (under 1.0) - routine wiggle will hit it "
                            "with nothing actually going wrong")
            elif x_atr >= 1.5:
                pros.append(f"the stop sits {x_atr:.2f} normal daily swings away - "
                            "comfortably outside day-to-day noise")
        c["risk_quality"] = round(30 * v, 1)
        c["_risk_pct"], c["_x_atr"] = round(risk_pct, 1), (round(x_atr, 2) if x_atr else None)
    else:
        c["risk_quality"] = 0.0
        cons.append("no usable stop level")

    # --- trend strength (0-25) ---------------------------------------------
    adx_v = _clamp((adx - 15) / 25)          # 15 -> 0, 40 -> 1
    di_v = _clamp((pdi - ndi) / 20)          # 20-point spread = full marks
    c["trend_strength"] = round(25 * (0.6 * adx_v + 0.4 * di_v), 1)
    if adx >= 25:
        pros.append(f"trend-strength reading (ADX) is {adx:.0f} - a real trend "
                    "is underway, not sideways chop")
    elif adx < ADX_MIN:
        cons.append(f"trend-strength reading (ADX) is only {adx:.0f}, under "
                    f"{ADX_MIN:.0f} - there is no trend here to ride")
    if pdi > ndi:
        pros.append(f"buyers are in control - buying pressure {pdi:.0f} vs "
                    f"selling pressure {ndi:.0f}")
    else:
        cons.append(f"sellers are in control - selling pressure {ndi:.0f} vs "
                    f"buying pressure {pdi:.0f}")

    # --- regime (0-20) ------------------------------------------------------
    if regime == "PASS":
        c["regime"] = 20.0
        pros.append(f"passes the long-term health check - price is "
                    f"{pct200:+.1f}% vs its 200-day average")
    elif regime == "REPAIR":
        c["regime"] = 7.0
        cons.append(f"still repairing - price is {pct200:+.1f}% vs its 200-day "
                    "average, so starter size only")
    else:
        c["regime"] = 0.0
        cons.append(f"fails the long-term health check badly ({pct200:+.1f}% vs "
                    "its 200-day average) - watch only, no size")

    # --- structure (0-10) ---------------------------------------------------
    if last and zl and zl > 0:
        above = (last / zl - 1) * 100
        if above <= 0:
            c["structure"] = 0.0
            cons.append(f"price is {abs(above):.1f}% BELOW its trend line "
                        "(ZLSMA) - the turn up has not actually happened yet")
        elif above <= 12:
            c["structure"] = 10.0
            pros.append(f"price is {above:.1f}% above its trend line (ZLSMA) - "
                        "the turn is confirmed and you are not chasing")
        else:
            c["structure"] = round(_clamp(1 - (above - 12) / 40) * 10, 1)
            cons.append(f"price is {above:.0f}% above its trend line (ZLSMA) - "
                        "stretched, a worse entry")
        c["_above_zlsma_pct"] = round(above, 1)
    else:
        c["structure"] = 0.0

    # --- freshness (0-10) ---------------------------------------------------
    if bars is None:
        c["freshness"] = 0.0
    elif bars == 0:
        c["freshness"] = 4.0
        cons.append("the signal fired TODAY - it can still un-print before the "
                    "close, so treat it as provisional")
    elif bars <= 3:
        c["freshness"] = 10.0
        pros.append(f"signal is {bars} sessions old - settled enough to trust, "
                    "early enough to still be worth entering")
    elif bars <= 5:
        c["freshness"] = 7.0
    else:
        c["freshness"] = 3.0
        cons.append(f"signal is {bars} sessions old - the easy part of the move "
                    "may already be gone")

    # --- liquidity (0-5) ----------------------------------------------------
    if adv:
        headroom = adv / 10.0 / position if position else 0
        c["liquidity"] = round(5 * _clamp(headroom / 3), 1)
        if headroom < 1:
            cons.append(f"too thinly traded - about ${adv:,.0f} changes hands "
                        f"daily, not enough to get a ${position:,.0f} order in "
                        "and out cleanly")
        elif headroom > 20:
            pros.append("deeply traded - getting in and out is never a problem")
    else:
        c["liquidity"] = 0.0

    score = round(sum(v for k, v in c.items() if not k.startswith("_")), 1)
    return score, c, pros, cons


# --------------------------------------------------------------------------- #
# score_long_v2 - re-weighted after the 2026-07-22 calibration.
#
# The calibration (170 signals, 60 names) found only TWO components with any
# forward-return signal: trend (ADX/DI, Spearman +0.092) and structure (vs ZLSMA,
# +0.086). Risk quality - the 30%-weight driver of v1 - was NEGATIVE (-0.052).
# Omar's instruction: re-weight toward trend + structure, stop letting risk
# quality drive the sort.
#
# So v2 ranks on trend + structure + a small regime tilt. Risk quality is REMOVED
# from the ranking and returned separately as risk_flag - it is a sizing/survival
# input, not a return predictor, and dressing it up as "quality" was the v1 error.
#
# HONESTY: these weights were chosen FROM the calibration sample, so any in-sample
# re-test is circular and optimistic. The only number that means anything is the
# held-out test in calibrate_buy_score.py. Even that rests on a weak +0.09 signal
# from one strong-tape window - treat v2 as "less wrong", not "calibrated".
# --------------------------------------------------------------------------- #

WEIGHTS_V2 = {"trend": 0.45, "structure": 0.35, "regime": 0.15,
              "freshness": 0.03, "liquidity": 0.02}


def score_long_v2(r, position=85_000.0):
    """Re-weighted 0-100 rank. Returns (score, components, risk_flag)."""
    last, stop, zl = r.get("last"), r.get("long_stop"), r.get("zlsma")
    atr, adx = r.get("atr"), r.get("adx") or 0
    pdi, ndi = r.get("plus_di") or 0, r.get("minus_di") or 0
    regime = r.get("regime")
    adv, bars = r.get("avg_dollar_vol") or 0, r.get("bars_back")

    sub = {}
    # trend 0-1: the strongest signal in the study
    sub["trend"] = _clamp(0.6 * _clamp((adx - 15) / 25) + 0.4 * _clamp((pdi - ndi) / 20))
    # structure 0-1: just above ZLSMA is best; below = 0; far above = decays
    if last and zl and zl > 0:
        above = (last / zl - 1) * 100
        if above <= 0:
            sub["structure"] = 0.0
        elif above <= 12:
            sub["structure"] = 1.0
        else:
            sub["structure"] = _clamp(1 - (above - 12) / 40)
    else:
        sub["structure"] = 0.0
    # regime 0-1: weak but positive
    sub["regime"] = {"PASS": 1.0, "REPAIR": 0.35}.get(regime, 0.0)
    # freshness / liquidity: near-zero signal, kept as tiny operational nudges
    sub["freshness"] = (1.0 if (bars is not None and 1 <= bars <= 3)
                        else 0.6 if (bars is not None and bars <= 5) else 0.3)
    sub["liquidity"] = _clamp((adv / 10.0 / position) / 3) if position else 0.0

    score = round(100 * sum(WEIGHTS_V2[k] * sub[k] for k in WEIGHTS_V2), 1)

    # risk_flag: sizing/survival read, NOT part of the sort
    risk_flag = {}
    if last and stop and atr and last > stop:
        x = (last - stop) / atr
        risk_flag = {"stop_pct": round((last - stop) / last * 100, 1),
                     "stop_x_atr": round(x, 2),
                     "ok": 1.0 <= x <= 4.0}
    return score, {"sub": sub, "weights": WEIGHTS_V2}, risk_flag


def score_short(r, position=85_000.0):
    """Best -> worst SHORT candidate. Mirror of the long test, plus squeeze checks.

    A failed long is NOT automatically a good short - see SHORT_POLICY.
    """
    c, pros, cons = {}, [], []
    last, zl = r.get("last"), r.get("zlsma")
    adx = r.get("adx") or 0
    pdi, ndi = r.get("plus_di") or 0, r.get("minus_di") or 0
    pct200, adv = r.get("pct_vs_200"), r.get("avg_dollar_vol") or 0
    stop = r.get("short_stop")
    atr = r.get("atr")

    # downtrend quality (0-30)
    if pct200 is not None:
        if pct200 < -10:
            c["downtrend"] = 30.0
            pros.append(f"price is {pct200:.1f}% below its 200-day average - an "
                        "established downtrend")
        elif pct200 < 0:
            c["downtrend"] = 18.0
            pros.append(f"price is {pct200:.1f}% below its 200-day average")
        else:
            c["downtrend"] = 0.0
            cons.append(f"still {pct200:+.1f}% ABOVE its 200-day average - this "
                        "is not actually a downtrend")
    else:
        c["downtrend"] = 0.0

    # trend strength (0-25)
    adx_v = _clamp((adx - 15) / 25)
    di_v = _clamp((ndi - pdi) / 20)
    c["trend_strength"] = round(25 * (0.6 * adx_v + 0.4 * di_v), 1)
    if adx < ADX_MIN:
        cons.append(f"trend-strength reading (ADX) is only {adx:.0f} - no real "
                    "trend, and shorting a sideways chop bleeds money")
    if ndi > pdi:
        pros.append(f"sellers are in control - selling pressure {ndi:.0f} vs "
                    f"buying pressure {pdi:.0f}")
    else:
        cons.append(f"buyers are in control (buying pressure {pdi:.0f}) - "
                    "wrong side to be short")

    # structure (0-15)
    if last and zl and zl > 0:
        below = (1 - last / zl) * 100
        c["structure"] = round(15 * _clamp(below / 8), 1) if below > 0 else 0.0
        if below <= 0:
            cons.append("price is ABOVE its trend line (ZLSMA) - the structure "
                        "has not broken down")
        else:
            pros.append(f"price is {below:.1f}% below its trend line (ZLSMA)")

    # stop quality (0-15)
    if last and stop and stop > last:
        risk_pct = (stop - last) / last * 100
        x_atr = ((stop - last) / atr) if atr else None
        c["stop_quality"] = round(15 * _clamp(1 - abs(risk_pct - 6) / 10), 1)
        c["_risk_pct"] = round(risk_pct, 1)
        if x_atr and x_atr < 1.0:
            cons.append(f"the stop sits only {x_atr:.2f} normal daily swings "
                        "away - too tight, routine bounces would hit it")
    else:
        c["stop_quality"] = 0.0
        cons.append("no Chandelier short stop available")

    # squeeze / exhaustion risk (0-15, higher = safer)
    risk_pts = 15.0
    if pct200 is not None and pct200 < -45:
        risk_pts -= 8
        cons.append(f"already {pct200:.0f}% below its 200-day average - the "
                    "move is late, and late shorts are squeeze bait")
    if adv and adv < 20_000_000:
        risk_pts -= 7
        cons.append(f"thinly traded (about ${adv:,.0f} a day) - shares are hard "
                    "to borrow and a squeeze moves it violently")
    c["squeeze_safety"] = round(max(0.0, risk_pts), 1)

    score = round(sum(v for k, v in c.items() if not k.startswith("_")), 1)
    return score, c, pros, cons


def rank_blocked_severity(r):
    """WORST -> best. Higher = more comprehensively unsuitable.

    'Worst' means furthest from ever being tradeable, so the top of the blocked
    list is what to stop looking at, and the bottom is what is nearly there.
    """
    sev = 0.0
    reasons = []
    pct200 = r.get("pct_vs_200")
    if r.get("regime") == "DEEP-FAIL":
        sev += 40
        reasons.append("regime DEEP-FAIL")
    elif r.get("regime") == "REPAIR":
        sev += 15
        reasons.append("regime REPAIR")
    if (r.get("adx") or 0) < ADX_MIN:
        sev += 20
        reasons.append("no trend")
    if (r.get("plus_di") or 0) <= (r.get("minus_di") or 0):
        sev += 15
        reasons.append("sellers in control")
    last, zl = r.get("last"), r.get("zlsma")
    if last and zl and last <= zl:
        sev += 15
        reasons.append("below ZLSMA")
    adv = r.get("avg_dollar_vol") or 0
    if adv and adv / 10.0 < 85_000:
        sev += 25
        reasons.append("illiquid")
    if pct200 is not None:
        sev += _clamp(-pct200 / 60) * 10
    return round(sev, 1), reasons


SHORT_POLICY = """SHOULD YOU SHORT THESE? - short answer: NO, not on this signal alone.

A name failing the long test is not thereby a good short. The long gates ask "is
this going up?"; answering no is not the same as "this is going down".

Three reasons these lists are NOT short recommendations:

1. **Your execution protocol has no short rules.** The $1M / $5k-per-trade /
   $100k-order / 2:1 framework was written for longs. Position sizing on an
   unbounded-loss instrument needs its own rules, and they do not exist yet.
2. **Borrow and squeeze risk is unmeasured.** Nothing in this scan sees short
   interest, days-to-cover, borrow cost or float. The thinnest, most broken names
   - which score best as shorts on price alone - are exactly the ones that squeeze.
3. **The short side has not been measured at all.** The long gates were at least
   tested (1,725 signals). Zero equivalent work exists for shorts. Trading them
   would be running an unvalidated system with unbounded downside.

What the SHORT RANK column IS for: if you already hold a name, a high short score
is a reason to exit or hedge. And it is the pre-registration list - if you want a
short book, these are the candidates to paper-trade first.

Nothing here is a recommendation to open a short.
"""
