# Recovering OneDrive files

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Recovering OneDrive files
Recovering OneDrive files
Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose backed-up data you want to recover. Otherwise, skip this step.

Expand the Users node, select All users, select the user whose OneDrive files you want to recover, and then click Recovery.

If the user was deleted, select the user in the Cloud Applications Backups section of the Backup storage tab, and then click Show backups.

You can search users by name. Wildcards are not supported.

Select a recovery point.

To see only the recovery points that contain OneDrive files, select OneDrive in Filter by content.

Click Recover > Files/folders.

Browse to the required folder or use search to obtain the list of the required files and folders.

Select the files that you want to recover.

If the backup is not encrypted and you selected a single file, you can click Show versions to select the file version to recover. You can select any backed-up version, earlier or later than the selected recovery point.

If you want to download a file, select the file, click Download, select the location to save the file to, and then click Save. Otherwise, skip this step.
Click Recover.

If multiple Microsoft 365 organizations were added to the Cyber Protection service, click Microsoft 365 organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must specify the target organization.

You cannot create a new OneDrive during recovery. To recover a file to a new OneDrive, first you need to create the target OneDrive in the desired Microsoft 365 organization, and then let the cloud agent synchronize the change. The cloud agent automatically synchronizes with Microsoft 365 every 24 hours. To synchronize the change immediately, in the Cyber Protect console, select the organization on the Microsoft 365 page, and then click Refresh.

In Recover to drive, view, change, or specify the target user.

By default, the original user is selected. If this user does not exist or a non-original organization is selected, you must specify the target user.

In Path, view or change the target folder in the target user's OneDrive. By default, the original location is selected.
Select whether to recover the sharing permissions for the files.
Click Start recovery.

Select one of the file overwriting options:

Option	Description
Overwrite an existing file if it is older	If there is a file with the same name in the destination location, and it is older than the source file, the source file will be saved in the destination location, replacing the older version.
Overwrite existing files	All existing files in the destination location are overwritten, regardless of their last modified date.
Do not overwrite existing files	If there is a file with the same name in the destination location, no changes are applied to it, and the source file is not saved to the destination location.

When you recover OneNote notebooks, both Overwrite an existing file if it is older and Overwrite existing files will result in overwriting the exiting OneNote notebooks.

Click Proceed to confirm your decision.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.