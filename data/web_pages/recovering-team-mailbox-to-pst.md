# Recovering team mailbox items to PST files

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Recovering team mailbox items to PST files
Recovering team mailbox items to PST files

To recover team mailbox items

Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose backed-up data you want to recover. Otherwise, skip this step.

You can search users and groups by name. Wildcards are not supported.

Expand the Teams node, select All teams, select a team whose mailbox originally contained the items that you want to recover, and then click Recovery.
Click Recover > Email messages.

Browse to the required folder or use search to obtain the list of the required items.

The following search options are available. Wildcards are not supported.

For email messages: search by subject, sender, recipient, attachment name, and date.
For events: search by title and date.
For tasks: search by subject and date.
For contacts: search by name, email address, and phone number.

Select the items that you want to recover. To be able to select folders, click the "recover folders" icon:

Additionally, you can do any of the following:

When an item is selected, click Show content to view its contents, including attachments. Click the name of an attached file to download it.
When an email message or a calendar item is selected, click Send as email to send the item to the specified email addresses. You can select the sender and write a text to be added to the forwarded item.
When the backup is not encrypted, you used search, and selected a single item from the search results: click Show versions to view the item version. You can select any backed-up version, no matter if it is earlier or later than the selected recovery point.
Click Recover as PST files.

Set the password to encrypt the archive with the PST files.

The password should contain at least one symbol.

Confirm the password and click DONE.

The selected mailbox items will be recovered as PST data files and archived in ZIP format. The maximum size of one PST file is limited to 2 GB, so if the data you are recovering exceeds 2 GB, it will be split into several PST files. The ZIP archive will be protected with the password you set.

You will receive an email with a link to a ZIP archive containing the created PST files.

The administrator will receive an email notification that you have performed the recovery procedure.

To download the archive with PST files and complete recovery

Do one of the following:

To download the archive from the email, follow the Download files link.
The archive is available for download within 24 hours. If the link expires, repeat the recovery procedure.

To download the archive from the Cyber Protect console:

Go to Backup Storage > PST files.

Select the latest highlighted archive.

Click Download in the right pane.

The archive will be downloaded to the default download directory on your computer.

Extract the PST files from the archive using the password you set to encrypt the archive.
In Microsoft Outlook open or import the PST files. To learn how to do it, refer to Microsoft documentation.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.