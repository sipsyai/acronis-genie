---
title: "Cloud server details, backups, firewall rules, and compute points"
section: "Implementing disaster recovery"
subsection: "Cloud servers"
page_range: "984-990"
tags: [cloud server details, RPO compliance, backups, firewall rules, compute points, server flavors, billing]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#compute-points.html"
---

# Viewing details about cloud servers

To view the details of the cloud servers, go to **Disaster Recovery** > **Servers**. There are two tabs there: **Recovery servers** and **Primary servers**. To show all optional columns in the table, click the gear icon.

You can find the following information about each cloud server by selecting it:

| Column | Description |
|--------|-------------|
| **Name** | A cloud server name defined by you |
| **Status** | The status reflecting the most severe issue with a cloud server (based on the active alerts) |
| **State** | A cloud server state |
| **VM state** | The power state of a virtual machine associated with a cloud server |
| **Active location** | The location where a cloud server is hosted. For example, **Cloud**. |
| **RPO threshold** | The maximum time interval allowed between the last suitable recovery point for failover and the current time. The value can be set within 15-60 minutes, 1-24 hours, 1-14 days. |
| **RPO compliance** | The RPO compliance is the ratio between the actual RPO and RPO threshold. The RPO compliance is shown if the RPO threshold is defined. It is calculated as follows: **RPO compliance = Actual RPO / RPO threshold** where **Actual RPO = current time - last recovery point time** |
| **Actual RPO** | The time passed since the last recovery point creation |
| **Last recovery point** | The date and time when the last recovery point was created |

## RPO compliance statuses

Depending on the value of the ratio between the actual RPO and RPO threshold, the following statuses are used:

| Status | Condition | Description |
|--------|-----------|-------------|
| **Compliant** | RPO compliance < 1x | A server meets the RPO threshold. |
| **Exceeded** | RPO compliance <= 2x | A server violates the RPO threshold. |
| **Severely exceeded** | RPO compliance <= 4x | A server violates the RPO threshold more than 2x times. |
| **Critically exceeded** | RPO compliance > 4x | A server violates the RPO threshold more than 4x times. |
| **Pending (no backups)** | N/A | The server is protected with the protection plan but the backup is being created and not completed yet. |

---

# Backups of cloud servers

Primary and recovery servers are backed up agentless on the cloud site. These backups have the following restrictions:

- The only possible backup location is the cloud storage. Primary servers are backed up to the **Primary servers backup** storage.
- Microsoft Azure backup locations are not supported.
- A backup plan cannot be applied to multiple servers. Each server must have its own backup plan, even if all of the backup plans have the same settings.
- Only one backup plan can be applied to a server.
- Application-aware backup is not supported.
- Encryption is not available.
- Backup options are not available.

When you delete a primary server, its backups are also deleted.

A recovery server is backed up only in the failover state. Its backups continue the backup sequence of the original server. When a failback is performed, the original server can continue this backup sequence. So, the backups of the recovery server can only be deleted manually or as a result of applying the retention rules. When a recovery server is deleted, its backups are always kept.

> **Note**
> The backup plans for cloud servers are performed according to UTC time.

---

# Firewall rules for cloud servers

You can configure firewall rules to control the inbound and outbound traffic of the primary and recovery servers on your cloud site.

You can configure inbound rules after you provision a public IP address for the cloud server. By default, TCP port 443 is allowed, and all other inbound connections are denied. You can change the default firewall rules, and add or remove Inbound exceptions. If a public IP is not provisioned, you can only view the inbound rules, but cannot configure them.

You can configure outbound rules after when you provision Internet access for the cloud server. By default, TCP port 25 is denied, and all other outbound connections are allowed. You can change the default firewall rules, and add or remove outbound exceptions. If Internet access is not provisioned, you can only view the outbound rules, but cannot configure them.

> **Note**
> For security reasons, there are predefined firewall rules that you cannot change:
> - For inbound and outbound: Permit ping (ICMP echo-request type 8, code 0 and ICMP echo-reply type 0, code 0), Permit ICMP need-to-frag (type 3, code 4), Permit TTL exceeded (type 11, code 0)
> - For inbound only: Non-configurable part: Deny all
> - For outbound only: Non-configurable part: Reject all

## Setting firewall rules for cloud servers

### To edit the firewall rules of a server on your cloud site

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Click the **Recovery servers** or **Primary servers** tab, depending on which server you want to edit.
3. Click the server, and then click **Edit**.
4. Click the **Cloud firewall rules** tab.
5. To change the default action for inbound connections:
   a. In the **Inbound** drop-down field, select the default action:
      - **Deny all** -- Denies any inbound traffic. You can add exceptions to allow traffic from specific IP addresses, protocols, and ports.
      - **Allow all** -- Allows all inbound TCP and UDP traffic. You can add exceptions to deny traffic from specific IP addresses, protocols, and ports.
   b. [Optional] Save filled-in exceptions if needed.
   c. Click **Confirm**.
6. To add an exception, click **Add exception** and specify the firewall parameters:

| Firewall parameter | Description |
|-------------------|-------------|
| **Protocol** | TCP, UDP, or TCP+UDP |
| **Server port** | A specific port number (e.g., 2298), a range of port numbers (e.g., 6000-6700), or any port number (use `*`) |
| **Client IP address** | A specific IP address (e.g., 192.168.0.0), a range using CIDR notation (e.g., 192.168.0.0/24), or any IP address (use `*`) |

7-11. Repeat similar steps for outbound rules, then click **Save**.

## Checking the cloud firewall activities

After an update of the configuration of the firewall rules of a cloud server, a log of the update activity becomes available in the Cyber Protect console. You can view the log and check the following information:

- User name of the user who updated the configuration
- Date and time of the update
- Firewall settings for inbound and outbound connections
- The default actions for inbound and outbound connections
- The protocols, ports and IP addresses of the exceptions for inbound and outbound connections

To view the details: go to **Monitoring** > **Activities**, click the corresponding activity, and click **All Properties**. The description should be **Updating cloud server configuration**. In the **context** field, inspect the information.

---

# Compute points

In Disaster Recovery to Cyber Protect Cloud, compute points are used for primary servers and recovery servers during test failover and production failover. Compute points reflect the compute resources used for running the servers (virtual machines) in the cloud.

The consumption of compute points during disaster recovery depends on the server's parameters, and the duration of the time period in which the server is in failover state. The more powerful the server and the longer the time period, the more compute points will be consumed. And the more compute points are consumed, the higher the price that you will be charged.

All servers that are running in Cyber Protect Cloud will be charged for compute points, depending on their configured flavor, and regardless of their state (powered on or powered off).

Recovery servers that are in the Standby state do not consume compute points and will not be charged for compute points.

| Type | CPU | RAM | Compute points |
|------|-----|-----|----------------|
| F1 | 1 vCPU | 2 GB | 1 |
| F2 | 1 vCPU | 4 GB | 2 |
| F3 | 2 vCPU | 8 GB | 4 |
| F4 | 4 vCPU | 16 GB | 8 |
| F5 | 8 vCPU | 32 GB | 16 |
| F6 | 16 vCPU | 64 GB | 32 |
| F7 | 16 vCPU | 128 GB | 64 |
| F8 | 16 vCPU | 256 GB | 128 |

For example, if you want to protect with Disaster Recovery one virtual machine with 4 vCPU of 16 GB RAM, and one virtual machine with 2 vCPU with 8 GB of RAM, the first virtual machine will consume 8 compute points per hour, and the second virtual machine -- 4 compute points per hour. If both virtual machines are in failover, the total consumption will be 12 compute points per hour, or 288 compute points for the whole day (12 compute points x 24 hours = 288 compute points).

> **Note**
> If the overage for the **Compute points** quota is reached, all primary and recovery servers will be shut down. It will not be possible to use these servers until the beginning of the next billing period, or until you increase the quota. The default billing period is a full calendar month.

\* vCPU refers to a physical central processing unit (CPU) that is assigned to a virtual machine, and is a time-dependent entity.
