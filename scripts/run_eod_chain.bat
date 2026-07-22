@echo off
rem ============================================================
rem EOD autonomous chain (registered in Windows Task Scheduler):
rem   1. Origination scan (stage2_leader_scanner_v3.py)
rem   2. Export Buy Zone / Fresh Ignitions / Coiled tabs to repo
rem   3. Claude headless: "run the universe" (needs TV open w/ CDP)
rem      Each model in %MODELS% is tried in order, so one model being
rem      out of credits no longer kills the whole universe leg.
rem   4. Compile the daily Excel report. The compiler refuses to
rem      republish an older day's results, so a failed step 3 can
rem      never masquerade as a fresh report.
rem Runs weekdays after the close. Log: reports\eod_chain.log
rem Exit code: 0 = chain complete, 1 = ran but INCOMPLETE (see log).
rem ============================================================
setlocal
set REPO=C:\Users\osuby\tradingview-mcp
set LOG=%REPO%\reports\eod_chain.log
set RC=0
rem Universe-leg model fallback, in order - first one that works wins.
rem Deliberately capable models only: this leg makes sized trade calls,
rem so it fails loudly rather than degrading to a cheaper model.
set "MODELS=claude-opus-4-8 claude-sonnet-5"
set UOK=0
if not exist "%REPO%\reports" mkdir "%REPO%\reports"

echo. >> "%LOG%"
echo ===== EOD chain start %date% %time% ===== >> "%LOG%"

rem -- 1. Origination scan --------------------------------------
cd /d "%USERPROFILE%\Documents\Equities_Scanner"
echo [1/4] origination scan... >> "%LOG%"
python stage2_leader_scanner_v3.py --universe russell_starter.csv --no-open >> "%LOG%" 2>&1
if errorlevel 1 (
    echo WARNING: origination scan exited nonzero >> "%LOG%"
    set RC=1
)

rem -- 2. Export tabs into the repo + archive a dated xlsx copy --
cd /d "%REPO%"
echo [2/4] export tabs... >> "%LOG%"
python scripts\export_origination_tabs.py >> "%LOG%" 2>&1
if errorlevel 1 (
    echo WARNING: tab export failed - universe will run watchlists-only >> "%LOG%"
    set RC=1
)
rem (dated origination_scan_<date>.xlsx archive is done inside export_origination_tabs.py)

rem -- 3. Universe scan via headless Claude ---------------------
rem Requires TradingView desktop open with CDP on :9222.
rem Grace period: wait up to 15 min (30 x 30s) for the feed, so a
rem catch-up run at login has time for TV to come up.
set TRIES=0
:feedcheck
curl -s --max-time 5 http://localhost:9222/json/version >nul 2>&1
if not errorlevel 1 goto feedup
set /a TRIES+=1
if %TRIES% geq 30 (
    echo [3/4] SKIPPED: TradingView CDP feed not reachable after 15 min of waiting >> "%LOG%"
    set RC=1
    goto report
)
rem ping-based 30s sleep - reliable in non-interactive Task Scheduler context (timeout.exe is not)
ping -n 31 127.0.0.1 >nul
goto feedcheck
:feedup
if /I "%~1"=="test" goto testrun
echo [3/4] claude run-the-universe... >> "%LOG%"
set "UPROMPT=run the universe - autonomous EOD chain run: on MONDAY and WEDNESDAY run the FULL universe, on Tue/Thu/Fri use the fast convergence variant; if today is SATURDAY or SUNDAY this is a catch-up run of a missed weekday - use the FAST variant on the latest settled data and say so in the results notes; write the machine-readable results JSON for the report compiler; commit everything via the PowerShell tool; if anything blocks, log it in the results file instead of waiting for input"
for %%M in (%MODELS%) do call :tryclaude %%M
if "%UOK%"=="0" (
    echo WARNING: universe leg FAILED on every model (%MODELS%) - no fresh results JSON this run >> "%LOG%"
    set RC=1
)
goto report

:testrun
echo [3/4] claude run-the-universe TEST MODE... >> "%LOG%"
set "UPROMPT=run the universe TEST MODE - smoke test of the autonomous chain: scan ONLY the origination Buy Zone and Fresh Ignitions tabs from watchlists/origination-tabs.md, about 26 names, through the O.G Chandelier chart per the run-the-universe memory; skip Coiled and the watchlists this time; run the protocol gates lightly on any fresh hits; you MUST write watchlists/universe-results-<date>.json in the schema from memory rule 8 with variant set to test, even if hits are empty, and commit it; never wait for user input - log any blocker into the JSON notes field; market is closed so Friday's bars are expected"
for %%M in (%MODELS%) do call :tryclaude %%M
if "%UOK%"=="0" (
    echo WARNING: universe TEST leg FAILED on every model (%MODELS%) >> "%LOG%"
    set RC=1
)

:report
rem -- 4. Compile the daily Excel report ------------------------
rem compile_daily_report.py compiles TODAY's results only; if step 3
rem wrote nothing it exits nonzero instead of rewriting an old report.
echo [4/4] compile report... >> "%LOG%"
python scripts\compile_daily_report.py >> "%LOG%" 2>&1
if errorlevel 1 (
    echo WARNING: no fresh report written this run - see compiler message above >> "%LOG%"
    set RC=1
)

:done
if "%RC%"=="0" (
    echo ===== EOD chain done %date% %time% STATUS=OK ===== >> "%LOG%"
) else (
    echo ===== EOD chain done %date% %time% STATUS=INCOMPLETE - see WARNINGs above ===== >> "%LOG%"
)
endlocal & exit /b %RC%

rem -- helper: run the universe prompt on one model --------------
rem %1 = model id. No-ops once an earlier model has already succeeded.
:tryclaude
if "%UOK%"=="1" goto :eof
echo   -- model %1 ... >> "%LOG%"
claude --model %1 -p "%UPROMPT%" >> "%LOG%" 2>&1
if errorlevel 1 (
    echo   WARNING: model %1 exited nonzero - falling back to next model >> "%LOG%"
    goto :eof
)
set UOK=1
echo   universe leg OK on model %1 >> "%LOG%"
goto :eof
