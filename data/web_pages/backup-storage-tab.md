# Backup storage

Managing the backup and recovery of workloads and files > Operations with backups > Backup storage
Backup storage

The Backup storage tab provides access to all backups, including backups of offline workloads, backups of workloads that are no longer registered in the Cyber Protect console, and backups to public clouds, such as Microsoft Azure.

Backups are organized into backup archives. The archives are named according to the following template:

<workload name> - <protection plan name>

The following archives are orphaned:

Archives that are no longer associated to a protection plan or cloud backup plan.
Archives that are no longer associated to a registered workload.

Orphaned backups use storage space and are billed accordingly.

Backups that are stored in a shared location (such as an SMB or NFS share) are visible to all users who have read permissions for that location. We recommend that you restrict the read permissions for the locations in which you store backups.

We recommend that you use backup replication instead of moving backup files manually.
Do not edit the backup files manually. This might result in file corruption and make the backups unusable. In the Cyber Protect console, corrupted backups are marked as Unknown, and you can only delete them. Recovering data from them might not be possible. For assistance with corrupted backups, contact the Support team.

In the cloud storage, access to backups depends on the user role:

Accounts with the administrator role can access all backups in their tenant or unit.
Accounts with the user role can only access their own backups.

Backup locations that are used in protection plans are automatically added to the Backup storage tab. Cloud-to-cloud backups are shown in Backup storage > Cloud applications backups.

A backup location (except for the cloud storage) disappears from the Backup storage tab if all workloads that are backed up to that location are deleted from the Cyber Protect console. If a new backup to this location occurs, the location is added again with all backups that are stored in it.

You can manually add backup location. For example, a USB memory or external hard disk.

To manually add a backup location

This operation is available only if you have an online agent.
Log in to the Cyber Protect console.
Go to the Backup storage tab, and then click Add location.

Select the location type:

Local folder
Network folder
Secure Zone
NFS folder
Public cloud
Configure the location, and then click Done.

To refresh the backup locations

If you manually added or removed backups, you must refresh the location to sync the change with the Cyber Protect console.

Log in to the Cyber Protect console.
Go to the Backup storage tab, and then select a backup location.
[Not applicable to Cloud application backups] In Machine to browse from, select an online machine.
In the Actions pane, click Refresh.

To filter the backup archives

Log in to the Cyber Protect console.
Go to the Backup storage tab, and then select a backup location.
In the main grid, click the gear icon and enable the columns that you want to see.
To filter the backups, click the column name.

To select a backup (recovery point)

Log in to the Cyber Protect console.

Go to the Backup storage tab, and then select a backup location.

Only backups that you can access are shown.

[Not applicable to Cloud application backups] In Machine to browse from, select an online machine.

Accessing some backups requires a specific agent. For example, to browse backups of SQL databases, you must select a machine that is running Agent for SQL.

The machine with the protection agent (Machine to browse from) is the default recovery destination for backups of physical machines. It you want to recover such a backup to a different machine, select that machine in Machine to browse from.

Select an archive from which you want to recover the data.
Click Show backups.
Select the backup (recovery point).
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.