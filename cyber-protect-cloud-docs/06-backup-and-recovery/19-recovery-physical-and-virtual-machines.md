---
title: "Recovering physical machines and virtual machines"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovery"
page_range: "628-637"
tags: ["recovery", "physical-machine", "virtual-machine", "P2V", "P2P", "VMware", "Hyper-V", "Azure", "Scale-Computing", "oVirt", "Nutanix", "Virtuozzo", "disk-mapping", "VM-settings", "safe-recovery"]
acronis_version: "26.02"
---

# Recovery of physical machines

You can recover a disk-level backup of a physical machine to another physical machine or to a virtual machine. A disk-level backup is an **Entire machine** backup or a **Disk/volumes** backup that contains the system disk and boot disk.

## Limitations

- In the Cyber Protect console, you cannot recover backups of machines registered in customer tenants in Compliance mode.
- In the Cyber Protect console, you cannot recover backups of macOS physical machines to another physical machine.
- You cannot recover backups of macOS physical machines to a virtual machine.
- During a recovery to a virtual machine, Cyber Protect stops the target virtual machine without a prompt. After the recovery, you must restart this machine manually. You can change the default behavior in **Recovery options** > **VM power management**.

**Use bootable media instead of the Cyber Protect console for:**
- A physical machine running macOS (you cannot recover disk-level backups of Intel-based Macs to Macs that use Apple silicon, and vice-versa; you can recover files and folders)
- A machine in a customer tenant in Compliance mode
- Any operating system to a bare metal machine or to an offline machine
- The structure of logical volumes (e.g., LVM in Linux); with bootable media, you can automatically recreate the logical volume structure

## Recovering a physical machine as a physical machine

1. In the Cyber Protect console, do one of the following:
   - **For online machines:** On the **Devices** tab, select a backed-up machine, click **Recovery**, and then select a backup (recovery point).
   - **For online and offline machines:** On the **Backup storage** tab, select a backup archive, and then select a backup (recovery point).
   - **For offline machines** (when the backup location is cloud storage or shared storage): On the **Devices** tab, select a backed-up machine, click **Recovery**. Click **Select machine**, select a target machine that is online, and then click **OK**. Select a recovery point.
2. Click **Recover** > **Entire machine**. A target machine is automatically selected.
3. [If prompted] Specify the credentials to access the backup storage, and then click **OK**.
4. [Optional] To change the target machine:
   - Click **Target machine**.
   - Select an online machine, and then click **OK**.
5. [Optional] Configure disk mapping between the backed-up machine and the target machine:
   - **Disk-level mapping:** Click **Disk mapping**, configure, click **Done**.
   - **Volume-level mapping:** Click **Disk mapping**, then click **Switch to volume mapping**, configure, click **Done**.
6. [Optional] [Windows only] Enable **Safe recovery** to ensure the recovered data is malware-free.
7. Click **Start recovery**.
8. [Optional] To restart the machine manually after recovery, clear the **Automatically restart the machine, if required** checkbox.
9. Confirm that you want to overwrite the disks of the target machine. Click **Start recovery**.

## Recovering a physical machine as a virtual machine

This operation is called cross-platform recovery (machine migration).

### Prerequisites

An agent for the relevant hypervisor is installed in your environment. For example, recovery to a VMware ESXi virtual machine requires Agent for VMware that is installed and registered in the Cyber Protect console.

### Supported target hypervisors

The general procedure is the same for all target hypervisors. The specific options differ:

#### VMware ESXi

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine**.
3. In **Recover to**, select **Virtual machine**.
4. Click **Target machine** > Select **Broadcom (VMware) ESXi**.
5. Choose **New machine** (select a host, specify name) or **Existing machine**.
6. [Optional] Configure additional options:
   - **Datastore** -- select a datastore for the new VM.
   - **Disk mapping** -- configure which disks to recover or exclude.
   - **VM settings** -- change memory size, number of virtual processors, or network connections.
7. Click **Start recovery**.

#### Microsoft Azure

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine** > **Recover to** > **Virtual machine**.
3. Click **Target machine** > Select **Microsoft Azure**.
4. Choose **New machine** (select subscription, region, resource group, and name) or **Original machine**.
5. [Optional] Configure:
   - **Disk mapping** -- change storage type (LRS or ZRS) for each target disk.
   - **VM settings** -- change availability type, zone, memory size, and network connections (subnets and security groups).
6. Click **Start recovery**.

#### Microsoft Hyper-V

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine** > **Recover to** > **Virtual machine**.
3. Click **Target machine** > Select **Microsoft Hyper-V**.
4. Choose **New machine** (select host, specify name) or **Existing machine**.
5. [Optional] Configure:
   - **Path** -- select storage for the VM.
   - **Disk mapping** -- configure disk mapping; change storage, interface, or provisioning mode for each virtual disk via the gear icon.
   - **VM settings** -- change memory, processors, or network connections.
6. Click **Start recovery**.

#### Virtuozzo Hybrid Infrastructure

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine** > **Recover to** > **Virtual machine**.
3. Click **Target machine** > Select **Virtuozzo Hybrid Infrastructure**.
4. Choose **New machine** or **Existing machine**.
5. [Optional] Configure: **Disk mapping** (select disks, set storage policy), **VM settings** (network adapters).
6. Click **Start recovery**.

#### Scale Computing HC3

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine** > **Recover to** > **Virtual machine**.
3. Click **Target machine** > Select **Scale Computing HC3**.
4. Choose **New machine** or **Existing machine**.
5. [Optional] Configure: **Disk mapping** (select disks, set storage container, interface, provisioning mode), **VM settings**.
6. Click **Start recovery**.

#### oVirt (Red Hat Virtualization)

1. Select backup and recovery point.
2. Click **Recover** > **Entire machine** > **Recover to** > **Virtual machine**.
3. Click **Target machine** > Select **oVirt**.
4. Choose **New machine** or **Existing machine**.
5. [Optional] Configure: **Storage domain**, **Disk mapping**.
6. Click **Start recovery**.

#### Nutanix

Similar procedure: select backup, choose **Recover** > **Entire machine** > **Virtual machine** > **Nutanix**. Configure new/existing machine, disk mapping, and VM settings.
