---
title: "Email Archiving"
section: "Managing the backup and recovery of workloads and files"
subsection: "Email archiving"
page_range: "719-745"
tags: [email-archiving, Microsoft-365, archiving-plan, retention-rules, legal-hold, search-queries, PST-import, compliance, eDiscovery, immutable-storage]
acronis_version: "26.02"
---

# Email Archiving

With email archiving, all emails in your Microsoft 365 organization are retained in an external archive that is stored in the cloud, allowing you to achieve compliance and respond to eDiscovery requests. New emails are added to the archive continuously, as they are sent or received, and cannot be modified or manually deleted.

The emails are shown in two folders for each user mailbox -- **Incoming** and **Outgoing**. In each folder, the emails are sorted chronologically, from most recent to the oldest. The archive is encrypted with the AES-256 algorithm. Only authorized users can access the archive, in accordance to their access level, and an audit trail for all actions is available.

You can perform the following actions:

- Browse the archive
- Search for specific messages by using ad-hoc search queries and saved search queries
- Preview emails without recovering them
- Recover specific emails, the **Incoming** and **Outgoing** folders, and whole mailboxes to the original or a non-original mailbox
- Download email attachments

By default, all emails are kept in the archive indefinitely. To delete emails that you no longer need, you can apply retention rules. When the retention period ends, the emails are automatically deleted. You cannot manually delete emails from the archive.

To keep specific emails in the archive regardless of any retention rules, you can apply legal hold rules. During the legal hold period, these emails cannot be deleted.

## Limitations

- The maximum size of an email that can be included in the archive is 150 MB, due to a Microsoft limitation.
- Draft emails are not included in the archive.
- You can apply one archiving plan to one mail server.

## Configuring Email Archiving

### Adding a Mail Server

**Prerequisites:** The following quotas must be enabled for the tenant in Management Portal:
- **Microsoft 365 email archiving seats**
- **Archiving storage**

> **Note:** Both quotas are required. If any of them is removed or misconfigured after the initial configuration, email archiving will be paused for all plans of the tenant until the quota is restored.

1. Log in to the Cyber Protect console as administrator.
2. Go to **Devices**, and then click **Add** > **Microsoft 365 Business -- Email archiving**.
3. On the Microsoft login page, sign in as global administrator.
4. Review the list of required permissions, and then click **Accept**.
5. Configure the archiving plan as described below.

### Viewing Activities and Alerts

- **Activities related to mail servers:** Go to **Devices** > **Mail servers**, click the server name, click the **Activities** tab.
- **All activities:** Go to **Monitoring** > **Activities**.
- **Alerts related to mail servers:** Go to **Devices** > **Mail servers**, click the server name, click the **Alerts** tab.
- **All alerts:** Go to **Monitoring** > **Alerts**.

### Removing a Mail Server

1. Go to **Devices** > **Mail servers**.
2. Click the name of the mail server, and then click **Delete**.
3. Confirm by clicking **Delete**.

The mail server is removed from the Cyber Protect console. The email archive will be kept, but it will no longer be updated.

## Email Archiving in Disabled or Deleted Tenants

| Disabled or deleted (soft delete) | Re-enabled or recovered | Deleted (hard delete) |
|---|---|---|
| Discovery operations do not run. New emails are not added. Retention rules and legal hold rules are not applied. Indexing operations do not run. | Discovery operations run again. New emails are added. Emails from the disabled period are imported. Retention and legal hold rules are applied. Indexing operations run again. | All data of the tenant, including the email archive, is permanently deleted. This action is irreversible. |

## Archiving Plans

With an archiving plan, you can configure which emails will be imported to the email archive. The initial import affects only the emails that were on the mail server prior to this server being added to the Cyber Protect console. After you add the mail server, all new emails will automatically be added to the archive. You can apply one archiving plan to one mail server.

### Creating an Archiving Plan

**New mail server:**
1. Add the mail server to the Cyber Protect console.
2. [Optional] Change the archiving plan name.
3. In **Import existing emails**, select **All mailboxes**, and then click **Done**.
4. Click **Encryption**, specify and confirm the encryption password, and then click **Save**.

> **Warning!** There is no way to browse the archive and recover data from it if you lose or forget this password.

5. Click **Create**.

**Existing mail server:**
1. Go to **Devices**, select the mail server.
2. Click the ellipsis icon (...), and then click **Protect**.
3-7. Follow the same steps as above.

### Editing, Applying, Revoking, and Deleting Archiving Plans

- **Edit:** Go to **Management** > **Archiving plans** > **Email archiving plans**, click the plan, click **Edit**.
- **Apply:** Go to **Devices** > **Mail servers**, click the mail server, click **Protect**, select the plan, click **Apply**.
- **Revoke:** Go to **Devices** > **Mail servers**, click the server, on the **Protect** tab click the ellipsis next to the plan, click **Revoke**.
- **Delete:** Go to **Management** > **Archiving plans**, click the plan, click **Delete**. The email archive will not be deleted, but it will no longer be updated.

## Importing Emails from PST Files

You can use PST files to import emails into an email archive. During import, the most frequent recipients become mailbox owners. Imported emails appear under **All mailboxes** > **Imported from PST**.

### Limitations

- PST files can be selected from a single personal OneDrive account only.
- Maximum allowed size per PST file is 50 GB.
- Only emails up to 200 MB are imported.
- You can select up to 100,000 PST files.
- Unicode PST files are fully supported; ANSI PST files might not be processed correctly.
- Deduplication is not supported.
- Rich text formatting (RTF) cannot be preserved in the body of an imported email.
- Emails imported from PST files can be recovered only to new targets.

### To Import Emails from PST Files

1. Go to **Backup storage** > **Cloud applications backups**, select the email archive.
2. Click **Import from PST files**.
3. Specify the encryption password and click **Proceed**.
4. In **Organization**, select the source Microsoft 365 organization.
5. In **What to import**, select PST files or folders from a user's OneDrive.
6. Click **Import**.
7. After the import completes, check its result under **All mailboxes** > **Imported from PST**.

## Search Queries

You can find specific emails in the email archive by using search queries, and then save the queries for future use. Search queries form the basis for creating retention rules and legal hold rules.

You can link a saved search query to a specific email archive (it can run only on the linked archive), or leave it non-linked (it can run on any email archive and be used in rules applied to multiple archives).

### Searching for Emails

1. Go to **Backup storage** > **Backups** > **Cloud application backups**.
2. Select an email archive, and then click **Browse archive**.
3. Enter the encryption password.
4. Select the search level (All emails, a user mailbox, or the Incoming/Outgoing folder).
5. Click **Search**, specify your search query, and then click **Search**.

The search is performed in the following fields: From, To, CC, BCC, Subject, Email body. You can use one or more words. To search for a specific phrase, put the phrase in quotation marks. Wildcards are not supported.

Use **Filter** to search in specific fields (From, To/CC/BCC, Subject contains), filter by attachment status, date, or deletion status.

### Sorting Emails

| Sort criteria | Sort order |
|---|---|
| Date | Chronological: Newest first, Oldest first |
| Subject | Alphabetical: A-Z, Z-A |
| Recipient | Alphabetical: A-Z, Z-A |
| Sender | Alphabetical: A-Z, Z-A |
| Attachments | With/without attachments on top (newest to oldest) |
| Relevance | Only available when performing a search. Uses a multi-tiered scoring system emphasizing match quality over quantity. |

### Creating, Running, Editing, and Deleting Saved Search Queries

- **Create from email archive:** While browsing an archive, perform a search, click **Save as**, specify a name, click **Save**.
- **Create from Management:** Go to **Management** > **Archiving plans** > **Search queries**, click **Create search query**, specify a name, optionally link to an email archive, specify the search query and criteria, click **Create**.
- **Run:** From the email archive's **Saved search queries** section, or from **Management** > **Archiving plans** > **Search queries**, click **Search**.
- **Edit:** Click the gear icon next to the query, click **Edit**, modify, click **Save**.
- **Delete:** Click **Delete** and confirm.

> **Warning!** Editing or deleting a search query affects the retention rules and legal hold rules in which this search query is used.

## Retention Rules

With retention rules, you can configure how long the emails will be kept in the email archive. Retention rules are based on search queries. Emails matching the search queries are kept for the configured retention period. After the retention period ends, the emails are automatically deleted.

> **Note:** If an email matches more than one retention rule, the rule with the longest retention period is applied.

Retention rules run on their email archives once every 24 hours. This operation is not user-configurable.

### Creating a Retention Rule

**From the email archive:** Run a search query, click **Apply retention rule**, configure the retention period (e.g., "By email age" -- 1 year, 2 months, 300 days), specify the encryption password, click **Create**.

**From Management > Archiving plans:** Go to **Retention rules**, click **Create retention rule**, select email archives, set the retention period, select saved search queries, specify the encryption password, click **Create**.

### Managing Retention Rules

- **Edit:** Go to **Management** > **Archiving plans** > **Retention rules**, select the rule, click **Edit**, modify settings, click **Save**.
- **Enable/Disable:** Select the rule, click **Enable** or **Disable**.
- **Delete:** Select the rule, click **Delete**, confirm.

## Legal Hold Rules

With legal hold rules, you can override the retention rules and prevent emails from being deleted. Legal hold rules are based on search queries. Emails matching the search queries are protected against deletion for the legal hold period. After the legal hold period ends, these emails can be deleted by a retention rule.

> **Note:** If an email matches more than one legal hold rule, the rule with the longest legal hold period is applied.

Legal hold rules run once every 24 hours. This operation is not user-configurable.

### Managing Legal Hold Rules

- **Create:** From the email archive (run a search query, click **Apply legal hold rule**) or from **Management** > **Archiving plans** > **Legal hold rules** (click **Create legal hold rule**). Configure the hold period (indefinite or until a specific date), select search queries, specify the encryption password, click **Create**.
- **Edit/Enable/Disable/Delete:** Go to **Management** > **Archiving plans** > **Legal hold rules**, select the rule, and use the corresponding action.

## Recovering Data from an Email Archive

### Previewing Emails

1. Go to **Backup storage** > **Cloud application backups**, select the archive, click **Browse archive**.
2. Enter the encryption password.
3. Search for and select the email to preview.

### Recovering Emails, Folders, and Mailboxes

**Emails:** Browse the archive, select the emails, click **Recover emails**, select the organization, select the recovery mailbox (original or another), click **Start recovery**. Incoming emails are recovered to the **Inbox** folder; outgoing emails to the **Sent** folder.

**Folders:** Browse the archive, select the **Incoming** or **Outgoing** folder, click **Recover folder**, select the organization and mailbox, click **Start recovery**.

**Mailboxes:** Browse the archive, select the mailbox, click **Recover user emails**, select the organization and mailbox, click **Start recovery**.

### Forwarding Archived Emails

You can select up to 10 emails from an email archive and send them to recipients of your choice. Select the emails, click **Send as email**, select the sender and specify recipients, click **Send**.

### Downloading Attachments

Browse the archive, search for emails with attachments, select them, click **Download attachments**. Multiple attachments are downloaded as a ZIP file.

### Immutable Storage for Email Archiving

With immutable storage, you can access deleted items (emails deleted by retention rules, or email archives deleted by an administrator) during the retention period. You can browse and search the deleted email messages, recover them, and undo their deletion.

> **Note:** You can undo deletion of individual emails. Undoing deletion of email archives is not supported.

To undo deletion: Go to **Backup storage** > **Cloud application backups**, click **Show deleted**, select an archive, click **Browse archive**, search for deleted emails, select up to 10, click **Undo deletion**.
