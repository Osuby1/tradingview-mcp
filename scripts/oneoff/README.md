# Spent one-off scripts

Scripts here have already run and are kept only as a record of what was done to
the data. Nothing calls them. Do not re-run them — several mutate dated JSON
files in place and would double-apply.

| Script | Ran | What it did |
|---|---|---|
| `_log_dq_20260723.py` | 2026-07-23 | Wrote the chart/web-side blockers found during the EOD run into `universe-results-2026-07-23.json` data_quality (the compiler only sees the sweep file, so it can't know what happened while the sweep was taken). |
| `_merge_fixups_20260723.py` | 2026-07-23 | Folded corrected BHP/EQR re-reads into the raw HA sweep — both bare tickers had resolved to their ASX listings in AUD. The symbol-resolution trap. |
| `_mk_alertboard_20260723.py` | 2026-07-23 | Built `watchlists/alert-board.json` from an in-page dump of TradingView's alert list: 379 raw alerts → 287 unique symbols. |
| `build_catalyst_mvp.bat` | 2026-07-23 | One-time Task Scheduler job that built the catalyst-feed MVP. The task has fired; the nightly refresh now lives in `run_eod_chain.bat`. |
