"""Markman alert screener — the decision card (built 2026-08-03, pre-subscription).

For each incoming Markman options alert, prints in seconds:
  1. THEIR contract, verified against the live chain (real? liquid? what
     you'd actually pay) + earnings inside their typical ~18-day hold.
  2. OUR translation - same ticker & direction, our 45-90 DTE delta .60-.75
     contract, priced side by side ("take their ideas, never their contracts",
     per the 7/31 audit: 0/44 of their recs passed our structure rules).
  3. The stock's own posture: regime vs 200-day, ADX/DI, direction-aware
     readiness, rested-leader tag if current.
  4. The DRAFT take/skip line. UNCALIBRATED - the line is hypothesis until the
     pre-registered 30-alert dual-cohort trial grades it
     (research/markman-trial-preregistration.md). Until frozen+graded, this
     screener INFORMS; it does not decide.

Usage:
  python scripts/markman_screener.py SYM CALL|PUT THEIR_STRIKE THEIR_EXPIRY [their_prem]
  e.g. python scripts/markman_screener.py CAKE CALL 105 2026-08-21 3.50

Every screened alert is appended to research/markman-trial-ledger.json with
its verdict and full card, so takes AND skips both get graded on Fridays.
"""
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import pandas as pd
import yfinance as yf
from options_analysis import (analyze, chain_row, readiness, realized_vol,
                              select_contract, validate_quote)

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(REPO, "research", "markman-trial-ledger.json")


def _og_chandelier_dir(df, ce_len=1, ce_mult=2.0):
    """O.G Chandelier daily mode on Heikin Ashi - copied from og_shadow.py
    (CE 1/2, Everget ratchet) so importing that module's side effects is
    avoided. Returns the direction array (+1 BUY / -1 SELL)."""
    ha = pd.DataFrame(index=df.index)
    ha["close"] = (df["Open"] + df["High"] + df["Low"] + df["Close"]) / 4
    op = np.empty(len(df))
    op[0] = (df["Open"].iloc[0] + df["Close"].iloc[0]) / 2
    hc = ha["close"].to_numpy()
    for i in range(1, len(df)):
        op[i] = (op[i - 1] + hc[i - 1]) / 2
    ha["open"] = op
    ha["high"] = np.maximum.reduce([df["High"].to_numpy(), op, hc])
    ha["low"] = np.minimum.reduce([df["Low"].to_numpy(), op, hc])
    prev_close = ha["close"].shift(1)
    tr = pd.concat([ha["high"] - ha["low"], (ha["high"] - prev_close).abs(),
                    (ha["low"] - prev_close).abs()], axis=1).max(axis=1)
    a = ce_mult * tr.ewm(alpha=1 / ce_len, adjust=False).mean()
    hi = ha["high"].rolling(ce_len).max()
    lo = ha["low"].rolling(ce_len).min()
    lsb, ssb = (hi - a).to_numpy(), (lo + a).to_numpy()
    c = ha["close"].to_numpy()
    n = len(c)
    ls, ss = lsb.copy(), ssb.copy()
    dirn = np.ones(n, dtype=int)
    for i in range(1, n):
        ls[i] = max(lsb[i], ls[i - 1]) if c[i - 1] > ls[i - 1] else lsb[i]
        ss[i] = min(ssb[i], ss[i - 1]) if c[i - 1] < ss[i - 1] else ssb[i]
        if c[i] > ss[i - 1]:
            dirn[i] = 1
        elif c[i] < ls[i - 1]:
            dirn[i] = -1
        else:
            dirn[i] = dirn[i - 1]
    return dirn


def stock_posture(sym, kind):
    h = yf.Ticker(sym).history(period="2y", auto_adjust=True)
    c, hi, lo = h.Close, h.High, h.Low
    out = {}
    if len(c) >= 200:
        sma200 = c.rolling(200).mean()
        out["ext_vs_200d_pct"] = round(float(c.iloc[-1] / sma200.iloc[-1] - 1) * 100, 1)
        out["sma200_rising"] = bool(sma200.iloc[-1] > sma200.iloc[-21])
    up, dn = hi.diff(), -lo.diff()
    plus = pd.Series(np.where((up > dn) & (up > 0), up, 0.0), index=h.index)
    minus = pd.Series(np.where((dn > up) & (dn > 0), dn, 0.0), index=h.index)
    tr = np.maximum(hi - lo, np.maximum(abs(hi - c.shift(1)), abs(lo - c.shift(1))))
    atr = tr.ewm(alpha=1 / 14, adjust=False).mean()
    pdi = 100 * plus.ewm(alpha=1 / 14, adjust=False).mean() / atr
    mdi = 100 * minus.ewm(alpha=1 / 14, adjust=False).mean() / atr
    dx = 100 * (pdi - mdi).abs() / (pdi + mdi)
    out["adx"] = round(float(dx.ewm(alpha=1 / 14, adjust=False).mean().iloc[-1]), 1)
    out["di_margin"] = round(float(pdi.iloc[-1] - mdi.iloc[-1]), 1)
    out["readiness"] = readiness(sym, kind, hist=h)
    try:
        rc = json.load(open(os.path.join(REPO, "research",
                                         "rest-continuation-ledger.json")))
        dates = sorted({r["date"] for r in rc["entries"]})
        out["rested_leader"] = any(r["sym"] == sym and r["member"]
                                   and r["date"] == dates[-1]
                                   for r in rc["entries"]) if dates else False
    except Exception:
        out["rested_leader"] = None
    return out


def earnings_within(sym, days):
    try:
        cal = yf.Ticker(sym).calendar
        ed = cal.get("Earnings Date")
        if ed:
            d = ed[0] if isinstance(ed, (list, tuple)) else ed
            delta = (pd.Timestamp(d) - pd.Timestamp.now()).days
            return {"date": str(d), "days_away": delta, "inside": 0 <= delta <= days}
    except Exception:
        pass
    return {"date": None, "days_away": None, "inside": None}


def screen(sym, kind, strike, expiry, their_prem=None):
    card = {"screened_at": datetime.datetime.now().isoformat(timespec="minutes"),
            "alert": {"sym": sym, "dir": kind, "their_strike": strike,
                      "their_expiry": expiry, "their_stated_prem": their_prem}}

    dte = (pd.Timestamp(expiry) - pd.Timestamp.now()).days
    card["their_contract"] = {"dte": dte}
    try:
        a = analyze(sym, kind, expiry, strike)
        card["their_contract"].update(a)
    except Exception as e:
        card["their_contract"]["error"] = str(e)[:200]
    card["their_hold_earnings"] = earnings_within(sym, min(dte, 21))

    try:
        ours = select_contract(sym, kind)
        card["our_translation"] = ours
    except Exception as e:
        card["our_translation"] = {"error": str(e)[:200]}

    card["stock"] = stock_posture(sym, kind)

    # ---- DRAFT take/skip line (freeze via preregistration before 1st live alert)
    tc = card["their_contract"]
    reasons, take = [], True
    if tc.get("validation") == "REJECT" or tc.get("error"):
        take = False; reasons.append("their contract fails the live-chain reality check")
    if card["their_hold_earnings"].get("inside"):
        take = False; reasons.append(
            f"earnings {card['their_hold_earnings']['date']} inside the hold window "
            "(the ONE gate with observed teeth in the 2021 audit)")
    ext = card["stock"].get("ext_vs_200d_pct")
    if ext is not None and ext < -10:
        take = False; reasons.append("stock regime DEEP-FAIL (>10% below 200-day)")
    # Finding #2 of the 8/3 calibration (Omar's emphasis): cheap OTM tickets
    # are where their subscribers die - delta>=0.45 entries went 14W-3L ~+38%,
    # sub-0.45/OTM went 8W-8L ~-25%, every near-total wipeout was OTM.
    delta = tc.get("bs_delta")
    spot = tc.get("spot")
    otm_pct = None
    if spot:
        otm_pct = ((strike / spot - 1) * 100 if kind == "CALL"
                   else (1 - strike / spot) * 100)
    if delta is not None and abs(delta) < 0.45:
        take = False; reasons.append(
            f"delta {delta:+.2f} below the 0.45 floor - the OTM-lotto profile "
            "(calibration: 8W-8L ~-25%, every wipeout was OTM)")
    elif otm_pct is not None and otm_pct > 10:
        take = False; reasons.append(
            f"strike {otm_pct:.0f}% out of the money (>10% floor)")
    if isinstance(card["our_translation"], dict) and card["our_translation"].get("error"):
        take = False; reasons.append("no compliant 45-90 DTE delta .60-.75 translation exists")
    # Line 6 (8/3 alignment study): direction must not contradict the O.G
    # Chandelier daily mode. Aligned archive trades: 18W-5L +22%;
    # contradicting: 4W-6L -26% - 4 of their 8 wipeouts were contra entries.
    try:
        # inlined from og_shadow (importing it triggers its module-level
        # grading run, which needs repo-cwd files - learned 8/3)
        hh = yf.Ticker(sym).history(period="2y", auto_adjust=True)
        hh = hh.rename(columns=str.capitalize)
        dirn = _og_chandelier_dir(hh)
        ce_mode = "BUY" if int(dirn[-1]) == 1 else "SELL"
        card["stock"]["og_chandelier_mode"] = ce_mode + " (shadow port ~84% chart fidelity)"
        if (kind == "CALL") != (ce_mode == "BUY"):
            take = False; reasons.append(
                f"contradicts the O.G Chandelier - underlying is in {ce_mode} mode "
                "(alignment study: contra entries 4W-6L, -26% avg)")
    except Exception as e:
        card["stock"]["og_chandelier_mode"] = "unavailable: " + str(e)[:60]
    card["draft_verdict"] = {
        "line": "TAKE (as OUR translation, paper)" if take else "SKIP",
        "reasons": reasons or ["passes all draft checks"],
        "label": "DRAFT/UNCALIBRATED - trial grades this line; it does not decide yet"}

    led = (json.load(open(LEDGER)) if os.path.exists(LEDGER)
           else {"kind": "markman-30-alert-trial", "preregistration":
                 "research/markman-trial-preregistration.md", "alerts": []})
    led["alerts"].append(card)
    json.dump(led, open(LEDGER, "w"), indent=1, default=str)
    print(json.dumps(card, indent=1, default=str))
    print(f"\nlogged as trial alert #{len(led['alerts'])} -> {os.path.basename(LEDGER)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 4:
        sys.exit(__doc__)
    screen(args[0].upper(), args[1].upper(), float(args[2]), args[3],
           float(args[4]) if len(args) > 4 else None)
