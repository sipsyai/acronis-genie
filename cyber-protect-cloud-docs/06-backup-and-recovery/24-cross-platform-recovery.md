---
title: "Cross-Platform Recovery"
section: "Managing the backup and recovery of workloads and files"
subsection: "Cross-platform recovery"
page_range: "620-627"
tags: [cross-platform, recovery, migration, physical-to-virtual, virtual-to-physical, compatibility-matrix, bootable-media]
acronis_version: "26.02"
---

# Cross-Platform Recovery

Cross-platform recovery is available for backups of entire machines and backups of disks that contain an operating system. A cross-platform recovery is performed in the following cases:

- A backup is created by one type of agent but it is recovered by another type of agent.
- An agent-based backup is recovered on the hypervisor level (agentless recovery), or an agentless backup is recovered by an agent (agent-based recovery).
- A backup is recovered to dissimilar hardware (including virtual hardware).

> **Note:** Some peripheral devices, such as printers, might not be recovered correctly when you perform a cross-platform recovery.

You can recover a disk-level backup to a physical machine or to a virtual machine. For example, a disk-level backup is an **Entire machine** backup or a **Disk/volumes** backup that contains the system disk and the boot disk.

Cross-platform recovery (machine migration) is performed in the following cases:

- When you recover a backup of a physical machine to a virtual machine.
- When you recover a backup of a virtual machine to a physical machine.
- When you recover a backup of a virtual machine to a virtual machine on a different type of hypervisor.

> **Note:** If a virtual machine is backed up by a protection agent installed inside the guest operating system, the backup is treated as a physical machine backup.

## Note for Mac Users

- Starting with 10.11 El Capitan, certain system files, folders, and processes are flagged for protection with an extended file attribute `com.apple.rootless` (System Integrity Protection / SIP). The protected files include preinstalled applications and most of the folders in `/system`, `/bin`, `/sbin`, `/usr`. These protected files and folders cannot be overwritten during a recovery under the operating system. If you need to overwrite the protected files, perform the recovery under bootable media.
- Starting with macOS Sierra 10.12, rarely used files can be moved to iCloud by the Store in Cloud feature. Small footprints of these files are kept on the file system. These footprints are backed up instead of the original files. When you recover a footprint to the original location, it is synchronized with iCloud and the original file becomes available. When you recover a footprint to a different location, it cannot be synchronized and the original file will be unavailable.

## Cross-Platform Recovery Compatibility Matrix

The following tables summarize supported cross-platform recovery paths for each source workload type.

### Physical Machine (Source)

| Target workload | Supported |
|---|---|
| Physical machine | Yes |
| Broadcom (VMware) ESXi virtual machine | Yes |
| Microsoft Azure virtual machine | Yes |
| Microsoft Hyper-V virtual machine | Yes* |
| Virtuozzo Hybrid Server virtual machine | Yes |
| Virtuozzo Hybrid Server container | No |
| Virtuozzo Hybrid Infrastructure virtual machine | Yes |
| Scale Computing HyperCore virtual machine | Yes |
| RHV/oVirt virtual machine | Yes |
| Nutanix virtual machine | Yes |
| Proxmox virtual machine | Yes |
| Proxmox container | No |

### Broadcom (VMware) ESXi Virtual Machine (Source)

| Target workload | Supported |
|---|---|
| Physical machine | Yes |
| Broadcom (VMware) ESXi virtual machine | Yes |
| Microsoft Azure virtual machine | Yes |
| Microsoft Hyper-V virtual machine | Yes* |
| Virtuozzo Hybrid Server virtual machine | Yes |
| Virtuozzo Hybrid Server container | No |
| Virtuozzo Hybrid Infrastructure virtual machine | Yes |
| Scale Computing HyperCore virtual machine | Yes |
| RHV/oVirt virtual machine | Yes |
| Nutanix virtual machine | Yes |
| Proxmox virtual machine | Yes |
| Proxmox container | No |

### Microsoft Azure Virtual Machine (Source)

| Target workload | Supported |
|---|---|
| Physical machine | Yes |
| Broadcom (VMware) ESXi virtual machine | Yes |
| Microsoft Azure virtual machine | Yes |
| Microsoft Hyper-V virtual machine | Yes* |
| Virtuozzo Hybrid Server virtual machine | Yes |
| Virtuozzo Hybrid Server container | No |
| Virtuozzo Hybrid Infrastructure virtual machine | Yes |
| Scale Computing HyperCore virtual machine | Yes |
| RHV/oVirt virtual machine | Yes |
| Nutanix virtual machine | Yes |
| Proxmox virtual machine | Yes |
| Proxmox container | No |

### Virtuozzo Hybrid Server Container (Source)

| Target workload | Supported |
|---|---|
| Physical machine | No |
| Broadcom (VMware) ESXi virtual machine | No |
| Microsoft Azure virtual machine | No |
| Microsoft Hyper-V virtual machine | No |
| Virtuozzo Hybrid Server virtual machine | No |
| Virtuozzo Hybrid Server container | Yes |
| Virtuozzo Hybrid Infrastructure virtual machine | No |
| Scale Computing HyperCore virtual machine | No |
| RHV/oVirt virtual machine | No |
| Nutanix virtual machine | No |
| Proxmox virtual machine | No |
| Proxmox container | No |

### Proxmox Container (Source)

| Target workload | Supported |
|---|---|
| Physical machine | No |
| Broadcom (VMware) ESXi virtual machine | No |
| Microsoft Azure virtual machine | No |
| Microsoft Hyper-V virtual machine | No |
| Virtuozzo Hybrid Server virtual machine | No |
| Virtuozzo Hybrid Server container | No |
| Virtuozzo Hybrid Infrastructure virtual machine | No |
| Scale Computing HyperCore virtual machine | No |
| RHV/oVirt virtual machine | No |
| Nutanix virtual machine | No |
| Proxmox virtual machine | No |
| Proxmox container | Yes |

> **Note:** The Secure Boot setting is not backed up. If Secure Boot is enabled on the original machine, the virtual machine recovered as a new machine will not boot. To start the recovered machine, disable Secure Boot in the VM console after recovery.

> **Note:** * EFI-based machines are recovered as Generation 2 virtual machines. You cannot recover macOS virtual machines to Hyper-V hosts because Hyper-V does not support macOS. You can recover macOS virtual machines to VMware hosts that are installed on Mac hardware.

## Cross-Platform Recovery via Bootable Media

You can perform a cross-platform recovery by using bootable media. We recommend that you use bootable media instead of the Cyber Protect console in the following cases:

- Performing a migration that is not natively supported (for example, use bootable media to recover a physical machine or a non-Virtuozzo Hybrid Server virtual machine as a Virtuozzo Hybrid Server virtual machine on a Virtuozzo host).
- Performing migration of a Linux machine that contains logical volumes (LVM). Use Agent for Linux or bootable media to create the backup, and then use bootable media to recover the backup.
- Providing drivers for specific hardware that is critical for the system bootability. Build bootable media that can use the required drivers.
