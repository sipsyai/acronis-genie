---
title: "Backup options: Fast incremental, file filters, snapshots, and forensic data"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup options"
page_range: "579-590"
tags: ["fast-incremental", "file-filters", "inclusion", "exclusion", "wildcards", "file-level-snapshot", "forensic-data", "memory-dump", "digital-evidence", "notarization", "tibxread"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#backup-options.html"
---

# Fast incremental/differential backup

Preset: **Enabled**.

This option is effective for incremental and differential disk-level backup. It is not effective (always disabled) for volumes formatted with JFS, ReiserFS3, ReiserFS4, ReFS, or XFS file systems.

Incremental or differential backup captures only data changes. To speed up the backup process, the program determines whether a file has changed or not by the file size and the date/time when the file was last modified. Disabling this feature will make the program compare the entire file contents to those stored in the backup.

# File filters (Inclusions/Exclusions)

You can use file filters to include only specific files and folders in a backup, or to exclude specific files and folders from a backup.

File filters are available for entire machine backups, disk-level backups, and file-level backups unless stated otherwise.

**Not available** with: XFS, JFS, exFAT, and ReiserFS4 file systems.

**Not applicable** to dynamic disks (LVM or LDM volumes) of virtual machines backed up in agentless mode.

## File filter types

- **Inclusion filters** ("Include only the files that match the following criteria") -- If you specify `C:\File.exe` in an inclusion filter, only this file will be backed up even in an **Entire machine** backup.
  - Not supported for **Version 11** file-level backups that are not stored in the cloud storage.
- **Exclusion filters** ("Exclude the files that match the following criteria") -- If you specify `C:\File.exe` in an exclusion filter, this file will be skipped.
  - The exclusion filter takes precedence over the inclusion filter. If the same file appears in both filters, it will be skipped.

## File filter values

- **File or folder name** -- e.g., `Document.txt`. All files and folders with that name will be selected.
- **Full path to a file or folder** -- Starting with the drive letter (Windows) or the root directory (Linux/macOS). Forward slashes and backslashes are both accepted in Windows.

> **Important:** If the operating system of the backed-up machine is not detected correctly during a disk-level backup, file filters with full paths will not work. A filter that does not use the drive letter or root directory (e.g., `Temp\*` or `*C:\`) will not result in warning or failure but may not work either.

## Wildcards

- **Asterisk (*)** -- Represents zero or more characters. `Doc*.txt` matches `Doc.txt` and `Document.txt`.
- **Double asterisk (**)** -- Represents zero or more characters, including the slash character. `**/Docs/**/*.txt` matches all TXT files in all subfolders of all folders named Docs. Available only for Version 12 format backups.
- **Question mark (?)** -- Represents only one character. `Doc?.txt` matches `Doc1.txt` and `Docs.txt` but not `Doc.txt` or `Doc11.txt`.

> **Note:** Use the question mark wildcard if the file or folder name includes a comma or semicolon. The comma and semicolon are interpreted as delimiters. For example, use `MyCompany?Inc` to filter the folder `MyCompany,Inc`.

## Configuring file filters

1. In a protection plan, expand the **Backup** module.
2. In **Backup options**, click **Change**.
3. Select **File filters (Inclusions/Exclusions)**.
4. Configure one filter (inclusion or exclusion) or both. The exclusion filter takes precedence.
5. Click **Done**.
6. Save the protection plan.

# File-level backup snapshot

This option is effective only for file-level backup. Files stored on network shares are always backed up one by one.

Presets:
- If only machines running Linux are selected: **Do not create a snapshot.**
- Otherwise: **Create snapshot if it is possible.**

Options:
- **Create a snapshot if it is possible** -- Back up files directly if taking a snapshot is not possible.
- **Always create a snapshot** -- Enables backing up of all files, including files opened for exclusive access. The files will be backed up at the same point in time. If a snapshot cannot be taken, the backup will fail.
- **Do not create a snapshot** -- Always back up files directly. Trying to back up files opened for exclusive access will result in a read error. Files in the backup may be not time-consistent.

# Forensic data

Backups with forensic data allow investigators to analyze disk areas that are not usually included in a regular disk backup. By enabling the **Forensic data** backup option, you can collect:

- Snapshots of unused disk space
- Memory dumps
- Snapshots of running processes

Backups with forensic data are automatically notarized.

## Requirements

The **Forensic data** option is available for **Entire machine** backups of Windows workloads running:
- Windows 8.1 and later
- Windows Server 2012 R2 and later

**Not available** for:
- Workloads connected through VPN without direct Internet access
- Workloads with disks encrypted by BitLocker

**Supported backup locations:**
- Cloud storage
- Network folder
- Local folder (only on external hard drives connected via USB; local dynamic disks are not supported)

## Forensic backup process

1. A raw memory dump and a list of running processes is captured.
2. The backed-up workload restarts and the bootable media interface opens.
3. A backup that includes both the used and unallocated space is created.
4. The backed-up disks are notarized.
5. The operating system of the workload reboots, and other configured operations run (replication, retention, validation).

> **Important:** The memory dump may contain sensitive data, such as passwords.

## Retrieving forensic data

1. In the Cyber Protect console, go to **Backup storage**.
2. Select a backup location that supports backup archives with forensic data.
3. Select a backup archive that contains forensic data, click **Show backups**.
4. Select a backup (recovery point) with forensic data, and then click **Recover**.
5. To download or recover only forensic data files, click **Forensic data**:
   - To download files: Select one or more files and click **Download**.
   - To recover files: Select one or more files and click **Recover**.
6. To recover the whole backup, click **Entire machine** and configure recovery options.

> **Note:** You cannot download files bigger than 100 MB in the Cyber Protect console. The memory dump file (`raw.dmp`) is usually bigger. Recover it and then copy it. You can use the Volatility Framework (https://www.volatilityfoundation.org/) for further memory analysis.

> **Important:** To ensure that no changes are made to the disk during the booting process, the recovered machine is not bootable.

## Configuring collection of forensic data

1. Go to **Devices** > **All devices**.
2. Select a workload, click **Protect**.
3. Click **Add plan** > **Create plan** > **Protection**.
4. Ensure the **Backup** module is enabled and expanded.
5. In **What to back up**, select **Entire machine**.
6. In **Backup options**, click **Change** > **Forensic data** > enable **Collect forensic data** > click **Done**.
7. Configure backup location, schedule, and encryption password.
8. Click **Create**.

> **Note:** You cannot change the forensic data settings after you apply the protection plan. To use different settings, create a new protection plan.

## The tool "tibxread" for getting the backed-up data

Cyber Protection provides the `tibxread` tool for manual check of the backed-up disk integrity. It allows you to get data from a backup and calculate hash of the specified disk. The tool is installed automatically with Agent for Windows, Agent for Linux, and Agent for Mac.

Installation path: same folder as the agent (e.g., `C:\Program Files\BackupClient\BackupAndRecovery`).

Supported locations: local disk, network folder (CIFS/SMB) without credentials, cloud storage (requires URL, port, and certificate).
