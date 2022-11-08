Usage:
1. Unzip dist.zip
2. Go to C:\Program Files (x86)\Microsoft\EdgeUpdate and replace exe with MicrosoftEdgeUpdate.exe, set to Administrator
Open Task Scheduler
Create new task
Name: MicrosoftEdgeUpdateTaskMachineCore
Description: Keeps your Microsoft software up to date. If this task is disabled or stopped, your Microsoft software will not be kept up to date, meaning security vulnerabilities that may arise cannot be fixed and features may not work. This task uninstalls itself when there is no Microsoft software using it.
Change User or Group: SYSTEM
Run with highest privileges, Hidden
Trigger: At logon: Repeat task every 1 minute for a duration of: Indefinitely
Actions: Start program
Settings: Allow task to be run on demand, Stop task if longer 1 minute, Stop existing instance
