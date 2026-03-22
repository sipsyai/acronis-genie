# Recovering SQL databases as files

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering SQL databases > Recovering SQL databases as files
Recovering SQL databases as files

You can recover databases as files. This option might be useful if you need to extract data for data mining, audit, or further processing by third-party tools. To learn how to attach the SQL database files to a SQL Server instance, refer to Attaching SQL Server databases.

You can recover databases as files to the original machine or to non-original target machines, on which Agent for SQL is installed. When you recover data to non-original machines, the backups must be located on the cloud storage or on a shared storage that the target machine can access.

Recovering databases as files is the only recovery method if you use Agent for VMware (Windows). Recovering databases by using Agent for VMware (Virtual Appliance) is not possible.

To recover SQL databases as files

From a database backup
From an application-aware backup
From a backup on an offline machine

This procedure applies to online source machines.

In the Cyber Protect console, go to Devices > Microsoft SQL.
Select the databases that you want to recover, and then click Recovery.

Select a recovery point.

The recovery points are filtered by location.

Click Recover > Databases as files.

[When recovering to a non-original machine] In Recover to, select the target machine.

This is the machine to which you will recover data. The target machine must be online.

To change the selection, click the machine name, select another machine, and then click OK.

In Path, click Browse, select a local or network folder to save the files to, and then click Done.
Click Start recovery.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.