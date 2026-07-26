"""Maintain the 20% trailing-ratchet exit line on the real open book.

Exit rule (Omar-approved 2026-07-25, from the pre-registered exit-redesign
test): exit line = max(initial stop, 0.8 x highest CLOSE since entry). The
ratchet only matters once 0.8 x high rises ABOVE the stop (~+17-22% on the
current book); until then the stop alert already guards a higher line and
this script does nothing but track the high.

Reads  watchlists/open-book.json      (positions; keep in sync with fills)
Writes watchlists/ratchet-actions.json  ONLY when a TV alert must be wired
       or raised - consumed and deleted by scripts/ratchet_alerts.mjs, which
       does the actual TradingView REST work in page context via CDP.

Highest close is recomputed from scratch every run (daily bars since entry),
so a missed night self-heals. The ratchet level only ever moves UP.

Usage: python scripts/ratchet_watch.py          (runs in EOD chain step 4)
"""
import json
import os
import sys

BOOK = os.path.join("watchlists", "open-book.json")
ACTIONS = os.path.join("watchlists", "ratchet-actions.json")
MIN_STEP = 1.001          # re-wire only when the level rises > 0.1%


def ratchet_level(high_close, stop, pct):
    """The tradeable ratchet line, or None while the stop still governs."""
    if high_close is None:
        return None
    lvl = (1.0 - pct) * high_close
    return round(lvl, 2) if lvl > stop * MIN_STEP else None


def build_actions(book, closes_by_sym):
    """Pure: update highs in-place, return the alert actions needed."""
    actions = []
    for pos in book["positions"]:
        closes = closes_by_sym.get(pos["sym"], [])
        if closes:
            pos["high_close"] = round(max(closes), 4)
        lvl = ratchet_level(pos["high_close"], pos["stop"], book["ratchet_pct"])
        if lvl is None:
            continue
        cur = pos.get("ratchet_alert") or {}
        if cur.get("level") and lvl <= cur["level"] * MIN_STEP:
            continue                      # ratchet never moves down or sideways
        msg = (f"{pos['sym']} {lvl:.2f} = 20% RATCHET exit line "
               f"(0.8 x highest close {pos['high_close']:.2f}). "
               f"LONG {pos['shares']} @ {pos['entry']:.2f}. "
               f"FIRE = gave back 20% from the peak -> EXIT the full position "
               f"per the 7/25 exit rule. This line only moves up (rewired nightly)."
               + (f" NOTE: {pos['notes']}" if pos.get("notes") else ""))
        actions.append({"sym": pos["sym"], "level": lvl,
                        "high_close": pos["high_close"],
                        "delete_id": cur.get("id"), "message": msg})
    return actions


def main():
    book = json.load(open(BOOK))
    if not book["positions"]:
        if os.path.exists(ACTIONS):
            os.remove(ACTIONS)
        print("open book is empty - nothing to watch")
        return

    import yfinance as yf
    syms = [p["sym"] for p in book["positions"]]
    earliest = min(p["opened"] for p in book["positions"])
    raw = yf.download(syms, start=earliest, interval="1d", auto_adjust=True,
                      progress=False, group_by="ticker", threads=True)
    closes = {}
    for p in book["positions"]:
        try:
            df = raw[p["sym"]] if len(syms) > 1 else raw
            ser = df["Close"].dropna()
            closes[p["sym"]] = [float(v) for d, v in ser.items()
                                if str(d)[:10] >= p["opened"]]
        except Exception:
            pass
        if not closes.get(p["sym"]):
            print(f"FAILED: no daily closes for {p['sym']} - "
                  f"cannot maintain its ratchet tonight")

    actions = build_actions(book, closes)
    json.dump(book, open(BOOK, "w"), indent=1)

    for p in book["positions"]:
        lvl = ratchet_level(p["high_close"], p["stop"], book["ratchet_pct"])
        state = (f"RATCHET {lvl:.2f} governs" if lvl
                 else f"stop {p['stop']:.2f} still governs")
        print(f"  {p['sym']:5s} entry {p['entry']:8.2f}  high close "
              f"{(p['high_close'] or 0):8.2f}  -> {state}")

    if actions:
        json.dump(actions, open(ACTIONS, "w"), indent=1)
        for a in actions:
            verb = "RAISE" if a["delete_id"] else "WIRE NEW"
            print(f"RATCHET ACTION: {verb} {a['sym']} alert at {a['level']:.2f}")
        print(f"wrote {ACTIONS} - ratchet_alerts.mjs must run next")
    else:
        if os.path.exists(ACTIONS):
            os.remove(ACTIONS)
        print("no alert changes needed")

    if any(p["sym"] not in closes for p in book["positions"]):
        sys.exit(1)                       # fail loud; chain logs a WARNING


if __name__ == "__main__":
    main()
