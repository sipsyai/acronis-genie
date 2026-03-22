# Recovering SQL databases to a non-original machine

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering SQL databases > Recovering SQL databases to a non-original machine
Recovering SQL databases to a non-original machine

You can recover both application-aware backups and database backups to SQL Server instances on non-original target machines on which Agent for SQL is installed. The backups must be located on the cloud storage or on a shared storage that the target machine can access.

The SQL Server version on the target machine must be the same as the version on the source machine, or newer.

To recover SQL databases to a non-original machine

From Backup storage
From Devices

This procedure applies to application-aware backups and database backups.

In the Cyber Protect console, go to Backup storage.

Select the location of the backup set from which you want to recover data.

In Machine to browse from, select the target machine.

This is the machine to which you will recover data. The target machine must be online.

Select the backup set, and then in the Actions pane, click Show backups.

Application-aware backup sets and database backup sets have different icons.

Select the recovery point from which you want to recover data.

[For database backups] Click Recover SQL databases.

[For application-aware backups] Click Recover > SQL databases.

Select the SQL Server instance or click the instance name to select specific databases that you want to recover, and then click Recover.

[If there is more than one SQL instance on the target machine] Click Target SQL Server instance, select the target instance, and then click Done.

Click the database name, specify the new database path and log path, and then click Done.

You can specify the same path in both fields, for example:

C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\
Click Start recovery.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.