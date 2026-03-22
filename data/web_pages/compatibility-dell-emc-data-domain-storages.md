# Compatibility with Dell EMC Data Domain storages

Managing the backup and recovery of workloads and files > Supported operating systems and environments for backup and recovery > Compatibility with Dell EMC Data Domain storages
Compatibility with Dell EMC Data Domain storages

You can use Dell EMC Data Domain devices as backup storage.

With this storage, we recommend that you use a backup scheme that regularly creates full backups, for example Always full. To learn more about the available backup schemes, see Backup schemes.

Retention lock

Retention lock (Governance mode) is supported. If retention lock is enabled on the Data Domain storage, you must add the AR_RETENTION_LOCK_SUPPORT environment variable to the machine with the protection agent that uses this storage as a backup destination. For more information, see Adding the AR_RETENTION_LOCK_SUPPORT variable.

Dell EMC Data Domain storages with enabled retention lock are not supported by Agent for Mac.

If retention lock is enabled on the Data Domain storage, the backups on the storage will not be deleted by the retention rules in the protection plan. No error will be shown. The backups will be deleted when the retention lock expires and the retention rules are applied again.

Depending on the configuration of the protection plan, retention rules are applied to an archive before or after a backup.

Adding the AR_RETENTION_LOCK_SUPPORT variable

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.