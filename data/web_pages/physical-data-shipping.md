# Physical Data Shipping

Managing the backup and recovery of workloads and files > Backup options > Physical Data Shipping
Physical Data Shipping

This option is available if the backup or replication destination is the cloud storage and the backup format is set to Version 12.

This option is effective for disk-level backups and file backups created by Agent for Windows, Agent for Linux, Agent for Mac, Agent for VMware, Agent for Hyper-V, and Agent for Virtuozzo.

Use this option to ship the first full backup created by a protection plan to the cloud storage on a hard disk drive by using the Physical Data Shipping service. The subsequent incremental backups are performed over the network.

For local backups that are replicated to cloud, incremental backups continue and are saved locally until the initial backup is uploaded in the cloud storage. Then all incremental changes are replicated to the cloud and the replication continues per the backup schedule.

The preset is: Disabled.

About the Physical Data Shipping service

The Physical Data Shipping service web interface is available only to administrators.

For detailed instructions about using the Physical Data Shipping service and the order creation tool, refer to the Physical Data Shipping Administrator's Guide. To access this document in the Physical Data Shipping service web interface, click the question mark icon.

Overview of the physical data shipping process

[To ship backups that have cloud storage as the primary backup location]

Create a new protection plan with backup to cloud.
In the Backup options row, click Change.
In the list of available options, click Physical Data Shipping.

You can back up directly to a removable drive or back up to a local or a network folder, and then copy/move the backup(s) to the drive.

[To ship local backups that are replicated to cloud]

This option is supported with protection agent version from release C21.06 or later.

Create a new protection plan with backup to a local or network storage.
Click Add location and select Cloud storage.
In the Cloud storage location row, click the gear wheel and select Physical Data Shipping.
Under Use Physical Data Shipping, click Yes and Done.

The Encryption option is enabled automatically in the protection plan because all backups that are shipped must are encrypted.

In the Encryption row, click Specify a password and enter a password for encryption.
In the Physical Data Shipping row, select the removable drive where the initial backup will be saved.
Click Create to save the protection plan.

After the first backup is complete, use the Physical Data Shipping service web interface to download the order creation tool and create the order.

To access this web interface, log in to Management Portal, click Overview > Usage, and then click Manage service under Physical Data Shipping.

Once the initial full backup is done, the subsequent backups must be performed by the same protection plan. Another protection plan, even with the same parameters and for the same machine, will require another Physical Data Shipping cycle.

Package the drives and ship them to the data center.

Ensure that you follow the packaging instructions provided in the Physical Data Shipping Administrator's Guide.

Track the order status by using the Physical Data Shipping service web interface. Note that the subsequent backups will fail until the initial backup is uploaded to the cloud storage.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.