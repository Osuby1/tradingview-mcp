@echo off
rem ============================================================
rem Live Picks Radar runner - Windows Task Scheduler "Live Picks Radar".
rem Fires 3x/day Central: 9:00 AM (30m after open), 11:45 AM (midday), 3:05 PM (close).
rem Runs the radar; if it flags NEW confirmed/extended movers among OUR picks
rem (python exit 10), invokes headless Claude to push Omar. Log: reports\live_picks.log
rem ============================================================
setlocal
set REPO=C:\Users\osuby\tradingview-mcp
set LOG=%REPO%\reports\live_picks.log
cd /d "%REPO%"
for /f %%d in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set TODAY=%%d
echo. >> "%LOG%"
echo ===== Live Picks Radar START %date% %time% ===== >> "%LOG%"
python scripts\live_picks_radar.py >> "%LOG%" 2>&1
if errorlevel 10 (
    echo   NEW movers detected - pushing >> "%LOG%"
    claude -p "Read watchlists\live-picks-%TODAY%.md. Its 'NEW - act now' section lists OUR OWN recommended names that just started running. Send Omar exactly ONE PushNotification (status proactive, one line under 200 chars) naming the tickers with their %% gain-from-flag and the action - which are CONFIRMING (enter/add per plan) vs EXTENDED (do NOT chase, wait for a pullback). Then stop; do nothing else." >> "%LOG%" 2>&1
) else (
    echo   no new movers this run >> "%LOG%"
)
echo ===== Live Picks Radar DONE %date% %time% ===== >> "%LOG%"
endlocal
