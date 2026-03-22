# Search in cloud-to-cloud backups

Managing the backup and recovery of workloads and files > Search in cloud-to-cloud backups
Search in cloud-to-cloud backups

When recovering data, you can search for specific backed-up items instead of browsing the backup archive.

Search capabilities depend on the following:

Search type – enhanced (index-based) or typical (non-index based)

The index-based search is faster and provides additional options, such as showing versions of the backed-up items, searching in attachment names, and full-text search in Gmail backups.

Archive type – encrypted or non-encrypted

In non-encrypted backups, search is always available. Only enhanced (index-based) search is supported.

In encrypted backups, enhanced (index-based) search is available as an option.

If you do not enable the enhanced search, basic search will be available for backups of Microsoft 365 mailboxes. For all other workloads, search will not be available. The table below summarizes the available options for encrypted backups.

Workload type	What to recover	Enhanced search is disabled	Enhanced search is enabled
Microsoft 365 workloads
Mailbox	Email messages	Basic (non-index based) search is available	Enhanced (index-based) search is available
OneDrive	Files/folders	Search is not available	Enhanced (index-based) search is available
SharePoint site	SharePoint files	Search is not available	Enhanced (index-based) search is available
Teams	Channels	Search is not available	Enhanced (index-based) search is available
Email messages	Basic (non-index based) search is available	Enhanced (index-based) search is available
Team site	Search is not available	Enhanced (index-based) search is available
Google Workspace workloads
Mailbox	Email messages	Search is not available	Enhanced (index-based) search is available
Google Drive	Files/folders	Search is not available	Enhanced (index-based) search is available
Shared Drives	Files/folders	Search is not available	Enhanced (index-based) search is available
Full-text search

Full-text search is available only for Gmail backups, and it is enabled by default. With it, you can search in the body text of the backed-up emails. If this option is disabled, you can search only by subject, sender, recipient, and date.

A full-text search index takes between 10 and 30 percent of the storage space that is used by the Gmail backup. An index without full-text search data is significantly smaller. To save storage space, you can disable the full-text search and clear the portion of the index that contains the full-text search data.

Search indexes

Checking the size of a search index

Updating, rebuilding, or deleting indexes

Enabling enhanced search in encrypted backups

Disabling full-text search for Gmail backups

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.