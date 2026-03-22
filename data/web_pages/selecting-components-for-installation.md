# Agent components

Installing and deploying Cyber Protection agents > Device discovery > Discovering multiple devices > Agent components
Agent components

When you add multiple devices that were discovered by searching in the Active Directory, you can select to install additional components.

The following table provides more information about the agent components that you can install.

Component	Description


Mandatory component


Agent for Windows	This agent backs up disks, volumes, files and will be installed on Windows machines. It will be always installed, not selectable.


Additional components


Agent for Data Loss Prevention	This agent enables you to limit the user access to local and redirected peripheral devices, ports, and clipboard on machines under protection plans. It will be installed if selected.


Antimalware and URL filtering

Antimalware



This component enables the Antivirus & Antimalware protection and URL filtering module in protection plans. Even if you select not to install it, it will be automatically installed later, if any of these modules is enabled in a protection plan for the machine.

This component enables the Antivirus & Antimalware protection module in protection plans. Even if you select not to install it, it will be automatically installed later, if this module is enabled in a protection plan for the machine.


Agent for Hyper-V	This agent backs up Hyper-V virtual machines. It will be installed on Hyper-V hosts. It will be installed if selected and detected Hyper-V role on a machine.
Agent for SQL	This agent backs up SQL Server databases. It will be installed on machines running Microsoft SQL Server. It will be installed if selected and application detected on a machine.
Agent for Exchange	This agent backs up Exchange databases and mailboxes. It will be installed on machines running the Mailbox role of Microsoft Exchange Server. It will be installed if selected and application detected on a machine.
Agent for Active Directory	This agent backs up the data of Active Directory Domain Services. It will be installed on domain controllers. It will be installed if selected and application detected on a machine.
Agent for VMware (Windows)	This agent backs up VMware virtual machines. It will be installed on Windows machines that have network access to vCenter Server. It will be installed if selected.
Agent for Microsoft 365	This agent backs up Microsoft 365 mailboxes to a local destination. It will be installed on Windows machines. It will be installed if selected.
Agent for Oracle	This agent backs up Oracle databases. It will be installed on machines running Oracle Database. It will be installed if selected.


Cyber Protection Monitor



This component enables a user to monitor execution of running tasks in the notification area. It will be installed on Windows machines. It will be installed if selected.

Supported on Windows 7 Service Pack 1 and later, and Windows Server 2008 R2 Service Pack 1 and later.


Command-line tool	Supports the command-line interface with the acrocmd utility. acrocmd does not contain any tools that physically execute the commands. It only provides the command-line interface to Cyber Protect components - agents and the management server.
Bootable Media Builder	Creates bootable media.
Supported on Windows and Linux.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.