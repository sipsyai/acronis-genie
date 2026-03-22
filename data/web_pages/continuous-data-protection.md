# Continuous data protection (CDP)

Managing the backup and recovery of workloads and files > Continuous data protection (CDP)
Continuous data protection (CDP)

Continuous data protection (CDP) is part of the standard protection. It backs up critical data immediately after this data is changed, ensuring that no changes will be lost if your system fails between two scheduled backups. You can configure CDP for the following data:

Files or folders in specific locations

Files modified by specific applications

Continuous data protection is supported only for the NTFS file system and the following operating systems:

Desktop: Windows 7 and later
Server: Windows Server 2008 R2 and later

Only local folders are supported. Network folders cannot be selected for Continuous data protection.

Continuous data protection is not compatible with the Application backup option.
Continuous data protection prevents the deletion of backup archives. If you want to manually delete a backup that is created with CDP enabled, you need to revoke or delete the corresponding protection plan first.
How it works

Changes in the files and folders that are tracked by Continuous data protection are immediately saved to a special CDP backup. There is only one CDP backup in a backup set, and it is always the most recent one.

When a scheduled regular backup starts, Continuous data protection is put on hold because the latest data is to be included in the scheduled backup. When the scheduled backup finishes, Continuous data protection resumes, the old CDP backup is deleted, and a new CDP backup is created. Thus, the CDP backup always stays the most recent backup in the backup set and stores only the latest state of the tracked files or folders.

If your machine crashes during a regular backup, Continuous data protection resumes automatically after the machine restarts and creates a CDP backup on top of the last successful scheduled backup.

Continuous data protection requires that at least one regular backup is created before the CDP backup. That is why, when you run a protection plan with Continuous data protection for the first time, a full backup is created, and a CDP backup is immediately added on top of it. If you enable the Continuous data protection option for an existing protection plan, the CDP backup is added to the existing backup set.

Continuous Data protection is disabled by default in newly created protection plans. It is not compatible with the Application backup option and cannot be enabled for machines that have this option enabled.
Supported data sources

You can configure Continuous data protection with the following data sources:

Entire machine

Disks/volumes

Files/folders

After selecting the data source in What to backup section in the protection plan, in the Items to protect continuously section, select the files, folders, or applications for Continuous data protection. For more information on how to configure Continuous data protection, refer to Configuring a CDP backup.

Supported destinations

You can configure Continuous data protection with the following destinations:

Local folder
Network folder
Cloud storage
Acronis Cyber Infrastructure

Location defined by a script

You can define by a script only the locations listed above.

Configuring a CDP backup

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.