# Schedule by time

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > Schedule by time
Schedule by time

The following table summarizes the scheduling options that are based on time. The availability of these options depends on the backup scheme. For more information, see Backup schemes.

Option	Description	Examples
Monthly	Select the months, days of the month or days of the week, and then select the backup start time.

Run a backup on January 1, and February 3, at 12:00 AM.

Run a backup on the first day of each month, at 10:00 AM.

Run a backup on March 1, March 5, April 1, and April 5, at 09:00 AM.

Run a backup on the second and third Friday of each month, at 11:00 AM.

Run a backup on the last Wednesday of the month, at 10:30 PM.


Weekly	Select the days of the week, and then select the backup start time.

Run a backup Monday to Friday, at 10:00 AM.

Run a backup on Monday, at 11:00 PM.

Run a backup on Tuesday and Saturday, at 08:00 AM.


Daily	Select the days (everyday or weekdays only), and then select the backup start time.

Run a backup every day, at 11:45 AM.

Run a backup Monday to Friday, at 09:30 PM.


Hourly

Select the days of the week, and then select a time interval between two consecutive backups and the time range within which the backups run.

When you configure the interval in minutes, you can select a suggested interval between 10 and 60 minutes, or specify a custom one, for example, 45 or 75 minutes.



Run a backup every hour between 08:00 AM and 06:00 PM, Monday to Friday.

Run a backup every 3 hours between 01:00 AM and 06:00 PM, on Saturday and Sunday.

Additional options

When you schedule a backup by time, the following additional scheduling options are available.

To access them, in the Schedule pane, click Show more.

If the machine is turned off, run missed tasks at the machine startup

Default setting: Disabled.

Prevent the sleep or hibernate mode during backup

This option is applicable only to machines running Windows.

Default setting: Enabled.

Wake up from the sleep or hibernate mode to start a scheduled backup

This option is applicable only to machines running Windows, in the power plans for which the Allow wake timers option is enabled.

This option does not use the Wake-on-LAN functionality and is not applicable to powered-off machines.

Default setting: Disabled.

See also
Retention rules
Retention rules according to the backup scheme
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.