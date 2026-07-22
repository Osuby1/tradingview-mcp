"""Biggest market gainers/losers for the day, screened + run through protocol.

Requested by Omar 2026-07-22: add the day's biggest market-wide gainers and
losers to the daily workbook, and run the full protocol on each - is it worth
buying or shorting?

THE HARD TRUTH THIS MODULE ENCODES
----------------------------------
The literal biggest percentage movers in the whole market are ALMOST ALWAYS
microcap pump-and-dumps, Chinese small-caps, and post-halt penny stocks. On
2026-07-22 the entire top-12 gainers ran $0.26-$12.25 with market caps from
$260K to $301M; ZCMD was +192%, ZBAO +45% on 494M shares at $0.26. None are
tradeable in a $1M account running $100k orders.

So "run the protocol on the biggest movers" cannot mean "chart every penny
stock". The protocol's FIRST answer for these is SKIP, and the screen says so
instantly and cheaply. Only movers that clear a liquidity bar get the full
gate-stack / short-score treatment.

Screen (a mover must clear ALL to earn full analysis):
  * price      >= MIN_PRICE      - below this it is a lottery ticket, not a trade
  * market cap >= MIN_MCAP       - microcaps gap and halt; you cannot size or exit
  * $ volume   >= MIN_DOLLAR_VOL - a $100k order must be a small slice of the day

Anything that fails gets a one-line SKIP reason. Survivors are charted elsewhere
(regime/ATR/CE) and passed to gate_stack + score_short here.
"""
import re

MIN_PRICE = 5.0
MIN_MCAP = 2_000_000_000.0        # $2B
MIN_DOLLAR_VOL = 25_000_000.0     # $25M traded today

_SUFFIX = {"K": 1e3, "M": 1e6, "B": 1e9, "T": 1e12}


def parse_num(s):
    """'19.77B' / '4.2M' / '128,560,724' -> float."""
    if s is None:
        return None
    s = str(s).strip().replace(",", "").replace("$", "").replace("%", "")
    if not s or s.upper() in ("N/A", "-", "NONE"):
        return None
    m = re.match(r"^(-?\d+(?:\.\d+)?)([KMBT])?$", s, re.I)
    if not m:
        try:
            return float(s)
        except ValueError:
            return None
    val = float(m.group(1))
    if m.group(2):
        val *= _SUFFIX[m.group(2).upper()]
    return val


def screen(mover):
    """Return (tradeable: bool, skip_reason: str|None).

    mover: dict with price, market_cap, volume (numbers already parsed).
    A short-side note: microcaps are the WORST shorts despite the big red number
    - no borrow, violent squeezes - so the SKIP applies to both sides.
    """
    price = mover.get("price")
    mcap = mover.get("market_cap")
    vol = mover.get("volume")
    dollar_vol = (price * vol) if (price and vol) else None

    reasons = []
    if price is None or price < MIN_PRICE:
        reasons.append(f"price ${price:.2f} < ${MIN_PRICE:.0f}" if price
                       else "no price")
    if mcap is None or mcap < MIN_MCAP:
        reasons.append(f"mkt cap {_fmt(mcap)} < $2B - microcap, gaps and halts"
                       if mcap else "no market cap")
    if dollar_vol is not None and dollar_vol < MIN_DOLLAR_VOL:
        reasons.append(f"only {_fmt(dollar_vol)} traded - too thin for $100k")

    if reasons:
        return False, "; ".join(reasons)
    return True, None


def _fmt(x):
    if x is None:
        return "?"
    for suf, div in (("B", 1e9), ("M", 1e6), ("K", 1e3)):
        if abs(x) >= div:
            return f"${x/div:.1f}{suf}"
    return f"${x:.0f}"


def classify_untradeable(mover, side):
    """Plain-English protocol verdict for a mover that failed the screen.

    side: 'gainer' or 'loser'. The verdict differs - a microcap SPIKE is a chase
    trap, a microcap CRASH is a falling-knife/short-squeeze trap.
    """
    if side == "gainer":
        return ("SKIP - do not chase",
                "A microcap up this much in a day is a momentum/pump move, not an "
                "investable trend. No size fits, it can halt or reverse violently, "
                "and it is not shortable either (no borrow, squeeze risk).")
    return ("SKIP - not a short",
            "A microcap crashing this hard is a falling knife with squeeze risk and "
            "usually no locate. The big red number looks like a short but it is the "
            "most dangerous kind. Not a buy either - catching it needs a catalyst "
            "read this scan does not have.")


def protocol_verdict(mover, gate_result=None, short_result=None):
    """Full-protocol verdict for a mover that CLEARED the screen.

    gate_result: (verdict, reasons, detail) from gate_stack.evaluate (long side).
    short_result: (score, components, pros, cons) from rank_candidates.score_short.
    Returns (headline, explanation).
    """
    if gate_result is None:
        return ("NEEDS CHART", "Cleared the liquidity screen - chart it and run the "
                               "gate stack before deciding.")
    verdict = gate_result[0]
    if verdict.startswith("CANDIDATE"):
        return ("BUY CANDIDATE",
                "Cleared the liquidity screen AND every gate. Size it on the Plans "
                "tab and verify the earnings date and the move's catalyst first - a "
                "gap this size usually has news behind it.")
    if verdict.startswith("STARTER"):
        return ("STARTER ONLY",
                "Liquid and mostly clean, but regime is REPAIR - half size at most.")
    # blocked long -> is it a clean short instead?
    sc = short_result[0] if short_result else 0
    if sc and sc >= 70:
        return ("POSSIBLE SHORT (watch only)",
                f"Fails as a long ({verdict.replace('BLOCKED: ', '')}) and scores "
                f"{sc:.0f}/100 as a short. BUT: shorting is not authorised - no short "
                f"rules in the protocol, borrow/squeeze unmeasured. Track, do not sell.")
    return (f"SKIP - {verdict.replace('BLOCKED: ', '')}",
            "Liquid enough to consider, but it fails the long gates and is not a "
            "clean short either. No trade.")
