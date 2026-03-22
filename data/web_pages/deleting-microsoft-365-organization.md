# Deleting a Microsoft 365 organization

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Deleting a Microsoft 365 organization
Deleting a Microsoft 365 organization
This topic applies to Microsoft 365 Business – Backup and Direct Backup to Microsoft Backup Storage.

Deleting a Microsoft 365 organization does not affect the existing backups of this organization's data. If you do not need these backups anymore, delete them first, and then delete the Microsoft 365 organization. Otherwise, the backups will still use cloud storage space that might be billed. For more information about how to delete backups, see To delete backups or backup archives.

To delete a Microsoft 365 organization

[To delete a Microsoft 365 organization on a customer tenant level] Log in to the Cyber Protect console an administrator.

[To delete a Microsoft 365 organization on a unit level] Depending on your role, do the following:

[For unit administrators] Log in to the Cyber Protect console a unit administrator.

[For company administrators acting on the unit level] Navigate to the unit in which the organization is added.

Go to Devices, and then select the backup solution that this organization uses:

Microsoft 365 Business – Backup
Direct Backup for Microsoft 365
Select the organization, and then click Delete.

As a result, the backup plans applied to this organization will be revoked and the workloads in it will become unprotected.

Next, revoke the access rights that are granted to the Backup Service application. For more information, see Revoking access rights of the Backup Service application.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.