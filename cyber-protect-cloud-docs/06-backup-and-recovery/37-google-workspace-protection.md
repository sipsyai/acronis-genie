---
title: "Protecting Google Workspace Data"
section: "Managing the backup and recovery of workloads and files"
subsection: "Protecting Google Workspace data"
page_range: "843-866"
tags: [Google-Workspace, Gmail, Google-Drive, Shared-Drives, cloud-backup, notarization, blockchain, search-indexes, full-text-search, Google-Cloud-project, service-account]
acronis_version: "26.02"
---

# Protecting Google Workspace Data

> **Note:** This feature is not available for tenants in Compliance mode.

## What Does Google Workspace Protection Mean?

- Cloud-to-cloud backup and recovery of Google Workspace user data (Gmail mailboxes, Calendars, Contacts, Google Drives) and Google Workspace Shared drives.
- Granular recovery of emails, files, contacts, and other items.
- Support for several Google Workspace organizations and cross-organization recovery.
- Optional notarization of backed-up files by means of the Ethereum blockchain database.
- Optional full-text search for searching emails by their content.
- Up to 5,000 items (mailboxes, Google Drives, and Shared drives) per company without performance degradation.
- Backed-up data is automatically compressed (Normal level for cloud-to-cloud backups).

## Required User Rights

**In Cyber Protection:** You need to be a company administrator acting on a customer tenant level. Company administrators acting on unit level, unit administrators, and users cannot back up or recover Google Workspace data.

**In Google Workspace:** You must be signed in as a Super Admin with enabled API access (**Security** > **API reference** > **Enable API access** in the Google Admin console). The Super Admin user should have at least the "Google Workspace Business Standard" license to discover and back up Shared Drives.

## Backup Schedule

The default option is **Once a day**. You can schedule up to six backups per day.

| Scheduling option | Approximate interval |
|---|---|
| Once a day (default) | 24 hours |
| Twice a day | 12 hours |
| 3 times a day | 8 hours |
| 6 times a day | 4 hours |

## Limitations

- Only users with an assigned Google Workspace license and a mailbox or Google Drive are shown.
- Archived or suspended users are shown as inactive after discovery (72-hour grace period).
- Backups of deleted users are not automatically deleted from cloud storage.
- Documents in native Google formats are backed up as generic office documents (.docx, .pptx) and converted back during recovery.
- You can manually run up to 10 backups per hour.
- You can simultaneously run up to 10 cloud-to-cloud recovery operations (including both Microsoft 365 and Google Workspace).
- **Direct Backup to Public Cloud** is not supported.

## Adding a Google Workspace Organization

You need a dedicated personal Google Cloud project.

1. Log in to the Cyber Protect console as a company administrator.
2. Click **Devices** > **Add** > **Google Workspace**.
3. Enter the Super Administrator email address.
4. Browse for the JSON file containing the private key of the service account.
5. Click **Confirm**.

**Useful tips:**
- After adding an organization, data from primary and secondary domains is backed up.
- The cloud agent synchronizes every 24 hours. Run discovery manually to sync immediately.
- If you apply a plan to **All users** or **All Shared drives**, newly added items are included after synchronization.

## Creating a Personal Google Cloud Project

1. **Create a new project** in the Google Cloud Platform console.
2. **Enable required APIs:** Admin SDK API, Gmail API, Google Calendar API, Google Drive API, Google People API.
3. **Configure the OAuth consent screen:** Select **Internal**, specify app name and support/developer emails.
4. **Create a service account** under IAM & Admin > Service accounts. Create a JSON key.
5. **Grant domain-wide delegation:** In the Google Admin console, go to **Security** > **Access and data control** > **API controls** > **Domain-wide delegation** > **Add new**. Enter the client ID and the following OAuth scopes:
   - `https://mail.google.com`
   - `https://www.googleapis.com/auth/contacts`
   - `https://www.googleapis.com/auth/calendar`
   - `https://www.googleapis.com/auth/admin.directory.user.readonly`
   - `https://www.googleapis.com/auth/admin.directory.domain.readonly`
   - `https://www.googleapis.com/auth/drive`
   - `https://www.googleapis.com/auth/gmail.modify`

## Protecting Gmail Data

### What Can Be Backed Up

Gmail user mailboxes (including Calendar and Contacts data). Optionally, shared calendars.

**Skipped items:** Birthdays, Reminders, Tasks calendars; folders attached to calendar events; the Directory folder in Contacts; appointment slots; conferencing field; All-day event notifications setting; Auto-accept invitations setting; Other contacts folder; external profiles; the contact field File as.

### Recoverable Items

Mailboxes, email folders (labels), email messages, calendar events, contacts.

**Limitations:** Contact photos cannot be recovered. The Out of office calendar item is recovered as a regular event.

### Selecting Gmail Mailboxes

1. Click **Google Workspace**, select the organization.
2. Expand **Users** > **All users**, select users or click **Group backup** for all.
3. Configure: select **Gmail** in What to back up, optionally enable **Include shared calendars**, set retention and encryption.

### Recovering Mailboxes

1. Navigate to the user, click **Recovery**, select a recovery point.
2. Click **Recover** > **Entire mailbox**.
3. Specify target organization, mailbox. Choose overwrite options.
4. Click **Start recovery**.

### Recovering Mailbox Items

1. Navigate to the user, click **Recovery**, select a recovery point.
2. Click **Recover** > **Email messages**, browse/search.
3. Select items. Use **Show versions** for version selection, **Show content** for previewing, **Send as email** for forwarding.
4. Click **Recover**, specify target organization, mailbox, path.
5. Choose overwrite options, click **Proceed**.

**Search options:** By subject, sender, recipient, date, attachment name, message content (if Full-text search enabled). For events: title and date. For contacts: name, email, phone.

## Protecting Google Drive Files

### What Can Be Backed Up

Entire Google Drive or individual files/folders with sharing permissions. The **Shared with me** folder and the **Computers** folder are not backed up.

**Supported Google formats:** Google Docs, Google Sheets, Google Slides are fully supported. Google Drawings recovered as .svg, Google Sites as .txt, Google Jamboard as .pdf, Google My Maps skipped.

### Recovery Limitations

Comments and sharing links are not recovered. Read-only Owner settings cannot be changed during recovery.

### Selecting Google Drive Files

1. Click **Google Workspace**, select the organization.
2. Expand **Users** > **All users**, select users or use Group backup.
3. Configure: select **Google Drive**, specify items/exclusions, retention, encryption.

### Recovering Google Drive

**Entire Drive:** Select user, click Recovery, select recovery point, click **Recover** > **Entire Drive**, specify target organization and user, choose sharing permissions and overwrite options.

**Individual files:** Select user, click Recovery, select recovery point, click **Recover** > **Files/folders**, browse/search, select files, choose target, permissions, and overwrite options.

## Protecting Shared Drive Files

### What Can Be Backed Up

Entire Shared drive or individual files/folders with sharing permissions. The **Shared with me** folder is not backed up. A Shared drive without members cannot be backed up.

### What Can Be Recovered

Entire Shared drive or any file/folder. Sharing permissions can be recovered or inherited. Some sharing permissions may not be recovered depending on organization and drive settings.

### Selecting Shared Drive Files

1. Click **Google Workspace**, expand **Shared drives** > **All Shared drives**.
2. Select drives or use Group backup. Configure items, exclusions, retention, encryption.

### Recovering Shared Drives

**Entire drive:** Select drive, click Recovery, click **Recover** > **Entire Shared drive**, specify target organization and drive/user, choose permissions.

**Individual files:** Select drive, click Recovery, click **Recover** > **Files/folders**, browse, select, specify target, permissions, and overwrite options.

## Notarization

Notarization proves that a file is authentic and unchanged since backup using the Ethereum blockchain. Available only for backups of Google Drive files and Shared drive files.

To enable: toggle the **Notarization** switch when creating a protection plan.

**How it works:** During backup, hash codes are calculated, a hash tree is built, and the hash tree root is stored in the Ethereum blockchain. When verifying, the agent compares file hashes against the stored hash tree and blockchain.

**To verify authenticity:** Select a notarized file, then click **Verify** or **Get certificate**.

## Search in Cloud-to-Cloud Backups

When recovering, you can search for specific backed-up items instead of browsing. Search capabilities depend on:

- **Search type:** Enhanced (index-based) or typical (non-index based). Index-based is faster and provides additional options.
- **Archive type:** In non-encrypted backups, only enhanced search is supported. In encrypted backups, enhanced search is optional.

| Workload | Data type | Without enhanced search | With enhanced search |
|---|---|---|---|
| M365 Mailbox | Email | Basic search available | Enhanced search |
| M365 OneDrive | Files/folders | Not available | Enhanced search |
| M365 SharePoint | Files | Not available | Enhanced search |
| M365 Teams Channels | Channels | Not available | Enhanced search |
| M365 Teams Email | Email | Basic search | Enhanced search |
| M365 Teams Site | Site | Not available | Enhanced search |
| Google Mailbox | Email | Not available | Enhanced search |
| Google Drive | Files/folders | Not available | Enhanced search |
| Shared Drives | Files/folders | Not available | Enhanced search |

### Full-Text Search

Available only for Gmail backups, enabled by default. Allows searching in email body text. The full-text search index takes 10-30% of the storage space used by the Gmail backup.

### Search Indexes

Archives are automatically indexed after each backup. Indexing does not affect backup performance. Search results become available after indexing completes (up to 24 hours for first backup).

**Managing indexes:** Go to **Backup storage** > **Cloud applications backup**, select archive, in **Actions** choose **Update index**, **Rebuild index**, or **Delete index**. Only company administrators in partner tenants can rebuild or delete indexes.

### Enabling Enhanced Search in Encrypted Backups

In a new backup plan: enable encryption, then select **Allow enhanced search in encrypted backups**. In an existing plan: edit the plan, select **Search options** tab, enable the switch, save settings.

> **Note:** You cannot disable encryption or enhanced search once enabled. Create a new backup plan instead.

### Disabling Full-Text Search for Gmail

When creating or editing a backup plan, click the gear icon, go to the **Full-text search** tab, disable the switch. If re-enabled later, all archives created by this plan will be re-indexed.
