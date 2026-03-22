# Importing emails from PST files

Managing the backup and recovery of workloads and files > Email archiving > Importing emails from PST files
Importing emails from PST files

You can use PST files to import emails into an email archive.

During the import, the emails in the PST file are enumerated, and statistical data about their recipients is collected. The most frequent recipients become mailbox owners, for whom a new mailbox is created under All mailboxes > Imported from PST in the Cyber Protect console. Imported emails are grouped by import time and mailbox owner. Emails that cannot be associated with a mailbox owner and emails that have missing or corrupted "From" or "To" fields, appear under Imported from PST > Other.

Imported emails are not added to the mailboxes that are being archived. A mailbox that is being archived appears under All mailboxes. Imported emails are shown in separate mailboxes under All mailboxes > Imported from PST.
Limitations

In one importing task, you can select PST files from a single personal OneDrive account.

Importing from a SharePoint or Group OneDrive account is not supported.

Import time depends on the download speed allowed by OneDrive and might vary significantly across different locations and times of the day.

You can select up to 100,000 PST files or a folder that contains PST files.

The selected folder can contain up to 10,000 subfolders and up to 100,000 PST files.

The maximum allowed size per PST file is 50 GB.

If you select a folder, PST files larger than 50 GB will be skipped.

Only emails that are up to 200 MB are imported.

Larger emails, tasks, notes, invitations, and other items are skipped.

Unicode PST files are fully supported. ANSI PST files might not be processed or might be processed incorrectly.

Deduplication is not supported.

If you use the same PST file twice, the imported emails will be duplicated.

Rich text formatting (RTF) cannot be preserved in the body of an imported email.

A plain text or html body of an RTF email is preserved. The RFT body is attached to the imported email as a separate body.rtf file.

OLE inline attachments are imported as image attachments with automatically assigned names and without file extensions.
No PST password is required when importing password-protected PST files that are created in Microsoft Outlook.
Emails that are imported from PST files can be recovered only to new targets.

Prerequisites

You have exported the required emails from the source email solution. For example, you might export them as part of a migration from another email archiving system.
You have uploaded all exported PST files to the OneDrive account of a user in your Microsoft 365 organization. For example, you can use the account of the administrator who will perform the import.

To import emails from PST files

Log in to the Cyber Protect console as administrator.
Go to Backup storage > Cloud applications backups, and then select the email archive into which you want to import emails.
Click Import from PST files.

Specify the encryption password for the email archive, and then click Proceed.

In Organization, select the source Microsoft 365 organization.

If a single Microsoft 365 organization is added to Cyber Protect console, this organization is preselected. You can use this organization as a source, or add a new one.

[If multiple Microsoft 365 organizations are added to Cyber Protect console] Do the following:

Click Select, and then select the source Microsoft 365 organization.
Click Select.

[If no Microsoft 365 organization is added to Cyber Protect console] Do the following:

Click Select, and then click Add organization.

On the Microsoft 365 login page, sign in with the Microsoft 365 global administrator credentials.

Microsoft 365 displays a list of permissions that are necessary to back up and recover your organization's data.

Confirm that you grant the required permissions.

In What to import, select one or more PST files, or folders that contain PST files.

Click Select.

On the Microsoft 365 login page, sign in with the global administrator credentials for the source Microsoft 365 organization.

Microsoft 365 requires the following additional permissions:

Read files in all site collections
Read all users' full profiles
Read all files that user can access
Sign in and read user profile

Confirm that you grant the required permissions.

In the Cyber Protect console, navigate to a user's OneDrive, and then select one or more PST files.

Click Select.

Click Import.

After the import operation completes, check its result.

After a successful import, imported emails are shown under All mailboxes > Imported from PST.

After an unsuccessful import, no imported emails are shown. A failed import will not resume or restart automatically.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.