# Recovering Exchange mailboxes and mailbox items

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering Exchange mailboxes and mailbox items
Recovering Exchange mailboxes and mailbox items

You can recover Exchange mailboxes and mailbox items from the following backups:

Database backups (including DAG backups)
Application-aware backups
Mailbox backups

You can recover the following items:

Mailboxes (except for archive mailboxes)
Public folders
Available only from database backups. See Selecting Exchange Server data.
Public folder items
Email folders
Email messages
Calendar events
Tasks
Contacts
Journal entries
Notes

You can use search to locate the items.

The mailboxes or mailbox items can be recovered to a live Exchange Server or to Microsoft 365.

Recovery to an Exchange Server
Recovery to Microsoft 365

Granular recovery can be performed to Microsoft Exchange Server 2010 Service Pack 1 (SP1) and later. The source backup may contain databases or mailboxes of any supported Exchange version.

Granular recovery can be performed by Agent for Exchange or Agent for VMware (Windows). The target Exchange Server and the machine running the agent must belong to the same Active Directory forest.

When a mailbox is recovered to an existing mailbox, the existing items with matching IDs are overwritten.

Recovery of mailbox items does not overwrite anything. Instead, the full path to a mailbox item is recreated in the target folder.

Requirements on user accounts

A mailbox being recovered from a backup must have an associated user account in Active Directory.

User mailboxes and their contents can be recovered only if their associated user accounts are enabled. Shared, room, and equipment mailboxes can be recovered only if their associated user accounts are disabled.

A mailbox that does not meet the above conditions is skipped during recovery.

If some mailboxes are skipped, the recovery will succeed with warnings. If all mailboxes are skipped, the recovery will fail.

Recovering mailboxes

Recovering mailbox items

Copying Microsoft Exchange Server libraries

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.