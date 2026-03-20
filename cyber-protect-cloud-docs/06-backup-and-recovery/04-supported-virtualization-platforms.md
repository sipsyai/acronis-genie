---
title: "Supported virtualization platforms"
section: "Managing the backup and recovery of workloads and files"
subsection: "Supported operating systems and environments for backup and recovery"
page_range: "495-503"
tags: ["virtualization", "VMware", "Hyper-V", "Scale-Computing", "Proxmox", "Citrix", "KVM", "oVirt", "public-clouds", "Azure", "Amazon-EC2", "agentless", "agent-based"]
acronis_version: "26.02"
---

# Supported virtualization platforms

The following tables summarize how various virtualization platforms are supported. For more information about the differences between the agent-based and agentless backup, see [Agent-based and agentless backup](../02-installing-deploying-agents/02-agent-based-vs-agentless.md).

> **Note:** If you use a virtualization platform or version that is not listed below, the **Agent-based backup (Backup from inside a guest OS)** method should still work correctly in all required scenarios.

## VMware (Broadcom)

| Platform | Agentless backup | Agent-based backup |
|----------|-----------------|-------------------|
| **VMware vSphere versions:** 4.1, 5.0, 5.1, 5.5, 6.0, 6.5, 6.7, 7.0, 8.0. **Editions:** vSphere Essentials*, Essentials Plus*, Standard*, Advanced, Enterprise, Enterprise Plus | Supported | Supported |
| VMware vSphere Hypervisor (Free ESXi)** | Not supported | Supported |
| VMware Server, VMware Workstation, VMware ACE, VMware Player | Not supported | Supported |

\* In these editions, the HotAdd transport for virtual disks is supported on vSphere 5.0 and later. On version 4.1, backups may run slower.

\*\* Backup at a hypervisor level is not supported for vSphere Hypervisor because this product restricts access to Remote Command Line Interface (RCLI) to read-only mode.

> **Note:** Cyber Protect Cloud officially supports any update within the supported major vSphere version. For example, vSphere 8.0 support includes support for any update within this version (e.g., vSphere 8.0 Update 1). Support for a specific VMware vSphere version means that vSAN of the corresponding version is also supported.

### VMware limitations

- **Fault tolerant machines** — Agent for VMware backs up a fault tolerant machine only if fault tolerance was enabled in VMware vSphere 6.0 and later. If you upgraded from an earlier vSphere version, it is enough to disable and enable fault tolerance for each machine. If you are using an earlier vSphere version, install an agent in the guest operating system.
- **Independent disks and RDM** — Agent for VMware does not back up Raw Device Mapping (RDM) disks in physical compatibility mode or independent disks. The agent skips these disks and adds warnings to the log.
- **In-guest iSCSI connection** — Agent for VMware does not back up LUN volumes connected by an iSCSI initiator that works within the guest operating system. The volumes are omitted from a backup without a warning.
- **Encrypted virtual machines** (introduced in VMware vSphere 6.5):
  - Encrypted VMs are backed up in an unencrypted state. If encryption is critical, enable encryption of backups when creating a protection plan.
  - Recovered VMs are always unencrypted. You can manually enable encryption after the recovery is complete.
  - If you back up encrypted VMs, we recommend that you also encrypt the VM where Agent for VMware is running.
  - Encrypted VMs will be backed up via LAN, even if SAN transport is configured. VMware does not support SAN transport for backing up encrypted virtual disks.
- **Secure Boot** — VMware VMs: Secure Boot is disabled after a VM is recovered as a new virtual machine. You can manually enable it after recovery.
- **ESXi configuration backup** is not supported for VMware vSphere 7.0 or later.
- **Virtual machines with empty Instance UUID** do not appear in the Cyber Protect console.
- **Network settings on the protection agent** — A backup can fail if the protection agent cannot resolve the name of the ESXi host registered in vCenter to an IP address. Resolve by configuring DNS or modifying the `/etc/hosts` file.

## Microsoft (Hyper-V)

| Platform | Agentless backup | Agent-based backup |
|----------|-----------------|-------------------|
| Windows Server 2008 (x64) with Hyper-V through Windows Server 2025 with Hyper-V, Microsoft Hyper-V Server 2008 through 2019 | Supported | Supported |
| Microsoft Virtual PC 2004, 2007, Windows Virtual PC | Not supported | Supported |
| Microsoft Virtual Server 2005 | Not supported | Supported |

> **Note:** Hyper-V VMs running on a hyper-converged cluster with Storage Spaces Direct (S2D) are supported. Storage Spaces Direct is also supported as a backup storage.

### Hyper-V limitations

- **Pass-through disks** — Agent for Hyper-V does not back up pass-through disks. The agent skips these disks and adds warnings to the log.
- **Hyper-V guest clustering** — Agent for Hyper-V does not support backup of Hyper-V VMs that are nodes of a Windows Server Failover Cluster. A VSS snapshot at the host level can even temporarily disconnect the external quorum disk.
- **In-guest iSCSI connection** — Agent for Hyper-V does not back up LUN volumes connected by an iSCSI initiator within the guest OS. The volumes are omitted from a backup without a warning.
- **Dependency on the Microsoft WMI subsystem** — Agentless backups of Hyper-V VMs depend on the Microsoft WMI subsystem, specifically the `Msvm_VirtualSystemManagementService` class. If WMI queries fail, the backups will also fail.
- **Virtual machines with PMEM disks** — Backup of Hyper-V VMs with persistent memory (PMEM) disks is not supported.
- **Cross-platform recovery** — If Agent for Hyper-V recovers a backup created by another agent as a new Hyper-V VM, the resulting machine is Generation 1.
- **Secure Boot** — For all Generation 2 Hyper-V VMs that are recovered, Secure Boot is disabled. You can re-enable it manually.
- **Crash-consistent backups of Linux VMs** — Backups of Linux VMs running on a Hyper-V 2019 host fail over to crash-consistent snapshots, due to a Microsoft limitation. To avoid warnings, disable the VSS for Virtual Machines backup option.

## Scale Computing

| Platform | Agentless backup | Agent-based backup |
|----------|-----------------|-------------------|
| Scale Computing HyperCore 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4 | Supported | Supported |

**Limitations:** VMs replicated by the native Scale Computing VM replication feature cannot be backed up.

## Proxmox VE

| Platform | Agentless backup | Agent-based backup |
|----------|-----------------|-------------------|
| Proxmox VE 7.x, 8, and 8.1 | Not supported | Supported (only HVM guests; PV guests not supported) |
| Proxmox VE 8.2, 8.3, 8.4, 9.0 | Supported | Supported (only HVM guests; PV guests not supported) |

## Citrix Hypervisor/XenServer

| Platform | Agentless backup | Agent-based backup |
|----------|-----------------|-------------------|
| Citrix Hypervisor/XenServer 4.1.5, 5.5, 5.6, 6.0, 6.1, 6.2, 6.5, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 8.0, 8.1, 8.2 | Not supported | Supported (only HVM guests; PV guests not supported) |

## Red Hat and Linux

| Platform | Agentless backup | Agent-based backup |
|----------|-----------------|-------------------|
| Red Hat Enterprise Virtualization (RHEV) 2.2, 3.0–3.6 | Not supported | Supported |
| Red Hat Virtualization (RHV) 4.0, 4.1 | Not supported | Supported |
| Red Hat Virtualization (managed by oVirt) 4.2, 4.3, 4.4, 4.5 | Supported | Supported |
| Kernel-based Virtual Machines (KVM) | Not supported | Supported |
| KVM managed by oVirt 4.3 (on RHEL/CentOS 7.6, 7.7) | Supported | Supported |
| KVM managed by oVirt 4.4 (on RHEL/CentOS Stream 8.x) | Supported | Supported |
| KVM managed by oVirt 4.5 (on RHEL/CentOS Stream 8.x) | Supported | Supported |

## Public clouds

| Platform | Agentless backup | Agent-based backup |
|----------|-----------------|-------------------|
| Amazon EC2 instances | Not supported | Supported |
| Microsoft Azure virtual machines | Supported | Supported |
