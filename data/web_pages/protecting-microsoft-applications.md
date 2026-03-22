# Protecting Microsoft applications

Managing the backup and recovery of workloads and files > Protecting Microsoft applications
Protecting Microsoft applications
Protecting Microsoft SQL Server and Microsoft Exchange Server
Microsoft SQL backup is supported only for databases running on NFTS, REFS, and FAT32 file systems. ExFat is not supported.

There are two methods of protecting Microsoft applications:

Database backup

This is a file-level backup of the databases and the metadata associated with them. The databases can be recovered to a live application or as files.

Application-aware backup

This is a disk-level backup that also collects the applications' metadata. This metadata enables browsing and recovery of the application data without recovering the entire disk or volume. The disk or volume can also be recovered as a whole. This means that a single solution and a single protection plan can be used for both disaster recovery and data protection purposes.

For Microsoft Exchange Server, you can opt for Mailbox backup. This is a backup of individual mailboxes via the Exchange Web Services protocol. The mailboxes or mailbox items can be recovered to a live Exchange Server or to Microsoft 365. Mailbox backup is supported for Microsoft Exchange Server 2010 Service Pack 1 (SP1) and later.

Protecting Microsoft SharePoint

A Microsoft SharePoint farm consists of front-end servers that run SharePoint services, database servers that run Microsoft SQL Server, and (optionally) application servers that offload some SharePoint services from the front-end servers. Some front-end and application servers may be identical to each other.

To protect an entire SharePoint farm:

Back up all of the database servers with application-aware backup.
Back up all of the unique front-end servers and application servers with usual disk-level backup.

The backups of all servers should be done on the same schedule.

To protect only the content, you can back up the content databases separately.

Protecting a domain controller

A machine running Active Directory Domain Services can be protected by application-aware backup. If a domain contains more than one domain controller, and you recover one of them, a nonauthoritative restore is performed and a USN rollback will not occur after the recovery.

Recovering applications

The following table summarizes the available application recovery methods.

From a database backup	From an application-aware backup	From a disk backup


Microsoft SQL Server



Databases to a live SQL Server instance

Databases as files



Entire machine

Databases to a live SQL Server instance

Databases as files



Entire machine




Microsoft Exchange Server



Databases to a live Exchange

Databases as files

Granular recovery to a live Exchange or to Microsoft 365*



Entire machine

Databases to a live Exchange

Databases as files

Granular recovery to a live Exchange or to Microsoft 365*



Entire machine




Microsoft SharePoint database servers



Databases to a live SQL Server instance

Databases as files

Granular recovery by using SharePoint Explorer



Entire machine

Databases to a live SQL Server instance

Databases as files

Granular recovery by using SharePoint Explorer



Entire machine




Microsoft SharePoint front-end web servers



-



-



Entire machine




Active Directory Domain Services



-



Entire machine



-

* Granular recovery is also available from a mailbox backup. Recovery of Exchange data items to Microsoft 365, and vice versa, is supported on the condition that Agent for Microsoft 365 is installed locally.

Requirements for application-aware backups

Database backup

Application-aware backup

Mailbox backup

Recovering SQL databases

Recovering Exchange databases

Recovering Exchange mailboxes and mailbox items

Changing the SQL Server or Exchange Server access credentials

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.