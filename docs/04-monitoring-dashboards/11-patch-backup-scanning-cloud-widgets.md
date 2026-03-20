---
title: "Patch installation, backup scanning, recently affected, and cloud application widgets"
section: "Understanding your current level of protection"
subsection: "Patch, backup scanning, and cloud widgets"
page_range: "340-344"
tags: [patch management, patch installation, backup scanning, recently affected, cloud applications, Microsoft 365, Google Workspace, widgets]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#recently-affected.html"
---

# Patch installation widgets

There are four widgets related to the patch management functionality.

## Patch installation status

This widget shows the number of machines grouped by the patch installation status:

- **Installed** -- all available patches are installed on a machine
- **Reboot required** -- after patch installation reboot is required for a machine
- **Failed** -- patch installation failed on a machine

## Patch installation summary

This widget shows the summary of patches on machines by the patch installation status. The table includes columns for installation status, total number of machines, total number of updates, Microsoft updates, application updates, critical severity, high severity, and medium severity.

## Patch installation history

This widget shows the detailed information about patches on machines. The table includes columns for machine name, update name, version, severity, stability, protection plan, size, approval status, release date, and installation status.

## Missing updates by categories

This widget shows the number of missing updates per category. The following categories are shown:

- Security updates
- Critical updates
- Other

# Backup scanning details

This widget shows the detailed information about the detected threats in backups. The table includes columns for device name, plan name, backup date and time, contents type, location, threat name, affected files, and date and time of detection.

# Recently affected

This widget shows detailed information about workloads that were affected by threats, such as viruses, malware, and ransomeware. You can find information about the detected threats, the time when the threats were detected, and how many files were affected.

The table includes columns for machine name, protection plan, threat, affected files, and detection time. You can customize the visible columns to also show folder, customer, detected by, file name, file path.

## Downloading data for recently affected workloads

You can download the data for the recently affected workloads, generate a CSV file, and send it to the recipients that you specify.

1. In the **Recently affected** widget, click **Download data**.
2. In the **Time period** field, enter the number of days for which you want to download data. The maximum number of days that you can enter is 200.
3. In the **Recipients** field, enter the email addresses of all the people who will receive an email with a link for downloading the CSV file.
4. Click **Download**.

The system starts generating the CSV file with the data for the workloads that were affected in the time period that you specified. When the CSV file is complete, the system sends an email to the recipients. Each recipient can then download the CSV file.

# Cloud applications

This widget shows detailed information about cloud-to-cloud resources:

- Microsoft 365 users (mailbox, OneDrive)
- Microsoft 365 groups (mailbox, group site)
- Microsoft 365 public folders
- Microsoft 365 site collections
- Microsoft 365 Teams
- Google Workspace users (Gmail, Google Drive)
- Google Workspace shared drives

The table displays device name, protection status, last successful backup, next backup, and number of backups.

Additional information about cloud-to-cloud resources is also available in the following widgets:

- Activities
- Activity list
- 5 latest alerts
- Alerts history
- Active alerts summary
- Historical alerts summary
- Active alert details
- Locations summary
