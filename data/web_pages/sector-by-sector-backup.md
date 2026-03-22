# Sector-by-sector backup

Managing the backup and recovery of workloads and files > Backup options > Sector-by-sector backup
Sector-by-sector backup

The option is effective only for disk-level backup.

This option defines whether an exact copy of a disk or volume on a physical level is created.

The preset is: Disabled.

If this option is enabled, all disk or volume's sectors will be backed up, including unallocated space and those sectors that are free of data. The resulting backup will be equal in size to the disk being backed up (if the "Compression level" option is set to None). The software automatically switches to the sector-by-sector mode when backing up drives with unrecognized or unsupported file systems.

It will be impossible to perform a recovery of application data from the backups which were created in the sector-by-sector mode.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.