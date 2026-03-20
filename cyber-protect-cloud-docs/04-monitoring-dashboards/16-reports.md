---
title: "Reports"
section: "Understanding your current level of protection"
subsection: "Reports"
page_range: "361-367"
tags: [reports, dashboard, widgets, PDF, Excel, CSV, scheduling, export]
acronis_version: "26.02"
---

# Reports

> **Note:** The availability of this feature depends on the service quotas that are enabled for your account.

A report about operations can include any set of dashboard widgets. All widgets show summary information for the entire company.

Depending on the widget type, the report includes data for a time range or for the moment of browsing or report generation. See "Reported data according to widget type" below.

All historical widgets show data for the same time range. You can change this range in the report settings.

You can use default reports or create a custom report. You can download a report or send it via email in XLSX (Excel) or PDF format.

## Default reports

The set of default reports depends on the Cyber Protection service edition that you have.

| Report name | Description |
|---|---|
| #CyberFit Score by machine | Shows the #CyberFit Score, based on the evaluation of security metrics and configurations for each machine, and recommendations for improvements. |
| Alerts | Shows alerts that occurred during a specified time period. |
| Backup scanning details | Shows the detailed information about detected threats in the backups. |
| Daily activities | Shows the summary information about activities performed during a specified time period. |
| Data protection map | Shows the detailed information about the number, size, location, protection status of all important files on machines. |
| Detected threats | Shows the details of the affected machines by number of blocked threats and the healthy and vulnerable machines. |
| Discovered machines | Shows all found machines in the organization network. |
| Disk health prediction | Shows predictions when your HDD/SSD will break down and current disk status. |
| Existing vulnerabilities | Shows the existing vulnerabilities for OS and applications in your organization. The report also displays the details of the affected machines in your network for every product that is listed. |
| GenAI Protection summary | Shows the summary information about GenAI Protection for a specified period. |
| Software inventory | Shows information about the software that is installed on your company devices. **Note:** The report can contain up to 20 workloads at a time. |
| Hardware inventory | Shows information about the hardware that is available on your company devices. **Note:** The report can contain up to 20 workloads at a time. |
| Patch management summary | Shows the number of missing patches, installed patches, and applicable patches. You can drill down the reports to get the missing/installed patch information and details of all the systems. |
| Summary | Shows the summary information about the protected devices for a specified time period. |
| Weekly activities | Shows the summary information about activities performed during a specified time period. |
| Remote sessions | Shows information about the remote desktop and file transfer sessions. |

> **Note:** Local storage usage data is reported only at the unit and customer tenant levels. Users do not receive information about the local storage usage in the Summary reports.

## Actions with reports

### Add

1. In the Cyber Protect console, go to **Reports**.
2. Under the list of available reports, click **Add report**.
3. [To add a predefined report] Click the name of the predefined report.
4. [To add a custom report] Click **Custom**, and then add widgets to the report.
5. [Optional] Drag and drop the widgets to rearrange them.

### View

To view a report, click its name.

### Edit

1. In the Cyber Protect console, go to **Reports**.
2. In the list of reports, select the report that you want to edit.
3. In the upper-right corner of the screen, click **Settings**.
4. Edit the report, and then click **Save**.

### Delete

1. In the Cyber Protect console, go to **Reports**.
2. In the list of reports, select the report that you want to delete.
3. In the upper-right corner of the screen, click the ellipsis icon (...), and then click **Delete report**.
4. In the confirmation window, click **Delete**.

### Schedule

1. In the Cyber Protect console, go to **Reports**.
2. In the list of reports, select the report that you want to schedule.
3. In the upper-right corner of the screen, click **Settings**.
4. Next to **Scheduled**, enable the switch.
   - Specify the email addresses of the recipients.
   - Select the format of the report.
   > **Note:** You can export up to 1,000 items in a PDF file, and up to 10,000 items in a XLSX file. The timestamps in the PDF and XLSX files use the local time of your machine.
   - Select the language of the report.
   - Configure the schedule.
5. Click **Save**.

### Download

1. In the Cyber Protect console, go to **Reports**.
2. In the list of reports, select the report.
3. In the upper-right corner of the screen, click **Download**.
4. Select the format of the report.

As a result, a file in the selected format is downloaded to your machine. If you selected **Excel and PDF**, a ZIP file is downloaded to your machine.

### Send

1. In the Cyber Protect console, go to **Reports**.
2. In the list of reports, select the report.
3. In the upper-right corner of the screen, click **Send**.
4. Specify the email addresses of the recipients.
5. Select the format of the report.
6. Click **Send**.

### Export structure

1. In the Cyber Protect console, go to **Reports**.
2. In the list of reports, select the report.
3. In the upper-right corner of the screen, click the ellipsis icon (...), and then click **Export**.

As a result, the report structure is saved on your machine as a JSON file.

### Dump data

You can export all data for a custom period, without filtering it, to a CSV file and send the CSV file to an email recipient. The CSV file contains only data about the widgets that are included in the report.

> **Note:** You can export up to 150,000 items in a CSV file. The timestamps in the CSV file use Coordinated Universal Time (UTC).

1. In the Cyber Protect console, go to **Reports**.
2. In the list of reports, select the report whose data you want to dump.
3. In the upper-right corner of the screen, click the ellipsis icon (...), and then click **Dump data**.
4. Specify the email addresses of the recipients.
5. In **Time range**, specify the custom period for which you want to dump data.
   > **Note:** Preparing CSV files for longer periods takes more time.
6. Click **Send**.

## Reported data according to widget type

According to the data range that they display, widgets on the dashboard are two types:

- Widgets that display actual data at the moment of browsing or report generation.
- Widgets that display historical data.

When you configure a date range in the report settings to dump data for a certain period, the selected time range will apply only for widgets that display historical data. For widgets that display actual data at the moment of browsing, the time range parameter is not applicable.

| Widget name | Data displayed in widget and reports |
|---|---|
| #CyberFit Score by machine | Actual |
| 5 latest alerts | Actual |
| Active alerts details | Actual |
| Active alerts summary | Actual |
| Activities | Historical |
| Activity list | Historical |
| Alerts history | Historical |
| Attack tactics statistics | Historical |
| Backup scanning details (threats) | Historical |
| Backup status | Historical (Total runs, Number of successful runs); Actual (all other columns) |
| Blocked URLs | Actual |
| Cloud applications | Actual |
| Cyber protection | Actual |
| Data protection map | Historical |
| Devices | Actual |
| Discovered devices | Actual |
| Disk health overview | Actual |
| Disk health status by physical devices | Actual |
| Existing vulnerabilities | Historical |
| Hardware changes | Historical |
| Hardware details | Actual |
| Hardware inventory | Actual |
| Historical alerts summary | Historical |
| Incident severity history | Historical |
| Locations summary | Actual |
| Missing updates by categories | Actual |
| Not protected | Actual |
| Patch installation history | Historical |
| Patch installation status | Historical |
| Patch installation summary | Historical |
| Protection status | Actual |
| Recently affected | Historical |
| Remote sessions | Historical |
| Security incident burndown | Historical |
| Security incident MTTR | Historical |
| Software inventory | Actual |
| Software overview | Historical |
| Threat status | Actual |
| Vulnerable machines | Actual |
| Workload network status | Actual |
