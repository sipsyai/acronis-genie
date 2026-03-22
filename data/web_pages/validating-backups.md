# Validating backups

Managing the backup and recovery of workloads and files > Operations with backups > Validating backups
Validating backups

You can validate a backup to verify that you can recover the data. For more information about this operation, refer to Validation.

In service-based billing mode, this feature requires the Servers quota to be enabled under Standard Protection as a prerequisite, but using the feature does not affect the quota usage.

With solution-based billing mode, this functionality is available in customer tenants that use Ultimate protection.

To validate a backup

Select the backed-up workload.
Click Recovery.

Select a recovery point. Note that recovery points are filtered by location.

If the workload is offline, the recovery points are not displayed. Do any of the following:

If the backup location is cloud or shared storage (that is, other agents can access it), click Select machine, select a target workload that is online, and then select a recovery point.
Select a recovery point on the Backup storage tab. For more information about the backups there, refer to Backup storage.
Click the gear icon, and then click Validate.
Select the agent that will perform the validation.
Select the validation method.
If the backup is encrypted, provide the encryption password.
Click Start.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.