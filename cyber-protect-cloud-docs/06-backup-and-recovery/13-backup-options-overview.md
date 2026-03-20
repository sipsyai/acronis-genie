---
title: "Default backup options and backup options overview"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup options"
page_range: "563-570"
tags: ["backup-options", "default-options", "alerts", "Azure-restore-points", "backup-consolidation", "backup-file-name", "backup-format", "version-11", "version-12", "TIBX", "TIB"]
acronis_version: "26.02"
---

# Default backup options

The default values of backup options exist at the company, unit, and user level. When a unit or a user account is created within a company or within a unit, it inherits the default values set for the company or for the unit.

Company administrators, unit administrators, and every user without administrator rights can change a default option value against the pre-defined one. The new value will be used by default in all protection plans created at the respective level after the change takes place.

When creating a protection plan, a user can override a default value with a custom value that will be specific for this plan only.

### To change a default option value

1. Sign in to the Cyber Protect console as the appropriate administrator or user.
2. Click **Settings** > **System settings**.
3. Expand the **Default backup options** section.
4. Select the option, and then make the necessary changes.
5. Click **Save**.

# Backup options

To modify the backup options of a protection plan, in the **Backup** module, in the **Backup options** field, click **Change**.

## Availability of the backup options

The set of available backup options depends on:
- The environment the agent operates in (Windows, Linux, macOS)
- The type of data being backed up (disks, files, virtual machines, application data)
- The backup destination (cloud storage, local or network folder)

The "Other" column under "Virtual machines (agentless backup)" contains aggregated information for: Virtuozzo Hybrid Server, Virtuozzo Hybrid Infrastructure, Scale Computing, oVirt, Proxmox VE, and Nutanix AHV.

## Alerts

**No successful backups for a specified number of consecutive days**

Preset: **Disabled**.

This option determines whether to generate an alert if no successful backups were performed by the protection plan for a specified period. In addition to failed backups, the software counts backups that did not run on schedule (missed backups). The alerts are generated on a per-machine basis and are displayed on the **Alerts** tab.

## Azure restore points

Three Microsoft Azure backup options are available when configuring agentless backup of Microsoft Azure virtual machines:

### Azure restore points: Retention

Defines how many Microsoft Azure restore points to keep after a backup (default is 3). These restore points improve the performance of incremental backups using CBT. The maximum is 200 (as recommended by Microsoft), and there must be only one restore point collection per VM.

When performing recovery to the original Microsoft Azure VM from a backup that has a corresponding Azure restore point still available, the recovery process uses this restore point to revert the VM state automatically instead of retrieving data from the backup file.

### Azure restore points: Consistency level

Select the consistency level of restore points:
- **Require application-consistent restore points** -- backup fails if not application-consistent. Application-consistent points use VSS writers (Windows) or pre/post scripts (Linux).
- **Warn on file-system or crash-consistent restore points** -- backup completes with a warning if the point is file-system consistent or crash-consistent.
- **Warn on crash-consistent restore points** (default) -- backup completes with a warning only if the point is crash-consistent.
- **Ignore consistency level** -- backup will complete successfully regardless of consistency.

### Azure restore points: Handling unsupported disks

Determines what to do if a VM with an unmanaged, shared, or Ephemeral disk is backed up (these are not supported in Microsoft Azure restore points):
- **Ignore unsupported disks** -- backup completes, unsupported disks are skipped.
- **Warn on unsupported disks** (default) -- backup completes with a warning.
- **Fail on unsupported disks** -- backup fails.

## Backup consolidation

Preset: **Disabled**.

This option defines whether to consolidate backups during cleanup or to delete entire backup chains.

Consolidation is the process of combining two or more subsequent backups into a single backup. If enabled, a backup that should be deleted during cleanup is consolidated with the next dependent backup (incremental or differential). Otherwise, the backup is retained until all dependent backups become subject to deletion.

> **Important:** Consolidation is just a method of deletion, but not an alternative to deletion. The resulting backup will not contain data that was present in the deleted backup and was absent from the retained incremental or differential backup.

This option is *not* effective if:
- The backup destination is the cloud storage
- The backup scheme is set to **Always incremental (single-file)**
- The backup format is set to **Version 12**

Backups stored in the cloud and single-file backups (both version 11 and 12) are always consolidated because their inner structure makes this fast and easy.

## Backup file name

This option defines the names of the backup files created by the protection plan or by the cloud applications backup plan.

### Default backup file names

- Standard backups: `[Machine Name]-[Plan ID]-[Unique ID]A`
- Exchange/M365 mailbox backups (local agent): `[Mailbox ID]_mailbox_[Plan ID]A`
- Microsoft Azure backups: `[Mailbox ID]_` (prefix cannot be removed)
- Cloud application backups (cloud agents): `[Resource Name]_[Resource Type]_[Resource Id]_[Plan Id]A`

### Default name variables

- `[Machine Name]` -- name of the machine as shown in the console
- `[Plan ID]`, `[Plan Id]` -- unique identifier of the protection plan
- `[Unique ID]` -- unique identifier of the selected machine
- `[Mailbox ID]` -- mailbox user's principal name (UPN)
- `[Resource Name]` -- cloud data source name (UPN, SharePoint site URL, or Shared drive name)
- `[Resource Type]` -- cloud data source type (mailbox, O365PublicFolder, OneDrive, SharePoint, GDrive)
- `[Resource ID]` -- unique identifier of the cloud data source
- `[Plan name]` -- name of the protection plan
- `[Virtualization Server Type]` -- "vmwesx" or "mshyperv"
- "A" -- safeguard letter to prevent ending with a digit

### Backup format and backup files

| | Always incremental (single-file) | Other backup schemes |
|---|---|---|
| **Version 11** | One TIB file and one XML metadata file | Multiple TIB files and one XML metadata file |
| **Version 12** | One TIBX file per backup chain. If the file exceeds 200 GB in a local or network (SMB) folder, it is split into 200-GB files by default. |

### Limitations for backup file names

- A backup file name cannot end with a digit.
- A backup file name cannot contain: `()&?*$<>":|\/#`, line endings (`\n`), and tabs (`\t`).

> **Note:** If you move backup files (.tibx) from their original storage, do not rename them. Renamed files will appear corrupted.

## Backup format

The **Backup format** option defines the format of the backups created by the protection plan. This option is available only for protection plans that already use the version 11 backup format. You can change to version 12; after that, the option becomes unavailable.

- **Version 11** -- The legacy format, preserved for backward compatibility. You cannot back up Database Availability Groups (DAG) using version 11.
- **Version 12** -- Introduced in Acronis Backup 12 for faster backup and recovery. Each backup chain is saved to a single TIBX file.

### In-archive deduplication (TIBX)

The TIBX backup format of version 12 supports in-archive deduplication:
- Significantly reduced backup size with built-in block-level deduplication
- Efficient handling of hard links ensures no storage duplicates
- Hash-based chunking

In-archive deduplication is enabled by default for all backups in the TIBX format.
