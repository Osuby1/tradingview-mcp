# CORRECTION 2026-07-22: the "98 missing names" finding was wrong

## What I claimed

Earlier today I reported that the live TradingView watchlist held 58 symbols while
`watchlists/main-watchlist.md` held ~170, and that **98 names were invisible to the
scan** - including NVDA, AAPL, AMZN, TSLA, PLTR, COIN, AMD and ARM. I called this
the root cause of SMCI being missed on 7/21, wrote it into memory, and committed it
in `a822204`.

## Why it was wrong

`mcp__tradingview__watchlist_get` reports `source: "data_attributes"` - it scrapes
rendered DOM rows. **TradingView virtualizes that list.** The tool therefore returns
only the currently-rendered window, not the watchlist.

The tell: two consecutive `watchlist_get` calls both returned exactly 58 symbols but
shared only **10** in common. A list cannot have 58 members and two nearly-disjoint
58-member readings.

Measured directly:

| Method | Symbols seen |
|---|---|
| `watchlist_get` (call 1) | 58 |
| `watchlist_get` (call 2, after 3 adds) | 58, only 10 overlapping |
| DOM scroll scan of `listContainer` | **144** |
| Union of all reads | **~157** |

The list container measured **7120px scrollHeight against a 517px viewport** at ~31px
per row - roughly 230 rows of capacity. `watchlist_get` sees about a quarter of it,
and *which* quarter depends on scroll position.

`main-watchlist.md` holds ~170 names. The live watchlist holds ~157+. **They were
never meaningfully out of sync.**

## What the real bug is

This is worse than watchlist drift, not better.

Any universe built by reading `watchlist_get` is **silently truncated to whatever
happened to be rendered**, and the truncation is *non-deterministic* - it depends on
where the watchlist panel was scrolled when the call fired. That explains the 7/21
run covering "47 watchlist equities/ETFs" when the watchlist actually held ~157.

So scans built this way cover a shifting, arbitrary ~30% of the watchlist and report
success. Nothing errors. Two runs on the same day can cover different names.

## What this does and does not change

**Unchanged - the fix is the same, and now more clearly correct.**
`scripts/build_og_sweep_universe.py` sources from the repo file. That was the right
call for a better reason than I gave: not because the live list is missing names, but
because the live list **cannot be read reliably at all**.

**Unchanged - SMCI was still not scanned on 7/21.** The 76-name run covered 29
origination candidates plus 47 watchlist names out of ~157. SMCI fell in the
unscanned majority.

**Changed - the mechanism.** Not "SMCI was absent from the watchlist" but "the
universe builder silently sampled a third of the watchlist and SMCI was not in the
sample."

**Changed - the remedy.** Syncing 98 names into TradingView was unnecessary; they
were already there. Three symbols (SMCI, NVDA, AAPL) were re-added before this was
caught. TradingView de-duplicates, so no harm, but the sync should not continue.

## How this got past me

I ran `watchlist_get` once, saw a clean alphabetical run from BBAI to UBER, and
treated 58 as the list. It looked complete because a rendered window of an
alphabetically-sorted list *looks exactly like a complete short list*.

The check that would have caught it immediately: call it twice and compare, or
cross-check one known symbol. I did neither before building a root-cause claim on it
and writing it to memory. The same class of error as the sweep staleness trap caught
earlier the same day - plausible-looking output from a tool that silently returns a
partial view.

## Action items

1. Treat `watchlist_get` as **unreliable for universe construction**. Use it only for
   spot checks, never as a source of truth for coverage.
2. Build every universe from `watchlists/main-watchlist.md` via
   `scripts/build_og_sweep_universe.py`.
3. If the live watchlist must be read, scroll-and-accumulate, then assert the count
   against the repo file and fail loudly on mismatch.
4. Correct the claim in memory and in the `a822204` commit message (superseded here).
