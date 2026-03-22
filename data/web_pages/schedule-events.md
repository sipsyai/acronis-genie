# Schedule by events

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > Schedule by events
Schedule by events

To configure a backup that runs upon a specific event, select one of the following options.

Option	Description	Examples
Upon time since last backup

A backup starts after a specified period following the last successful backup.

This option depends on how the previous backup completed. If a backup fails, the next backup will not start automatically. In this case, you must run the backup manually and ensure that it completes successfully, in order to reset the schedule.


Run a backup one day after the last successful backup.

Run a backup four hours after the last successful backup.


When a user logs on to the system

A backup starts when a user logs in to the machine.

You can configure this option for any login or for a login of a specific user.

Logging in with a temporary user profile will not start a backup.
Run a backup when user John Doe logs in.
When a user logs off the system

A backup starts when a user logs off the machine.

You can configure this option for any logoff or for the logoff of a specific user.

Logging off from a temporary user profile will not start a backup.

Shutting down a machine will not start a backup.

Run a backup when every user logs off.
On the system startup	A backup runs when the protected machine starts up.	Run a backup when a user starts the machine.
On the system shutdown	A backup runs when the protected machine shuts down.	Run a backup when a user shuts down the machine.
On Windows Event Log event	A backup runs upon a Windows event that you specify.	Run a backup when event 7 of type error and source disk is recorded in the Windows System log.

The availability of these options depends on the backup source and the operating system of the protected workloads. The table below summarizes the available options for Windows, Linux, and macOS.

Event	Backup source (What to back up)
Entire machine, Disks/volumes, or Files/folders (physical machines)	Entire machines or Disk/volumes (virtual machines)	ESXi configuration	Microsoft 365 mailboxes	Exchange databases and mailboxes	SQL databases
Upon time since last backup	Windows, Linux, macOS	Windows, Linux	Windows, Linux	Windows	Windows	Windows
When a user logs on to the system	Windows	N/A	N/A	N/A	N/A	N/A
When a user logs off the system	Windows	N/A	N/A	N/A	N/A	N/A
On the system startup	Windows, Linux, macOS	N/A	N/A	N/A	N/A	N/A
On the system shutdown	Windows	N/A	N/A	N/A	N/A	N/A
On Windows Event Log event	Windows	N/A	N/A	Windows	Windows	Windows
On Windows Event Log event

You can automatically run a backup when a specific event is recorded in a Windows Event log, such as the Application log, Security log, or System log.

You can browse the events and view their properties in Computer Management > Event Viewer in Windows. To open the Security log, you need administrator rights.
Event parameters

The following table summarizes the parameters that you must specify when configuring the On Windows Event Log event option.

Parameter	Description
Log name

The name of the log.

Select the name of a standard log (Application, Security, System) or specify another log name. For example, Microsoft Office Sessions.


Event source

The event source indicates the program or the system component that caused the event. For example, disk.

Any event source that contains the specified text string will trigger the scheduled backup. This option is not case-sensitive. For example, if you specify service, both Service Control Manager and Time-Service event sources will trigger a backup.


Event type	Type of the event: Error, Warning, Information, Audit success, or Audit failure.
Event ID

The event ID identifies a particular kind of event within an event source.

For example, an Error event with event source disk and event ID 7 occurs when Windows discovers a bad block on a disk, while an Error event with event source disk and event ID 15 occurs when a disk is not ready for access.

Example: Emergency backup in case of bad blocks on the hard disk

One or more bad blocks on a hard disk drive might indicate an imminent fail. That is why you might want to create a backup when a bad block is detected.

When Windows detects a bad block on the disk, an error event with the event source disk and event number 7 is recorded to the system log. In the protection plan, configure the following schedule:

Schedule: On Windows Event log event
Log name: System
Event source: disk
Event type: Error
Event ID: 7

To ensure that the backup completes despite the bad blocks, in Backup options, go to Error handling, and then select the Ignore bad sectors check box.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.