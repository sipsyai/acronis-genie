# Adding the AR_RETENTION_LOCK_SUPPORT variable

Managing the backup and recovery of workloads and files > Supported operating systems and environments for backup and recovery > Compatibility with Dell EMC Data Domain storages > Adding the AR_RETENTION_LOCK_SUPPORT variable
Adding the AR_RETENTION_LOCK_SUPPORT variable

If retention lock is enabled on the Data Domain storage, you must add the AR_RETENTION_LOCK_SUPPORT environment variable to the machine with the protection agent that uses this storage as a backup destination.

To add the AR_RETENTION_LOCK_SUPPORT environment variable

In Windows
In Linux
In a virtual appliance

Log in as administrator to the machine with the protection agent.

In Control Panel, go to System and Security > System > Advanced system settings.

On the Advanced tab, click Environment Variables.

In the System variables panel, click New.

In the New System Variable window, add the new variable as follows:

Variable name: AR_RETENTION_LOCK_SUPPORT

Variable value: 1

Click OK.

In the Environment Variables window, click OK.

Restart the machine.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.