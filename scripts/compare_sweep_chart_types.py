"""Diff the same O.G Chandelier sweep read on candles vs Heikin Ashi.

Answers, with counts rather than opinion:
  - how often do the two chart types DISAGREE on BUY/SELL mode?
  - how often does HA report the flip on a LATER bar than candles?
  - how far apart are the Magical readings, and how often would that alone
    flip the gate verdict?

Usage:
    python scripts/compare_sweep_chart_types.py \
        watchlists/og-sweep-raw-2026-07-22-candles.json \
        watchlists/og-sweep-raw-2026-07-22-ha.json
"""
import json
import sys
from datetime import datetime

MAGICAL_HOT = 100.0   # provisional divider - see compile_og_sweep.py


def load(path):
    rows = json.load(open(path))
    return {r['rname']: r for r in rows if r.get('ok') and r.get('rname')}


def main():
    c = load(sys.argv[1])
    h = load(sys.argv[2])
    both = sorted(set(c) & set(h))

    mode_diff, flip_diff, gate_diff = [], [], []
    mag_deltas = []

    for s in both:
        a, b = c[s], h[s]
        if a.get('ce_mode') != b.get('ce_mode'):
            mode_diff.append((s, a.get('ce_mode'), b.get('ce_mode')))

        fa, fb = a.get('flip_date'), b.get('flip_date')
        if fa and fb and fa != fb:
            later = 'HA later' if fb > fa else 'candles later'
            flip_diff.append((s, fa, fb, later,
                              (b.get('bars_back') or 0) - (a.get('bars_back') or 0)))

        ma, mb = a.get('magical'), b.get('magical')
        if ma is not None and mb is not None:
            mag_deltas.append(abs(ma - mb))
            if (ma >= MAGICAL_HOT) != (mb >= MAGICAL_HOT):
                gate_diff.append((s, round(ma, 1), round(mb, 1)))

    stamp = datetime.now().strftime('%Y-%m-%d %H:%M local')
    out = []
    out.append('# Chart-type disagreement: candles vs Heikin Ashi')
    out.append('')
    out.append(f'**Written at** {stamp}  ')
    out.append(f'**Symbols compared** {len(both)}')
    out.append('')
    out.append('## Headline')
    out.append('')
    out.append(f'- BUY/SELL mode disagrees on **{len(mode_diff)}/{len(both)}** names '
               f'({100*len(mode_diff)/len(both):.0f}%)')
    out.append(f'- flip DATE disagrees on **{len(flip_diff)}/{len(both)}** names '
               f'({100*len(flip_diff)/len(both):.0f}%)')
    if mag_deltas:
        mag_deltas.sort()
        med = mag_deltas[len(mag_deltas)//2]
        out.append(f'- Magical median absolute difference **{med:.1f}**, '
                   f'max **{max(mag_deltas):.1f}**')
    out.append(f'- Magical alone flips the too-hot verdict on **{len(gate_diff)}** names')
    out.append('')

    if mode_diff:
        out.append('## Mode disagreements (candles -> HA)')
        out.append('')
        out.append('| Sym | Candles | Heikin Ashi |')
        out.append('|---|---|---|')
        for s, x, y in mode_diff:
            out.append(f'| {s} | {x} | {y} |')
        out.append('')

    if flip_diff:
        later_ha = [f for f in flip_diff if f[3] == 'HA later']
        out.append(f'## Flip-date disagreements ({len(later_ha)} of {len(flip_diff)} '
                   f'are HA reporting LATER)')
        out.append('')
        out.append('| Sym | Candles flip | HA flip | Who lags | Bar delta |')
        out.append('|---|---|---|---|---|')
        for s, fa, fb, later, d in sorted(flip_diff, key=lambda x: -abs(x[4]))[:40]:
            out.append(f'| {s} | {fa} | {fb} | {later} | {d:+d} |')
        out.append('')

    if gate_diff:
        out.append(f'## Names where Magical alone changes the gate verdict')
        out.append('')
        out.append('| Sym | Magical candles | Magical HA |')
        out.append('|---|---|---|')
        for s, x, y in gate_diff:
            out.append(f'| {s} | {x} | {y} |')
        out.append('')

    out.append('## What this means')
    out.append('')
    out.append('These are the SAME indicator on the SAME symbols at the SAME moment.')
    out.append('Every disagreement above is the chart-type setting alone. Whichever')
    out.append('type the system runs on must be fixed and recorded per run, and the')
    out.append('Magical thresholds must be recalibrated against THAT type - the two')
    out.append('are not interchangeable and mixing them invalidates the gate.')

    path = 'watchlists/og-sweep-2026-07-22-charttype-diff.md'
    with open(path, 'w') as fh:
        fh.write('\n'.join(out) + '\n')
    print('\n'.join(out))
    print(f'\nwrote {path}')


if __name__ == '__main__':
    main()
