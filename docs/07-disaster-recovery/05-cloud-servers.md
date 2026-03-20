---
title: "Cloud servers: recovery servers and primary servers"
section: "Implementing disaster recovery"
subsection: "Cloud servers"
page_range: "970-989"
tags: [cloud servers, recovery server, primary server, firewall rules, compute points, backups, IP addresses]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#configuring-cloud-servers.html"
---

# IP address reassignment

You must reassign the IP addresses of the cloud networks and the cloud servers in order to complete the configuration in the following cases:

- After you switch from Site-to-site Open VPN to Multi-site IPsec VPN, or the opposite.
- After you apply a protection plan (if the Multi-site IPsec VPN connectivity is configured).

## Cloud network

1. In the **Connectivity** tab, click the IP address of the cloud network.
2. In the **Network** pop-up, click **Edit**.
3. Type the new the network address and network mask.
4. Click **Done**.

After you reassign the IP address of a cloud network, you must reassign the cloud servers that belong to the reassigned cloud network.

## Cloud server

1. In the **Connectivity** tab, click the IP address of the server in the cloud network.
2. In the **Servers** pop-up, click **Change IP address**.
3. In the **Change IP address** pop-up, type the new IP address of the server, or use the automatically generated IP address which is part of the reassigned cloud network.

> **Note:** Disaster Recovery automatically assigns IP addresses from the cloud network to all cloud servers that were part of the cloud network before the reassignment. You can use the suggested IP addresses to reassign all the cloud servers at once.

4. Click **Confirm**.

## Reinstalling the VPN gateway

If there is an issue with the VPN gateway which you cannot resolve, you might want to reinstall it. Possible issues include: the VPN gateway is in **Error** status, **Pending** status for a long time, or the status is undetermined for a long time.

Reinstalling includes: deleting the existing VPN gateway VM completely, installing a new VM from the template, and applying the settings of the previous VPN gateway on the new VM.

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click the gear icon of the VPN gateway, and select **Reinstall VPN gateway**.
3. In the **Reinstall VPN gateway** dialog, enter your login.
4. Click **Reinstall**.

## Configuring custom DNS servers

When you configure a connectivity, Disaster Recovery creates your cloud network infrastructure. The cloud DHCP server automatically assigns default DNS servers to the recovery servers and primary servers, but you can change the default settings and configure custom DNS servers.

1. In the Cyber Protect console, go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**.
3. Click **Default (Provided by Cloud Site)**.
4. Select **Custom servers**.
5. Type the IP address of the DNS server.
6. [Optional] Click **Add** to add another DNS server IP address.

> **Note:** After you add the custom DNS servers, you can also add the default DNS servers as a fallback.

7. Click **Done**.

## Configuring local routing

In addition to your local networks extended through the VPN appliance, you may have other local networks that are not registered in the VPN appliance but have servers which need to communicate with cloud servers.

1. Go to **Disaster Recovery** > **Connectivity**.
2. Click **Show properties**, and then click **Local routing**.
3. Specify the local networks in the CIDR notation.
4. Click **Save**.

# Cloud servers

With Disaster Recovery to Cyber Protect Cloud, you can use two types of cloud servers: primary and recovery.

- **A primary server** is a virtual machine that is not linked to a machine on the local site. You can use primary servers to protect a specific application or run various auxiliary services (such as a web server).
- **A recovery server** is a virtual machine that is a replica of the original machine (protected server). The recovery server is based on the protected server backups that are stored in the cloud. In case of a disaster, recovery servers are used for switching workloads from the original servers.

## Creating a recovery server

> **Important:** When you perform a failover, you can select only recovery points that were created after the creation of the recovery server.

**Prerequisites:**
- A protection plan must back up the entire machine, or only the disks required for booting up and providing the necessary services, to a cloud storage.
- One of the connectivity types to the cloud site must be set.

### To create a recovery server

1. On the **All devices** tab, select the machine that you want to protect.
2. Click **Disaster recovery**, and then click **Create recovery server**.
3. In the **Create recovery server** wizard, on the **Server configuration** tab:
   a. Select the number of virtual cores and the size of RAM.

   > **Note:** You can see the compute points for every option. The number of compute points reflects the cost of running the recovery server per hour.

   b. [Optional] Change the default name of the recovery server.
   c. [Optional] Add a description.

4. On the **Network** tab:
   a. Specify the cloud network to which the server will be connected.
   b. Select the **DHCP** option:

   | DHCP option | Description |
   |-------------|-------------|
   | **Provided by cloud site** | Default setting. The IP address will be provided by an automatically configured DHCP server in the cloud. |
   | **Custom** | The IP address will be provided by your own DHCP server in the cloud. |

   c. Specify the **MAC address** (unique identifier assigned to the network adapter; can be used with custom DHCP to ensure the same IP is always assigned).
   d. Specify the IP address that the server will have in the production network (default: the IP address of the original machine).
   e. [Optional] Select the **Test IP address** check box and specify the IP address for test failover access.
   f. [Optional] Select the **Internet access** check box.
   g. [Optional] Select the **Use public IP address** check box (requires Internet access to be selected).

5. On the **Settings** tab, select **Set RPO threshold** and set the value (15-60 minutes, 1-24 hours, 1-14 days).

6. [Optional] If backups are encrypted, click **Enter password** and provide the password for the encrypted backup.

7. On the **Cloud firewall rules** tab, edit the default firewall rules.

8. Click **Create**.

The recovery server appears in **Disaster Recovery** > **Servers** > **Recovery servers**.

## Operations with recovery servers

Recovery servers are shown on **Disaster Recovery** > **Servers** > **Recovery servers** tab:

- **Power on** -- Click the recovery server, then click **Power on**.
- **Power off** -- Click the recovery server, click **Power off**, then confirm.
- **Force power off** -- Click the recovery server, click **Power off**, select **Force power off the server**, then click **Power off**.
- **Stop** -- Click the recovery server, then click **Stop**.
- **Edit settings** -- Click the recovery server, click **Stop**, then click **Edit** and modify the settings.

## Creating a primary server

A **primary server** is a virtual machine that does not have a linked machine on the local site. Primary servers are used for protecting an application by replication, or running various auxiliary services. Typically, a primary server is used for real-time data replication across servers running crucial applications (Active Directory replication, SQL replication, etc.).

Primary servers are always launched only in the production network and have the following network parameters:

| Parameter | Description |
|-----------|-------------|
| **Cloud network** | (required) The cloud network to which a primary server will be connected. |
| **IP address in production network** | (required) The IP address that the primary server will have. By default, the first free IP address from your production network is set. |
| **Public IP address** | (optional) The IP address for accessing a primary server from the Internet. |
| **Internet access** | (optional) Enables a primary server to access the Internet. |

### To create a primary server

1. Go to **Disaster Recovery** > **Servers** > **Primary servers** tab.
2. Click **Create**.
3. On the **Server configuration** tab:
   a. Select a template for the new virtual machine.
   b. Select the flavor of the configuration:

   | Type | vCPU | RAM (GB) | Maximum total disk space (GB) |
   |------|------|----------|-------------------------------|
   | F1 | 1 | 2 | 500 |
   | F2 | 1 | 4 | 1,000 |
   | F3 | 2 | 8 | 2,000 |
   | F4 | 4 | 16 | 4,000 |
   | F5 | 8 | 32 | 8,000 |
   | F6 | 16 | 64 | 16,000 |
   | F7 | 16 | 128 | 32,000 |
   | F8 | 16 | 256 | 64,000 |

   c. [Optional] Change the virtual disk size. Click **Add disk** if you need more than one hard disk (up to 10 disks).
   d. Change the default name.
   e. Add a description.

4. On the **Network** tab: configure cloud network, DHCP option, MAC address, IP address, Internet access, and public IP address.

5. [Optional] On the **Settings** tab, select **Set RPO threshold**.

6. [Optional] On the **Cloud firewall rules** tab, edit the default firewall rules.

7. Click **Create**.

The primary server becomes available in the production network. You can manage the server by using its console, RDP, SSH, or TeamViewer.

## Operations with primary servers

Primary servers are shown on **Disaster Recovery** > **Servers** > **Primary servers** tab. Same operations as recovery servers: Power on, Power off, Force power off, Stop, Edit settings, Apply protection plan.

## Viewing details about cloud servers

To view details, go to **Disaster Recovery** > **Servers**. Information available:

| Column | Description |
|--------|-------------|
| **Name** | A cloud server name defined by you |
| **Status** | The status reflecting the most severe issue with a cloud server (based on active alerts) |
| **State** | A cloud server state |
| **VM state** | The power state of a virtual machine associated with a cloud server |
| **Active location** | The location where a cloud server is hosted (e.g., Cloud) |
| **RPO threshold** | Maximum time interval allowed between the last suitable recovery point for failover and the current time (15-60 minutes, 1-24 hours, 1-14 days) |
| **RPO compliance** | The ratio between the actual RPO and RPO threshold. Statuses: **Compliant** (< 1x), **Exceeded** (<= 2x), **Severely exceeded** (<= 4x), **Critically exceeded** (> 4x), **Pending (no backups)** |
| **Actual RPO** | The time passed since the last recovery point creation |
| **Last recovery point** | The date and time when the last recovery point was created |

## Backups of cloud servers

Primary and recovery servers are backed up agentless on the cloud site. Restrictions:

- The only possible backup location is the cloud storage. Primary servers are backed up to the **Primary servers backup** storage.
- Microsoft Azure backup locations are not supported.
- A backup plan cannot be applied to multiple servers.
- Only one backup plan can be applied to a server.
- Application-aware backup is not supported.
- Encryption is not available.
- Backup options are not available.

When you delete a primary server, its backups are also deleted. A recovery server is backed up only in the failover state. Its backups continue the backup sequence of the original server.

> **Note:** The backup plans for cloud servers are performed according to UTC time.

## Firewall rules for cloud servers

You can configure firewall rules to control the inbound and outbound traffic of the primary and recovery servers on your cloud site.

**Inbound rules:** Configurable after you provision a public IP address. By default, TCP port 443 is allowed; all other inbound connections are denied. You can change defaults and add/remove exceptions.

**Outbound rules:** Configurable after you provision Internet access. By default, TCP port 25 is denied; all other outbound connections are allowed. You can change defaults and add/remove exceptions.

### Predefined rules (cannot change)

For inbound and outbound:
- Permit ping: ICMP echo-request (type 8, code 0) and ICMP echo-reply (type 0, code 0)
- Permit ICMP need-to-frag (type 3, code 4)
- Permit TTL exceeded (type 11, code 0)

### Setting firewall rules

1. In the Cyber Protect console, go to **Disaster Recovery** > **Servers**.
2. Click the **Recovery servers** or **Primary servers** tab.
3. Click the server, and then click **Edit**.
4. Click the **Cloud firewall rules** tab.
5. Configure inbound rules: In the **Inbound** drop-down, select **Deny all** or **Allow all**.
6. Add exceptions as needed, specifying: **Protocol** (TCP, UDP, TCP+UDP), **Server port**, and **Client IP address**.
7. Configure outbound rules similarly.
8. Click **Save**.

### Checking the cloud firewall activities

After updating firewall rules, a log of the update activity becomes available in the Cyber Protect console. You can view: user name, date and time, firewall settings, default actions, and protocols/ports/IP addresses of exceptions.
