# Creating a software deployment plan

RMM > Managing software > Software deployment plans > Creating a software deployment plan
Creating a software deployment plan

The availability of this feature depends on the license that you have.

You can create a software deployment plan, and then assign it to one or several workloads. Thus, you ensure that you distribute and install approved software on your managed workloads, and at the same time uninstall software that is obsolete or unapproved by your organization.

When Active Protection is enabled in the protection plan that is applied to the workloads, the software deployment is protected by the antimalware engine. Before installing a package on the workloads, the system will automatically run an antimalware scan. This proactive layer of defense safeguards against malicious injections, ensuring that the software deployment will not introduce vulnerabilities into the systems. This is especially valuable in environments where security is critical, and reduces the risk of downtime and costly incident responses.

A single software deployment plan supports only one of the deployment actions: install or uninstall. This means that if you must create separate plans - one for software installation, and another one for software uninstallation.

Prerequisites

2FA is enabled for your user account.
You have one of the following roles for Cyber Protection: Company administrator or Cyber administrator.

To create a software deployment plan

From Software deployment plans
From All devices

In the Cyber Protect console, go to Management > Software deployment plans.

Create a plan by using one of the two options:

If there are no software deployment plans in the list, click Create.
If there are software deployment plans in the list, click Create plan.

[Optional] To add workloads to the plan:

Click Add workloads.
Select the workloads, and then click Add.
To change the default name of the plan, click the pencil icon, enter the name of the plan, and then click Proceed.

In the Action field, select whether the plan will install or uninstall software.

In the Software field, click Select software, select one or several applications from the list, and the click Done.

To configure the restart options, do the following:

Click the Restart options field.

On the Restart options screen, configure if the system will restart the workloads after the software installation or uninstallation.

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

Click Done.

To create a schedule for the plan execution, do the following:

Click the Schedule field.

On the Schedule screen, in the Schedule the task run using the following events field, the event that will start the plan.

Option	Description
Run once	If you select this option, you must configure the date and time when the plan will run.
Schedule by time

If you select this option, you can configure plans that run hourly, daily, or monthly.

If you want this schedule to be effective only during a specific time period, select the Run within a date range check box, and then configure the period (in days) during which the scheduled plan will run.


When user logs in to the system	If you select this option, the plan will run when either a specific user or any user logs in to the target workload.
When user logs off the system	If you select this option, the plan will run when either a specific user or any user logs off from the target workload.
On the system startup	If you select this option, the plan will run when the target workload is started.
When system is shut down	If you select this option, the plan will run when the target workload is shut down.
When system goes online	If you select this option, the plan will run when the target workload becomes online.

In the Start conditions section, select all conditions that must be met simultaneously to start the plan.

Condition	Description
Run only if workload is online	This condition is met when the target workload is connected to the Internet.
User is idle	This condition is met when a screen saver is running on the machine or the machine is locked.
User logged off	If you select this condition, you can postpone a scheduled plan until the user of the target workload logs off.
Fits time interval	If you select this condition, you must define the time interval in which the plan can run.
Save battery power

If you select this condition, you can ensure that the plan would not be interrupted because of a low battery. The following options are available:

Do not start when on battery

The plan will start only if the machine is connected to a power source.

Start when on battery if the battery level is higher than

The plan will start if the machine is connected to a power source or if the battery level is higher than the specified value.


Do not start on metered connection	If you select this condition, the plan will not run if the target workload accesses the Internet via a metered connection.
Do not start when connected to the following Wi-Fi networks

If you select this condition, the plan will not run if the target workload is connected to any of the specified wireless networks.

To use this condition, you must specify the SSID of the forbidden network. The restriction applies to all networks that contain the specified name as a substring in their name, case-insensitive. For example, if you specify phone as the network name, the plan will not start when the device is connected to any of the following networks: John's iPhone, phone_wifi, or my_PHONE_wifi.


Check device IP address

If you select this condition, the plan will not run if any of the IP addresses of the target workload are within or outside of the specified IP address range.

The following options are available:

Start if outside IP range
Start if within IP range

Only IPv4 addresses are supported.


If start conditions are not met, run the task anyway

Use this option to set the time interval after which the plan will run, irrespective of any other conditions. The plan will start either when the other conditions are met or when this period ends, depending on which happens first.

This option is not available if you selected the Run once option for the schedule.

Click Done.
Click Create.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.