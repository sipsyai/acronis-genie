# Recovering Mailboxes 43087

Managing the backup and recovery of workloads and files > Protecting Google Workspace data > Protecting Gmail data > Recovering mailboxes
Recovering mailboxes
Click Google Workspace.
If multiple Google Workspace organizations were added to the Cyber Protection service, select the organization whose backed-up data you want to recover. Otherwise, skip this step.

Expand the Users node, select All users, select the user whose mailbox you want to recover, and then click Recovery.

If the user was deleted, select the user in the Cloud applications backups section of the Backup storage tab, and then click Show backups.

You can search users and groups by name. Wildcards are not supported.

Select a recovery point.

To see only the recovery points that contain mailboxes, select Gmail in Filter by content.

Click Recover > Entire mailbox.

If multiple Google Workspace organizations are added to the Cyber Protection service, click Google Workspace organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must select a new target organization from the available registered organizations.

In Recover to mailbox, view, change, or specify the target mailbox.

By default, the original mailbox is selected. If this mailbox does not exist or a non-original organization is selected, you must specify the target mailbox.

You cannot create a new target mailbox during recovery. To recover a mailbox to a new one, first you need to create the target mailbox in the desired Google Workspace organization, and then let the cloud agent synchronize the change. The cloud agent automatically synchronizes with Google Workspace every 24 hours. To synchronize the change immediately, in the Cyber Protect console, select the organization on the Google Workspace page, and then click Refresh.

Click Start recovery.

Select one of the overwriting options:

Overwrite existing items
Do not overwrite existing items
Click Proceed to confirm your decision.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.