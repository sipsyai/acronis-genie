# Updating protection agents manually

Installing and deploying Cyber Protection agents > Updating protection agents > Updating protection agents manually
Updating protection agents manually

You can update agents either by using the Cyber Protect console or by downloading and running the installation file.

Virtual appliances with the following versions must be updated only by using the Cyber Protect console:

Agent for VMware (Virtual Appliance): version 12.5.23094 and later.
Agent for Virtuozzo Hybrid Infrastructure (Virtual Appliance): version 12.5.23094 and later.

Agents with the following versions can also be updated by using the Cyber Protect console:

Agent for Windows, Agent for VMware (Windows), Agent for Hyper-V: version 12.5.21670 and later.
Agent for Linux: version 12.5.23094 and later.
Other agents: version 12.5.23094 and later.

To update earlier agent versions of those agents, download and install the newest version manually. To find the download links, click All devices > Add.

To find the agent version, in the Cyber Protect console, select the machine, and then click Details.

Prerequisites

On Windows machines, Cyber Protect features require Microsoft Visual C++ 2017 Redistributable. Ensure that it is already installed on your machine or install it before updating the agent. After the installation, a restart may be required. You can find the Microsoft Visual C++ Redistributable package on the Microsoft website: https://support.microsoft.com/help/2999226/update-for-universal-c-runtime-in-windows.

To update an agent by using the Cyber Protect console

[For protection plans created after November 2024] The uninstallation and modification of the protection agents for Windows is prohibited by default. Agent for Windows can be modified only during a maintenance window or through the agent auto update functionality. For instructions on how to enable the one-time uninstallation or modification of an agent, see To allow the modification of an agent with uninstallation protection enabled. Do disable the agent uninstallation protection, see To disable agent uninstallation protection.

Click Settings > Agents.

The list of protected machines appears. The machines with outdated agent versions are marked with an orange exclamation mark.

Select the machines that you want to update the agents on.

The machines must be online.
Click Update agent.

During the update, any backups that are in progress will fail.

To update the Cyber Protection definitions on a machine

Click Settings > Agents.
Select the machine on which you want to update the Cyber Protection definitions and click Update definitions. The machine must be online.

To assign the Updater role to an agent

Click Settings > Agents.

Select the machine to which you want to assign the Updater role, click Details, and then in the Cyber Protection definitions section, enable Use this agent to download and distribute patches and updates.

An agent with the Updater role can download and distribute patches only for Windows third-party products. For Microsoft products, patch distribution is not supported by the Updater agent.

To clear cached data on an agent

Click Settings > Agents.
Select the machine on which you want to clear the cached data (outdated update files and patch management data) and click Clear cache.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.