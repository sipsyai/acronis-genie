# Replication

Managing the backup and recovery of workloads and files > Replication
Replication

With replication, each new backup is automatically copied to a replication location. The backups in the replication location do not depend on the backups in the source location, and vice versa.

Only the last backup in the source location is replicated. However, if earlier backups are not replicated (for example, due to a network connection problem), the replication operation will include all backups that are created after the last successful replication.

If a replication operation is interrupted, the processed data will be used by the next replication operation.

This topic describes replication as a part of a protection plan. You can also create a separate backup replication plan. For more information, see Backup replication.
Usage examples

Ensuring reliable recovery

Store your backups both on-site (for immediate recovery) and off-site (to guarantee that the backups stay safe even in case of storage failure or a natural disaster that affects the primary location).

Using the cloud storage to protect data from a natural disaster

Replicate the backups to the cloud storage by transferring only the data changes.

Keeping only the latest recovery points

Configure retention rules to delete the older backups from a fast storage, in order to save on storage costs.

Supported locations
Location	As source location	As replication location
Local folder

+



+


Network folder

+



+


Cloud storage

-*



+




Secure Zone



+



+


Public cloud	- *	+

*Replication from public cloud is available only in off-host data processing plans. See Supported locations for off-host data processing.

To enable replication

In a protection plan, expand the Backup module, and then click Add location.

The Add location option is not available when you select the cloud storage in Where to back up.

From the list of available locations, select the replication location.

The location appears in the protection plan as 2nd location, 3rd location, 4th location, or 5th location, depending on the number of locations you added for replication.

Click the gear icon to configure the options for the replication location.

Performance and backup window – set the backup window for the selected location, as described in Performance and backup window. These settings define the replication performance.
Remove location – delete the currently selected replication location.

[Only for the cloud storage] Physical Data Shipping – save the initial backup on a removable storage device and ship it for upload to the cloud storage, instead of replicating it over the Internet.

This option is suitable for locations with slow network connection or when you want to save bandwidth on big file transfers over the network. Enabling the option does not require advanced Cyber Protect service quotas, but you will need a Physical Data Shipping service quota to create a shipping order and track it. See Physical Data Shipping.

This option is supported with protection agent version from release C21.06 or later.

In the How many to keep row under the replication location, configure the retention rules for that location, as described in Retention rules.

Repeat steps 1 – 4 to add more replication locations.

You can configure up to four replication locations (2nd location, 3rd location, 4th location, and 5th location). If you select Cloud storage, you cannot add more replication locations.

If you enable backup and replication in the same protection plan, ensure that the replication completes before the next scheduled backup. If the replication is still in progress, the scheduled backup will not start―for example, a scheduled backup that runs once every 24 hours will not start if the replication takes 26 hours to complete.

To avoid the this dependency, use a separate plan for backup replication. For more information about this specific plan, see Backup replication.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.