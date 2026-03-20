---
title: "Workloads - Types, adding, and removing"
section: "Managing workloads in the Cyber Protect console"
subsection: "Workloads"
page_range: "379-388"
tags: ["workloads", "adding", "removing", "physical-machines", "virtual-machines", "cloud-workloads", "mobile", "applications"]
acronis_version: "26.02"
---

# Workloads

A workload is any type of protected resource — for example, a physical machine, a virtual machine, a mailbox, or a database instance. In the Cyber Protect console, the workload is shown as an object to which you can apply a plan (protection plan, backup plan, or scripting plan).

Some workloads require installing a protection agent or deploying a virtual appliance. You can install agents by using the graphical user interface or by using the command-line interface (unattended installation).

A virtual appliance (VA) is a ready-made virtual machine that contains a protection agent. With a virtual appliance, you can back up other virtual machines in the same environment without installing a protection agent on them (agentless backup).

> **Important:** Agents must be online at least once every 30 days. Otherwise, their plans will be revoked and the workloads will become unprotected.

## Workload types and their agents

| Workload type | Agent | Examples |
|--------------|-------|----------|
| **Physical machines** | A protection agent is installed on every protected machine. | Workstation, Laptop, Server |
| **Virtual machines** | Agent-based backup: agent installed on every protected machine. Agentless backup: agent installed only on the hypervisor host or as a virtual appliance. | VMware VM, Hyper-V VM, KVM managed by oVirt, Scale Computing HC3 |
| **Microsoft 365 Business / Google Workspace workloads** | Backed up by a cloud agent for which no installation is required. A local Agent for Office 365 is also available (Exchange Online mailboxes only). | Microsoft 365 mailbox, OneDrive, Microsoft Teams, SharePoint site, Google mailbox, Google Drive |
| **Applications** | Backed up by dedicated agents such as Agent for SQL, Agent for Exchange, Agent for MySQL/MariaDB, or Agent for Active Directory. | SQL Server databases, MySQL/MariaDB databases, Oracle databases, Active Directory |
| **Mobile devices** | A mobile app is installed on the protected devices. | Android or iOS devices |
| **Websites** | Backed up by a cloud agent for which no installation is required. | Websites accessed via the SFTP or SSH protocols |

## Adding workloads to the Cyber Protect console

To start protecting your workloads, add them to the Cyber Protect console first.

> **Note:** The workload types that you can add depend on the service quotas for your account. If a specific workload type is not available, it is grayed out in the **Add devices** pane. A partner administrator can enable the required service quotas in Management Portal.

### To add a workload

1. Log in to the Cyber Protect console.
2. Go to **Devices** > **All devices**, and then click **Add**. The **Add devices** pane opens on the right.
3. Select the release channel.
4. Click the workload type that you want to add, and then follow the instructions for the specific workload that you selected.

### Adding workloads — summary by type

| Workloads to add | Required action | Procedure |
|-----------------|----------------|-----------|
| **Multiple Windows machines** | Perform autodiscovery in your environment. Requires at least one machine with a protection agent in your local network or AD domain. | "Adding multiple devices" (p. 178) |
| **Windows workstations/servers** | Install Agent for Windows. | "Installing protection agents in Windows" (p. 61) |
| **macOS workstations** | Install Agent for Mac. | "Installing protection agents in macOS" (p. 68) |
| **Linux servers** | Install Agent for Linux. | "Installing protection agents in Linux" (p. 66) |
| **Mobile devices (iOS, Android)** | Install the mobile app. | "Protecting mobile devices" (p. 777) |
| **Microsoft 365 Business** | Add your Microsoft 365 organization to the Cyber Protect console and use the cloud agent. | "Protecting Microsoft 365 data" (p. 780) |
| **Google Workspace** | Add your Google Workspace organization to the Cyber Protect console and use the cloud agent. | "Protecting Google Workspace data" (p. 843) |
| **VMware ESXi (Broadcom)** | Deploy Agent for VMware (VA) or install Agent for VMware (Windows). | "Deploying Agent for VMware" (p. 131) |
| **Virtuozzo Hybrid Infrastructure** | Deploy Agent for Virtuozzo Hybrid Infrastructure (VA). | "Deploying Virtuozzo HI VA" (p. 140) |
| **Microsoft Hyper-V** | Install Agent for Hyper-V. | "Installing protection agents in Windows" (p. 61) |
| **Virtuozzo Hybrid Server** | Install Agent for Virtuozzo. | "Installing protection agents in Linux" (p. 66) |
| **KVM** | Install Agent for Windows or Agent for Linux. | Same as physical machines |
| **Red Hat Virtualization (oVirt)** | Deploy Agent for oVirt (VA). | "Deploying Agent for oVirt" (p. 151) |
| **Nutanix AHV** | Deploy Agent for Nutanix AHV. | "Deploying Agent for Nutanix AHV" (p. 162) |
| **Citrix Hypervisor/XenServer** | Install Agent for Windows or Agent for Linux. | Same as physical machines |
| **Oracle LVM (oVirt)** | Deploy Agent for oVirt (VA). | "Deploying Agent for oVirt" (p. 151) |
| **Scale Computing HyperCore** | Deploy Agent for Scale Computing HC3 (VA). | "Deploying SC HC3 VA" (p. 135) |
| **Proxmox VE** | Install Agent for Proxmox (bundled with Agent for Linux). | "Installing protection agents in Linux" (p. 66) |
| **Synology** | Deploy Agent for Synology (VA). | "Deploying Agent for Synology" (p. 167) |
| **Microsoft SQL Server** | Install Agent for SQL. | "Installing protection agents in Windows" (p. 61) |
| **Microsoft Exchange Server** | Install Agent for Exchange. | Same |
| **Microsoft Active Directory** | Install Agent for Active Directory. | Same |
| **Oracle Database** | Install Agent for Oracle. | "Protecting Oracle Database" (p. 867) |

### Information for partner administrators

- A workload type might be missing in the **Add devices** pane if a required service quota is not enabled in Management Portal.
- As a partner administrator, you cannot add workloads on the **All customers** level. To add a workload, select an individual customer tenant.

## Removing workloads from the Cyber Protect console

You can remove from the Cyber Protect console the workloads that you do not need to protect anymore. The procedure depends on the workload type.

Alternatively, you can uninstall the agent on the protected workload. When you uninstall an agent, the protected workload is automatically removed from the Cyber Protect console.

> **Important:** When you remove a workload from the Cyber Protect console, all plans that are applied to that workload are revoked. Removing a workload does not delete any plans or backups, and does not uninstall the protection agent.

### Removing procedures by workload type

- **Workload with a protection agent:** Navigate to **Devices** > **All devices**, select the check box, click **Delete** in the Actions pane, and confirm. Optionally uninstall the agent.
- **Workload without a protection agent:** In the Cyber Protect console, go to **Devices** > **All devices**, enable the **Agent** column via the gear icon, find the machine where the agent is installed, select that machine, click **Delete**, and confirm.
- **Cloud-to-cloud workload:** Navigate to **Devices** > **Microsoft 365** or **Google Workspace**, click the organization name, click **Delete group**, and confirm.
- **Mobile device:** Navigate to **Devices** > **All devices**, select the workload, click **Delete**, and confirm. Optionally uninstall the app from the mobile device.
- **Website:** Navigate to **Devices** > **All devices**, select the workload, click **Delete**, and confirm.
