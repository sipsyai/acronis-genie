---
title: "Continuous data protection (CDP)"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup"
page_range: "531-534"
tags: ["CDP", "continuous-data-protection", "real-time-backup", "file-tracking", "application-tracking", "NTFS"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#continuous-data-protection.html"
---

# Continuous data protection (CDP)

Continuous data protection (CDP) is part of the standard protection. It backs up critical data immediately after this data is changed, ensuring that no changes will be lost if your system fails between two scheduled backups. You can configure CDP for the following data:

- Files or folders in specific locations
- Files modified by specific applications

## Requirements and limitations

- Supported only for the NTFS file system
- Supported operating systems:
  - Desktop: Windows 7 and later
  - Server: Windows Server 2008 R2 and later
- Only local folders are supported. Network folders cannot be selected for Continuous data protection.
- Continuous data protection is not compatible with the **Application backup** option.
- Continuous data protection prevents the deletion of backup archives. If you want to manually delete a backup created with CDP enabled, you need to revoke or delete the corresponding protection plan first.

## How it works

Changes in the files and folders that are tracked by CDP are immediately saved to a special CDP backup. There is only one CDP backup in a backup set, and it is always the most recent one.

When a scheduled regular backup starts, Continuous data protection is put on hold because the latest data is to be included in the scheduled backup. When the scheduled backup finishes, Continuous data protection resumes, the old CDP backup is deleted, and a new CDP backup is created. Thus, the CDP backup always stays the most recent backup in the backup set and stores only the latest state of the tracked files or folders.

If your machine crashes during a regular backup, Continuous data protection resumes automatically after the machine restarts and creates a CDP backup on top of the last successful scheduled backup.

Continuous data protection requires that at least one regular backup is created before the CDP backup. When you run a protection plan with CDP for the first time, a full backup is created, and a CDP backup is immediately added on top of it.

> **Note:** Continuous Data protection is disabled by default in newly created protection plans. It is not compatible with the **Application backup** option and cannot be enabled for machines that have this option enabled.

## Supported data sources

You can configure CDP with the following data sources:
- Entire machine
- Disks/volumes
- Files/folders

## Supported destinations

- Local folder
- Network folder
- Cloud storage
- Acronis Cyber Infrastructure
- Location defined by a script

## Configuring a CDP backup

1. In the **Backup** module of a protection plan, enable the **Continuous data protection (CDP)** switch.
2. In **Items to protect continuously**, configure CDP for **Applications** or **Files/folders**, or both:
   - Click **Applications** to configure CDP backup for files modified by specific applications. You can select applications from predefined categories or add other applications by specifying the path to their executable file, for example:
     - `C:\Program Files\Microsoft Office\Office16\WINWORD.EXE`
     - `*:\Program Files (x86)\Microsoft Office\Office16\WINWORD.EXE`
   - Click **Files/folders** to configure CDP backup for files in specific locations. You can define these locations by using selection rules or by selecting files and folders directly.
     - For all machines: use the text box with full paths to files or paths with wildcard characters (`*` and `?`). The asterisk matches zero or more characters. The question mark matches a single character.
     - For online machines: in **Machine to browse from**, select the machine, then click **Select files and folders** to browse. Your direct selection creates a selection rule.

> **Important:** To create a CDP backup for a folder, you must specify its content by using the asterisk wildcard character. Correct path: `D:\Data\*`. Incorrect path: `D:\Data\`.

3. In the protection plan pane, click **Create**.

As a result, the data that you specified will be backed up continuously between the scheduled backups.
