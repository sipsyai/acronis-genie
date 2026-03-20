---
title: "Backup options: Validation, CBT, cluster mode, compression, error handling"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup options"
page_range: "575-578"
tags: ["backup-validation", "CBT", "changed-block-tracking", "cluster-backup", "SQL-Server", "Exchange-Server", "AAG", "DAG", "compression", "error-handling", "bad-sectors", "silent-mode"]
acronis_version: "26.02"
---

# Backup validation

Preset: **Disabled**.

Validation is an operation that checks the possibility of data recovery from a backup. When this option is enabled, each backup created by the protection plan is validated immediately after creation by using the checksum verification method. This operation is performed by the protection agent.

> **Note:** Validation might not be available when backing up to the cloud storage or for backup locations on public clouds.

# Changed block tracking (CBT)

Preset: **Enabled**.

This option is effective for:
- Disk-level backups of virtual machines
- Disk-level backups of physical machines running Windows
- Backups of Microsoft SQL Server databases
- Backups of Microsoft Exchange Server databases

This option determines whether to use Changed Block Tracking (CBT) when performing an incremental or differential backup. The CBT technology accelerates the backup process. Changes to the disk or database content are continuously tracked at the block level. When a backup starts, the changes can be immediately saved to the backup.

# Cluster backup mode

These options are effective for database-level backup of Microsoft SQL Server and Microsoft Exchange Server. These options are effective only if the cluster itself (Microsoft SQL Server Always On Availability Groups (AAG) or Microsoft Exchange Server Database Availability Group (DAG)) is selected for backup, rather than individual nodes or databases.

## Microsoft SQL Server

Preset: **Secondary replica if possible.**

This option determines the backup mode for SQL Server Always On Availability Groups (AAG). Agent for SQL must be installed on all of the AAG nodes.

- **Secondary replica if possible** -- if all secondary replicas are offline, the primary replica is backed up. May slow down the SQL Server operation.
- **Secondary replica** -- if all secondary replicas are offline, the backup will fail. Backing up secondary replicas does not affect the SQL server performance but may contain information that is not up-to-date (lagged replicas).
- **Primary replica** -- if the primary replica is offline, the backup will fail. May slow down the SQL Server operation but provides the most recent state.

The software skips databases not in the **SYNCHRONIZED** or **SYNCHRONIZING** states when the backup starts. If all databases are skipped, the backup fails.

## Microsoft Exchange Server

Preset: **Passive copy if possible.**

This option determines the backup mode for Exchange Server Database Availability Groups (DAG). Agent for Exchange must be installed on all of the DAG nodes.

- **Passive copy if possible** -- if all passive copies are offline, the active copy is backed up.
- **Passive copy** -- if all passive copies are offline, the backup will fail. Passive copies may contain information that is not up-to-date.
- **Active copy** -- if the active copy is offline, the backup will fail. Provides the most recent state.

The software skips databases not in the **HEALTHY** or **ACTIVE** states when the backup starts. If all databases are skipped, the backup fails.

# Compression level

> **Note:** This option is not available for cloud-to-cloud backups. Compression for these backups is enabled by default at a fixed level corresponding to **Normal**.

Preset: **Normal**.

The available levels are: **None**, **Normal**, **High**, **Maximum**.

A higher compression level means the backup process takes more time, but the resulting backup occupies less space. Currently, the **High** and **Maximum** levels work similarly.

The optimal data compression level depends on the type of data. For example, even maximum compression will not significantly reduce the backup size if the backup contains essentially compressed files (such as .jpg, .pdf, or .mp3). However, formats such as .doc or .xls will be compressed well.

# Error handling

## Re-attempt, if an error occurs

Preset: **Enabled. Number of attempts: 30. Interval between attempts: 30 seconds.**

When a recoverable error occurs, Cyber Protect re-attempts the unsuccessful operation. You can set the maximum number of re-attempts and the interval between them. If the operation cannot finish successfully after the maximum number of re-attempts, it fails.

For backups to a network location or cloud storage, the error handling depends on the moment when the error occurs:

| Error occurs when the backup starts | Error occurs during an ongoing backup |
|---|---|
| The number of re-attempts depends on the response from the storage API. If the API returns a retriable response (e.g., "503 Service unavailable"), it might take up to two hours. | The number of retries depends on the **Error handling** settings configured in the protection plan. For example, 30 retries with 30-second interval between each retry. |

For backups to local folders, the **Error handling** settings only apply to errors that occur during an ongoing backup.

## Do not show messages and dialogs while processing (silent mode)

Preset: **Enabled**.

With silent mode enabled, the program automatically handles situations requiring user interaction (except for handling bad sectors). If an operation cannot continue without user interaction, it will fail. Details can be found in the operation log.

## Ignore bad sectors

Preset: **Disabled**.

When this option is disabled, each time the program comes across a bad sector, the backup activity will be assigned the **Interaction required** status. To back up valid information on a rapidly dying disk, enable ignoring bad sectors. The rest of the data will be backed up, and you will be able to mount the resulting disk backup and extract valid files to another disk.

> **Note:** Skipping bad sectors is not supported on Linux. You can back up Linux systems with bad sectors in offline mode by using the bootable media builder in the on-premises version of Cyber Protect.

## Re-attempt, if an error occurs during VM snapshot creation

Preset: **Enabled. Number of attempts: 3. Interval between attempts: 5 minutes.**

When taking a virtual machine snapshot fails, the program re-attempts the operation. You can set the time interval and the number of attempts.
