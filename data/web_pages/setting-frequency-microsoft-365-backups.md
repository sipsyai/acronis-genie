# Setting the frequency of Microsoft 365 backups

Managing the backup and recovery of workloads and files > Protecting Microsoft 365 data > Setting the frequency of Microsoft 365 backups
Setting the frequency of Microsoft 365 backups
This topic applies to Microsoft 365 Business – Backup. With Direct Backup to Microsoft Backup Storage, this functionality is not available.

With the standard included features, Microsoft 365 backups run once a day by default and no additional scheduling options are available.

If the backup functionality is enabled in your tenant, the Once a day option is enabled by default, and more frequencies are available for you to select.

You can select the number of backups per day, but you cannot configure the backup start time. The backups start automatically at approximate intervals that depend on the current load of the cloud agent, which serves multiple customers in a data center. This ensures an even load during the day and equal quality of service for all customers.

The following options are available.

Scheduling options	Approximate interval between each backup
Once a day (default)	24 hours
Twice a day	12 hours
3 times a day	8 hours
6 times a day	4 hours

Depending on the load on the cloud agent and possible throttling on the Microsoft 365 side, a backup might start later than scheduled or take longer to complete. If a backup takes longer that the average interval between two backups, the next backup will be rescheduled, which might result in fewer backups per day than selected. For example, only two backups per day might be able to complete, even though you selected six per day.

Backups of group mailboxes can only run once a day.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.