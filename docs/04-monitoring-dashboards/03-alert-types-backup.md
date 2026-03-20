---
title: "Alert types and categories - Backup alerts"
section: "Understanding your current level of protection"
subsection: "Alerts"
page_range: "295-298"
tags: ["alerts", "backup", "alert-types", "troubleshooting", "CDP", "validation", "encryption"]
acronis_version: "26.02"
---

# Alert types and categories

The alert types are grouped by the following categories:

- Backup alerts
- Disaster recovery alerts
- Antimalware protection alerts
- URL Filtering alerts
- Licensing alerts
- EDR alerts
- Device Control alerts
- System alerts
- Public Clouds connection alerts
- Software deployment alerts
- Management
- Search
- Monitoring

## Backup alerts

| Alert type | Description | How to resolve the alert |
|------------|-------------|------------------------|
| **Backup failed** | Generated when a backup failed with a resolvable error or it was interrupted due to system shut down. | Check the log of the backup operation. Click the workload to select it, and then click **Activities** to find the warning in the log. The message should point you to the root cause of the issue. |
| **Backup succeeded with warnings** | Generated when a backup succeeded with warnings. | Check the log of the backup operation. Click the workload to select it, and then click **Activities** to find the warning in the log. |
| **Backup is canceled** | Generated every time a backup is manually canceled by the user. | You can either start the backup manually by clicking **Run now** or wait until it runs at the next scheduled time. |
| **Backup canceled due to closed backup window** | Generated when the backup activity was missed because it did not fit in the window specified in the backup options. | Re-configure the schedule or edit the backup options of the backup plan in the **Performance and backup** window. |
| **Backup is waiting** | Generated when there is a scheduling conflict and two backup tasks are initiated at the same time. In this case, the second backup task is queued until the first one is finished or stopped. | Ensure that your backups are running in the expected time windows and according to their schedule, and avoid scheduling conflicts. |
| **Backup is not responding** | Generated when a backup has not shown any progress for some time, and might be frozen. | The issue might be caused by a lockup. For more information, see the Acronis knowledge base article. |
| **Backup did not start** | Generated when the scheduled backup failed to start for unknown reason. | Ensure that you are using the latest build of your Acronis Backup product. If the agent machine was available during the backup start time, edit the backup task start time and recreate if needed. If the agent was offline, do not turn off machine during backup time, and ensure Acronis Managed Machine Service is running. |
| **Backup status is unknown** | Generated when the backup agent was offline at a scheduled backup time. The status of the resource backups will be unknown until the backup agent comes online. | 1. Check if the agent is expected to be offline. 2. If the agent should not be offline, ensure that Acronis Managed Machine Service is running. |
| **Backup is missing** | Generated when there has not been a successful backup for more than [Days from last backup] days, which is defined in the Alerts backup option. | Ensure that the plan with enabled **Alerts** backup option is scheduled and runs at least once within the defined period configured for this option. |
| **Backup is corrupted** | Generated when the validation activity is successful and shows that the backup is corrupted. | Follow steps from article Troubleshooting Issues with Corrupt Backups. If you need assistance with identifying the root cause for archive corruption, contact the Support team. |
| **Continuous Data Protection failed** | Generated if the continuous protection of backup failed. | Verify: (1) CDP is supported only for NTFS file system on Windows 7+ and Windows Server 2008 R2+. (2) CDP does not support Acronis Secure Zone as destination. (3) NFS folders mounted on Windows are not supported. (4) Continuous replication is not supported with two locations. (5) Changes from network sources are not detected. (6) If a file is being used, CDP does not detect changes — save and close the file. |
| **Validation failed** | Generated when the validation process of the backup cannot be completed. | Check the log of the failed operation. Click the workload to select it, and then click **Activities** to find the warning in the log. |
| **Encryption password is missing** | Generated when the database encryption key is incorrect, corrupt, or missing. | There is no way to recover encrypted backups if you lose or forget the password. You must set the encryption password locally, on the protected device. |
| **Upload is pending** | Generated if scheduled check finds that Physical Data Shipping to cloud archive for this backup plan is not uploaded to the storage. | |
| **Backup recovery failed** | Generated when the recovery operation fails when you try to recover files or system backups. | Determine the exact date of the backup failure and attempt recovery with the last successful backup. |
