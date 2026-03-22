# Backup types

Managing the backup and recovery of workloads and files > Backup schedule > Backup types
Backup types

The following backup types are available:

Full—a full backup contains all source data. This backup is self-sufficient. To recover data, you do not need access to any other backups.

The first backup created by any protection plan is a full backup.

Incremental—an incremental backup stores changes to the data since the latest backup, regardless of whether the latest backup is full, differential, or incremental. To recover data, you need the whole chain of backups on which the incremental backup depends, back to the initial full backup.

Differential—a differential backup stores changes to the data since the latest full backup. To recover data, you need both the differential backup and the corresponding full backup on which the differential backup depends.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.