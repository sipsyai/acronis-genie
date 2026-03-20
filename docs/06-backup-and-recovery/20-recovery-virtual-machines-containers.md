---
title: "Recovering virtual machines and containers"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovery"
page_range: "640-652"
tags: ["VM-recovery", "V2V", "V2P", "VMware", "Hyper-V", "Azure", "Virtuozzo", "Scale-Computing", "oVirt", "Nutanix", "Proxmox", "container-recovery", "agentless-recovery"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#protecting-proxmox-virtual-machines-containers.html"
---

# Recovery of virtual machines

You can recover a disk-level backup of a virtual machine to a physical machine or another virtual machine. A disk-level backup is an **Entire machine** backup or a **Disk/volumes** backup that contains the system disk and boot disk.

## Limitations

- Cannot recover backups of machines registered in customer tenants in Compliance mode.
- During a recovery to a virtual machine, Cyber Protect stops the target VM without a prompt. After recovery, you must restart the machine manually (changeable in **Recovery options** > **VM power management**).
- You can recover a backup of a VM to a physical machine only if the disk configuration exactly matches. Alternatively, use bootable media for V2P migration.
- You cannot recover macOS virtual machines to Hyper-V hosts (Hyper-V does not support macOS). You can recover macOS virtual machines to VMware hosts installed on Mac hardware.

## Recovering a virtual machine as a physical machine

1. In the Cyber Protect console, select the backed-up machine on the **Devices** tab or **Backup storage** tab, and select a recovery point.
2. Click **Recover** > **Entire machine**.
3. In **Recover to**, select **Physical machine**. A target machine is automatically selected.
4. [Optional] Change the target machine: Click **Target machine** > select an online machine > **OK**.
5. [Optional] Configure disk mapping (disk level or volume level via **Switch to volume mapping**).
6. [Optional] [Windows only] Enable **Safe recovery**.
7. Click **Start recovery**.
8. Confirm overwrite of target machine disks.

## Recovering a virtual machine as a virtual machine

You can recover a backup of a virtual machine to the original hypervisor or to a different type of hypervisor (cross-platform recovery/machine migration).

Recovering to a virtual machine on which a protection agent is not installed is done on the hypervisor level (agentless recovery). Recovery to a VM on which a protection agent is installed is agent-based recovery -- the same as recovery to a physical machine.

### Prerequisites

An agent for the relevant hypervisor must be installed in your environment.

### VMware ESXi

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine**. The original VM is selected as target.
3. [Optional] Change the target: Click **Target machine** > **VMware ESXi** > **New machine** or **Existing machine**.
4. [Optional] Configure: **Datastore**, **Disk mapping**, **VM settings** (memory, processors, network).
5. Click **Start recovery**.

### Microsoft Azure

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine**. The original VM is selected.
3. [Optional] Change target: **Target machine** > **Microsoft Azure** > **New machine** (select subscription, region, resource group) or **Original machine**.
4. [Optional] Configure: **Disk mapping** (storage type: LRS or ZRS), **VM settings** (availability type, zone, memory, network connections, subnets, security groups).
5. Click **Start recovery**.

### Microsoft Hyper-V

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine**. The original VM is selected.
3. [Optional] Change target: **Target machine** > **Microsoft Hyper-V** > **New machine** or **Existing machine**.
4. [Optional] Configure: **Path** (storage), **Disk mapping** (storage, interface, provisioning mode per virtual disk), **VM settings**.
5. Click **Start recovery**.

### Virtuozzo

> **Note:** Only a Virtuozzo virtual machine can be recovered to a Virtuozzo virtual machine.

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine**.
3. [Optional] Change target: **Target machine** > **Virtuozzo** > **New machine** or **Existing machine**.
4. [Optional] Configure: **Path**, **Disk mapping** (storage, interface, provisioning), **VM settings**.
5. Click **Start recovery**.

### Virtuozzo Hybrid Infrastructure

Same general procedure. Select **Virtuozzo Hybrid Infrastructure** as hypervisor. Configure **Disk mapping** (storage policy) and **VM settings** (network adapters).

### Scale Computing HC3

Same general procedure. Select **Scale Computing HC3** as hypervisor. Configure **Disk mapping** (storage container, interface, provisioning mode) and **VM settings**.

### oVirt (Red Hat Virtualization)

Same general procedure. Select **oVirt** as hypervisor. Configure **Storage domain** and **Disk mapping**.

### Nutanix

Same general procedure. Select **Nutanix** as hypervisor. Configure **Storage container**, **Disk mapping** (storage container, interface), and **VM settings**.

### Proxmox

Same general procedure. Select **Proxmox** as hypervisor. Configure **Storage**, **Disk mapping** (disk controller type, disk provisioning mode), and **VM settings**.

> **Note (Proxmox):**
> - To recover a disk as VirtIO type disk, in the recovery options select NVME.
> - During recovery to a new machine, VDMK disks are recovered as QCOW2 disks or RAW disks (if you change the provisioning type to thick).

# Recovering containers

You can recover a backed-up container to the original container or to a new container on the same hypervisor. Cross-platform recovery is not supported for containers.

## Virtuozzo container

1. Select the backed-up container, click **Recovery**, select a recovery point.
2. Click **Recover** > **Entire machine**. Original container is selected.
3. [Optional] Change target: **Target container** > **Virtuozzo** > **New container** or **Existing container**.
4. [Optional] Configure: **Storage**, **Disk mapping**, **Container settings** (memory, processors, network).
5. Click **Start recovery**.

## Proxmox container

1. Select the backed-up container, click **Recovery**, select a recovery point.
2. Click **Recover** > **Entire machine**. Original container is selected.
3. [Optional] Change target: **Target container** > **Proxmox** > **New container** or **Existing container**.
4. [Optional] Configure: **Storage**, **Disk mapping**, **Container settings**.
5. Click **Start recovery**.
