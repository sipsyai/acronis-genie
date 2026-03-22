# Creating a remote management plan

RMM > Connecting to workloads for remote desktop or remote assistance > Remote management plans > Creating a remote management plan
Creating a remote management plan

You can create a remote management plan, and then assign it to a workload to configure the remote desktop and assistance functionality on the managed workload.

The availability of the remote management plan's settings depends on the license that is assigned to the workload.

Prerequisites

2FA is enabled for your user account.
If the managed device is joined to Entra ID (formerly Azure AD), and you want to connect to it by using the NEAR protocol, see this KB article.

To create a remote management plan

From Remote management plans
From All devices

In the Cyber Protect console, go to Management > Remote management plans.

Create a remote management plan by using one of the two options.

If there are no remote management plans in the list, click Create.

If there are remote management plans in the list, click Create plan.

To change the default name of the plan, click the pencil icon, enter the name of the plan, and then click Proceed.

Click Connection protocols, and enable the protocols that you want to be available in this remote management plan for remote connections - NEAR, RDP, or Apple Screen Sharing.

[Optional] For the NEAR protocol, in the Security settings section, select or clear the check boxes to enable or disable the corresponding setting, and then click Done.

Setting	Description	Available for
Lock the workload when the user disconnects from the console session	If you select this setting, the remote workload will be locked when you disconnect from the console session.	Windows, macOS
Allow only one user at a time to connect using NEAR or to transfer files	If you select this setting, connections using NEAR and file transfers will not be possible while there is an active remote connection to the workload.	Windows, macOS, Linux
Allow the workload's administrator to connect to any non-admin user session

If you select this setting, the administrator will be allowed to connect to any standard user session on the workload.

If both Allow the workload's administrator to connect to any non-admin user session and Allow system session creation are clear, you will only be able to connect to active administrator sessions on the remote macOS workloads.


Windows, macOS
Allow system session creation

If you select this setting, when establishing remote connections, the administrator will connect in a new session, instead of one of the existing active sessions.

macOS
Allow clipboard synchronization	If you select this setting, you will be able to transfer data between your clipboard and the clipboard of the remote workload. For example, you will be able to copy some text from a file on the remote workload and paste it in a file on your workload, and the opposite.	Windows, macOS, Linux

Click Security settings, select or clear the check boxes to enable or disable the corresponding setting, and then click Done.

Setting	Description
Show if the workload is controlled remotely	If you select this setting, a notification will be displayed on the desktop of the remote workload when there is an active remote desktop connection to the workload.
Ask for the user's permission to take screenshots of the workload	If you select this setting, the user of the remote workload will be notified when the administrator requests screenshot transmission from the workload.

Click Workload management, select the features that you want to be available on the remote workloads, and then click Done.

Setting	Description	Available on
File transfer	Enables the file transfers between local and remote workloads.	Windows, macOS, Linux
Screenshot transmission	Enables the transmission of screenshots of the desktop of the remote workload to the Cyber Protect console.	Windows, macOS, Linux
Geolocation tracking	Enables tracking the workload location when location services are enabled in the operating system settings of the workload.

Windows, macOS, Linux


Chat	Enables live chat between a technician who is logged in to the Cyber Protect console and a user who is logged in to the remote workload.	Windows, macOS

Click Display settings, select or clear the check boxes to enable or disable the corresponding setting, and then click Done.

The Display settings are only available for connections via NEAR.

Setting	Description	Available on
Use Desktop Deduplication for desktop capturing	Desktop duplication is one of the screen capture methods on Windows. In some environments, it might be unstable. If you do not use Desktop deduplication, you will use the basic method (BitBlt) instead- it is much slower, but more stable.	Windows
Use OpenCL acceleration

OpenCL acceleration can speed up the Adaptive codec, which is responsible for the Balanced quality mode, by running some computations on the graphics processing unit (GPU). This requires an installation of an OpenCL driver on the remote Linux.

Adaptive Codec is using OpenCL on macOS and Windows, if it is available in your graphics drivers.

Linux
Use hardware H.264 encoding

NEAR supports three quality modes: Smooth, Balanced, and Sharp.

Smooth mode uses hardware H.264 encoding to encode the desktop picture.

Balanced mode uses Adaptive codec, which provides full picture quality in 32 bit, compared to the 'video' mode used by H.264. The picture quality is automatically adjusted according to your current network conditions and retains the current framerate.

Sharp mode uses Adaptive codec, which provides full picture quality in 32 bit, compared to the 'video' mode used by H.264. The picture quality is always full, but it might be with reduced frames per seconds, if your network or processor/video card are overloaded.



Windows, macOS

Click Toolbox, select or clear the check boxes to enable or disable the corresponding setting, and then click Done.

Setting	Description	Available on
Show last logged-in users	If you select this setting, the information about the users who last logged in to the workloads will be visible in the workload's details.
For more information about the last logged-in users, see Viewing the last logged-in user.

Windows, macOS, Linux


Remote command-line interface

This setting enables the remote access to the command-line interface of the managed device.

Windows, macOS

[Optional] To add workloads to the plan:

Click Add workloads.
Select the workloads, and then click Add.
If there are compatibility issues that you want to resolve, follow the procedure as described in Resolving compatibility issues.
Click Create.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.