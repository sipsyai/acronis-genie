# Changed block tracking (CBT)

Managing the backup and recovery of workloads and files > Backup options > Changed block tracking (CBT)
Changed block tracking (CBT)

This option is effective for the following backups:

Disk-level backups of virtual machines

Disk-level backups of physical machines running Windows

Backups of Microsoft SQL Server databases

Backups of Microsoft Exchange Server databases

The preset is: Enabled.

This option determines whether to use Changed Block Tracking (CBT) when performing an incremental or differential backup.

The CBT technology accelerates the backup process. Changes to the disk or database content are continuously tracked at the block level. When a backup starts, the changes can be immediately saved to the backup.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.