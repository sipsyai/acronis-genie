# Recovering databases

Managing the backup and recovery of workloads and files > Protecting MySQL and MariaDB data > Recovering data from an application-aware backup > Recovering databases
Recovering databases

From an application-aware backup, you can recover databases to live MySQL or MariaDB instances.

In the Cyber Protect console, select the machine that originally contained the data that you want to recover.

Click Recovery.

Select a recovery point. Note that recovery points are filtered by location.

If the machine is offline, the recovery points are not displayed. Do one of the following:

If the backup location is cloud or shared storage (that is, other agents can access it), click Select machine, select an online machine that has Agent for MySQL/MariaDB, and then select a recovery point.

Select a recovery point on the Backup storage tab.

The machine chosen for browsing in either of the above actions becomes a target machine for the recovery.

Click Recover > MySQL/MariaDB databases.

Click the name of the desired instance to drill down to its databases.

Select one or more databases that you want to recover.

Click Recover.

Click Target MySQL/MariaDB instance to specify the connection parameters and access credentials for the target instance.

Verify the instance to which you want to recover data. By default, the original instance is selected.

Specify the credentials of a user account that can access the target instance. This user account must have the following privileges assigned for all databases and tables (*.*):
INSERT
CREATE
DROP
LOCK_TABLES
ALTER
SELECT
Click OK.

Verify the target database.

By default, the original database is selected.

To recover a database as a new one, click the name of the target database and change it. This action is only available when you recover a single database.

Under Overwrite existing databases, select the overwriting mode.

By default, overwriting is enabled and the backed-up database will replace the target database that has the same name.

If overwriting is disabled, the backed-up database will be skipped during the recovery operation and will not replace the target database that has the same name.

Click Start recovery.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.