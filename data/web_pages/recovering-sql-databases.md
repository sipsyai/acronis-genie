# Recovering SQL databases

Managing the backup and recovery of workloads and files > Protecting Microsoft applications > Recovering SQL databases
Recovering SQL databases

You can recover SQL databases from database backups and application-aware backups. For more information about the difference between the two backup types, refer to Protecting Microsoft SQL Server and Microsoft Exchange Server.

You can recover SQL databases to the original instance, to a different instance on the original machine, or to an instance on a non-original machine. When you perform recovery to a non-original machine, Agent for SQL must be installed on the target machine.

Also, you can recover databases as files.

If you use Windows authentication for the SQL instance, you must provide credentials for an account that is a member of the Backup Operators or Administrators group on the machine and a member of the sysadmin role on the target instance. If you use SQL Server authentication, you must provide credentials for an account that is a member of the sysadmin role on the target instance.

System databases are recovered as user databases, with some distinctions. To learn more about these distinctions, refer to Recovering system databases.

During a recovery, you can check the progress of the operation in the Cyber Protect console, on the Monitoring > Activities tab.

Recovering SQL databases to the original machine

Recovering SQL databases to a non-original machine

Recovering SQL databases as files

Recovering system databases

Attaching SQL Server databases




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.