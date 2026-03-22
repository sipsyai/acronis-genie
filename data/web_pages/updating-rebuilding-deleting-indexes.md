# Updating, rebuilding, or deleting indexes

Managing the backup and recovery of workloads and files > Search in cloud-to-cloud backups > Updating, rebuilding, or deleting indexes
Updating, rebuilding, or deleting indexes

To troubleshoot search-related issues in cloud-to-cloud backups, you can update, rebuild, or delete search indexes.

Operations with indexes are not supported in encrypted backups.

These operations might be time-consuming and are only available to administrators, as follows:

Tenant type	Role	Can update index	Can rebuild index	Can delete index
Partner tenant	Company administrator

+

+	+
Protection cyber administrator

+

-	-


Protection administrator



+

-	-


Protection read-only administrator

-	-	-
Customer tenant

Company administrator

+	-	-


Protection administrator

+	-	-
Protection read-only administrator	-	-	-
Unit	Unit administrator	+	-	-
Protection administrator	+	-	-
Protection read-only administrator	-	-	-

To update, rebuild, or delete an index

Log in to the Cyber Protect console as an administrator.
On the Backup storage tab, click Cloud applications backup.
Select the archive for which you want to update, rebuild, or delete the index.

In the Actions pane, select the action that you want to perform:

Update index—the recovery points in the archive are checked, and the missing indexes are added.
Rebuild index—the indexes for all recovery points in the archive are deleted, and then the indexes are created again.
Delete index—the indexes for all recovery points in the archive are deleted.

Select the scope of the action, and then click OK.

Depending on the archive and the selected action, one or more of the following options are available:

Metadata only
Content only
Metadata and content search
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.