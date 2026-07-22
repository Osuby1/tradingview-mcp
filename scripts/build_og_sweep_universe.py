"""Build the O.G Chandelier sweep universe for a given date.

Root cause this addresses (2026-07-22): the live TradingView watchlist had drifted
from watchlists/main-watchlist.md. SMCI sat in the repo file but NOT in the live
watchlist, so every run that sourced from the live watchlist silently skipped it.
This script emits the UNION so a name can only be missed on purpose.
"""
import json
import sys

# Non-equity instruments the O.G equity/ETF scan does not apply to, plus known
# bad tickers carried in memory (GOLD = Gold.com Inc not Barrick; NUVL delisted).
NON_EQUITY = {
    'AVAXUSDT', 'BIPZ2030', 'BTCUSD', 'DOGEUSD', 'DOTUSD', 'ETHUSD', 'ETPZ2030',
    'EURUSD', 'GBPUSD', 'HYPEHUSD', 'SOLUSD', 'SUIUSD', 'USDJPY',
    'DJI', 'DXY', 'NDQ', 'OVX', 'SPX', 'VIX', 'SILVER', 'WTI', 'USOIL',
    'PURR', 'HYPD', 'CBRS', 'ORBS',
    'GOLD', 'NUVL',
}

# Exchange-qualified symbols read from the LIVE TradingView watchlist via
# watchlist_get on 2026-07-22.
LIVE = [
    "NYSE:BBAI", "NYSE:BHP", "NYSE:C", "NYSE:CB", "NASDAQ:CENX", "NASDAQ:CHYM",
    "NYSE:CLX", "NASDAQ:COST", "AMEX:CTM", "NYSE:CVX", "NYSE:DE", "NASDAQ:DFDV",
    "NYSE:DIS", "NYSE:DTE", "NYSE:DVN", "NYSE:DOW", "NASDAQ:FHB", "NASDAQ:FUTU",
    "NYSE:GD", "NASDAQ:GOOG", "NYSE:GS", "NASDAQ:HAS", "NYSE:HD", "NASDAQ:HON",
    "NASDAQ:INTC", "NYSE:JNJ", "NYSE:JPM", "NYSE:KO", "AMEX:KRE", "AMEX:KWEB",
    "NASDAQ:LAES", "NYSE:MCD", "NYSE:MDT", "NASDAQ:MELI", "NASDAQ:META", "NYSE:MP",
    "NASDAQ:MSFT", "NASDAQ:MU", "NYSE:NEM", "NYSE:NET", "NASDAQ:NFLX", "NYSE:NKE",
    "OTC:NSRGY", "NASDAQ:NVAX", "NASDAQ:NVTS", "NYSE:PBF", "NYSE:PBR", "NASDAQ:PEP",
    "NYSE:PFE", "NYSE:PM", "NASDAQ:RIVN", "NASDAQ:ROKU", "NASDAQ:SBUX", "NYSE:SNOW",
    "NYSE:TDOC", "NASDAQ:TGTX", "AMEX:UAVS", "NYSE:UBER",
]

# Explicit prefixes for repo-only names where bare-ticker resolution is a known
# trap (see memory: symbol-resolution-traps).
FORCE_PREFIX = {
    'FITB': 'NYSE:FITB',
    'SMCI': 'NASDAQ:SMCI',
}


def main(date_str):
    with open('watchlists/main-watchlist.md') as fh:
        line = fh.read().splitlines()[5]
    repo = [s.strip().upper() for s in line.split(',') if s.strip()]
    repo_equities = [s for s in repo if s not in NON_EQUITY]

    live_bare = {s.split(':')[1] for s in LIVE}
    repo_only = sorted(set(repo_equities) - live_bare)
    repo_only = [FORCE_PREFIX.get(s, s) for s in repo_only]

    universe = LIVE + repo_only
    out = {
        'date': date_str,
        'total': len(universe),
        'live_watchlist_count': len(LIVE),
        'repo_only_count': len(repo_only),
        'repo_only': repo_only,
        'symbols': universe,
    }
    path = f'watchlists/og-sweep-universe-{date_str}.json'
    with open(path, 'w') as fh:
        json.dump(out, fh, indent=1)

    print(f'live={len(LIVE)} repo_only={len(repo_only)} TOTAL={len(universe)}')
    print(f'SMCI included: {any(u.endswith("SMCI") for u in universe)}')
    print(f'wrote {path}')
    print()
    print('IN REPO FILE BUT MISSING FROM LIVE WATCHLIST (the blind spot):')
    print(', '.join(repo_only))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '2026-07-22')
