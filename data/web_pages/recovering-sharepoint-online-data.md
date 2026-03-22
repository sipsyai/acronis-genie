# Recovering SharePoint Online data

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Recovering SharePoint Online data
Recovering SharePoint Online data
Click Microsoft 365.
If multiple Microsoft 365 organizations were added to the Cyber Protection service, select the organization whose backed-up data you want to recover. Otherwise, skip this step.

Do one of the following:

To recover data from a group (modern team) site, expand the Groups node, select All groups, select the group whose site originally contained the items that you want to recover, and then click Recovery.
To recover data from a classic site, expand the Site Collections node, select All site collections, select the site that originally contained the items that you want to recover, and then click Recovery.
If the site was deleted, select it in the Cloud applications backups section of the Backup storage tab, and then click Show backups.

You can search groups and sites by name. Wildcards are not supported.

Select a recovery point.

To see only the recovery points that contain SharePoint sites, select SharePoint sites in Filter by content.

Click Recover SharePoint files.

Browse to the required folder or use search to obtain the list of the required data items.

Select the items that you want to recover.

If the backup is not encrypted, you used search, and selected a single item in the search results, you can click Show versions to select the item version to recover. You can select any backed-up version, earlier or later than the selected recovery point.

To download an item, select the item, click Download, select the location in which you want to save the item, and then click Save.

Click Recover.

If multiple Microsoft 365 organizations were added to the Cyber Protection service, click Microsoft 365 organization to view, change, or specify the target organization.

By default, the original organization is selected. If this organization is no longer registered in the Cyber Protection service, you must specify the target organization.

In Recover to site, view, change, or specify the target site.

You cannot create a new SharePoint site during recovery. To recover a SharePoint site to a new one, first you need to create the target site in the desired Microsoft 365 organization, and then let the cloud agent synchronize the change. The cloud agent automatically synchronizes with Microsoft 365 every 24 hours. To synchronize the change immediately, in the Cyber Protect console, select the organization on the Microsoft 365 page, and then click Refresh.

Select whether to recover the sharing permissions of the recovered items.

Sharing permissions for both internal and external users are recovered.

Click Start recovery.

Select one of the overwriting options:

Option	Description
Overwrite an existing file if it is older	If there is a file with the same name in the destination location, and it is older than the source file, the source file will be saved in the destination location, replacing the older version.
Overwrite existing files	All existing files in the destination location are overwritten, regardless of their last modified date.
Do not overwrite existing files	If there is a file with the same name in the destination location, no changes are applied to it, and the source file is not saved to the destination location.

When you recover OneNote notebooks, both Overwrite an existing file if it is older and Overwrite existing files will result in overwriting the exiting OneNote notebooks.

Click Proceed to confirm your decision.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.