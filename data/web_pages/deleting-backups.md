# Deleting backups

Managing the backup and recovery of workloads and files > Operations with backups > Deleting backups
Deleting backups

A backup archive contains one or more backups. You can delete specific backups (recovery points) in an archive or the whole archive.

Deleting the backup archive deletes all backups in it. Deleting all backups of a workload deletes the backup archives that contain these backups.

Continuous data protection prevents the deletion of backup archives. If you want to manually delete a backup that is created with CDP enabled, you need to revoke or delete the corresponding protection plan first.

You can delete backups by using the Cyber Protect console – on the Devices tab and on the Backup storage tab. Also, you can delete backups from the cloud storage by using the Web Restore console.

If immutable storage is disabled, backed-up data is permanently deleted and cannot be recovered.

To delete backups or backup archives

On the Devices tab
On the Backup storage tab
In the Web Restore console

This procedure applies only to online workloads.

In the Cyber Protect console, go to Devices > All devices.
Select the workload backups of which you want to delete.
Click Recovery.
[If more than one backup location is available] Select the backup location.

[To delete all backups of the workload] Click Delete all.

Deleting all backups also deletes the backup archives that contain these backups.

[To delete a specific backup] Select the backup (recovery point) that you want to delete, and then click Actions > Delete.

[When deleting all backups] Select the check box, and then click Delete to confirm your decision.

[When deleting a specific backup] Click Delete to confirm your decision.

Deleting backups outside the Cyber Protect console

We recommend that you delete backups by using the Cyber Protect console. If you delete backups from the cloud storage by using the Web Restore console or delete local backups by using a file manager, you must refresh the backup location to sync the changes to the Cyber Protect console.

Prerequisite

An online agent that can access the backup location must be selected as Machine to browse from in the Cyber Protect console.

To refresh a backup location

In the Cyber Protect console, go to Backup storage.
Select the backup location in which the deleted backups were stored.

In the Actions pane, click Refresh.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.