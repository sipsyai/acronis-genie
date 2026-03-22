# Recovering SQL databases to the original machine

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering SQL databases > Recovering SQL databases to the original machine
Recovering SQL databases to the original machine

You can recover SQL databases to their original instance, to a different instance on the original machine, or to an instance on a non-original target machine.

To recover SQL databases to the original machine

From a database backup
From an application-aware backup
In the Cyber Protect console, go to Devices > Microsoft SQL.

Select the SQL Server instance or click the instance name to select specific databases that you want to recover, and then click Recovery.

If the machine is offline, the recovery points are not displayed. To recover data to a non-original machine, refer to Recovering SQL databases to a non-original machine.

Select a recovery point.

The recovery points are filtered by location.

Click Recover > Databases to an instance.

By default, the instance and the databases are recovered to the original ones. You can also recover an original database as a new database.

[When recovering to a non-original instance on the same machine] Click Target SQL Server instance, select the target instance, and then click Done.

[When recovering a database as a new database] Click the database name, and then in Recover to, select New database.
Specify the new database name.
Specify the new database path.

Specify the log path.

[Not available when recovering a database as a new database] To change the database state after recovery, click the database name, choose one of the following states, and then click Done.

Ready to use (RESTORE WITH RECOVERY) (default)

After the recovery completes, the database will be ready for use. Users will have full access to it. The software will roll back all uncommitted transactions of the recovered database that are stored in the transaction logs. You will not be able to recover additional transaction logs from the native Microsoft SQL backups.

Non-operational (RESTORE WITH NORECOVERY)

After the recovery completes, the database will be non-operational. Users will have no access to it. The software will keep all uncommitted transactions of the recovered database. You will be able to recover additional transaction logs from the native Microsoft SQL backups and thus reach the necessary recovery point.

Read-only (RESTORE WITH STANDBY)

After the recovery completes, users will have read-only access to the database. The software will undo any uncommitted transactions. However, it will save the undo actions in a temporary standby file so that the recovery effects can be reverted.

This value is primarily used to detect the point in time when a SQL Server error occurred.

Click Start recovery.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.