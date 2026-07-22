"""Ingest a raw ui_evaluate sweep dump (saved tool-result file) into the repo.

The MCP layer truncates oversized tool results to a file. This reads that file,
unwraps whatever envelope it carries, validates it is the expected array of
per-symbol reads, and writes clean JSON into watchlists/.
"""
import json
import sys


def main():
    src, date, ctype = sys.argv[1], sys.argv[2], sys.argv[3]
    raw = open(src, encoding='utf-8', errors='replace').read().strip()

    data = None
    # Try direct parse, then common envelopes.
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find('[')
        end = raw.rfind(']')
        if start >= 0 and end > start:
            data = json.loads(raw[start:end + 1])

    # Unwrap {success, result:"<json string>"} if present.
    if isinstance(data, dict) and 'result' in data:
        inner = data['result']
        data = json.loads(inner) if isinstance(inner, str) else inner

    if not isinstance(data, list):
        raise SystemExit(f'expected a list, got {type(data).__name__}')

    required = {'req', 'ce_mode', 'last', 'zlsma', 'magical'}
    missing = [i for i, r in enumerate(data)
               if not isinstance(r, dict) or not required.issubset(r.keys())]
    if missing:
        print(f'WARNING: {len(missing)} rows missing expected keys (first: {missing[:3]})')

    out = f'watchlists/og-sweep-raw-{date}-{ctype}.json'
    with open(out, 'w') as fh:
        json.dump(data, fh, indent=1)

    ok = sum(1 for r in data if r.get('ok'))
    print(f'ingested {len(data)} rows ({ok} ok) -> {out}')


if __name__ == '__main__':
    main()
