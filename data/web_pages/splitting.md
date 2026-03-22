# Splitting

Managing the backup and recovery of workloads and files > Backup options > Splitting
Splitting

While creating a protection plan, you can select the method of splitting large backups into smaller files.

Splitting is not available in protection plans that use the cloud storage as a primary or secondary backup location.

The default is:

If the backup location is a local or network (SMB) folder, and the backup format is TIBX (a.k.a. Version 12): Fixed size - 200 GB

This setting allows the backup software to work with large volumes of data on NTFS file systems, without negative effects caused by file fragmentation.

Otherwise: Automatic

The following settings are available:

Automatic

A backup will be split if it exceeds the maximum file size supported by the file system.

Fixed size

Enter the desired file size or select it from the dropdown, and save the plan.

Changing the splitting option in a backup plan does not affect already created archives.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.