# Selecting entire machine

Managing the backup and recovery of workloads and files > Selecting data to back up > Selecting entire machine
Selecting entire machine

A backup of an entire machine is a backup of all its non-removable disks. For more information about disk backup, refer to Selecting disks or volumes.

Limitations

Disk-level backups are not supported for encrypted APFS volumes that are locked. During a backup of an entire machine, such volumes are skipped.

You cannot recover the content of the OneDrive root folder from an Entire machine or Disk/volumes backup, even though the OneDrive folder is shown when browsing the backup archive in a file manager app, such as File Explorer. When browsing the archive in the Cyber Protect console, the OneDrive folder is not shown. When browsing the archive in the Web Restore console, the OneDrive folder is shown as a file but recovery from this backup is not possible.

To be able to recover the content of the OneDrive folder, create a Files/folders backup. Files that are not available on the device will be shown in the archive, but cannot be recovered.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.