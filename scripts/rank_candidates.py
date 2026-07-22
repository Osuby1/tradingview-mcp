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

ADX_MIN = 20.0

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
            v, why = 0.35, f"stop only {risk_pct:.1f}% - likely inside daily noise"
            cons.append(why)
        elif risk_pct <= 8:
            v = 1.0
            pros.append(f"stop {risk_pct:.1f}% supports a full-size position")
        elif risk_pct <= 12:
            v = 0.6
            cons.append(f"stop {risk_pct:.1f}% forces a reduced position")
        else:
            v = 0.15
            cons.append(f"stop {risk_pct:.1f}% - position shrinks to a token")
        if x_atr is not None:
            if x_atr < 1.0:
                v *= 0.4
                cons.append(f"stop is {x_atr:.2f}x ATR - BELOW the floor, noise will hit it")
            elif x_atr >= 1.5:
                pros.append(f"stop {x_atr:.2f}x ATR - comfortably outside the noise")
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
        pros.append(f"ADX {adx:.0f} - a real trend, not chop")
    elif adx < ADX_MIN:
        cons.append(f"ADX {adx:.0f} below {ADX_MIN:.0f} - no trend to ride")
    if pdi > ndi:
        pros.append(f"buyers in control (+DI {pdi:.0f} vs -DI {ndi:.0f})")
    else:
        cons.append(f"sellers in control (-DI {ndi:.0f} vs +DI {pdi:.0f})")

    # --- regime (0-20) ------------------------------------------------------
    if regime == "PASS":
        c["regime"] = 20.0
        pros.append(f"regime PASS, {pct200:+.1f}% vs the 200-day")
    elif regime == "REPAIR":
        c["regime"] = 7.0
        cons.append(f"regime REPAIR ({pct200:+.1f}% vs 200-day) - starter size only")
    else:
        c["regime"] = 0.0
        cons.append(f"regime DEEP-FAIL ({pct200:+.1f}% vs 200-day) - no size")

    # --- structure (0-10) ---------------------------------------------------
    if last and zl and zl > 0:
        above = (last / zl - 1) * 100
        if above <= 0:
            c["structure"] = 0.0
            cons.append(f"price is {abs(above):.1f}% BELOW the ZLSMA - trend has not turned")
        elif above <= 12:
            c["structure"] = 10.0
            pros.append(f"{above:.1f}% above the ZLSMA - confirmed without chasing")
        else:
            c["structure"] = round(_clamp(1 - (above - 12) / 40) * 10, 1)
            cons.append(f"{above:.0f}% above the ZLSMA - extended")
        c["_above_zlsma_pct"] = round(above, 1)
    else:
        c["structure"] = 0.0

    # --- freshness (0-10) ---------------------------------------------------
    if bars is None:
        c["freshness"] = 0.0
    elif bars == 0:
        c["freshness"] = 4.0
        cons.append("flipped TODAY - can still repaint before the close")
    elif bars <= 3:
        c["freshness"] = 10.0
        pros.append(f"{bars} sessions old - settled but still early")
    elif bars <= 5:
        c["freshness"] = 7.0
    else:
        c["freshness"] = 3.0
        cons.append(f"{bars} sessions old - the easy move may be gone")

    # --- liquidity (0-5) ----------------------------------------------------
    if adv:
        headroom = adv / 10.0 / position if position else 0
        c["liquidity"] = round(5 * _clamp(headroom / 3), 1)
        if headroom < 1:
            cons.append(f"illiquid - ${adv:,.0f} ADV cannot absorb ${position:,.0f}")
        elif headroom > 20:
            pros.append("deeply liquid - size is never the constraint")
    else:
        c["liquidity"] = 0.0

    score = round(sum(v for k, v in c.items() if not k.startswith("_")), 1)
    return score, c, pros, cons


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
            pros.append(f"{pct200:.1f}% below the 200-day - established downtrend")
        elif pct200 < 0:
            c["downtrend"] = 18.0
            pros.append(f"{pct200:.1f}% below the 200-day")
        else:
            c["downtrend"] = 0.0
            cons.append(f"still {pct200:+.1f}% ABOVE the 200-day - not a downtrend")
    else:
        c["downtrend"] = 0.0

    # trend strength (0-25)
    adx_v = _clamp((adx - 15) / 25)
    di_v = _clamp((ndi - pdi) / 20)
    c["trend_strength"] = round(25 * (0.6 * adx_v + 0.4 * di_v), 1)
    if adx < ADX_MIN:
        cons.append(f"ADX {adx:.0f} - no trend; shorting chop bleeds")
    if ndi > pdi:
        pros.append(f"sellers in control (-DI {ndi:.0f} vs +DI {pdi:.0f})")
    else:
        cons.append(f"buyers in control (+DI {pdi:.0f}) - wrong side")

    # structure (0-15)
    if last and zl and zl > 0:
        below = (1 - last / zl) * 100
        c["structure"] = round(15 * _clamp(below / 8), 1) if below > 0 else 0.0
        if below <= 0:
            cons.append("price is ABOVE the ZLSMA - not broken")
        else:
            pros.append(f"{below:.1f}% below the ZLSMA")

    # stop quality (0-15)
    if last and stop and stop > last:
        risk_pct = (stop - last) / last * 100
        x_atr = ((stop - last) / atr) if atr else None
        c["stop_quality"] = round(15 * _clamp(1 - abs(risk_pct - 6) / 10), 1)
        c["_risk_pct"] = round(risk_pct, 1)
        if x_atr and x_atr < 1.0:
            cons.append(f"stop {x_atr:.2f}x ATR - too tight for a short")
    else:
        c["stop_quality"] = 0.0
        cons.append("no Chandelier short stop available")

    # squeeze / exhaustion risk (0-15, higher = safer)
    risk_pts = 15.0
    if pct200 is not None and pct200 < -45:
        risk_pts -= 8
        cons.append(f"already {pct200:.0f}% below the 200-day - late, squeeze-prone")
    if adv and adv < 20_000_000:
        risk_pts -= 7
        cons.append(f"thin (${adv:,.0f} ADV) - hard to borrow, easy to squeeze")
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
