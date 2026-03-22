# Protecting Google Workspace data

Managing the backup and recovery of workloads and files > Protecting Google Workspace data
Protecting Google Workspace data
This feature is not available for tenants in Compliance mode. For more information, see Compliance mode.
What does Google Workspace protection mean?
Cloud-to-cloud backup and recovery of Google Workspace user data (Gmail mailboxes, Calendars, Contacts, Google Drives) and Google Workspace Shared drives.
Granular recovery of emails, files, contacts, and other items.
Support for several Google Workspace organizations and cross-organization recovery.
Optional notarization of the backed-up files by means of the Ethereum blockchain database. When enabled, you can prove that a file is authentic and unchanged since it was backed up.
Optional full-text search. When enabled, you can search emails by their content.
Up to 5,000 items (mailboxes, Google Drives, and Shared drives) per company can be protected without performance degradation.

Backed-up data is automatically compressed and it uses less space on the backup location than on its original location. The compression level for cloud-to-cloud backups is fixed and corresponds to the Normal level of non-cloud-to-cloud backups. For more information about these levels, see Compression level.

Required user rights
In Cyber Protection

In Cyber Protection, you need to be a company administrator acting on a customer tenant level. Company administrators acting on a unit level, unit administrators, and users cannot back up or recover Google Workspace data.

In Google Workspace

To add your Google Workspace organization to the Cyber Protection service, you must be signed in as a Super Admin with enabled API access (Security > API reference > Enable API access in the Google Admin console).

The Super Admin password is not stored anywhere and is not used to perform backup and recovery. Changing this password in Google Workspace does not affect Cyber Protection service operation.

If the Super Admin who added the Google Workspace organization is deleted from Google Workspace or assigned a role with less privileges, the backups will fail with an error like 'Access denied'. In this case, repeat the procedure described in Adding a Google Workspace organization, and specify valid Super Admin credentials. To avoid this case, we recommend that you create a dedicated Super Admin user for backup and recovery purposes.

In order to discover and back up Shared Drives, the Super Admin user should have at least "Google Workspace Business Standard" license assigned.

About the backup schedule

Because the cloud agent serves multiple customers, it determines the start time for each protection plan on its own, to ensure an even load during a day and an equal quality of service for all of the customers.

Each protection plan runs daily at the same time of day.

The default option is Once a day. You can schedule up to six backups per day. The backups start at approximate intervals that depend on the current load of the cloud agent, which serves multiple customers in a data center. This ensures an even load during the day and an equal quality of service for all customers.

Limitations
The Cyber Protect console shows only users who have an assigned Google Workspace license and a mailbox or Google Drive.

Archived or suspended Google Workspace users are shown as inactive (grayed out) in the Cyber Protect console after the discovery operation that follows the change of their status. You cannot apply new backup plans to inactive users. The existing backup plans remain active for 72 hours.

After the discovery operation that follows the 72-hour period, the archived or suspended users are removed from the Cyber Protect console and their data will no longer be backed up. The existing backups remain available.

The backups of deleted Google Workspace user accounts are not automatically deleted from the cloud storage. These backups are billed for the storage space that they use.
Documents in the native Google formats are backed up as generic office documents and are shown with a different extension in the Cyber Protect console – such as .docx or .pptx, for example. The documents are converted back to their original format during recovery.
You can manually run up to 10 backups per hour. For more information, see Running cloud-to-cloud backups manually.
You can simultaneously run up to 10 cloud-to-cloud recovery operations. This number includes both Microsoft 365 and Google Workspace recovery operations.
You cannot simultaneously recover items from different recovering points, even though you can select such items from the search results.
Direct Backup to Public Cloud is not supported.

You can apply only one individual backup plan to a workload.

When an individual backup plan and a group backup plan are applied to the same workload, the settings of the individual plan take precedence.

Actions with cloud-to-cloud resources, such as viewing the content of backed-up emails, downloading attachments or files, recovering emails to non-original mailboxes, or sending them as emails might violate user privacy. These actions are logged in Monitoring > Audit log in Management Portal.

Adding a Google Workspace organization

Creating a personal Google Cloud project

Discovering Google Workspace resources

Setting the frequency of Google Workspace backups

Protecting Gmail data

Protecting Google Drive files

Protecting Shared drive files

Notarization

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.