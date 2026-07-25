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

rem Weekday gate (added 2026-07-25): the radar was firing on Saturdays and
rem Sundays - 338 price fetches per run against a closed market, and any "mover"
rem it reported would just be Friday's close re-read. Task Scheduler is set to
rem run daily, so the guard lives here.
for /f %%w in ('powershell -NoProfile -Command "[int](Get-Date).DayOfWeek"') do set DOW=%%w
if "%DOW%"=="0" goto :weekend
if "%DOW%"=="6" goto :weekend

echo. >> "%LOG%"
echo ===== Live Picks Radar START %date% %time% ===== >> "%LOG%"
python scripts\live_picks_radar.py >> "%LOG%" 2>&1
if errorlevel 10 (
    echo   NEW movers detected - pushing >> "%LOG%"
    claude -p "Read watchlists\live-picks-%TODAY%.md. It flags OUR OWN names that either JUST STARTED RUNNING ('NEW - act now' section) or just went BEAT-AND-HOLD after earnings ('Post-earnings watch' section = a clean PEAD entry). Send Omar exactly ONE PushNotification (status proactive, one line under 200 chars) naming the new tickers with their %% move and the action: CONFIRMING or beat-and-hold = enter/add per plan; EXTENDED = do NOT chase, wait for a pullback. Then stop; do nothing else." >> "%LOG%" 2>&1
) else (
    echo   no new movers this run >> "%LOG%"
)
echo ===== Live Picks Radar DONE %date% %time% ===== >> "%LOG%"
goto :done

:weekend
echo ===== Live Picks Radar SKIPPED (weekend) %date% %time% ===== >> "%LOG%"

:done
endlocal
