# Volume Shadow Copy Service (VSS)

Managing the backup and recovery of workloads and files > Backup options > Volume Shadow Copy Service (VSS)
Volume Shadow Copy Service (VSS)

This option is applicable only to Windows operating systems.

It defines whether a backup can succeed if one or more Volume Shadow Copy Service (VSS) writers fail and which provider has to notify the VSS-aware applications that the backup will start.

Using the Volume Shadow Copy Service ensures the consistent state of all data used by the applications; in particular, completion of all database transactions at the moment of taking the data snapshot by the backup software. Data consistency, in turn, ensures that the application will be recovered in the correct state and become operational immediately after recovery.

The snapshot is used only during the backup operation, and is automatically deleted when the backup operation completes. No temporary files are kept.

You may also use Pre/Post data capture commands to ensure that the data is backed up in a consistent state. For instance, specify pre-data capture commands that will suspend the database and flush all caches to ensure that all transactions are completed, and then specify post-data capture commands that will resume the database operations after the snapshot is taken.

Files and folders that are specified in the HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\BackupRestore\FilesNotToSnapshot registry key are not backed up. In particular, offline Outlook Data Files (.ost) are not backed up because they are specified in the OutlookOST value of this key.

Ignore failed VSS writers

You can select one of the following:

Ignore failed VSS writers

With this option, you can achieve successful backups even when one or more VSS writers fail.

Application-aware backups will always fail if the application-specific writer fails. For example, if you are making application-aware backup of SQL Server data, and SqlServerWriter fails, the backup operation will also fail.

When this option is enabled, up to three consecutive attempts for a VSS snapshot will be made.

In the first attempt, all VSS writers are required. If this attempt fails, it will be repeated. If the second attempt also fails, the failed VSS writers will be excluded from the scope of the backup operation, and then a third attempt will be made. If the third attempt is successful, the backup will complete with a warning about the failed VSS writers. If the third attempt is not successful, the backup will fail.

Require successful processing for all VSS writers

If any of the VSS writers fails, the backup operation will also fail.

Select the snapshot provider

You can select one of the following:

Automatically select snapshot provider

Automatically select the hardware snapshot provider, a software snapshot provider, or the Microsoft Software Shadow Copy provider.

We recommend that you use automatic selection of a snapshot provider whenever possible.

Use Microsoft Software Shadow Copy provider

We recommend that you force the use of the Microsoft Software Shadow Copy provider if you have other third-party VSS providers that you do not want to use, and when the protected workload does not contain Cluster Shared volumes.

Force the use of Microsoft Software Shadow Copy provider only if you need to use it explicitly, because it may cause backups to fail in environments with Cluster Shared volumes and other volumes not supported by the Microsoft Software Shadow Copy provider.
Enable VSS full backup

If this option is enabled, the logs of Microsoft Exchange Server and of other VSS-aware applications (except for Microsoft SQL Server) will be truncated after each successful full, incremental or differential disk-level backup.

The preset is: Disabled.

Leave this option disabled in the following cases:

If you use Agent for Exchange or third-party software for backing up the Exchange Server data. This is because the log truncation will interfere with the consecutive transaction log backups.
If you use third-party software for backing up the SQL Server data. The reason for this is that the third-party software will take the resulting disk-level backup for its "own" full backup. As a result, the next differential backup of the SQL Server data will fail. The backups will continue failing until the third-party software creates the next "own" full backup.
If other VSS-aware applications are running on the machine and you need to keep their logs for any reason.
Enabling this option does not result in the truncation of Microsoft SQL Server logs. To truncate the SQL Server log after a backup, enable the Log truncation backup option.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.