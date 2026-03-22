# File-level backup snapshot

Managing the backup and recovery of workloads and files > Backup options > File-level backup snapshot
File-level backup snapshot

This option is effective only for file-level backup.

This option defines whether to back up files one by one or by taking an instant data snapshot.

Files that are stored on network shares are always backed up one by one.

The preset is:

If only machines running Linux are selected for backup: Do not create a snapshot.
Otherwise: Create snapshot if it is possible.

You can select one of the following:

Create a snapshot if it is possible

Back up files directly if taking a snapshot is not possible.

Always create a snapshot

The snapshot enables backing up of all files including files opened for exclusive access. The files will be backed up at the same point in time. Choose this setting only if these factors are critical, that is, backing up files without a snapshot does not make sense. If a snapshot cannot be taken, the backup will fail.

Do not create a snapshot

Always back up files directly. Trying to back up files that are opened for exclusive access will result in a read error. Files in the backup may be not time-consistent.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.