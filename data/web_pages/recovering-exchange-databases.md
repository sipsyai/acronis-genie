# Recovering Exchange databases

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering Exchange databases
Recovering Exchange databases

This section describes recovery from both database backups and application-aware backups.

You can recover Exchange Server data to a live Exchange Server. This may be the original Exchange Server or an Exchange Server of the same version running on the machine with the same fully qualified domain name (FQDN). Agent for Exchange must be installed on the target machine.

The following table summarizes the Exchange Server data that you can select for recovery and the minimal user rights required to recover the data.

Exchange version	Data items	User rights


2007



Storage groups

Membership in the Exchange Organization Administrators role group.


2010/2013/2016/2019



Databases

Membership in the Server Management role group.

Alternatively, you can recover the databases (storage groups) as files. The database files, along with transaction log files, will be extracted from the backup to a folder that you specify. This can be useful if you need to extract data for an audit or further processing by third-party tools, or when the recovery fails for some reason and you are looking for a workaround to mount the databases manually.

If you use only Agent for VMware (Windows), recovering databases as files is the only available recovery method. Recovering databases by using Agent for VMware (Virtual Appliance) is not possible.

We will refer to both databases and storage groups as "databases" throughout the below procedures.

To recover Exchange databases to a live Exchange Server

Do one of the following:

When recovering from an application-aware backup, under Devices, select the machine that originally contained the data that you want to recover.
When recovering from a database backup, click Devices > Microsoft Exchange > Databases, and then select the databases that you want to recover.
Click Recovery.

Select a recovery point. Note that recovery points are filtered by location.

If the machine is offline, the recovery points are not displayed. Do one of the following:

[Only when recovering from an application-aware backup] If the backup location is cloud or shared storage (i.e. other agents can access it), click Select machine, select an online machine that has Agent for Exchange, and then select a recovery point.
Select a recovery point on the Backup storage tab.

The machine chosen for browsing in either of the above actions becomes a target machine for the Exchange data recovery.

Do one of the following:

When recovering from an application-aware backup, click Recover > Exchange databases, select the databases that you want to recover, and then click Recover.
When recovering from a database backup, click Recover > Databases to an Exchange server.

By default, the databases are recovered to the original ones. If the original database does not exist, it will be recreated.

To recover a database as a different one:

Click the database name.
In Recover to, select New database.
Specify the new database name.
Specify the new database path and log path. The folder you specify must not contain the original database and log files.
Click Start recovery.

The recovery progress is shown on the Activities tab.

To recover Exchange databases as files

Do one of the following:

When recovering from an application-aware backup, under Devices, select the machine that originally contained the data that you want to recover.
When recovering from a database backup, click Devices > Microsoft Exchange > Databases, and then select the databases that you want to recover.
Click Recovery.

Select a recovery point. Note that recovery points are filtered by location.

If the machine is offline, the recovery points are not displayed. Do one of the following:

[Only when recovering from an application-aware backup] If the backup location is cloud or shared storage (i.e. other agents can access it), click Select machine, select an online machine that has Agent for Exchange or Agent for VMware, and then select a recovery point.
Select a recovery point on the Backup storage tab.

The machine chosen for browsing in either of the above actions becomes a target machine for the Exchange data recovery.

Do one of the following:

When recovering from an application-aware backup, click Recover > Exchange databases, select the databases that you want to recover, and then click Recover as files.
When recovering from a database backup, click Recover > Databases as files.
Click Browse, and then select a local or a network folder to save the files to.
Click Start recovery.

The recovery progress is shown on the Activities tab.

Mounting Exchange Server databases

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.