# Recovering Mailbox Items 47005

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering Exchange mailboxes and mailbox items > Recovering mailbox items
Recovering mailbox items

To recover mailbox items from an application-aware backup or a database backup

[Only when recovering from a database backup to Microsoft 365] If Agent for Microsoft 365 is not installed on the machine running Exchange Server that was backed up, do one of the following:

If there is not Agent for Microsoft 365 in your organization, install Agent for Microsoft 365 on the machine that was backed up (or on another machine with the same Microsoft Exchange Server version).
If you already have Agent for Microsoft 365 in your organization, copy libraries from the machine that was backed up (or from another machine with the same Microsoft Exchange Server version) to the machine with Agent for Microsoft 365, as described in "Copying Microsoft Exchange libraries".

Do one of the following:

When recovering from an application-aware backup: under Devices, select the machine that originally contained the data that you want to recover.
When recovering from a database backup, click Devices > Microsoft Exchange > Databases, and then select the database that originally contained the data that you want to recover.
Click Recovery.

Select a recovery point. Note that recovery points are filtered by location.

If the machine is offline, the recovery points are not displayed. Use other ways to recover:

[Only when recovering from an application-aware backup] If the backup location is cloud or shared storage (i.e. other agents can access it), click Select machine, select an online machine that has Agent for Exchange or Agent for VMware, and then select a recovery point.
Select a recovery point on the Backup storage tab.

The machine chosen for browsing in either of the above actions will perform the recovery instead of the original machine that is offline.

Click Recover > Exchange mailboxes.
Click the mailbox that originally contained the items that you want to recover.

Select the items that you want to recover.

The following search options are available. Wildcards are not supported.

For email messages: search by subject, sender, recipient, and date.
For events: search by title and date.
For tasks: search by subject and date.
For contacts: search by name, email address, and phone number.

When an email message is selected, you can click Show content to view its contents, including attachments.

Click the name of an attached file to download it.

To be able to select folders, click the recover folders icon.

Click Recover.

To recover to Microsoft 365, select Microsoft 365 in Recover to.

To recover to an Exchange Server, keep the default Microsoft Exchange value in Recover to.

[Only when recovering to an Exchange Server] Click Target machine with Microsoft Exchange Server to select or change the target machine. This step allows recovery to a machine that is not running Agent for Exchange.

Specify the fully qualified domain name (FQDN) of a machine where the Client Access role (in Microsoft Exchange Server 2010/2013) or Mailbox role (in Microsoft Exchange Server 2016 or later) is enabled. The machine must belong to the same Active Directory forest as the machine that performs the recovery.

If prompted, provide the credentials of an account that will be used to access the machine. The requirements for this account are listed in Required user rights.

In Target mailbox, view, change, or specify the target mailbox.

By default, the original mailbox is selected. If this mailbox does not exist or a non-original target machine is selected, you must specify the target mailbox.

[Only when recovering email messages] In Target folder, view or change the target folder in the target mailbox. By default, the Recovered items folder is selected. Due to Microsoft Exchange limitations, events, tasks, notes, and contacts are restored to their original location regardless of any different Target folder specified.
Click Start recovery.

You can check the recovery progress in the Cyber Protect console, on the Activities tab.

To recover a mailbox item from a mailbox backup

Click Devices > Microsoft Exchange > Mailboxes.

Select the mailbox that originally contained the items that you want to recover, and then click Recovery.

You can search mailboxes by name. Wildcards are not supported.

If the mailbox was deleted, select it on the Backup storage tab, and then click Show backups.

Select a recovery point. Note that recovery points are filtered by location.
Click Recover > Email messages.

Select the items that you want to recover.

The following search options are available. Wildcards are not supported.

For email messages: search by subject, sender, recipient, and date.
For events: search by title and date.
For tasks: search by subject and date.
For contacts: search by name, email address, and phone number.

When an email message is selected, you can click Show content to view its contents, including attachments.

Click the name of an attached file to download it.

When an email message is selected, you can click Send as email to send the message to an email address. The message is sent from your administrator account's email address.

To be able to select folders, click the recover folders icon:

Click Recover.
Perform steps 9-13 of the above procedure.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.