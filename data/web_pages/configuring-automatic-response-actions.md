# Configuring automatic response actions

RMM > Monitoring the health and performance of workloads > Monitoring plans > Configuring automatic response actions
Configuring automatic response actions

Automatic response actions on the alerted events are predefined actions or measures that are triggered automatically in response to detected events or incidents. These actions are designed to mitigate potential threats and to minimize damage.

You can configure one or several automatic response actions on the alerted events. The maximum number of automatic response actions per monitor can be 20.

To configure automatic response actions

In the Protection console, go to Management > Monitoring plans.
Select the monitoring plan for which you want to configure automatic response actions.
Select the monitor, to which you want to configure automatic response actions, or, if you have not added monitors yet, click Add monitor, click the monitor in the list, click Add, and then select the monitor.
Click the link next to Automatic response actions.
In the Automatic response actions window, add one or several response actions that will be performed automatically when an alert is triggered.
Configure each response action. For example, if you have added the response action Start a Windows service, do the following:
Next to Windows service, click Specify.
In the Service field, select a service to start as a response action.
Click Done.
In the list of all added response actions use the up and down arrows or drag and drop to set the sequence of the response actions.
Configure how to handle successive response actions if a previous response action fails. Select one of the following:
Continue with the next response action.
Do not continue with the next response action.
Click Done.

You will see the number of configured actions next to the Automatic response actions setting of your monitoring plan. You can edit or delete these actions, as well as add the new ones at any time later.

The following table lists and describes all the automatic response actions available in the monitor settings.

Automatic response action	Description	Supported OS
Run a script

If you add this action, you can:

Select a certain script to run on the workload.
Specify the account under which you want to execute the script.
Specify maximum duration of the operation.
Specify PowerShell execution policy.
Run a script.
To perform this action, you need the RMM license (service-based licensing mode) or Security and RMM (solution-based licensing mode) for the workload, if not assigned yet.

The system will run the selected remote script with specified parameters when the conditions are met.

Windows, macOS
Restart the workload

If you add this action, the system will restart the workload remotely when the conditions are met.

Windows, macOS
Stop the process

If you add this action, you can specify the process to stop via manual input of process name.

The system will stop the process when the conditions are met.

Windows, macOS
Start the Windows service

If you add this action, you can select which Windows service to start from the dynamic list of services populated from the agents.

The system will start the service when the conditions are met.

Windows
Stop the Windows service

If you add this action, you can select which Windows service to stop from the dynamic list of services populated from the agents.

The system will stop the service when the conditions are met.

Windows
Enable Windows Update

If you add this action, the system will enable Windows Update when the conditions are met.
This action is available only for Windows Update status monitor.

Windows
Disable AutoRun on removable drives

If you add this action, the system will disable the AutoRun feature on removable storage media for the workload when the conditions are met.
This action is available only for Autorun feature status monitor.

Windows
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.