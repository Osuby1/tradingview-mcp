"""SHADOW WOC stage 2: the ignition trigger.

STATUS: SHADOW LANE ONLY. Pre-registered 2026-07-22. NOT a live rule.

Stage 1 (shadow_woc_detector.py) answers "which broken charts have stopped
falling and coiled?" - it fires on ~40 names/day. That is a WATCH LIST, not a
buy signal. Firing on 40 names a day and calling it a signal would be lying.

Stage 2 asks the only question that makes it tradeable: which of yesterday's
coiled names ignited TODAY on real volume?

    trigger = was on stage-1 list on day N-1
              AND relvol_today >= 2.0 on day N
              AND price closed higher than day N-1

This is the same before-photo / convergence shape the Early Ignition system
already uses. It is NOT tuned to SMCI - note in the output that SMCI does NOT
trigger on 7/21 (its volume was 0.55x). That is the honest result and it is the
whole point: a volume-confirmed system would have bought SMCI on 7/22 near $30,
not on 7/21 at $23.83. The miss was real but it was never worth the full move.

USAGE
    python scripts/shadow_woc_trigger.py 2026-07-20 2026-07-21
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from shadow_woc_detector import scan_workbook, _num, COLS
import openpyxl

TRIGGER = {
    'version': 'woc-trigger-v1',
    'relvol_min': 2.0,
    'require_price_up': True,
}


def load_day_rows(date):
    """ticker -> row dict from the Excluded tab, for price/relvol lookup."""
    wb = openpyxl.load_workbook(f'reports/origination_scan_{date}.xlsx',
                                read_only=True, data_only=True)
    ws = wb['Excluded']
    rows = list(ws.iter_rows(values_only=True))
    header = [str(c).strip() if c is not None else '' for c in rows[0]]
    idx = {k: header.index(v) for k, v in COLS.items() if v in header}
    out = {}
    for row in rows[1:]:
        if not row or not row[0]:
            continue
        g = lambda k: row[idx[k]] if k in idx and idx[k] < len(row) else None
        out[str(row[0]).strip()] = {
            'price': _num(g('price')),
            'relvol': _num(g('relvol')),
            'relvol3': _num(g('relvol3')),
            'rsi': _num(g('rsi')),
            'pct52': _num(g('pct52')),
        }
    return out


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return
    prior, today = sys.argv[1], sys.argv[2]

    _, watch, _ = scan_workbook(f'reports/origination_scan_{prior}.xlsx')
    watch_names = [h['ticker'] for h in watch]
    today_rows = load_day_rows(today)

    print(f'SHADOW WOC TRIGGER  [{TRIGGER["version"]}]')
    print('STATUS: shadow lane - logging only, NOT a live rule\n')
    print(f'stage-1 watch list from {prior}: {len(watch_names)} names')
    print(f'trigger on {today}: relvol >= {TRIGGER["relvol_min"]} AND price up\n')

    fired, missing, quiet = [], [], []
    for h in watch:
        t = h['ticker']
        row = today_rows.get(t)
        if not row or row['relvol'] is None or row['price'] is None:
            missing.append(t)
            continue
        price_up = (h['price'] is not None and row['price'] > h['price'])
        if row['relvol'] >= TRIGGER['relvol_min'] and (price_up or not TRIGGER['require_price_up']):
            fired.append({
                'ticker': t,
                'price_prior': h['price'], 'price_today': row['price'],
                'pct_move': round((row['price'] / h['price'] - 1) * 100, 1) if h['price'] else None,
                'relvol_today': row['relvol'],
                'pct_of_52wk_high': row['pct52'],
                'adx': h['adx'],
            })
        else:
            quiet.append((t, row['relvol']))

    print(f'TRIGGERED: {len(fired)}')
    for f in sorted(fired, key=lambda x: -(x['relvol_today'] or 0)):
        print(f"  {f['ticker']:<6} {f['price_prior']:>8} -> {f['price_today']:<8} "
              f"({f['pct_move']:+.1f}%)  relvol {f['relvol_today']:.2f}  "
              f"{f['pct_of_52wk_high']}% of 52wk high")
    if not fired:
        print('  (none)')

    print(f'\nno ignition: {len(quiet)}   not in {today} sheet: {len(missing)}')

    smci = next((q for q in quiet if q[0] == 'SMCI'), None)
    if smci:
        print(f'\nSMCI: on the watch list, did NOT trigger - volume only {smci[1]:.2f}x normal.')
        print('      Its ignition bar came the NEXT session. A volume-confirmed')
        print('      system buys it then, not before.')

    out = f'research/shadow-woc-trigger-{today}.json'
    with open(out, 'w') as fh:
        json.dump({'trigger': TRIGGER, 'prior': prior, 'today': today,
                   'watch_count': len(watch_names), 'fired': fired,
                   'quiet': len(quiet), 'missing': len(missing)}, fh, indent=1)
    print(f'\nwrote {out}')


if __name__ == '__main__':
    main()
