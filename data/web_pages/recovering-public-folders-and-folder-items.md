# Recovering public folders and folder items

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Recovering public folders and folder items
Recovering public folders and folder items

In order to recover a public folder or public folder items, at least one administrator of the target Microsoft 365 organization must have the Owner's rights for the target public folder. If the recovery fails with an error about denied access, assign these rights in the target folder properties, select the target organization in the Cyber Protect console, click Refresh, and then repeat the recovery.

To recover a public folder or folder items

Click Microsoft 365.
If multiple Microsoft 365 organizations are added to the Cyber Protection service, expand the organization whose backed-up data you want to recover. Otherwise, skip this step.

Do one of the following:

Expand the Public folders node, select All public folders, select the public folder that you want to recover or that originally contained the items that you want to recover, and then click Recovery.
If the public folder was deleted, select it in the Cloud applications backups section of the Backup storage tab, and then click Show backups.

You can search public folders by name. Wildcards are not supported.

Select a recovery point.
Click Recover data.

Browse to the required folder or use search to obtain the list of the required items.

You can search email messages and posts by subject, sender, recipient, and date. Wildcards are not supported.

Select the items that you want to recover. To be able to select folders, click the "recover folders" icon:

Additionally, you can do any of the following:

When an email message or a post is selected, click Show content to view its contents, including attachments. Click the name of an attached file to download it.
When an email message or a post is selected, click Send as email to send the item to specified email addresses. You can select the sender and write a text to be added to the forwarded item.
Only if the backup is not encrypted, you used search, and selected a single item in the search results: click Show versions to select the item version to recover. You can select any backed-up version, earlier or later than the selected recovery point.
Click Recover.

If multiple Microsoft 365 organizations were added to the Cyber Protection service, click Microsoft 365 organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must specify the target organization.

In Recover to public folder, view, change, or specify the target public folder.

By default, the original folder is selected. If this folder does not exist or a non-original organization is selected, you must specify the target folder.

You cannot create a new public folder during recovery. To recover a public folder to a new one, first you need to create the target public folder in the desired Microsoft 365 organization, and then let the cloud agent synchronize the change. The cloud agent automatically synchronizes with Microsoft 365 every 24 hours. To synchronize the change immediately, in the Cyber Protect console, select the organization on the Microsoft 365 page, and then click Refresh.

In Path, view or change the target subfolder in the target public folder. By default, the original path will be recreated.
Click Start recovery.

Select one of the overwriting options:

Option	Description
Overwrite existing items	All existing files in the destination location are overwritten.
Do not overwrite existing items	If the destination location contains a file of the same name, that file is not overwritten and the source file is not saved to the destination location.
Click Proceed to confirm your decision.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.