---
title: "Recovery of Physical Machines"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovery of physical machines"
page_range: "628-639"
tags: [recovery, physical-machine, virtual-machine, p2v, p2p, VMware, Azure, Hyper-V, Virtuozzo, Scale-Computing, oVirt, Nutanix, Proxmox]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#recovery-physical-machines.html"
---

# Recovery of Physical Machines

You can recover a disk-level backup of a physical machine to another physical machine or to a virtual machine. For example, a disk-level backup is an **Entire machine** backup or a **Disk/volumes** backup that contains the system disk and boot disk.

## Limitations

- In the Cyber Protect console, you cannot recover backups of machines that are registered in customer tenants in Compliance mode.
- In the Cyber Protect console, you cannot recover backups of macOS physical machines to another physical machine.
- You cannot recover backups of macOS physical machines to a virtual machine.
- During a recovery to a virtual machine, Cyber Protect stops the target virtual machine without a prompt. After the recovery, you must restart this machine manually. You can change the default behavior in **Recovery options** > **VM power management**.

If you want to recover one of the following, use bootable media instead of the Cyber Protect console:

- A physical machine running macOS (you cannot recover disk-level backups of Intel-based Macs to Macs that use Apple silicon processors, and vice-versa; you can recover files and folders).
- A machine in a customer tenant in Compliance mode.
- Any operating system to a bare metal machine or to an offline machine.
- The structure of logical volumes (for example, volumes created by Logical Volume Manager in Linux). With the bootable media, you can automatically recreate the logical volume structure.

## Recovering a Physical Machine as a Physical Machine

You can recover a disk-level backup of a physical machine to the original machine or to a new machine. This procedure describes recovery from the Cyber Protect console. Alternatively, you can use bootable media to recover a backup (including a backup of an offline machine) to a physical machine.

### To recover a physical machine as a physical machine

1. In the Cyber Protect console, do one of the following:
   - **[For online machines]** On the **Devices** tab, select a backed-up machine, click **Recovery**, and then select a backup (recovery point).
   - **[For online and offline machines]** On the **Backup storage** tab, select a backup archive, and then select a backup (recovery point).
   - **[For offline machines]** If the backup location is cloud storage or a shared storage that other agents can access: On the **Devices** tab, select a backed-up machine, and then click **Recovery**. Click **Select machine**, select a target machine that is online, and then click **OK**. Select a backup (recovery point).
2. Click **Recover** > **Entire machine**. A target machine is automatically selected.
3. [If prompted] Specify the credentials to access the backup storage, and then click **OK**.
4. [Optional] To change the target machine: Click **Target machine**, select an online machine, and then click **OK**.
5. [If prompted] Specify the credentials to access the backup storage, and then click **OK**.
6. [Optional] Configure the disk mapping between the backed-up machine and the target machine:
   - **Disk level mapping:** Click **Disk mapping**, configure the mapping, click **Done**.
   - **Volume level mapping:** Click **Disk mapping**, then click **Switch to volume mapping**, configure the mapping, click **Done**.
7. [Optional] [Only available for Windows machines] To ensure that the recovered data is malware-free, enable the **Safe recovery** switch.
8. Click **Start recovery**.
9. [Optional] If you prefer to restart the machine manually after the recovery, clear the **Automatically restart the machine, if required** checkbox.
10. To confirm that you want to overwrite the disks of the target machine, click **Start recovery**.

## Recovering a Physical Machine as a Virtual Machine

You can recover a disk-level backup of a physical machine to a virtual machine. This operation is called cross-platform recovery (machine migration).

### Prerequisites

- An agent for the relevant hypervisor is installed in your environment. For example, recovery to a VMware ESXi virtual machine requires Agent for VMware that is installed and registered in the Cyber Protect console.

### Recovery to VMware ESXi

1. In the Cyber Protect console, select the backed-up machine and select a recovery point.
2. Click **Recover** > **Entire machine**.
3. [If prompted] Specify the credentials to access the backup storage, and then click **OK**.
4. In **Recover to**, select **Virtual machine**.
5. Select a target machine:
   - Click **Target machine**, select **Broadcom (VMware) ESXi**.
   - For a new machine: Select **New machine**, select a host, specify a **Machine name**, click **OK**.
   - For an existing machine: Select **Existing machine**, select the target machine, click **OK**.
6. [If prompted] Specify the credentials to access the backup storage, and then click **OK**.
7. [Optional] When recovering to a new machine, configure additional options:
   - Change the storage: Click **Datastore** and select a datastore.
   - Change disk mapping: Click **Disk mapping**, configure, click **Done**.
   - Change VM settings (memory, vCPUs, network): Click **VM settings**, configure, click **OK**.
8. Click **Start recovery**.

### Recovery to Azure

1. Select the backed-up machine and select a recovery point.
2. Click **Recover** > **Entire machine**, select **Virtual machine** in **Recover to**.
3. Select **Microsoft Azure** as the target hypervisor.
   - For a new machine: Select **New machine**, select an Azure subscription, region, and resource group, specify a name, click **OK**.
   - For the original machine: Select **Original machine**, click **OK**.
4. [Optional] Configure **Disk mapping** (storage type: LRS or ZRS) and **VM settings** (availability type, zone, memory, subnets, security groups).
5. Click **Start recovery**.

### Recovery to Hyper-V

1. Select the backed-up machine and recovery point.
2. Click **Recover** > **Entire machine**, select **Virtual machine** in **Recover to**.
3. Select **Microsoft Hyper-V** as the target hypervisor.
   - For a new machine: Select **New machine**, select a host, specify a name, click **OK**.
   - For an existing machine: Select **Existing machine**, select the target, click **OK**.
4. [Optional] Configure storage (**Path**), **Disk mapping** (including storage, interface, and provisioning mode per virtual disk), and **VM settings**.
5. Click **Start recovery**.

### Recovery to Other Hypervisors

The same general procedure applies for recovery to:

- **Virtuozzo Hybrid Infrastructure** -- configure disk mapping and storage policy per disk, network adapters via VM settings.
- **Scale Computing HC3** -- configure disk mapping, storage container/interface/provisioning mode per disk.
- **oVirt** -- configure storage domain and disk mapping.
- **Nutanix** -- configure storage container, disk mapping, and storage container/interface per disk, plus VM settings.
- **Proxmox** -- configure storage, disk mapping (disk controller type, provisioning mode), and VM settings.

In each case, follow the standard steps: select the backed-up machine, choose a recovery point, select **Recover** > **Entire machine**, set **Recover to** to **Virtual machine**, choose the hypervisor, select a new or existing machine, configure options, and click **Start recovery**.

> **Note:** To recover a disk as VirtIO type disk, in the recovery options, select NVME. During a recovery to a new machine, VDMK disks are recovered as QCOW2 disks or RAW disks (if you change the provisioning type to thick).
