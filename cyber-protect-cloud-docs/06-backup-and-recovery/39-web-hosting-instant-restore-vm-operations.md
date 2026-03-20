---
title: "Web Hosting Servers and Special VM Operations (Instant Restore)"
section: "Managing the backup and recovery of workloads and files"
subsection: "Web hosting servers and special VM operations"
page_range: "876-905"
tags: [web-hosting, Plesk, cPanel, DirectAdmin, Instant-Restore, Run-as-VM, finalization, VM-replication, VMware-vSphere, failover, failback, LAN-free-backup, SAN, locally-attached-storage, virtual-machine-binding, Hyper-V-cluster, Azure-backup, EC2-backup, simultaneous-backups]
acronis_version: "26.02"
---

# Protecting Web Hosting Servers

You can protect Linux-based web hosting servers that run Plesk, cPanel, DirectAdmin, VirtualMin, or ISPManager control panels. Servers running other vendors' panels are protected as regular workloads.

## Quotas

Servers running Plesk, cPanel, DirectAdmin, VirtualMin, or ISPManager consume the **Web hosting servers** quota. If this quota is disabled or exceeded:

- Physical servers fall back to the **Servers** quota.
- Virtual servers fall back to the **Virtual machines** quota.

## Integrations for DirectAdmin, cPanel, and Plesk

Web hosting administrators can integrate these control panels with the Cyber Protection service for:

- Backing up entire web hosting servers to cloud storage with disk-level backup.
- Recovering the entire server, including all websites and accounts.
- Performing granular recovery and downloading of accounts, websites, individual files, mailboxes, or databases.
- Enabling resellers and customers to perform self-service recovery of their own data.

Integration requires a Cyber Protection service extension. Refer to the corresponding integration guides: DirectAdmin Integration Guide, WHM and cPanel Integration Guide, Plesk Integration Guide.

---

# Special Operations with Virtual Machines

## Running a Virtual Machine from a Backup (Instant Restore)

By using **Run as VM**, you can start a virtual machine from a disk-level backup that contains an operating system. This operation, also known as Instant Restore, quickly brings a virtual machine online. While running, its disks are emulated directly from the backup, and storage space is only needed for ongoing changes.

### Typical Use Cases

- **Disaster recovery:** Instantly bring online a copy of a failed machine.
- **Backup verification:** Run a machine from backup to confirm the OS and applications function correctly.
- **Accessing application data:** Use the application's native management tools on the running machine.

We recommend keeping the temporary machine for up to three days, then converting it to a regular VM by finalizing it.

### Prerequisites

- At least one agent (Agent for VMware, Agent for Hyper-V, or Agent for Proxmox) must be registered.
- The backup must be located in a network folder or local folder. Cloud storage is supported but performance will be slower.
- **Run as VM** requires a backup of the entire machine or all volumes needed for OS startup.
- You can use backups of physical and virtual machines. You cannot use backups of containers.
- If the backup contains Linux logical volumes (LVM), the temporary VM must match the original platform (VMware ESXi, Hyper-V, or Proxmox).

### Running a VM from a Backup

**VMware ESXi:**
1. Select a backup (recovery point), click **Run as VM**.
2. [Optional] Set **Power state** for auto-start.
3. In **Target machine**, select **VMware ESXi**, choose a location and name, click **OK**.
4. In **Datastore**, select storage.
5. [Optional] In **VM settings**, edit memory, network. Click **OK**.
6. Click **Run now**.

**Microsoft Hyper-V:**
1. Select a backup, click **Run as VM**.
2. [Optional] Set **Power state**.
3. In **Target machine**, select **Hyper-V**, choose location and name.
4. In **Path**, select storage location.
5. [Optional] In **VM settings**, edit memory/network.
6. Click **Run now**.

**Proxmox VE:**
1. Select a backup, click **Run as VM**.
2. [Optional] Set **Power state**.
3. In **Target machine**, select **Proxmox VE**, choose location and name.
4. In **Storage**, select storage.
5. [Optional] In **VM settings**, edit memory/network.
6. Click **Run now**.

The VM running from a backup appears with special icons in the Cyber Protect console. You cannot back up these machines.

### Deleting a VM Running from a Backup

1. Select the machine in the Cyber Protect console.
2. In **Actions**, click **Delete**. Confirm.

The machine is removed from the console, hypervisor inventory, and storage. All changes made while running are discarded.

> **Note:** Do not delete these machines directly in vSphere, Hyper-V, or Proxmox VE consoles.

### Finalizing a VM Running from a Backup

Finalization converts the temporary VM into an independent, permanent virtual machine stored on production-ready storage. The VM remains powered on throughout the process.

**VMware ESXi:** Select the machine > **Actions** > **Finalize** > specify name > select disk provisioning mode > click **Finalize**.

**Hyper-V / Proxmox VE:** Select the machine > **Actions** > **Finalize** > specify name > click **Finalize**.

> **Note:** Finalization is not supported for Hyper-V machines running on Windows Server 2008/2008 R2.

**Finalization vs. backup recovery:** Finalization is slower because it involves random reads from the backup (supporting both the running VM and the migration process), while backup recovery reads sequentially.

**Finalization from cloud backups:** Typically slower than from local backups due to bandwidth constraints. Use local backups whenever possible if you plan to perform finalization.

---

## Working in VMware vSphere

### Replication of Virtual Machines

Replication creates an exact copy (replica) of a VM and keeps it in sync with the original. The first replication is full; subsequent replications are incremental using Changed Block Tracking (CBT).

**Replication vs. backing up:** A replica keeps only the latest state and consumes datastore space. Backups can be stored on cheaper storage. However, powering on a replica is much faster than a recovery and faster than Run as VM.

**Usage examples:**
- Replicate VMs to a remote site for datacenter failure protection.
- Replicate within a single site for high availability.

**What you can do with a replica:** Test it, failover to it, back it up.

**Limitations:**
- Fault-tolerant machines (ESXi 5.5 and lower), machines running from backups, and replicas of VMs cannot be replicated.
- NIC hardware changes on the ESXi host require recreating replication plans.

### Creating a Replication Plan

1. Select a VM, click **Replication**.
2. [Optional] Modify the plan name.
3. Click **Target machine**: select new or existing replica, specify ESXi host and name.
4. [For new machines] Click **Datastore** to select storage.
5. [Optional] Click **Schedule** (default: daily, Mon-Fri).
6. [Optional] Click the gear icon for **Replication options** (CBT, disk provisioning, error handling, pre/post commands, VSS).
7. Click **Apply**.

### Replication Options

- **Changed Block Tracking (CBT):** Same as backup option.
- **Disk provisioning:** Thin (default), Thick, or Keep original setting.
- **Error handling, Pre/Post commands, VSS for VMs:** Same as corresponding backup options.

### Testing a Replica

1. Select the replica, click **Test replica** > **Start testing**.
2. Choose whether to connect it to a network.
3. [Optional] Select **Stop original virtual machine** if connecting to network.
4. Click **Start**. To stop: **Test replica** > **Stop testing**.

### Failing Over to a Replica

1. Select the replica, click **Replica actions** > **Failover**.
2. Choose network connection and optionally stop the original machine.
3. Click **Start**.

During failover state, you can: **Stop failover** (power off replica, resume replication), **Perform permanent failover** (remove replica flag, make it a regular VM), or **Failback** (recover replica to original or new machine).

### Seeding an Initial Replica

To speed up replication to a remote location:
1. Create a replication plan targeting **New replica** on the original ESXi.
2. Run the plan once.
3. Export the replica as an OVF template to an external drive.
4. Transfer the drive to the remote location.
5. Import the replica to the target ESXi.
6. Edit the replication plan to target **Existing replica** (the imported one).

### Agent for VMware - LAN-Free Backup

If your ESXi uses SAN attached storage, install Agent for VMware on a machine connected to the same SAN. The agent reads VM data directly from storage via FC or iSCSI, eliminating LAN transfer.

**To enable:** Install Agent for VMware (Windows), connect the LUN hosting the datastore to the machine. The LUN must NOT be initialized and must appear as "offline" in Disk Management.

**SAN policy configuration:** Open `diskpart`, type `san`, ensure `SAN Policy: Offline All`. If not, type `san policy=offlineall`, press Enter, restart.

**Limitations:** In vSphere 6.0+, SAN transport cannot be used if some VM disks are on VMware Virtual Volumes (VVol) and some are not. Encrypted VMs (vSphere 6.5) are always backed up via LAN.

### Using Locally Attached Storage

Agent for VMware (Virtual Appliance) or Agent for Scale Computing HC3 can use locally attached storage to eliminate network traffic. Recommended disk size: up to 5 TB. Add a hard disk (minimum 10 GB) to the virtual appliance, then configure it via the console under **Local storages** > **Refresh** > **Create storage**.

### Virtual Machine Binding

VMs are automatically distributed evenly among Agents for VMware. The distribution algorithm prefers agents on the same host, then the same cluster. Redistribution occurs when load imbalance reaches 20%.

**Manual binding:** Select machine > **Details** > **Assigned agent** > **Change** > **Manual** > select agent > **Save**.

**Disabling automatic assignment:** Go to **Settings** > **Agents**, select the agent, click **Details**, disable the **Automatic assignment** switch.

### Pre-Freeze and Post-Thaw Scripts

VMware Tools allows running custom scripts on VMs during agentless backup. Scripts are placed in:
- **Windows:** `C:\Program Files\VMware\VMware Tools\backupScripts.d\` (create the folder manually)
- **Linux:** `/usr/sbin/pre-freeze-script` and `/usr/sbin/post-thaw-script`

Enable **Volume Shadow Copy Service (VSS) for virtual machines** in the protection plan.

### vMotion and Storage vMotion Support

- vMotion is not supported for Agent for VMware (Virtual Appliance) VMs. Disable it after deployment.
- During backup, vMotion is automatically disabled temporarily.
- Backups cannot start while a VM is migrating.

### Protection of Virtualization Environments

On the **VMware** tab, you can back up vSphere infrastructure objects: vCenter, Datacenter, Folder, Cluster, ESXi host, Resource pool, Virtual machine. Click **Protect** for individual objects or **Protect group** for parent objects.

### Required Privileges for Agent for VMware

Agent for VMware authenticates to vCenter/ESXi with a user account needing specific privileges for each operation (backup, recover to new/existing VM, Run VM from backup). Key privilege categories include: Cryptographic operations, Datastore, Global, Host, Network, Resource, Virtual machine (Change Configuration, Guest operations, Interaction, Inventory, Provisioning, State, Snapshot management), and vApp.

### Changing the User Account for Agent for VMware

**For all agents:** Go to **Devices** > **VMware** > **Hosts and clusters**, click next to vCenter/ESXi host, click **Details** > **Credentials** > update account.

**For an individual agent:** Go to **Settings** > **Agents**, select agent, click **Details** > **Assigned virtual machines** > click vCenter/ESXi name > update credentials.

---

## Backing Up Clustered Hyper-V Machines

In a Hyper-V cluster:
1. Install Agent for Hyper-V on each node.
2. Run the agent service under a domain user account with administrative privileges on each node.
3. Register all agents in the Cyber Protection service.

**High Availability of recovered machines:** Recovery to an existing Hyper-V VM preserves the HA property. Recovery to a new VM creates a non-HA spare machine. Configure HA from the **Failover Cluster Management** snap-in.

## Limiting Simultaneous Backups

To limit the number of simultaneously backed-up VMs at the agent level, configure a registry key (Windows agents) or the `/etc/Acronis/MMS.config` file (virtual appliances and Linux-based agents):

- **Agent for VMware (Windows) / Agent for Hyper-V:** Create `limit.reg` with `MaxNumberOfSimultaneousBackups` DWORD value, run it, restart the `mms` service.
- **Virtual appliances:** Edit `/etc/Acronis/MMS.config`, modify `MaxNumberOfSimultaneousBackups`, reboot.
- **Agents bundled with Agent for Linux:** Edit `/etc/Acronis/MMS.config`, modify the value, run `sudo service acronis_mms restart`.

---

## Agent-Based Backup of Microsoft Azure and Amazon EC2 VMs

If you do not use Agent for Azure, install a protection agent directly on the Azure or EC2 VM. Backup and recovery operations are the same as for physical machines. The backed-up machine will be counted as virtual when you set quotas.

> **Note:** You cannot boot Azure and EC2 VMs from bootable media.

**To recover as a new Azure or EC2 VM:**
1. Create a new VM from an image/template with the same disk configuration.
2. Install Agent for Windows or Agent for Linux.
3. Recover the backup to this new machine.

> **Note:** For Azure VMs, this recovery procedure applies only to backups of machines that contain drivers for running in Azure natively.
