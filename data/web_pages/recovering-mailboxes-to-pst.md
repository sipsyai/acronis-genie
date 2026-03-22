# Recovering entire mailboxes to PST data files

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Recovering entire mailboxes to PST data files
Recovering entire mailboxes to PST data files
You can recover emails or folders from the in-place archive as separate mailbox items by using the Recovery > Email messages option. For more information, see Recovering mailbox items. The in-place archive is not recovered when you use the Recovery > Entire mailbox or Recovery > As PST files options.

To recover mailbox

Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose backed-up data you want to recover. Otherwise, skip this step.

Do one of the following:

To recover a user mailbox to PST data file, expand the Users node, select All users, select the mailbox you want to recover, and then click Recovery.
To recover a shared mailbox to PST data file, expand the Users node, select All users, select the mailbox that you want to recover, and then click Recovery.
To recover a group mailbox to PST data file, expand the Groups node, select All groups, select the group whose mailbox you want to recover, and then click Recovery.

You can search users and groups by name. Wildcards are not supported.

If the user, group, or the shared Outlook data file was deleted, select the item in the Cloud applications backups section of the Backup storage tab, and then click Show backups.

Click Recover > As PST files.

Set the password to encrypt the archive with the PST files.

The password must contain at least one symbol.

Confirm the password and click Done.

The selected mailbox items will be recovered as PST data files and archived in ZIP format. The maximum size of one PST file is limited to 2 GB, so if the data you are recovering exceeds 2 GB, it will be split into several PST files. The ZIP archive will be protected with the password you set.

You will receive an email with a link to a ZIP archive containing the created PST files.

The administrator will receive an email notification that you have performed the recovery procedure.

Mailbox recovery to PST files can be time-consuming, as it involves not only data transfer, but also data transformation using complex algorithms.

To download the archive with PST files and complete recovery

Do one of the following:

To download the archive from the email, follow the Download files link.

The archive is available for 96 hours. To download the archive after the 96-hour period, repeat the recovery procedure.

To download the archive from the Cyber Protect console:

Go to Backup Storage > PST files.

Select the latest highlighted archive.

Click Download in the right pane.

The archive will be downloaded to the default download directory on your computer.

Extract the PST files from the archive using the password you set to encrypt the archive.

Open the PST files with Microsoft Outlook.

The resulting PST files could be much smaller in size that the original mailbox. That is normal.

Do not import these files to Microsoft Outlook by using the Import and Export Wizard.

Open the files by double-clicking them or right-clicking them and selecting Open with... > Microsoft Outlook in the context menu.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.