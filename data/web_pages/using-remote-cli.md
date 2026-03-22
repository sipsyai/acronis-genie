# Connecting to a remote command line

RMM > Connecting to workloads for remote desktop or remote assistance > Working with managed workloads > Connecting to a remote command line
Connecting to a remote command line

You can remotely connect to the command-line interface of your managed Windows and macOS workloads and perform tasks that are related to diagnostics, troubleshooting, configuration management, maintenance, automation, and scheduling of tasks.

Prerequisites

You have the Cyber Administrator role.
2FA is enabled for your account in Acronis Cyber Protect Cloud.
The operating system of the remote workload is supported for remote command line. For more information, see Supported operating systems for remote command line.
Windows
macOS

To remotely connect to the command line of a Windows device

In the Cyber Protect console, go to Devices > Machines with agents.

Click the workload for which you want to start the remote command line.

In the Actions menu, click Manage, and then click Command line.

[If a remote management plan is not applied to the workload] In the Apply remote management plan window, do one of the following:

If you want to apply an existing remote management plan, click the Available plans field, select the plan, and then click Apply.

The system automatically suggests the most appropriate plan.

If you want to create a new remote management plan, click Add new, configure the settings, click Create, and then, in the confirmation window, click Confirm.

For more information about creating and configuring a remote management plan, see Creating a remote management plan.

In the new tab that opens, select the command-line interface that you want to use.

You will see the following options, based on the command-line tools that are available on the workload:

PowerShell 7 (64-bit)
PowerShell 7 (32-bit)
PowerShell 5 (64-bit)
PowerShell 5 (32-bit)
Command Prompt (64-bit)
Command Prompt (32-bit)

In the User field, select the user account under which you want to start the command line.

If you start the command line with the system account, your actions will not be visible to the user of the remote workload.

If you start the command line with the logged-in user account, your actions will be visible.

Depending on whether you want to save the settings for the next session, select or clear Save settings for next session.

Click Start session.

The console of the command line opens. You can now perform tasks in the console.

Starting and ending a remote command-line session creates a record in Audit log. The record includes details about the event, such as date and time, tenant, workload name, IP address, and initiator.

Additional actions with the remote command-line console

Supported operating systems for remote command line




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.