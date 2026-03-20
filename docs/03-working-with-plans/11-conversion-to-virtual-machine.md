---
title: "Conversion to a virtual machine"
section: "Working with plans"
subsection: "Conversion to virtual machine"
page_range: "252-259"
tags: [conversion, virtual machine, VMware, Hyper-V, Proxmox, Scale Computing, Virtuozzo, off-host data processing]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#conversion-to-virtual-machine.html"
---

# Conversion to a virtual machine

> **Note:** In service-based billing mode, this feature requires the **Servers** quota to be enabled under Standard Protection as a prerequisite, but using the feature does not affect the quota usage. With solution-based billing mode, this functionality is available in customer tenants that use **Ultimate protection**.

With a conversion to VM plan, you can create a virtual machine from a disk-level backup that includes an operating system. This enables you to quickly start a pre-created standby machine or perform cross-platform recovery. For example, you can recover a backup of a physical or virtual machine to a different hypervisor.

You can schedule the plan and incrementally apply backed-up changes to the resulting virtual machine. You can convert a backup to a virtual machine by using a protection agent that has access to the backup archive.

## Conversion or Running a virtual machine from a backup (Instant Restore)

Both operations provide a virtual machine that you can start if the original workload fails.

Conversion to a virtual machine uses CPU and memory resources during the conversion process, and the resulting virtual machine uses storage space on the datastore. However, the performance of the resulting virtual machine is better, compared to the machine that was created by the **Run as VM** operation (Instant Restore).

Running a virtual machine from a backup (Instant Restore) uses resources only while the virtual machine is running. In this case, datastore space is required only for storing changes to the virtual disks. The host does not access the virtual disks directly. Instead, it communicates with the agent, which reads data from the backup. As a result, performance is lower than that of a machine created via a conversion to VM plan. Also, with Instant Restore, the resulting virtual machine is temporary.

## Limitations

- Conversion to a virtual machine is available only for disk-level backups. If a backup includes the system volume and contains all of the information necessary for the operating system to start, the resulting virtual machine can start on its own. Otherwise, you can add its virtual disks to another virtual machine.
- Backups that are stored on NFS cannot be converted.
- Backups that are stored in Secure Zone can be converted only by the agent that is running on the same machine.
- If the backup contains Linux logical volumes (LVM), you must create it by using Agent for VMware, Agent for Hyper-V, Agent for Scale Computing HC3, or Agent for Proxmox. Converted machines must match the platform of the original machine (VMware ESXi, Hyper-V, Scale Computing HC3, or Proxmox VE). Cross-hypervisor conversion is not supported.
- When backups of a Windows machine are converted to VMware Workstation or VHDX files, the resulting virtual machine inherits the CPU type from the machine that performs the conversion. If it is started on a host with a different CPU type, the guest system displays a driver error. Update this driver manually.
- With Proxmox, conversion to a virtual machine is also supported on storages that do not provide snapshot capabilities. In such cases, incremental updates of the resulting virtual machine are not possible.

## Types of conversion to virtual machine

When you convert a backup to a virtual machine, you can choose one of the following conversion types:

### Save the resulting virtual machine as a set of files

With this option, the conversion process creates one or more virtual disk files without requiring access to a hypervisor. You can save the files to a local or network folder and later manually use them on a hypervisor.

The resulting files depend on the selected type:
- **VMware Workstation** creates VMDK files
- **VHDX files** creates VHDX and VMX files

| Conversion to a virtual machine (as a set of files) | Agent for VMware | Agent for Hyper-V | Agent for Windows | Agent for Linux |
|---|---|---|---|---|
| VMware Workstation | + | + | + | + |
| VHDX files | + | + | + | + |

With this conversion type, each conversion recreates the virtual machine from scratch. Cyber Protect temporarily renames the existing machine, creates a new virtual machine with the original name. If conversion is successful, the old machine is deleted. If conversion fails, the old machine is restored. Additional temporary storage is required.

> **Note:** Incremental updates are not available for virtual machines that are created by **VMware Workstation** and **VHDX files** options.

### Create the resulting virtual machine directly on a virtualization server

With this option, the conversion process creates a virtual machine directly on the selected virtualization server. Unlike conversion as a set of files, this method supports incremental updates.

During the first conversion, Cyber Protect creates a new virtual machine. For subsequent conversions:
- If no full backup has occurred since the last conversion, an incremental update is performed, and only changed data are transferred to the virtual machine. Incremental updates are faster and reduce network and CPU usage on the host.
- If a full backup has occurred, or if an incremental update is not possible (for example, due to missing intermediate snapshots), the virtual machine is created from scratch.

| Conversion to a virtual machine | Agent for VMware | Agent for Hyper-V | Agent for Scale Computing HC3 | Agent for Virtuozzo Hybrid Infrastructure | Agent for Proxmox |
|---|---|---|---|---|---|
| VMware ESXi | + | -- | -- | -- | -- |
| Microsoft Hyper-V | -- | + | -- | -- | -- |
| Scale Computing HC3 | -- | -- | + | -- | -- |
| Virtuozzo Hybrid Infrastructure | -- | -- | -- | + | -- |
| Proxmox | -- | -- | -- | -- | + |

### Intermediate snapshots

To enable incremental updates of the resulting virtual machine, Cyber Protect stores an intermediate snapshot named **Replica**. This snapshot captures the state of the virtual machine after the most recent successful conversion. You can revert the virtual machine to this snapshot if you want to discard any subsequent changes and return to the last converted state.

For conversions to Scale Computing HC3 virtual machines, an additional snapshot named **Utility Snapshot** is created. This snapshot is used only by Cyber Protect and must remain intact to ensure proper operation.

## Creating a conversion plan

To convert a disk-level backup to a virtual machine, you must create a conversion plan. You can use this plan to migrate a virtual machine to a non-original hypervisor. For example, you can convert a backup of a VMware virtual machine to a Proxmox virtual machine. Also, with a conversion plan, you can update the resulting virtual machine after each incremental or differential backup.

The general steps for creating a conversion plan are similar across all hypervisors:

1. In the Cyber Protect console, go to **Management** > **Conversion to VM**.
2. Click **Create plan**.
3. [Optional] To rename the plan, click the pencil icon, enter a new name, and then click **OK**.
4. In **Convert to**, select the target hypervisor type (VMware ESXi, Microsoft Hyper-V, Scale Computing HC3, Virtuozzo Hybrid Infrastructure, Proxmox VE, VMware Workstation, or VHDX files).
5. In **Host**, select the target host, specify the virtual machine name, and then click **OK**.
6. In **Agent**, select the agent that will perform the conversion.
7. In **Items to convert**, select one or more backups to convert, and then click **Done**. To switch between individual backups and backup locations, click **Locations / Backups**. If the selected backups are encrypted, all of them must use the same encryption password.
8. [If prompted] Specify the credentials to access the backup location, and then click **OK**.
9. In **Datastore** (ESXi/Proxmox) or **Path** (Hyper-V/file-based), select the storage for the virtual machine.
10. In **Provisioning mode**, select the disk provisioning mode.
11. [Optional] In **VM settings**, change the memory size, the number of processors, or the network connections of the virtual machine, and then click **OK**.
12. [Optional] In **Schedule**, change the plan schedule, and then click **OK**.
13. [If the selected backups are encrypted] Turn on the **Backup password** switch, provide the encryption password, and then click **OK**.
14. [Optional] To change error handling, performance, pre-post commands or task failure handling, click the gear icon, update the settings, and then click **Done**.
15. Click **Create**.

> **Note:** For VMware Workstation conversions, each conversion overwrites the VMDK files in the target location. For VHDX files conversions, each conversion overwrites the VHDX and VMX files in the target location.

> **Note:** For Proxmox VE, conversion to a virtual machine is also supported on storages that do not provide snapshot capabilities. In such cases, incremental updates of the resulting virtual machine are not possible. For more details about the storage types that are supported by Proxmox, see [https://pve.proxmox.com/pve-docs/chapter-pvesm.html](https://pve.proxmox.com/pve-docs/chapter-pvesm.html).
