"""Restore the 12 allow rules deleted by the /permissions session on 2026-07-22.

.claude/settings.local.json is globally gitignored, so there is no git history to
restore from. These strings are reconstructed verbatim from the deletion log that
/permissions printed.

Idempotent: re-adds only what is currently missing, and writes a timestamped
backup first. Run from the repo root:

    python scripts/restore_permissions.py
"""
import json
import shutil
from datetime import datetime

PATH = '.claude/settings.local.json'

DELETED = [
    "AskUserQuestion",
    "Bash(cd /c/Users/osuby/tradingview-mcp)",
    "Bash(curl -s --max-time 5 http://localhost:9222/json/version)",
    "Bash(curl -s 'https://gamma-api.polymarket.com/events?closed=false&order=volume&ascending=false&limit=6&tag_slug=fed')",
    "Bash(curl -s 'https://gamma-api.polymarket.com/events?closed=false&order=volume&ascending=false&limit=8&tag_slug=economy')",
    "Bash(curl -s 'https://gamma-api.polymarket.com/events?closed=false&order=volume&ascending=false&limit=8&tag_slug=geopolitics')",
    "Bash(curl -s 'https://publicreporting.cftc.gov/resource/6dca-aqww.json?$limit=1&$where=cftc_contract_market_code=%27067651%27&$order=report_date_as_yyyy_mm_dd%20DESC')",
    "Bash(curl -s 'https://publicreporting.cftc.gov/resource/6dca-aqww.json?$limit=2&$order=report_date_as_yyyy_mm_dd%20DESC&$where=cftc_contract_market_code=%27067651%27')",
    "Bash(curl -s 'https://publicreporting.cftc.gov/resource/6dca-aqww.json?$limit=2&$order=report_date_as_yyyy_mm_dd%20DESC&$where=cftc_contract_market_code=%27088691%27')",
    "Bash(curl -s 'https://publicreporting.cftc.gov/resource/6dca-aqww.json?$limit=3&$order=report_date_as_yyyy_mm_dd%20DESC&$where=contract_market_name%20like%20%27%25CRUDE%20OIL%2C%20LIGHT%20SWEET%25%27')",
    "Bash(curl -s 'https://publicreporting.cftc.gov/resource/6dca-aqww.json?$limit=3&$order=report_date_as_yyyy_mm_dd%20DESC&$where=contract_market_name%20like%20%27%25GOLD%25%27')",
    "Bash(curl -s 'https://publicreporting.cftc.gov/resource/6dca-aqww.json?$limit=3&$order=report_date_as_yyyy_mm_dd%20DESC&$where=contract_market_name%20like%20%27%25CRUDE%20OIL%2C%20LIGHT%20SWEET%25%27%20AND%20cftc_market_code=%27NYME%27')",
]


def main():
    backup = f'{PATH}.bak-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
    shutil.copy2(PATH, backup)
    print(f'backup -> {backup}')

    with open(PATH) as fh:
        cfg = json.load(fh)

    allow = cfg.setdefault('permissions', {}).setdefault('allow', [])
    before = len(allow)

    restored, already = [], []
    for rule in DELETED:
        (already if rule in allow else restored).append(rule)
    allow.extend(restored)

    with open(PATH, 'w') as fh:
        json.dump(cfg, fh, indent=2)
        fh.write('\n')

    print(f'allow rules: {before} -> {len(allow)}')
    print(f'restored {len(restored)}, already present {len(already)}')
    for r in restored:
        print(f'  + {r[:90]}')

    print('\nNOTE: 10 of these are curl rules already covered by the existing')
    print('wildcard "Bash(curl *)" - they are redundant but harmless.')
    print('The one that actually matters is AskUserQuestion.')
    print('\nRestart Claude Code for the change to take effect - the running')
    print('session caches its permission table at startup.')


if __name__ == '__main__':
    main()
