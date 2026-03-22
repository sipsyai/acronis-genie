# Log truncation

Managing the backup and recovery of workloads and files > Backup options > Log truncation
Log truncation

This option is effective for backups of Microsoft SQL Server databases and for disk-level backups with enabled Microsoft SQL Server application backup.

The option defines whether the SQL Server transaction logs are truncated after a snapshot is taken in the beginning of the backup operation.

The preset is: Enabled.

When this option is enabled, a database can be recovered only to a point in time of a backup created by Cyber Protection.

Disable this option if you are backing up transaction logs by using the native backup engine of Microsoft SQL Server.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.