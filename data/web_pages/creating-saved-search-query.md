# Creating a saved search query

Managing the backup and recovery of workloads and files > Email archiving > Search queries > Creating a saved search query
Creating a saved search query

You can create a saved search query from the email archive or from the Management > Archiving plans tab.

You can use a saved search query in retention rules or legal hold rules, or run it in the email archive to find the emails that you want to preview or recover.

To create a saved search query

From the email archive
From Management > Archiving plans
Log in to the Cyber Protect console as administrator.
Go to Backup storage > Backups > Cloud application backups.
[To search in an archive in immutable storage] Click Show deleted.
Select an email archive, and then click Browse archive.
[If a privacy warning is shown] In the Privacy warning dialog, click Proceed.
In the Encryption password dialog, specify the password, and then click Proceed.

Select the level at which you want to perform the search.

You can select All emails, a user mailbox, or the Incoming or Outgoing folder in a user mailbox.

To search for the mailbox of a specific user, in the left-column search field, type at least three characters of the user name, and then press Enter.

On the main screen, click Search, specify your search query, and then click Search.

You can use one or more words. To search for a specific phrase, put the phrase in quotation marks. Wildcards are not supported.

The search is performed in the following fields:

From
To
CC
BCC
Subject
Email body

To search only in a specific field, such as From, To/CC/BCC, Subject contains, or to specify additional search criteria, click Filter.

Configure your search criteria.

For example, you can search only for emails that have attachments, or emails that were sent or received on a specific date.

In Deletion status, select the search scope.

Selecting Non-deleted items limits the search only to emails that are not in immutable storage.

Selecting Deleted items limits the search only to emails that are in immutable storage.

Click Apply.
Click Save as.
In the Search query name, specify a name.
Click Save.

As a result, a saved search query is created and is shown in the Saved search queries section. Search results are dynamic and include all new emails that match the query.

The search query is linked to this email archive and can run only on it. Do not use this search query in a retention rule or legal hold rule that you want to apply to another email archive.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.