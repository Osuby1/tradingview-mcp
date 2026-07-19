@echo off
rem ============================================================
rem EOD autonomous chain (registered in Windows Task Scheduler):
rem   1. Origination scan (stage2_leader_scanner_v3.py)
rem   2. Export Buy Zone / Fresh Ignitions / Coiled tabs to repo
rem   3. Claude headless: "run the universe" (needs TV open w/ CDP)
rem   4. Compile the daily Excel report
rem Runs weekdays after the close. Log: reports\eod_chain.log
rem ============================================================
setlocal
set REPO=C:\Users\osuby\tradingview-mcp
set LOG=%REPO%\reports\eod_chain.log
if not exist "%REPO%\reports" mkdir "%REPO%\reports"

echo. >> "%LOG%"
echo ===== EOD chain start %date% %time% ===== >> "%LOG%"

rem -- 1. Origination scan --------------------------------------
cd /d "%USERPROFILE%\Documents\Equities_Scanner"
echo [1/4] origination scan... >> "%LOG%"
python stage2_leader_scanner_v3.py --universe russell3000.csv --no-open >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: origination scan exited nonzero >> "%LOG%"

rem -- 2. Export tabs into the repo + archive a dated xlsx copy --
cd /d "%REPO%"
echo [2/4] export tabs... >> "%LOG%"
python scripts\export_origination_tabs.py >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: tab export failed - universe will run watchlists-only >> "%LOG%"
powershell -NoProfile -Command "Copy-Item \"$env:USERPROFILE\Documents\Equities_Scanner\origination_scan.xlsx\" (\"%REPO%\reports\origination_scan_\" + (Get-Date -Format yyyy-MM-dd) + \".xlsx\") -Force" >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: dated origination xlsx archive failed >> "%LOG%"

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
    goto report
)
timeout /t 30 /nobreak >nul
goto feedcheck
:feedup
if /I "%~1"=="test" goto testrun
echo [3/4] claude run-the-universe... >> "%LOG%"
claude -p "run the universe - autonomous EOD chain run: on MONDAY and WEDNESDAY run the FULL universe, on Tue/Thu/Fri use the fast convergence variant; write the machine-readable results JSON for the report compiler; commit everything via the PowerShell tool; if anything blocks, log it in the results file instead of waiting for input" >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: claude universe run exited nonzero >> "%LOG%"
goto report

:testrun
echo [3/4] claude run-the-universe TEST MODE... >> "%LOG%"
claude -p "run the universe TEST MODE - smoke test of the autonomous chain: scan ONLY the origination Buy Zone and Fresh Ignitions tabs from watchlists/origination-tabs.md, about 26 names, through the O.G Chandelier chart per the run-the-universe memory; skip Coiled and the watchlists this time; run the protocol gates lightly on any fresh hits; you MUST write watchlists/universe-results-<date>.json in the schema from memory rule 8 with variant set to test, even if hits are empty, and commit it; never wait for user input - log any blocker into the JSON notes field; market is closed so Friday's bars are expected" >> "%LOG%" 2>&1
if errorlevel 1 echo WARNING: claude test run exited nonzero >> "%LOG%"

:report
rem -- 4. Compile the daily Excel report ------------------------
echo [4/4] compile report... >> "%LOG%"
python scripts\compile_daily_report.py >> "%LOG%" 2>&1
echo ===== EOD chain done %date% %time% ===== >> "%LOG%"
endlocal
