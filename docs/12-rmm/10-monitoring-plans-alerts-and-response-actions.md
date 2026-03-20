---
title: "Monitoring Plans, Alerts, and Response Actions"
section: "RMM"
subsection: "Monitoring Plans and Alerts"
page_range: "1433-1452"
tags: [rmm, monitoring-plans, alerts, response-actions, automatic-response, manual-response, email-notifications, alert-variables, machine-learning, viewing-data]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#monitoring-plan-actions.html"
---

# Monitoring Plans

Monitoring plans are plans that you apply on your managed workloads to enable and configure the monitoring functionality. If no monitoring plan is applied on a workload, the monitoring features will not be available for that workload.

## Creating a Monitoring Plan

### From Monitoring Plans

1. In the Protection console, go to **Management > Monitoring plans**.
2. Create a monitoring plan using one of two options:
   - If there are no monitoring plans in the list, click **Create**.
   - If there are monitoring plans in the list, click **Create plan**.
3. In the **Create monitoring plan** window:
   - **Standard protection** (service-based licensing): Four monitors are automatically added: Disk space, Hardware changes, Last system restart, and Files and folders size.
   - **RMM pack** (service-based) or **Security and RMM** (solution-based): Select **Recommended** (default configuration) or **Custom** (from scratch), and click **Next**.
4. (Optional) Change the plan name.
5. (Optional) Click **Add monitor**, select the monitor, and click **Add**. You can add up to 30 monitors to a monitoring plan.
6. (Optional) In the monitor parameters screen, change default settings of the monitor and alerts, and click **Done**.
7. (Optional) To delete a monitor, click the bin icon and click **Delete**.
8. (Optional) Add workloads to the plan.
9. Click **Create**.

### From All Devices

1. Go to **Devices > All devices**.
2. Click the workload to apply a monitoring plan to.
3. Click **Protect**.
4. Depending on whether a monitoring plan is already applied:
   - If a plan is already applied: Click **Create plan**, select **Monitoring**.
   - If no plan is applied: Click **Add plan**, select **Create plan**, select **Monitoring**.
5. Select **Recommended** or **Custom** template.
6. Configure monitors and alerts as needed.
7. Click **Create**.

## Adding Workloads to Monitoring Plans

### From Monitoring Plans

1. Go to **Management > Monitoring plans**.
2. Click the monitoring plan.
3. Click **Add workloads** or **Manage workloads**.
4. Select a workload and click **Add**.
5. Click **Save**.
6. If necessary, click **Confirm** to apply the required service quota.

### From All Devices

1. Go to **Devices > All devices**.
2. Click the workload, then click **Protect**.
3. Find the monitoring plan and click **Apply**.
4. If necessary, click **Confirm**.

## Revoking Monitoring Plans

1. Go to **Devices > All devices**.
2. Click the workload, then click **Protect**.
3. Click the **More actions** icon of the monitoring plan, then click **Revoke**.

## Additional Actions with Monitoring Plans

From the **Monitoring plans** screen, you can: view details, edit, view activities, view alerts, rename, enable, disable, clone, export (JSON format), import (from JSON file), set as favorite, set as default, clear default, and delete.

# Configuring Automatic Response Actions

Automatic response actions are predefined actions or measures that are triggered automatically in response to detected events or incidents. These actions are designed to mitigate potential threats and minimize damage.

You can configure one or several automatic response actions on the alerted events. The maximum number of automatic response actions per monitor is 20.

## Steps to Configure Automatic Response Actions

1. Go to **Management > Monitoring plans**.
2. Select the monitoring plan.
3. Select the monitor (or click **Add monitor** to add one).
4. Click the link next to **Automatic response actions**.
5. In the **Automatic response actions** window, add one or several response actions.
6. Configure each response action. For example, for **Start a Windows service**: click **Specify** next to Windows service, select a service, click **Done**.
7. Use the up and down arrows or drag and drop to set the sequence of response actions.
8. Configure failure handling: **Continue with the next response action** or **Do not continue with the next response action**.
9. Click **Done**.

## Available Automatic Response Actions

| Action | Description | Supported OS |
|--------|-------------|-------------|
| Run a script | Select and run a script on the workload with specified parameters. Requires RMM or Security and RMM license. | Windows, macOS |
| Restart the workload | Restarts the workload remotely when conditions are met. | Windows, macOS |
| Stop the process | Stops a specified process by name when conditions are met. | Windows, macOS |
| Start the Windows service | Starts a selected Windows service from the dynamic list of services populated from the agents. | Windows |
| Stop the Windows service | Stops a selected Windows service from the dynamic list. | Windows |
| Enable Windows Update | Enables Windows Update when conditions are met. Available only for Windows Update status monitor. | Windows |
| Disable AutoRun on removable drives | Disables the AutoRun feature on removable storage media. Available only for AutoRun feature status monitor. | Windows |

### Script Settings for Automatic Response Actions

| Setting | Description |
|---------|-------------|
| Account to execute the script | System account (default) or Currently logged in account |
| Maximum duration | Maximum period the script can run (1-1440 min, default 3 min). If not complete during this period, the operation will fail. |
| PowerShell execution policy | Undefined, AllSigned, Bypass (default), RemoteSigned, Restricted, or Unrestricted |

# Monitoring Alerts

Monitoring alerts are displayed in the Protection console and are sent via email when the monitored behavior of workloads is out of norm. To enable monitoring alerts via email, you must configure at least one email notification policy.

## Configuring Monitoring Alerts

1. In the **Monitor parameters** window, go to the **Generate alerts** section.
2. In **Alert severity**, select the severity:
   - **Critical**: Highest priority, related to issues critical for operation. Resolve ASAP.
   - **Error**: Less severe, indicates something is wrong or not behaving normally.
   - **Warning** (default): Some condition you should be aware of, might not be causing a problem yet.
   - **Informational**: Lowest priority, does not indicate a problem. Information about actions related to a monitored object.
3. In **Alert frequency**, select how often to generate alerts:
   - **Once until the check passes** (default): Generate alert one time until the check completes successfully.
   - **After X consecutive failures**: Generate alert after X consecutive failed checks.
4. In **Alert message**, click the pencil icon to edit the default alert message. You can use variables enclosed in `{{}}`.
5. Enable **Alert auto-resolution** to automatically resolve the alert when the monitored metric returns to normal. Enabled by default.

## Monitoring Alert Variables

Variables can be used in alert messages. Enclose them in `{{}}`.

| Variable | Description | Available For |
|----------|-------------|---------------|
| plan_name | Name of the policy | All monitors |
| monitor_name | Name of the sub policy | All monitors |
| workload_name | Name of the workload | All monitors |
| threshold_value | Monitoring conditions or thresholds | Threshold-based monitors |
| threshold_unit | Unit for the threshold value (%, MB, mb/s) | Threshold-based monitors |
| time_period | Period for detected issue | Threshold-based monitors |
| time_unit | Unit for time period (sec/min/hours/day) | Threshold-based monitors |
| anomaly_value | The anomaly value | Anomaly-based monitors |
| anomaly_unit | Unit for the anomaly value | Anomaly-based monitors |
| deviation_value | The deviation value | Anomaly-based monitors |
| deviation_unit | Unit for the deviation value | Anomaly-based monitors |
| drive_name | Drive or partition name | Disk space |
| CPU_model | Model of the monitored CPU | CPU temperature |
| GPU_model | Model of the monitored GPU | GPU temperature |
| hardware_model | Model of the monitored component | Hardware changes |
| hardware_component | Type of monitored hardware | Hardware changes |
| disk_model | Model of the disk | Disk transfer rate |
| network_adapter_model | Model of the network adapter | Network usage |
| process_name | Name of the process | CPU/Memory/Disk/Network usage by process, Process status |
| service_name | Name of the service | Windows service status |
| software_name | Name of the software application | Installed software |
| software_version | Version of the software application | Installed software |
| script_name | Name of the script | Custom |

## Manual Response Actions

When you see an alert, you can select a response action from the alert's **Response action** drop-down list. The available actions depend on the alert type, features, and workload OS.

| Action | Description | OS |
|--------|-------------|-----|
| Browse disk space usage trend | Opens Disk space usage graph (1 day/7 days/1 month) | Windows, macOS |
| Browse files size growth trend | Opens File size growth graph | Windows, macOS |
| Run a script | Select and run a script on the workload (requires RMM license) | Windows, macOS |
| Connect via NEAR | Establishes a remote NEAR connection | Windows, macOS |
| Connect via RDP | Establishes a remote RDP connection | Windows |
| Run command line | Starts Command Prompt or PowerShell | Windows |
| Run Terminal | Starts Terminal (BASH or ZSH) | macOS |
| Open hardware inventory | Opens Hardware inventory tab for the workload | Windows, macOS |
| Browse top 10 processes that loaded CPU | Shows processes that loaded the CPU at alert generation time | Windows, macOS |
| Browse top 10 processes that loaded GPU | Shows processes that loaded the GPU | Windows, macOS |
| Browse top 10 processes that loaded memory | Shows processes that loaded memory | Windows, macOS |
| Browse top 10 processes that loaded disk | Shows processes that loaded the disk | Windows, macOS |
| Browse top 10 processes that loaded network | Shows processes that loaded the network adapter | Windows, macOS |
| Browse resource usage by process | Shows CPU, memory, disk I/O, network usage by related process | Windows, macOS |
| Restart workload | Restarts the workload after confirmation | Windows, macOS |
| Start/Stop Windows service | Starts or stops a Windows service | Windows |
| Stop process | Stops the process referenced by the alert | Windows, macOS |
| Enable Windows Update | Enables Windows Update | Windows |
| Disable AutoRun on removable drives | Disables AutoRun feature on system level | Windows |

For security reasons, 2FA is required for manual response actions including: Run a script, Connect via NEAR/RDP, Restart workload, Start/Stop Windows service, Stop process, Enable Windows Update, and Disable AutoRun.

# Configuring Email Notification Policies

Email notification policies specify which users will receive email notifications from different monitors.

## Steps to Add an Email Notification Policy

1. Go to **Settings > Email notifications**.
2. Click **Add policy**.
3. Click **Select recipients** and select the users to receive alerts.
4. In **Alert types**, select the monitors for which to send email alerts.
5. Click **Add**.

You can also edit, enable, disable, and delete email notification policies from the **Email notifications** screen.

# Viewing Monitor Data

For each workload, you can view the list of applied monitors, the current status, and historical performance details in a graphical view.

1. Go to **Devices > All devices**.
2. Click a workload, then click the **Monitoring** tab.

The Monitoring tab displays a widget for each enabled monitor, showing:
- Monitor name
- Last result (latest value or event state)
- Last check (date and time of last data collection)
- Alerts (number of unresolved alerts)

Widgets become visible 15 minutes (or the minimum monitor frequency) after applying a monitoring plan.

## Monitor Widget Details

| Detail | Description |
|--------|-------------|
| Monitoring plan | Name of the monitoring plan containing the monitor |
| Monitor frequency | Time interval at which the monitor collects data |
| Last result | Latest value of the monitored metric |
| Last check | Date and time of last data collection |
| Last alert | Date and time of last alert generated |
| Historical graph | For time-series monitors: displays historical data for 1 hour, 6 hours, 12 hours, 1 day, 1 week, or 1 month in graphical view |

For anomaly-based monitoring, the graph displays the baselines area, a line showing actual values, and anomalies (spikes or values out of baselines) as red dots. Hovering over the graph shows the actual value and threshold values for a specific time.

## Resetting Machine Learning Models

You can reset the models of a workload when they become outdated or invalid. This deletes all created models and data collected by anomaly-based monitors.

1. Go to **Devices > All devices**.
2. Click a workload and click the **Details** tab.
3. In the **Reset machine learning models** section, click **Reset**.
4. In the confirmation window, click **Reset** again.
