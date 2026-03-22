# Updating protection agents automatically

Installing and deploying Cyber Protection agents > Updating protection agents > Updating protection agents automatically
Updating protection agents automatically

To facilitate the management of multiple workloads, you can configure automatic updates for Agent for Windows, Agent for Linux, and Agent for Mac. Automatic updates are available for agents version 26986 (released in May 2021) or later. Older agents must be updated manually to the latest version first.

The configuration of automatic updates for a protection agent overrides the Agent uninstallation protection setting in all protection plans for the agent.

Automatic updates are supported on machines running any of the following operating systems:

Windows XP SP 3 and later
Red Hat Enterprise Linux 6 and later, CentOS 6 and later
OS X 10.9 Mavericks and later

The settings for automatic updates are preconfigured on a data center level. A partner or company administrator can customize these settings – for all machines in a company or a unit, or for individual machines. If no custom settings are applied, then the settings from the upper level are used, in this order:

Cyber Protection data center
Company (customer tenant)
Unit
Machine

For example, a unit administrator can configure custom auto-update settings for all machines in the unit, which might differ from the setting applied to the machines on the company level. The administrator can also configure different settings for one or more individual machines in the unit, to which neither the unit settings nor the company settings will be applied.

Even within the enabled maintenance window, updates will not be installed while the agent is running any of the following operations:
Backup
Recovery
Backup replication
Virtual machine replication
Testing a replica
Running a virtual machine from backup (including finalization)
Disaster recovery failover
Disaster recovery failback
Running a script (for Cyber Scripting functionality)
Patch installation
ESXi configuration backup
Automatic updates for all agents
Automatic updates for a single agent
Monitoring the auto update status
Removing the auto update settings

To configure the automatic updates of agents from the Cyber Protection console

Select Settings > Agents.

Under Actions in the upper right corner, click Edit default agent update settings.

Under Update channel, select which version to use for automatic updates.

Option	Description
Latest (selected by default)	Install the latest available version of the Cyber Protection agent.
Previous stable	Install the most recent stable version of the Cyber Protection agent from previous releases.

Verify that the option Automatically update agents is switched on.

Automatic updates are only available for the following agents:

Cyber Protect agent versions 26986 (released in May 2021) or later.

Desktop Agent for File Sync & Share, version 15.0.30370 or later.

Older agents must be updated manually to the latest version before automatic updates can take effect.

Enable the maintenance window.
The default window is daily, from 23:00 to 08:00 o'clock on the machine where the agent is installed.

Despite that the agent update processes are designed to be fast and seamless, we recommend choosing a time frame which will cause minimum disruption for users, as users cannot prevent or postpone automatic updates.

Click Save.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.