# Schedule and start conditions

Managing workloads in the Cyber Protect console > Cyber Scripting > Scripting plans > Schedule and start conditions
Schedule and start conditions
Schedule

You can configure a scripting plan to run once or repeatedly, and to start on a schedule or to be triggered by a certain event.

The following options are available:

Run once

For this option, you must configure the date and time when the plan will run.

Schedule by time

With this option, you can configure scripting plans that run hourly, daily, or monthly.

To make the schedule effective only temporarily, select the Run within a date range check box, and then configure the period during which the scheduled plan will run.

When user logs in to the system

You can choose whether a specific user or any user who logs in triggers the scripting plan.

When user logs off the system

You can choose whether a specific user or any user who logs off triggers the scripting plan.

On the system startup

When system is shut down

This scheduling option only works with scripts that run under the system account.

When system goes online

Start conditions

Start conditions add more flexibility to your scheduled plans. If you configure multiple conditions, all of them must be met simultaneously in order for the plan to start.

Start conditions are not effective if you run the plan manually, by using the Run now option.

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

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.