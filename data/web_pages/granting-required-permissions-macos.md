# Granting the required system permissions to the Connect Agent

Installing and deploying Cyber Protection agents > Before you start > Granting the required system permissions to the Connect Agent
Granting the required system permissions to the Connect Agent

To enable all features from the remote desktop functionality on macOS workloads, in addition to the full disk access permission, you must grant the following permissions to the Connect Agent:

Screen Recording - enables screen recording of the macOS workload via NEAR. Until this permission is granted, all remote control connections are denied.
Accessibility - enables remote connections in control mode via NEAR.
Microphone - enables sound redirection from the remote macOS workload to the local workload via NEAR. To enable the sound redirection feature, a sound capture driver must be installed on the workload. For more information, see Remote sound redirection.
Automation - enables the empty recycle bin action.
Location Services - enables the location services on the workload. Until this permission is granted, the agent cannot track the location of the workload.

After you start the agent on the macOS workload, it will check if the agent has these rights and will ask you to grant the permissions, if needed.

To grant the Screen Recording permission

In the Grant required system permissions to Cyber Protect Agent dialog, click Set up system permissions.
In the System permissions dialog, on the Screen Recordingrow, click Acquire.
Click Open System Settings.
For Connect Agent, enable the toggle.

If the agent does not have the permission when you try to access the workload remotely, it will show the Screen Recording permission request dialog. Only the local user may answer the dialog.

To grant the Accessibility permission

In the Grant required system permissions to Cyber Protect Agent dialog, click Set up system permissions.
In the System permissions dialog, on the Accessibility row, click Acquire.
Click Open System Settings.
Click the lock icon in the bottom-left corner of the window so that it changes to an unlocked icon. The system will ask you for an administrator password to make changes.
Select Connect Agent.

To grant the Microphone permission

In the Grant required system permissions to Cyber Protect Agent dialog, click Set up system permissions.
In the System permissions dialog, on the Microphone row, click Acquire.
In the confirmation window, click Allow.

To let the agent utilize the given permission and redirect the sound of the workload, you must also install a sound capture driver on the macOS workload . For more information, see Remote sound redirection.

To grant the Automation permission

In the Grant required system permissions to the Connect Agent dialog, click Set up system permissions.
In the System permissions dialog, on the Automation row, click Acquire.
In the confirmation window, click Allow.

To grant the Location Services permission

In the Grant required system permissions to the Connect Agent dialog, click Set up system permissions.
In the System permissions dialog, on the Location Services row, click Acquire.
In the confirmation window, click Allow.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.