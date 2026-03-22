# Discovering Microsoft 365 resources

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Discovering Microsoft 365 resources
Discovering Microsoft 365 resources
This topic applies to Microsoft 365 Business – Backup and Direct Backup to Microsoft Backup Storage.

When you add a Microsoft 365 organization to Cyber Protect Cloud, the resources in this organization, such as Exchange mailboxes, OneDrive accounts, or SharePoint sites, are synchronized to the Cyber Protect console. This operation is called discovery and it is logged in Monitoring > Activities.

After the discovery operation completes, you can see the resources of the Microsoft 365 organization in the Cyber Protect console, and you can apply backup plans to them.

An automatic discovery operation runs once a day to keep the list of resources in the Cyber Protect console up to date. You can synchronize this list on demand, by running a discovery operation manually.

To run a discovery operation manually

[For Microsoft 365 Business – Backup] In the Cyber Protect console, go to Devices > Microsoft 365.
[For Direct Backup to Microsoft 365 Backup Storage] In the Cyber Protect console, go to Devices > Direct Backup for Microsoft 365.
Select the Microsoft 365 organization, and then, in the Actions pane, click Refresh.

You can manually run a discovery operation up to 10 times per hour. When this number is reached, the allowed runs are reset to one per hour, and then every hour an additional run becomes available, until a total of 10 runs per hour is reached again.
Useful tips

The cloud agent synchronizes with Microsoft 365 every 24 hours, starting from the moment when the organization is added to the Cyber Protection service. If you add or remove a user, group, or site, you will not see this change in the Cyber Protect console immediately. To synchronize the change immediately, run a discovery operation manually.

If you apply a backup plan to All groups, All public folders, All site collections, All teams, or All users, the newly added items will be included in the backup after synchronization.
According to Microsoft policy, when a user, group, or site is removed from the Microsoft 365 graphical user interface, it remains available via an API for a few days. During this period, the removed item is inactive (grayed out) in the Cyber Protect console and is not backed up. When the removed item becomes unavailable via the API, it disappears from the Cyber Protect console. You can find the backups of the removed user, group, or site (if any) in the Cyber Protect console, on the Backup Storage > Cloud applications backups tab.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.