# Multi-volume snapshot

Managing the backup and recovery of workloads and files > Backup options > Multi-volume snapshot
Multi-volume snapshot

This option is effective for backups of physical machines running Windows or Linux.

This option applies to disk-level backup. This option also applies to file-level backup when the file-level backup is performed by taking a snapshot. (The "File-level backup snapshot" option determines whether a snapshot is taken during file-level backup).

This option determines whether to take snapshots of multiple volumes at the same time or one by one.

The preset is:

If at least one machine running Windows is selected for backup: Enabled.
Otherwise: Disabled.

When this option is enabled, snapshots of all volumes being backed up are created simultaneously. Use this option to create a time-consistent backup of data spanning multiple volumes; for instance, for an Oracle database.

When this option is disabled, the volumes' snapshots are taken one after the other. As a result, if the data spans several volumes, the resulting backup may be not consistent.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.