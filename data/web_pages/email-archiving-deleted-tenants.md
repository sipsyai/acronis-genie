# Email archiving in disabled or deleted tenants

Managing the backup and recovery of workloads and files > Email archiving > Configuring email archiving > Email archiving in disabled or deleted tenants
Email archiving in disabled or deleted tenants

Email archiving is not active in the following types of tenants:

Disabled

You can re-enable a disabled tenant.

Soft-deleted (within 30 days of deletion)

You can recover a deleted tenant within 30 days of its deletion.

Hard-deleted (more than 30 days of deletion)

You cannot recover a tenant if it was deleted more than 30 days ago.

The table below summarizes the product behavior.

Tenant type


Disabled or deleted (soft delete)



Re-enabled or recovered

Deleted (hard delete)

Discovery operations do not run.
New incoming and outgoing emails are not added to the email archive.
Retention rules are not applied.
Legal hold rules are not applied.
Indexing operations do not run.

Discovery operations run again.
New incoming and outgoing emails are added to the email archive.

Metadata of the Microsoft 365 seats is updated. For example, changes of the email address of the users.

The emails from the period when the tenant was disabled or deleted are imported to the email, according to the configuration of the archiving plan. For example, email from all mailboxes or emails from selected mailboxes.
Retention rules are applied.
Legal hold rules are applied.
Indexing operations run again.


All data of the tenant, including the email archive, is permanently deleted.

This action is irreversible.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.