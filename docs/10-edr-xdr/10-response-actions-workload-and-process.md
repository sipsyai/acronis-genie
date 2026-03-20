---
title: "Response Actions for Workloads and Processes"
section: "Endpoint Detection and Response (EDR)"
subsection: "Response Actions"
page_range: "1192-1201"
tags: [edr, response-actions, restart, forensic-backup, remote-desktop, remote-command, recovery, disaster-recovery, stop-process, quarantine, rollback]
acronis_version: "26.02"
---

# Response Actions for Workloads and Processes

This section details the specific response actions available for workload and process nodes in the EDR cyber kill chain.

## Restart a Workload

As part of your remediation response to an attack, EDR enables you to immediately restart a workload, or restart the workload according to a predefined timeout period.

### Steps to Restart a Workload

1. In the cyber kill chain, click the workload node you want to set a restart schedule for.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Remediate** section, click **Restart workload**.
4. In the **Restart timeout** field, click the displayed link and select one of the following:
   - **Set timeout**: Set the restart period for the workload, and then click **Save**.
   - **Restart immediately**: Restart the workload immediately.
5. (Optional) Select the **Fail if end-user is logged in** check box to ensure the workload is not restarted if the user is logged in.
6. In the **Message to display** field, add a message to display to users when they access the workload.
7. (Optional) Add a **Comment**.
8. Click **Restart**.

### Restart Options (for Patching)

| Option | Description |
|--------|-------------|
| **Restart if required** | Restart only if the software requires it. |
| **Always restart** | Always restart after the software is installed or uninstalled. |
| **Do not restart** | Do not restart after the software is installed or uninstalled. |
| **Schedule automatic restart** | Available when Restart if required or Always restart is selected. Enables automatic restart of the workload. |
| **If a user is logged on to the device** | Available with Schedule automatic restart. Set the period after which the workload will be restarted automatically. The user will be notified about a pending automatic restart. |
| **Additional notifications** | Available with Schedule automatic restart. Repeatedly notify the user about a pending restart. Notifications are triggered at: 24h, 8h, 4h, 1h, 30 min, 15 min, and 5 min before the automatic restart. The last (5 min) notification cannot be closed or dismissed. |
| **If no user is logged on to the device, restart it immediately** | Available with Schedule automatic restart. If no user is logged in, the workload will be restarted immediately without waiting. |

## Run an On-Demand Forensic Backup on a Workload

As part of your investigation into an attack, EDR enables you to run an on-demand forensic backup for audit or further investigation purposes.

### Steps to Run a Forensic Backup

1. In the cyber kill chain, click the workload node you want to run a forensic backup on.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Investigate** section, click **Forensic backup**.
4. (Optional) In the **Backup name** field, click the edit icon to edit the backup name.
5. In the **Forensic options** field, click the displayed link. In the Forensic options dialog, select one of the following:
   - **Collect raw memory dump**
   - **Collect kernel memory dump**
   - You can also select the **Snapshot of running processes** check box to add information about the processes running at the moment the backup starts.
   - Click **Save** to close the Forensic options dialog.
6. In the **Where to back up** field, click the displayed link to define a location for the backup.
7. (Optional) Click the **Encryption** option to enable encryption. Enter the password and select the relevant encryption algorithm.
8. (Optional) Add a **Comment**.
9. Click **Run**. The forensic backup is started.

## Remote Connection to a Workload

As part of your investigation into an attack, EDR enables you to remotely access the workload under investigation.

### Steps to Remotely Connect

1. In the cyber kill chain, click the workload node you want to remotely connect to.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Investigate** section, click **Remote desktop connection**.
4. Select one of the following remote connection methods:
   - **Connect via RDP client**: Prompts you to download and install the Remote Desktop Connection Client. You can then remotely connect from the Cyber Protect console.
   - **Connect via Web client**: Does not require the installation of an RDP client on your workload. You are redirected to the login screen where credentials must be entered.

## Running the Remote Command Line

As part of your investigation, you can remotely run the command line of the workload under investigation.

1. In the cyber kill chain, click the workload node to which you want to connect remotely.
2. In the displayed sidebar, click the **Response Actions** tab.
3. Depending on the workload's operating system:
   - **For Windows workloads**: In the **Investigate** section, expand **Remote command-line interface**, and then click **Run command line**.
   - **For macOS workloads**: In the **Investigate** section, expand **Remote Terminal**, and then click **Run Terminal**.

## Recovery from Backup

As part of your recovery response to an attack, EDR enables you to recover your entire machine from backup or specific files or folders.

### Steps to Recover from Backup

1. In the cyber kill chain, click the workload node you want to recover.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Recovery** section, click **Recover from backup**.
4. In the **Recovery point** field, click **Select** and then:
   a. Select the relevant recovery point.
   b. Click **Recover > Entire workload** to recover all files and folders, or click **Recover > Files/folders** to recover specific files and folders.
5. (Optional) Select **Automatically restart the workload** check box (relevant only for Entire workload recovery).
6. (Optional) Add a **Comment**.
7. Click **Start recovery**. If the recovery point is encrypted, you will be prompted for the password.

## Disaster Recovery Failover

As part of your recovery response, EDR enables you to switch the workload to the recovery server. Your workload must have a subscription for Advanced Disaster Recovery.

### Steps to Run Disaster Recovery Failover

1. In the cyber kill chain, click the workload node you want to recover.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Recovery** section, click **Disaster Recovery failover**.
4. In the **Recovery point** field, click the current recovery point date to select a recovery point.
5. (Optional) Add a **Comment**.
6. Click **Failover**. The workload is switched to the recovery server.

If you have an Advanced Disaster Recovery subscription, you can select the relevant recovery server (the offline VM) created in Disaster Recovery. If you do not have a subscription, you will be prompted to configure Disaster Recovery.

## Define Response Actions for a Suspicious Process

As part of your remediation response, you can apply the following actions to suspicious processes:

### Stop a Process

1. In the cyber kill chain, click the process node you want to remediate. Windows critical processes or non-running processes cannot be stopped and are disabled in the cyber kill chain.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Remediate** section, click **Stop process**.
4. Select one of the following:
   - **Stop process** (stops the specific process)
   - **Stop process tree** (stops the specific process and all child processes)
5. (Optional) Add a comment.
6. Click **Stop**. The process is stopped and the related application is closed. Any unsaved data will be lost.

### Quarantine a Process

1. In the cyber kill chain, click the process node you want to quarantine. Windows critical processes cannot be quarantined and are disabled in the cyber kill chain.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Remediate** section, click **Quarantine**.
4. (Optional) Add a comment.
5. Click **Quarantine**. The process is stopped and then quarantined. The process is added to and managed in the quarantine section available under antimalware protection.

### Rollback Changes

1. In the cyber kill chain, click the process node you want to rollback changes for. This action is available for detection nodes (shown as red or yellow nodes) only.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Remediate** section, click **Rollback changes**.
4. To view the items affected by the rollback changes, click the **Affected items** link. The dialog shows all items (files, registry, scheduled tasks) that the rollback will revert and with what action (Delete, Recover, or None).
5. (Optional) Add a comment.
6. Click **Rollback**. The rollback functionality reverts any registry, file or scheduled task changes made by the process in the following steps:
   a. Any new entries (registry, scheduled tasks, files) created by the threat (and its child threats) are deleted.
   b. Any modifications to the registry, scheduled tasks and/or files existing on the workload prior to the attack are reverted.
   c. Rollback tries to recover items from the local cache. For items that cannot be recovered, EDR will automatically recover them from clean backup images.
