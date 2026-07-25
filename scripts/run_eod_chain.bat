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
set TRIES=0
:feedcheck
curl -s --max-time 5 http://localhost:9222/json/version >nul 2>&1
if not errorlevel 1 goto feedup
set /a TRIES+=1
if !TRIES! geq 30 (
    echo [3/6] FAILED: TradingView CDP feed not reachable after 15 min >> "%LOG%"
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
python scripts\build_catalyst_calendar.py >> "%LOG%" 2>&1             || echo WARNING: catalyst_calendar failed >> "%LOG%"

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

:finish
if "!FAILED!"=="1" (
    echo ===== EOD CHAIN FAILED %date% %time% ===== >> "%LOG%"
    echo *** No trustworthy output for %TODAY% - do not act on any workbook dated %TODAY%. *** >> "%LOG%"
    endlocal
    exit /b 1
)
echo ===== EOD chain done OK %date% %time% (full pipeline) ===== >> "%LOG%"
endlocal
exit /b 0
