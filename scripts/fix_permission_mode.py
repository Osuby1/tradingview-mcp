"""Turn OFF "don't ask" mode and grant WebFetch. Run from the repo root:

    python scripts/fix_permission_mode.py

Claude Code blocks agents from writing their own permission files, so this has
to be run by the user.

WHAT IT CHANGES
---------------
1. permissions.defaultMode: "dontAsk"  ->  "default"

   "dontAsk" is DENY-BY-DEFAULT: anything not explicitly allow-listed is
   auto-denied with no prompt. On 2026-07-22 that silently blocked
   AskUserQuestion, Edit on settings, WebFetch on non-listed domains, and
   several git commit invocations whose message text did not match the
   allow pattern. "default" restores normal behaviour: allow-listed tools run
   without asking, everything else prompts.

2. Adds a blanket "WebFetch" allow rule.

   TRADE-OFF, stated plainly: this permits fetching ANY url with no prompt,
   not just the ~25 domains currently listed. That is broader than what was
   there before. The ~25 existing WebFetch(domain:...) rules become redundant
   but are left in place - they do no harm and document which sources have
   been used historically.

   If you would rather keep per-domain control, delete the "WebFetch" entry
   from the allow list afterwards and add specific domains instead, e.g.
       WebFetch(domain:ir.supermicro.com)

A timestamped backup is written first. Safe to run twice.
"""
import json
import shutil
from datetime import datetime

PATH = '.claude/settings.local.json'


def main():
    backup = f'{PATH}.bak-{datetime.now().strftime("%Y%m%d-%H%M%S")}'
    shutil.copy2(PATH, backup)
    print(f'backup -> {backup}')

    with open(PATH) as fh:
        cfg = json.load(fh)

    perms = cfg.setdefault('permissions', {})

    old_mode = perms.get('defaultMode')
    if old_mode == 'default':
        print('defaultMode already "default" - unchanged')
    else:
        perms['defaultMode'] = 'default'
        print(f'defaultMode: {old_mode!r} -> "default"')

    allow = perms.setdefault('allow', [])
    if 'WebFetch' in allow:
        print('WebFetch already allowed - unchanged')
    else:
        allow.append('WebFetch')
        print('added allow rule: WebFetch  (all domains, no prompt)')

    # AskUserQuestion was deleted once already by a /permissions session
    if 'AskUserQuestion' not in allow:
        allow.append('AskUserQuestion')
        print('re-added allow rule: AskUserQuestion (was missing again)')

    with open(PATH, 'w') as fh:
        json.dump(cfg, fh, indent=2)
        fh.write('\n')

    print(f'\nallow rules: {len(allow)}')
    print('\nRESTART Claude Code - the running session cached its permission')
    print('table at startup and will not see this until it reloads.')
    print('For an immediate in-session change instead, press Shift+Tab to')
    print('cycle the permission mode.')


if __name__ == '__main__':
    main()
