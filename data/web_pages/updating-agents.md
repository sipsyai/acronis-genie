# Updating protection agents

Installing and deploying Cyber Protection agents > Updating protection agents
Updating protection agents

You can update all agents manually either by using the Cyber Protect console or by downloading and running the installation file.

You can configure automatic updates for the following agents:

Agent for Windows
Agent for Linux
Agent for Mac
Cyber Files Cloud Agent for File Sync & Share
Free disk space that is required for the update

Free space is required to update an agent automatically or manually, by using the Cyber Protect console.

Operating System	Download location	Required disk space
Linux	/opt/acronis/Acroinst2/	3 GB
Mac	/Library/Application Support/Acronis/Acroinst2	2 GB
Windows

%ProgramData%\Acronis\Acroinst2\

%ProgramData%\Acronis\InstallationCache\

2 GB

[For all agents provided in the form of a virtual appliance, including Agent for VMware, Agent for Scale Computing, Agent for Virtuozzo Hybrid Infrastructure, Agent for RHV (oVirt)]

In order to perform automatic or manual update of a virtual appliance located behind a proxy, the proxy server must be configured on each appliance as follows.

In the /opt/acronis/etc/va-updater/config.yaml file, add the following line to the bottom of the file and enter the values specific to your environment:

httpProxy: http://proxy_login:proxy_password@proxy_address:port

Configuring the default method for updating agents

You can configure the default method for updating agents - manual or automatic, for all agents on all machines or on individual machines.

The default settings for agent updates are accessible from the Cyber Protection console and Management Portal, for all user roles.

Automatic updates
Manual updates
Monitoring the agent updates

To configure default settings for automatic updates for all agents in the Cyber Protect console

Select Settings > Agents.
In the upper-right corner, under Actions, click Edit default agent update settings.

Under Update channel, select which version to use for automatic updates.

Option	Description
Latest (selected by default)	Install the latest available version of the Cyber Protection agent.
Previous stable	Install the most recent stable version of the Cyber Protection agent from previous releases.

Verify that the option Automatically update agents is switched on.

Automatic updates are only available for the following agents:

Cyber Protect agent versions 26986 (released in May 2021) or later.

Desktop Agent for File Sync & Share, version 15.0.30370 or later.

Older agents must be updated manually to the latest version before automatic updates can take effect.

Set the maintenance window.
The default window is daily, from 23:00 to 08:00 on the machine where the agent is installed.

Although agent updates are fast and seamless, we recommend that you choose a time frame that will cause minimum disruption for users, because users cannot prevent or postpone automatic updates.

Click Save.

To configure default settings for automatic updates for selected agents in the Cyber Protect console.

Select Settings > Agents.
In the list of agents, select the ones for which you want to configure the automatic updates.
In the upper-right corner, under Actions, click Agent update settings.

Click Edit default agent update settings.

Under Update channel, select which version to use for automatic updates.

Option	Description
Latest (selected by default)	Install the latest available version of the Cyber Protection agent.
Previous stable	Install the most recent stable version of the Cyber Protection agent from previous releases.

Verify that the option Automatically update agents is switched on.

Automatic updates are only available for the following agents:

Cyber Protect agent versions 26986 (released in May 2021) or later.

Desktop Agent for File Sync & Share, version 15.0.30370 or later.

Older agents must be updated manually to the latest version before automatic updates can take effect.

Set the maintenance window.
The default window is daily, from 23:00 to 08:00 on the machine where the agent is installed.

Although agent updates are fast and seamless, we recommend that you choose a time frame that will cause minimum disruption for users, because users cannot prevent or postpone automatic updates.

Click Save.

Updating protection agents manually

Updating protection agents automatically

Updating protection agents on BitLocker-encrypted workloads

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.