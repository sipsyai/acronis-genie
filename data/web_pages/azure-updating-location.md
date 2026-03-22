# Viewing and updating public cloud backup locations

Managing the backup and recovery of workloads and files > Backing up workloads to public clouds > Viewing and updating public cloud backup locations
Viewing and updating public cloud backup locations

You can view and update the Microsoft Azure, Amazon S3, and S3-compatible cloud backup locations that you defined in the Backup storage module, or when creating or editing a protection plan.

For information about removing access to a Microsoft Azure subscription from the Cyber Protect console, see Removing access to a Microsoft Azure subscription. For information about removing access to other public cloud connections, see Managing access to other public cloud storage services.

You cannot manually refresh or delete a public cloud backup location in the Backup storage module. The contents of the backup location are updated automatically after each backup or recovery operation.

To view public cloud backup locations

In the Cyber Protect console, go to Backup storage.

A list of backup locations is displayed, with details of the storage capacity and number of backups assigned to each location.

For more information about working with the listed backup locations, see Backup storage.

Select the relevant location.

Any current backups for the selected location are listed.

(Optional) Click on a backup to view more details for the backup.

To update a public cloud backup location in a protection plan

Go to the relevant protection plan, and select Edit.
Click the link in the Where to back up row.

Select from the list of existing backup locations, or click Add location to add a new location.

If the relevant Microsoft Azure subscription or public cloud connection is already registered in the Cyber Protect console, select it from the displayed list.

If you are adding a new Microsoft Azure subscription, you will be prompted to authenticate your Microsoft account details (see Adding access to a Microsoft Azure subscription). For more information about the required permissions when connecting to Microsoft Azure, see article Microsoft Azure connection security and audit (72684).

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.