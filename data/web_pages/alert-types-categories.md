# Alert types and categories

Understanding your current level of protection > Monitoring > The Alerts dashboard > Alert types and categories
Alert types and categories

The alert types are grouped by the following categories:

Backup alerts
Disaster recovery alerts
Antimalware protection alerts
URL Filtering alerts
Licensing alerts
EDR alerts
Device Control alerts
System alerts
Public Clouds connection alerts
Software deployment alerts
Management
Search
Monitoring
Backup alerts
Alert type	Description	How to resolve the alert
Backup failed	The alert is generated when a backup failed with a resolvable error or it was interrupted due to system shut down.	Check the log of the backup operation. Click the workload to select it, and then click Activities to find the warning in the log. The message should point you to the root cause of the issue.
Backup succeeded with warnings	The alert is generated when a backup succeeded with warnings.

Check the log of the backup operation. Click the workload to select it, and then click Activities to find the warning in the log. The message should point you to the root cause of the issue.


Backup is canceled	The alert is generated every time a backup is manually canceled by the user.	You can either start the backup manually by clicking Run now or wait until it runs at the next scheduled time.
Backup canceled due to closed backup window	The alert is generated when the backup activity was missed because it did not fit in the window specified in the backup options.	Re-configure the schedule or edit options of the backup plan in the Performance and backup window. Expand the section with your product for instructions.
Backup is waiting	The alert is generated when there is a scheduling conflict and two backup tasks are initiated at the same time. In this case, the second backup task is queued until the first one is finished or stopped.	Ensure that your backups are running in the expected time windows and according to their schedule, and avoid scheduling conflicts.
Backup is not responding	The alert is generated when a backup has not shown any progress for some time, and might be frozen.	The issue might be caused by a lockup. For more information, see this knowledge base article.
Backup did not start	The alert is generated when the scheduled backup failed to start for unknown reason.

Ensure that you are using the latest build of your Acronis Backup product.

If the agent machine was available during the backup start time:

Edit the backup task start time.

If the alert appears again, recreate the backup task.

If the newly created backup task also triggers the alert, contact the Support team for assistance.

If the agent was offline:

Do not turn off machine during backup time.

If the machine was not turned off, ensure that Acronis Managed Machine Service is running: Start -> Search -> services.msc -> locate Acronis Managed Machine Service. If you need assistance, contact the Support team.


Backup status is unknown	The alert is generated when the backup agent was offline at a scheduled backup time. The status of the resource backups will be unknown until the backup agent comes online.

Check if the agent is expected to be offline (for example, it is a notebook that is outside the Management Server network).

If the agent should not be offline, ensure that Acronis Managed Machine Service is running: Start -> Search -> services.msc -> locate Acronis Managed Machine Service and check its status. If the service is stopped, start it.


Backup is missing	The alert is generated when there has not been a successful backup for more than [Days from last backup] days, which is defined in the Alerts backup option.	Ensure that the plan with enabled Alerts backup option is scheduled and runs at least once within the defined period configured for this option
Backup is corrupted	The alert is generated when the validation activity is successful and shows that the backup is corrupted.

Follow steps from article Troubleshooting Issues with Corrupt Backups.

If you need assistance with identifying the root cause for archive corruption, contact the Support team.


Continuous Data Protection failed	The alert is generated if the continuous protection of backup failed.

Verify the following limitations:

Continuous data protection is supported only for the NTFS file system and the following operating systems:

Desktop: Windows 7 and later

Server: Windows Server 2008 R2 and later

CDP does not support Acronis Secure Zone as a destination.

NFS folders that are mounted on Windows are not supported.

Continuous replication is not supported: if there are two locations in the protection plan, CDP slices are created only in the first destination, and then the changes are replicated to the second one with the next backup.

If changes in a local protected folder are applied from a network source (for example, when users access the folder from the network), CDP does not detect them.

If a file is being used (for example, some changes are being made in an Excel file), CDP does not detect the changes. For the changes to be detected by CDP, save them, and then close the file.


Validation failed	The alert is generated when the validation process of the backup cannot be completed.	Check the log of the failed operation. Click the workload to select it, and then click Activities to find the warning in the log. The message should point you to the root cause of the issue.
Encryption password is missing	The alert is generated when the database encryption key is incorrect, corrupt, or missing.	There is no way to recover encrypted backups if you lose or forget the password. You must set the encryption password locally, on the protected device. You cannot set the encryption password in the protection plan. For more information, see Setting the encryption password.
Upload is pending	The alert is generated if scheduled check finds that Physical Data Shipping to cloud archive for this backup plan is not uploaded to the storage.
Backup recovery failed

The alert is generated when the recovery operation fails when you try to recover files or system backups.

Determine the exact date of the backup failure and attempt recovery with the last successful backup.
Disaster recovery alerts
Alert type	Description	How to resolve the alert
Soft quota for Cloud servers reached	The alert is generated when the soft quota for the Disaster recovery storage is exceeded.	Increase the quota or remove some backups from the cloud storage.
Soft quota is reached

The alert is generated when the soft quota is exceeded for the following offering items:

Cloud server.
Compute points.
Public IP addresses.

Storage quota is exceeded

The alert is generated when the hard quota for the Disaster recovery storage is exceeded.

This storage is used by primary and recovery servers. If the overage for this quota is reached, it is not possible to create primary and recovery servers, or to add or extend disks of the existing primary servers. If the overage for this quota is exceeded, it is not possible to perform a failover or to just start a stopped server. Running servers continue to run.

Contact your partner to increase the assigned quota.
Hard quota is exceeded

The alert is generated when the hard quota for the following offering items is exceeded:

Cloud servers.

Compute points.

Public IP addresses.

Consider purchasing additional quotas or disable backup tasks for the devices you no longer need to protect.
Failover error	The alert is generated when a system problem occurs after a failover was initiated.

Select the recovery server, and then click Edit.

Decrease CPU/RAM of the recovery server.

Try to perform a failover again.


Test failover error	The alert is generated when a system problem occurs after a test failover was initiated.

Select the recovery server, and then click Edit.

Decrease CPU/RAM of the recovery server.

Try to perform a test failover again.

Ensure that the IP address in production network is the same as the IP address that is configured in the DHCP server.

Failback error	The alert is generated when a system problem occurs after a failback was initiated.

You can see the erroneous location in the list of backup storages: it has a number instead of a name (normally, a location name matches one of the existing end user names) and you have not created this location. Remove the erroneous location:

In the Cyber Protect console, go to Backup Storage.

Find the location and click the cross (x) icon to delete it.

Confirm your choice by clicking Delete.

Retry the failover.


Failback error: backup failed	This alert is generated when backing up the recovery server during failback process failed.
Failback error: switchover failed.	This alert is generated when the failback process returned to the data transfer stage, and the virtual machine in the cloud was started.	Try performing switchover again. If it fails, contact the support team.
Failback is canceled	The alert is generated when a failback was canceled by a user.	Manually dismiss the alert from the console.
VPN connection error	The alert is generated when a VPN connection failure occurs due to reasons that are not related to the user's actions. Status report from VPN appliance is outdated.

If you faced an issue while deploying or connecting the Acronis VPN appliance, contact the Support team.

Include the following information in your email:

Screenshots of the error messages (if there are any)

Screenshot of the Acronis VPN Appliance CLI interface

Your Acronis Backup Cloud data center and group name.


(Vpn Unreachable) Connectivity gateway is not reachable	The alert is generated when the Disaster Recovery service cannot reach the connectivity gateway. Status report from connectivity gateway is outdated.

In case you have faced an issue with deploying or connecting the Acronis VPN appliance, contact the Support team.

Include the following information in your email:

Screenshots of the error messages (if there are any)

Screenshot of the Acronis VPN Appliance CLI interface

Your Acronis Backup Cloud data center and group name


IPsec VPN connection error	This alert is generated when there is an error during IKE (Internet Key Exchange) Phase 1 negotiation.	Check the IPsec IKE (Internet Key Exchange) settings on the Cloud and Local site.
DR IP reassignment required	The alert is generated when the VPN appliance detects network changes.	Reassign the IP address. For more information, see Reassigning IP addresses
Connectivity gateway failure	The alert is generated when the deployment of the VPN server in the cloud failed.

Use Connection Verification Tool and check its output for errors.

Allow Acronis software through application control of your firewalls and antimalware software.


Primary server creation failure	The alert is generated when the primary server was not created due to an error.
Recovery server creation failure	The alert is generated when the recovery server was not created due to an error.	Ensure the recovery server matches the Software requirements. For more information, see Software requirements for Disaster Recovery to Cyber Protect Cloud.
Delete Primary Server	The alert is generated when a primary server is deleted.
Server recovery failure	The alert is generated when the primary or recovery server failed to recover.	Find the details. If the error message is generic or unclear (for example "Internal error") navigate to Disaster Recovery → Servers, click to select the affected machine, and then click Activities. Click an activity, hold CTRL and left-click the activity. Click the ellipsis (...) icon of the activity, and then click Task activity info.
Backup failed	The alert is generated when a backup of cloud server (primary or server in the production failover state) failed.

Verify the connection to the backup location.

Check the backup storage device (local backups).


Network limit exceeds	The alert is generated when the maximum number of cloud networks is reached (5 networks).	Remove or edit the cloud networks to ensure that they match the local network settings.
Runbook failure	The alert is generated when the runbook execution failed.	This does not affect the product functionality, and it can be safely ignored. For more information, see Creating a runbook.
Runbook warning	The alert is generated when the runbook execution completed with warnings.	This does not affect the product functionality, and it can be safely ignored. For more information, see Creating a runbook.
Runbook User Interaction Required	The alert is generated when the runbook is waiting for a user interaction.	This does not affect the product functionality, and it can be safely ignored. Alternatively, you can perform the action that is described in the User action section. For more information, see Creating a runbook.
Internet traffic blocked	The alert is generated when, due to security risks, an administrator blocks the internet traffic for one or more of the public IPs in your account.	Contact the support team.
Internet traffic unblocked	The alert is generated when the internet traffic for your account was unblocked by an administrator.
Local networks overlap	The alert is generated when identical or overlapping local networks is detected.	Check the configuration of the VPN appliance.
Licensing switch insufficient server quota	The alert is generated when the cloud servers quota is not enough.

If the alert is generated for a physical server, ensure that the tenant and user have sufficient quota for the Web hosting servers or Servers offering items.

If the alert is generated for a virtual server, ensure that the tenant and user have sufficient quota for the Web hosting servers or Virtual machines offering items. A virtual server cannot use the quota for the Servers offering item.


Licensing switch insufficient offering item	The alert is generated when the Disaster recovery storage offering item is disabled.
Licensing switch error	The alert is generated when the disaster recovery upgrade encountered an error.	Contact the Support team.
Licensing switch insufficient compute points	The alert is generated when there are no compute points available.	Increase the hard quota for the Compute points offering item.
Licensing switch insufficient servers offering items	The alert is generated when the Cloud servers offering item is disabled.
Policy failed to create recovery server	The alert is generated when an error occurs while setting up the disaster recovery infrastructure.	Manually create a recovery server, without the Internet Access property. For more information, see Creating a recovery server.
Backup processor auto test failover rescheduled	The alert is generated when the automated test failover was rescheduled.

Start a test failover of the recovery server manually. For more information, see Performing a test failover.

Wait for the next scheduled date for the automatic test failover.


Backup processor auto test failover timeout reached

The alert is generated when the automated test failover expired.

Each automated test failover consumes compute points.


Increase the timeout value for automated test failover.

Wait for the next scheduled date for the automatic test failover.

Start a test failover of the recovery server manually. For more information, see Performing a test failover.


Backup processor auto test failover overall failure	The alert is generated when the last scheduled automated test failover of the recovery server failed.

Start a test failover of the recover server manually. For more information, see Performing a test failover.

Wait for the next scheduled date when automatic test failover will be performed.


Automated test failover warning	This alert is generated when the backup is encrypted.	Enter the encryption password in the recovery server settings.
Automated test failover error	This alert is generated when an automated test failover failed.	Enter the encryption password for the backup in the recovery server settings. The operation will start again.
Automated test failover failed - offering item quota exceeded

This alert is generated when the automated test failover failed. The recovery server is no longer licensed due to exceeded hard quota for one of the following offering items:

DR and direct backup to Azure

DR to Acronis or hybrid cloud

Workstations

Virtual machines

Servers

Contact your partner to increase the assigned quota.
Automated test failover failed - offering item disabled

This alert is generated when the automated test failover failed. The recovery server is no longer licensed because one of the following offering items was disabled:

Workstations

Virtual machines

Servers

Contact your partner to increase the assigned quota.
Disaster Recovery protection was disabled for a workload

This alert is generated when Disaster Recovery protection was disabled for a worklad because the hard quota was exceeded for one of the following offering items:

DR and direct backup to Azure

DR to Acronis or hybrid cloud

Contact your partner to increase the assigned quota.
Recovery server is unlicensed

This alert is generated when the recovery server is no longer licensed because the hard quota was exceeded for one of the following offering items:

DR and direct backup to Azure

DR to Acronis or hybrid cloud

Contact your partner to increase the assigned quota.
Primary server is unlicensed

This alert is generated when the primary server is no longer licensed because:

the hard quota for the Primary Servers offering item was exceeded.

the Primary Servers offering item was disabled.

Contact your partner to increase the assigned quota.
Recovery server is unlicensed - offering item quota exceeded

This alert is generated when the recovery server is no longer licensed due to exceeded hard quota for one of the following offering items:

Workstations

Virtual machines

Servers

The disaster recovery operations might be limited or unsupported.

Contact your partner to increase the assigned quota.
Recovery server is unlicensed - offering item disabled

This alert is generated when the recovery server is no longer licensed because one of the following offering items was disabled:

Workstations

Virtual machines

Servers

The disaster recovery operations might be limited or unsupported.

Contact your partner to increase the assigned quota.
Failback data transfer error	The alert is generated when data transfer phase of the failback fails.	Retry the operation. If it fails again, contact the Support team.
Failback failed

The alert is generated when there is an error in the failback.



You can see the erroneous location in the list of backup storages: it has a number instead of a name (normally, a location name matches one of the existing end users names) and you have not created this location. Remove the erroneous location:

In Cyber Protection, go to Backup Storage.

Find the location, and then click the cross (x) icon to delete it.

Confirm your choice by clicking Delete.
Start failover again.

Failback confirming failed	The alert is generated when the failback confirmation failed.	Retry the operation. If it fails again, contact the support team.
Failback machine is ready for switchover	The alert is generated when the machine is ready for switchover. More than 90% of the data is transferred to the local site.
Failback switchover finished	The alert is generated when the switchover is successful. The virtual machine is restored on the local site.	Manually dismiss the alert from the console.
Failback target agent offline	The alert is generated when the agent that is used in the failback process is offline.	Ensure that the agent has Internet access. If necessary, restart the agent.
Duplicated WebCP client_id	This alert is generated when there is a duplicated client_id for a resource.
Azure deployment restored from recycle bin	This alert is generated when the disaster recovery infrastructure was restored from the Recycle bin. The recovery servers in production failover were stopped.
Deployment restored from recycle bin	This alert is generated when the disaster recovery infrastructure was restored from the Recycle bin. The primary and recovery servers in production failover were stopped.
Azure resource group deletion skipped	This alert is generated when an Azure resource group could not be deleted due to a cloud connection issue.
Antimalware protection alerts
Alert type	Description	How to resolve the alert
Prevented agent uninstall/update attempt	The alert is generated on every attempt to manually update or uninstall a protection agent outside the specified maintenance period, when the Agent uninstallation protection option is enabled for the agent.	Manually dismiss the alert from the console.

See To allow the modification of an agent with uninstallation protection enabled.


Suspicious remote connection activity is detected	The alert is generated when ransomware coming from a remote connection is detected.	Manually dismiss the alert from the console.
Suspicious activity is detected

The alert is generated when ransomware is detected in the workload.



Manually dismiss the alert from the console. to deactivate the alert.

Depending on the option you have specified in Active Protection plan, the malicious process is stopped, the changes made by the process are reverted or none actions have been taken yet and you need to resolve this issue manually.

Read the details of the alert to check which process is encrypting files and which files are affected.

If you decide that the process encrypting the files is sanctioned (false-positive alert), add this process to the Trusted processes:

Open Active Protection plan.

Click Edit to modify the settings.

In Trusted processes, specify trusted processes that will never be considered ransomware. Specify the full path to the process executable, starting with the drive letter.

For example: C:\Windows\Temp\er76s7sdkh.exe


Cryptomining activity is detected	The alert is generated when Illicit cryptominers are detected in the workload.	Manually dismiss the alert from the console.
MBR defence: Suspicious activity is detected and suspended

The alert is generated when ransomware is detected in the workload (specifically MBR / GPT partition is modified by ransomware).

Manually dismiss the alert from the console.
Unsupported network path is specified	The alert is generated when the recovery path provided by the administrator is not a local folder path.	Specify the local path for network folder protection (recovery path). Manually dismiss the alert from the console.
Critical process is added as harmful to the Active Protection plan	The alert is generated when a critical process is added as a blocked process in the Protection exclusions list.	Contact the administrator to remove the critical process from the Exclusions list.
Failed to apply Active Protection policy	The alert is generated when Active Protection policy failed to be applied.	Check the error message to see why Active Protection policy cannot be applied.
Secure Zone: Unauthorized operation is detected and blocked	The alert is generated when ransomware is detected in the workload (ASZ partition is modified by ransomware).	Manually dismiss the alert from the console.
Active Protection service is not running	The alert is generated when the Active Protection service crashed or is not running.	Check the error message to see why Active Protection service is not running.
Active Protection service is not available	The alert is generated when the Active Protection service is not available because a driver is incompatible or missing.	Check Windows event logs for crashes of Acronis Active Protection service (acronis_protection_service.exe).
Conflict with another security solution	An alert is generated if Active Protection is not available for machine '{{resourceName}}' because a conflict with another security solution was detected. To enable Active Protection, disable or uninstall the conflicting security solution.

Solution 1: If you want to use Acronis real-time protection, uninstall the third-party antivirus software from the workload.

Solution 2: If you want to use the third-party antivirus, in the protection plan that is applied to the workload, disable Acronis real-time protection, URL filtering, and Windows defender antivirus.


Quarantine action failed	The alert is generated when antimalware failed to quarantine a detected malware.	Check the error message to see why quarantine failed.
Malicious process is detected	The alert is generated when a malware (process type) is detected by Behavior engine. The detected malware is quarantined.	Manually dismiss the alert from the console.
Malicious process is detected, but not quarantined	The alert is generated when a malware (process type) is detected by Behavior engine. The detected malware is not quarantined.	Manually dismiss the alert from the console.
Malware is detected and blocked (ODS)	The alert is generated when a malware is detected by scheduled scan. The detected malware is quarantined.	Manually dismiss the alert from the console.
Malware is detected and blocked (RTP)	The alert is generated when a malware is detected by Real-Time protection. The detected malware is quarantined.	Manually dismiss the alert from the console.
Malware is detected in a backup	The alert is generated when a malware is detected during backup scanning.	Manually dismiss the alert from the console.
Conflict detected between Real-time antimalware protection and a security product	The alert is generated when antimalware failed to register with Windows Security Center.	Solution 1: If you want to use Acronis real-time protection, uninstall the third-party antivirus software from the workload.

Solution 2: If you want to use the third-party antivirus, in the protection plan that is applied to the workload, disable Acronis real-time protection, URL filtering, and Windows defender antivirus.


Failed to run the Microsoft Security Essentials module	The alert is generated when the Microsoft Security Essentials module failed to run.	Check the error message to see why Microsoft Security Essentials module failed to run.
Real-time protection is not available because third-party antivirus software is installed	The alert is generated when Real-time protection failed to turn on, because third-party antivirus has Real-time protection enabled.	Disable or uninstall third-party security product, or disable Real-time antimalware protection in the protection plan.
Real-time protection is not available due to incompatible or missing driver	The alert is generated when Real-time protection is not available, due to an incompatible or missing driver.	Check the error message to see why the installation of the driver on the workload failed.
Cyber Protection (or Active Protection) service is not responding	The alert is generated when the Cyber Protection service responds to a health check ping from the console.
Security definition update failed	The alert is generated when a security definition update failed.	Check the error message to see why the security definition update failed.
Tamper Protection is enabled	The alert is generated when the Microsoft Defender settings cannot be changed because tamper protection is enabled.	Disable Tamper Protection settings on the Windows workload.
Windows Defender module execution failed	The alert is generated when the Windows Defender module execution failed.	Check the error message to see why the Windows defender module failed to run.
Windows Defender is blocked by a third-party antivirus software	The alert is generated when Windows Defender is blocked because a third-party antivirus software is installed on the machine.	Disable or uninstall the third-party security product.
Group policy conflict	The alert is generated when the Microsoft Defender settings cannot be changed because they are controlled by a group policy.	Disable the group policy settings on the Windows workload.
Microsoft Security Essentials took action to protect this machine from malware	The alert is generated when Microsoft Security Essentials deleted or quarantined a malware.	Manually dismiss the alert from the console.
Microsoft Security Essentials detected malware	The alert is generated when Microsoft Security Essentials detected malware or other potentially unwanted software.	Manually dismiss the alert from the console.
Malware detected in M365 mailbox backup	The alert is generated when malware is detected during backup scanning.	Manually dismiss the alert from the console.
Behavior engine is not available	This alert is generated when Behavior engine is not available on a workload because a driver is incompatible or missing.	Ensure that the driver is installed properly on the workload.
Potentially unwanted application was detected	This alert is generated when a potentially unwanted application is detected.	Manually dismiss the alert from the console.
Backup scanning for malware did not start	This alert is generated when backup scanning does not run on schedule.	Check error message, why backup scanning did not start.
URL Filtering alerts
Alert type	Description	How to resolve the alert
Malicious URL was blocked	The alert is generated when a malicious URL is blocked by URL filtering.	Check the URL filtering settings. URL filtering is blocking pages which are supposed to be blocked, according to the URL filtering settings. For more information, see URL filtering.
A malicious URL warning was ignored

The alert is generated when you selected to proceed with the malicious URL blocked by URL filtering.

Check the URL filtering settings.
Conflict detected between URL filtering and a security product	The alert is generated when the URL filtering cannot be enabled, due to a conflict with another security product.	Check the URL filtering settings.
Website URL is blocked

The alert is generated when a URL meets all the criteria specified in the blocked category for URL filtering.

Check the URL filtering settings.
A malicious URL is detected in an email	This alert is generated when URL filtering detected a malicious URL in a M365 mailbox backup. Action on detection for URL filtering is set to Notify only.	Check the URL filtering settings.
A malicious URL was detected	This alert is generated when the URL filtering detected a malicious URL. Action on detection for URL filtering is set to Notify only.	Check the URL filtering settings.
Unable to connect to the URL filtering web browser extension	This alert is generated when Browser protection is enabled in the protection plan, a previous connection to the browser extension was successful, but the extension is currently disconnected.	Click Get support to view the KB article.
Browser protection is almost ready	This alert is generated when Browser protection setup is incomplete. The required registry keys are created, but no connection to the web browser extension has been detected.	Close all browser windows and restart the web browser. Ensure that no browser processes are running in the background.
Licensing alerts
Alert type	Description	How to resolve the alert
Storage quota almost reached	The alert is generated when the usage drops below 80% (after cleanup or quota upgrade).

Purchase additional storage or free some space in your cloud storage.


Storage quota exceeded

The alert is generated when all 100% of the storage quota is used.

Buy more storage space. For more information, see this knowledge base article.
Workload quota reached	The alert is generated when usage for offering item > 0 and usage > quota, but usage <= quota + overage.
Workload quota exceeded

The alert is generated when the usage for offering item > quota + overage.


The workload has no quota to apply a backup plan (resource has no service quota)

The alert is generated when:

The quota was removed manually: Device > Details > Service quota, and then click Change and select the No quota option.

The Management Console offering item is disabled.

The Management Console quota+overage value of the offering item is decreased below current usage.


Cannot protect a workload with assigned quota

The alert is generated when the offering item is not sufficient, and you need to have:

a dynamic group.

a backup plan assigned to that group.

a resource that falls to that dynamic group, but has some qualities that forbid applying the same backup plan to it.


Subscription license expired	The alert is generated when a license expired.

After a subscription expires, all product functionality, except recovery, is blocked until a subscription renewal. Backed up data is still accessible for recovery.

Purchase a new license.

If you have recently purchased a new subscription but still receive the message that your subscription is expired, import the new subscription from the Acronis Account: In the management console, go to Settings -> Licenses, and then in the top right corner, click Sync. Subscriptions will be synchronized.

Subscription license will expire soon	The alert is generated if a license will expire in less than 30 days.	Purchase a new subscription.
EDR alerts
Alert type	Description	How to resolve the alert
Incident Detected	The alert is generated when an incident is created or when the status for an existing incident is updated.	This alert informs you about a new incident or an old incident that has been updated. You can view the alert and close it. You can choose to open the incident for further investigation.
Indicator of compromise (IOCs) detected

The alert is generated when a new indicator of compromise was detected by the EDR IOC threat search service.

This alert is to inform you that an IOC has been detected on one or many workloads. You will view the alert and then you can click on the link in the alert to view details about the IOC.
Failed to isolate the workload from the network	The alert is generated when the user triggers the action to isolate the machine from network, and isolation action fails.	Take the necessary actions.
Failed to reconnect the workload to the network

The alert is generated when the user triggers the action to reconnect the machine back to network, and the action failed.

Take the necessary actions.
Windows Defender Firewall settings was modified	The alert is generated when the settings to the firewall were modified on an isolated machine.	This alert is to inform you that firewall details were modified on the isolated machine. It is informative only and you can close the alert after viewing it.
Device Control alerts
Alert type	Description	How to resolve the alert
Device control and Data loss prevention will run with limited functionality (Incompatible CPU detected)	The alert is generated when the DeviceLock agent started on physical machine with CPU which has supporting for CET technology.	Disable the option on the affected machines to avoid these alerts.
Device control functionality is not yet supported on macOS Ventura	The alert is generated when DeviceLock agent started on physical macOS Ventura machine, and the protection plan with Device Control is applied to the agent. Applicable only for versions when there is a problem with the kernel panic due DeviceLock driver.
Allowed transfer of sensitive data	The alert is generated if transferring for sensitivity content is allowed.
Justified transfer of sensitive data	The alert is generated if transferring sensitivity content is justified.
Denied transfer of sensitive data	The alert is generated if transferring sensitivity content is blocked.
Review the results of Data Loss Prevention observation mode

The alert is generated when it is time to review the Observation results:

DLP license is not applied.

A month passed since the Observation mode was enabled in any protection plan that is applied to at least one workload.

A month has passed since the last similar alert was raised and some usage of DLP in Observation mode is detected.


Security identifier was changed for user	The alert is generated when a SID is updated for a known username. This might happen when the operating system is reinstalled on a non-domain workload.
Peripheral device access is blocked	The alert is generated when some actions (read/write operations) for supported devices are blocked.
Unable to connect to a remote SSL resource.	The alert is generated when the access to a remote SSL resource is blocked due to additional handshake prevention used at the resource.	Add the resource to the allowlist for remote hosts.
System alerts
Alert type	Description	How to resolve the alert
Agent is outdated	The alert is generated when the agent version is outdated.	Go to the Agents list and update the agent.
Automatic update failed

The alert is generated when the auto update of the agent failed.

Try to perform a manual update.
You need to restart device after installing a new agent	The alert is generated when a restart is required after a successful remote installation.	Restart the workload.
You need to restart device after updating the agent	The alert is generated when a restart is required after a successful local installation.	Restart the workload.
Activity failed

The alert is generated when an activity failed.

Restart all Acronis services on the workload.
Activity succeeded with warnings	The alert is generated when an activity was successful but some warnings were generated.
Activity is not responding	The alert is generated when an activity in progress is not responding.
Plan deployment failed	The alert is generated when the protection plan deployment failed.
Failed to convert user name to SID	The alert is generated when the schedule SID conversion failed.
Machine is offline for more than 20 days

This alert is generated when there has been no connection to a workload for more than 20 days. Backups of the workload will be stopped if the connection is not restored before the offline status reaches 30 days.


Machine is offline for more than 30 days	This alert is generated when there has been no connection to a workload for more than 30 days. Backups of the workload are stopped. To resume the backups, restore the connection to the workload.
Prevented agent uninstall/update	This alert is generated when the Active Protection service terminated an attempt to uninstall or update the protection agent.	Click Allow for 1 hour to enable the operation.
Protection plan conflict detected	This alert is generated when there is a conflict between a protection plan applied to a workload and a protection plan from a dynamic group.
Protection failure detected	This alert is generated when some drivers on a workload are not functioning properly and the Antivirus and Antimalware protection module is temporarily unavailable.
Not enough disk space	This alert is generated when installation of an agent failed due to insufficient disk space on a workload.	Free up some disk space and restart the installation.
Restart required to complete the agent installation	This alert is generated when installation of an agent completed successfully and a restart is required to apply the changes.
Agent installation cannot be started due to the operating system pending reboot	This alert is generated when installation of an agent cannot be started because the workload is waiting for a reboot.
Agent installation failed due to the operating system pending reboot	This alert is generated when installation of an agent failed because the workload requires a reboot.
Automatic update failed	This alert is generated when an automatic update of the agent installed on a workload has failed and it is now suspended.	Update the agent manually.
Automatic update stalled	This alert is generated when the automatic update to another version on a workload has failed. The system will automatically retry the update.
Agent is offline	This alert is generated when a scheduled plan was not run because the agent was offline.
Public clouds connection alerts
Alert type	Description	How to resolve the alert
Access to Azure subscription will expire soon	The alert is generated one month before the connection token for Azure subscription expires.	Go to Infrastructure > Public clouds, select the Azure subscription, and then click Renew access.
Access to Azure subscription expired

The alert is generated when the connection token for Azure subscription expires.

Go to Infrastructure > Public clouds, select the Azure subscription, and then click Renew access.
New version of agent for Azure is available	The alert is generated when there is a new version of Agent for Azure.	Go to Infrastructure > Public clouds, select the Azure subscription, and then click Update for Agent for Azure.
The version of Agent for Azure will reach end of life soon	This alert is generated when a version of Agent for Azure will reach end of life after one release (monthly release).	Go to Infrastructure > Public clouds, select the Azure subscription, and then click Update for Agent for Azure.
The version of Agent for Azure has reached end of life	This alert is generated when a version of Agent for Azure has reached end of life.	Go to Infrastructure > Public clouds, select the Azure subscription, and then click Update for Agent for Azure.
Agent for Azure configuration failed	This alert is generated when the Agent for Azure configuration failed. Go to the Activities tab.	Go to Infrastructure > Public clouds, select the Azure subscription, and then check the Activities tab for details.
Agent for Azure is in status Failed	This alert is generated when the Agent for Azure is in status Failed. Check the status of the Azure virtual machine.	Go to Infrastructure > Public clouds, select the Azure subscription, and then check the Agent for Azure tab for details and the link to Microsoft Azure portal to manage the virtual machine.
Agent for Azure update failed	This alert is generated when the Agent for Azure update failed and the Agent for Azure version is reverted back to the previous version.	Go to Infrastructure > Public clouds, select the Azure subscription, and then check the Activities tab for details.
Agent for Azure deletion failed	This alert is generated when the Agent for Azure was not deleted successfully.	Go to Infrastructure > Public clouds, select the Azure subscription, and then check the Agent for Azure tab for details, for the link to Microsoft Azure portal where you can perform the deletion operation for the virtual machine, and for the corresponding resource groups.
Agent for Azure deallocation failed	This alert is generated when an unused agent for Azure was not deleted.	Go to Infrastructure > Public clouds, select the Azure subscription and check the Agent for Azure tab for details, for a link to Microsoft Azure portal where you can perform the deletion operation for the virtual machine, and for the corresponding resource groups.
Access to S3 public cloud expiring	This alert is generated one month before the connection token for access to Amazon S3 or another S3-compatible public cloud expires.	Go to Infrastructure > Public clouds, select the Amazon S3/S3-compatible connection in the list, and then click Renew access.
Access to S3 public cloud expired	This alert is generated when the connection token for access to Amazon S3 or another S3-compatible public cloud expires.	Go to Infrastructure > Public clouds, select the Amazon S3/S3-compatible connection in the list, and then click Renew access.

Software deployment alerts
Alert type	Description
Software package incompatibility detected

This is a critical alert that is generated when a software package cannot be installed because it is not compatible with the target workload's operating system.


Attempt to install missing software	This is a critical alert that is generated when a software deployment plan attempts to install a software package that not found in the repository.
Attempt to uninstall missing software	This is a critical alert that is generated when a software deployment plan attempts to uninstall a software package that not found in the repository.
Reboot required after software installation	This is a warning alert that is generated when the installation of the software package requires a reboot of the target workload's operating system.
Reboot required after software uninstallation	This is a warning alert that is generated when the uninstallation of the software package requires a reboot of the target workload's operating system.

Management
Alert type	Description
Pending restart

This alert is generated when a device has not been restarted for 7 days, following successful software deployment.


Vulnerability scan failed	This is a warning alert that is generated when a vulnerability assessment scan has failed due to an error.
Patch installation failed	This is a warning alert that is generated when a patch management installation has failed due to en error.
PM reboot required	This is a warning alert that is generated when a reboot of the system is required to complete the patch installation process.
Remote desktop connection failed	This alert is generated when connection to a remote workload cannot be established due to an error.
Credentials missing	This is a warning alert that is generated when a script cannot run on a workload due to missing credentials for the script.
Script execution failed

This is a critical alert that is generated when:

a script cannot run because it has the status 'Draft'.

a script is not in the script repository.

a script cannot run because it is not possible to download its dependencies.

a script takes too long to run on a workload.

a script cannot run on a workload because the script executor went offline.


Firewall preferences

This is a warning alert that is generated when:

the Microsoft Defender settings were modified.

the Microsoft Defender settings are locked and cannot be changed due to an internal error.


Firewall local rules disabled	This is a warning alert that is generated when the local rules for firewall management are disabled.
Package incompatible	This is a critical alert that is generated when software cannot be installed because it is not compatible with the operating system of the target workload.
Missing package install	This is a critical alert that is generated when software cannot be installed because it is missing.
Missing package uninstall	This is a critical alert that is generated when software cannot be uninstalled because it is missing.
Reboot required package install	This is a warning alert that is generated when a reboot is required to complete the software installation.
Reboot required package uninstall	This is a warning alert that is generated when a reboot is required to complete the software uninstallation.

Search
Alert type	Description	How to resolve the alert
Search indexing failed	This alert is generated when the index failed to build for Microsoft 365 email archive.	Try to update or rebuild the index.
Search item deletion failed	This alert is generated when an item failed to be deleted from Microsoft 365 email archive due to an error in the retention rules.

Monitoring
Alert type	Description
Disk failure is possible	This is a warning alert that is generated when a disk on a workoad is likely to fail in the future.
Disk failure is imminent	This is a critical alert that is generated when a disk on a workload is in a critical state and will fail soon.
Data collection failed	This alert is generated when the monitor failed to collect data for a workload due to an error.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.