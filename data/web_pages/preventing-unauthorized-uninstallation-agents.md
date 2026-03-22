# Preventing unauthorized uninstallation or modification of agents

Installing and deploying Cyber Protection agents > Preventing unauthorized uninstallation or modification of agents
Preventing unauthorized uninstallation or modification of agents

The Cyber Protection agent for Windows is protected against unauthorized uninstallation or modification through the Agent uninstallation protection option in protection plans. For all protection plans created after November 2024, this option is enabled by default. In legacy protections plans, you need to enable it manually to enhance the security of your workloads.

This option is available only when the Self-protection setting is enabled.

To enable agent uninstallation protection

In a protection plan, expand the Antivirus & Antimalware protection module (Active Protection module for Cyber Backup editions).
Ensure that the Self-protection switch is enabled.
Select the Agent uninstallation protection checkbox.
In the Self-protection pane, click Done.
Save the protection plan.

Agent uninstallation protection will be enabled for the Windows machines to which this protection plan is applied. All modifications will be prohibited unless an administrator authorizes them. See To allow the modification of an agent with uninstallation protection enabled.

You can apply a protection plan with the Agent uninstallation protection option enabled to a machine running macOS or Linux, but no protection will be provided.

Also, you cannot apply more than one protection plan with Agent uninstallation protection enabled to the same Windows machine. To learn how to resolve a possible conflict, see Resolving compatibility issues.

To allow the modification of an agent with uninstallation protection enabled

After an unsuccessful attempt to modify the protection agent, navigate to the Alerts tab.
Locate the alert related to the failed modification/uninstallation attempt.

Alert severity: Warning

Alert title: Prevented agent uninstall/update attempt

Click the alert and select a response action from the dropdown list:
Allow agent changes for 1 hour - to allow modifications to the protection agent in the next hour.
Go to agent update settings - to configure a longer maintenance window.

The duration can be between 1 hour and 7 days from the present moment.

Modifications or uninstallation of the agent will only be allowed during this period, unless you enable the automatic updates for the protection agent.

[Only if you selected to go to the agent update settings] In the agent configuration dialog, select the duration of the maintenance period for manual updates or enable the Automatically update agents option.
If you configure a maintenance period without enabling automatic updates, only manual modifications will be allowed only during the maintenance period that you configured.
If you enable automatic updates without configuring a maintenance window, automatic updates can occur at any point in time.
If you configure both a maintenance window and automatic updates, both automatic and manual updates can occur only during the maintenance window.
Click Apply.

To disable agent uninstallation protection

Disabling the Agent uninstallation protection setting puts the protected workloads at security risk.
Open the protection plan for editing and expand the Antivirus & Antimalware protection module (Active Protection module for Cyber Backup editions).
Expand the Self-protection section.
Clear the Agent uninstallation protection checkbox.
In the Self-protection pane, click Done.
Save the protection plan.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.