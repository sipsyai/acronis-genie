# Patch a workload

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Remediating incidents > Patch a workload
Patch a workload

EDR automatically detects if a workload requires a patch, and enables you to patch the workload to prevent vulnerability exploitations in future potential attacks. Note that this feature is available only if the partner's workload has a subscription for RMM.

To patch a workload

In the cyber kill chain, click the workload node you want to patch.
In the displayed sidebar, click the Response Actions tab.
In the Remediate section, click Patch.
In the Patches to install field, click Select. In the displayed dialog, select the relevant patches and then click Select.
In the Restart options field, click the displayed link. The Restart options dialog is displayed.

Select if you want the workload to be restarted after the patches are installed.

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

Click Save.
In the Response Actions tab, click Patch.

The selected patch is run. This action can also be viewed in the Activities tabs of both the individual node and the entire incident. For more information, see Understand the actions taken to mitigate an incident.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.