# Required User Rights M365 Backup

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Required user rights
Required user rights
This topic applies to Microsoft 365 Business – Backup and Direct Backup to Microsoft Backup Storage.

Using the cloud agent requires the following user rights in Cyber Protect Cloud and in Microsoft 365.

In Cyber Protect Cloud
With Microsoft 365 Business – Backup, the cloud agent can be used both on the customer tenant level and on a unit level. For more information about these levels and their respective administrators, see Administering Microsoft 365 organizations added on different levels.
With Direct Backup to Microsoft 365 Backup Storage, the cloud agent can be used on the customer-tenant level.
The local agent must be registered under a company administrator account and used on the customer tenant level. Company administrators acting on the unit level, unit administrators, and users cannot back up or recover Microsoft 365 data.
In Microsoft 365
Your account must be assigned the global administrator role in Microsoft 365.
To discover, back up, and recover Microsoft 365 public folders, at least one of your Microsoft 365 administrator accounts must have a mailbox and read/write rights to the public folders that you want to back up.
The local agent will log in to Microsoft 365 by using this account. To enable the agent to access the contents of all mailboxes, this account will be assigned the ApplicationImpersonation management role. If you change the account password, update the password in the Cyber Protect console, as described in Changing the Microsoft 365 access credentials.

The cloud agent does not log in to Microsoft 365. To grant the cloud agent the permissions that are required for its operation, you must log in to Microsoft 365 as a global administrator.

The following table summarizes the required permissions.

Microsoft 365 Business – Backup	Direct Backup to Microsoft 365 Backup Storage

Sign in and read user profile
Read and write files in all site collections
Read and write all users' full profiles
Read and write all groups
Read directory data
Read all channel messages
Read and write managed metadata
Read and write items and lists in all site collections
Have full control of all site collections
Use Exchange Web Services with full access to all mailboxes

Use Exchange Web Services with full access to all mailboxes
Read and write items in all site collections
Read and write items and lists in all site collections
Have full control of all site collections
Read all backup configuration policies
Read and edit all backup configuration policies
Read all restore sessions
Read restore all sessions and start restore sessions from backups
Read all monitoring, quota, and billing information for the tenant
Search for metadata properties in all backup snapshots
Update or read the status of the M365 backup service
Read the status of the M365 backup service
Read all users' full profiles
Read organization information
Update or read the status of the M365 backup service
Sign in and read user profile
Read and write all users' full profiles
Read files in all site collections
Read all groups
Read directory data

The cloud agent does not store your account credentials and does not use them to perform backup and recovery. Changing the credentials, disabling the account, or deleting the account does not affect the operation of the cloud agent.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.