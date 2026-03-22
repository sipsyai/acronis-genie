# Backup schemes

Managing the backup and recovery of workloads and files > Backup schedule > Backup schemes
Backup schemes

A backup scheme is a part of the protection plan schedule that defines which type of backup (full, differential, or incremental) is created and when. You can select one of the predefined backup schemes or create a custom scheme.

The available backup schemes and types depend on the backup location and source. For example, a differential backup is not available when you back up SQL data, Exchange data, or system state.

Backup scheme	Description	Configurable elements
Always incremental (single-file)

The first backup is full and might be time-consuming. Subsequent backups are incremental and significantly faster.

The backups use the single-file backup format*.

By default, backups are performed on a daily basis, Monday to Friday.

We recommend that you use this scheme when you store your backups in the cloud storage, because incremental backups are fast and involve less network traffic.


Schedule type: monthly, weekly, daily, hourly
Backup trigger: time or event
Start time
Start conditions
Additional options

Always full

All backups in the backup set are full.

By default, backups are performed on a daily basis, Monday to Friday.


Schedule type: monthly, weekly, daily, hourly
Backup trigger: time or event
Start time
Start conditions
Additional options

Weekly full, Daily incremental

A full backup is created once a week and other backups are incremental.

The first backup is full and the other backups during the week are incremental, then the cycle repeats.

To select the day on which the weekly full backup is created, in the protection plan, click the gear icon, and then go to Backup options > Weekly backup.

By default, backups are performed on a daily basis, Monday to Friday.


Backup trigger: time or event
Start time
Start conditions
Additional options

Monthly full, Weekly differential, Daily incremental (GFS)

By default, incremental backups are performed on a daily basis, Monday to Friday. Differential backups are performed every Saturday. Full backups are performed on the first day of each month.

This is a predefined custom scheme. In the protection plan, it is shown as Custom.

Change the existing schedule per backup type:
Schedule type: monthly, weekly, daily, hourly
Backup trigger: time or event
Start time
Start conditions
Additional options
Add new schedules per backup type

Custom	You must select the backup types (full, differential, and incremental), and configure a separate schedule for each of them*.
Change the existing schedule per backup type:
Schedule type: monthly, weekly, daily, hourly
Backup trigger: time or event
Start time
Start conditions
Additional options
Add new schedules per backup type

* After you create a protection plan, you cannot switch between Always incremental (single-file) and the other backup schemes, and vice versa. Always incremental (single-file) is a single-file format scheme, and the other schemes are multi-file format. If you want to switch between formats, create a new protection plan.

See also
Retention rules
Retention rules according to the backup scheme
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.