#!/usr/bin/env python3
"""Daily market structure — the computable half of the Market & Rotation read.

WHY THIS EXISTS (Omar, 2026-07-28): the "1 - Market & Rotation" tab used to be a
breadth count plus the rotation radar's 1W/1M/6M table. That is data, not a read.
He asked for the 7/27 recap's level of detail EVERY day. What made that recap
useful was four things the workbook never computed:

  1. THE DAY'S PATH, not just the close. "Finished flat" hid "opened +0.8%, fell
     1.3%, closed unchanged."
  2. A sector table sorted by TODAY's move, with SPY in it so out/under-performance
     is visible. The radar carries no daily change at all.
  3. CLOSE-WITHIN-RANGE, (close-low)/(high-low) — the tell for who won the last
     hour. On 7/27 energy closed at 12% of its range and oil E&P at 8% (sellers
     never let up) while China internet closed at 78%, and the INDEX closed at 33%
     despite finishing green.
  4. REBOUND vs GIVE-BACK, from 1M against 6M. This is what proves a day was
     "unwinding of winners", not "rotation into a new theme": on 7/27 every leader
     was up on the month but still deep underwater over six (software +6.8/-7.3,
     China +16.2/-25.9) while the worst loser was the biggest 6M winner
     (semis -11.1/+32.1).

Volume vs the 10-day average comes free from the same call and is kept as a
conviction read (SMH traded 2.8x normal on 7/27 - that selling was real).

WHAT THIS DELIBERATELY DOES NOT DO: write the narrative. Naming what the day
actually was is judgement, and a script faking it would be worse than a blank.
The workbook renders a NARRATIVE block that gets written each evening with the
EOD brief. See memory `market-rotation-tab-depth-standard`.

Data: TradingView scanner API (public, no auth, no chart tab needed) - the same
endpoint rotation_radar.py uses, and the UNIVERSE is imported from it so the two
can never drift apart.

Usage: python scripts/market_structure.py [YYYY-MM-DD]
Writes: watchlists/market-structure-<date>.json
Exit:   0 ok, 1 fetch/parse failure (caller treats as non-fatal - the tab
        degrades to the radar table rather than blocking the workbook).
"""
import datetime
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rotation_radar import UNIVERSE  # noqa: E402  single source of truth for the groups

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BENCH = "AMEX:SPY"
COLS = ["name", "close", "open", "high", "low", "change",
        "Perf.W", "Perf.1M", "Perf.3M", "Perf.6M",
        "volume", "average_volume_10d_calc"]


def fetch(tickers):
    body = json.dumps({"symbols": {"tickers": list(tickers)}, "columns": COLS}).encode()
    req = urllib.request.Request(
        "https://scanner.tradingview.com/america/scan", data=body,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())["data"]


def range_pos(close, high, low):
    """Where the close sat inside the day's range, 0-100. None if there was no range."""
    if None in (close, high, low) or high <= low:
        return None
    return round(100.0 * (close - low) / (high - low), 1)


def character(m1, m6):
    """Is this group climbing out of a hole, or handing back a big run?

    The distinction is the whole point: a market where the leaders are REBOUND and
    the losers are GIVE-BACK is unwinding, not rotating.
    """
    if m1 is None or m6 is None:
        return "?"
    if m1 > 0 and m6 < 0:
        return "REBOUND"          # up lately, still underwater - climbing out of a hole
    if m1 < 0 and m6 >= 15:
        return "GIVE-BACK"        # down lately after a big run - handing back gains
    if m1 > 0 and m6 > 0:
        return "LEADING"          # up on both - a real trend
    return "LAGGING"


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    try:
        data = fetch(UNIVERSE.keys())
    except Exception as e:                                    # noqa: BLE001
        print("[market-structure] FAILED to fetch: %s" % e, file=sys.stderr)
        return 1
    if not data:
        print("[market-structure] FAILED: scanner returned no rows", file=sys.stderr)
        return 1

    rows, bench = [], None
    for r in data:
        tk = r["s"]
        v = dict(zip(COLS, r["d"]))
        chg = v.get("change")
        close = v.get("close")
        prev = None
        if close is not None and chg is not None and chg != -100:
            prev = close / (1.0 + chg / 100.0)
        row = {
            "ticker": tk,
            "group": UNIVERSE[tk][0],
            "close": close,
            "prev_close": round(prev, 4) if prev else None,
            "open": v.get("open"),
            "high": v.get("high"),
            "low": v.get("low"),
            "day_pct": round(chg, 2) if chg is not None else None,
            "range_pos": range_pos(close, v.get("high"), v.get("low")),
            "w": v.get("Perf.W"),
            "m1": v.get("Perf.1M"),
            "m3": v.get("Perf.3M"),
            "m6": v.get("Perf.6M"),
            "vol_x": (round(v["volume"] / v["average_volume_10d_calc"], 2)
                      if v.get("volume") and v.get("average_volume_10d_calc") else None),
        }
        row["character"] = character(row["m1"], row["m6"])
        # Keep the UNROUNDED accel for any threshold test. Rounding first then
        # testing >= 8 promoted IGV (true accel 7.986) into the "igniting" count
        # and made this script disagree with rotation_radar.py, which classifies
        # on the raw value. Round for display only.
        if row["m1"] is not None and row["m6"] is not None:
            row["_accel_raw"] = row["m1"] - row["m6"] / 6.0
            row["accel"] = round(row["_accel_raw"], 1)
        else:
            row["_accel_raw"] = None
            row["accel"] = None
        if tk == BENCH:
            bench = row
        rows.append(row)

    if bench is None:
        print("[market-structure] FAILED: benchmark %s missing from response" % BENCH,
              file=sys.stderr)
        return 1

    # --- the index's path through the day -------------------------------------
    path = {"ticker": BENCH, "group": bench["group"]}
    o, h, lo, c, p = (bench["open"], bench["high"], bench["low"],
                      bench["close"], bench["prev_close"])
    if None not in (o, h, lo, c, p) and p:
        path.update({
            "prev_close": round(p, 2), "open": o, "high": h, "low": lo, "close": c,
            "gap_pct": round(100.0 * (o - p) / p, 2),
            "day_pct": bench["day_pct"],
            "range_pct": round(100.0 * (h - lo) / p, 2),
            "high_pct": round(100.0 * (h - p) / p, 2),
            "low_pct": round(100.0 * (lo - p) / p, 2),
            "range_pos": bench["range_pos"],
        })
        # Plain-English shape of the session.
        bits = []
        if path["gap_pct"] >= 0.25:
            bits.append("opened up %.1f%%" % path["gap_pct"])
        elif path["gap_pct"] <= -0.25:
            bits.append("opened down %.1f%%" % abs(path["gap_pct"]))
        else:
            bits.append("opened flat")
        if path["low_pct"] < min(0.0, path["gap_pct"]) - 0.25:
            bits.append("fell to %.1f%% below the prior close" % abs(path["low_pct"]))
        if path["high_pct"] > max(0.0, path["gap_pct"]) + 0.25:
            bits.append("ran to +%.1f%%" % path["high_pct"])
        bits.append("closed %+.2f%%" % path["day_pct"])
        path["shape"] = ", ".join(bits)
        rp = path["range_pos"]
        if rp is not None:
            path["close_quality"] = (
                "closed in the TOP third of the day's range - buyers pressed into the bell"
                if rp >= 66 else
                "closed in the BOTTOM third of the day's range - sellers had the last word"
                if rp <= 33 else
                "closed mid-range - no side won the last hour")

    # --- leadership concentration ---------------------------------------------
    groups = [r for r in rows if r["ticker"] != BENCH and r["accel"] is not None]
    conc = {}
    if groups:
        accels = sorted(r["_accel_raw"] for r in groups)
        conc = {
            "groups": len(groups),
            "accel_max": round(accels[-1], 1), "accel_min": round(accels[0], 1),
            "accel_spread": round(accels[-1] - accels[0], 1),
            "igniting_count": sum(1 for a in accels if a >= 8),
            "n_up_today": sum(1 for r in groups if (r["day_pct"] or 0) > 0),
            "n_down_today": sum(1 for r in groups if (r["day_pct"] or 0) < 0),
        }
        conc["read"] = (
            "Only %d group is running clearly ahead - a market with no leadership."
            % conc["igniting_count"] if conc["igniting_count"] <= 1 else
            "%d groups are running clearly ahead - leadership is broad."
            % conc["igniting_count"])

    # --- did the day's winners come from the hole, or the podium? -------------
    ranked = sorted((r for r in rows if r["ticker"] != BENCH and r["day_pct"] is not None),
                    key=lambda r: -r["day_pct"])
    top, bottom = ranked[:3], ranked[-3:]
    unwind = {
        "top3": [r["group"] for r in top],
        "top3_character": [r["character"] for r in top],
        "bottom3": [r["group"] for r in bottom],
        "bottom3_character": [r["character"] for r in bottom],
    }
    rebound_led = sum(1 for r in top if r["character"] == "REBOUND")
    giveback_lagged = sum(1 for r in bottom if r["character"] in ("GIVE-BACK", "LEADING"))
    unwind["verdict"] = (
        "UNWINDING - the day's leaders were beaten-up groups bouncing and the "
        "losers were recent winners handing gains back. Money left what was "
        "working; it did not enter a new theme."
        if rebound_led >= 2 and giveback_lagged >= 2 else
        "MIXED - the day's movers do not line up cleanly as either unwinding or "
        "a rotation into new leadership.")

    out = {
        "date": date,
        "generated": datetime.datetime.now().isoformat(timespec="seconds"),
        "note": ("Computable half of the Market & Rotation read. The NARRATIVE is "
                 "written by hand each evening - see memory "
                 "market-rotation-tab-depth-standard."),
        "benchmark": BENCH,
        "index_path": path,
        "concentration": conc,
        "unwind": unwind,
        "rows": sorted(rows, key=lambda r: (r["day_pct"] is None, -(r["day_pct"] or 0))),
    }
    for r in out["rows"]:
        r.pop("_accel_raw", None)   # internal precision helper, not part of the contract
    outp = os.path.join(REPO, "watchlists", "market-structure-%s.json" % date)
    with open(outp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=1)
        f.write("\n")
    print("[market-structure] wrote %s | %d groups | index %s"
          % (outp, len(rows), path.get("shape", "n/a")))
    print("[market-structure] %s" % unwind["verdict"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
