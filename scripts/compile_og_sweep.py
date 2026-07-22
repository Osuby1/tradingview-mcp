"""Compile a raw O.G Chandelier sweep dump into an actionable read.

Input: watchlists/og-sweep-raw-<date>-<type>.json  (array of per-symbol reads
straight off the live chart, produced by the in-page __ogSweep runner)

Output: markdown summary + json, split into fresh BUY flips, gate verdicts,
SELL-mode names, and data-quality flags.

GATE CALIBRATION WARNING
------------------------
The Magical OB/OS "too hot" threshold is NOT calibrated. Observed on 2026-07-21:
passes ran -68 to +79, fails at 113.6 / 176.1 / 233.2. The true line sits
somewhere in the untested 79-113 gap. This script uses 100 as a PROVISIONAL
divider and labels every verdict near it as UNCALIBRATED. Do not treat a
borderline Magical verdict as a decision.
"""
import json
import sys
from datetime import datetime

MAGICAL_HOT = 100.0          # PROVISIONAL - see warning above
MAGICAL_UNCERTAIN = (79.0, 113.0)
FRESH_BARS = 5


def gates(r):
    """Return (verdict, [reasons]) for a BUY-mode name."""
    reasons = []
    last, zl, mag = r.get('last'), r.get('zlsma'), r.get('magical')

    if last is None or zl is None or mag is None:
        return 'NO DATA', ['missing readings']

    if last <= zl:
        reasons.append(f'below ZLSMA {zl}')
    if mag >= MAGICAL_HOT:
        reasons.append(f'Magical {mag} too hot (provisional cut {MAGICAL_HOT:.0f})')

    stretch = (last / zl - 1) * 100 if zl else None
    if stretch is not None and stretch > 25:
        reasons.append(f'{stretch:.0f}% above ZLSMA - extended')

    verdict = 'PASS' if not reasons else 'FAIL'
    if MAGICAL_UNCERTAIN[0] <= mag <= MAGICAL_UNCERTAIN[1]:
        verdict += ' (UNCALIBRATED - Magical in untested band)'
    return verdict, reasons


def main():
    path = sys.argv[1]
    chart_type = sys.argv[2] if len(sys.argv) > 2 else 'candles'
    rows = json.load(open(path))

    stamp = datetime.now().strftime('%Y-%m-%d %H:%M local')
    ok = [r for r in rows if r.get('ok')]
    bad = [r for r in rows if not r.get('ok')]

    buys = [r for r in ok if r.get('ce_mode') == 'BUY']
    sells = [r for r in ok if r.get('ce_mode') == 'SELL']
    fresh = sorted([r for r in buys if (r.get('bars_back') is not None
                                        and r['bars_back'] <= FRESH_BARS)],
                   key=lambda r: r['bars_back'])

    out = []
    out.append(f'# O.G Chandelier sweep - {chart_type}')
    out.append('')
    out.append(f'**Data as of** live feed, bar date {ok[0].get("bar_date") if ok else "?"} '
               f'(session in progress if intraday)  ')
    out.append(f'**Written at** {stamp}  ')
    out.append(f'**Chart type** {chart_type}  ')
    out.append(f'**Scanned** {len(ok)}/{len(rows)} clean'
               + (f', {len(bad)} unreadable' if bad else ''))
    out.append('')
    out.append(f'> Magical gate is PROVISIONAL (cut at {MAGICAL_HOT:.0f}; true line unknown '
               f'inside {MAGICAL_UNCERTAIN[0]:.0f}-{MAGICAL_UNCERTAIN[1]:.0f}). '
               f'Verdicts marked UNCALIBRATED are not decisions.')
    out.append('')
    out.append(f'## Fresh BUY flips (<= {FRESH_BARS} bars back): {len(fresh)}')
    out.append('')
    out.append('| Sym | Flip | Bars | Last | Stop | ZLSMA | Magical | Verdict | Blocked by |')
    out.append('|---|---|---|---|---|---|---|---|---|')
    for r in fresh:
        v, why = gates(r)
        out.append(f'| {r.get("rname")} | {r.get("flip_date")} | {r["bars_back"]} '
                   f'| {r.get("last")} | {r.get("long_stop")} | {r.get("zlsma")} '
                   f'| {r.get("magical")} | {v} | {"; ".join(why) or "-"} |')

    out.append('')
    out.append(f'## Mode census')
    out.append('')
    out.append(f'- BUY: {len(buys)}')
    out.append(f'- SELL: {len(sells)}')
    out.append(f'- older BUY (> {FRESH_BARS} bars): {len(buys) - len(fresh)}')

    if bad:
        out.append('')
        out.append('## Unreadable')
        for r in bad:
            out.append(f'- {r.get("req")}: {r.get("why")}')

    # symbol-resolution sanity: currency and exchange surprises
    odd = [r for r in ok if r.get('rccy') and r['rccy'] != 'USD']
    if odd:
        out.append('')
        out.append('## Non-USD resolutions (symbol-trap check)')
        for r in odd:
            out.append(f'- {r.get("req")} -> {r.get("rfull")} ({r.get("rccy")}) {r.get("rdesc")}')

    date = datetime.now().strftime('%Y-%m-%d')
    md = f'watchlists/og-sweep-{date}-{chart_type}.md'
    with open(md, 'w') as fh:
        fh.write('\n'.join(out) + '\n')

    js = f'watchlists/og-sweep-{date}-{chart_type}.json'
    with open(js, 'w') as fh:
        json.dump({'written_at': stamp, 'chart_type': chart_type,
                   'scanned': len(ok), 'unreadable': len(bad),
                   'fresh': fresh, 'buys': len(buys), 'sells': len(sells),
                   'rows': rows}, fh, indent=1)

    print('\n'.join(out))
    print(f'\nwrote {md}\nwrote {js}')


if __name__ == '__main__':
    main()
