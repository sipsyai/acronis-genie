# Exporting backups

Managing the backup and recovery of workloads and files > Operations with backups > Exporting backups
Exporting backups

The export operation creates a self-sufficient copy of a backup in the location that you specify. The original backup remains untouched. Exporting backups allows you to separate a specific backup from a chain of incremental and differential backups for fast recovery, for writing onto removable or detachable media, or for other purposes.

In service-based billing mode, this feature requires the Servers quota to be enabled under Standard Protection as a prerequisite, but using the feature does not affect the quota usage.

With solution-based billing mode, this functionality is available in customer tenants that use Ultimate protection.

The result of an export operation is always a full backup. If you want to replicate the entire backup chain to a different location and preserve multiple recovery points, use a backup replication plan. For more information about this plan, refer to Backup replication.

The backup file name of the exported backup is the same as that of the original backup, except for the sequence number. If multiple backups from the same backup chain are exported to the same location, a four-digit sequence number is appended to the file names of all backups except for the first one.

The exported backup inherits the encryption settings and password from the original backup. When exporting an encrypted backup, you must specify the password.

To export a backup

Select the backed-up workload.
Click Recovery.

Select a recovery point. Note that recovery points are filtered by location.

If the workload is offline, the recovery points are not displayed. Do any of the following:

If the backup location is cloud or shared storage (that is, other agents can access it), click Select machine, select a target workload that is online, and then select a recovery point.
Select a recovery point on the Backup storage tab. For more information about the backups there, refer to Backup storage.
Click the gear icon, and then click Export.
Select the agent that will perform the export.
If the backup is encrypted, provide the encryption password. Otherwise, skip this step.
Specify the export destination.
Click Start.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.