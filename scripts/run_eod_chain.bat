@echo off
rem ============================================================
rem EOD autonomous chain (Windows Task Scheduler, weekdays after close)
rem Log: reports\eod_chain.log
rem
rem UPGRADED 2026-07-22 to the FULL pipeline (was the basic 156-name / 10-tab run):
rem   1.  Origination scan (stage2_leader_scanner_v3.py)
rem   2.  Export Buy Zone / Fresh Ignitions / Coiled tabs to repo
rem   3.  DETERMINISTIC (2026-07-25): build_extended_universe.py -> og_sweep_cdp.mjs
rem       (a plain Node/CDP process that drives the Heikin Ashi sweep and CANNOT run
rem       out of turn/credit budget - fixes the 7/21 + 7/24 headless-Claude failures)
rem       -> build_universe_results.py (gate stack). Market movers is the only leftover
rem       LLM/web step and is NON-FATAL.
rem   3b. VERIFY step 3 produced TODAY's gated results (blocks a stale compile).
rem   4.  Deterministic Python analysis (run here, not via Claude, so it is
rem       reliable): rotation radar, ignition sweep, HQ Swing lens, track record,
rem       outcome tracker (dump prices + grade vs SPY).
rem   5.  Compile the full workbook (compile_universe_report_v2.py).
rem   6.  Commit everything.
rem
rem Safety rules kept from the 2026-07-22 fix:
rem   * A failed scan/verify STOPS the compile - no stale report ever.
rem   * The chain exits NON-ZERO + writes "EOD CHAIN FAILED" on any core failure.
rem   * Supplementary analysis (step 4) warns on failure but does NOT fail the run.
rem ============================================================
setlocal EnableDelayedExpansion
set REPO=C:\Users\osuby\tradingview-mcp
set LOG=%REPO%\reports\eod_chain.log
set FAILED=0
if not exist "%REPO%\reports" mkdir "%REPO%\reports"

for /f %%d in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set TODAY=%%d
set RAWSWEEP=%REPO%\watchlists\og-sweep-raw-%TODAY%-heikinashi.json

echo. >> "%LOG%"
echo ===== EOD chain start %date% %time% (target %TODAY%, FULL pipeline) ===== >> "%LOG%"

rem -- 0. Gate stack unit tests (added 2026-07-25) ---------------
rem The gate stack decides what is tradeable and its promise is that it FAILS
rem CLOSED. A regression there is a name quietly passing, which is invisible in
rem the output. Run the tests BEFORE the 40-minute sweep, and refuse to run the
rem pipeline on a broken gate rather than produce a confident wrong workbook.
cd /d "%REPO%"
echo [0/6] unit tests (gate stack + data contract)... >> "%LOG%"
python -m unittest discover -s tests -p "test_*.py" >> "%LOG%" 2>&1
if errorlevel 1 (
    echo FAILED: unit tests did not pass - refusing to run the pipeline. >> "%LOG%"
    set FAILED=1
    goto finish
)
rem The CDP target-picking test is JS, so the Python discover above cannot see it.
rem Added 2026-07-27 after the loose /tradingview/i match bound the MCP server to a
rem Desktop-app helper window all morning. That same race can kill step 3.
node --test tests\connection.test.js >> "%LOG%" 2>&1
if errorlevel 1 (
    echo FAILED: CDP target-picking tests did not pass - refusing to run the pipeline. >> "%LOG%"
    set FAILED=1
    goto finish
)

rem -- 1. Origination scan (refreshes recommendations_log for the Track Record) --
cd /d "%USERPROFILE%\Documents\Equities_Scanner"
echo [1/6] origination scan... >> "%LOG%"
python stage2_leader_scanner_v3.py --universe russell_starter.csv --no-open >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: origination scan exited nonzero >> "%LOG%"

rem -- 2. Export tabs into the repo -----------------------------
cd /d "%REPO%"
echo [2/6] export tabs... >> "%LOG%"
python scripts\export_origination_tabs.py >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: tab export failed >> "%LOG%"

rem -- 3. Extended universe + Heikin Ashi sweep + gates (headless Claude, needs chart) --
rem Wait for an actual CHART PAGE, not merely "the app answers CDP" (2026-07-27).
rem /json/version returns 200 as soon as the Desktop app is up, several seconds
rem before the chart tab exists - and the app's file:// helper windows used to get
rem picked in its place, which fails the sweep. Poll /json/list for a real
rem tradingview.com/chart page instead, so a slow chart is waited out.
set TRIES=0
:feedcheck
curl -s --max-time 5 http://localhost:9222/json/list | findstr /I /C:"tradingview.com/chart" >nul 2>&1
if not errorlevel 1 goto feedup
set /a TRIES+=1
if !TRIES! geq 30 (
    echo [3/6] FAILED: no TradingView CHART page on CDP after 15 min >> "%LOG%"
    echo        (app may be running with no chart tab open - helper windows do not count) >> "%LOG%"
    set FAILED=1
    goto finish
)
ping -n 31 127.0.0.1 >nul
goto feedcheck

:feedup
if /I "%~1"=="test" goto testrun
echo [3/6] DETERMINISTIC: build universe, Node/CDP HA sweep, gate stack... >> "%LOG%"
rem (a) build the extended ~480-name universe (Python - reliable)
python scripts\build_extended_universe.py %TODAY% >> "%LOG%" 2>&1
if errorlevel 1 ( echo FAILED: build_extended_universe.py >> "%LOG%" & set FAILED=1 & goto finish )
rem (b) drive the Heikin Ashi sweep via CDP as a PLAIN NODE PROCESS (not headless
rem     Claude) - it cannot run out of turn/credit budget, which is what killed the
rem     2026-07-21 and 2026-07-24 nightly runs. Writes og-sweep-raw-<date>-heikinashi.json.
node scripts\og_sweep_cdp.mjs %TODAY% >> "%LOG%" 2>&1
if errorlevel 1 ( echo FAILED: og_sweep_cdp.mjs - CDP sweep did not complete/verify >> "%LOG%" & set FAILED=1 & goto finish )
rem (c) gate stack (Python - fails closed; a name that cannot be gated is BLOCKED)
python scripts\build_universe_results.py "%RAWSWEEP%" "%RAWSWEEP%" %TODAY% >> "%LOG%" 2>&1
if errorlevel 1 ( echo FAILED: build_universe_results.py >> "%LOG%" & set FAILED=1 & goto finish )
rem (d) market movers - the ONLY remaining web/LLM bit, NON-FATAL (can't break the run)
claude -p "Fetch stockanalysis.com/markets/gainers and /losers, write watchlists/market-movers-%TODAY%.json as {gainers:[],losers:[]} with each item sym/company/price/pct_change/market_cap_raw/volume. If it fails, just stop - do not retry endlessly. Never wait for input." >> "%LOG%" 2>&1
if errorlevel 1 echo NOTE: market-movers step nonzero (non-fatal) >> "%LOG%"
goto verify

:testrun
echo [3/6] TEST MODE (deterministic, 5-name universe)... >> "%LOG%"
echo ["DVN","MLI","SJM","AAPL","XOM"]> watchlists\og-sweep-universe-%TODAY%-extended.json
node scripts\og_sweep_cdp.mjs %TODAY% >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: test CDP sweep failed >> "%LOG%"
python scripts\build_universe_results.py "%RAWSWEEP%" "%RAWSWEEP%" %TODAY% >> "%LOG%" 2>&1

rem -- 3b. VERIFY the scan produced today's gated data ----------
:verify
echo [3b/6] verifying scan output... >> "%LOG%"
python scripts\verify_eod_output.py %TODAY% >> "%LOG%" 2>&1
if errorlevel 1 (
    echo FAILED: scan output did not verify - SKIPPING everything downstream. >> "%LOG%"
    set FAILED=1
    goto finish
)

rem -- 4. Deterministic analysis (supplementary: warn, do not fail the run) ------
echo [4/6] analysis: rotation radar, ignition sweep, HQ Swing lens, track record, outcome tracker... >> "%LOG%"
rem readiness_batch (Omar standing order 2026-07-31, DGX post-mortem): score every
rem hit + gated long 0-100 on poised-to-move BEFORE the compile, so the workbook's
rem Readiness column is filled. NON-FATAL: on failure the column reads "n/a" and
rem the compiler will also try to compute it inline itself.
python scripts\readiness_batch.py %TODAY% >> "%LOG%" 2>&1              || echo WARNING: readiness_batch failed - Readiness column will read n/a >> "%LOG%"
rem rest_continuation_tracker (pre-registered 2026-08-01, Omar-adopted): tags every
rem candidate as rest-continuation cohort member / control per the FROZEN rule in
rem research\rest-continuation-preregistration.md. Measurement only - no trading
rem power. Runs AFTER readiness_batch (needs the readiness stamp). NON-FATAL.
python scripts\rest_continuation_tracker.py %TODAY% >> "%LOG%" 2>&1    || echo WARNING: rest_continuation_tracker failed - cohort not tagged tonight >> "%LOG%"
python scripts\rotation_radar.py >> "%LOG%" 2>&1                       || echo WARNING: rotation_radar failed >> "%LOG%"
python scripts\ignition_sweep.py >> "%LOG%" 2>&1                       || echo WARNING: ignition_sweep failed >> "%LOG%"
if exist "%RAWSWEEP%" (
    python scripts\hq_swing_lens.py "%RAWSWEEP%" >> "%LOG%" 2>&1       || echo WARNING: hq_swing_lens failed >> "%LOG%"
) else (
    echo WARNING: raw sweep file not found, skipping HQ Swing lens >> "%LOG%"
)
python scripts\track_record.py %TODAY% >> "%LOG%" 2>&1                 || echo WARNING: track_record failed >> "%LOG%"
python scripts\dump_call_prices.py %TODAY% >> "%LOG%" 2>&1             || echo WARNING: dump_call_prices failed >> "%LOG%"
python scripts\outcome_tracker.py %TODAY% >> "%LOG%" 2>&1              || echo WARNING: outcome_tracker failed >> "%LOG%"
rem gate_outcomes: forward-grades the scan's OWN cull (passed vs blocked). Added
rem 2026-07-25 - before it, the gate stack was unfalsifiable because only the ~14
rem hand-registered calls were ever graded.
python scripts\gate_outcomes.py >> "%LOG%" 2>&1                        || echo WARNING: gate_outcomes failed >> "%LOG%"
rem og_shadow: grades the chart-free Python port against the night's chart truth.
rem Added to the chain 2026-07-25 because nothing called it, so when the results
rem schema changed on 7/21 it silently exited "nothing to grade" for four days.
python scripts\og_shadow.py %TODAY% >> "%LOG%" 2>&1                    || echo WARNING: og_shadow failed >> "%LOG%"
python scripts\build_catalyst_calendar.py >> "%LOG%" 2>&1             || echo WARNING: catalyst_calendar failed >> "%LOG%"
rem market_structure (added 2026-07-28): the day's path, close-within-range, and
rem rebound-vs-giveback that the Market ^& Rotation tab needs. Non-fatal - without
rem it that tab degrades to the old radar-only view rather than blocking the run.
python scripts\market_structure.py %TODAY% >> "%LOG%" 2>&1            || echo WARNING: market_structure failed - tab 1 will be radar-only >> "%LOG%"
rem ratchet watch (added 2026-07-25): maintains the 20%% trailing-ratchet exit
rem alerts on the REAL open book (watchlists\open-book.json). The Python step
rem decides, the Node/CDP step does the TradingView REST work in page context.
python scripts\ratchet_watch.py >> "%LOG%" 2>&1                        || echo WARNING: ratchet_watch failed - open-book ratchet NOT updated >> "%LOG%"
if exist "%REPO%\watchlists\ratchet-actions.json" (
    node scripts\ratchet_alerts.mjs >> "%LOG%" 2>&1                    || echo WARNING: ratchet_alerts failed - a ratchet alert was NOT wired on TV >> "%LOG%"
)

rem -- 5. Compile the full workbook ----------------------------
echo [5/6] compile full workbook (explicit date %TODAY%)... >> "%LOG%"
python scripts\compile_universe_report_v2.py %TODAY% >> "%LOG%" 2>&1
if errorlevel 1 (
    echo FAILED: report compile exited nonzero >> "%LOG%"
    set FAILED=1
    goto finish
)

rem -- 6. Commit everything ------------------------------------
echo [6/6] commit... >> "%LOG%"
git add reports watchlists research >> "%LOG%" 2>&1
git commit -m "EOD chain %TODAY% (full pipeline, automated)" >> "%LOG%" 2>&1
if errorlevel 1 echo NOTE: nothing to commit or commit failed (non-fatal) >> "%LOG%"

rem -- 7. Brief check (added 2026-07-25) -------------------------
rem The standing rule is that every EOD owes TWO artifacts: the workbook AND
rem daily-ignition-brief\<date>-eod.md. That rule was written 7/22 and broken on
rem both 7/23 and 7/24 - the workbooks appeared, the briefs did not, and nobody
rem noticed until an audit. The chain cannot write the brief (it needs judgement)
rem but it must not look like a clean run without one.
if not exist "%REPO%\daily-ignition-brief\%TODAY%-eod.md" (
    echo *** MISSING BRIEF: daily-ignition-brief\%TODAY%-eod.md was never written. >> "%LOG%"
    echo *** The workbook alone is NOT the deliverable - write the brief. >> "%LOG%"
)

:finish
rem -- 8. TELL OMAR (added 2026-07-25) ---------------------------
rem Until now this chain's entire "fail loudly" design terminated in a log file
rem nobody reads. On 2026-07-24 it failed at 15:25 and that went unnoticed for
rem ~8 hours. Meanwhile run_live_picks.bat - a far less important job - pushes to
rem his phone. The critical job now pushes too, on BOTH outcomes, so that silence
rem from this chain is itself suspicious rather than reassuring.
set BRIEFMISSING=0
if not exist "%REPO%\daily-ignition-brief\%TODAY%-eod.md" set BRIEFMISSING=1
if "!FAILED!"=="1" (
    claude -p "The EOD universe chain FAILED for %TODAY%. Read the last 60 lines of reports\eod_chain.log, find the step that failed and why. Send Omar exactly ONE PushNotification (status proactive, one line under 200 chars): say the EOD scan failed, name the failing step in plain English, and warn that there is NO trustworthy workbook for %TODAY%. Then stop; do nothing else." >> "%LOG%" 2>&1
) else (
    if "!BRIEFMISSING!"=="1" (
        claude -p "The EOD universe chain completed for %TODAY% but the brief file daily-ignition-brief\%TODAY%-eod.md was never written. Send Omar exactly ONE PushNotification (status proactive, one line under 200 chars): the scan ran clean and the workbook is ready, but the written brief is MISSING. Then stop; do nothing else." >> "%LOG%" 2>&1
    ) else (
        claude -p "The EOD universe chain completed cleanly for %TODAY%. Read watchlists\universe-results-%TODAY%.json for scanned/fresh counts and how many names passed every gate. Send Omar exactly ONE PushNotification (status proactive, one line under 200 chars): confirm the scan ran clean, give the scanned count, the fresh-signal count and the number that cleared every gate. Then stop; do nothing else." >> "%LOG%" 2>&1
    )
)

if "!FAILED!"=="1" (
    echo ===== EOD CHAIN FAILED %date% %time% ===== >> "%LOG%"
    echo *** No trustworthy output for %TODAY% - do not act on any workbook dated %TODAY%. *** >> "%LOG%"
    endlocal
    exit /b 1
)
echo ===== EOD chain done OK %date% %time% (full pipeline) ===== >> "%LOG%"
endlocal
exit /b 0
