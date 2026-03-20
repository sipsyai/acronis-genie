---
title: "Understanding plans"
section: "Working with plans"
subsection: null
page_range: "208-210"
tags: ["plans", "overview", "plan-types", "modules", "protection", "monitoring", "scripting"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#understanding-plans.html"
---

# Understanding plans

> **Note:** The availability of some of the features depends on the offering items that are enabled for your account, and the administration level in the Cyber Protect console.

A plan is a set of configurations and rules that you can apply on one or several workloads to achieve different goals, such as backing up a workload, protecting a workload from malware, monitoring the workload performance, etc.

A plan consists of modules that you can enable or disable. Each module contains settings that are related to a specific functionality.

All plans that you created are visible on the **Management** tab.

## Plan types

| Plan | Description | Partner | Customer | Unit |
|------|-------------|---------|----------|------|
| **Protection plan** | Protects the data on the workload. At the partner level, includes: Antivirus and Antimalware protection, Vulnerability assessment, Patch management. At the customer and unit level, includes: Backup, Disaster Recovery, EDR, Antivirus and Antimalware protection, URL filtering, Windows Defender Antivirus, Microsoft Security Essentials, Vulnerability assessment, Patch management, Data protection map, Device control, Data Loss Prevention. | Yes (with limitations) | Yes | Yes |
| **Remote management plan** | Enables the remote desktop and assistance functionality on your managed workloads. | Yes | Yes | Yes |
| **Scripting plan** | Enables script execution on multiple workloads, scheduled script execution, and additional script settings. | Yes | Yes | Yes |
| **Monitoring plan** | Monitors the performance, hardware, software, system, and security parameters of your managed workloads. | Yes | Yes | Yes |
| **Software deployment plan** | Automates the software deployment process and ensures consistent software distribution across your managed workloads. | Yes | Yes | Yes |
| **Cloud applications backup** | Backs up applications running in the cloud by means of agents that run in the cloud and uses the cloud storage as a backup location. | No | Yes | Yes |
| **Archiving plan** | With email archiving, all emails in a Microsoft 365 organization are retained in an external archive that is stored in the cloud. New emails are added to the archive continuously. | Yes | Yes | No |
| **Backup scanning plan** | Scans backups for malware (including ransomware). | No | Yes | Yes |
| **SIEM forwarding plan** | Configures how Acronis alerts, events, tasks, and audit log information are forwarded to third-party Security Event and Incident Management (SIEM) platforms. | Yes | No | No |
| **Backup replication** | Replicates a backup to another location. | No | Yes | Yes |
| **Validation** | Validates a backup and verifies that the data from the backup can be recovered. | No | Yes | Yes |
| **Cleanup** | Deletes outdated backups according to the retention rules. Only applicable to agents and workloads, and not cloud to cloud backups. | No | Yes | Yes |
| **Conversion to VM** | Checks if a backup includes the system volume and contains all information necessary for the OS to start so that the resulting virtual machine can start on its own. | No | Yes | Yes |
| **VM replication** | Scans backups for malware (including ransomware). Replication of virtual machines. | No | Yes | Yes |
