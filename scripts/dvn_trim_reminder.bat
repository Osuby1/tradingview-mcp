@echo off
rem ============================================================
rem One-time reminder: trim DVN before its 2026-08-04 earnings.
rem Task Scheduler "DVN Trim Reminder", fires Mon 2026-08-03 ~8:45 AM CT.
rem Log: reports\reminders.log
rem ============================================================
setlocal
cd /d C:\Users\osuby\tradingview-mcp
echo. >> reports\reminders.log
echo ===== DVN trim reminder fired %date% %time% ===== >> reports\reminders.log
claude -p "Scheduled DVN trim reminder - it is Mon 2026-08-03, the last trading day before DVN's 2026-08-04 earnings. Pull DVN's current price via quote_get NYSE:DVN, then send Omar exactly ONE PushNotification (status proactive, one line under 200 chars): remind him to TRIM or EXIT his DVN long (1000 sh @ 45.11) ahead of the 8/4 print - do NOT hold full size through the binary - and include DVN's current price and gain from 45.11. Then stop; do nothing else." >> reports\reminders.log 2>&1
echo ===== done %date% %time% ===== >> reports\reminders.log
endlocal
