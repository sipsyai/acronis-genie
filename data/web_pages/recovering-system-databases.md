# Recovering system databases

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering SQL databases > Recovering system databases
Recovering system databases

All system databases of an instance are recovered at once. When recovering system databases, the software automatically restarts the destination instance in the single-user mode. After the recovery completes, the software restarts the instance and recovers other databases (if any).

Other things to consider when recovering system databases:

System databases can only be recovered to an instance of the same version as the original instance.
System databases are always recovered in the "ready to use" state.
Recovering the master database

System databases include the master database. The master database records information about all databases of the instance. Hence, the master database in a backup contains information about databases which existed in the instance at the time of the backup. After recovering the master database, you may need to do the following:

Databases that have appeared in the instance after the backup was done are not visible by the instance. To bring these databases back to production, attach them to the instance manually by using SQL Server Management Studio.
Databases that have been deleted after the backup was done are displayed as offline in the instance. Delete these databases by using SQL Server Management Studio.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.