#!/usr/bin/env python3
"""Options analysis + data-validation engine for the paper-trading overlay.

Standing order 2026-07-29 (Omar): "state of the art, gold standard analysis
and data validation." What that concretely means here:

  ANALYSIS (per contract)
  - Black-Scholes delta/theta computed from the market's own implied vol -
    replaces the moneyness eyeballing used on night one. No dividend
    adjustment (labeled; ~2% yield names skew delta slightly high).
  - IV vs realized movement (IV / 20d and 60d historical vol): the price of
    the option relative to how much the stock ACTUALLY moves. Buying premium
    at IV >> realized is paying for movement that historically doesn't happen.
  - Expected move to expiry (S * IV * sqrt(T)) vs the move the trade NEEDS:
    breakeven at expiry, and the underlying move required for the +100%
    premium target (BS-repriced at the time-exit date, same IV).
  - Theta burden: % of premium that bleeds per week if the stock sits still.

  VALIDATION (every quote, before it may enter the ledger)
  - market not crossed (bid < ask), bid > 0, mid >= intrinsic (stale-quote
    tell), IV in a plausible band, quote from the current session,
    cross-source spot check (chain's implied spot vs the scan's close).
  - Every check logged PASS/FLAG/REJECT with reasons - a REJECT price never
    becomes an entry or a mark.

  GATES (documented in research/options-paper-ledger.json rules)
  - BS delta in 0.60-0.75 band | spread <=10% pass, 10-15% FLAG, >15% REJECT
  - OI >= 100 hard | IV/RV20 <= 1.4 pass, 1.4-1.8 FLAG (paying up), > 1.8
    REJECT unless a flagged catalyst justifies it
  - breakeven move must sit inside the expected move to expiry

  IV HISTORY (--collect-iv): appends today's ATM IV per symbol to
  research/iv-history.json. IV *rank* (today's IV vs its own past year) is the
  real gold-standard entry filter, but it needs history we don't have yet -
  this starts the archive; the rank column stays honest ("n/a, collecting")
  until ~60 sessions accumulate. Do not fake it from proxies.

Usage:
  python scripts/options_analysis.py --analyze SYM DIR [SYM DIR ...]
  python scripts/options_analysis.py --ledger        # analyze open ledger trades
  python scripts/options_analysis.py --collect-iv    # append today's ATM IVs
"""
import argparse
import datetime as dt
import json
import math
import os
import sys

import numpy as np
import yfinance as yf

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(REPO, "research", "options-paper-ledger.json")
IV_HIST = os.path.join(REPO, "research", "iv-history.json")
RISK_FREE = 0.04  # ~13wk bill zone under a 3.50-3.75% funds rate; constant, labeled


# ------------------------------------------------------------ Black-Scholes ---
def _n(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _phi(x):
    return math.exp(-x * x / 2) / math.sqrt(2 * math.pi)


def bs_price(S, K, T, iv, kind, r=RISK_FREE):
    if T <= 0 or iv <= 0:
        intr = max(S - K, 0) if kind == "CALL" else max(K - S, 0)
        return intr
    d1 = (math.log(S / K) + (r + iv * iv / 2) * T) / (iv * math.sqrt(T))
    d2 = d1 - iv * math.sqrt(T)
    if kind == "CALL":
        return S * _n(d1) - K * math.exp(-r * T) * _n(d2)
    return K * math.exp(-r * T) * _n(-d2) - S * _n(-d1)


def bs_greeks(S, K, T, iv, kind, r=RISK_FREE):
    """Returns (delta, theta_per_day)."""
    d1 = (math.log(S / K) + (r + iv * iv / 2) * T) / (iv * math.sqrt(T))
    d2 = d1 - iv * math.sqrt(T)
    delta = _n(d1) if kind == "CALL" else _n(d1) - 1
    core = -S * _phi(d1) * iv / (2 * math.sqrt(T))
    if kind == "CALL":
        theta = core - r * K * math.exp(-r * T) * _n(d2)
    else:
        theta = core + r * K * math.exp(-r * T) * _n(-d2)
    return delta, theta / 365.0


def implied_move_for_double(S, K, T_entry, T_exit, iv, kind, entry_premium):
    """Underlying move (%) needed for the premium to double by the time-exit
    date, repriced with Black-Scholes at the same IV. Bisection on spot."""
    target = 2 * entry_premium
    lo, hi = (S, S * 2.0) if kind == "CALL" else (S * 0.4, S)
    for _ in range(60):
        mid = (lo + hi) / 2
        v = bs_price(mid, K, T_exit, iv, kind)
        if kind == "CALL":
            lo, hi = (mid, hi) if v < target else (lo, mid)
        else:
            lo, hi = (lo, mid) if v < target else (mid, hi)
    spot_needed = (lo + hi) / 2
    return (spot_needed / S - 1) * 100


# ------------------------------------------------------------- market data ---
def realized_vol(sym, sessions):
    h = yf.Ticker(sym).history(period="6mo", auto_adjust=True)
    if h.empty or len(h) < sessions + 2:
        return None, None
    r = np.log(h.Close / h.Close.shift(1)).dropna()
    rv = float(r.tail(sessions).std() * math.sqrt(252))
    return rv, float(h.Close.iloc[-1])


def chain_row(sym, expiry, strike, kind):
    t = yf.Ticker(sym)
    if expiry not in t.options:
        return None
    ch = t.option_chain(expiry)
    df = ch.calls if kind == "CALL" else ch.puts
    row = df[df.strike == strike]
    return None if row.empty else row.iloc[0]


# ---------------------------------------------------------------- readiness ---
_SPY_CACHE = {}


def _spy_hist():
    if "h" not in _SPY_CACHE:
        _SPY_CACHE["h"] = yf.Ticker("SPY").history(period="1y", auto_adjust=True)
    return _SPY_CACHE["h"]


def readiness(sym, kind):
    """Is the stock POISED to move soon in the trade's direction? Five
    direction-aware components, 0-20 points each, composite 0-100.

    UNCALIBRATED (2026-07-29): built on the standard imminence toolkit
    (volatility compression, trigger proximity, OBV accumulation, MACD
    inflection, relative strength). Our own studies killed two timing myths
    already (DI margin and ADX at pick predict nothing), so this score RANKS
    candidates and is graded in the Friday reviews - it does not gate/veto
    until the data earns it that power.
    """
    h = yf.Ticker(sym).history(period="1y", auto_adjust=True)
    if h.empty or len(h) < 130:
        return {"score": None, "note": "insufficient history (<130 sessions)"}
    c, hi, lo, vol = h.Close, h.High, h.Low, h.Volume
    up = kind == "CALL"
    notes, pts = [], {}

    # 1. volatility compression - BB(20,2) width percentile vs trailing 120
    sma, sd = c.rolling(20).mean(), c.rolling(20).std()
    width = (4 * sd / sma).dropna()
    w120 = width.tail(120)
    pctile = float((w120 <= w120.iloc[-1]).mean() * 100)
    pts["squeeze"] = 20 if pctile <= 10 else 15 if pctile <= 25 else 8 if pctile <= 50 else 0
    # TTM squeeze: BB inside Keltner (EMA20 +/- 1.5*ATR14)
    tr = np.maximum(hi - lo, np.maximum(abs(hi - c.shift(1)), abs(lo - c.shift(1))))
    atr = tr.ewm(alpha=1 / 14, adjust=False).mean()
    ema20 = c.ewm(span=20, adjust=False).mean()
    sq_on = bool((sma.iloc[-1] + 2 * sd.iloc[-1] < ema20.iloc[-1] + 1.5 * atr.iloc[-1])
                 and (sma.iloc[-1] - 2 * sd.iloc[-1] > ema20.iloc[-1] - 1.5 * atr.iloc[-1]))
    notes.append(f"band width in the {pctile:.0f}th percentile of the last 120 "
                 f"sessions{' + TTM squeeze ON (bands inside Keltner)' if sq_on else ''}")

    # 2. proximity to the trigger level (20-day extreme in trade direction)
    if up:
        dist = float((hi.tail(20).max() - c.iloc[-1]) / c.iloc[-1] * 100)
        lbl = "below the 20-day high"
    else:
        dist = float((c.iloc[-1] - lo.tail(20).min()) / c.iloc[-1] * 100)
        lbl = "above the 20-day low"
    pts["trigger"] = 20 if dist <= 1 else 12 if dist <= 3 else 6 if dist <= 5 else 0
    notes.append(f"{dist:.1f}% {lbl}")

    # 3. volume accumulation/distribution - OBV extreme + 20d slope, direction-aware
    obv = (np.sign(c.diff()).fillna(0) * vol).cumsum()
    o20 = obv.tail(20)
    at_ext = bool(o20.iloc[-1] >= o20.max()) if up else bool(o20.iloc[-1] <= o20.min())
    slope_dir = bool((o20.iloc[-1] - o20.iloc[0]) > 0) == up
    pts["volume"] = 20 if at_ext else 10 if slope_dir else 0
    notes.append("volume flow at a fresh 20-day extreme in trade direction"
                 if at_ext else ("volume flow leaning with the trade" if slope_dir
                                 else "volume flow NOT confirming"))

    # 4. momentum inflection - MACD(12,26,9) histogram slope + sign
    macd = c.ewm(span=12, adjust=False).mean() - c.ewm(span=26, adjust=False).mean()
    hist = macd - macd.ewm(span=9, adjust=False).mean()
    slope_ok = bool((hist.iloc[-1] - hist.iloc[-3]) > 0) == up
    sign_ok = bool(hist.iloc[-1] > 0) == up
    pts["momentum"] = (10 if slope_ok else 0) + (10 if sign_ok else 0)
    notes.append(f"momentum {'turning with' if slope_ok else 'turning against'} "
                 f"the trade, {'already' if sign_ok else 'not yet'} on its side")

    # 5. relative strength vs SPY - ratio near its 60-day extreme in direction
    spy = _spy_hist().Close.reindex(c.index).ffill()
    ratio = (c / spy).dropna().tail(60)
    if up:
        near = float(ratio.iloc[-1] / ratio.max())
        pts["rel_strength"] = 20 if near >= 0.98 else 10 if near >= 0.95 else 0
    else:
        near = float(ratio.iloc[-1] / ratio.min())
        pts["rel_strength"] = 20 if near <= 1.02 else 10 if near <= 1.05 else 0
    notes.append("beating the market at a 60-day extreme" if pts["rel_strength"] == 20
                 else ("near its relative extreme" if pts["rel_strength"] == 10
                       else "relative strength not at an extreme"))

    return {"score": int(sum(pts.values())), "components": pts,
            "squeeze_pctile": round(pctile), "squeeze_on": sq_on,
            "dist_to_trigger_pct": round(dist, 1),
            "label": "UNCALIBRATED - ranks candidates, does not veto",
            "notes": notes}


# --------------------------------------------------------------- validation ---
def validate_quote(row, spot_scan, spot_yf, strike, kind, session_date):
    """Battery of data-quality checks. Returns (verdict, [reasons])."""
    flags, rejects = [], []
    bid, ask = float(row.bid or 0), float(row.ask or 0)
    mid = (bid + ask) / 2 if bid and ask else None
    iv = float(row.impliedVolatility or 0)
    if bid <= 0:
        rejects.append("no live bid - quote unusable (bid=0)")
    if bid and ask and bid >= ask:
        rejects.append(f"crossed market (bid {bid} >= ask {ask}) - stale book")
    spot = spot_yf or spot_scan
    intr = max(spot - strike, 0) if kind == "CALL" else max(strike - spot, 0)
    if mid and intr and mid < intr * 0.98:
        rejects.append(f"mid {mid:.2f} below intrinsic {intr:.2f} - stale/bad quote")
    if not 0.05 <= iv <= 2.5:
        rejects.append(f"implied vol {iv:.0%} outside plausible band (5%-250%)")
    if mid and ask and bid:
        spr = (ask - bid) / mid * 100
        if spr > 15:
            rejects.append(f"spread {spr:.1f}% > 15% - mid fill not realistic")
        elif spr > 10:
            flags.append(f"spread {spr:.1f}% (10-15%) - watch fill quality")
    oi = int(row.openInterest) if row.openInterest == row.openInterest else 0
    if oi < 100:
        rejects.append(f"open interest {oi} < 100")
    if spot_scan and spot_yf and abs(spot_yf / spot_scan - 1) > 0.005:
        flags.append(f"cross-source spot gap {abs(spot_yf/spot_scan-1)*100:.2f}% "
                     f"(scan {spot_scan} vs yf {spot_yf:.2f}) - sources disagree")
    lt = getattr(row, "lastTradeDate", None)
    if lt is not None and str(lt)[:10] < session_date:
        flags.append(f"last trade {str(lt)[:10]} (before this session) - "
                     "quote is book-only, no prints today")
    verdict = "REJECT" if rejects else ("FLAG" if flags else "PASS")
    return verdict, rejects + flags


# ----------------------------------------------------------------- analysis ---
def analyze(sym, kind, expiry, strike, contracts=None, entry=None,
            spot_scan=None, time_exit=None, session_date=None):
    session_date = session_date or dt.date.today().isoformat()
    rv20, spot_yf = realized_vol(sym, 20)
    rv60, _ = realized_vol(sym, 60)
    row = chain_row(sym, expiry, strike, kind)
    if row is None:
        return {"sym": sym, "error": f"no {kind} {strike} {expiry} in chain"}
    spot = spot_yf or spot_scan
    bid, ask = float(row.bid or 0), float(row.ask or 0)
    mid = round((bid + ask) / 2, 2) if bid and ask else None
    iv = float(row.impliedVolatility or 0)
    today = dt.date.fromisoformat(session_date)
    T = max(( dt.date.fromisoformat(expiry) - today).days, 1) / 365.0
    T_exit = (max((dt.date.fromisoformat(time_exit) - today).days, 1) / 365.0
              if time_exit else T)
    delta, theta_d = bs_greeks(spot, strike, T, iv, kind)
    prem = entry or mid
    exp_move = iv * math.sqrt(T) * 100                       # % expected by expiry
    be_spot = strike + prem if kind == "CALL" else strike - prem
    be_move = (be_spot / spot - 1) * 100
    dbl_move = (implied_move_for_double(spot, strike, T, T_exit, iv, kind, prem)
                if prem else None)
    verdict, reasons = validate_quote(row, spot_scan, spot_yf, strike, kind,
                                      session_date)
    ivrv = round(iv / rv20, 2) if rv20 else None
    gates = []
    if not 0.60 <= abs(delta) <= 0.75:
        gates.append(f"delta {delta:+.2f} outside 0.60-0.75 band")
    if ivrv and ivrv > 1.8:
        gates.append(f"IV/RV20 {ivrv} > 1.8 - paying far above realized movement")
    elif ivrv and ivrv > 1.4:
        gates.append(f"IV/RV20 {ivrv} (1.4-1.8) - paying up vs realized, FLAG")
    if abs(be_move) > exp_move:
        gates.append(f"breakeven needs {be_move:+.1f}% but expected move to "
                     f"expiry is only ±{exp_move:.1f}%")
    out = {
        "sym": sym, "kind": kind, "expiry": expiry, "strike": strike,
        "session": session_date, "spot": round(spot, 2),
        "bid": bid, "ask": ask, "mid": mid,
        "iv_pct": round(iv * 100, 1),
        "rv20_pct": round(rv20 * 100, 1) if rv20 else None,
        "rv60_pct": round(rv60 * 100, 1) if rv60 else None,
        "iv_over_rv20": ivrv,
        "bs_delta": round(delta, 2),
        "theta_day": round(theta_d, 3),
        "theta_week_pct_of_prem": (round(-theta_d * 7 / prem * 100, 1)
                                   if prem else None),
        "oi": int(row.openInterest) if row.openInterest == row.openInterest else 0,
        "spread_pct": round((ask - bid) / mid * 100, 1) if mid else None,
        "expected_move_to_expiry_pct": round(exp_move, 1),
        "breakeven_move_pct": round(be_move, 1),
        "move_needed_for_double_pct": round(dbl_move, 1) if dbl_move else None,
        "iv_rank": None,  # honest n/a until iv-history has ~60 sessions
        "validation": verdict, "reasons": reasons + gates,
    }
    rd = readiness(sym, kind)
    out["readiness"] = rd
    # PRIME SETUP: compression + cheap premium together attack both enemies of
    # long options (time decay while waiting, and overpaying for movement).
    out["prime_setup"] = bool(rd.get("squeeze_pctile") is not None
                              and rd["squeeze_pctile"] <= 25
                              and ivrv is not None and ivrv <= 1.2)
    if out["prime_setup"]:
        out["reasons"] = ["PRIME SETUP: volatility compressed (squeeze "
                          f"{rd['squeeze_pctile']}th pctile) AND premium cheap "
                          f"vs realized (IV/RV {ivrv}) - the textbook long-"
                          "options pairing"] + out["reasons"]
    return out


def market_regime():
    """SPY vs its own 200-day: the one filter our backtests showed IS the
    edge (HQ Swing study). PASS = above a rising 200-day; REPAIR = below it;
    DEEP-FAIL = >10% below. Overlay rule: REPAIR blocks new CALLS unless the
    pick is a PRIME SETUP; DEEP-FAIL blocks new calls entirely (puts allowed,
    flagged as late-trend)."""
    if "regime" in _SPY_CACHE:
        return _SPY_CACHE["regime"]
    h = _spy_hist().Close
    sma200 = h.rolling(200).mean()
    spy, ma = float(h.iloc[-1]), float(sma200.iloc[-1])
    rising = bool(ma > float(sma200.iloc[-21]))
    if spy < ma * 0.90:
        state = "DEEP-FAIL"
    elif spy < ma or not rising:
        state = "REPAIR"
    else:
        state = "PASS"
    out = {"state": state, "spy": round(spy, 2), "sma200": round(ma, 2),
           "sma200_rising": rising,
           "spy_vs_200d_pct": round((spy / ma - 1) * 100, 1)}
    _SPY_CACHE["regime"] = out
    return out


def macro_blackout(session_date=None):
    """Is the NEXT session (the morning fill day) the day before or day of a
    macro binary (Fed decision, CPI, jobs report)? Known events from
    research/macro-calendar-2026H2.json; jobs report computed as the first
    Friday of each month. Blocks NEW entries only - open trades just get a
    heads-up."""
    d = dt.date.fromisoformat(session_date) if session_date else dt.date.today()
    fill = d + dt.timedelta(days=1)
    while fill.weekday() >= 5:
        fill += dt.timedelta(days=1)
    watch = {fill, fill + dt.timedelta(days=1)}
    hits = []
    cal = os.path.join(REPO, "research", "macro-calendar-2026H2.json")
    if os.path.exists(cal):
        for e in json.load(open(cal, encoding="utf-8"))["events"]:
            if dt.date.fromisoformat(e["date"]) in watch:
                hits.append(f"{e['event']} {e['date']} ({e['confidence']})")
    for w in watch:  # first-Friday jobs report
        if w.weekday() == 4 and w.day <= 7:
            hits.append(f"Jobs report (NFP) {w.isoformat()} (computed)")
    return {"blocked": bool(hits), "fill_day": fill.isoformat(), "events": hits}


def entry_gates(kind, prime_setup, session_date=None):
    """Overlay-level gates for NEW picks (not applied to open positions):
    market regime + macro-event blackout. Returns list of blocking reasons."""
    blocks = []
    reg = market_regime()
    if kind == "CALL" and reg["state"] == "DEEP-FAIL":
        blocks.append(f"regime {reg['state']} (SPY {reg['spy_vs_200d_pct']:+.1f}% "
                      "vs 200-day) - no new calls in a broken tape")
    elif kind == "CALL" and reg["state"] == "REPAIR" and not prime_setup:
        blocks.append(f"regime {reg['state']} - new calls need a PRIME SETUP")
    bo = macro_blackout(session_date)
    if bo["blocked"]:
        blocks.append("macro blackout - " + "; ".join(bo["events"]) +
                      " sits on/next to the fill day; do not open into a coin-flip")
    return blocks, reg, bo


def scorecard():
    """Friday-review expectancy math + pre-registered kill criteria."""
    led = json.load(open(LEDGER, encoding="utf-8"))
    closed = [t for t in led["trades"] if t.get("close")
              and t.get("status") != "VOIDED"]
    opens = [t for t in led["trades"] if not t.get("close")
             and t.get("status") not in ("VOIDED", "PLANNED")]
    def pnl(t, prem):
        return (prem - t["entry_premium"]) * 100 * t["contracts"]
    banked = [pnl(t, t["close"]["premium"]) for t in closed]
    marking = [pnl(t, t["mark_premium"]) for t in opens if t.get("mark_premium")]
    wins = [p for p in banked if p > 0]
    losses = [p for p in banked if p <= 0]
    exp = (sum(banked) / len(banked)) if banked else None
    total = sum(banked) + sum(marking)
    out = {"closed": len(closed), "wins": len(wins),
           "win_pct": round(len(wins) / len(closed) * 100) if closed else None,
           "avg_win": round(sum(wins) / len(wins)) if wins else None,
           "avg_loss": round(sum(losses) / len(losses)) if losses else None,
           "expectancy_per_trade": round(exp) if exp is not None else None,
           "banked": round(sum(banked)), "open_marking": round(sum(marking)),
           "total_paper_pnl": round(total), "verdicts": []}
    # pre-registered kill criteria (research/options-exit-policy-preregistration.md)
    if len(closed) >= 30 and exp is not None and exp < 0:
        out["verdicts"].append("KILL CRITERIA MET: 30+ closed trades with "
                              "negative expectancy - overlay STOPS pending redesign")
    if total <= -12500:
        out["verdicts"].append("DRAWDOWN BREAKER: paper P&L below -$12,500 "
                              "(five max losses) - pause + red-team before any new pick")
    if not out["verdicts"]:
        out["verdicts"].append(f"experiment continues ({len(closed)}/30 closed "
                               "trades toward the pre-registered verdict)")
    return out


def select_contract(sym, kind, session_date=None):
    """EOD selection: find the compliant contract for a candidate name.
    Expiry 45-90 DTE (prefer monthlies = deepest OI), strike whose BS delta
    (from that strike's own market IV) lands nearest 0.67 inside the
    0.60-0.75 band, then full analysis + validation on the winner."""
    session_date = session_date or dt.date.today().isoformat()
    today = dt.date.fromisoformat(session_date)
    t = yf.Ticker(sym)
    _, spot = realized_vol(sym, 20)
    if not spot:
        return {"sym": sym, "error": "no price history"}
    exps = [e for e in t.options
            if 45 <= (dt.date.fromisoformat(e) - today).days <= 90]
    if not exps:
        return {"sym": sym, "error": "no expiry in the 45-90 day window"}
    # third-Friday monthlies have the deepest open interest; prefer them
    monthly = [e for e in exps
               if 15 <= dt.date.fromisoformat(e).day <= 21
               and dt.date.fromisoformat(e).weekday() == 4]
    expiry = (monthly or exps)[0]
    T = (dt.date.fromisoformat(expiry) - today).days / 365.0
    ch = t.option_chain(expiry)
    df = ch.calls if kind == "CALL" else ch.puts
    best, best_gap = None, 9e9
    for _, r in df.iterrows():
        iv = float(r.impliedVolatility or 0)
        if not 0.05 <= iv <= 2.5 or not r.bid:
            continue
        d, _th = bs_greeks(spot, float(r.strike), T, iv, kind)
        if 0.60 <= abs(d) <= 0.75 and abs(abs(d) - 0.67) < best_gap:
            best, best_gap = float(r.strike), abs(abs(d) - 0.67)
    if best is None:
        return {"sym": sym, "error": f"no strike with BS delta 0.60-0.75 and a "
                                     f"live bid on {expiry} - do not force"}
    res = analyze(sym, kind, expiry, best, session_date=session_date)
    blocks, reg, bo = entry_gates(kind, res.get("prime_setup"), session_date)
    res["market_regime"] = reg["state"]
    res["macro_fill_day"] = bo["fill_day"]
    if blocks:
        res["validation"] = "REJECT"
        res["reasons"] = blocks + res.get("reasons", [])
    return res


# ------------------------------------------------------------------ drivers ---
def run_ledger(write=True):
    led = json.load(open(LEDGER, encoding="utf-8"))
    out = []
    for t in led["trades"]:
        if t.get("close") or t.get("status") == "VOIDED":
            continue
        a = analyze(t["sym"], t["direction"], t["expiry"], t["strike"],
                    t.get("contracts"), t.get("entry_premium") or t.get("planned_premium"),
                    t.get("entry_underlying"), t.get("time_exit"))
        t["analysis"] = a
        out.append(a)
        print(json.dumps(a, indent=1))
    if write:
        json.dump(led, open(LEDGER, "w", encoding="utf-8"), indent=2)
        print(f"\nanalysis blocks written into {LEDGER}")
    return out


def collect_iv():
    """Append today's ~ATM IV per symbol (open trades + gate list arg) to the
    history file that will eventually power a real IV-rank entry filter."""
    led = json.load(open(LEDGER, encoding="utf-8"))
    syms = sorted({t["sym"] for t in led["trades"] if not t.get("close")}
                  | set(sys.argv[2:]))
    hist = json.load(open(IV_HIST, encoding="utf-8")) if os.path.exists(IV_HIST) else {}
    today = dt.date.today().isoformat()
    for s in syms:
        try:
            t = yf.Ticker(s)
            exps = [e for e in t.options
                    if 30 <= (dt.date.fromisoformat(e) - dt.date.today()).days <= 90]
            if not exps:
                continue
            ch = t.option_chain(exps[0]).calls
            spot = float(t.history(period="1d").Close.iloc[-1])
            atm = ch.iloc[(ch.strike - spot).abs().argsort()[:1]]
            iv = float(atm.impliedVolatility.iloc[0])
            hist.setdefault(s, {})[today] = round(iv * 100, 1)
            print(f"{s}: ATM IV {iv:.0%} ({exps[0]})")
        except Exception as e:
            print(f"{s}: collect failed - {e}")
    json.dump(hist, open(IV_HIST, "w", encoding="utf-8"), indent=1)
    print(f"wrote {IV_HIST} ({len(hist)} symbols)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", action="store_true")
    ap.add_argument("--collect-iv", action="store_true")
    ap.add_argument("--analyze", nargs="+", metavar="SYM DIR")
    ap.add_argument("--scorecard", action="store_true")
    ap.add_argument("--gates", action="store_true",
                    help="print tonight's overlay-level regime + macro gates")
    args, _ = ap.parse_known_args()
    if args.scorecard:
        print(json.dumps(scorecard(), indent=1))
    elif args.gates:
        blocks_c, reg, bo = entry_gates("CALL", False)
        blocks_p, _, _ = entry_gates("PUT", False)
        print(json.dumps({"regime": reg, "macro": bo,
                          "new_calls": blocks_c or ["allowed"],
                          "new_puts": blocks_p or ["allowed"]}, indent=1))
    elif args.ledger:
        run_ledger()
    elif args.collect_iv:
        collect_iv()
    elif args.analyze:
        pairs = list(zip(args.analyze[::2], args.analyze[1::2]))
        for sym, d in pairs:
            print(json.dumps(select_contract(sym, d.upper()), indent=1))
