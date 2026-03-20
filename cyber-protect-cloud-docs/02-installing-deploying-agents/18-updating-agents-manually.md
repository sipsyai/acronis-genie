---
title: "Updating protection agents manually"
section: "Installing and deploying Cyber Protection agents"
subsection: "Updating protection agents manually"
page_range: "124-125"
tags: ["update", "agents", "manual", "Cyber Protect console", "definitions", "Updater role", "cache"]
acronis_version: "26.02"
---

# Updating protection agents manually

You can update agents either by using the Cyber Protect console or by downloading and running the installation file.

## Version requirements for console updates

Virtual appliances with the following versions must be updated only by using the Cyber Protect console:

- Agent for VMware (Virtual Appliance): version 12.5.23094 and later
- Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance): version 12.5.23094 and later

Agents with the following versions can also be updated by using the Cyber Protect console:

- Agent for Windows, Agent for VMware (Windows), Agent for Hyper-V: version 12.5.21670 and later
- Agent for Linux: version 12.5.23094 and later
- Other agents: version 12.5.23094 and later

To update earlier agent versions, download and install the newest version manually. To find the download links, click **All devices** > **Add**. To find the agent version, select the machine in the Cyber Protect console and click **Details**.

## Prerequisites

On Windows machines, Cyber Protect features require Microsoft Visual C++ 2017 Redistributable. Ensure it is already installed on your machine before updating the agent. After installation, a restart may be required. You can find the package on the Microsoft website: https://support.microsoft.com/help/2999226/update-for-universal-c-runtime-in-windows.

> **Note:** For protection plans created after November 2024, the uninstallation and modification of the protection agents for Windows is prohibited by default. Agent for Windows can be modified only during a maintenance window or through the agent auto update functionality. See "Preventing unauthorized uninstallation or modification of agents" for more details.

## To update an agent by using the Cyber Protect console

1. Click **Settings** > **Agents**. The list of protected machines appears. Machines with outdated agent versions are marked with an orange exclamation mark.
2. Select the machines that you want to update on. The machines must be online.
3. Click **Update agent**. During the update, any backups that are in progress will fail.

## To update the Cyber Protection definitions on a machine

1. Click **Settings** > **Agents**.
2. Select the machine on which you want to update the Cyber Protection definitions and click **Update definitions**. The machine must be online.

## To assign the Updater role to an agent

1. Click **Settings** > **Agents**.
2. Select the machine to which you want to assign the Updater role, click **Details**, and then in the **Cyber Protection definitions** section, enable **Use this agent to download and distribute patches and updates**.

> **Note:** An agent with the Updater role can download and distribute patches only for Windows third-party products. For Microsoft products, patch distribution is not supported by the Updater agent.

## To clear cached data on an agent

1. Click **Settings** > **Agents**.
2. Select the machine on which you want to clear the cached data (outdated update files and patch management data) and click **Clear cache**.
