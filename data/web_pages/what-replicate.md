# What to replicate

Working with plans > Off-host data protection plans > Backup replication > What to replicate
What to replicate
Some replication operations, such as replicating a whole location or replicating all backups in a backup set, might be very time-consuming.

You can replicate individual backup sets or whole backup locations. When you replicate a backup location, all backup sets in it are replicated.

Backup sets consist of backups (also known as recovery points). You must select which backups to replicate.

The following options are available:

All backups

All backups in the backup set are replicated every time the replication plan runs.

Only full backups

Only the full backups in the backup set are replicated.

Only the last backup

Only the newest backup in the backup set is replicated, regardless of its type (full, differential, or incremental).

Select an option according to your needs and the backup scheme that you use. For example, if you use the Always incremental (single-file) backup scheme and you want to replicate only the newest incremental backup, in the backup replication plan, select Only last backup.

The following table summarizes which backups will be replicated with different backup schemes.

Always incremental (single-file)	Always full	Weekly full, Daily incremental	Monthly full, Weekly differential, Daily incremental (GFS)
All backups	All backups in the backup set	All backups in the backup set	All backups in the backup set	All backups in the backup set
Only full backups	Only the first backup, which is full	All backups	One backup every week*	One backup every month*
Only last backup	Only the newest backup in the backup set*	Only the newest backup in the backup set*	Only the newest in the backup set, regardless of its type*	Only the newest in the backup set, regardless of its type*

* When configuring the schedule of the backup replication plan, ensure that the last replicated backup will still be available in its original location when the backup replication starts. If this backup is not available in the original location, for example, because it was deleted by a retention rule, the whole archive will be replicated as a full backup. This might be very time-consuming and will use additional storage space.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.