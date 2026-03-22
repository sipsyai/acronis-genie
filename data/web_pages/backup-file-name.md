# Backup file name

Managing the backup and recovery of workloads and files > Backup options > Backup file name
Backup file name

This option defines the names of the backup files that are created by the protection plan or by the cloud applications backup plan.

For backup files that are created by protection plans, you can see these names in a file manager when you browse the backup location.

What is a backup file?

Each protection plan creates one or more files in the backup location, depending on which backup scheme and which backup format is used. The following table lists the files that can be created per machine or mailbox.

Always incremental (single-file)	Other backup schemes


Version 11 backup format



One TIB file and one XML metadata file



Multiple TIB files and one XML metadata file




Version 12 backup format



One TIBX file per backup chain (a full or differential backup, and all incremental backups that depend on it). If the size of a file stored in a local or network (SMB) folder exceeds 200 GB, the file is split to 200-GB files by default.

All files have the same name, with or without the addition of a timestamp or a sequence number. You can define this name (referred to as the backup file name) when you create or edit a protection plan or a cloud applications backup plan.

Timestamp is added to the backup file name only in the version 11 backup format.

If you change a backup file name in a protection plan or a cloud applications backup plan, the next backup will be a full backup.

If you specify a file name of an existing backup of the same machine, a full, incremental, or differential backup will be created according to the plan schedule.

If you move backup files (.tibx) from their original storage, do not rename them. Renamed files will appear corrupted and you will not be able to recover data from them.

It is possible to set backup file names for locations that cannot be browsed by a file manager (such as the cloud storage). In this case, you will see the custom names on the Backup storage tab.

Where can I see backup file names?

For protection plans, on the Backup storage tab, select the location, and then select the backup archive.

The default backup file name is shown on the Details panel.
If you set a non-default backup file name, it will be shown directly on the Backup storage tab, in the Name column.

For cloud applications backup plans, on the Backup storage tab, select the location, select the backup archive, and then click the gear icon.

Limitations for backup file names

A backup file name cannot end with a digit.

In the default backup file name, to prevent the name from ending with a digit, the letter "A" is appended. When creating a custom name, always make sure that it does not end with a digit. When using variables, the name must not end with a variable, because a variable might end with a digit.

A backup file name cannot contain the following symbols: ()&?*$<>":\|/#, line endings (\n), and tabs (\t).

Choose user-friendly backup file names. This will help you to easily distinguish backups when browsing the backup location with a file manager.

Default backup file name

The default backup file name for backups of entire physical and virtual machines, disks/volumes, files/folders, Microsoft SQL Server databases, Microsoft Exchange Server databases, and ESXi configuration is [Machine Name]-[Plan ID]-[Unique ID]A.

The default name for Exchange mailbox backups and Microsoft 365 mailbox backups created by a local Agent for Microsoft 365 is [Mailbox ID]_mailbox_[Plan ID]A.

The default name for Microsoft Azure backups is prefixed with [Mailbox ID]_. This prefix cannot be removed.

The default name for cloud application backups created by cloud agents is [Resource Name]_[Resource Type]_[Resource Id]_[Plan Id]A.

The default name consists of the following variables:

[Machine Name] This variable is replaced with the name of the machine (the same name that is shown in the Cyber Protect console).
[Plan ID], [Plan Id] These variables are replaced with the unique identifier of the protection plan. This value does not change if the plan is renamed.
[Unique ID] This variable is replaced with the unique identifier of the selected machine. This value does not change if the machine is renamed.
[Mailbox ID] This variable is replaced with the mailbox user's principal name (UPN).
[Resource Name] This variable is replaced with the cloud data source name, such as the user's principal name (UPN), SharePoint site URL, or Shared drive name.
[Resource Type] This variable is replaced with the cloud data source type, such as mailbox, O365Mailbox, O365PublicFolder, OneDrive, SharePoint, GDrive.
[Resource ID] This variable is replaced with the unique identifier of the cloud data source. This value does not change if the cloud data source is renamed.
"A" is a safeguard letter that is appended to prevent the name from ending with a digit.

The diagram below shows the default backup file name.

The diagram below shows the default backup file name for Microsoft 365 mailbox backups performed by a local agent.

Names without variables

If you change the backup file name to MyBackup, the backup files will look like the following examples. Both examples assume daily incremental backups scheduled at 14:40, starting from September 13, 2016.

For the version 12 format with the Always incremental (single-file) backup scheme:

MyBackup.tibx

For the version 12 format with other backup schemes:

MyBackup.tibx
MyBackup-0001.tibx
MyBackup-0002.tibx
...
Using variables

Besides the variables that are used by default, you can use the following variables:

The [Plan name] variable, which is replaced with the name of the protection plan.
The [Virtualization Server Type] variable, which is replaced with "vmwesx" if virtual machines are backed up by Agent for VMware or with "mshyperv" if virtual machines are backed up by Agent for Hyper-V.

If multiple machines or mailboxes are selected for backup, the backup file name must contain the [Machine Name], the [Unique ID], the [Mailbox ID], the [Resource Name], or the [Resource Id] variable.

Creating backups in an existing backup archive

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.