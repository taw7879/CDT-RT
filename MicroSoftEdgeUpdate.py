import os
import subprocess
import time

def power_run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=False)
    return completed

command = "Get-PnpDevice -Class 'Mouse' | select InstanceId > MouseDrivers.txt"
mouse = power_run(command)
f = open("MouseDrivers.txt", encoding='utf-16')
lines = f.readlines()
mouses = list()
for line in lines:
    if 'HID' in line:
        line = line[:len(line)-1]
        mouses.append(line)
for mouse in mouses:
    command = "pnputil /disable-device \"" + mouse + "\""
    os.popen(command)
time.sleep(12)
for mouse in mouses:
    command = "pnputil /enable-device \"" + mouse + "\""
    os.popen(command)
f.close()
