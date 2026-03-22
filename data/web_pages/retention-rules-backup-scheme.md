# Retention rules according to the backup scheme

Managing the backup and recovery of workloads and files > Retention rules > Retention rules according to the backup scheme
Retention rules according to the backup scheme

The available retention rules and their settings depend on the backup scheme that you use in the protection plan. For more information about the backup schemes, see Backup schemes.

The following table summarizes the available retention rules and their settings.

Backup scheme	Schedule	Available retention rules and settings
Always incremental (single-file)

Monthly

Weekly

Daily

Hourly

Event-triggered backups



By number of backups

By backup age (separate settings for monthly, weekly, daily, and hourly backups)

Keep backups indefinitely


Always full

Monthly

Weekly

Daily

Hourly

Event-triggered backups



By number of backups

By backup age (separate settings for monthly, weekly, daily, and hourly backups)

By total size of backups

Keep backups indefinitely


Weekly full, Daily incremental

Daily

Event-triggered backups



By number of backups

By backup age (separate settings for weekly and daily backups)

By total size of backups

Keep backups indefinitely


Monthly full, Weekly differential, daily incremental

Monthly

Weekly

Daily

Hourly

Event-triggered backups



By number of backups

By backup age (separate settings for full, differential, and incremental backups)

By total size of backups

Keep backups indefinitely


Custom

Monthly

Weekly

Daily

Hourly

Event-triggered backups



By number of backups

By backup age (separate settings for full, differential, and incremental backups)

By total size of backups

Keep backups indefinitely

Why are there monthly backups with an hourly scheme?

Depending on the backup scheme, you can configure the By backup age option for one the following backups:

Monthly, weekly, daily, and hourly backups.

These setting are available with all non-custom backup schemes, and are based on time. All these backups (monthly, weekly, daily, and hourly) are available, even if you configure your backups to run hourly. See the example below.

Backup	Description
Monthly

A monthly backup is the first backup each month.


Weekly

A weekly backup is the first backup on the day of the week that you specify in the Weekly backup option. This day is considered as the beginning of the week in terms of retention rules.

If a weekly backup is also the first backup of the month, it is considered a monthly backup. In this case, a weekly backup is created on the selected day the following week.


Daily

A daily backup is the first backup of the day, unless this backup falls within the definition of a monthly or weekly backup. In this case, a daily backup is created the following day.


Hourly	An hourly backup is the first backup of the hour, unless this backup falls within the definition of a monthly, weekly, or daily backup. In this case, an hourly backup is created the next hour.

Full, differential, and incremental backups.

These setting are available for the Custom backup scheme, and are based on the backup method. The Monthly full, Weekly differential, Daily incremental is a pre-configured custom scheme.

Example

You use the Always incremental (single-file) backup scheme with the default setting for hourly backups:

Scheduled by time.
Backups run hourly: Monday to Friday, every 1 hour, from 08:00 AM to 06:00 PM.
The Weekly backup option is set to Monday.

In the How long to keep section of the protection plan, you can apply retention rules to monthly, weekly, daily, and hourly backups.

The following table summarizes the backup types that are created during an 8-day period.

Date	Day of week	Description
July 1	Monday

The first backup each month is monthly, so the first backup today is a monthly backup. The other backups during the day are hourly.

This week, the first backup is considered a monthly backup. That is why there is no weekly backup. The first backup next week will be a weekly backup.


July 2	Tuesday	The first backup is daily, the other backups during the day are hourly.
July 3	Wednesday	The first backup is daily, the other backups during the day are hourly.
July 4	Thursday	The first backup is daily, the other backups during the day are hourly.
July 5	Friday	The first backup is daily, the other backups during the day are hourly.
July 6	Saturday	The first backup is daily, the other backups during the day are hourly.
July 7	Sunday	The first backup is daily, the other backups during the day are hourly.
July 8	Monday	The first backup is weekly, the other backups during the day are hourly.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.