"""Measure whether the Magical (CCI-20) +/-100 cut actually separates returns.

The gate currently rejects a fresh Chandelier BUY when Magical >= 100, on the
grounds that +100 is the indicator's own Overbought Level. That is a principled
DEFAULT, not evidence. This asks the empirical question: across every historical
Chandelier BUY flip on the sweep universe, does the Magical reading AT THE
SIGNAL BAR predict forward returns at all?

Input: CSV dumped from the live chart - sym,date,mag,entry,f5,f10,f21
       (f5/f10/f21 = forward % return 5/10/21 bars after the signal bar)

Usage:
    python scripts/calibrate_magical_gate.py <dump.txt>
"""
import csv
import json
import sys
from datetime import datetime

BUCKETS = [
    ('<= -100  (oversold)',      None,   -100),
    ('-100 to -50',              -100,    -50),
    ('-50 to 0',                  -50,      0),
    ('0 to 50',                     0,     50),
    ('50 to 79',                   50,     79),
    ('79 to 100  (untested band)', 79,    100),
    ('100 to 130 (just over cut)',100,    130),
    ('130 to 200',                130,    200),
    ('> 200  (extreme)',          200,   None),
]

HORIZONS = ['f5', 'f10', 'f21']


def load(path):
    rows = []
    with open(path, encoding='utf-8', errors='replace') as fh:
        text = fh.read()

    # The MCP layer saves oversized results as {"success":true,"result":"<csv>"}
    # with the newlines escaped. Unwrap that before parsing.
    body = None
    try:
        env = json.loads(text)
        if isinstance(env, dict) and isinstance(env.get('result'), str):
            body = env['result']
    except json.JSONDecodeError:
        pass
    if body is None:
        start = text.find('sym,date,mag')
        if start < 0:
            raise SystemExit('header not found in dump')
        body = text[start:]
    if 'sym,date,mag' not in body:
        raise SystemExit('header not found after unwrapping')
    for rec in csv.DictReader(body.splitlines()):
        try:
            r = {'sym': rec['sym'], 'date': rec['date'], 'mag': float(rec['mag'])}
        except (TypeError, ValueError):
            continue
        for h in HORIZONS:
            v = rec.get(h, '')
            r[h] = float(v) if v not in ('', None) else None
        rows.append(r)
    return rows


def stats(vals):
    vals = [v for v in vals if v is not None]
    if not vals:
        return None
    vals_sorted = sorted(vals)
    n = len(vals)
    mean = sum(vals) / n
    med = vals_sorted[n // 2] if n % 2 else (vals_sorted[n//2 - 1] + vals_sorted[n//2]) / 2
    win = 100.0 * sum(1 for v in vals if v > 0) / n
    return {'n': n, 'mean': round(mean, 2), 'median': round(med, 2), 'win': round(win, 1)}


def main():
    rows = load(sys.argv[1])
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M local')

    out = []
    out.append('# Does the Magical +/-100 cut actually separate returns?')
    out.append('')
    out.append(f'**Written at** {stamp}  ')
    out.append(f'**Signals** {len(rows)} historical Chandelier BUY flips, '
               f'candles, ~300 bars/symbol  ')
    out.append('**Magical measured AT THE SIGNAL BAR**, not today  ')
    out.append('**Forward returns** simple close-to-close, no stops, no costs')
    out.append('')

    # ---- headline: the gate as currently written -------------------------
    below = [r for r in rows if r['mag'] < 100]
    above = [r for r in rows if r['mag'] >= 100]
    out.append('## The gate as currently written')
    out.append('')
    out.append('| Group | Horizon | n | mean % | median % | win rate |')
    out.append('|---|---|---|---|---|---|')
    for label, grp in (('Magical < 100 (ALLOWED)', below), ('Magical >= 100 (REJECTED)', above)):
        for h in HORIZONS:
            s = stats([r[h] for r in grp])
            if s:
                out.append(f'| {label} | {h[1:]}d | {s["n"]} | {s["mean"]:+.2f} '
                           f'| {s["median"]:+.2f} | {s["win"]:.1f}% |')
    out.append('')

    # ---- full curve ------------------------------------------------------
    out.append('## Return by Magical bucket')
    out.append('')
    out.append('| Bucket | n | 5d mean | 10d mean | 21d mean | 21d median | 21d win |')
    out.append('|---|---|---|---|---|---|---|')
    curve = []
    for label, lo, hi in BUCKETS:
        grp = [r for r in rows
               if (lo is None or r['mag'] > lo) and (hi is None or r['mag'] <= hi)]
        if not grp:
            continue
        s5, s10, s21 = (stats([r[h] for r in grp]) for h in HORIZONS)
        curve.append({'bucket': label, 'n': len(grp),
                      'f5': s5, 'f10': s10, 'f21': s21})
        out.append(f'| {label} | {len(grp)} '
                   f'| {s5["mean"]:+.2f} ' if s5 else f'| {label} | {len(grp)} | - '
                   )
        # rebuild the row cleanly
        out[-1] = (f'| {label} | {len(grp)} '
                   f'| {s5["mean"]:+.2f} ' if s5 else f'| {label} | {len(grp)} | - ')
        row = f'| {label} | {len(grp)} |'
        row += f' {s5["mean"]:+.2f} |' if s5 else ' - |'
        row += f' {s10["mean"]:+.2f} |' if s10 else ' - |'
        row += f' {s21["mean"]:+.2f} |' if s21 else ' - |'
        row += f' {s21["median"]:+.2f} |' if s21 else ' - |'
        row += f' {s21["win"]:.1f}% |' if s21 else ' - |'
        out[-1] = row
    out.append('')

    # ---- where is the best split? ---------------------------------------
    out.append('## Every candidate cut, ranked by 21d mean separation')
    out.append('')
    out.append('| Cut | n below | n above | 21d mean below | 21d mean above | gap |')
    out.append('|---|---|---|---|---|---|')
    best = []
    for cut in range(-50, 301, 10):
        lo = stats([r['f21'] for r in rows if r['mag'] < cut])
        hi = stats([r['f21'] for r in rows if r['mag'] >= cut])
        if not lo or not hi or lo['n'] < 50 or hi['n'] < 50:
            continue
        best.append((lo['mean'] - hi['mean'], cut, lo, hi))
    for gap, cut, lo, hi in sorted(best, reverse=True)[:10]:
        out.append(f'| {cut} | {lo["n"]} | {hi["n"]} | {lo["mean"]:+.2f} '
                   f'| {hi["mean"]:+.2f} | {gap:+.2f} |')
    out.append('')

    verdict_100 = next((b for b in best if b[1] == 100), None)
    if verdict_100:
        gap, _, lo, hi = verdict_100
        out.append('## Verdict on 100 specifically')
        out.append('')
        out.append(f'- Below 100: n={lo["n"]}, 21d mean {lo["mean"]:+.2f}%, '
                   f'win {lo["win"]:.1f}%')
        out.append(f'- At/above 100: n={hi["n"]}, 21d mean {hi["mean"]:+.2f}%, '
                   f'win {hi["win"]:.1f}%')
        out.append(f'- Separation: **{gap:+.2f} pts of 21-day return**')
        if abs(gap) < 1.0:
            out.append('')
            out.append('**The cut does essentially nothing.** A gate that does not '
                       'separate returns is not risk control, it is just lost trades.')
        elif gap < 0:
            out.append('')
            out.append('**The cut is BACKWARDS** - the rejected group outperformed.')
    out.append('')
    out.append('## Caveats')
    out.append('')
    out.append('- Close-to-close returns. No stops, no slippage, no position sizing.')
    out.append('  The live system exits on the Chandelier stop, so real results differ.')
    out.append('- ~300 bars/symbol covers roughly mid-2025 to now: a strong tape for')
    out.append('  most of it. Momentum cuts flatter themselves in a bull market.')
    out.append('- Survivorship: the universe is today\'s watchlist, not the watchlist')
    out.append('  as it stood in 2025.')
    out.append('- Signals in the last 21 bars have no complete forward window and are')
    out.append('  excluded from that horizon automatically.')

    path = 'research/magical-gate-calibration-2026-07-22.md'
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    with open('research/magical-gate-calibration-2026-07-22.json', 'w', encoding='utf-8') as fh:
        json.dump({'written_at': stamp, 'n_signals': len(rows), 'curve': curve}, fh, indent=1)

    print('\n'.join(out))
    print(f'\nwrote {path}')


if __name__ == '__main__':
    main()
