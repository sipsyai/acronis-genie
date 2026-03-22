# Comparison of backup solutions for Microsoft 365 data

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Comparison of backup solutions for Microsoft 365 data
Comparison of backup solutions for Microsoft 365 data

Depending on the services that are enabled for the customer tenant, the following backup solutions are available:

Microsoft 365 Business – Backup
Direct Backup to Microsoft 365 Backup Storage

Agent for Office 365 (locally installed agent)

For tenants in Compliance mode, only the locally installed agent is available. These tenants can back up only Microsoft 365 mailboxes. They cannot use the extended functionality provided by the cloud agent.

Azure Information Protection (AIP) is supported with all solutions.

The following table summarizes the functionality of the backup solutions.

Solution	Microsoft 365 Business – Backup	Direct Backup to Microsoft 365 Backup Storage	Agent for Office 365
Agent type

Cloud agent

The cloud agent provides extended backup functionality, which is directly accessible in the Cyber Protect console

No installation is required



Cloud agent

The cloud agent provides extended backup functionality, which is directly accessible in the Cyber Protect console

No installation is required



Local agent

The locally installed agent only provides backup of Exchange online mailboxes

The agent must be installed on a Windows machine that is connected to the Internet


Data items that can be backed up
Exchange Online:
user mailboxes and shared mailboxes (including mailboxes of users on a Kiosk plan and mailboxes on litigation hold)
group mailboxes
public folders
OneDrive: user files and folders
SharePoint Online:
classic communication sites
modern team sites
individual data items
Microsoft 365 Teams:
entire teams
team channels
channel files
team mailboxes
files and email messages in team mailboxes
meetings
team sites
OneNote notebooks: as part of OneDrive, SharePoint Online, and Microsoft 365 Teams backups

Exchange Online:
user mailboxes
OneDrive: user files and folders
SharePoint Online:
classic communication sites
modern team sites


Exchange Online: user mailboxes and shared mailboxes (including mailboxes of users on a Kiosk plan and mailboxes on litigation hold)


Backup of archive mailboxes (In-Place Archive)

Yes

Yes

No


Backup schedule

Up to six times per day*



Every 10 minutes



User-defined


Backup retention	Flexible – by date, number of backups, or unlimited

Fixed

For mailboxes – one year of frequent backups

For OneDrive accounts and SharePoint sites – one year, with trailing two weeks of frequent backups, and weekly backups for the rest of the period

Flexible – by date, number of backups, or unlimited
Backup locations

Cloud storage

(including partner-hosted storage)

Microsoft 365 Backup Storage

Cloud storage, local folder, network folder


Backup resiliency	Provided as standard – cloud storage data centers are not co-located with any Microsoft data centers	Automatic replication to other storage containers within the Microsoft network	No
Automatic protection of new Microsoft 365 users, groups, sites, and teams

Yes, by applying a protection plan to the All users, All groups, All sites, All teams groups

Yes, by applying a protection plan to the All users and All groups, and All sites

No


Protecting more than one Microsoft 365 organization

Yes

Yes

No


Granular recovery

Yes

No

Yes


Recovery to another user in the same Microsoft 365 organization within the same backup solution

Yes

No

Yes


Recovery to another Microsoft 365 organization in the same tenant, within the same backup solution

Yes

No

No


Recovery to an on-premises Microsoft Exchange Server

No

No

No


Maximum number of items that can be backed up without performance degradation

Up to 50,000 protected workloads per company**

N/A

When backing up to the cloud storage: 5,000 mailboxes per company

When backing up to other destinations: 2,000 mailboxes per protection plan (no limitation for number of mailboxes per company)


Maximum number of manual backup runs

10 manual runs during an hour

N/A

Unlimited


Maximum number of simultaneous recovery operations

10 operations, including Google Workspace recovery operations

N/A

Unlimited


Performance	Typical speeds for cloud-to-cloud backup and recovery	Faster backup and recovery, no data throttling	Typical speeds for backup and recovery

* The default option is Once a day. You can schedule up to six backups per day. The backups start at approximate intervals that depend on the current load of the cloud agent, which serves multiple customers in a data center. This ensures an even load during the day and an equal quality of service for all customers.

The protection schedule might be affected by the operation of third-party services, for example, the accessibility of Microsoft 365 servers, throttling settings on the Microsoft servers, and others. See also Microsoft Graph throttling guidance.

** The maximum number of workloads depends on the workload type, as follows: 50,000 Exchange mailboxes or 10,000 teams or 10,000 SharePoint sites or 5,000 OneDrive accounts.

To calculate the supported combinations, use the following formula:

10 mailboxes = 2 teams = 2 sites = 1 OneDrive account

For example:

50,000 mailboxes
40,000 mailboxes and 1,000 OneDrive accounts
40,000 mailboxes and 2,000 sites
40,000 mailboxes and 2,000 teams
30,000 mailboxes, 1,000 OneDrive accounts, 1,000 sites, and 1,000 teams
30,000 mailboxes, 2,000 sites, and 2,000 teams

We recommend that you back up the workloads sequentially and in the following order:

Mailboxes
OneDrive accounts
Teams
SharePoint sites

The first full backup might take several days, depending on the number of protected items and their size. Do not start the next backup until the previous one is complete.

Limitations
All users with a mailbox or OneDrive account are shown in the Cyber Protect console, including users without a Microsoft 365 license and users who are blocked from signing in to the Microsoft 365 services.
A mailbox backup includes only folders visible to users. The Recoverable items folder and its subfolders (Deletions, Versions, Purges, Audits, DiscoveryHold, Calendar Logging) are not included in a mailbox backup.
Automatic creation of users, public folders, groups, or sites during a recovery is not possible. For example, if you want to recover a deleted SharePoint Online site, first create a new site manually, and then specify it as the target site during a recovery.
You cannot simultaneously recover items from different recovering points, even though you can select such items from the search results.
During a backup, any sensitivity labels that are applied to the content will be preserved. Therefore, sensitive content might not be shown if it is recovered to a non-original location and its user has different access permissions.
[For Microsoft 365 Business – Backup] You can apply only one individual backup plan to a workload.
[For Microsoft 365 Business – Backup] When an individual backup plan and a group backup plan are applied to the same workload, the settings in the individual plan take precedence.
[For Direct Backup to Microsoft 365 Backup Storage] You can create and apply one backup plan per type of data (Exchange mailboxes, SharePoint sites, or OneDrive accounts).
Direct Backup to Public Cloud is not supported.
See also
Microsoft 365 Business – Backup
Direct Backup to Microsoft 365 Backup Storage
Locally installed Agent for Office 365
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.