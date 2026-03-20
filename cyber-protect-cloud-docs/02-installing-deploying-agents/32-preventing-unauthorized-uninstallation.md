---
title: "Preventing unauthorized uninstallation or modification of agents"
section: "Installing and deploying Cyber Protection agents"
subsection: "Preventing unauthorized uninstallation or modification of agents"
page_range: "200-201"
tags: ["uninstallation protection", "self-protection", "agent modification", "security", "anti-tamper", "protection plan"]
acronis_version: "26.02"
---

# Preventing unauthorized uninstallation or modification of agents

The Cyber Protection agent for Windows is protected against unauthorized uninstallation or modification through the **Agent uninstallation protection** option in protection plans. For all protection plans created after November 2024, this option is enabled by default. In legacy protection plans, you need to enable it manually to enhance the security of your workloads.

> **Note:** This option is available only when the **Self-protection** setting is enabled.

## To enable agent uninstallation protection

1. In a protection plan, expand the **Antivirus & Antimalware protection** module (**Active Protection** module for Cyber Backup editions).
2. Ensure that the **Self-protection** switch is enabled.
3. Select the **Agent uninstallation protection** checkbox.
4. In the **Self-protection** pane, click **Done**.
5. Save the protection plan.

Agent uninstallation protection will be enabled for the Windows machines to which this protection plan is applied. All modifications will be prohibited unless an administrator authorizes them.

You can apply a protection plan with the **Agent uninstallation protection** option enabled to a machine running macOS or Linux, but no protection will be provided.

You cannot apply more than one protection plan with Agent uninstallation protection enabled to the same Windows machine.

## To allow the modification of an agent with uninstallation protection enabled

1. After an unsuccessful attempt to modify the protection agent, navigate to the **Alerts** tab.
2. Locate the alert related to the failed modification/uninstallation attempt.
   - Alert severity: Warning
   - Alert title: Prevented agent uninstall/update attempt
3. Click the alert and select a response action from the dropdown list:
   - **Allow agent changes for 1 hour** -- Allow modifications to the protection agent in the next hour.
   - **Go to agent update settings** -- Configure a longer maintenance window (between 1 hour and 7 days from the present moment). Modifications or uninstallation of the agent will only be allowed during this period, unless you enable the automatic updates for the protection agent.
4. (Only if you selected agent update settings) In the agent configuration dialog, select the duration of the maintenance period for manual updates or enable the **Automatically update agents** option.
   - If you configure a maintenance period without enabling automatic updates, only manual modifications will be allowed during that period.
   - If you enable automatic updates without configuring a maintenance window, automatic updates can occur at any point in time.
   - If you configure both a maintenance window and automatic updates, both automatic and manual updates can occur only during the maintenance window.
5. Click **Apply**.

## To disable agent uninstallation protection

> **Warning!** Disabling the **Agent uninstallation protection** setting puts the protected workloads at security risk.

1. Open the protection plan for editing and expand the **Antivirus & Antimalware protection** module (**Active Protection** module for Cyber Backup editions).
2. Expand the **Self-protection** section.
3. Clear the **Agent uninstallation protection** checkbox.
4. In the **Self-protection** pane, click **Done**.
5. Save the protection plan.
