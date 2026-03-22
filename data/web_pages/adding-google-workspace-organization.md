# Adding a Google Workspace organization

Managing the backup and recovery of workloads and files > Protecting Google Workspace data > Adding a Google Workspace organization
Adding a Google Workspace organization

To add a Google Workspace organization to the Cyber Protection service, you need a dedicated personal Google Cloud project. For more information about how to create and configure such a project, refer to Creating a personal Google Cloud project.

To add a Google Workspace organization by using a dedicated personal Google Cloud project

Log in to the Cyber Protect console as a company administrator.
Click Devices > Add > Google Workspace.
Enter the email address of a Super Administrator of your Google Workspace account.

For this procedure, it is irrelevant whether 2-Step Verification is enabled for the Super Administrator email account.

Browse for the JSON file that contains the private key of the service account that you created in your Google Cloud project.

You can also paste the file content as text.

Click Confirm.

As a result, your Google Workspace organization appears under the Devices tab in the Cyber Protect console.

Useful tips
After adding a Google Workspace organization, the user data and Shared drives in both the primary domain and all the secondary domains, if there are any, will be backed up. The backed-up resources will be displayed in one list, and will not be grouped by their domain.

The cloud agent synchronizes with Google Workspace every 24 hours, starting from the moment when the organization is added to the Cyber Protection service. If you add or remove a user or Shared drive, you will not see this change in the Cyber Protect console immediately. To synchronize the change immediately, select the organization on the Google Workspace page, and then click Refresh.

For more information about synchronizing the resources of a Google Workspace organization and the Cyber Protect console, refer to Discovering Google Workspace resources.

If you applied a protection plan to the All users or All Shared drives group, the newly added items will be included in the backup only after the synchronization.

According to Google policy, when a user or Shared drive is removed from the Google Workspace graphical user interface, it remains available via an API for a few days. During this period, the removed item is inactive (grayed out) in the Cyber Protect console and is not backed up. When the removed item becomes unavailable via the API, it disappears from the Cyber Protect console. Its backups (if any) can be found at Backup storage > Cloud applications backups.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.