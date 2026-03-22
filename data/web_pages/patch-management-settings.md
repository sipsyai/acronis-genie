# Patch management settings in the protection plan

RMM > Managing software > Assessing vulnerabilities and managing patches > Patch management settings in the protection plan
Patch management settings in the protection plan

In the Patch management module of the protection plan, you can configure the following patch management settings:

What updates to install for Microsoft and third-party products for Windows OS.
When to run the automatic patch installation.
Whether to run a pre-update backup.

For more information about creating a protection plan and enabling the Patch management module, see Creating a protection plan.

The availability of this feature depends on the service quotas that are enabled for your account.
Microsoft products

To install the Microsoft updates on the selected machines

Enable the Update Microsoft products option in the protection plan.

Select the installation option:

Option	Description
All updates	Use this option if you want to install all approved updates.
Only Security and Critical updates	Use this option if you want to install all approved security and critical updates.
Updates of specific products (Automatic patch approval and testing)

Use this option if you want to define custom settings for different products.

If you want to update specific products, for each product you can define which updates to install by category, severity, or approval status.

If you want to configure automatic test approval and testing of the patches, select this option.

The patch management feature supports upgrades to Windows 11. However, you must verify that the Windows 10 workloads that you are planning to upgrade are properly prepared for it. See this Microsoft article for details.

For Microsoft products, patch distribution uses the Windows API service. Patches and updates are not downloaded or stored internally or on distribution agents. Instead, they are downloaded from Microsoft CDN. Thus, even with the Updater role assigned, the agent cannot download and distribute patches.

Windows third-party products

The availability of this feature depends on the license that you have.

To install the third-party updates for Windows OS on the selected machines

Enable the Windows third-party products option in the protection plan.

Select the installation options:

Option	Description
All updates	Use this option if you want to install all approved updates. *
Only major updates	Use this option if you want to install all approved major updates.
Only minor updates	Use this option if you want to install approved minor updates.
Updates of specific products (Automatic patch approval and testing)

Use this option if you want to define custom settings for different products.

If you want to update specific products then, for each product, you can define which updates to install by category, severity, or approval status.

If you want to configure automatic test approval and testing of the patches, select this option.


Install the latest versions only for applications with detected vulnerabilities	Select this check box if you want to install the latest updates only for applications that have detected vulnerabilities.

For Windows third party products, patches are distributed directly to managed workloads when internet access is available. If internet access is not available for all workloads, the Updater role should be assigned to an agent that does have internet access. This agent will then download the patches and distribute them to other agents on the network.

Schedule

Define the schedule and conditions according to which the updates will be installed on the selected machines.

Field	Description
Schedule the task run using the following events

This setting defines when the task will be run.

The following values are available:

Schedule by time – This is the default setting. The task will run according to the specified time.
When user logs in to the system – By default, a login of any user will start the task. You can modify this setting so that only a specific user account can trigger the task.

When user logs off the system – By default, a logoff of any user will start the task. You can modify this setting so that only a specific user account can trigger the task.

The task will not run at system shutdown. Shutting down and logging off are different events in the scheduling configuration.

On the system startup – The task will run when the operating system starts.
On the system shutdown – The task will run when the operating system shuts down.

Schedule type

The field appears if, in Schedule the task run using the following events, you have selected Schedule by time.

The following values are available:

Monthly – Select the months and the weeks or days of the month when the task will run.
Daily – This is the default setting. Select the days of the week when the task will run.
Hourly – Select the days of the week, repetition number, and the time interval in which the task will run.

Start at

The field appears if, in Schedule the task run using the following events, you have selected Schedule by time

Select the exact time when the task will run.


Configure maintenance window for patches

The field appears if, in Schedule the task run using the following events, you have selected Schedule by time.

Select this setting if you want the patch installation to run only during the time interval that you will specify. If the patch installation process has not completed by the end time defined by the maintenance window for patches, it will be stopped automatically.


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
Restart options

Configure if you want the workloads to be restarted after the patches installation.

The following table provides more information about the restart options.

Option	Description
Restart if required	If you want the workload to be restarted after the software is installed or uninstalled only if the software requires it, select this checkbox.
Always restart

If you want the workload to always be restarted after the software is installed or uninstalled, select this checkbox.


Do not restart

If you do not want the workload to be restarted after the software is installed or uninstalled, select this checkbox.


Schedule automatic restart

This option is available if you selected Restart if required or Always restart.

The option enables automatic restart of the workload.


If a user is logged on to the device, the device will be automatically restarted after:

This option is available if you selected Schedule automatic restart.

Select the period after which the workload will be restarted automatically. The user who is logged in to the workload will be notified about a pending automatic restart and the time when it will happen. Thus, users can save their work and prepare for the restart.


Additional notifications

This option is available if you selected Schedule automatic restart.

Select this option if you want the user who is logged in to the workload to be reminded repeatedly about a pending restart before the selected period passes.

The timing of notifications depends on the selected period and transitions into a countdown as the restart time nears. This ensures that users stay informed and prepared for the restart. Notifications are triggered by a successful software update or deployment and are sent at the following times.

The timing of the first notification coincides with the selected period.

24 h before the automatic restart.
8 h before the automatic restart.
4 h before the automatic restart.
1 h before the automatic restart.
30 min before restart.
15 min before restart.
5 min before the automatic restart. The last user notification cannot be closed or dismissed.

If no user is logged on to the device, restart it immediately

This option is available if you selected Schedule automatic restart.

If you select this option and no user is logged in to the workload, the workload will be restarted immediately, without waiting for the selected period before automatic restart to pass.

Pre-update backup

Run backup before installing software updates – the system will create an incremental backup of machine before installing any updates on it. If there were no backups created earlier, then a full backup of machine will be created. It allows you to prevent such cases when the installation of updates was unsuccessful and you need to get back to the previous state. For the Pre-update backup option to work, the corresponding machines must have both the patch management and the backup module enabled in a protection plan and the items to back up – entire machine or boot+system volumes. If you select inappropriate items to back up, then the system will not allow you to enable the Pre-update backup option.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.