Set WshShell=CreateObject("WScript.Shell")
WshShell.run chr(34) & "C:\ProgramData\start.bat" & chr(34), 0
Set WshShell = Nothing