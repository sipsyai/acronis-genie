---
title: "Alert types and categories - Disaster recovery alerts"
section: "Understanding your current level of protection"
subsection: "Alerts"
page_range: "299-307"
tags: ["alerts", "disaster-recovery", "failover", "failback", "VPN", "quota", "licensing", "troubleshooting"]
acronis_version: "26.02"
---

# Disaster recovery alerts

| Alert type | Description | How to resolve the alert |
|------------|-------------|------------------------|
| **Soft quota for Cloud servers reached** | Generated when the soft quota for the Disaster recovery storage is exceeded. | Increase the quota or remove some backups from the cloud storage. |
| **Soft quota is reached** | Generated when the soft quota is exceeded for Cloud server, Compute points, or Public IP addresses. | |
| **Storage quota is exceeded** | Generated when the hard quota for the Disaster recovery storage is exceeded. This storage is used by primary and recovery servers. If overage for this quota is reached, it is not possible to create primary and recovery servers, or to add or extend disks. If the overage is exceeded, it is not possible to perform a failover or to just start a stopped server. Running servers continue to run. | Contact your partner to increase the assigned quota. |
| **Hard quota is exceeded** | Generated when the hard quota for Cloud servers, Compute points, or Public IP addresses is exceeded. | Consider purchasing additional quotas or disable backup tasks for the devices you no longer need to protect. |
| **Failover error** | Generated when a system problem occurs after a failover was initiated. | 1. Select the recovery server, and then click **Edit**. 2. Decrease CPU/RAM of the recovery server. 3. Try to perform a failover again. |
| **Test failover error** | Generated when a system problem occurs after a test failover was initiated. | 1. Select the recovery server, and then click **Edit**. 2. Decrease CPU/RAM of the recovery server. 3. Try to perform a test failover again. **Note:** Ensure that the IP address in production network is the same as the IP address configured in the DHCP server. |
| **Failback error** | Generated when a system problem occurs after a failback was initiated. | You can see the erroneous location in the list of backup storages: it has a number instead of a name. Remove the erroneous location: 1. In the Cyber Protect console, go to **Backup Storage**. 2. Find the location and click the cross (x) icon to delete it. 3. Confirm your choice by clicking **Delete**. 4. Retry the failover. |
| **Failback error: backup failed** | Generated when backing up the recovery server during failback process failed. | |
| **Failback error: switchover failed** | Generated when the failback process returned to the data transfer stage, and the virtual machine in the cloud was started. | Try performing switchover again. If it fails, contact the support team. |
| **Failback is canceled** | Generated when a failback was canceled by a user. | Manually dismiss the alert from the console. |
| **VPN connection error** | Generated when a VPN connection failure occurs due to reasons not related to the user's actions. Status report from VPN appliance is outdated. | Contact the Support team. Include in your email: Screenshots of error messages, Screenshot of the Acronis VPN Appliance CLI interface, your Acronis Backup Cloud data center and group name. |
| **(Vpn Unreachable) Connectivity gateway is not reachable** | Generated when the Disaster Recovery service cannot reach the connectivity gateway. Status report from connectivity gateway is outdated. | Contact the Support team with relevant screenshots and details. |
| **IPsec VPN connection error** | Generated when there is an error during IKE (Internet Key Exchange) Phase 1 negotiation. | Check the IPsec IKE settings on the Cloud and Local site. |
| **DR IP reassignment required** | Generated when the VPN appliance detects network changes. | Reassign the IP address. See "Reassigning IP addresses" (p. 970). |
| **Connectivity gateway failure** | Generated when the deployment of the VPN server in the cloud failed. | Use Connection Verification Tool and check its output for errors. Allow Acronis software through application control of your firewalls and antimalware software. |
| **Primary server creation failure** | Generated when the primary server was not created due to an error. | |
| **Recovery server creation failure** | Generated when the recovery server was not created due to an error. | Ensure the recovery server matches the Software requirements for Disaster Recovery to Cyber Protect Cloud. |
| **Delete Primary Server** | Generated when a primary server is deleted. | |
| **Server recovery failure** | Generated when the primary or recovery server failed to recover. | Find the details. If the error message is generic, navigate to **Disaster Recovery** → **Servers**, click to select the affected machine, and then click **Activities**. Click an activity, hold CTRL and left-click the activity. Click the ellipsis (...) icon and then click **Task activity info**. |
| **Backup failed** | Generated when a backup of cloud server (primary or server in the production failover state) failed. | 1. Verify the connection to the backup location. 2. Check the backup storage device (local backups). |
| **Network limit exceeds** | Generated when the maximum number of cloud networks is reached (5 networks). | Remove or edit the cloud networks to ensure that they match the local network settings. |
| **Runbook failure** | Generated when the runbook execution failed. | This does not affect the product functionality, and it can be safely ignored. See "Creating a runbook" (p. 1011). |
| **Runbook warning** | Generated when the runbook execution completed with warnings. | This does not affect the product functionality. |
| **Runbook User Interaction Required** | Generated when the runbook is waiting for a user interaction. | Perform the action described in the **User action** section. |
| **Internet traffic blocked** | Generated when, due to security risks, an administrator blocks the internet traffic for one or more of the public IPs in your account. | Contact the support team. |
| **Internet traffic unblocked** | Generated when the internet traffic for your account was unblocked by an administrator. | |
| **Local networks overlap** | Generated when identical or overlapping local networks is detected. | Check the configuration of the VPN appliance. |
| **Various licensing alerts** | Multiple alert types related to licensing switches for server quotas, offering items, compute points, and disaster recovery storage being insufficient, exceeded, or disabled. | Contact your partner to increase the assigned quota. |
| **Failback data transfer error** | Generated when data transfer phase of the failback fails. | Retry the operation. If it fails again, contact the Support team. |
| **Failback failed** | Generated when there is an error in the failback. | Remove the erroneous location from Backup Storage and start failover again. |
| **Failback confirming failed** | Generated when the failback confirmation failed. | Retry the operation. If it fails again, contact the support team. |
| **Failback machine is ready for switchover** | Generated when the machine is ready for switchover. More than 90% of the data is transferred to the local site. | |
| **Failback switchover finished** | Generated when the switchover is successful. The virtual machine is restored on the local site. | Manually dismiss the alert from the console. |
| **Failback target agent offline** | Generated when the agent that is used in the failback process is offline. | Ensure that the agent has Internet access. If necessary, restart the agent. |
