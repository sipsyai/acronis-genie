---
title: "Monitoring Health and Performance of Workloads"
section: "RMM"
subsection: "Monitoring"
page_range: "1397-1416"
tags: [rmm, monitoring, anomaly-based, threshold-based, machine-learning, monitors, cpu, memory, disk, network, security, alerts, monitoring-plans]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#monitoring-workloads.html"
---

# Monitoring the Health and Performance of Workloads

You can monitor the system parameters and the health of the workloads in your organization. If a parameter is out of norm, you will be notified immediately and will be able to quickly resolve the issue. You can also configure custom alerts and automatic response actions that will be performed automatically to resolve anomalies in workload behavior.

The monitoring functionality requires installation of Protection agent version 15.0.35324 or later on the workloads.

## Monitoring Plans

To start monitoring the performance, hardware, software, system, and security parameters of your managed workloads, apply a monitoring plan to them. The monitoring plans consist of different monitors that you can enable and configure. Some monitors support the anomaly-based monitoring type.

If the agent cannot collect data from a workload for some reason, the system will generate an alert.

## Monitoring Types

You must configure the monitoring type for each monitor that you enable in the plan:

### Threshold-Based Monitoring
Tracks if the values of the parameters are above or below a threshold value that you configure. You are responsible for defining the correct threshold values. The system determines normal behavior based on static threshold values without considering other specific conditions that might cause the behavior. Threshold-based monitoring might be less accurate compared to anomaly-based monitoring.

### Anomaly-Based Monitoring
Uses machine learning models to create the normal behavior patterns for a workload and to detect anomalies (unexpected spikes in time-series data). When activated, the system creates a model and starts training itself, adjusting the model for the specific workload based on collected data.

At the beginning of the training period, the data might not be fully accurate. Creating a reliable model requires at least three weeks of training. As the system collects more data and analyzes historical data sets, it gradually refines the model and creates dynamic upper and lower thresholds for each metric. This monitoring type is more flexible because the system monitors the values of the parameters and their context.

You can reset the machine learning models of a workload, which will delete all data and models for the monitors applied to the workload.

## Supported Platforms

| Supported Windows Versions | Supported macOS Versions |
|---------------------------|-------------------------|
| Windows 7 SP1 | macOS 10.14 (Mojave) |
| Windows 8, 8.1 | macOS 10.15 (Catalina) |
| Windows 10 | macOS 11.x (Big Sur) |
| Windows 11 | macOS 12.x (Monterey) |
| Windows Server 2008 R2 | macOS 13.x (Ventura) |
| Windows Server 2012, 2012 R2 | macOS 14.x (Sonoma) |
| Windows Server 2016 | macOS 15.x (Sequoia) |
| Windows Server 2019 | |
| Windows Server 2022 | |

## Configurable Monitors

The monitoring functionality supports monitors divided into six categories: Hardware, Performance, Software, System, Security, and Custom.

### Hardware Monitors

| Monitor | Description | OS | Frequency | Anomaly Support |
|---------|-------------|-----|-----------|----------------|
| Disk space | Free space on a specific drive | Windows, macOS | 1 min | Yes |
| CPU temperature | CPU temperature | macOS | 30 sec | Yes |
| GPU temperature | GPU temperature | Windows, macOS | 30 sec | Yes |
| Hardware changes | Adding, removing, or replacing hardware | Windows, macOS | 24 hours | No |

### Performance Monitors

| Monitor | Description | OS | Frequency | Anomaly Support |
|---------|-------------|-----|-----------|----------------|
| CPU usage | Overall CPU usage (processor utilization) | Windows, macOS | 30 sec | Yes |
| CPU usage by process | CPU usage by a specific process | Windows, macOS | 30 sec | No |
| Memory usage | Overall memory usage | Windows, macOS | 30 sec | Yes |
| Memory usage by process | Memory usage by a specific process | Windows, macOS | 30 sec | No |
| Disk transfer rate | Read and write speed of each physical disk | Windows, macOS | 30 sec | Yes |
| Disk transfer rate by process | Read and write speed by a specific process | Windows, macOS | 30 sec | No |
| Network usage | Incoming and outgoing traffic for each network adapter | Windows, macOS | 30 sec | Yes |
| Network usage by process | Traffic by a specific process | Windows, macOS | 30 sec | No |

### Software Monitors

| Monitor | Description | OS | Frequency | Anomaly Support |
|---------|-------------|-----|-----------|----------------|
| Windows service status | Status of a selected Windows service (Running or Stopped) | Windows | 30 sec | No |
| Process status | Status of a selected process (Running or Stopped) | Windows, macOS | 30 sec | No |
| Installed software | Installation, update, or deletion of software | Windows, macOS | 24 hours | No |

### System Monitors

| Monitor | Description | OS | Frequency | Anomaly Support |
|---------|-------------|-----|-----------|----------------|
| Last system restart | When the workload was restarted | Windows, macOS | 1 hour | No |
| Windows event log | Specific business-critical events in Windows event logs | Windows | 10 min | No |
| Files and folders size | Total size of selected files or folders | Windows, macOS | 10 min | No |

### Security Monitors

| Monitor | Description | OS | Frequency | Anomaly Support |
|---------|-------------|-----|-----------|----------------|
| Windows Update status | Windows Update status and whether latest updates are installed | Windows | 15 min | No |
| Firewall status | Status of built-in or third-party firewall | Windows, macOS | 5 min | No |
| Antimalware software status | Status of built-in or third-party antimalware software | Windows, macOS | 5 min | No |
| Failed logins | Unsuccessful login attempts on the workload | Windows | 1 hour | No |
| AutoRun status | Whether AutoRun for removable storage media is enabled | Windows | 1 hour | No |

### Custom Monitors

| Monitor | Description | OS | Frequency | Anomaly Support |
|---------|-------------|-----|-----------|----------------|
| Custom | Monitors custom objects via running scripts | Windows, macOS | Custom | No |

## Monitor Settings Details

### Disk Space Monitor Settings

**Threshold-based**: Configure Drive (System drive or Any drive), Operator (Less than / Less than or equal to), Disk free space threshold (1-100%, default 20%), Include removable drives, and Time period (1-60 min, default 30).

**Anomaly-based**: Configure Drive, Model training period (days, default 21, minimum 21), Receive anomaly alerts during training, Sensitivity level (Low/Normal/High), and Anomaly duration (default 30 min).

### CPU Temperature Monitor Settings

**Threshold-based**: CPU temperature threshold (default 80 degrees C), Time period (1-60 min, default 5).

**Anomaly-based**: Model training period (default 21 days), Sensitivity level (Low/Normal/High), Anomaly duration (default 15 min).

### CPU Usage Monitor Settings

**Threshold-based**: Operator (More than/Less than/etc.), CPU usage threshold (1-100%, default 90%), Time period (1-60 min, default 5).

**Anomaly-based**: Model training period (default 21 days), Receive anomaly alerts during training, Sensitivity level (Low/Normal/High), Anomaly duration (default 15 min).

### Memory Usage Monitor Settings

**Threshold-based**: Operator, Memory usage threshold (1-100%, default 90%), Time period (1-60 min, default 5).

**Anomaly-based**: Model training period (default 21 days), Receive anomaly alerts during training, Sensitivity level (Low/Normal/High), Anomaly duration (default 30 min).

### Disk Transfer Rate Monitor Settings

**Threshold-based**: What to monitor (Read speed and Write speed / Read speed / Write speed), Read/Write speed operator, Read/Write speed threshold (default 0 kb/s), Read/Write speed time period (1-60 min, default 5).

**Anomaly-based**: What to monitor, Model training period (default 21 days), Sensitivity level, Anomaly duration (default 15 min).

### Network Usage Monitor Settings

**Threshold-based**: What to monitor (Incoming and Outgoing / Incoming / Outgoing), Network adapter, Incoming/Outgoing speed operator, threshold, and time period.

**Anomaly-based**: What to monitor, Network adapter, Model training period, Sensitivity level, Anomaly duration.
