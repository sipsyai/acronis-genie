# Adding workloads to the Cyber Protect console

Managing workloads in the Cyber Protect console > Workloads > Adding workloads to the Cyber Protect console
Adding workloads to the Cyber Protect console

To start protecting your workloads, add them to the Cyber Protect console first.

The workload types that you can add depend on the service quotas for your account. If a specific workload type is not available, it is grayed out in the Add devices pane.

A partner administrator can enable the required service quotas in Management Portal. For details, see Information for partner administrators.

To add a workload

Log in to the Cyber Protect console.

Go to Devices > All devices, and then click Add.

The Add devices pane opens on the right.

Select the release channel.
Click the workload type that you want to add, and then follow the instructions for the specific workload that you selected.

The following table summarizes the workload types and required actions.

Workloads to add	Required action	Procedure to follow
Multiple Windows machines

Perform autodiscovery in your environment.

To perform autodiscovery, you need at least one machine with an installed protection agent in your local network or Active Directory domain. This agent is used as a discovery agent.

Adding multiple devices


Windows workstations

Windows servers



Install Agent for Windows.



Installing protection agents in Windows

or

Installing and uninstalling protection agents in Windows




macOS workstations

Install Agent for macOS.

Installing protection agents in macOS

or

Installing and uninstalling protection agents in macOS


Linux servers	Install Agent for Linux.

Installing protection agents in Linux

or

Installing and uninstalling protection agents in Linux




Mobile devices

(iOS, Android)

Install the mobile app.	Protecting mobile devices
Cloud-to-cloud workloads
Microsoft 365 Business

Add your Microsoft 365 organization to the Cyber Protect console and use the cloud agent to protect Exchange online mailboxes, OneDrive files, Microsoft Teams, and SharePoint sites.

Alternatively, you can install the local Agent for Office 365. It only provides backup of Exchange Online mailboxes.

For more information on the differences between the local and the cloud agent, see Protecting Microsoft 365 data.

Protecting Microsoft 365 data
Google Workspace	Add your Google Workspace organization to the Cyber Protect console and use the cloud agent to protect Gmail mailboxes and Google Drive files.	Protecting Google Workspace data
Virtual machines
VMware ESXi (Broadcom)

Deploy Agent for VMware (Virtual Appliance) in your environment.



Deploying Agent for VMware (Virtual Appliance)


Install Agent for VMware (Windows).	Installing protection agents in Windows

or

Installing and uninstalling protection agents in Windows


Virtuozzo Hybrid infrastructure	Deploy Agent for Virtuozzo Hybrid Infrastructure

(Virtual appliance) in your environment.

Deploying Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance)
Microsoft Hyper-V	Install Agent for Hyper-V.

Installing protection agents in Windows

or

Installing and uninstalling protection agents in Windows


Virtuozzo Hybrid Server	Install Agent for Virtuozzo.

Installing protection agents in Linux

or

Installing and uninstalling protection agents in Linux


KVM	Install Agent for Windows.

Installing protection agents in Windows

or

Installing and uninstalling protection agents in Windows


Install Agent for Linux.	Installing protection agents in Linux

or

Installing and uninstalling protection agents in Linux


Red Hat Virtualization (oVirt)	Deploy Agent for oVirt (Virtual Appliance) in your environment.	Deploying Agent for oVirt (Virtual Appliance)
Citrix Hypervisor/XenServer	Install Agent for Windows.

Installing protection agents in Windows

or

Installing and uninstalling protection agents in Windows


Install Agent for Linux.

Installing protection agents in Linux

or

Installing and uninstalling protection agents in Linux


Nutanix AHV	Deploy Agent for Nutanix AHV.

Deploying Agent for Nutanix AHV


Oracle VM	Install Agent for Windows.

Installing protection agents in Windows

or

Installing and uninstalling protection agents in Windows


Install Agent for Linux.	Installing protection agents in Linux

or

Installing and uninstalling protection agents in Linux


Oracle LVM (oVirt)	Deploy Agent for oVirt (Virtual Appliance) in your environment.	Deploying Agent for oVirt (Virtual Appliance)
Scale Computing HyperCore	Deploy Agent for Scale Computing HC3 (Virtual Appliance) in your environment.	Deploying Agent for Scale Computing HC3 (Virtual Appliance)
Proxmox VE	Install Agent for Proxmox (bundled with Agent for Linux, 64-bit)	Installing protection agents in Linux

or

Installing and uninstalling protection agents in Linux


Network-attached storage
Synology	Deploy Agent for Synology (Virtual Appliance) in your environment.	Deploying Agent for Synology
Applications
Microsoft SQL Server	Install Agent for SQL.

Installing protection agents in Windows

or

Installing and uninstalling protection agents in Windows


Microsoft Exchange Server	Install Agent for Exchange.
Microsoft Active Directory	Install Agent for Active Directory.
Oracle Database	Install Agent for Oracle.	Protecting Oracle Database

For more information about the available protection agents and where to install them, see Which agent do I need?

Information for partner administrators

A workload type might be missing in the Add devices pane if a required service quota is not enabled in Management Portal. For more information about which service quotas are required for which workloads, see Enabling or disabling offering items in the Partner administrator guide.

As a partner administrator, you cannot add workloads on the All customers level. To add a workload, select an individual customer tenant.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.