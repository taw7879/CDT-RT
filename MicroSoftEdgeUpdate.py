# Name: Thomas Wang
# email: taw7879@rit.edu
# This tool will disable the mouse by disabling its drivers and deleting its registry keys
import os
import subprocess
import time


def power_run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    return completed

# gets list of InstanceIds of all mouse drivers
command = "Get-PnpDevice -Class 'Mouse' | select InstanceId > mouses.txt"
mouse = power_run(command)
#finds actual InstanceIds of mouse drivers
f = open("mouses.txt", encoding='utf-16')
lines = f.readlines()
mouses = list()
for line in lines:
    if 'HID' in line:
        line = line[:len(line)-1]
        mouses.append(line)
#disables mouse drivers
for mouse in mouses:
    #command = "pnputil /disable-device \"" + mouse + "\""
    command = "dir"
    os.system(command)

time.sleep(20)
for mouse in mouses:
    #command = "pnputil /enable-device \"" + mouse + "\""
    command = "dir"
    os.system(command)

#deletes registry keys
#p = os.popen("reg delete HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\mouclass", "w")
#p.write("y\n")
#p = os.popen("reg add HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\mouclass% /v Start /t REG_DWORD /d 4", "w")
#p.write("y\n")

