@echo off
rem ============================================================
rem EOD autonomous chain (Windows Task Scheduler, weekdays after close)
rem   1. Origination scan (stage2_leader_scanner_v3.py)
rem   2. Export Buy Zone / Fresh Ignitions / Coiled tabs to repo
rem   3. Claude headless: "run the universe" (needs TV open w/ CDP)
rem   3b. VERIFY step 3 actually produced TODAY's results
rem   4. Compile the daily Excel workbook (v2/v3 layout)
rem Log: reports\eod_chain.log
rem
rem REWRITTEN 2026-07-22 after the chain silently shipped a stale report.
rem
rem What went wrong on 2026-07-21:
rem   step 3 died ("out of usage credits"), the chain logged a WARNING and
rem   carried on, and step 4 compiled 07-20's leftover results into a report
rem   while running on 07-21 - then logged "EOD chain done". Half of recent
rem   runs also died mid-way with no alert at all.
rem
rem Three rules now enforced:
rem   * A failed step 3 STOPS the report. No stale compile, ever.
rem   * The chain exits NON-ZERO and writes "EOD CHAIN FAILED" so Task
rem     Scheduler shows a failure instead of a green tick.
rem   * Step 4 uses compile_universe_report_v2.py (the current layout),
rem     with an explicit date - not "newest file it can find".
rem ============================================================
setlocal EnableDelayedExpansion
set REPO=C:\Users\osuby\tradingview-mcp
set LOG=%REPO%\reports\eod_chain.log
set FAILED=0
if not exist "%REPO%\reports" mkdir "%REPO%\reports"

rem Locale-independent ISO date (the %date% builtin varies by machine locale)
for /f %%d in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set TODAY=%%d

echo. >> "%LOG%"
echo ===== EOD chain start %date% %time% (target %TODAY%) ===== >> "%LOG%"

rem -- 1. Origination scan --------------------------------------
cd /d "%USERPROFILE%\Documents\Equities_Scanner"
echo [1/4] origination scan... >> "%LOG%"
python stage2_leader_scanner_v3.py --universe russell_starter.csv --no-open >> "%LOG%" 2>&1
if errorlevel 1 (
    echo WARNING: origination scan exited nonzero - universe will run watchlists-only >> "%LOG%"
)

rem -- 2. Export tabs into the repo + archive a dated xlsx copy --
cd /d "%REPO%"
echo [2/4] export tabs... >> "%LOG%"
python scripts\export_origination_tabs.py >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: tab export failed >> "%LOG%"

rem -- 3. Universe scan via headless Claude ---------------------
rem Requires TradingView desktop open with CDP on :9222.
rem Grace period: up to 15 min (30 x 30s) for the feed to come up.
set TRIES=0
:feedcheck
curl -s --max-time 5 http://localhost:9222/json/version >nul 2>&1
if not errorlevel 1 goto feedup
set /a TRIES+=1
if !TRIES! geq 30 (
    echo [3/4] FAILED: TradingView CDP feed not reachable after 15 min >> "%LOG%"
    set FAILED=1
    goto finish
)
rem ping-based 30s sleep - timeout.exe is unreliable under Task Scheduler
ping -n 31 127.0.0.1 >nul
goto feedcheck

:feedup
if /I "%~1"=="test" goto testrun
echo [3/4] claude run-the-universe... >> "%LOG%"
claude -p "run the universe - autonomous EOD chain run for %TODAY%. Scan on CANDLES only (never Heikin Ashi). Build the universe from watchlists/main-watchlist.md via scripts/build_og_sweep_universe.py - do NOT use watchlist_get, it returns only rendered DOM rows. Sweep with scripts/og_sweep_runner.js, which captures regime (200/50 SMA, ADX, DI) and 20-day average dollar volume inline. Then run scripts/build_universe_results.py to apply the MANDATORY gate stack in scripts/gate_stack.py (regime, ADX>=20, +DI>-DI, above ZLSMA, liquidity) - a name that cannot be gate-evaluated must be BLOCKED, never passed. Write watchlists/universe-results-%TODAY%.json with the date field set to %TODAY%, every hit carrying a verdict and a gates object, and any problems recorded as severity-ranked data_quality entries. Zero passing names is a valid and honest result - do not relax a gate to produce a candidate. Commit via the PowerShell tool. Never wait for user input; log any blocker into the JSON instead." >> "%LOG%" 2>&1
if errorlevel 1 (
    echo WARNING: claude universe run exited nonzero >> "%LOG%"
)
goto verify

:testrun
echo [3/4] claude run-the-universe TEST MODE... >> "%LOG%"
claude -p "run the universe TEST MODE for %TODAY% - smoke test of the autonomous chain: scan ONLY the origination Buy Zone and Fresh Ignitions tabs from watchlists/origination-tabs.md, about 26 names, on CANDLES through the O.G Chandelier. Apply the full gate stack from scripts/gate_stack.py. You MUST write watchlists/universe-results-%TODAY%.json with date=%TODAY%, variant=test, every hit carrying a verdict and a gates object, even if there are no hits. Commit it. Never wait for user input - log blockers into the JSON." >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: claude test run exited nonzero >> "%LOG%"

rem -- 3b. VERIFY the scan really produced today's data ----------
:verify
echo [3b/4] verifying scan output... >> "%LOG%"
python scripts\verify_eod_output.py %TODAY% >> "%LOG%" 2>&1
if errorlevel 1 (
    echo FAILED: scan output did not verify - SKIPPING the report on purpose. >> "%LOG%"
    echo         Compiling now would ship an older run stamped as today. >> "%LOG%"
    set FAILED=1
    goto finish
)

rem -- 4. Compile the daily Excel workbook ----------------------
echo [4/4] compile report (v3 layout, explicit date %TODAY%)... >> "%LOG%"
python scripts\compile_universe_report_v2.py %TODAY% >> "%LOG%" 2>&1
if errorlevel 1 (
    echo FAILED: report compile exited nonzero >> "%LOG%"
    set FAILED=1
)

:finish
if "!FAILED!"=="1" (
    echo ===== EOD CHAIN FAILED %date% %time% ===== >> "%LOG%"
    echo *** No trustworthy output was produced for %TODAY%. Do not act on any *** >> "%LOG%"
    echo *** universe workbook dated %TODAY% - check this log first.           *** >> "%LOG%"
    endlocal
    exit /b 1
)
echo ===== EOD chain done OK %date% %time% ===== >> "%LOG%"
endlocal
exit /b 0
