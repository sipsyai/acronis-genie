# Installing software

RMM > Managing software > Installing software
Installing software

The availability of this feature depends on the license that you have.

You can remotely install software on your managed workloads without creating a software deployment plan. This action is supported for up to 15 software packages and up to 150 target workloads at a time.

Prerequisites

You have one of the following roles for Cyber Protection: Company administrator or Cyber administrator.

To install a software package

From My packages
From All devices
In the Cyber Protect console, go to Software management > My packages.
Select the software that you want to install, and then click Install.
In the Deploy software window, click Add workloads.

Select the workloads on which you want to install the package, and then click Add.

To configure the restart options, do the following:

Click the Restart options field.

On the Restart options screen, configure if the system will restart the workloads after the software installation.

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

Click Install now.

Packages that failed the digital signature check will not be deployed.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.