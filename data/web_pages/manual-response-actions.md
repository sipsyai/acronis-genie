# Manual response actions

RMM > Monitoring the health and performance of workloads > Monitoring alerts > Manual response actions
Manual response actions

When you see an alert, you can select a response action that you want to perform on the alerted events.

To perform a manual response action

In the Protection console, go to Alerts.
Open the alert that you want to view.
Click Response action, and then select a response action from the drop-down list.

The list of response actions available for a particular alert depends on the alert type, availability of features for a particular tenant and the workload operating system.

The following table lists and describes all the manual response actions for your reference.

Manual response action	Description	Supported OS
Browse disk space usage trend

Opens a window with Disk space usage graph, where you can:

Browse how the disk space usage changed over time (for the last 1 day / 7 days / 1 month).

Browse the delta for disk space usage in relative value (%) for the selected period.

Windows, macOS
Browse files size growth trend

Opens a window with File size growth graph, where you can:

Browse how the total size of the monitored files and folders changed over time (for the last 1 day / 7 days / 1 month).

Browse the delta for total size of files in relative value (%) for the selected period.

Windows, macOS
Run a script

Opens a window, where you can:

Select a certain script to run on the workload.

Specify the account under which you want to execute the script.

Specify maximum duration of the operation.

Specify PowerShell execution policy.

Run a script.

To perform this action, an RMM (service-based licensing mode) or Security and RMM (solution-based licensing mode) license must be assigned to the workload.

Windows, macOS
Connect via NEAR

Acronis Connect Client establishes a remote connection.

Windows, macOS
Connect via RDP

Acronis Connect Client establishes a remote connection.

Windows
Run command line	Starts the command line (Command Prompt or PowerShell) of the workload.	Windows
Run Terminal	Starts the Terminal app (BASH or ZSH) of the workload.	macOS
Open hardware inventory

You are redirected to Hardware inventory tab for the current workload.

Windows, macOS
Browse top 10 processes that loaded CPU

Opens a window with top 10 processes that have loaded the CPU and may have caused its overheating (The system snapshot at the moment of alert generation).

Windows, macOS
Browse top 10 processes that loaded GPU

Opens a window with top 10 processes that have loaded the GPU and may have caused its overheating (The system snapshot at the moment of alert generation).

Windows, macOS
Browse top 10 processes that loaded memory

Opens a window with top 10 processes that have loaded the memory (The system snapshot at the moment of alert generation).

Windows, macOS
Browse top 10 processes that loaded disk

Opens a window with top 10 processes that have loaded the disk (The system snapshot at the moment of alert generation).

Windows, macOS
Browse top 10 processes that loaded network

Opens a window with top 10 processes that have loaded the network interface adapter (The system snapshot at the moment of alert generation).

Windows, macOS
Browse resource usage by process

Opens a window with detailed information about the usage of hardware resources by the related process: CPU usage, memory usage, disk I/O, network usage.

Windows, macOS
Restart workload

Opens a confirmation window. Restarts the workload after the confirmation.

Windows, macOS
Start Windows service

Opens a confirmation window. Starts the Windows service after the confirmation.

Windows
Stop Windows service

Opens a confirmation window. Stops the Windows service after the confirmation.

Windows
Stop process

Opens a confirmation window. Stops the process to which the alert refers to after the confirmation.

Windows, macOS
Enable Windows Update

Opens a confirmation window. Enables Windows Update after the confirmation.

Windows
Disable AutoRun feature on removable drives

Opens a confirmation window. Disables AutoRun feature on the system level of the workload after the confirmation.

Windows

For security reasons, two-factor authentication is required to perform the following manual response actions:

Run a script
Connect via NEAR
Connect via RDP
Restart workload
Start Windows service
Stop Windows service
Stop process
Enable Windows Update
Disable AutoRun feature on removable drives
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.