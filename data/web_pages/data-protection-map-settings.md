# Data protection map settings

Understanding your current level of protection > Monitoring > Smart protection > Data protection map settings
Data protection map settings

To learn how to create a protection plan with the Data protection map module, refer to "Creating a protection plan".

The Data protection map option is disabled by default in newly created protection plans.

The following settings can be specified for the Data protection map module.

Schedule

You can define different settings to create the schedule according to which the task for data protection map will be performed.

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
Extensions and exception rules

On the Extensions tab, you can define the list of file extensions that will be considered as important during data discovery and checked whether they are protected. Use the following format for defining extensions:

.html, .7z, .docx, .zip, .pptx, .xml

On the Exception rules tab, you can define which files and folders not to check on protection status during data discovery.

Hidden files and folders – if selected, hidden files and folders will be skipped during data examination.
System files and folders – if selected, system files and folders will be skipped during data examination.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.