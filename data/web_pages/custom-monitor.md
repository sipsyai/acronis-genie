# Settings of the Custom monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Custom monitor
Settings of the Custom monitor

Custom monitors custom objects via running a script.

If the script was executed, but returned a code different from 0, the system generates an alert.

You can configure the following settings for the monitor.

Setting	Description
Script to run

List of predefined scripts from the script repository.


Schedule

The time when the script is run and, optionally, additional conditions that should be met to run the script.

The following values are available.

Schedule by time — The script will run in the exact time, days, weeks, or months that you specify. This is the default value.

Schedule type — Hourly, Daily, or Monthly

Run within a date range — A time range in which to run the script.

When user logs in to the system — The script will run when a user logs in to the workload.
When user logs off the system — The script will run when a user logs out of the workload.
On the system startup — The script will run when the operating system of the workload starts.
When system is shut down — The script will run when the workload is shut down.
When system goes online — The script will run when the workload becomes available online.

Start conditions — The task will be performed at a specified time or event only if the condition is met. With multiple conditions are selectedl, all of them must be met simultaneously to start the task.

By default, the Prevent the sleep or hibernate mode to start a scheduled task condition is selected.

If start conditions are not met, run the task anyway after — By default, this condition is enabled. The default value is 1 hour.


Account to execute the script

The account on which the script will be run.

The following values are available.

System account — This is the default value.
Currently logged in account

Maximum duration

The maximum period during which the script can run on the workload.

If the script does not complete during this period, the operation will fail.

Enter an integer value in the range 1-1440 (minutes). The default value is 3 minutes.


PowerShell execution policy

The PowerShell execution policy.

The following values are available.

Undefined
AllSigned
Bypass — This is the default value.
RemoteSigned
Restricted
Unrestricted

For more information about these values, see the Microsoft documentation.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.