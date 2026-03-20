---
title: "Which agent do I need?"
section: "Installing and deploying Cyber Protection agents"
subsection: "Before you start"
page_range: "39-43"
tags: ["agent", "selection", "physical-machines", "virtual-machines", "databases", "cloud", "mobile"]
acronis_version: "26.02"
---

# Which agent do I need?

Selecting an agent depends on what you are going to back up. The table below summarizes the information, to help you decide.

In Windows, Agent for Exchange, Agent for SQL, Agent for Active Directory, and Agent for Oracle require that Agent for Windows is also installed. Thus, if you install, for example, Agent for SQL, you also will be able to back up the entire machine where the agent is installed.

We recommend that you also install Agent for Windows when you install Agent for VMware (Windows) and Agent for Hyper-V.

In Linux, Agent for Oracle, Agent for MySQL/MariaDB, Agent for Virtuozzo, and Agent for Proxmox require that Agent for Linux (64-bit) is also installed. These agents are bundled into the Agent for Linux (64-bit) installation file.

## Physical machines

| What to back up | Agent to install | Where to install |
|----------------|-----------------|-----------------|
| Physical machines running Windows | Agent for Windows | On the machine that will be backed up. |
| Physical machines running Linux | Agent for Linux | On the machine that will be backed up. |
| Physical machines running macOS | Agent for Mac | On the machine that will be backed up. |

## Databases

| What to back up | Agent to install | Where to install |
|----------------|-----------------|-----------------|
| SQL databases | Agent for SQL | On the machine running Microsoft SQL Server. |
| MySQL databases | Agent for MySQL/MariaDB (Bundled into Agent for Linux 64-bit) | On the machine running MySQL Server. |
| MariaDB databases | Agent for MySQL/MariaDB (Bundled into Agent for Linux 64-bit) | On the machine running MariaDB Server. |
| Exchange databases | Agent for Exchange | On the machine running the Mailbox role of Microsoft Exchange Server.* |
| Oracle databases | Agent for Oracle (In Linux, bundled into Agent for Linux 64-bit) | On the machine running Oracle Database. |

*During the installation, Agent for Exchange checks for enough free space on the machine where it will run. Free space equal to 15 percent of the biggest Exchange database is temporarily needed during a granular recovery.

## Cloud-to-cloud workloads

| What to back up | Agent to install | Where to install |
|----------------|-----------------|-----------------|
| Microsoft 365 mailboxes | Cloud agent (No installation required) or Agent for Office 365 | Cloud agent is deployed in the data center. Agent for Office 365 on a Windows machine connected to the Internet. |
| Microsoft 365 OneDrive files and SharePoint Online sites | Cloud agent (No installation required) | Cloud agent is deployed in the data center. |
| Google Workspace Gmail mailboxes, Google Drive files, and Shared drive files | Cloud agent (No installation required) | Cloud agent is deployed in the data center. |

## Active Directory

| What to back up | Agent to install | Where to install |
|----------------|-----------------|-----------------|
| Machines running Active Directory Domain Services | Agent for Active Directory | On the domain controller. |

## Virtual machines

| What to back up | Agent to install | Where to install |
|----------------|-----------------|-----------------|
| VMware ESXi (Broadcom) VMs | Agent for VMware (Windows) or Agent for VMware (Virtual Appliance) | Windows agent on a machine with network access to vCenter Server. VA on the ESXi host.** |
| Microsoft Hyper-V VMs | Agent for Hyper-V | On the Hyper-V host. |
| Scale Computing HyperCore VMs | Agent for Scale Computing HC3 (Virtual Appliance) | On the Scale Computing HyperCore host. |
| Nutanix virtual machines | Agent for Nutanix AHV (Virtual appliance) | On the Nutanix AHV host. |
| Proxmox virtual machines | Agent for Proxmox (Bundled into Agent for Linux 64-bit) | On the Proxmox VE host. |
| Red Hat Virtualization VMs (managed by oVirt) | Agent for oVirt (Virtual Appliance) | On the Red Hat Virtualization host. |
| Virtuozzo Hybrid Server VMs and containers*** | Agent for Virtuozzo (Bundled into Agent for Linux 64-bit) | On the Virtuozzo Hybrid Server host. |
| Virtuozzo Hybrid Infrastructure VMs | Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance) | On the Virtuozzo Hybrid Infrastructure host. |
| VMs on Amazon EC2, Windows Azure, Citrix Hypervisor/XenServer, Red Hat (RHV/RHEV not managed by oVirt), KVM (not managed by oVirt), Oracle VMs (not managed by oVirt) | The same as for physical machines**** | On the machine that will be backed up. |
| Red Hat/KVM/Oracle VMs (managed by oVirt) | Agent for oVirt (Virtual Appliance) | On the virtualization host. |

## Network-attached storage

| What to back up | Agent to install | Where to install |
|----------------|-----------------|-----------------|
| Synology | Agent for Synology (Virtual Appliance) | On the NAS device. |

## Mobile devices

| What to back up | Agent to install | Where to install |
|----------------|-----------------|-----------------|
| Mobile devices running Android | Mobile app for Android | On the mobile device that will be backed up. |
| Mobile devices running iOS | Mobile app for iOS | On the mobile device that will be backed up. |

### Notes

**If your ESXi uses SAN attached storage, install the agent on a machine connected to the same SAN. The agent will back up the virtual machines directly from the storage (LAN-free backup).

***For Virtuozzo 7, only ploop containers are supported. Virtual machines are not supported.

****A virtual machine is considered virtual if it is backed up by an external agent. If an agent is installed in the guest system, the backup and recovery operations are the same as with a physical machine. Nevertheless, if Cyber Protection can identify a virtual machine by using the CPUID instruction, a virtual machine service quota is assigned to it.
