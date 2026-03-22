# Recovering instances

Managing the backup and recovery of workloads and files > Protecting MySQL and MariaDB data > Recovering data from an application-aware backup > Recovering instances
Recovering instances

From an application-aware backup, you can recover MySQL or MariaDB instances as files.

To recover an instance

In the Cyber Protect console, select the machine that originally contained the data that you want to recover.

Click Recovery.

Select a recovery point. Note that recovery points are filtered by location.

If the machine is offline, the recovery points are not displayed. Do one of the following:

If the backup location is cloud or shared storage (that is, other agents can access it), click Select machine, select an online machine that has Agent for MySQL/MariaDB, and then select a recovery point.

Select a recovery point on the Backup storage tab.

The machine chosen for browsing in either of the above actions becomes a target machine for the recovery.

Click Recover > MySQL/MariaDB databases.

Select the instance that you want to recover, and then click Recover as files.

Under Path, select the directory to which the files will be recovered.

Click Start recovery.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.