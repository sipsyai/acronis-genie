---
title: "Backup schedule, schemes, and types"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup"
page_range: "535-550"
tags: ["backup-schedule", "backup-scheme", "incremental", "differential", "full-backup", "always-incremental", "GFS", "custom-scheme", "schedule-by-time", "schedule-by-event", "start-conditions", "single-file", "tibx"]
acronis_version: "26.02"
---

# Backup schedule, schemes, and types

You can configure a backup to run automatically at a specific time, at specific intervals, or on a specific event. Scheduled backups for non-cloud-to-cloud resources run according to the time zone settings of the workload on which the protection agent is installed.

Scheduling a backup includes:
- Selecting a backup scheme
- Configuring the time or selecting the event that triggers the backup
- Configuring optional settings and start conditions

## Backup schemes

A backup scheme is a part of the protection plan schedule that defines which type of backup (full, differential, or incremental) is created and when. You can select one of the predefined backup schemes or create a custom scheme.

> **Note:** After you create a protection plan, you cannot switch between **Always incremental (single-file)** and the other backup schemes, and vice versa. **Always incremental (single-file)** is a single-file format scheme, and the other schemes are multi-file format. If you want to switch between formats, create a new protection plan.

| Backup scheme | Description | Configurable elements |
|---|---|---|
| **Always incremental (single-file)** | The first backup is full; subsequent backups are incremental and significantly faster. Uses the single-file backup format (.tibx). Recommended when storing backups in the cloud. Default: daily backups, Monday to Friday. | Schedule type (monthly, weekly, daily, hourly), Backup trigger (time or event), Start time, Start conditions, Additional options |
| **Always full** | All backups in the backup set are full. Default: daily backups, Monday to Friday. | Schedule type (monthly, weekly, daily, hourly), Backup trigger (time or event), Start time, Start conditions, Additional options |
| **Weekly full, Daily incremental** | A full backup is created once a week and other backups are incremental. The first backup is full, other backups during the week are incremental, then the cycle repeats. To select the day for the weekly full backup: **Backup options** > **Weekly backup**. Default: daily backups, Monday to Friday. | Backup trigger (time or event), Start time, Start conditions, Additional options |
| **Monthly full, Weekly differential, Daily incremental (GFS)** | Incremental backups are performed daily (Mon-Fri). Differential backups every Saturday. Full backups on the first day of each month. This is a predefined custom scheme shown as **Custom** in the protection plan. | Change existing schedule per backup type (schedule type, trigger, start time, conditions, additional options). Add new schedules per backup type. |
| **Custom** | You must select the backup types (full, differential, and incremental), and configure a separate schedule for each of them. | Change existing schedule per backup type. Add new schedules per backup type. |

### Single-file backup format (.tibx)

The single-file format stores the initial full and subsequent incremental backups in a single .tibx file. The software marks blocks used by outdated backups as "free" and writes new backups to these blocks. This results in extremely fast cleanup with minimal resource consumption. The single-file backup format is not available when backing up to locations that do not support random-access reads and writes.

## Backup types

- **Full** -- contains all source data. Self-sufficient; you do not need access to any other backups to recover data. The first backup created by any protection plan is always a full backup.
- **Incremental** -- stores changes to the data since the latest backup, regardless of whether the latest backup is full, differential, or incremental. To recover data, you need the whole chain of backups on which the incremental backup depends, back to the initial full backup.
- **Differential** -- stores changes to the data since the latest full backup. To recover data, you need both the differential backup and the corresponding full backup.

## Running a backup on a schedule

### To enable a schedule

1. In the protection plan, expand the **Backup** module.
2. Click **Schedule**.
3. Enable the schedule switch.
4. Select the backup scheme.
5. Configure the schedule as required, and then click **Done**.
6. [Optional] Configure start conditions or additional scheduling options.
7. Save the protection plan.

### To disable a schedule

1. In the protection plan, expand the **Backup** module.
2. Click **Schedule**.
3. Disable the schedule switch.
4. Save the protection plan.

> **Note:** If the schedule is disabled, the retention rules are not applied automatically. To apply them, run the backup manually.

## Schedule by time

| Option | Description | Examples |
|---|---|---|
| **Monthly** | Select the months, days of the month or days of the week, and then select the backup start time. | Run a backup on January 1, and February 3, at 12:00 AM. Run on the first day of each month at 10:00 AM. Run on the last Wednesday of the month at 10:30 PM. |
| **Weekly** | Select the days of the week, and then select the backup start time. | Run a backup Monday to Friday at 10:00 AM. Run on Tuesday and Saturday at 08:00 AM. |
| **Daily** | Select the days (everyday or weekdays only), and then select the backup start time. | Run a backup every day at 11:45 AM. Run Monday to Friday at 09:30 PM. |
| **Hourly** | Select the days of the week, time interval between two consecutive backups, and the time range within which backups run. | Run every hour between 08:00 AM and 06:00 PM, Monday to Friday. Run every 3 hours between 01:00 AM and 06:00 PM, on Saturday and Sunday. |

### Additional time-based scheduling options

Access these in the **Schedule** pane by clicking **Show more**:

- **If the machine is turned off, run missed tasks at the machine startup** -- Default: Disabled.
- **Prevent the sleep or hibernate mode during backup** -- Windows only. Default: Enabled.
- **Wake up from the sleep or hibernate mode to start a scheduled backup** -- Windows only, requires **Allow wake timers** enabled in power plans. Default: Disabled. Does not use Wake-on-LAN; not applicable to powered-off machines.

## Schedule by events

| Option | Description | Examples |
|---|---|---|
| **Upon time since last backup** | A backup starts after a specified period following the last successful backup. If a backup fails, the next backup will not start automatically; you must run it manually to reset the schedule. | Run a backup one day after the last successful backup. |
| **When a user logs on to the system** | A backup starts when a user logs in. You can configure for any login or for a specific user. Logging in with a temporary user profile will not start a backup. | Run a backup when user John Doe logs in. |
| **When a user logs off the system** | A backup starts when a user logs off. You can configure for any logoff or for a specific user. Logging off from a temporary user profile will not start a backup. Shutting down a machine will not start a backup. | Run a backup when every user logs off. |
| **On the system startup** | A backup runs when the protected machine starts up. | Run a backup when a user starts the machine. |
| **On the system shutdown** | A backup runs when the protected machine shuts down. | Run a backup when a user shuts down the machine. |
| **On Windows Event Log event** | A backup runs upon a Windows event that you specify. | Run a backup when event 7 of type error and source disk is recorded in the Windows System log. |

### Event availability by backup source and OS

| Event | Physical machines (Win/Linux/macOS) | Virtual machines (Win/Linux) | ESXi config (Win/Linux) | M365 mailboxes (Win) | Exchange DB (Win) | SQL DB (Win) |
|---|---|---|---|---|---|---|
| Upon time since last backup | Win, Linux, macOS | Win, Linux | Win, Linux | Windows | Windows | Windows |
| When a user logs on | Windows | N/A | N/A | N/A | N/A | N/A |
| When a user logs off | Windows | N/A | N/A | N/A | N/A | N/A |
| On system startup | Win, Linux, macOS | N/A | N/A | N/A | N/A | N/A |
| On system shutdown | Windows | N/A | N/A | N/A | N/A | N/A |
| On Windows Event Log event | Windows | N/A | N/A | Windows | Windows | Windows |

### On Windows Event Log event -- parameters

| Parameter | Description |
|---|---|
| **Log name** | The name of the log (Application, Security, System, or specify another). |
| **Event source** | The program or system component that caused the event (e.g., disk). Any event source containing the specified text string will trigger the backup. Not case-sensitive. |
| **Event type** | Type of the event: Error, Warning, Information, Audit success, or Audit failure. |
| **Event ID** | The event ID that identifies a particular kind of event within an event source. For example, event source disk and event ID 7 = bad block detected; event source disk and event ID 15 = disk not ready. |

**Example: Emergency backup on bad blocks**
Configure: Schedule = On Windows Event log event, Log name = System, Event source = disk, Event type = Error, Event ID = 7. Also enable **Ignore bad sectors** in **Backup options** > **Error handling**.

## Start conditions

Start conditions make a backup run only if specific conditions are met. If you configure multiple conditions, all must be met simultaneously. You can specify a period after which the backups will run regardless of whether the conditions are met.

| Start condition | Physical machines (Win/Linux/macOS) | Virtual machines (Win/Linux) | ESXi config (Win/Linux) | M365 (Win) | Exchange DB (Win) | SQL DB (Win) |
|---|---|---|---|---|---|---|
| **User is idle** | Windows | N/A | N/A | N/A | N/A | N/A |
| **Backup location's host is available** | Win, Linux, macOS | Win, Linux | Win, Linux | Windows | Windows | Windows |
| **Users logged off** | Windows | N/A | N/A | N/A | N/A | N/A |
| **Fits the time interval** | Win, Linux, macOS | Win, Linux | N/A | N/A | N/A | N/A |
| **Save battery power** | Windows | N/A | N/A | N/A | N/A | N/A |
| **Do not start when on metered connection** | Windows | N/A | N/A | N/A | N/A | N/A |
| **Do not start on specified Wi-Fi** | Windows | N/A | N/A | N/A | N/A | N/A |
| **Check device IP address** | Windows | N/A | N/A | N/A | N/A | N/A |

### Start condition details

- **User is idle** -- "User is idle" means a screen saver is running or the machine is locked.
- **Backup location's host is available** -- The machine hosting the backup location is available over the network. This condition checks host availability, not the location itself (e.g., if the host is available but the network folder is not shared, the condition is still considered met).
- **Users logged off** -- Postpone a backup until all users log off from a Windows machine.
- **Fits the time interval** -- Restrict a backup start to a specified interval.
- **Save battery power** -- Prevent a backup if a machine is not connected to a power source. Options: "Do not start when on battery" or "Start when on battery if the battery level is higher than" a specified value.
- **Do not start when on metered connection** -- Prevent a backup if connected through a metered connection in Windows. Also automatically enables Wi-Fi network restrictions (default blocked names: android, phone, mobile, modem).
- **Do not start when connected to the following Wi-Fi** -- Prevent backups on specified wireless networks by SSID. Substring matching, not case-sensitive.
- **Check device IP address** -- Prevent a backup if the machine's IP addresses are within or outside a specified IPv4 range. Options: "Start if outside IP range" or "Start if within IP range".

## Additional scheduling options

- **To configure start conditions:** In the **Schedule** pane, click **Show more** and select the conditions.
- **To configure a time range:** Select **Run the plan within a date range** and specify the period.
- **To configure a delay:** In **Backup options** > **Scheduling**, set a random delay (default max: 30 minutes) to avoid excessive network load when backing up multiple workloads to a network location.

## Running a backup manually

You can manually run scheduled and unscheduled backups at any time.
