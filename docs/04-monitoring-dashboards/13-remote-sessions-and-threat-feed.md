---
title: "Remote sessions widget, smart protection, and threat feed"
section: "Understanding your current level of protection"
subsection: "Remote sessions and threat feed"
page_range: "348-354"
tags: [remote sessions, smart protection, threat feed, CPOC, data protection map, security alerts, widgets]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#remote-sessions.html"
---

# Remote sessions widget

This widget shows the detailed information about the remote desktop and file transfer sessions. The table includes columns for start time, end time, duration, connection type, protocol, connection source, accessed by, and connection destination.

> **Note:** In the **Machine name** filter, you can select up to 20 values.

# Smart protection

## Threat feed

Acronis Cyber Protection Operations Center (CPOC) generates security alerts that are sent only to the related geographic regions. These security alerts provide information about malware, vulnerabilities, natural disasters, public health, and other types of global events that may affect your data protection. The threat feed informs you about all the potential threats and allows you to prevent them.

> **Note:** The availability of this feature depends on the service quotas that are enabled for your account.

Some security alerts can be resolved by following a set of specific actions that are provided by the security experts. Other security alerts just notify you about the upcoming threats but no recommended actions are available.

> **Note:** Malware alerts are generated only for machines that have the Agent for Antimalware protection and URL filtering installed.

### How it works

Acronis Cyber Protection Operations Center monitors external threats and generates alerts about malware, vulnerability, natural disaster, and public health threats. You will be able to see all these alerts in the Cyber Protect console, in the **Threat feed** section. You can perform respective recommended actions depending on the type of alert.

### Running recommended actions

To run the recommended actions on received alerts from Acronis Cyber Protection Operations Center, do the following:

1. In the Cyber Protect console, go to **Monitoring** > **Threat feed** to review if there are any existing security alerts.
2. Select an alert in the list and review the provided details.
3. Click **Start** to launch the wizard.
4. Enable the actions that you want to be performed and machines to which these actions must be applied. The following actions can be suggested:
   - **Vulnerability assessment** -- to scan machines for vulnerabilities
   - **Patch management** -- to install patches on the selected machines
   - **Antimalware Protection** -- to run full scan of the selected machines
     > **Note:** This action is available only for machines that have the agent for Antimalware protection installed.
   - **Backup of protected or unprotected machines** -- to back up protected and unprotected workloads. If there are no backups yet for the workload (in all accessible locations, cloud and local), or the existing backups are encrypted, the system creates a full backup with the following name format: `%workload_name%-Remediation`. By default, the destination for the backup is the Cyber Protect Cloud storage, but you can configure another location before you start the operation. If a non-encrypted backup already exists, the system will create an incremental backup in the existing archive.
5. Click **Start**.
6. On the **Activities** page, verify that the activity was successfully performed.

### Deleting all alerts

Automatic clean-up from the threat feed is made after the following time periods:

- Natural disaster -- 1 week
- Vulnerability -- 1 month
- Malware -- 1 month
- Public health -- 1 week

## Data protection map

With Data protection map you can:

- Receive detailed information about stored data (classification, locations, protection status, and additional information) on your workloads.
- Check whether data is protected. Data is considered protected if a protection plan with backup module enabled is applied to the workload.
- Perform actions for data protection.

> **Note:** The **Data protection map** option is disabled by default in newly created protection plans.

### How it works

1. First, you create a protection plan with the Data protection map module enabled.
2. Then, after the plan was performed and your data were discovered and analyzed, you will get a visual representation of data protection on the Data protection map widget.

You can also go to **Devices** > **Data protection map** and find there information about unprotected files per device.

### Managing the detected unprotected files

To protect the important files that were detected as unprotected:

1. In the Cyber Protect console, go to **Devices** > **Data protection map**. In the list of devices, you can find general information about the number of unprotected files, size of such files per device, and the last data discovery. To protect files on a particular machine, click the Ellipsis icon and then **Protect all files**. You will be redirected to the list of plans where you can create a protection plan with the backup module enabled. To delete the particular device with unprotected files from the list, click **Hide until next data discovery**.
2. To view a more detailed information about the unprotected files on a particular device, click on the name of the device. You will see the number of unprotected files per extension and per location.
3. To protect all unprotected files, click **Protect all files**. You will be redirected to the list of plans where you can create a protection plan with the backup module enabled.

To get the information about the unprotected files in the form of report, click **Download detailed report in CSV**.

### Data protection map settings

> **Note:** The **Data protection map** option is disabled by default in newly created protection plans.

The following settings can be specified for the Data protection map module.

#### Schedule

| Field | Description |
|---|---|
| Schedule the task run using the following events | **Schedule by time** -- This is the default setting. The task will run according to the specified time. **When user logs in to the system** -- By default, a login of any user will trigger the task. You can modify this setting so that only a specific user account can trigger the task. **When user logs off the system** -- By default, a logoff of any user will trigger the task. You can modify this setting so that only a specific user account can trigger the task. **Note:** The task will not run at system shutdown. Shutting down and logging off are different events in the scheduling configuration. **On the system startup** -- The task will run when the operating system starts. **On the system shutdown** -- The task will run when the operating system shuts down. |
| Schedule type | Appears if you selected **Schedule by time**. Options: **Monthly**, **Daily** (default), **Hourly**. |
| Start at | Appears if you selected **Schedule by time**. Select the exact time when the task will run. |
| Run within a date range | Set a range in which the configured schedule will be effective. |
| Start conditions | Defines all conditions that must be met simultaneously for the task to run. Options include: **Distribute task start time within a time window**, **If the machine is turned off, run missed tasks at the machine startup**, **Prevent the sleep or hibernate mode during task running** (Windows only), **If start conditions are not met, run the task anyway after** a specified period. **Note:** Start conditions are not supported for Linux. |

#### Extensions and exception rules

On the **Extensions** tab, you can define the list of file extensions that will be considered as important during data discovery and checked whether they are protected. Use the following format for defining extensions:

`.html, .7z, .docx, .zip, .pptx, .xml`

On the **Exception rules** tab, you can define which files and folders not to check on protection status during data discovery.

- **Hidden files and folders** -- if selected, hidden files and folders will be skipped during data examination.
- **System files and folders** -- if selected, system files and folders will be skipped during data examination.
