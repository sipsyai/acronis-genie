---
title: "Disaster recovery dashboard"
section: "Implementing disaster recovery"
subsection: "Disaster recovery dashboard"
page_range: "1058-1061"
tags: [DR dashboard, eligible devices, health check, automated test failover, recovery servers in failover, primary servers, cloud server alerts, compute points usage, monitoring]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#disaster-recovery-dashboard.html"
---

# Disaster recovery dashboard

The disaster recovery **Dashboard** page contains widgets that provide a real-time overview and actionable insights for your disaster recovery site throughout its lifecycle. This helps you to:

- Quickly detect and resolve problems by monitoring the status of recovery and primary servers.
- Avoid overuse of compute points by monitoring the number of servers that consume them.

---

## Disaster recovery - eligible devices

The widget shows the total number of devices that are protected by Disaster recovery (have a recovery server) and the total number of devices that are eligible for protection by Disaster recovery.

To go to the **All devices** page where you can configure Disaster recovery for the eligible devices, click **Protect**.

---

## Health check

The widget shows information about the health of your disaster recovery infrastructure. You can check the state of the site configuration, network availability (available for Disaster Recovery to Cyber Protect Cloud only), and if there are missing service quotas.

The health check monitors the following:

| Item | Description |
|------|-------------|
| **Disaster recovery infrastructure** | Overall readiness state of the DR infrastructure (e.g., Ready) |
| **Network connectivity** | Status of the network connectivity (e.g., OK, Warning) |
| **Service quotas** | Whether service quotas are sufficient (e.g., OK) |

To view more information about detected issues (warnings or errors), click **View issues**.

---

## Automated test failover

The widget shows information about the automated test failover operations of your recovery servers. It displays:

- **Last run successful** -- Number of servers where the last automated test failover succeeded
- **Last run failed** -- Number of servers where the last automated test failover failed
- **No runs yet** -- Number of servers with automated test failover enabled but not yet run
- **Not configured** -- Number of servers where automated test failover is not configured

To start configuring automated test failover for your servers, click **Configure**.

To download the data from the widget, click **Report**, and then choose the format -- **PDF** or **CSV**.

The **PDF** report includes screenshots of the result of the automated test failover operations, which you can use to check the readiness of the servers for disaster recovery.

---

## Recovery servers in failover

The widget shows the number and status of the recovery servers that are in production or test failover.

If there are no recovery servers currently running in the cloud, you will see a zero. If there is an issue with any server, you will see a warning or an error status.

The displayed compute points usage per hour is a real-time snapshot, not a historical value. This means that if, for example, you have two recovery servers and each one of them uses eight points, you will see a total of 16 points displayed in the widget.

You can use this information to estimate the cost of running these servers, and also as a reminder to stop a failover of a server that you do not need anymore.

---

## Primary servers

The widget is available for Disaster Recovery to Cyber Protect Cloud only. It shows the number and status of the primary servers in your environment, and their compute point usage per hour. You can use this information to quickly spot and resolve any issues.

The displayed compute points usage per hour is a real-time snapshot, not a historical value. This means that if, for example, you have two recovery servers and each one of them uses eight points, you will see a total of 16 points displayed in the widget.

You can use this information to estimate the cost of running these servers, and also as a reminder to stop a failover of a server that you do not need anymore.

---

## Cloud server alerts

The widget shows the latest alerts by severity, so that you can see critical alerts at a glance. The **Alert type** and **Recovery server** values in the widget are links that open the alert details and recovery server details, respectively.

---

## Compute points usage

This widget shows the number of compute points that were used in your environment for the last 6 months -- the current month and each of the past five months.

You can download a detailed report as a CSV or PDF file. The report includes the following information about the servers that used compute points, for each month: server name, server type, state, started by, start time, stop time, hours on during the month, compute usage per hour, and total compute points usage for the month.

To download the data from the widget, click **Report**, and then select the file format that you prefer.

---

# Disaster Recovery compatibility with encryption software

Disaster recovery is compatible with the following disk-level encryption software:

- Microsoft BitLocker Drive Encryption
- McAfee Endpoint Encryption
- PGP Whole Disk Encryption

> **Note**
> - For workloads with disk-level encryption, we recommend that you install the protection agent in the guest operating system of the workload, and perform agent-based backups.
> - Failover and failback will not be supported for agentless backups of encrypted workloads.
