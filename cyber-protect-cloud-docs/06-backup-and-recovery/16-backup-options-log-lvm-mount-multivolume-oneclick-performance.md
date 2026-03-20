---
title: "Backup options: Log truncation, LVM, mount points, multi-volume, one-click recovery, performance"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup options"
page_range: "595-605"
tags: ["log-truncation", "SQL-Server", "LVM-snapshotting", "mount-points", "multi-volume-snapshot", "one-click-recovery", "Startup-Recovery-Manager", "performance", "backup-window", "CPU-priority", "output-speed", "physical-data-shipping"]
acronis_version: "26.02"
---

# Log truncation

Preset: **Enabled**.

This option is effective for backups of Microsoft SQL Server databases and for disk-level backups with enabled Microsoft SQL Server application backup. It defines whether the SQL Server transaction logs are truncated after a snapshot is taken in the beginning of the backup operation.

When this option is enabled, a database can be recovered only to a point in time of a backup created by Cyber Protection.

> **Note:** Disable this option if you are backing up transaction logs by using the native backup engine of Microsoft SQL Server.

# LVM snapshotting

This option is effective only for physical machines. It is effective for disk-level backup of volumes managed by Linux Logical Volume Manager (LVM) -- logical volumes.

Preset: **By the backup software**.

- **By the backup software** -- The snapshot data is kept mostly in RAM. The backup is faster, and unallocated space on the volume group is not required. Change the preset only if you are experiencing problems with backing up logical volumes.
- **By LVM** -- The snapshot is stored on unallocated space of the volume group. If the unallocated space is missing, the snapshot will be taken by the backup software.

The snapshot is used only during the backup operation, and is automatically deleted when the backup operation completes.

# Mount points

This option is effective only in Windows for a file-level backup of a data source that includes mounted volumes or cluster shared volumes.

Preset: **Disabled**.

> **Note:** For Linux and macOS, the **Backup Mount Points** option is ignored. Data in "local" mount points (local disks, USB drives, etc.) will always be backed up. Data in "remote" mount points (CIFS/NFS shares, etc.) will never be backed up.

This option is effective only when you select for backup a folder that is higher in the folder hierarchy than the mount point:
- If such a parent folder is selected and **Mount points** is enabled, files on the mounted volume will be included in the backup.
- If **Mount points** is disabled, the mount point folder in the backup will be empty.
- If you select the mount point directly or any folder within the mounted volume, the selected folders are backed up regardless of the **Mount points** option state.

# Multi-volume snapshot

This option is effective for backups of physical machines running Windows or Linux. It applies to disk-level backup and also to file-level backup when the snapshot option is enabled.

Preset:
- If at least one machine running Windows is selected: **Enabled**.
- Otherwise: **Disabled**.

When enabled, snapshots of all volumes being backed up are created simultaneously. Use this option to create a time-consistent backup of data spanning multiple volumes -- for instance, for an Oracle database.

When disabled, the volumes' snapshots are taken one after the other. If the data spans several volumes, the resulting backup may be not consistent.

# One-click recovery

With One-click recovery, you can automatically recover a disk backup of your Windows or Linux machine. The backup can be of the entire machine, or of specific disks or volumes. Machines with Secure Boot and BitLocker encryption are supported.

One-click recovery supports:
- Automatic recovery from the latest backup
- Recovery from a specific backup (recovery point) within the backup archive

Supported backup storages: Secure Zone, Network folder, Cloud storage.

> **Important:** Suspend the BitLocker encryption until the next restart of your machine when you perform any of the following: creating/modifying/deleting Secure Zone, enabling/disabling Startup Recovery Manager, running the first backup after enabling One-click recovery, or updating Startup Recovery Manager.

## Enabling One-click recovery

1. In the protection plan, expand the **Backup** module.
2. In **What to back up**, select **Entire machine** or **Disk/volumes**.
3. [If Disk/volumes] In **Items to back up**, specify the disks or volumes to back up.
4. In **Backup options**, click **Change**, and then select **One-click recovery**.
5. Enable the **One-click recovery** switch.
6. [Optional] Enable the **Recovery password** switch, and then specify a password.
7. Click **Done**.
8. Save the plan.

> **Note:** Enabling One-click recovery also enables Startup Recovery Manager on the target machine. If Startup Recovery Manager cannot be enabled, the backup operation that creates One-click recovery backups will fail.

## Recovering a machine with One-click recovery

Prerequisites: A protection plan with enabled **One-click recovery** is applied to the machine, and there is at least one disk backup.

1. Reboot the machine that you want to recover.
2. During the reboot, press F11 to enter Startup Recovery Manager.
3. Select **Acronis Cyber Protect**.
4. [If password specified] Enter the recovery password, and click **OK**.
5. Select a One-click recovery option:
   - To recover the latest backup automatically, select the first option and click **OK**.
   - To recover another backup within the archive, select the second option and click **OK**. Then select the backup and click **OK**.
6. Confirm your choice by clicking **Yes**.

After a while, the recovery starts. When the recovery completes, your machine reboots.

# Performance and backup window

Preset: **Disabled**.

This option enables you to set one of three levels of backup performance (high, low, prohibited) for every hour within a week. This way, you can define a time window when backups are allowed to start and run.

This option is not available for backups executed by cloud agents (website backups, cloud recovery site backups).

This option is effective only for the backup and backup replication processes. Post-backup commands and other operations (validation, etc.) will run regardless.

When disabled, backups are allowed to run at any time with:
- CPU priority: **Low** (Below normal in Windows)
- Output speed: **Unlimited**

When enabled, scheduled backups are allowed or blocked according to the performance parameters specified for the current hour. At the beginning of an hour when backups are blocked, a backup process is automatically stopped and an alert is generated.

### Backup window states

- **Green:** backup is allowed with the green section parameters below.
- **Blue:** backup is allowed with the blue section parameters below. Not available if the backup format is Version 11.
- **Gray:** backup is blocked.

### CPU priority

This parameter defines the priority of the backup process (**service_process.exe** in Windows, **service_process** in Linux/macOS).

| Cyber Protection priority | Windows priority | Linux and macOS niceness |
|---|---|---|
| Low | Below normal | 10 |
| Normal | Normal | 0 |
| High | High | -10 |

### Output speed during backup

This parameter enables you to limit the hard drive writing speed (local folder) or the speed of transferring backup data through the network (network share or cloud storage).

When enabled, you can specify the maximum allowed output speed:
- As a percentage of the estimated writing speed of the destination hard disk or the estimated maximum speed of the network connection (works only in Windows).
- In KB/second (for all destinations).

# Physical Data Shipping

Preset: **Disabled**.

This option is available if the backup or replication destination is the cloud storage and the backup format is set to **Version 12**.

This option is effective for disk-level backups and file backups created by Agent for Windows, Agent for Linux, Agent for Mac, Agent for VMware, Agent for Hyper-V, and Agent for Virtuozzo.

Use this option to ship the first full backup created by a protection plan to the cloud storage on a hard disk drive. The subsequent incremental backups are performed over the network.

### Overview of the physical data shipping process

1. Create a new protection plan with backup to cloud (or local with replication to cloud).
2. In **Backup options**, click **Change** > **Physical Data Shipping**.
3. Under **Use Physical Data Shipping**, click **Yes** and **Done**. Encryption is enabled automatically.
4. Specify an encryption password.
5. In the **Physical Data Shipping** row, select the removable drive where the initial backup will be saved.
6. Click **Create** to save the protection plan.
7. After the first backup is complete, use the Physical Data Shipping service web interface to download the order creation tool and create the order. Access via **Overview** > **Usage** > **Manage service** under **Physical Data Shipping**.
8. Package the drives and ship them to the data center.
9. Track the order status. Subsequent backups will fail until the initial backup is uploaded to the cloud storage.
