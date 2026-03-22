# Protecting MySQL and MariaDB data

Managing the backup and recovery of workloads and files > Protecting MySQL and MariaDB data
Protecting MySQL and MariaDB data

You can protect MySQL or MariaDB data with application-aware backup. It collects application metadata and allows granular recovery on the instance, database, or table level.

To protect a physical or virtual machine that runs MySQL or MariaDB instances with application-aware backup, you need to install Agent for MySQL/MariaDB on this machine. Agent for MySQL/MariaDB is bundled with Agent for Linux (64-bit) and therefore can be installed only on 64-bit Linux-based operating systems. See Supported operating systems and environments for backup and recovery.

To download the Agent for Linux (64-bit) installation file

Log in to the Cyber Protect console.
Click the account icon in the upper-right corner, and then select Downloads.
Click Agent for Linux (64-bit).

The installation file is downloaded to your machine. To install the agent, proceed as described in Installing protection agents in Linux or Installing and uninstalling protection agents in Linux. Ensure that you select Agent for MySQL/MariaDB, which is an optional component.

To recover databases and tables to a live instance, Agent for MySQL/MariaDB needs a temporary storage to operate. By default, the /tmp directory is used. You can change this directory by setting the ACRONIS_MYSQL_RESTORE_DIR environment variable.

Limitations
MySQL or MariaDB clusters are not supported.
MySQL or MariaDB instances running in Docker containers are not supported.
MySQL or MariaDB instances running on operating systems that use BTRFS file system are not supported.

System databases (sys, mysql, information-schema, and performance_schema) and databases that do not contain any tables cannot be recovered to live instances. However, these databases can be recovered as files, when recovering the whole instance.

Recovery is supported only to target instances of the same version as the backed-up instance or later, with the following restrictions:
Recovery from MySQL 5.x instances to MySQL 8.x instances is not supported.

Recovery to a later MySQL 5.x version (including the minor versions) is supported only via recovery of the whole instance as files. Before attempting recovery, consult the official MySQL upgrade guide for the target version, for example, the MySQL 5.7 upgrade guide.

Recovery from backups stored on Secure Zone is not supported.

Databases and tables cannot be recovered by Agent for MySQL/MariaDB that is running on a machine on which AppArmor is installed. You can still recover an instance as files, or the entire machine.
Recovery to target databases that are configured with symbolic links is not supported. You can recover the backed-up databases as new databases, by changing their name.
Known issues

If you encounter issues while recovering data from password protected Samba shares, log out from the Cyber Protect console, and then log in back to it. Select the desired recovery point, and then click MySQL/MariaDB databases. Do not click Entire machine or Files/folders.

Configuring an application-aware backup

Recovering data from an application-aware backup

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.