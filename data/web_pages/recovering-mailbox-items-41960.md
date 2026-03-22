# Recovering Mailbox Items 41960

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Recovering mailbox items
Recovering mailbox items
Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose backed-up data you want to recover. Otherwise, skip this step.

Do one of the following:

To recover items from a user mailbox, expand the Users node, select All users, select the user whose mailbox originally contained the items that you want to recover, and then click Recovery.
To recover items from a shared mailbox, expand the Users node, select All users, select the shared mailbox that originally contained the items that you want to recover, and then click Recovery.
To recover items from a group mailbox, expand the Groups node, select All groups, select the group whose mailbox originally contained the items that you want to recover, and then click Recovery.
If the user, group, or the shared mailbox was deleted, select the item in the Cloud applications backups section of the Backup storage tab, and then click Show backups.

You can search users and groups by name. Wildcards are not supported.

Select a recovery point.

To see only the recovery points that contain mailboxes, select Mailboxes in Filter by content.

Click Recover > Email messages.

Browse to the required folder or use search to obtain the list of the required items.

The following search options are available. Wildcards are not supported.

For email messages: search by subject, sender, recipient, attachment name, and date. You can select a start date or an end date (both inclusive), or both dates to search within a time range.
For events: search by title and date.
For tasks: search by subject and date.
For contacts: search by name, email address, and phone number.

Select the items that you want to recover. To be able to select folders, click the "recover folders" icon:

You cannot create a new target mailbox during recovery. To recover a new mailbox item to a new mailbox, first you need to create the target new mailbox item in Microsoft 365 organization, and then let the cloud agent synchronize the change. The cloud agent automatically synchronizes with Microsoft 365 every 24 hours. To synchronize the change immediately, in the Cyber Protect console, select the organization on the Microsoft 365 page, and then click Refresh.

Additionally, you can do any of the following:

When an item is selected, click Show content to view its contents, including attachments. Click the name of an attached file to download it.
When an email message or a calendar item is selected, click Send as email to send the item to the specified email addresses. You can select the sender and write a text to be added to the forwarded item.
Only if the backup is not encrypted, you used search, and selected a single item in the search results: click Show versions to select the item version to recover. You can select any backed-up version, earlier or later than the selected recovery point.
Click Recover.

If multiple Microsoft 365 organizations were added to the Cyber Protection service, click Microsoft 365 organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must specify the target organization.

In Recover to mailbox, view, change, or specify the target mailbox.

By default, the original mailbox is selected. If this mailbox does not exist or a non-original organization is selected, you must specify the target mailbox.

[Only when recovering to a user or a shared mailbox] In Path, view or change the target folder in the target mailbox. By default, the Recovered items folder is selected.

Group mailbox items are always recovered to the Inbox folder.

Click Start recovery.

Select one of the overwriting options:

Overwrite existing items
Do not overwrite existing items
Click Proceed to confirm your decision.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.