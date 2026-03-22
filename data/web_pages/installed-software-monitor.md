# Settings of the Installed software monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Installed software monitor
Settings of the Installed software monitor

Installed software monitors the installation, updates, or deletion of software applications on the workload.

You can configure the following settings for the monitor.

Setting	Description
What software to monitor

Specify the software that you want to monitor.

The following values are available.

Any software —This is the default value.
Specific software

Software names

This setting becomes available if you select the Specific software value for What software to monitor.

Enter the name of one or several software applications.

You can select a software application name from the list of Windows services. The list is populated by all agents of the tenant after software inventory scan completes successfully on the workloads. You can also add a software application name that is not in the list. This is the only available option if software inventory scan was not performed on the workloads.


Installation status

Specify if you want to monitor installed, not installed, or updated software.

The following values are available.

Installed - This is the default value. If you select this value, the monitor will generate an alert when a new software application is installed on the workload.
Updated - If you select this value, the monitor will generate an alert when a software application is updated.
Not installed - If you select this value, the monitor will generate an alert when a software application is uninstalled or not available on the workload.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.