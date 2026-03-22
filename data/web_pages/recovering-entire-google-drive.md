# Recovering an entire Google Drive

Managing the backup and recovery of workloads and files > Protecting Google Workspace data > Protecting Google Drive files > Recovering an entire Google Drive
Recovering an entire Google Drive
Click Google Workspace.
If multiple Google Workspace organizations were added to the Cyber Protection service, select the organization whose backed-up data you want to recover. Otherwise, skip this step.

Expand the Users node, select All users, select the user whose Google Drive you want to recover, and then click Recovery.

If the user was deleted, select the user in the Cloud applications backups section of the Backup storage tab, and then click Show backups.

You can search users by name. Wildcards are not supported.

Select a recovery point.

To see only the recovery points that contain Google Drive files, select Google Drive in Filter by content.

Click Recover > Entire Drive.

If multiple Google Workspace organizations were added to the Cyber Protection service, click Google Workspace organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must select a new target organization from the available registered organizations.

In Recover to drive, view, change, or specify the target user or the target Shared drive.

By default, the original user is selected. If this user does not exist or a non-original organization is selected, you must specify the target user or the target Shared drive.

If the backup contains shared files, the files will be recovered to the root folder of the target drive.

Select whether to recover the sharing permissions for the files.
Click Start recovery.

Select one of the overwriting options:

Option	Description
Overwrite an existing file if it is older	If there is a file with the same name in the destination location, and it is older than the source file, the source file will be saved in the destination location, replacing the older version.
Overwrite existing files	All existing files in the destination location are overwritten, regardless of their last modified date.
Do not overwrite existing files	If there is a file with the same name in the destination location, no changes are applied to it, and the source file is not saved to the destination location.
Click Proceed to confirm your decision.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.