---
title: "Microsoft 365 Teams Protection, Direct Backup, and Local Agent"
section: "Managing the backup and recovery of workloads and files"
subsection: "Protecting Microsoft 365 Teams and Direct Backup"
page_range: "820-842"
tags: [Microsoft-365, Teams, Direct-Backup, M365-Backup-Storage, Agent-for-Office-365, OneNote, team-channels, team-mailbox, team-site, meetings, local-agent, Entra-admin-center]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#microsoft-365-business-backup.html"
---

# Protecting Microsoft 365 Teams

## What Can Be Backed Up

You can back up entire teams, including team name, team members list, team channels and their content, team mailbox and meetings, and team site. OneNote notebooks can be included via a separate option in the backup plan.

## Recoverable Items

- Entire team
- Team channels
- Channel files
- Team mailbox (email folders, email messages)
- Meetings
- Team site

You cannot recover conversations in team channels directly, but you can download them as a single HTML file.

## Limitations

The following items are not backed up:
- Settings of the general channel (moderation preferences) -- due to Microsoft Teams API limitation.
- Settings of custom channels (moderation preferences) -- due to Microsoft Teams API limitation.
- Meeting notes.
- Messages in the Chat section (private one-on-one chats and group chats).
- Stickers and praises.

Backup and recovery are supported for the following channel tabs: Word, Excel, PowerPoint, PDF, Document Library.

## Selecting Teams

1. Click **Microsoft 365**, select the organization.
2. Expand **Teams** > **All teams**, select teams or click **Group backup** for all.
3. Configure schedule, retention, encryption, and optionally enable **Include OneNote**.
4. Apply the plan.

## Recovering an Entire Team

1. Click **Microsoft 365**, select the organization.
2. Expand **Teams** > **All teams**, select the team, click **Recovery**.
3. Select a recovery point.
4. Click **Recover** > **Entire Team**. Specify target organization and team.
5. Click **Start recovery**. Choose overwrite options.
6. Click **Proceed**.

> **Note:** You can recover a team only into an existing team. You cannot create teams during recovery operations. When you delete a channel in Microsoft Teams, it is not immediately removed. The recovered team will have a postfix added to such channel names.

Conversations are recovered as a single HTML file in the **Files** tab of the channel, in a folder named: `<Team name>_<Channel name>_conversations_backup_<date>T<time>Z`.

> **Important:** After recovering a team or team channels, go to Microsoft Teams, select the recovered channels, and click their **Files** tab. Otherwise, subsequent backups of these channels will not include this tab's content.

## Recovering Team Channels or Files in Team Channels

1. Navigate to the team, click **Recovery**, select a recovery point.
2. Click **Recover** > **Channels**.
3. Select channels and/or open the **Files** folder to select individual files.
4. Specify target organization, team, and channel.
5. Choose overwrite options, click **Proceed**.

## Recovering a Team Mailbox

1. Navigate to the team, click **Recovery**, select a recovery point.
2. Click **Recover** > **Email messages**.
3. Select the root mailbox folder, click **Recover**.
4. Specify target organization, mailbox.
5. Choose overwrite options, click **Proceed**.

## Recovering Team Mailbox Items to PST Files

1. Navigate to the team, click **Recovery**, select a recovery point.
2. Click **Recover** > **Email messages**, browse/search for items.
3. Select items, click **Recover as PST files**.
4. Set encryption password, confirm.

The items are delivered as password-protected ZIP (max 2 GB per PST file). Download link is available for 24 hours.

## Recovering Email Messages and Meetings

1. Navigate to the team, click **Recovery**, select a recovery point.
2. Click **Recover** > **Email messages**, browse/search.
3. Select items, click **Recover**. Specify target organization, mailbox.
4. Choose overwrite options, click **Proceed**.

## Recovering a Team Site or Specific Items

1. Navigate to the team, click **Recovery**, select a recovery point.
2. Click **Recover** > **Team site**, browse/search for items.
3. Select items, click **Recover**. Specify target organization, team.
4. Choose sharing permissions recovery and overwrite options, click **Proceed**.

## Protecting OneNote Notebooks

By default, OneNote notebooks are included in backups of OneDrive files, Microsoft Teams, and SharePoint sites. To exclude them, disable the **Include OneNote** switch.

**Supported versions:** OneNote 2016 and later, OneNote for Windows 10.

**Limitations:**
- Notebooks saved in OneDrive or SharePoint are limited to 2 GB recovery size.
- Notebooks with section groups are not supported.
- When recovering with overwrite options, the default OneNote notebook of a team may not be overwritten.

## Protecting Microsoft 365 Collaboration App Seats

The Advanced Email Security pack provides real-time protection for Microsoft 365, Google Workspace, or Open-Xchange mailboxes: antimalware, anti-spam, URL scan, DMARC analysis, anti-phishing, impersonation protection, attachments scan, content disarm and reconstruction, graph of trust.

To access: **Devices** > **Microsoft 365** > **Users** > click **Go to Email Security**.

---

# Direct Backup to Microsoft 365 Backup Storage

**Direct Backup to Microsoft 365 Backup Storage** provides frequent backups (every 10 minutes), fast recovery, and simplified backup plans. Data never leaves the Microsoft 365 data trust boundary, as it is stored in Microsoft 365 Backup Storage. No separate Azure subscription is required.

## Supported Data Types and Retention

- **Exchange mailboxes:** All backups available for one year.
- **OneDrive accounts:** One year, with trailing two weeks of frequent backups. After day 15, weekly backups are available.
- **SharePoint sites:** Same retention as OneDrive.

## Creating and Applying a Backup Plan

1. Go to **Devices** > **Direct Backup for Microsoft 365** or **Management** > **Cloud applications backup**.
2. Select data items (Exchange mailboxes, OneDrive, SharePoint sites).
3. Create or select a backup plan. Only one plan per type of data is allowed per customer tenant.
4. Click **Apply**. Applying may take up to 45 minutes.

Backups run automatically every 10 minutes. You cannot run them manually.

## Recovering Backed-Up Items

Recovery is to original locations only. You can recover one item at a time.

- **Exchange mailbox:** Items changed or deleted are replaced by backed-up items. New/unchanged items are not overwritten.
- **OneDrive account:** Content is completely overwritten by backed-up content.
- **SharePoint site:** Content is completely overwritten by backed-up content.

Recovery can be initiated from the **Devices** tab or from **Backup storage** > **Microsoft 365 Backup storage**.

## Revoking and Deleting Backup Plans

Revoking or deleting a backup plan may take a few minutes due to processing on the Microsoft 365 Backup Storage side. On the **Devices** tab, you cannot delete plans applied to device groups.

---

# Locally Installed Agent for Office 365

The locally installed Agent for Office 365 provides backup of Exchange Online user mailboxes and shared mailboxes only. Group mailboxes and archive mailboxes (In-Place Archive) cannot be backed up.

## Adding a Microsoft 365 Organization (Local Agent)

1. Download and install Agent for Office 365 on a Windows machine connected to the Internet.
2. In the Cyber Protect console, go to **Devices** > **Microsoft Office 365**.
3. Enter your application ID, application secret, and Microsoft 365 tenant ID.
4. Click **OK**.

> **Important:** There must be only one locally installed Agent for Office 365 in an organization.

## Obtaining Application ID and Application Secret

Create a custom application in **Microsoft Entra admin center** > **Azure Active Directory** > **App registrations**:

1. Register a new application with supported account types set to **Accounts in this organizational directory only**.
2. Grant API permissions: **Office 365 Exchange Online** > **Application permissions** > **full_access_as_app**. Then **Microsoft Graph** > **Application permissions** > **Directory.Read.All**. Grant admin consent.
3. Create a client secret under **Certificates & secrets** > **New client secret** (Expires: Never).

## Recovering Mailboxes and Items (Local Agent)

**Mailboxes:** Select the mailbox, click **Recovery**, select a recovery point, click **Recover** > **Mailbox**, specify target mailbox, click **Start recovery**. Existing items with matching IDs are overwritten.

**Mailbox items:** Select the mailbox, click **Recovery**, select a recovery point, click **Recover** > **Email messages**, browse/search, select items, click **Recover**, specify target mailbox, click **Start recovery**. Items are recovered to the **Recovered items** folder.
