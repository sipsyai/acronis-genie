# Recovering Mailboxes 41959

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Recovering mailboxes
Recovering mailboxes
Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose backed-up data you want to recover. Otherwise, skip this step.

Do one of the following:

To recover a user mailbox, expand the Users node, select All users, select the user whose mailbox you want to recover, and then click Recovery.
To recover a shared mailbox, expand the Users node, select All users, select the shared mailbox that you want to recover, and then click Recovery.
To recover a group mailbox, expand the Groups node, select All groups, select the group whose mailbox you want to recover, and then click Recovery.
If the user, group, or the shared mailbox was deleted, select the item in the Cloud applications backups section of the Backup storage tab, and then click Show backups.

You can search users and groups by name. Wildcards are not supported.

Select a recovery point.

To see only the recovery points that contain mailboxes, select Mailboxes in Filter by content.

Click Recover > Entire mailbox.

If multiple Microsoft 365 organizations are added to the Cyber Protection service, click Microsoft 365 organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must specify the target organization.

In Recover to mailbox, view, change, or specify the target mailbox.

By default, the original mailbox is selected. If this mailbox does not exist or a non-original organization is selected, you must specify the target mailbox.

You cannot create a new target mailbox during recovery. To recover a mailbox to a new one, first you need to create the target mailbox in the desired Microsoft 365 organization, and then let the cloud agent synchronize the change. The cloud agent automatically synchronizes with Microsoft 365 every 24 hours. To synchronize the change immediately, in the Cyber Protect console, select the organization on the Microsoft 365 page, and then click Refresh.

Click Start recovery.

Select one of the overwriting options:

Overwrite existing items
Do not overwrite existing items
Click Proceed to confirm your decision.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.