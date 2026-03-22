# Schedule scan

Configuring your antivirus and antimalware protection > Antivirus and antimalware protection > Antivirus and antimalware protection settings > Schedule scan
Schedule scan

On-demand scanning checks your computer system for viruses according to the specified schedule. A full scan checks all the files on your machine, while a quick scan checks only the machine system files.

To configure Schedule scan

Default settings:

Custom scan is disabled.
Quick and Full scan are scheduled.
In the Create protection plan window, expand the Antivirus & Antimalware protection module.
Click Schedule scan.
Use the toggle to enable the type of scan that you want to apply for your machine.

Available types of scan:

Full — takes much longer to finish in comparison to the quick scan because every file will be checked.

Quick — only scans the common areas where malware normally resides on the machine.

Custom — Checks the files/folders that were selected by the administrator of the Protection plan.

You can schedule all three scans - Quick, Full, and Custom - in one protection plan.

To configure custom scan

Use the Custom scan toggle to enable or disable this type of scan.
In the Action on detection drop-down list, select one of the available options:

Default setting: Quarantine

Quarantine

The software generates an alert and moves the executable file to the quarantine folder.

Notify only

The software generates an alert about the process that is suspected to be malware.

Field	Description
Schedule the task run using the following events

This setting defines when the task will run.

The following values are available:

Schedule by time – This is the default setting. The task will run according to the specified time.
When user logs in to the system – By default, a login of any user will trigger the task. You can modify this setting so that only a specific user account can trigger the task.

When user logs off the system – By default, a logoff of any user will trigger the task. You can modify this setting so that only a specific user account can trigger the task.

The task will not run at system shutdown. Shutting down and logging off are different events in the scheduling configuration.

On the system startup – The task will run when the operating system starts.
On the system shutdown – The task will run when the operating system shuts down.

Schedule type

The field appears if in Schedule the task run using the following events you have selected Schedule by time.

The following values are available:

Monthly – Select the months and the weeks or days of the month when the task will run.
Daily – This is the default setting. Select the days of the week when the task will run.
Hourly – Select the days of the week, repetition number, and the time interval in which the task will run.

Start at

The field appears if in Schedule the task run using the following events you have selected Schedule by time

Select the exact time when the task will run.


Run within a date range

The field appears if, in Schedule the task run using the following events, you have selected Schedule by time.

Set a range in which the configured schedule will be effective.


Specify a user account whose login to the operating system will initiate a task

The field appears if, in Schedule the task run using the following events, you have selected When user logs in to the system.

The following values are available:

Any user - Use this option if you want the login of any user to trigger the task.
The following user - Use this option if you want only the login of a specific user account to trigger the task.

Specify a user account whose logout from the operating system will initiate a task

The field appears if, in Schedule the task run using the following events, you have selected When user logs off the system.

The following values are available:

Any user - Use this option if you want the logout of any user to trigger the task.
The following user - Use this option if you want only the logout of a specific user account to trigger the task.

Start conditions

Defines all conditions that must be met simultaneously for the task to run.

Start conditions for antimalware scans are similar to the start conditions for the Backup module that are described in "Start conditions".

You can define the following additional start conditions:

Distribute task start time within a time window – This option allows you to set the time frame for the task in order to avoid network bottlenecks. You can specify the delay in hours or minutes. For example, if the default start time is 10:00 AM and the delay is 60 minutes, then the task will start between 10:00 AM and 11:00 AM.
If the machine is turned off, run missed tasks at the machine startup
Prevent the sleep or hibernate mode during task running – This option is effective only for machines running Windows.
If start conditions are not met, run the task anyway after – Specify the period after which the task will run, regardless of the other start conditions.
Start conditions are not supported for Linux.
Select the Scan only new and changed files check box if you want to scan only newly created and modified files.

Default setting: Enabled

Two additional options displayed for Custom scan for Full scan only:
Scan archive files

Default setting: Enabled.

Max recursion depth

Default setting: 16

How many levels of embedded archives can be scanned. For example, MIME document > ZIP archive > Office archive > document content.

Max size

Default setting: 100

Maximum size of an archive file to be scanned.

Scan removable drives

Default setting: Disabled

Mapped (remote) network drives
USB storage devices (such as pens and external hard drives)
CDs/DVDs
Scan removable drives is not supported for Linux.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.