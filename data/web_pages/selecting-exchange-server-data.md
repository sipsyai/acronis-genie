# Selecting Exchange Server data

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Database backup > Selecting Exchange Server data
Selecting Exchange Server data

The following table summarizes the Microsoft Exchange Server data that you can select for backup and the minimal user rights required to back up the data.

Exchange version	Data items	User rights


2007



Storage groups

Membership in the Exchange Organization Administrators role group


2010/2013/2016/2019



Databases, Database Availability Groups (DAG)

Membership in the Server Management role group.

A full backup contains all of the selected Exchange Server data.

An incremental backup contains the changed blocks of the database files, the checkpoint files, and a small number of the log files that are more recent than the corresponding database checkpoint. Because changes to the database files are included in the backup, there is no need to back up all the transaction log records since the previous backup. Only the log that is more recent than the checkpoint needs to be replayed after a recovery. This makes for faster recovery and ensures successful database backup, even with circular logging enabled.

The transaction log files are truncated after each successful backup.

To select Exchange Server data

Click Devices > Microsoft Exchange.

The software shows the tree of Exchange Server Database Availability Groups (DAG), machines running Microsoft Exchange Server, and Exchange Server databases. If you configured Agent for Exchange as described in Mailbox backup, mailboxes are also shown in this tree.

Browse to the data that you want to back up.

Expand the tree nodes or double-click items in the list to the right of the tree.

Select the data that you want to back up.

If you select a DAG, one copy of each clustered database will be backed up. For more information about backing up DAGs, refer to Protecting Database Availability Groups (DAG).
If you select a machine running Microsoft Exchange Server, all databases that are mounted to the Exchange Server running on the selected machine will be backed up.
If you select databases directly, only the selected databases will be backed up.

If you configured Agent for Exchange as described in Mailbox backup, you can select mailboxes for backup.

If your selection includes multiple databases, they are processed two at a time. When the backup of the first group finishes, the backup of the next group will begin.

If prompted, provide the credentials to access the data.
Click Protect.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.