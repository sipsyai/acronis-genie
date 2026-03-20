---
title: "Updating protection agents automatically"
section: "Installing and deploying Cyber Protection agents"
subsection: "Updating protection agents automatically"
page_range: "125-129"
tags: ["update", "automatic", "agents", "maintenance window", "update channel", "BitLocker", "auto-update"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#updating-agents-automatically.html"
---

# Updating protection agents automatically

To facilitate the management of multiple workloads, you can configure automatic updates for Agent for Windows, Agent for Linux, and Agent for Mac. Automatic updates are available for agents version 26986 (released in May 2021) or later. Older agents must be updated manually to the latest version first.

> **Note:** The configuration of automatic updates for a protection agent overrides the **Agent uninstallation protection** setting in all protection plans for the agent.

## Supported operating systems

- Windows XP SP 3 and later
- Red Hat Enterprise Linux 6 and later, CentOS 6 and later
- OS X 10.9 Mavericks and later

## Settings hierarchy

The settings for automatic updates are preconfigured on a data center level. A partner or company administrator can customize these settings for all machines in a company or a unit, or for individual machines. If no custom settings are applied, settings from the upper level are used, in this order:

1. Cyber Protection data center
2. Company (customer tenant)
3. Unit
4. Machine

Even within the enabled maintenance window, updates will not be installed while the agent is running any of the following operations:

- Backup
- Recovery
- Backup replication
- Virtual machine replication
- Testing a replica
- Running a virtual machine from backup (including finalization)
- Disaster recovery failover
- Disaster recovery failback
- Running a script (for Cyber Scripting functionality)
- Patch installation
- ESXi configuration backup

## Automatic updates for all agents

1. Select **Settings** > **Agents**.
2. Under **Actions** in the upper right corner, click **Edit default agent update settings**.
3. Under **Update channel**, select which version to use for automatic updates.

| Option | Description |
|--------|-------------|
| **Latest** (selected by default) | Install the latest available version of the Cyber Protection agent. |
| **Previous stable** | Install the most recent stable version of the Cyber Protection agent from previous releases. |

4. Verify that the option **Automatically update agents** is switched on.

> **Note:** Automatic updates are only available for:
> - Cyber Protect agent versions 26986 (released in May 2021) or later.
> - Desktop Agent for File Sync & Share, version 15.0.30370 or later.
> Older agents must be updated manually to the latest version before automatic updates can take effect.

5. (Optional) Enable the maintenance window. The default window is daily, from 23:00 to 08:00 on the machine where the agent is installed.

> **Note:** Agent update processes are designed to be fast and seamless. We recommend choosing a time frame that will cause minimum disruption for users, as users cannot prevent or postpone automatic updates.

6. Click **Save**.

## Automatic updates for a single agent

1. Select **Settings** > **Agents**.
2. In the list of agents, select the agent for which you want to configure the auto update settings.
3. Under **Actions** in the upper right corner, click **Agent update settings**.
4. Under **Update channel**, select which version to use for automatic updates (Latest or Previous stable).
5. Verify that the option **Automatically update agents** is switched on.
6. (Optional) Enable the maintenance window.
7. Click **Save**.

## Configuring manual updates for all agents

1. Go to **Settings** > **Agents**.
2. In the upper-right corner, under **Actions**, click **Edit default agent update settings**.
3. Under **Update channel**, select which version to use.
4. Select **Manually update agents**.
5. (Optional) To prevent security risks from significantly outdated agents, select **Enforce automatic updates for unsupported versions**. Agents older than 6 months will be updated automatically during the specified maintenance window.

> **Important:** If you have not enabled the automated updates of agents before the C25.02 release, this option will be enabled automatically for all tenants in your environment.

6. Click **Save**.

## Configuring manual updates for selected agents

1. Go to **Settings** > **Agents**.
2. In the list of agents, select the ones for which you want to configure the automatic updates.
3. In the upper-right corner, under **Actions**, click **Agent update settings**.
4. Click **Edit default agent update settings**.
5. Under **Update channel**, select which version to use.
6. Select **Manually update agents**.
7. (Optional) Enable **Enforce automatic updates for unsupported versions**.
8. Click **Save**.

## Monitoring the auto update status

1. In the Cyber Protect console, go to **Settings** > **Agents**.
2. Click the gear icon in the upper right corner of the table, and ensure that **Auto-update** check box is selected.
3. Check the status in the **Auto-update** column.

## Removing the auto update settings

> **Important:** To ensure proper operation and robust protection of your workloads, we do not recommend disabling automatic updates of protection agents.

1. In the Cyber Protect console, go to **Settings** > **Agents**.
2. Select the scope for the settings:
   - To remove custom settings for all machines, click **Edit default agent update settings**.
   - To remove custom settings for specific machines, select the desired machines, and then click **Agent update settings**.
3. Click **Reset to default settings**, and then click **Save**.

## Updating protection agents on BitLocker-encrypted workloads

Agent updates that introduce changes to Startup Recovery Manager interfere with BitLocker on workloads on which both BitLocker and Startup Recovery Manager are enabled. In this case, after a restart, the BitLocker recovery key is required. To mitigate this issue, suspend or disable BitLocker before you update the agent.

**Affected agent versions:**

- 23.12.36943, released in December 2023
- 25.01.XXXXX released in January 2025
- 25.03.XXXXX released in March 2025

You can also check whether an update introduces changes to Startup Recovery Manager in the release notes of the protection agent.

**To update the agent on a workload with BitLocker and Startup Recovery Manager enabled:**

1. On the workload, suspend or disable BitLocker.
2. Update the agent.
3. Restart the workload.
4. Enable BitLocker.
