---
title: "Recovery overview and cross-platform recovery"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovery"
page_range: "618-627"
tags: ["recovery", "cross-platform", "P2V", "V2P", "V2V", "machine-migration", "recovery-cheat-sheet", "bootable-media", "macOS", "SIP"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#machine-migration.html"
---

# Recovery overview

## Recovery cheat sheet

| What to recover | Recovery method |
|---|---|
| Physical machine (Windows or Linux) | Using the Cyber Protect console; Using bootable media |
| Physical machine (Mac) | Using bootable media |
| Virtual machine (VMware, Hyper-V, Red Hat Virtualization, oVirt, Scale Computing HC3, Proxmox) | Using the Cyber Protect console; Using bootable media |
| Virtual machine (Virtuozzo Hybrid Server, Virtuozzo Hybrid Infrastructure) | Using the Cyber Protect console |
| Container (Virtuozzo Hybrid Server, Proxmox) | Using the Cyber Protect console |
| ESXi configuration | Using bootable media |
| Files/Folders | Using the Cyber Protect console; Downloading files from the cloud storage; Using bootable media; Extracting files from local backups |
| System state | Using the Cyber Protect console |
| SQL databases | Using the Cyber Protect console |
| Exchange databases | Using the Cyber Protect console |
| Exchange mailboxes | Using the Cyber Protect console |
| **Microsoft 365** | |
| Mailboxes (local Agent) | Using the Cyber Protect console |
| Mailboxes (cloud Agent) | Using the Cyber Protect console |
| Public folders | Using the Cyber Protect console |
| OneDrive files | Using the Cyber Protect console |
| SharePoint Online data | Using the Cyber Protect console |
| **Google Workspace** | |
| Mailboxes | Using the Cyber Protect console |
| Google Drive files | Using the Cyber Protect console |
| Shared drive files | Using the Cyber Protect console |

> **Note:** In the Cyber Protect console, you cannot recover backups in tenants in Compliance mode.

## Note for Mac users

- Starting with macOS 10.11 El Capitan, certain system files, folders, and processes are flagged for protection with System Integrity Protection (SIP). The protected files and folders cannot be overwritten during a recovery under the operating system. If you need to overwrite protected files, perform the recovery under bootable media.
- Starting with macOS Sierra 10.12, rarely used files can be moved to iCloud by the Store in Cloud feature. Small footprints of these files are kept on the file system and are backed up instead of the original files. When you recover a footprint to the original location, it is synchronized with iCloud and the original file becomes available. When you recover a footprint to a different location, it cannot be synchronized and the original file will be unavailable.

# Cross-platform recovery

Cross-platform recovery is available for backups of entire machines and backups of disks that contain an operating system. A cross-platform recovery is performed when:

- A backup is created by one type of agent but is recovered by another type of agent.
- An agent-based backup is recovered on the hypervisor level (agentless recovery), or an agentless backup is recovered by an agent (agent-based recovery).
- A backup is recovered to dissimilar hardware (including virtual hardware).

> **Note:** Some peripheral devices, such as printers, might not be recovered correctly when you perform a cross-platform recovery.

> **Note:** If a virtual machine is backed up by a protection agent installed inside the guest operating system, the backup is treated as a physical machine backup.

## Cross-platform recovery support matrix (summary)

Most source workloads can be recovered to most target workload types. The key exceptions are:

- **Containers** (Virtuozzo Hybrid Server containers, Proxmox containers) can only be recovered to the same container type. They cannot be migrated to virtual machines or physical machines.
- **macOS** physical machines cannot be recovered to virtual machines via the Cyber Protect console. You can recover macOS VMs to VMware hosts installed on Mac hardware.
- **Hyper-V** does not support macOS. You cannot recover macOS virtual machines to Hyper-V hosts.
- **EFI-based machines** are recovered as Generation 2 virtual machines on Hyper-V (marked as Yes* in the tables).
- **Secure Boot** setting is not backed up. If Secure Boot is enabled on the original machine, the virtual machine recovered as a new machine will not boot. Disable Secure Boot in the VM console after recovery.

### Source to target support (high-level summary)

| Source | Physical | VMware ESXi | Azure | Hyper-V | VHI | Scale Computing | oVirt | Nutanix | Proxmox VM |
|---|---|---|---|---|---|---|---|---|---|
| Physical machine | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |
| VMware ESXi VM | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |
| Azure VM | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |
| Hyper-V VM | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |
| Virtuozzo HS VM | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |
| VHI VM | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |
| Scale Computing VM | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |
| oVirt VM | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |
| Nutanix VM | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |
| Proxmox VM | Yes | Yes | Yes | Yes* | Yes | Yes | Yes | Yes | Yes |

**Not supported:** Virtuozzo HS container and Proxmox container can only be recovered to their own container type respectively.

## Cross-platform recovery via bootable media

Use bootable media instead of the Cyber Protect console when:
- Performing a migration that is not natively supported (e.g., recovering a physical machine or non-Virtuozzo VM as a Virtuozzo Hybrid Server VM).
- Performing migration of a Linux machine that contains logical volumes (LVM). Use Agent for Linux or bootable media to create the backup, and then use bootable media to recover it.
- Providing drivers for specific hardware that is critical for the system bootability. Build bootable media that includes the required drivers.
