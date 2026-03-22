# Fast incremental/differential backup

Managing the backup and recovery of workloads and files > Backup options > Fast incremental/differential backup
Fast incremental/differential backup

This option is effective for incremental and differential disk-level backup.

This option is not effective (always disabled) for volumes formatted with the JFS, ReiserFS3, ReiserFS4, ReFS, or XFS file systems.

The preset is: Enabled.

Incremental or differential backup captures only data changes. To speed up the backup process, the program determines whether a file has changed or not by the file size and the date/time when the file was last modified. Disabling this feature will make the program compare the entire file contents to those stored in the backup.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.