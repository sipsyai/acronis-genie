# Configuring an application-aware backup

Managing the backup and recovery of workloads and files > Protecting MySQL and MariaDB data > Configuring an application-aware backup
Configuring an application-aware backup
Prerequisites
At least one MySQL or MariaDB instance must be running on the selected machine.
On the machine where the MySQL or MariaDB instance is running, the protection agent must be started under the root user.
Application-aware backup is available only when the Entire machine is selected as a backup source in the protection plan.
The Sector-by-sector backup option must be disabled in the protection plan. Otherwise, it is impossible to recover application data.

To configure an application-aware backup

In the Cyber Protect console, select one or more machines on which MySQL or MariaDB instances are running.

You can have one or more instances on each machine.

Create a protection plan with the backup module enabled.

In What to back up, select Entire machine.

Click Application backup, and then enable the switch next to MySQL/MariaDB Server.

Select how to specify the MySQL or MariaDB instances:

For all workloads

Use this option if you run instances with identical configurations on multiple servers. The same connection parameters and access credentials will be used for all instances.


For specific workloads

Use this option to specify the connection parameters and access credentials for each instance.

Click Add instance to configure the connection parameters and access credentials.
Select the connection type, and then specify the following:
[For TCP socket] IP address and port.
[For Unix socket] Socket path.

Specify the credentials of a user account that has the following privileges for the instance:

FLUSH_TABLES OR RELOAD for all databases and tables (*.*)
SELECT for the information_schema.tables
Click OK.
Click Done.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.