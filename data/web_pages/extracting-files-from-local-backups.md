# Extracting files from local backups

Managing the backup and recovery of workloads and files > Recovery > Recovering files > Extracting files from local backups
Extracting files from local backups

You can browse the contents of backups and extract files that you need.

Requirements
This functionality is available only in Windows by using File Explorer.
The backed-up file system must be one of the following: FAT16, FAT32, NTFS, ReFS, Ext2, Ext3, Ext4, XFS, or HFS+.
Prerequisites
A protection agent must be installed on the machine from which you browse a backup.
The backup must be stored in a local folder or on a network share (SMB/CIFS).

To extract files from a backup

Browse to the backup location by using File Explorer.

Double-click the backup file. The file names are based on the following template:

<machine name> - <protection plan GUID>

If the backup is encrypted, enter the encryption password. Otherwise, skip this step.

File Explorer displays the recovery points.

Double-click the recovery point.

File Explorer displays the backed-up data.

Browse to the required folder.
Copy the required files to any folder on the file system.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.