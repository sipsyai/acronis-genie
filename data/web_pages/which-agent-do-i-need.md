# Which agent do I need?

Installing and deploying Cyber Protection agents > Before you start > Which agent do I need?
Which agent do I need?

Selecting an agent depends on what you are going to back up. The table below summarizes the information, to help you decide.

In Windows, Agent for Exchange, Agent for SQL, Agent for Active Directory, and Agent for Oracle require that Agent for Windows is also installed. Thus, if you install, for example, Agent for SQL, you also will be able to back up the entire machine where the agent is installed.

We recommend that you also install Agent for Windows when you install Agent for VMware (Windows) and Agent for Hyper-V.

In Linux, Agent for Oracle, Agent for MySQL/MariaDB, Agent for Virtuozzo, and Agent for Proxmox require that Agent for Linux (64-bit) is also installed. These agents are bundled into the Agent for Linux (64-bit) installation file.

What are you going to back up?	Which agent to install?	Where to install it?


Physical machines


Physical machines running Windows	Agent for Windows	On the machine that will be backed up.
Physical machines running Linux	Agent for Linux
Physical machines running macOS	Agent for Mac


Databases


SQL databases

Agent for SQL

On the machine running Microsoft SQL Server.
MySQL databases

Agent for MySQL/MariaDB

(Bundled into the Agent for Linux (64-bit) installation file)

On the machine running MySQL Server.
MariaDB databases

Agent for MySQL/MariaDB

(Bundled into the Agent for Linux (64-bit) installation file)

On the machine running MariaDB Server.
Exchange databases

Agent for Exchange

On the machine running the Mailbox role of Microsoft Exchange Server.*
Oracle databases

Agent for Oracle

(In Linux, bundled into the Agent for Linux (64-bit) installation file)

On the machine running Oracle Database.
Cloud-to-cloud workloads


Microsoft 365 mailboxes

(Cloud agent or local agent)



Cloud agent

(No installation required)



This functionality is available with a cloud agent that is deployed in the data center. For more information, see Comparison of backup solutions for Microsoft 365 data.




Agent for Office 365

On a Windows machine that is connected to the Internet. For more information, see Locally installed Agent for Office 365.
Microsoft 365 OneDrive files and SharePoint Online sites

Cloud agent

(No installation required)



This functionality is available with a cloud agent that is deployed in the data center. For more information, see Comparison of backup solutions for Microsoft 365 data.


Google Workspace Gmail mailboxes, Google Drive files, and Shared drive files

Cloud agent

(No installation required)



This functionality is available with a cloud agent that is deployed in the data center. For more information, see Protecting Google Workspace data.


Active Directory
Machines running Active Directory Domain Services

Agent for Active Directory

On the domain controller.


Virtual machines


VMware ESXi (Broadcom) virtual machines	Agent for VMware (Windows)	On a Windows machine that has network access to vCenter Server and to the virtual machine storage.**
Agent for VMware (Virtual Appliance)	On the ESXi host.
Microsoft Hyper-V virtual machines	Agent for Hyper-V	On the Hyper-V host.
Scale Computing HyperCore virtual machines	Agent for Scale Computing HC3
(Virtual Appliance)	On the Scale Computing HyperCore host.
Nutanix virtual machines	Agent for Nutanix AHV (Virtual appliance)	On the Nutanix AHV host.
Proxmox virtual machines

Agent for Proxmox

(Bundled into the Agent for Linux (64-bit) installation file)

On the Proxmox VE host.
Red Hat Virtualization virtual machines (managed by oVirt)	Agent for oVirt (Virtual Appliance)	On the Red Hat Virtualization host.
Virtuozzo Hybrid Server virtual machines and containers***

Agent for Virtuozzo

(Bundled into the Agent for Linux (64-bit) installation file)

On the Virtuozzo Hybrid Server host.
Virtuozzo Hybrid Infrastructure virtual machines

Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance)

On the Virtuozzo Hybrid Infrastructure host.
Virtual machines hosted on Amazon EC2	The same as for physical machines****	On the machine that will be backed up.
Virtual machines hosted on Windows Azure
Citrix Hypervisor/XenServer virtual machines
Red Hat Virtualization (RHV/RHEV), not managed by oVirt
Kernel-based Virtual Machines (KVM), not managed by oVirt
Oracle virtual machines, not managed by oVirt
Red Hat Virtualization (RHV/RHEV), managed by oVirt

Agent for oVirt (Virtual Appliance)

On the virtualization host.
Kernel-based Virtual Machines (KVM), managed by oVirt
Oracle virtual machines, managed by oVirt
Network-attached storage
Synology	Agent for Synology (Virtual Appliance)	On the NAS device.


Mobile devices


Mobile devices running Android	Mobile app for Android	On the mobile device that will be backed up.
Mobile devices running iOS	Mobile app for iOS

*During the installation, Agent for Exchange checks for enough free space on the machine where it will run. Free space equal to 15 percent of the biggest Exchange database is temporarily needed during a granular recovery.

**If your ESXi uses a SAN attached storage, install the agent on a machine connected to the same SAN. The agent will back up the virtual machines directly from the storage rather than via the ESXi host and LAN. For detailed instructions, see Agent for VMware - LAN-free backup.

***For Virtuozzo 7, only ploop containers are supported. Virtual machines are not supported.

****A virtual machine is considered virtual if it is backed up by an external agent. If an agent is installed in the guest system, the backup and recovery operations are the same as with a physical machine. Nevertheless, if Cyber Protection can identify a virtual machine by using the CPUID instruction, a virtual machine service quota is assigned to it. If you use direct passthrough or another option that masks the CPU manufacturer ID, only service quotas for physical machines can be assigned.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.