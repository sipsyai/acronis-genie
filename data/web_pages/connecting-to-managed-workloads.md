# Connecting to managed workloads for remote desktop or remote assistance

RMM > Connecting to workloads for remote desktop or remote assistance > Working with managed workloads > Connecting to managed workloads for remote desktop or remote assistance
Connecting to managed workloads for remote desktop or remote assistance

The availability of the connection protocols that you can use for remote connections depends on the remote management plan configuration and on the remote workload's operating system.

Prerequisites

[For Apple Screen Sharing connections] Apple Screen Sharing is enabled on the macOS workload.
2FA is enabled for your user account in Acronis Cyber Protect Cloud.

To remotely connect to a managed workload for remote desktop or remote assistance

In the Cyber Protect console, go to Devices > Machines with agents.

Click the workload to which you want to connect.

Click Remote desktop.

By default, NEAR is selected as a connection protocol.

In the Connection protocol drop-down list, select the connection protocol that you want to use.

Click the view mode that you want to use.

Protocol	Remote connections to	View mode	Supported remote action
NEAR

Windows

Linux

macOS



Control - In this mode, you will be able to observe and perform operations on the remote workload.

View-only- In this mode, you will be only able to observe the remote workload.



Remote desktop

Remote assistance


RDP	Windows

Control - In this mode, you will be able to view and perform operations on the remote workload.

If RDP is disabled in the OS settings of the workload, a pop-up window will appear. Use this window to enable RDP for the workload for the current session or in general:

If you want to enable RDP for this workload only for the current session, select Disable it after the session is over, and then click Allow.

If you want to enable RDP for this workload, click Allow.

Remote desktop
Apple Screen Sharing	macOS

Control - In this mode, you will be able to observe and perform operations on the remote workload.

View-only - In this mode, you will be only able to observe the remote workload.

Curtain - available only for macOS workloads. If you connect to the remote workload in curtain mode, the display of the remote workload will be dimmed, and the remote user will not be able to see your actions on the workload.



Remote desktop

Remote assistance

[If a remote management plan is not applied to the workload] In the Apply remote management plan window, do one of the following:

If you want to apply an existing remote management plan, click the Available plans field, select the plan, and then click Apply.

The system automatically suggests the most appropriate plan, depending on the protocol that you selected in the previous step.

If you want to create a new remote management plan, click Add new, configure the settings, click Create, and then, in the confirmation window, click Confirm.

For more information about creating and configuring a remote management plan, see Creating a remote management plan.

[If the corresponding feature is not enabled in the remote management plan that is applied to the workload] In the Update remote management plan window, click Update, enable the feature, save the changes, and then start this procedure from step 1.

[If Connect Client is not installed on your workload] In the Connect to workload dialog, click Download Connect Client, download and install the client on your workload, and then click Connect.

[If a confirmation pop-up appears] Click Open Connect Client.

In the Authentication window, select an authentication option, and then provide the required credentials.

If you have assigned credentials to the workload, authentication will be done automatically and this step will be skipped. For more information, see Assigning credentials to a workload.

Authentication option	Description
With remote workload credentials

You will be allowed to establish the remote connection after you provide username and password of an administrator user of the remote workload.

This option is available for NEAR, RDP, and Apple Screen Sharing.

You can use this option to authenticate for remote desktop and remote assistance.


Ask for permission to observe

You will be allowed to establish the remote connection in observe mode after the user who is logged in on the remote workload allows it.

This option is available for NEAR and Apple Screen Sharing.

You can use this option to authenticate for remote assistance.


Ask for permission to control

You will be allowed to establish the remote connection in control mode after the user who is logged in on the remote workload allows it.

This option is available for NEAR and Apple Screen Sharing.

You can use this option to authenticate for remote assistance.

Click Connect, and then click the session to display (if more than one user session is available on the workload).

Connect Client will open a new viewer window on which you will be able to see the remote workload's desktop. The viewer has a toolbar with additional actions that you can perform on the remote workload after the remote connection is established. For more information, see Using the toolbar in the Viewer window.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.