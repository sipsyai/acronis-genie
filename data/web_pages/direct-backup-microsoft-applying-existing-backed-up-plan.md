# Applying a backup plan

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Direct Backup to Microsoft 365 Backup Storage > Applying a backup plan
Applying a backup plan

You can have one backup plan per type of data (Exchange mailboxes, SharePoint sites, or OneDrive). If a backup plan is already created, you can only apply that plan. You will not be allowed to create a new plan.

If you revoke and then reapply a backup plan to a workload, the existing backups (recovery points) will become unavailable when a new backup is created.

You can apply a backup plan on the Devices tab or on the Management > Cloud applications backup tab.

To apply a backup plan

Devices
Management > Cloud applications backup
In the Cyber Protect console, go to Devices > Direct Backup for Microsoft 365.
[If multiple Microsoft 365 organizations are added] Select a Microsoft 365 organization.

Select the items to which you want to apply a backup plan.

[To select the mailboxes or OneDrive accounts of all users, including mailboxes and OneDrive accounts that will be created in the future] Expand the Users node, select All users, and then click Group backup.
[To select individual mailboxes or OneDrive accounts] Expand the Users node, select All users, select user accounts, and then click Backup.
[To select all modern team sites, including sites that will be created in the future] Expand the Groups node, select All groups, and then click Group backup.
[To select individual modern team sites] Expand the Groups node, select All groups, select sites, and then click Backup.
[To select all classic communication sites, including sites that will be created in the future] Expand the Site collections node, select All site collections, and then click Group backup.

[To select individual classic communication sites] Expand the Site collections node, select All site collections, select sites, and then click Backup.

Select a backup plan, and then click Apply.

Applying a backup plan might take up to 45 minutes, due to the processing time that is required on the Microsoft 365 Backup Storage side.

The backup plans that are shown depend on the type of data. For example, in Users, only backup plans for mailboxes or OneDrive accounts are available.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.