# Protection settings

Installing and deploying Cyber Protection agents > Protection settings
Protection settings

To configure the general protection settings for Cyber Protection, in the Cyber Protect console, go to Settings > Protection.

Automatic updates for components

By default, all agents can connect to the Internet and download updates.

An administrator can minimize the network bandwidth traffic by selecting one or several agents in the environment and assigning the Updater role to them. Thus, the dedicated agents will connect to the Internet and download updates. All other agents will connect to the dedicated updater agents by using peer-to-peer technology, and then download the updates from them.

The agents without the Updater role will connect to the Internet if there is no dedicated updater agent in the environment, or if the connection to a dedicated updater agent cannot be established for about five minutes.

The updater agent distributes updates and patches for Antivirus and Antimalware protection, Vulnerability assessment, and Patch management, but does not include updates of the agent version.

An agent with the Updater role can download and distribute patches only for Windows third-party products. For Microsoft products, patch distribution is not supported by the Updater agent.

Before assigning the Updater role to an agent, ensure that the machine on which the agent runs is powerful enough, and has a stable high-speed Internet connection and enough disk space.

To prepare a machine for the Updater role

On agent machine where you plan to enable the Updater role, apply the following firewall rules:
Inbound (incoming) "updater_incoming_tcp_ports": allow connection to TCP ports 18018 and 6888 for all firewall profiles (public, private, and domain).
Inbound (incoming) "updater_incoming_udp_ports": allow connection to UDP port 6888 for all firewall profiles (public, private, and domain).

Restart the Acronis Agent Core Service.

Restart the Firewall Service.

If you do not apply these rules and the firewall is enabled, peer agents will download the updates from the Cloud.

To assign the Updater role to a protection agent

In the Cyber Protect console, go to Settings > Agents.
Select the machine with the agent to which you want to assign the Updater role.
Click Details, and then enable the Use this agent to download and distribute patches and updates switch.

The peer-to-peer update works as follows.

The agent with the Updater role checks by schedule the index file provided by the service provider to update the core components.
The agent with the Updater role starts to download and distribute updates to all agents.

You can assign the Updater role to multiple agents in the environment. Thus, if an agent with the Updater role is offline, other agents with this role can serve as the source for definition updates.

Automatic collection of performance data

On protected machines running Microsoft Windows, company administrators can enable or disable the automatic collection of performance logs. Data collection starts if the performance of the system drops under expected thresholds for a set period of up to 3600 seconds. The set period is specified on the platform, and the performance thresholds are configured on the machine where the protection agent runs.

The automatic collection of performance logs is disabled by default.

To enable the automatic collection of performance data

Required role: Company administrator

In the Cyber Protect console, go to Settings > Agents.
Select the machine on which you want to enable the performance monitor.
Click Details, and then enable the Allow this agent to automatically collect performance logs switch.

The performance monitor works as follows.

The Protection agent monitors several performance metrics on the machine (like memory usage and CPU load).
If the metrics drop under certain threshold for a certain time period, the agent collects an ETL trace.
An alert (info) indicates that performance data collection has started.

The automatic collection lasts for 1 hour (3600 seconds) and this period cannot be modified.

An alert (info) indicates that performance data collection has ended.

The automatically collected data is stored on the local disk of the protected machine, in folder C:\ProgramData\Acronis\ETLTool\ETL\

Updating the Cyber Protection definitions by schedule

On the Schedule tab, you can set up the schedule for automatic update of the Cyber Protection definitions for each of the following components:

Antimalware
Vulnerability assessment
Patch management

To change the definition updates setting, navigate to Settings > Protection > Protection definitions update > Schedule.

Schedule type:

Daily – define on which days of the week to update definitions.

Start at – select at what time to update definitions.

Hourly – define more granular hourly schedule for updates.

Run every – define the periodicity of updates.

From... To – define a specific time range for the updates.

Updating the Cyber Protection definitions on-demand

To update the Cyber Protection definitions for a particular machine on-demand

In the Cyber Protect console, go to Settings > Agents.
Select the machines on which you want to update the protection definitions, and then click Update definitions.
Cache storage

The location of cached data is the following:

On Windows machines: C:\ProgramData\Acronis\Agent\var\atp-downloader\Cache
On Linux machines: /opt/acronis/var/atp-downloader/Cache
On macOS machines: /Library/Application Support/Acronis/Agent/var/atp-downloader/Cache

To change the cache storage setting, navigate to Settings > Protection > Protection definitions update > Cache Storage.

In Outdated update files and patch management data, specify after what period to remove cached data.

Maximum cache storage size (GB) for agents:

Updater role – define storage size for cache on the machines with the Updater role.
Other roles – define storage size for cache on other machines.
Cyber Protection collects samples of detected malware for additional analysis so that we can improve our software. You can change this setting at any time in the Protection tab, by disabling the Collect and upload malware samples to CPOC toggle.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.