# Protecting SharePoint Online sites

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Protecting SharePoint Online sites
Protecting SharePoint Online sites
What items can be backed up?

You can back up SharePoint classic communication sites and modern team sites. You can select individual subsites, lists, and libraries for backup.

Starting from Cyber Protect Cloud 25.06, unprotected groups that are part of a team are not shown in Devices > Microsoft 365 > Microsoft 365 organization > Groups. You can protect the SharePoint site and group mailbox of these groups by applying a backup plan to the whole team. For more information, see Protecting Microsoft 365 Teams.

A separate option in the backup plan enables the backup of OneNote notebooks.

The following items are skipped during a backup:

The Look and Feel site settings (except for Title, description, and logo).
Site page comments and page comments settings (comments On/Off).
The Site features site settings.
Web part pages and web parts embedded in the wiki pages (due to SharePoint Online API limitations).
Checked out files—files that are manually checked out for editing and all files that are created or uploaded in libraries, for which the option Require Check Out was enabled. To backup these files, first check them in.
External data and Managed Metadata types of columns.
The default site collection "domain-my.sharepoint.com". This is a collection where all of the organization users’ OneDrive files reside.
The contents of the recycle bin.
Limitations
Titles and descriptions of sites/subsites/lists/columns are truncated during a backup if the title/description size is greater than 10,000 bytes.
You cannot back up previous versions of files created in SharePoint Online. Only the latest versions of the files are protected.
You cannot back up the Preservation Hold library.
You cannot back up sites created in the Business Productivity Online Suite (BPOS), the predecessor of Microsoft 365.
You cannot back up the settings for sites that use the managed path /portals (for example, https://<tenant>.sharepoint.com/portals/...).
Information Rights Management (IRM) settings of a list or a library can be recovered only if IRM is enabled in the target Microsoft 365 organization.
What items can be recovered?

The following items can be recovered from a site backup:

Entire site
Subsites
Lists
List items
Document libraries
Documents
List item attachments
Site pages and wiki pages

You can use search to locate the items.

Items can be recovered to the original or a non-original site. The path to a recovered item is the same as the original one. If the path does not exist, it is created.

You can choose whether to recover the sharing permissions or let the items inherit the permissions from the parent object after the recovery.

What items cannot be recovered?
Subsites based on the Visio Process Repository template.
Lists of the following types: Survey list, Task list, Picture library, Links, Calendar, Discussion Board, External, and Import Spreadsheet.
Lists for which multiple content types are enabled.

Selecting SharePoint Online data

Recovering SharePoint Online data

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.