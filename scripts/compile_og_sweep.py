"""Compile a raw O.G Chandelier sweep dump into an actionable read.

Input: watchlists/og-sweep-raw-<date>-<type>.json  (array of per-symbol reads
straight off the live chart, produced by the in-page __ogSweep runner)

Output: markdown summary + json, split into fresh BUY flips, gate verdicts,
SELL-mode names, and data-quality flags.

WHAT "MAGICAL" IS
-----------------
Verified 2026-07-22 by reading the study's inputs on the live chart: the Magical
Overbought & Oversold Indicator is a **20-period CCI on close**, with its own
Overbought Level = +100 and Oversold Level = -100. Its "Topology Map" plot reads
identically to its "CCI Overlay" plot.

So the 100 cut below is the indicator's OWN declared overbought band, not an
invented threshold. It matches 2026-07-21 outcomes exactly: every gate pass sat
inside +/-100 (MU -22.8, GDX -30.4, FLEX -68.1, HON +22.7, PM +79.1) and every
fail sat outside (PFE 113.6, CTRE 176.1, SKK 233.2).

What remains genuinely untested is whether +/-100 is the right cut FOR RETURNS
rather than just the indicator default. Until that is measured in the shadow
lane, readings in the 79-113 band are still flagged so a borderline number is
never the sole reason a name is rejected.
"""
import json
import sys
from datetime import datetime

MAGICAL_HOT = 100.0          # the indicator's own Overbought Level input
MAGICAL_UNCERTAIN = (79.0, 113.0)   # band with no return data either side yet
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
    out.append(f'> Magical = 20-period CCI on close. The {MAGICAL_HOT:.0f} cut is the '
               f"indicator's own Overbought Level input, not an invented threshold. "
               f'Still untested: whether +/-{MAGICAL_HOT:.0f} is the right cut FOR RETURNS. '
               f'Readings in {MAGICAL_UNCERTAIN[0]:.0f}-{MAGICAL_UNCERTAIN[1]:.0f} are flagged '
               f'so a borderline number is never the sole rejection reason.')
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
