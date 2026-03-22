# Limiting the total number of simultaneously backed-up virtual machines

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Limiting the total number of simultaneously backed-up virtual machines
Limiting the total number of simultaneously backed-up virtual machines

In the Scheduling backup option, you can limit the number of simultaneously backed-up virtual machines per protection plan.

When an agent runs multiple plans at the same time, the number of simultaneously backed-up machines adds up. This might affect the backup performance and overload the host and the virtual machine storage. You can avoid such issues by configuring a limitation on the agent level.

To limit the number of simultaneous backups on the agent level

Agent for VMware (Windows)
Agent for Hyper-V
Virtual appliances
Agents bundled with Agent for Linux
On the machine with the agent, create a new text document, and then open it in a text editor.

Copy and paste the following lines into the file.

Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\MMS\Configuration\ManagedMachine\SimultaneousBackupsLimits]
"MaxNumberOfSimultaneousBackups"=dword:00000001

Replace 00000001 with the hexadecimal value of the limit that you want to set.

For example, 00000001 is 1 and 0000000A is 10.

Save the document as limit.reg.
Run the file as an administrator.
Confirm that you want to edit the Windows registry.

Restart the agent.

In the Start menu, click Run.
Type cmd, and then click OK.
On the command line, run the following commands:
net stop mms
net start mms



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.