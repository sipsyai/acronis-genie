---
title: "Protecting Microsoft 365 Data"
section: "Managing the backup and recovery of workloads and files"
subsection: "Protecting Microsoft 365 data"
page_range: "780-842"
tags: [Microsoft-365, Exchange-Online, OneDrive, SharePoint-Online, Teams, cloud-backup, mailbox-backup, PST-recovery, antimalware-scan, cloud-agent, backup-plan]
acronis_version: "26.02"
---

# Protecting Microsoft 365 Data

Regular backups of Microsoft 365 data provide an additional layer of protection from user errors and intentional malicious actions. You can recover deleted items from a backup even after the Microsoft 365 retention period expires, and keep a local copy of Exchange Online mailboxes for regulatory compliance.

> **Important:** Actions with cloud-to-cloud resources (viewing content of backed-up emails, downloading attachments, recovering to non-original mailboxes, sending emails) might violate user privacy. These actions are logged in **Monitoring** > **Audit log** in Management Portal.

## Backup Solutions Comparison

Three solutions are available:

| Feature | Microsoft 365 Business - Backup | Direct Backup to M365 Backup Storage | Agent for Office 365 |
|---|---|---|---|
| Agent type | Cloud agent (no installation) | Cloud agent (no installation) | Local agent (Windows machine) |
| Exchange Online | User, shared, group mailboxes; public folders | User mailboxes | User and shared mailboxes |
| OneDrive | User files and folders | User files and folders | - |
| SharePoint Online | Classic and modern team sites; individual data items | Classic communication sites; modern team sites | - |
| Teams | Entire teams, channels, files, mailboxes, meetings, team sites | - | - |
| OneNote notebooks | Yes (as part of OneDrive/SharePoint/Teams) | - | - |
| Archive mailboxes (In-Place Archive) | Yes | Yes | No |
| Backup schedule | Up to 6x/day* | Every 10 minutes | User-defined |
| Backup retention | Flexible (date, count, unlimited) | Fixed (1 year) | Flexible |
| Backup location | Cloud storage | Microsoft 365 Backup Storage | Cloud, local, network |
| Granular recovery | Yes | No | Yes |
| Recovery to another user | Yes | No | Yes |
| Recovery to another M365 org | Yes | No | No |
| Max protected workloads | 50,000 per company** | N/A | 5,000 mailboxes (cloud); 2,000/plan (other) |

\* Default is once a day. Backups start at approximate intervals based on cloud agent load.

\*\* The maximum number depends on workload type: 50,000 Exchange mailboxes or 10,000 teams or 10,000 SharePoint sites or 5,000 OneDrive accounts. Formula: `10 mailboxes = 2 teams = 2 sites = 1 OneDrive account`.

> **Note:** For tenants in Compliance mode, only the locally installed agent is available, limited to Exchange Online mailbox backup.

## Limitations

- A mailbox backup includes only folders visible to users. The **Recoverable items** folder and subfolders (Deletions, Versions, Purges, Audits, DiscoveryHold, Calendar Logging) are not included.
- Automatic creation of users, public folders, groups, or sites during recovery is not possible.
- You cannot simultaneously recover items from different recovery points.
- Sensitivity labels applied to content are preserved but might not be shown if recovered to a non-original location.
- **Direct Backup to Public Cloud** is not supported.

## Required User Rights

**In Cyber Protect Cloud:**
- **Microsoft 365 Business - Backup**: Cloud agent can operate at customer tenant and unit level.
- **Direct Backup to Microsoft 365 Backup Storage**: Cloud agent operates at customer-tenant level only.
- Local agent must be registered under a company administrator account at the customer tenant level.

**In Microsoft 365:**
- Your account must have the global administrator role.
- At least one administrator account must have a mailbox and read/write rights to the public folders you want to back up.

## Adding a Microsoft 365 Organization

1. Log in to the Cyber Protect console as administrator.
2. Navigate to the appropriate level (customer tenant or unit).
3. Click **Devices** > **Add**.
4. Select the backup solution: **Microsoft 365 Business - Backup**, **Direct Backup to Microsoft 365 Backup Storage**, or **Microsoft 365** (if both are enabled).
5. On the Microsoft 365 login page, sign in with global administrator credentials.
6. Confirm that you grant the required permissions.

You can add multiple Microsoft 365 organizations in the tenant, but you cannot add the same organization in both backup solutions.

## Discovering Microsoft 365 Resources

When you add a Microsoft 365 organization, resources (mailboxes, OneDrive accounts, SharePoint sites) are synchronized to the Cyber Protect console. This discovery operation runs automatically once a day; you can also run it manually (up to 10 times per hour).

**Tips:**
- The cloud agent synchronizes with Microsoft 365 every 24 hours. To synchronize changes immediately, run a discovery operation manually.
- If you apply a backup plan to **All groups**, **All public folders**, **All site collections**, **All teams**, or **All users**, newly added items will be included after synchronization.

## Backup Frequency

| Scheduling option | Approximate interval |
|---|---|
| Once a day (default) | 24 hours |
| Twice a day | 12 hours |
| 3 times a day | 8 hours |
| 6 times a day | 4 hours |

> **Note:** Backups of group mailboxes can only run once a day.

## Protecting Exchange Online Data

### What Can Be Backed Up

User mailboxes, shared mailboxes, group mailboxes, and optionally online archive mailboxes (In-Place Archive) of the selected mailboxes.

### Recoverable Items

From a mailbox backup: Mailboxes, email folders, email messages, calendar events, tasks, contacts, journal entries, notes.

From a public folder backup: Subfolders, posts, email messages.

### Selecting Mailboxes

1. In the Cyber Protect console, click **Microsoft 365**.
2. Select the Microsoft 365 organization.
3. Select mailboxes: expand **Users** > **All users** for user/shared mailboxes, or **Groups** > **All groups** for group mailboxes.
4. Create or select a backup plan, configure schedule, retention, encryption, and optional archive mailbox and antimalware scan settings.
5. Click **Apply**.

### Antimalware Scan of Mailboxes

Requires the **Advanced Security + XDR** pack with **Microsoft 365 seats** quota enabled. Scans run automatically after each backup. Backups are marked with green (clean), red (threats detected), or gray (not yet scanned) indicators.

**Limitations:** Not supported for RAR, 7z, ISO file types. Not supported for Loop components. Supported only on default cloud storage. Not supported for tenants in Compliance mode.

### Recovering Mailboxes

1. Click **Microsoft 365**, select the organization.
2. Navigate to the user/shared/group mailbox, click **Recovery**.
3. Select a recovery point.
4. Click **Recover** > **Entire mailbox**.
5. Specify the target organization and mailbox. Choose overwrite options.
6. Click **Start recovery**.

### Recovering Mailbox Items

1. Navigate to the mailbox, click **Recovery**, select a recovery point.
2. Click **Recover** > **Email messages**.
3. Browse or search for items. Select items to recover.
4. Click **Recover**, specify target organization, mailbox, and folder.
5. Choose overwrite options, click **Start recovery**.

### Recovering to PST Files

Select the mailbox or items, click **Recover** > **As PST files**, set encryption password. The PST files (max 2 GB each) are delivered as a password-protected ZIP archive via email link. The archive is available for 96 hours.

> **Important:** Do not import PST files using the Import and Export Wizard. Open them by double-clicking or right-clicking and selecting **Open with... > Microsoft Outlook**.

## Protecting OneDrive Files

### What Can Be Backed Up

Entire OneDrive or individual files and folders. OneNote notebooks can be included via a separate option. Files are backed up with their sharing permissions (except advanced permission levels: Design, Full, Contribute).

**Limitation:** OneDrive content backup is not supported for shared mailboxes.

### Selecting OneDrive Files

1. Click **Microsoft 365**, select the organization.
2. Expand **Users** > **All users**, select users.
3. Configure the backup plan: select **OneDrive** in What to back up, specify items/exclusions, encryption, and optionally enable **Include OneNote**.
4. Apply the plan.

### Recovering OneDrive

- **Entire OneDrive:** Select user, click **Recovery**, select recovery point, click **Recover** > **Entire OneDrive**, specify target organization and user, choose sharing permissions recovery and overwrite options.
- **Individual files:** Select user, click **Recovery**, select recovery point, click **Recover** > **Files/folders**, browse/search, select files, optionally download them, then click **Recover** and specify target.

## Protecting SharePoint Online Sites

### What Can Be Backed Up

SharePoint classic communication sites and modern team sites. You can select individual subsites, lists, and libraries. OneNote notebooks can be included.

**Items skipped during backup:** Look and Feel settings (except title/description/logo), site page comments settings, Site features settings, web parts in wiki pages, checked out files, external data and Managed Metadata columns, the default `domain-my.sharepoint.com` collection, recycle bin contents.

### Recoverable Items

Entire site, subsites, lists, list items, document libraries, documents, list item attachments, site pages and wiki pages.

**Items that cannot be recovered:** Subsites based on Visio Process Repository template; lists of types Survey, Task, Picture library, Links, Calendar, Discussion Board, External, Import Spreadsheet; lists with multiple content types enabled.

### Selecting SharePoint Data

1. Click **Microsoft 365**, select the organization.
2. For classic sites: expand **Site collections** > **All site collections**.
3. For modern team sites: expand **Groups** > **All groups**.
4. Configure items to back up, exclusions, schedule, retention, encryption, and optionally include OneNote.

### Recovering SharePoint Data

1. Navigate to the site, click **Recovery**, select a recovery point.
2. Click **Recover SharePoint files**.
3. Browse or search for items, select them.
4. Click **Recover**, specify target organization and site.
5. Choose sharing permissions recovery and overwrite options.
6. Click **Start recovery**.

## Avoiding Duplicate Backups of Microsoft 365 Groups

Groups that are part of a Microsoft team can appear under both **Teams** and **Groups**. To avoid duplicate backups, configure backup only at the team level. Check the **Team** column in **Groups** > **All groups** to identify groups that are part of a team.

## Deleting a Microsoft 365 Organization

Deleting a Microsoft 365 organization does not affect existing backups. Delete the backups first if no longer needed, then delete the organization. After deletion, revoke the access rights of the Backup Service application in **Microsoft Entra admin center** > **Identity** > **Applications** > **Enterprise applications** > **Backup Service** > **Properties** > **Delete**.

## Changing Microsoft 365 Access Credentials

To update access credentials: Go to **Devices** > **Microsoft 365**, select the organization, click **Settings**, and update the credentials.
