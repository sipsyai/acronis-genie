---
title: "Built-in plans"
section: "Working with plans"
subsection: "Understanding plans"
page_range: "211-219"
tags: ["built-in", "plans", "protection", "monitoring", "remote-management", "essential", "extended", "complete"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#built-in-plans.html"
---

# Built-in plans

Built-in plans are plans that are preconfigured with some of the most commonly used or recommended settings. Built-in plans are available for selection out of the box. You cannot change built-in plans, but after applying a built-in plan to a workload, you can edit the settings.

Built-in plans are available for the following plan types: protection plans, monitoring plans, and remote management plans.

## Built-in protection plans

| Modules and settings | Essential protection | Extended protection | Complete protection | Backup entire workload |
|---------------------|---------------------|--------------------|--------------------|----------------------|
| **Description** | Minimal downtime and data loss, effortless recovery with short RPO and easy maintenance | Second level of protection: Business continuity, proactive mitigation of security risks and compliance | Third level of protection: Business continuity, near-zero RPO, proactive mitigation of security risks, data leaks prevention and compliance | Backs up the entire workload to the cloud |
| **Backup** | On | On | On | On |
| What to back up | Entire machine | Entire machine | Entire machine | Entire machine |
| CDP | Disabled | Disabled | Enabled | Enabled |
| Where to back up | Cloud storage | Cloud storage | Cloud storage | Cloud storage |
| Schedule | Mon-Fri at 12:00 PM | Mon-Fri at 12:00 AM | Mon-Fri at 12:00 AM | Mon-Fri at 12:00 AM |
| Backup scheme | Always incremental | Always incremental | Always incremental | Always incremental |
| How long to keep | Keep all backups 90 days | Keep all backups 90 days | Keep all backups 90 days | Keep all backups 90 days |
| **EDR** | Off | Off | On | |
| **Antivirus and Antimalware** | On | On | On | |
| Active Protection | On | On | On | |
| Advanced Antimalware | On | On | On | |
| Self protection | On | On | On | |
| Cryptomining process detection | On | On | On | |
| Quarantine cleanup | Remove after 30 days | Remove after 30 days | Remove after 30 days | |
| Exploit prevention | Notify and stop the process | Notify and stop the process | Notify and stop the process | |
| Real-time protection | Quarantine | Quarantine | Quarantine | |
| **URL filtering** | Off | On | On | |
| **Microsoft Defender Antivirus** | Off | Off | Off | |
| **Firewall management** | Off | On | On | |
| **Vulnerability assessment** | On | On | On | |
| Scope | Microsoft products, Windows third-party products, Apple products, macOS third-party products, Scan Linux package | Microsoft products, Windows third-party products, macOS products, macOS third-party products, Scan Linux package | Microsoft products, Windows third-party products, Apple products, macOS third-party products, Scan Linux package | |
| Schedule | At 11:00 AM, only on Wednesday and Friday | At 11:00 AM, only on Wednesday and Friday | At 11:00 AM, only on Wednesday and Friday | |
| **Patch management** | On | On | On | |
| Microsoft products | All updates | All updates | All updates | |
| Schedule | At 12:30 PM, only on Wednesday and Friday | At 12:30 PM, only on Wednesday and Friday | At 12:30 PM, only on Wednesday and Friday | |
| Pre-update backup | On | On | On | |
| **Data protection map** | Off | Off | On | |
| **Device control** | Off | Off | Off | |
| **Data Loss Prevention** | Off | Off | Off | |
| **Disaster Recovery** | Off | Off | Off | |

## Built-in monitoring plans

| Name | Description | Enabled monitors |
|------|-------------|-----------------|
| **Recommended monitoring for Windows** | Monitors the health and performance of Windows machines | Antimalware software status, Autorun feature status, CPU temperature, CPU usage, Disk space, Disk transfer rate, Failed logins, Firewall status, GPU temperature, Last system reboot, Memory usage, Network usage, Windows Update status (13 monitors) |
| **Recommended monitoring for macOS** | Monitors the health and performance of macOS machines | Antimalware software status, CPU temperature, CPU usage, Disk space, Disk transfer rate, Firewall status, GPU temperature, Last system reboot, Memory usage, Network usage (10 monitors) |
| **Recommended monitoring for servers** | Monitors the health and performance of Windows servers | Antimalware software status, CPU temperature (2 monitors: 80°/warning, 90°/critical), CPU usage (3 monitors: <20%/info, >80%/warning, >90%/critical), Disk space (2 monitors: <20%/warning, <10%/critical), Disk transfer rate, Failed logins (3 monitors: 5/info, 10/warning, 20/critical), Firewall status, Hardware changes, Installed software, Memory usage (3 monitors: <20%/info, >80%/warning, >90%/critical), Network usage, Windows Update status (20 monitors) |

## Built-in remote management plans

| Name | Description | Settings |
|------|-------------|----------|
| **Essential remote desktop** | Enables the remote desktop and file transfer capabilities | **Connection protocols:** Allow connections via NEAR: On, Allow connections via RDP: On, Allow connections via Apple Screen Sharing: Off. **NEAR security settings:** Lock workload when user disconnects: Off, Allow only one user at a time: Off, Allow workload administrator to connect to any session: On, Allow system session creation: Off, Allow clipboard synchronization: On. **Security settings:** Show if workload is controlled remotely: On, Ask for user's permission to take screenshots: On. **Workload management:** File transfer: On, Screenshots transmission: Off. **Display settings:** Desktop Deduplication: On, OpenCL acceleration: On, Hardware H.264 encoding: On. **Toolbox:** Show last logged-in users: Off |
