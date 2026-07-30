"""Official intraday day-changes for briefs - the ONLY sanctioned way to state
"X is up/down N% today" in any brief.

Why this exists (2026-07-30): day-%s were hand-computed from quote_get's
synthetic "open" field twice (7/8 and 7/30) and shipped wrong tape reads
(SPY reported -0.2% on a +0.82% day). quote_get is for the live LAST price
only; the scanner's `change` column is the official prior-close comparison.

Usage:
  python scripts/day_changes.py                # indices + open-book positions
  python scripts/day_changes.py NYSE:JNJ CAKE  # add extras (exchange prefix optional)
"""
import json
import sys
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent.parent
SCANNER_URL = "https://scanner.tradingview.com/america/scan"
INDICES = ["AMEX:SPY", "NASDAQ:QQQ", "AMEX:DIA", "AMEX:IWM"]

# scanner needs exchange-qualified tickers and silently drops bad ones, so for a
# bare ticker submit all three US listings - only the real one comes back
def qualify(sym: str) -> list[str]:
    if ":" in sym:
        return [sym.upper()]
    return [f"{ex}:{sym.upper()}" for ex in ("NYSE", "NASDAQ", "AMEX")]


def main() -> None:
    tickers = list(INDICES)
    bare = []
    book = REPO / "watchlists" / "open-book.json"
    if book.exists():
        bare += [p["sym"] for p in json.loads(book.read_text()).get("positions", [])]
    bare += sys.argv[1:]
    for s in bare:
        tickers += qualify(s)
    seen, ordered = set(), []
    for t in tickers:
        if t not in seen:
            seen.add(t)
            ordered.append(t)

    resp = requests.post(
        SCANNER_URL,
        data=json.dumps(
            {"symbols": {"tickers": ordered}, "columns": ["name", "close", "change"]}
        ),
        headers={"Content-Type": "text/plain"},
        timeout=15,
    )
    resp.raise_for_status()
    rows = resp.json()["data"]
    returned = {r["d"][0] for r in rows}
    for r in sorted(rows, key=lambda r: r["d"][2], reverse=True):
        name, close, change = r["d"]
        print(f"{name:8s} {close:10.2f}  {change:+6.2f}%")
    missing = sorted({t.split(":")[1] for t in ordered} - returned)
    if missing:
        print(f"MISSING (no US listing found - do NOT guess these): {', '.join(missing)}")


if __name__ == "__main__":
    main()
