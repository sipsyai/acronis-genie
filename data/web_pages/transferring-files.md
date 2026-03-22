# Transferring files

RMM > Connecting to workloads for remote desktop or remote assistance > Working with managed workloads > Transferring files
Transferring files

You can easily transfer files between the local workload and a managed workload.

Prerequisites

2FA is enabled for your user account in Acronis Cyber Protect Cloud.

To remotely transfer files between your workload and a managed workload

In the Cyber Protect console, go to Devices > Machines with agents.

Click the workload with which you want to transfer files.

Click Manage, and then Transfer files.

[If a remote management plan is not applied to the workload] In the Apply remote management plan window, do one of the following:

If you want to apply an existing remote management plan, click the Available plans field, select the plan, and then click Apply.

The system automatically suggests the most appropriate plan.

If you want to create a new remote management plan, click Add new, configure the settings, click Create, and then, in the confirmation window, click Confirm.

For more information about creating and configuring a remote management plan, see Creating a remote management plan.

[If Allow connections via NEAR or File transfer is disabled in the remote management plan that is applied to the workload] In the Update remote management plan window, click Update, enable the settings, save the changes, and then start this procedure from step 1.

[If Connect Client is not installed on your workload] In the Connect to workload dialog, click Download Connect Client, download and install the client on your workload, and then click Connect.

[If a confirmation pop-up appears] Click Open Connect Client.

In the Authentication window, select an authentication option, and then provide the required credentials.

Authentication option	Description
With remote workload credentials	You will be allowed to establish the remote connection after you provide username and password of an administrator user of the remote workload.
Ask for permission to transfer files	You will be allowed to transfer files after the user who is logged in on the remote workload allows it.

[To view hidden files] In the File transfer window, click View, and then click Show hidden files.

Browse to the files that you want to transfer, and then drag and drop them to the desired destination.

The files of the local workload are listed in the left pane, and the files of the remote workload are listed in the right pane.

When a file transfer begins, it is listed in the Tasks pane.

If you want to remove the completed tasks from the Tasks pane, click Clear finished.

When all transfers complete, close the window.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.