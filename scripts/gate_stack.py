"""THE GATE STACK - the single place a scan decides whether a name is tradeable.

Made permanent 2026-07-22 at Omar's instruction, after HQ Swing v1's regime
filter vetoed a GDX call that every Chandelier gate had passed, then culled 29
fresh signals to zero.

Design rule: **a gate that is documented but not executed is not a gate.**
On 2026-07-22 the liquidity check existed only as an unused constant, so SKK was
auto-scored PASSING and had to be caught by hand. Every gate here executes, and
`evaluate()` raises if the data needed to run one is missing rather than
silently letting the name through.

Order matters - cheapest and most decisive first:

  1. REGIME   - DEEP-FAIL (>10% below the 200-day) = no size, ever.
                REPAIR (below the 200-day) = starter size only.
                PASS = above a rising 200-day AND above the 50-day.
  2. TREND    - ADX(14) >= 20. Below that there is no trend to ride.
  3. DIRECTION- +DI > -DI. Bulls actually in control.
  4. STRUCTURE- price above the ZLSMA (the Chandelier stack's own test).
  5. LIQUIDITY- the intended position must be <= 1/10th of average daily
                DOLLAR volume, so you can get out.

Why both 1-3 and 4: on 2026-07-22 GDX passed 4 and failed 1-3; PANW, DE and KRE
passed 1-3 and failed 4. The two systems disagree in BOTH directions, so neither
substitutes for the other.
"""

ADX_MIN = 20.0
DEEP_FAIL_PCT = -10.0
ADV_MULTIPLE = 10.0          # position must be <= ADV / this
DEFAULT_POSITION = 85_000.0  # sizing assumption for the liquidity test
ATR_FLOOR = 1.0              # stop must be at least this many ATRs from entry
ATR_CEILING = 4.0            # a stop this far out makes the position a token
MAX_STOP_PCT = 12.0          # volatility cap: a trend stop this far out = too wild to size


class MissingGateData(Exception):
    """Raised when a gate cannot be evaluated. Never silently pass instead."""


REQUIRED = ("last", "zlsma", "regime", "adx", "plus_di", "minus_di",
            "avg_dollar_vol", "atr")


def evaluate(row, position_size=DEFAULT_POSITION, strict=True):
    """Run the full stack. Returns (verdict, reasons, detail).

    row: a sweep record carrying last/zlsma/regime/adx/plus_di/minus_di/
         avg_dollar_vol (all produced by og_sweep_runner.js).
    strict: raise MissingGateData if a gate's inputs are absent. Turning this
            off is how gates quietly stop running - only do it deliberately.
    """
    missing = [k for k in REQUIRED if row.get(k) is None]
    if missing:
        msg = f"{row.get('rname') or row.get('sym')}: cannot evaluate gates, missing {missing}"
        if strict:
            raise MissingGateData(msg)
        return "BLOCKED: no gate data", [msg], {}

    fails, notes = [], []
    regime = row["regime"]
    pct200 = row.get("pct_vs_200")
    adx, pdi, ndi = row["adx"], row["plus_di"], row["minus_di"]
    last, zl, adv = row["last"], row["zlsma"], row["avg_dollar_vol"]

    # 1. regime
    if regime == "DEEP-FAIL":
        fails.append(f"regime DEEP-FAIL ({pct200}% vs 200-day) - watch only, no size")
    elif regime == "REPAIR":
        notes.append(f"regime REPAIR ({pct200}% vs 200-day) - starter size only")

    # 2. trend
    if adx < ADX_MIN:
        fails.append(f"ADX {adx} below {ADX_MIN:.0f} - no trend to ride")

    # 3. direction
    if pdi <= ndi:
        fails.append(f"-DI {ndi} >= +DI {pdi} - sellers in control")

    # 4. structure
    if last <= zl:
        fails.append(f"price {last} at/below ZLSMA {zl} - structure has not turned")

    # 5. ATR floor - the stop must sit outside normal daily noise.
    #
    # Wired 2026-07-22 at Omar's instruction. FRT was the case that forced it:
    # stop 1.63 against ATR 1.99 = 0.82x, so ordinary daily range would have
    # stopped it out with nothing happening. It passed the automated stack and
    # had to be caught by hand - the same failure as SKK and liquidity.
    atr, stop = row.get("atr"), row.get("long_stop") or row.get("stop")
    if atr and stop and last and last > stop:
        x_atr = (last - stop) / atr
        detail_atr = round(x_atr, 2)
        if x_atr < ATR_FLOOR:
            fails.append(
                f"stop is {x_atr:.2f}x ATR ({atr}) - inside daily noise, it gets "
                f"hit by nothing happening (floor {ATR_FLOOR:.1f}x)")
        elif x_atr > ATR_CEILING:
            fails.append(
                f"stop is {x_atr:.2f}x ATR - so wide the position shrinks to a "
                f"token (ceiling {ATR_CEILING:.1f}x)")
    else:
        detail_atr = None
        if not atr:
            fails.append("no ATR available - cannot check the stop against noise")

    # 5b. Absolute stop cap - the VOLATILITY CAP (re-justified 2026-07-26).
    #
    # HISTORY: born 2026-07-22 as "the 2:1 gate expressed as arithmetic" (a stop
    # N% away needs a 2N% move to pay 2:1; DELL's 20.3% stop was the trigger).
    # The 2:1 profit target was RETIRED 2026-07-25 (exit-redesign test), which
    # killed that rationale - with tail-riding exits, +2N% moves are precisely
    # what we hold for. The BEHAVIOR is deliberately unchanged (Omar-directed
    # 7/26, freeze-compatible): what the cap actually screens is volatility - a
    # name whose trend stop sits >12% away swings so hard that a fixed-risk
    # position becomes a token and any sane initial stop lives inside its daily
    # range. Whether that screen still earns its keep under the new exits is an
    # OPEN question: it blocked SOXL before +539% (Jan-Jun replay), and
    # gate_outcomes.py now grades cap-blocks as their own forward cohort so the
    # answer arrives as data, not anecdote.
    if last and stop and last > stop:
        stop_pct = (last - stop) / last * 100
        if stop_pct > MAX_STOP_PCT:
            fails.append(
                f"stop is {stop_pct:.1f}% away - volatility cap {MAX_STOP_PCT:.0f}%: "
                f"a name this wild shrinks a fixed-risk position to a token")

    # 6. liquidity
    max_pos = adv / ADV_MULTIPLE
    if position_size > max_pos:
        pct = position_size / adv * 100 if adv else float("inf")
        fails.append(
            f"illiquid - ${adv:,.0f} avg daily dollar volume; a ${position_size:,.0f} "
            f"position is {pct:.0f}% of a day's turnover (max ${max_pos:,.0f})")

    detail = {"regime": regime, "pct_vs_200": pct200, "adx": adx,
              "plus_di": pdi, "minus_di": ndi, "above_zlsma": last > zl,
              "avg_dollar_vol": adv, "max_position": round(max_pos),
              "atr": atr, "stop_x_atr": detail_atr}

    if fails:
        head = fails[0].split(" - ")[0]
        return f"BLOCKED: {head}", fails, detail
    if notes:
        return "STARTER ONLY - regime REPAIR", notes, detail
    return "CANDIDATE - passes every gate", [], detail


def funnel(rows, position_size=DEFAULT_POSITION):
    """Stage-by-stage survivor counts, for the workbook and the brief."""
    stages = [("fresh signals", lambda r: True),
              ("regime PASS", lambda r: r.get("regime") == "PASS"),
              (f"ADX >= {ADX_MIN:.0f}", lambda r: (r.get("adx") or 0) >= ADX_MIN),
              ("+DI > -DI", lambda r: (r.get("plus_di") or 0) > (r.get("minus_di") or 0)),
              ("above ZLSMA", lambda r: (r.get("last") or 0) > (r.get("zlsma") or 0)),
              (f"stop >= {ATR_FLOOR:.0f}x ATR",
               lambda r: bool(r.get("atr")) and bool(r.get("long_stop"))
               and (r["last"] - r["long_stop"]) / r["atr"] >= ATR_FLOOR),
              ("liquid enough",
               lambda r: (r.get("avg_dollar_vol") or 0) / ADV_MULTIPLE >= position_size)]
    out, cur = [], list(rows)
    for name, fn in stages:
        cur = [r for r in cur if fn(r)]
        out.append((name, len(cur)))
    return out, cur
