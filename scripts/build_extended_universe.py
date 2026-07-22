"""Build the EXTENDED scan universe: all three watchlists + origination tabs.

Sources (all files in the repo - NEVER watchlist_get, which returns only the
rendered DOM rows and silently truncates; hq-swing.md has documented that since
2026-06-23 and it still got missed twice):

  watchlists/main-watchlist.md      ~170 equities/ETFs + non-equity instruments
  watchlists/hq-swing.md            ~95  HQ Swing names
  watchlists/sector-themes.md       ~37  thematic stocks + ETFs
  watchlists/origination-tabs.md    Buy Zone + Fresh Ignitions + Coiled

Usage:
    python scripts/build_extended_universe.py 2026-07-22
    python scripts/build_extended_universe.py 2026-07-22 --no-coiled
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tracked_symbols import tracked  # noqa: E402

# Non-equity instruments the O.G equity/ETF scan does not apply to, plus tickers
# known bad (GOLD = Gold.com Inc not Barrick; NUVL delisted).
NON_EQUITY = {
    'AVAXUSDT', 'BIPZ2030', 'BTCUSD', 'DOGEUSD', 'DOTUSD', 'ETHUSD', 'ETPZ2030',
    'EURUSD', 'GBPUSD', 'HYPEHUSD', 'SOLUSD', 'SUIUSD', 'USDJPY',
    'DJI', 'DXY', 'NDQ', 'OVX', 'SPX', 'VIX', 'SILVER', 'WTI', 'USOIL',
    'PURR', 'HYPD', 'CBRS', 'ORBS', 'GOLD', 'NUVL',
}

# Exchange prefixes where bare-ticker resolution is a known trap.
FORCE_PREFIX = {'FITB': 'NYSE:FITB', 'SMCI': 'NASDAQ:SMCI'}

TICKER_RE = re.compile(r'^[A-Z][A-Z0-9.\-]{0,6}$')


def _from_list_line(path, header_prefix="## Full list"):
    """Pull the comma-separated ticker line that follows a header."""
    try:
        lines = open(path, encoding='utf-8').read().splitlines()
    except OSError:
        return set()
    out, grab = set(), False
    for ln in lines:
        if ln.strip().startswith(header_prefix):
            grab = True
            continue
        if grab:
            if not ln.strip():
                continue
            if ln.startswith('#'):
                break
            for tok in ln.split(','):
                t = tok.strip().upper()
                t = re.sub(r'\(.*?\)', '', t).strip()   # drop "WCN(TSX)" suffixes
                if TICKER_RE.match(t):
                    out.add(t)
            break
    return out


def _main_watchlist(path):
    """main-watchlist.md keeps its list on line 6."""
    try:
        line = open(path, encoding='utf-8').read().splitlines()[5]
    except (OSError, IndexError):
        return set()
    return {t.strip().upper() for t in line.split(',') if TICKER_RE.match(t.strip().upper())}


def _origination(path, include_coiled=True):
    """Pull Buy Zone / Fresh Ignitions / (optionally) Coiled from the tabs file."""
    try:
        text = open(path, encoding='utf-8').read()
    except OSError:
        return {}, None
    wanted = ['Buy Zone', 'Fresh Ignitions'] + (['Coiled'] if include_coiled else [])
    tabs = {}
    for name in wanted:
        m = re.search(rf'^## {re.escape(name)} \(\d+\)\s*\n(.+?)$', text, re.M)
        if m:
            tabs[name] = {t.strip().upper() for t in m.group(1).split(',')
                          if TICKER_RE.match(t.strip().upper())}
    m = re.search(r'DATA AS OF: (\d{4}-\d{2}-\d{2})', text)
    return tabs, (m.group(1) if m else None)


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else 'latest'
    include_coiled = '--no-coiled' not in sys.argv

    src = {}
    src['main-watchlist'] = _main_watchlist('watchlists/main-watchlist.md')
    src['hq-swing'] = _from_list_line('watchlists/hq-swing.md')
    src['sector-themes'] = _from_list_line('watchlists/sector-themes.md')

    orig_tabs, orig_asof = _origination('watchlists/origination-tabs.md', include_coiled)
    for k, v in orig_tabs.items():
        src[f'origination:{k}'] = v

    # Names we have ACTED on must never fall out of the universe, even after the
    # origination scanner demotes them or they leave every watchlist. ECVT was
    # recommended 7/20 with a sized plan and an armed alert, then vanished from
    # the scan on 7/21 when the scanner moved it to Excluded - while the plan was
    # still live and the trade was working. See scripts/tracked_symbols.py.
    tracked_syms, tracked_why = tracked(repo='.')
    src['TRACKED (alerts + plans)'] = tracked_syms

    everything = set()
    for v in src.values():
        everything |= v
    equities = sorted(t for t in everything if t not in NON_EQUITY)
    symbols = [FORCE_PREFIX.get(t, t) for t in equities]

    # Which tracked names would have been MISSED without the tracked source -
    # the ones no watchlist or origination tab covers. This is the ECVT set.
    from_lists = set()
    for k, v in src.items():
        if not k.startswith('TRACKED'):
            from_lists |= v
    tracked_only = sorted((tracked_syms - from_lists) - NON_EQUITY)

    out = {
        'date': date,
        'total': len(symbols),
        'origination_data_as_of': orig_asof,
        'include_coiled': include_coiled,
        'sources': {k: len(v) for k, v in src.items()},
        'tracked_only_rescued': tracked_only,
        'tracked_reasons': {s: tracked_why.get(s) for s in tracked_only},
        'dropped_non_equity': sorted(everything & NON_EQUITY),
        'symbols': symbols,
    }
    path = f'watchlists/og-sweep-universe-{date}-extended.json'
    json.dump(out, open(path, 'w'), indent=1)

    print(f'EXTENDED UNIVERSE: {len(symbols)} equities/ETFs')
    for k, v in sorted(src.items(), key=lambda x: -len(x[1])):
        print(f'  {k:28} {len(v):>4}')
    print(f'  {"(dropped non-equity)":28} {len(everything & NON_EQUITY):>4}')
    print(f'\norigination data as of: {orig_asof or "UNKNOWN"}')
    if tracked_only:
        print(f'\nRESCUED by the tracked source ({len(tracked_only)} names no list '
              f'covers):')
        print('  ' + ', '.join(f'{s} ({tracked_why.get(s)})' for s in tracked_only))
    print(f'wrote {path}')


if __name__ == '__main__':
    main()
