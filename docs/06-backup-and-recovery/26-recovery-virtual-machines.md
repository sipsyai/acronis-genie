---
title: "Recovery of Virtual Machines"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovery of virtual machines"
page_range: "640-653"
tags: [recovery, virtual-machine, v2p, v2v, containers, VMware, Azure, Hyper-V, Virtuozzo, oVirt, Nutanix, Proxmox, Scale-Computing, bootable-media]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#recovery-virtual-machines.html"
---

# Recovery of Virtual Machines

You can recover a disk-level backup of a virtual machine to a physical machine or another virtual machine. For example, a disk-level backup is an **Entire machine** backup or a **Disk/volumes** backup that contains the system disk and boot disk.

## Limitations

- In the Cyber Protect console, you cannot recover backups of machines that are registered in customer tenants in Compliance mode.
- During a recovery to a virtual machine, Cyber Protect stops the target virtual machine without a prompt. After the recovery, you must restart this machine manually. You can change the default behavior in **Recovery options** > **VM power management**.
- You can recover a backup of a virtual machine to a physical machine if the disk configuration of the target machine exactly matches the disk configuration in the backup. Alternatively, you can perform a virtual-to-physical migration by using bootable media.
- You cannot recover macOS virtual machines to Hyper-V hosts because Hyper-V does not support macOS. You can recover macOS virtual machines to a VMware host that is installed on Mac hardware.

## Recovering a Virtual Machine as a Physical Machine

This operation is called cross-platform recovery (machine migration). The following procedure describes recovery from the Cyber Protect console. Alternatively, you can use bootable media.

### To recover a virtual machine as a physical machine

1. In the Cyber Protect console, select the backed-up machine and a recovery point:
   - On the **Devices** tab, select the machine, click **Recovery**, and select a backup.
   - On the **Backup storage** tab, select a backup archive and select a backup.
2. Click **Recover** > **Entire machine**.
3. [If prompted] Specify the credentials to access the backup storage, and then click **OK**.
4. In **Recover to**, select **Physical machine**. A target machine is automatically selected.
5. [Optional] To change the target machine: Click **Target machine**, select an online machine, click **OK**.
6. [If prompted] Specify the credentials to access the backup storage.
7. [Optional] Configure the disk mapping:
   - **Disk level:** Click **Disk mapping**, configure, click **Done**.
   - **Volume level:** Click **Disk mapping**, then **Switch to volume mapping**, configure, click **Done**.

> **Note:** You can select individual disks or volumes for recovery. Ensure that the disk or volume configuration of the backed-up machine matches exactly the disk or volume configuration of the target machine.

8. [Optional] [Windows only] Enable the **Safe recovery** switch for malware-free recovery.
9. Click **Start recovery**.
10. [Optional] Clear the **Automatically restart the machine, if required** checkbox if you prefer manual restart.
11. Confirm that you want to overwrite the disks of the target machine by clicking **Start recovery**.

## Recovering a Virtual Machine as a Virtual Machine

You can recover a backup of a virtual machine to the original hypervisor or to a different type of hypervisor. Recovery to a different type of hypervisor is called cross-platform recovery (machine migration).

- **Agentless recovery:** Recovering to a virtual machine on which a protection agent is not installed is done on the hypervisor level.
- **Agent-based recovery:** Recovering to a virtual machine on which a protection agent is installed. This type of recovery is the same as a recovery to a physical machine.

### Prerequisites

An agent for the relevant hypervisor is installed in your environment.

### Recovery Procedures by Hypervisor

For each target hypervisor (VMware ESXi, Azure, Hyper-V, Virtuozzo, Virtuozzo Hybrid Infrastructure, Scale Computing HC3, oVirt, Nutanix, Proxmox), the general process is the same:

1. In the Cyber Protect console, select the backed-up machine and a recovery point.
2. Click **Recover** > **Entire machine**. The original virtual machine is selected as a target machine.
3. [If prompted] Specify the credentials to access the backup storage, and then click **OK**.
4. [Optional] To change the target machine:
   - Click **Target machine**.
   - Select the desired hypervisor.
   - For a new machine: Select **New machine**, select a host, specify a **Machine name**, click **OK**.
   - For an existing machine: Select **Existing machine**, select the target machine, click **OK**.
5. [If prompted] Specify the credentials to access the backup storage.
6. [Optional] When recovering to a new machine, configure additional options specific to each hypervisor:
   - **VMware ESXi:** Datastore, disk mapping, VM settings (memory, vCPUs, network).
   - **Azure:** Disk mapping (LRS/ZRS storage type), VM settings (availability type, zone, memory, subnets, security groups).
   - **Hyper-V:** Path (storage), disk mapping (storage, interface, provisioning mode per virtual disk), VM settings.
   - **Virtuozzo:** Path (storage), disk mapping, VM settings. Only a Virtuozzo virtual machine can be recovered to a Virtuozzo virtual machine.
   - **Virtuozzo Hybrid Infrastructure:** Disk mapping, storage policy per disk, VM settings (network adapters).
   - **Scale Computing HC3:** Disk mapping, storage container/interface/provisioning mode per disk.
   - **oVirt:** Storage domain, disk mapping.
   - **Nutanix:** Storage container, disk mapping (storage container/interface per disk), VM settings.
   - **Proxmox:** Storage, disk mapping (disk controller type, provisioning mode), VM settings.
7. Click **Start recovery**.
8. [When recovering to an existing machine] Confirm that you want to overwrite the target machine.

## Recovering Containers

You can recover a backed-up container to the original container or to a new container on the same hypervisor. Cross-platform recovery is not supported for containers.

### Virtuozzo Container Recovery

1. In the Cyber Protect console, select the backed-up container and a recovery point.
2. Click **Recover** > **Entire machine**. The original container is selected as a target container.
3. [If prompted] Specify the credentials to access the backup storage.
4. [Optional] To change the target container: Click **Target container**, select **Virtuozzo**, then select **New container** or **Existing container**.
5. [If prompted] Specify credentials.
6. [Optional] Configure storage, disk mapping, and **Container settings** (memory, vCPUs, network).
7. Click **Start recovery**.

### Proxmox Container Recovery

1. In the Cyber Protect console, select the backed-up container and a recovery point.
2. Click **Recover** > **Entire machine**. The original container is selected as a target container.
3. [If prompted] Specify the credentials to access the backup storage.
4. [Optional] To change the target container: Click **Target container**, select **Proxmox**, then select **New container** or **Existing container**.
5. [If prompted] Specify credentials.
6. [Optional] Configure storage, disk mapping, and **Container settings** (memory, vCPUs, network).
7. Click **Start recovery**.

## Recovering Disks by Using Bootable Media

Running the bootable media requires 1.5 GB of RAM.

> **Note:** You cannot recover disk-level backups of Intel-based Macs to Macs that use Apple silicon processors, and vice-versa. You can recover files and folders.

### To recover disks by using bootable media

1. Boot the target machine by using bootable media.
2. [Only when recovering a Mac] If you are recovering APFS-formatted disks/volumes to a non-original machine or to bare metal, re-create the original disk configuration manually using **Disk Utility**.
3. Click **Manage this machine locally** or click **Rescue Bootable Media** twice.
4. If a proxy server is enabled, click **Tools** > **Proxy server** and configure the proxy.
5. [Optional] Click **Tools** > **Register media in the Cyber Protection service** and specify the registration token.
6. On the welcome screen, click **Recover**.
7. Click **Select data**, and then click **Browse**.
8. Specify the backup location (Cloud storage, Local folders, Network folders, or public cloud storage via Register media).
9. Select the backup. If prompted, type the password for the backup.
10. In **Backup contents**, select the disks that you want to recover. Click **OK**.
11. Under **Where to recover**, the software automatically maps the selected disks to the target disks. Re-map disks manually if needed.
12. [When recovering Linux with LVM] To reproduce the original LVM structure, ensure target disks match or exceed original capacity, then click **Apply RAID/LVM**.
13. [Optional] Click **Recovery options** to specify additional settings.
14. Click **OK** to start the recovery.

> **Note:** Changing disk layout may affect the operating system bootability. Please use the original machine's disk layout unless you feel fully confident of success.
