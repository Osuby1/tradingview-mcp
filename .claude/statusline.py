#!/usr/bin/env python3
"""Claude Code status line: shows task progress so Omar doesn't have to nudge.

Wired via .claude/settings.json -> statusLine.command.

Claude Code pipes a JSON blob about the session on stdin. This script ignores
most of it and instead reads .claude/progress.json, which Claude writes as it
works, then prints ONE line for the bottom of the screen.

progress.json shape (all fields optional):
    {"task": "universe sweep", "done": 40, "total": 156,
     "step": 2, "steps": 4, "note": "candles", "updated": "14:44"}

Prints e.g.:
    ~/tradingview-mcp | step 2/4 | universe sweep [####------] 26% 40/156 | candles

If progress.json is missing or stale (>15 min), it degrades to just the
directory and model, so a forgotten file never shows a misleading percentage.
"""
import json
import os
import sys
import time

BAR_W = 10


def read_stdin():
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}


def main():
    ctx = read_stdin()

    cwd = ctx.get("cwd") or ctx.get("workspace", {}).get("current_dir") or os.getcwd()
    short_cwd = os.path.basename(cwd.rstrip("/\\")) or cwd
    model = (ctx.get("model") or {}).get("display_name") or ""

    parts = [f"\x1b[36m{short_cwd}\x1b[0m"]
    if model:
        parts.append(f"\x1b[90m{model}\x1b[0m")

    pfile = os.path.join(cwd, ".claude", "progress.json")
    prog = None
    try:
        if os.path.exists(pfile):
            age = time.time() - os.path.getmtime(pfile)
            if age < 900:  # ignore anything older than 15 minutes
                with open(pfile) as fh:
                    prog = json.load(fh)
    except Exception:
        prog = None

    if prog:
        if prog.get("steps"):
            parts.append(f"\x1b[35mstep {prog.get('step', '?')}/{prog['steps']}\x1b[0m")

        task = prog.get("task", "working")
        done, total = prog.get("done"), prog.get("total")
        if isinstance(done, (int, float)) and isinstance(total, (int, float)) and total:
            pct = max(0, min(100, int(done / total * 100)))
            filled = int(pct / 100 * BAR_W)
            bar = "#" * filled + "-" * (BAR_W - filled)
            colour = "32" if pct >= 100 else "33"
            parts.append(f"\x1b[{colour}m{task} [{bar}] {pct}% {int(done)}/{int(total)}\x1b[0m")
        else:
            parts.append(f"\x1b[33m{task}\x1b[0m")

        if prog.get("note"):
            parts.append(f"\x1b[90m{prog['note']}\x1b[0m")

    print(" | ".join(parts))


if __name__ == "__main__":
    main()
