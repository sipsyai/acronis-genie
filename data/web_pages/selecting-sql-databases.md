# Selecting SQL databases

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Database backup > Selecting SQL databases
Selecting SQL databases

A backup of an SQL database contains the database files (.mdf, .ndf), log files (.ldf), and other associated files. The files are backed with the help of the SQL Writer service. The service must be running at the time that the Volume Shadow Copy Service (VSS) requests a backup or recovery.

The SQL transaction logs are truncated after each successful backup. SQL log truncation can be disabled in the protection plan options.

To select SQL databases

Click Devices > Microsoft SQL.

The software shows the tree of SQL Server Always On Availability Groups (AAG), machines running Microsoft SQL Server, SQL Server instances, and databases.

Browse to the data that you want to back up.

Expand the tree nodes or double-click items in the list to the right of the tree.

Select the data that you want to back up. You can select AAGs, machines running SQL Server, SQL Server instances, or individual databases.

If you select an AAG, all databases that are included into the selected AAG will be backed up. For more information about backing up AAGs or individual AAG databases, refer to "Protecting Always On Availability Groups (AAG)".
If you select a machine running an SQL Server, all databases that are attached to all SQL Server instances running on the selected machine will be backed up.
If you select a SQL Server instance, all databases that are attached to the selected instance will be backed up.
If you select databases directly, only the selected databases will be backed up.

Click Protect. If prompted, provide credentials to access the SQL Server data.

If you use Windows authentication, the account must be a member of the Backup Operators or Administrators group on the machine and a member of the sysadmin role on each of the instances that you are going to back up.

If you use SQL Server authentication, the account must be a member of the sysadmin role on each of the instances that you are going to back up.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.