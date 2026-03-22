# Selecting SharePoint Online data

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Selecting SharePoint Online data
Selecting SharePoint Online data

Select the data as described below, and then specify other settings of the protection plan as appropriate.

To select SharePoint Online data

Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose users' data you want to back up. Otherwise, skip this step.

Do one of the following:

To back up all classic SharePoint sites in the organization, including sites that will be created in the future, expand the Site collections node, select All site collections, and then click Group backup.
To back up individual classic sites, expand the Site collections node, select All site collections, select the sites that you want to back up, and then click Backup.

To back up all group (modern team) sites, including sites that will be created in the future, expand the Groups node, select All groups, and then click Group backup.

Starting from Cyber Protect Cloud 25.06, unprotected groups that are part of a team are not shown in Devices > Microsoft 365 > Microsoft 365 organization > Groups. You can protect the SharePoint site and group mailbox of these groups by applying a backup plan to the whole team. For more information, see Protecting Microsoft 365 Teams.

To back up individual group (modern team) sites, expand the Groups node, select All groups, select the groups whose sites you want to back up, and then click Backup.

Starting from Cyber Protect Cloud 25.06, unprotected groups that are part of a team are not shown in Devices > Microsoft 365 > Microsoft 365 organization > Groups. You can protect the SharePoint site and group mailbox of these groups by applying a backup plan to the whole team. For more information, see Protecting Microsoft 365 Teams.

In the backup plan, configure the following:

In Items to back up, do one of the following:

Keep the default setting [All] (all items of the selected sites).

Specify the subsites, lists, and libraries to back up by adding their names or paths.

To back up a subsite or a top-level site list/library, specify its display name in the following format: /display name/**

To back up a subsite list/library, specify its display name in the following format: /subsite display name/list display name/**

The display names of subsites, lists, and libraries are shown on the Site contents page of a SharePoint site or subsite.

Specify the subsites to back up by browsing.

The Browse link is available only when creating a protection plan for a single site.

[Optional] In Items to back up, click Show exclusions to specify the subsites, lists, and libraries to skip during the backup.

Item exclusions override the item selection; i.e. if you specify the same subsite in both fields, this subsite will be skipped during a backup.

In Schedule, select the backup frequency.

In How long to keep, configure the retention rules for the backups.
In Encryption, click Specify password.
Specify and confirm the encryption password, and then select the encryption algorithm.
Click OK.

To back up OneNote notebooks, enable the Include OneNote switch.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.