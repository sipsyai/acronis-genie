# Creating and applying a new backup plan

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Direct Backup to Microsoft 365 Backup Storage > Creating and applying a new backup plan
Creating and applying a new backup plan

You can create a backup plan on the Devices tab or on the Management > Cloud applications backup tab.

You can have only one backup plan per type of data (Exchange mailboxes, OneDrive accounts, or SharePoint sites) in a customer tenant.

To create and apply a backup plan

Devices
Management > Cloud applications backup
In the Cyber Protect console, go to Devices > Direct Backup for Microsoft 365.
[If multiple Microsoft 365 organizations are added] Select a Microsoft 365 organization.

Select the items that you want to back up.

You can select Exchange mailboxes, OneDrive, and SharePoint sites.

[To back up the mailboxes or OneDrive accounts of all users, including mailboxes and OneDrive accounts that will be created in the future] Expand the Users node, select All users, and then click Group backup.
[To back up individual mailboxes or OneDrive accounts] Expand the Users node, select All users, select user accounts, and then click Backup.
[To back up all modern team sites, including sites that will be created in the future] Expand the Groups node, select All groups, and then click Group backup.
[To back up individual modern team sites] Expand the Groups node, select All groups, select sites, and then click Backup.
[To back up all classic communication sites, including sites that will be created in the future] Expand the Site collections node, select All site collections, and then click Group backup.

[To back up individual classic communication sites] Expand the Site collections node, select All site collections, select sites, and then click Backup.

To create a backup plan, click Create new.

This option is available only if there is no existing plan for the selected type of data. If there is an existing plan, you can only apply that plan. For more information, see Applying a backup plan.

[If more than one type of data is available] In the backup plan, click What to back up, and then select Microsoft 365 mailboxes or OneDrive.

Click Apply.

Applying a backup plan might take up to 45 minutes, due to the processing time that is required on the Microsoft 365 Backup Storage side.

As a result, the backup plan is created and applied to the selected workloads. The backups will run automatically every 10 minutes. With Direct Backup to Microsoft 365 Backup Storage, you cannot run a backup plan manually.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.