"""Fetch stockanalysis.com gainers/losers and write watchlists/market-movers-<date>.json."""
import json
import re
import sys

import requests

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
    )
}

URLS = {
    "gainers": "https://stockanalysis.com/markets/gainers/",
    "losers": "https://stockanalysis.com/markets/losers/",
}


def parse_table(html):
    """Parse the main movers table. Columns on these pages:
    Symbol | Company Name | % Change | Stock Price | Volume | Market Cap"""
    rows = []
    # Grab all table rows in the main table body
    body_match = re.search(r"<tbody[^>]*>(.*?)</tbody>", html, re.S)
    if not body_match:
        return rows
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", body_match.group(1), re.S):
        cells = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        if len(cells) < 7:
            continue
        # Strip tags/entities from each cell
        clean = []
        for c in cells:
            c = re.sub(r"<[^>]+>", "", c)
            c = c.replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"')
            clean.append(c.strip())
        _rank, sym, company, pct, price, volume, mcap = clean[:7]
        try:
            price_val = float(price.replace(",", ""))
        except ValueError:
            price_val = None
        try:
            pct_val = float(pct.replace("%", "").replace(",", "").replace("+", ""))
        except ValueError:
            pct_val = None
        rows.append(
            {
                "sym": sym,
                "company": company,
                "price": price_val,
                "pct_change": pct_val,
                "market_cap_raw": mcap,
                "volume": volume,
            }
        )
    return rows


def main():
    out = {}
    for key, url in URLS.items():
        r = requests.get(url, headers=HEADERS, timeout=30)
        r.raise_for_status()
        rows = parse_table(r.text)
        if not rows:
            print(f"FAIL: no rows parsed from {url}", file=sys.stderr)
            sys.exit(1)
        out[key] = rows
        print(f"{key}: {len(rows)} rows, first={rows[0]['sym']} {rows[0]['pct_change']}%")

    path = r"C:\Users\osuby\tradingview-mcp\watchlists\market-movers-2026-08-05.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
