---
title: "Cloud servers - recovery servers and primary servers"
section: "Implementing disaster recovery"
subsection: "Cloud servers"
page_range: "976-984"
tags: [cloud servers, recovery server, primary server, create server, server configuration, DHCP, MAC address, RPO threshold, firewall rules, server operations]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#configuring-cloud-servers.html"
---

# Cloud servers

With Disaster Recovery to Cyber Protect Cloud, you can use two types of cloud servers: primary and recovery.

A **primary server** is a virtual machine that is not linked to a machine on the local site. You can use primary servers to protect a specific application or run various auxiliary services (such as a web server).

A **recovery server** is a virtual machine that is a replica of the original machine (protected server). The recovery server is based on the protected server backups that are stored in the cloud. In case of a disaster, recovery servers are used for switching workloads from the original servers.

---

# Configuring recovery servers

A **recovery server** is a replica of the original machine based on the protected server backups stored in the cloud. Recovery servers are used for switching workloads from the original servers in case of a disaster.

When creating a recovery server, you must specify the following network parameters:

| Parameter | Description |
|-----------|-------------|
| **Cloud network** | (required) The cloud network to which a recovery server will be connected. |
| **IP address in production network** | (required) The IP address with which a virtual machine for a recovery server will be launched. This address is used in both the production and test networks. Before launching, the virtual machine is configured for getting the IP address via DHCP. |
| **Test IP address** | (optional) The IP address to access a recovery server from the client-production network during a test failover, to prevent the production IP address from being duplicated in the same network. This IP address is different from the IP address in the production network. Internet access from the recovery server in the test network will be available if the **Internet access** option is selected during the recovery server creation. |
| **Public IP address** | (optional) The IP address to access a recovery server from the Internet. If a server has no public IP address, it can be reached only from the local network. |
| **Internet access** | (optional) Enables the recovery server to access the Internet (in both the production and test failover cases). |

## Creating a recovery server

To create a recovery server that will be a copy of your workload, follow the procedure below.

> **Important**
> When you perform a failover, you can select only recovery points that were created after the creation of the recovery server.

### Prerequisites

- A protection plan must be applied to the original machine that you want to protect. This plan must back up the entire machine, or only the disks, required for booting up and providing the necessary services, to a cloud storage.
- One of the connectivity types to the cloud site must be set.

### To create a recovery server

1. On the **All devices** tab, select the machine that you want to protect.
2. Click **Disaster recovery**, and then click **Create recovery server**.
3. In the **Create recovery server** wizard, on the **Server configuration** tab, do the following:
   a. Select the number of virtual cores and the size of RAM.
   b. [Optional] Change the default name of the recovery server.
   c. [Optional] Add a description.

> **Note**
> You can see the compute points for every option. The number of compute points reflects the cost of running the recovery server per hour.

4. On the **Network** tab, do the following:
   a. Specify the cloud network to which the server will be connected.
   b. Select the **DHCP** option.

   | DHCP option | Description |
   |-------------|-------------|
   | **Provided by cloud site** | This is the default setting. The IP address of the server will be provided by an automatically configured DHCP server in the cloud. |
   | **Custom** | The IP address of the server will be provided by your own DHCP server in the cloud. |

   c. Specify the **MAC address**. The MAC address is a unique identifier that is assigned to the network adapter of the server. If you use custom DHCP, you can configure it to always assign a specific IP address to a specific MAC address.
   d. Specify the IP address that the server will have in the production network. By default, the IP address of the original machine is set.
   e. [Optional] Select the **Test IP address** check box, and then specify the IP address. If you select this setting, you can test a failover in the isolated test network and connect to the recovery server via RDP or SSH during a test failover. During a test failover, the VPN gateway will replace the test IP address with the production IP address by using the NAT protocol.
   f. [Optional] Select the **Internet access** check box. If you select this setting, the recovery server will have access to the Internet during a production or test failover. By default, the TCP port 25 is open for outbound connections to public IP addresses.
   g. [Optional] Select the **Use public IP address** check box. With a public IP address, the recovery server becomes accessible from the Internet during a failover or test failover. The **Use public IP address** option requires the **Internet access** option to be selected. By default, TCP port 443 is open for inbound connections to public IP addresses.

> **Note**
> If you use a DHCP server, add the production IP address and test IP address to the server exclusion list to avoid IP address conflicts.

> **Note**
> If you clear the **Use Public IP address** check box or delete the recovery server, its public IP address will not be reserved.

5. On the **Settings** tab, select **Set RPO threshold**, and then set the value. The RPO threshold defines the maximum time interval between the last recovery point that is suitable for a failover and the current time. The value can be set within 15 - 60 minutes, 1 - 24 hours, 1 - 14 days.

6. [Optional] If the backups for the selected machine are encrypted by using encryption as a machine property, specify the password that will be automatically used when creating a virtual machine for the recovery server from the encrypted backup.
   a. Click **Enter password**, and then enter the password for the encrypted backup and define a name for the credentials.
   b. To view all the backups, select **Show all backups**.
   c. Click **Save**.

7. On the **Cloud firewall rules** tab, edit the default firewall rules.

8. Click **Create**.

The recovery server appears in the **Disaster Recovery** > **Servers** > **Recovery servers** tab.

---

# Operations with recovery servers

In the Cyber Protect console, recovery servers are shown on the **Disaster Recovery** > **Servers** > **Recovery servers** tab.

| Operation | Procedure |
|-----------|-----------|
| **Power on** | On the **Recovery servers** tab, click the recovery server, then click **Power on**. |
| **Power off** | On the **Recovery servers** tab, click the recovery server, click **Power off**, then in the **Power off server** screen, click **Power off**. |
| **Force power off** | On the **Recovery servers** tab, click the recovery server, click **Power off**, then in the **Power off server** screen, select **Force power off the server**, and then click **Power off**. |
| **Stop** | On the **Recovery servers** tab, click the recovery server, then click **Stop**. |
| **Edit settings** | On the **Recovery servers** tab, click the recovery server, click **Stop**, then click **Edit**, and then edit the settings. |

---

# Configuring primary servers

A **primary server** is a virtual machine that does not have a linked machine on the local site if compared to a recovery server. Primary servers are used for protecting an application by replication, or running various auxiliary services (such as a web server).

Typically, a primary server is used for real-time data replication across servers running crucial applications. You set up the replication by yourself, using the application's native tools. For example, Active Directory replication, or SQL replication, can be configured among the local servers and the primary server. Alternatively, a primary server can be included in an AlwaysOn Availability Group (AAG) or Database Availability Group (DAG).

Primary servers are always launched only in the production network and have the following network parameters:

| Parameter | Description |
|-----------|-------------|
| **Cloud network** | (required) The cloud network to which a primary server will be connected. |
| **IP address in production network** | (required) The IP address that the primary server will have in the production network. By default, the first free IP address from your production network is set. |
| **Public IP address** | (optional) The IP address for accessing a primary server from the Internet. If a server has no public IP address, it can be reached only from the local network, not through the Internet. |
| **Internet access** | (optional) Enables a primary server to access the Internet. |

## Creating a primary server

### Prerequisites

One of the connectivity types to the cloud site must be set.

### To create a primary server

1. Go to **Disaster Recovery** > **Servers** > **Primary servers** tab.
2. Click **Create**.
3. In the **Create primary server** wizard, on the **Server configuration** tab, do the following:
   a. Select a template for the new virtual machine.
   b. Select the flavor of the configuration (number of virtual cores and the size of RAM).

   | Type | vCPU | RAM (GB) | Maximum total amount of disk space (GB) |
   |------|------|----------|----------------------------------------|
   | F1 | 1 | 2 | 500 |
   | F2 | 1 | 4 | 1,000 |
   | F3 | 2 | 8 | 2,000 |
   | F4 | 4 | 16 | 4,000 |
   | F5 | 8 | 32 | 8,000 |
   | F6 | 16 | 64 | 16,000 |
   | F7 | 16 | 128 | 32,000 |
   | F8 | 16 | 256 | 64,000 |

   c. [Optional] Change the virtual disk size. If you need more than one hard disk, click **Add disk**, and then specify the new disk size. You can add up to 10 disks for a primary server.
   d. Change the default name of the recovery server.
   e. Add a description.

4. On the **Network** tab, configure network settings (cloud network, DHCP, MAC address, IP address, Internet access, public IP address).

5. [Optional] On the **Settings** tab, select **Set RPO threshold**, and then set the value. The value can be set within 15 - 60 minutes, 1 - 24 hours, 1 - 14 days.

6. [Optional] On the **Cloud firewall rules** tab, edit the default firewall rules.

7. Click **Create**.

The primary server becomes available in the production network. You can manage the server by using its console, RDP, SSH, or TeamViewer.

## Operations with primary servers

In the Cyber Protect console, primary servers are shown on the **Disaster Recovery** > **Servers** > **Primary servers** tab. Operations available: Power on, Power off, Force power off, Stop, Edit settings, Apply protection plan.

### Apply protection plan

1. On the **Primary servers** tab, click the primary server.
2. On the **Plan** tab, click **Create**.
   You will see a predefined protection plan where you can change only the schedule and retention rules.
