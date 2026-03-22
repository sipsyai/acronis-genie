# Protecting OneNote notebooks

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Microsoft 365 Business – Backup > Protecting OneNote notebooks
Protecting OneNote notebooks

By default, OneNote notebooks are included in the backups of OneDrive files, Microsoft Teams, and SharePoint sites.

To exclude the OneNote notebooks from these backups, disable the Include OneNote switch in the respective backup plan.

Recovering backed-up OneNote notebooks

To learn how to recover a backed-up OneNote notebook, refer to the respective topic:

For OneDrive backups, see Recovering an entire OneDrive or Recovering OneDrive files.
For Teams backups, see Recovering an entire team, Recovering team channels or files in team channels or Recovering a team site or specific items of a site.
For SharePoint site backups, see Recovering SharePoint Online data.
Supported versions
OneNote (OneNote 2016 and later)
OneNote for Windows 10
Limitations and known issues
OneNote notebooks saved in OneDrive or SharePoint are limited to 2 GB. You cannot recover larger OneNote notebooks to OneDrive or SharePoint targets.
OneNote notebooks with section groups are not supported.
In backed-up OneNote notebooks that contain sections with non-default names, the first section is shown with the default name (such as New section or Untitled section). This might affect the section order in notebooks with multiple sections.

When you recover OneNote notebooks, both of the options Overwrite existing content if it is older and Overwrite existing content will result in overwriting the exiting OneNote notebooks.

When you recover an entire team, a team site, or the Site Assets folder of a team site, and you selected the Overwrite existing content if it is older or the Overwrite existing content option, the default OneNote notebook of that team will not be overwritten. The recovery succeeds with the warning Failed to update the properties of file '/sites/<Team name>/SiteAssets/<OneNote notebook name>'.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.