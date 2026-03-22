# Recovering backed-up items

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Direct Backup to Microsoft 365 Backup Storage > Recovering backed-up items
Recovering backed-up items

You can recover entire Exchange mailboxes, OneDrive accounts, and SharePoint sites to their original locations. You can recover only one mailbox, OneDrive account, or SharePoint site at a time. To recover multiple items, repeat the recovery procedure for each item.

To recover backed-up items from Devices

Exchange mailbox
OneDrive account
SharePoint site
In the Cyber Protect console, go to Devices > Direct Backup for Microsoft 365.
[If multiple Microsoft 365 organizations are added] Select a Microsoft 365 organization.
Expand the Users node, and then select All users.

Select a user account, and then click Recovery.

You can select only one user account at a time.
[If both the mailbox and OneDrive account are backed up] In Filter by content, select Microsoft 365 mailboxes.
Select a backup (recovery point), and then click Recover entire mailbox.
Click Start recovery.

As a result, the items that are changed or deleted from the mailbox are replaced by the backed-up items. New items and unchanged items are not overwritten. You cannot change the overwrite settings because they depend on the Microsoft integration. For more information, see Restore data in Microsoft 365 Backup in the Microsoft documentation.

To recover backed-up items from Backup storage

In the Cyber Protect console, go to Backup storage, and then select Microsoft 365 Backup storage.
Select a backup archive, and then click Show backups.

Select a backup (recovery point), and then click Recover entire SharePoint site, Recover entire OneDrive, or Recover entire mailbox.

The name of the button depends on the type of data that is backed up.

Click Start recovery.

When recovering mailboxes, the items that are changed or deleted are replaced by the backed-up items. New items and unchanged items are not overwritten. When recovering OneDrive accounts and SharePoint sites, the backup overwrites the existing files completely. Any changes that are not included in the backup are lost.

You cannot change the overwrite settings because they depend on the Microsoft integration. For more information, see Restore data in Microsoft 365 Backup in the Microsoft documentation.


Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.