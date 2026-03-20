---
title: "Alert types - System, Public Clouds, Software deployment, Management, Search, Monitoring"
section: "Understanding your current level of protection"
subsection: "Alerts"
page_range: "316-324"
tags: ["alerts", "system", "public-clouds", "Azure", "S3", "software-deployment", "management", "monitoring", "disk-health"]
acronis_version: "26.02"
---

# System alerts

| Alert type | Description | How to resolve |
|------------|-------------|----------------|
| **Agent is outdated** | The agent version is outdated. | Go to the Agents list and update the agent. |
| **Automatic update failed** | The auto update of the agent failed. | Try to perform a manual update. |
| **You need to restart device after installing/updating a new agent** | A restart is required after a successful remote or local installation. | Restart the workload. |
| **Activity failed** | An activity failed. | Restart all Acronis services on the workload. |
| **Activity succeeded with warnings** | An activity was successful but some warnings were generated. | |
| **Activity is not responding** | An activity in progress is not responding. | |
| **Plan deployment failed** | The protection plan deployment failed. | |
| **Failed to convert user name to SID** | The schedule SID conversion failed. | |
| **Machine is offline for more than 20 days** | No connection to a workload for more than 20 days. Backups will be stopped if the connection is not restored before 30 days. | |
| **Machine is offline for more than 30 days** | No connection to a workload for more than 30 days. Backups of the workload are stopped. | To resume the backups, restore the connection to the workload. |
| **Prevented agent uninstall/update** | The Active Protection service terminated an attempt to uninstall or update the protection agent. | Click **Allow for 1 hour** to enable the operation. |
| **Protection plan conflict detected** | A conflict between a protection plan applied to a workload and a protection plan from a dynamic group. | |
| **Protection failure detected** | Some drivers on a workload are not functioning properly and the Antivirus and Antimalware protection module is temporarily unavailable. | |
| **Not enough disk space** | Installation of an agent failed due to insufficient disk space on a workload. | Free up some disk space and restart the installation. |
| **Restart required to complete the agent installation** | Installation completed successfully and a restart is required. | |
| **Agent installation cannot be started due to pending reboot** | Installation cannot be started because the workload is waiting for a reboot. | |
| **Agent installation failed due to pending reboot** | Installation failed because the workload requires a reboot. | |
| **Automatic update failed (suspended)** | An automatic update of the agent installed on a workload has failed and is now suspended. | Update the agent manually. |
| **Automatic update stalled** | The automatic update to another version on a workload has failed. The system will automatically retry. | |
| **Agent is offline** | A scheduled plan was not run because the agent was offline. | |

---

# Public Clouds connection alerts

| Alert type | Description | How to resolve |
|------------|-------------|----------------|
| **Access to Azure subscription will expire soon** | Connection token for Azure subscription will expire in one month. | Go to **Infrastructure** > **Public clouds**, select the Azure subscription, and then click **Renew access**. |
| **Access to Azure subscription expired** | Connection token for Azure subscription has expired. | Go to **Infrastructure** > **Public clouds**, select the Azure subscription, and then click **Renew access**. |
| **New version of agent for Azure is available** | A new version of Agent for Azure is available. | Go to **Infrastructure** > **Public clouds**, select the Azure subscription, and then click **Update** for Agent for Azure. |
| **Agent for Azure version will reach / has reached end of life** | Agent for Azure will reach or has reached end of life. | Update Agent for Azure via **Infrastructure** > **Public clouds**. |
| **Agent for Azure configuration/update/deletion failed** | Agent for Azure configuration, update, or deletion operations failed. | Go to **Infrastructure** > **Public clouds** and check the **Activities** tab for details. |
| **Agent for Azure is in status Failed** | Agent for Azure is in status Failed. | Check the **Agent for Azure** tab for details and the link to Microsoft Azure portal. |
| **Agent for Azure deallocation failed** | An unused Agent for Azure was not deleted. | Check the **Agent for Azure** tab for a link to Microsoft Azure portal. |
| **Access to S3 public cloud expiring / expired** | Connection token for Amazon S3 or another S3-compatible public cloud will expire or has expired. | Go to **Infrastructure** > **Public clouds**, select the S3 connection, and then click **Renew access**. |

---

# Software deployment alerts

| Alert type | Description |
|------------|-------------|
| **Software package incompatibility detected** | A software package cannot be installed because it is not compatible with the target workload's OS. |
| **Attempt to install missing software** | A software deployment plan attempts to install a software package that is not found in the repository. |
| **Attempt to uninstall missing software** | A software deployment plan attempts to uninstall a software package that is not found in the repository. |
| **Reboot required after software installation/uninstallation** | The installation or uninstallation of the software package requires a reboot of the target workload's OS. |

---

# Management alerts

| Alert type | Description |
|------------|-------------|
| **Pending restart** | A device has not been restarted for 7 days following successful software deployment. |
| **Vulnerability scan failed** | A vulnerability assessment scan has failed due to an error. |
| **Patch installation failed** | A patch management installation has failed due to an error. |
| **PM reboot required** | A reboot is required to complete the patch installation process. |
| **Remote desktop connection failed** | Connection to a remote workload cannot be established due to an error. |
| **Credentials missing** | A script cannot run on a workload due to missing credentials. |
| **Script execution failed** | A script cannot run (status 'Draft', not in repository, dependencies unavailable, takes too long, or script executor went offline). |
| **Firewall preferences** | Microsoft Defender settings were modified, locked, or cannot be changed due to internal error. |
| **Firewall local rules disabled** | Local rules for firewall management are disabled. |
| **Package incompatible / Missing package install/uninstall** | Software cannot be installed or uninstalled because it is not compatible or missing. |
| **Reboot required package install/uninstall** | A reboot is required to complete the software installation or uninstallation. |

---

# Search alerts

| Alert type | Description | How to resolve |
|------------|-------------|----------------|
| **Search indexing failed** | The index failed to build for Microsoft 365 email archive. | Try to update or rebuild the index. |
| **Search item deletion failed** | An item failed to be deleted from Microsoft 365 email archive due to an error in the retention rules. | |

---

# Monitoring alerts

| Alert type | Description |
|------------|-------------|
| **Disk failure is possible** | A warning alert generated when a disk on a workload is likely to fail in the future. |
| **Disk failure is imminent** | A critical alert generated when a disk on a workload is in a critical state and will fail soon. |
| **Data collection failed** | Generated when the monitor failed to collect data for a workload due to an error. |

---

# Alert widgets

In the alert widgets, you can see the following details of alerts related to your workload:

| Field | Description |
|-------|-------------|
| **5 latest alerts widget** | A list of five latest alerts. |
| **Historical alerts summary** | A graphical widget showing alerts by alert severity, alert type and the time range. |
| **Active alerts summary** | A graphical widget showing active alerts by alert severity and alert type, as well as the sum of active alerts. |
| **Alerts history** | A table view of historical alerts. |
| **Active alerts details** | A table view of active alerts. |
