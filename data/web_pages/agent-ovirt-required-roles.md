# Agent for oVirt – required roles and ports

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for oVirt (Virtual Appliance) > Agent for oVirt – required roles and ports
Agent for oVirt – required roles and ports
Required roles

For its deployment and operation, Agent for oVirt requires an administrator account with the following roles assigned.

oVirt/Red Hat Virtualization 4.2 and 4.3/Oracle Virtualization Manager 4.3
DiskCreator
UserVmManager
TagManager
UserVmRunTimeManager
VmCreator
oVirt/Red Hat Virtualization 4.4, 4.5

SuperUser

Required ports

Agent for oVirt connects to the oVirt Engine by using the URL that you specify when you configure the virtual appliance. Usually, the engine URL has the following format: https://ovirt.company.com. In this case, the HTTPS protocol and port 443 are used.

Non-default oVirt settings may require another port. You can find the exact port by analyzing the URL format. For example:

oVirt Engine URL	Port	Protocol
https://ovirt.company.com/	443	HTTPS
http://ovirt.company.com/	80	HTTP
https://ovirt.company.com:1234/	1234	HTTPS

No additional ports are required for disk Read/Write operations, because the backup is performed in the HotAdd mode.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.