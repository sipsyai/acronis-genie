---
title: "Service quota, protection settings, and system information"
section: "Installing and deploying Cyber Protection agents"
subsection: "Service quota, protection settings, Cyber Protection services, and system information"
page_range: "202-207"
tags: ["service quota", "protection settings", "Updater role", "performance data", "definitions update", "cache storage", "services", "system information"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#protection-settings.html"
---

# Service quota, protection settings, and system information

## Changing the service quota of workloads

A service quota is automatically assigned when a protection plan is applied to a workload for the first time. The most appropriate quota is assigned, depending on the type of the protected workload, its operating system, required level of protection, and the quota availability.

### Examples of quota assignment

- A physical machine running a Windows Server or Linux operating system is assigned the **Servers** quota.
- A physical machine running a Windows desktop operating system is assigned the **Workstations** quota.
- A physical machine running Windows 10 with enabled Hyper-V role is assigned the **Workstations** quota.
- A desktop machine on a virtual desktop infrastructure with the protection agent installed inside the guest OS is assigned the **Virtual machines** quota (can also use **Workstations** quota if Virtual machines quota is not available).
- A desktop machine on a virtual desktop infrastructure backed up in agentless mode (e.g., by Agent for VMware or Agent for Hyper-V) is assigned the **Virtual machines** quota.
- A Hyper-V or vSphere server is assigned the **Servers** quota.
- A server with cPanel or Plesk is assigned the **Web Hosting Servers** quota (can also use **Virtual machines** or **Servers** quota).
- The application-aware backup requires the **Servers** quota, even for a workstation.

You can manually change the original assignment later. If the features required by a protection plan are not supported by the currently assigned service quota, the protection plan will fail.

### To change the service quota of an individual workload

1. In the Cyber Protect console, go to **Devices**.
2. Select a workload, and then click **Details**.
3. In the **Service quota** section, click **Change**.
4. In the **Change quota** window, select the service quota or **No quota**, and then click **Change**.

### To change the service quota for a group of workloads

1. In the Cyber Protect console, go to **Devices**.
2. Select more than one workloads, and then click **Assign quota**.
3. In the **Change quota** window, select the service quota or **No quota**, and then click **Change**.

## Protection settings

To configure the general protection settings for Cyber Protection, in the Cyber Protect console, go to **Settings** > **Protection**.

### Automatic updates for components

By default, all agents can connect to the Internet and download updates. An administrator can minimize the network bandwidth traffic by selecting one or several agents in the environment and assigning the Updater role to them. The dedicated agents will connect to the Internet and download updates. All other agents will connect to the dedicated updater agents by using peer-to-peer technology, and download the updates from them.

The agents without the Updater role will connect to the Internet if there is no dedicated updater agent in the environment, or if the connection to a dedicated updater agent cannot be established for about five minutes.

The updater agent distributes updates and patches for Antivirus and Antimalware protection, Vulnerability assessment, and Patch management, but does not include updates of the agent version.

> **Note:** An agent with the Updater role can download and distribute patches only for Windows third-party products. For Microsoft products, patch distribution is not supported by the Updater agent.

### To prepare a machine for the Updater role

1. On an agent machine where you plan to enable the Updater role, apply the following firewall rules:
   - Inbound (incoming) "updater_incoming_tcp_ports": allow connection to TCP ports 18018 and 6888 for all firewall profiles (public, private, and domain).
   - Inbound (incoming) "updater_incoming_udp_ports": allow connection to UDP port 6888 for all firewall profiles.
2. Restart the Acronis Agent Core Service.
3. Restart the Firewall Service.

### To assign the Updater role to a protection agent

1. In the Cyber Protect console, go to **Settings** > **Agents**.
2. Select the machine with the agent to which you want to assign the Updater role.
3. Click **Details**, and then enable the **Use this agent to download and distribute patches and updates** switch.

### Automatic collection of performance data

On protected machines running Microsoft Windows, company administrators can enable or disable the automatic collection of performance logs. Data collection starts if the performance of the system drops under expected thresholds for a set period of up to 3600 seconds. The automatic collection is disabled by default.

### To enable the automatic collection of performance data

Required role: Company administrator

1. In the Cyber Protect console, go to **Settings** > **Agents**.
2. Select the machine on which you want to enable the performance monitor.
3. Click **Details**, and then enable the **Allow this agent to automatically collect performance logs** switch.

The performance monitor works as follows:

1. The Protection agent monitors several performance metrics (memory usage and CPU load).
2. If the metrics drop under a certain threshold for a certain time period, the agent collects an ETL trace.
3. An alert (info) indicates that performance data collection has started. The automatic collection lasts for 1 hour (3600 seconds) and cannot be modified.
4. An alert (info) indicates that performance data collection has ended. The collected data is stored at `C:\ProgramData\Acronis\ETLTool\ETL\`.

### Updating the Cyber Protection definitions by schedule

On the **Schedule** tab, you can set up the schedule for automatic update of the Cyber Protection definitions for each of the following components:

- Antimalware
- Vulnerability assessment
- Patch management

To change the setting, navigate to **Settings** > **Protection** > **Protection definitions update** > **Schedule**.

**Schedule type:**

- **Daily** -- define on which days of the week to update definitions. **Start at** -- select the time to update.
- **Hourly** -- define more granular hourly schedule for updates. **Run every** -- define the periodicity. **From... To** -- define a specific time range.

### Updating the Cyber Protection definitions on-demand

1. In the Cyber Protect console, go to **Settings** > **Agents**.
2. Select the machines on which you want to update the protection definitions, and then click **Update definitions**.

### Cache storage

The location of cached data is the following:

- On Windows machines: `C:\ProgramData\Acronis\Agent\var\atp-downloader\Cache`
- On Linux machines: `/opt/acronis/var/atp-downloader/Cache`
- On macOS machines: `/Library/Application Support/Acronis/Agent/var/atp-downloader/Cache`

To change the cache storage setting, navigate to **Settings** > **Protection** > **Protection definitions update** > **Cache Storage**.

In **Outdated update files and patch management data**, specify after what period to remove cached data.

**Maximum cache storage size (GB) for agents:**

- **Updater role** -- define storage size for cache on the machines with the Updater role.
- **Other roles** -- define storage size for cache on other machines.

> **Note:** Cyber Protection collects samples of detected malware for additional analysis. You can change this setting at any time in the **Protection** tab, by disabling the **Collect and upload malware samples to CPOC** toggle.

## Cyber Protection services installed in your environment

Cyber Protection installs some or all of the following services, depending on the Cyber Protection options that you use.

### Services installed in Windows

| Service name | Purpose |
|-------------|---------|
| Acronis Managed Machine Service | Provides backup, recovery, replication, retention, validation functionality |
| Acronis Scheduler2 Service | Executes scheduled tasks on certain events |
| Acronis Active Protection Service | Provides protection against ransomware |
| Acronis Cyber Protection Service | Provides antimalware protection |

### Services installed in macOS

| Service name and location | Purpose |
|--------------------------|---------|
| `/Library/LaunchDaemons/com.acronis.aakore.plist` | Communication between agent and management components |
| `/Library/LaunchDaemons/com.acronis.cyber-protect-service.plist` | Detection of malware |
| `/Library/LaunchDaemons/com.acronis.mms.plist` | Backup and recovery functionality |
| `/Library/LaunchDaemons/com.acronis.schedule.plist` | Executes scheduled tasks |

## Collecting system information

You can save an agent log to a .zip file. If a backup fails for an unknown reason, this file will help the technical support personnel to identify the problem.

By default, the information in the log is optimized for the last three days, but you can change this period.

### Collect from the Cyber Protect console

1. Do one of the following:
   - Under **Devices**, select the workload from which you want to collect the logs, and then click **Activities**.
   - Under **Settings** > **Agents**, select the workload from which you want to collect the logs, and then click **Details**.
2. (Optional) To change the default period, click the arrow next to the **Collect system information** button, and then select the period.
3. Click **Collect system information**.
4. If prompted by your web browser, specify where to save the file.

### Collect locally

This procedure is applicable for workloads that are offline and bootable media.

- Follow the steps in the Acronis knowledge base article for collecting agent logs locally.
