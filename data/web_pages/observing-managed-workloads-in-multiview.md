# Observing multiple managed workloads simultaneously

RMM > Connecting to workloads for remote desktop or remote assistance > Working with managed workloads > Observing multiple managed workloads simultaneously
Observing multiple managed workloads simultaneously

You can observe the desktops of multiple remote workloads simultaneously in a single window. This functionality requires that NEAR or Apple Screen Sharing is enabled in the remote management plans that are applied to the workloads.

The number of desktops that you can see simultaneously in the window depends on the size of your monitor.

Prerequisites

2FA is enabled for your user account in Acronis Cyber Protect Cloud.

To observe multiple workloads simultaneously

In the Cyber Protect console, go to Devices > All devices.

Select the workloads which you want to observe.

Click Multi view.

[If a remote management plan is not applied to any of the workloads] In the Apply remote management plan window, do one of the following:

If you want to apply an existing remote management plan, click the Available plans field, select the plan, and then click Apply.

The system automatically suggests the most appropriate plan.

If you want to create a new remote management plan, click Add new, configure the settings, click Create, and then, in the confirmation window, click Confirm.

For more information about creating and configuring a remote management plan, see Creating a remote management plan.

[If the corresponding feature is not enabled in the remote management plan that is applied to the workloads] In the Update remote management plan window, click Update, enable the feature, and then start this procedure from step 1.

[If Connect Client is not installed on your workload] In the Connect to workload dialog, click Download Connect Client, download and install the client on your workload, and then click Connect.

[If a confirmation pop-up appears] Click Open Connect Client.

In the Authentication window, select an authentication option, and then provide the required credentials.

Authentication option	Description
With remote workload credentials	You will be allowed to establish the remote connection after you provide username and password of an administrator user on the remote workload.
Ask for permission to observe

You will be allowed to establish the remote connection in observe mode after the user who is logged in on the remote workload allows it.

If you want to use the same authentication method and credentials when connecting to all the remote workloads that you selected in step 2, select Use on other computers.

Click Connect.

In toolbar of the multi-view window, you can select a view mode in which to connect to a workload. This action will open a separate Viewer window for that workload.

If any of the selected workloads is offline, or has an outdated version of the agent installed, it will not be shown in the multi-view window.

All multi-view connections to remote workloads are in View-only mode.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.