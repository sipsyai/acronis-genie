# Task failure handling

Managing the backup and recovery of workloads and files > Backup options > Task failure handling
Task failure handling

This option determines the program behavior when a scheduled execution of a protection plan fails or your machine restarts while a backup is running. This option is not effective when a protection plan is started manually.

If this option is enabled, the program will try to execute the protection plan again. You can specify the number of attempts and the time interval between the attempts. The program stops trying as soon as an attempt completes successfully or the specified number of attempts is performed, depending on which comes first.

If this option is enabled and your machine restarts while a backup is running, the backup operation will not fail. A few minutes after the restart, the backup operation will continue automatically and complete the backup file with the missing data. In this use case, the option Interval between attempts is not relevant.

The preset is: Enabled.

This option is not effective in forensic backups.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.