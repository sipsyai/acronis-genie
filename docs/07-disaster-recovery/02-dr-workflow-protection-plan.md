---
title: "DR workflow, protection plan, and default infrastructure"
section: "Implementing disaster recovery"
subsection: "Working with Disaster Recovery to Cyber Protect Cloud"
page_range: "935-938"
tags: [disaster recovery, workflow, protection plan, recovery server, cloud network, default settings]
acronis_version: "26.02"
---

# Automatic deletion of unused customer environments on the cloud site

The Disaster Recovery service tracks the usage of the customer environments created for disaster recovery purposes and automatically deletes them if they are unused.

The following criteria are used to define if the customer tenant is active:

- Currently, there is at least one cloud server or there were cloud server(s) in the last seven days. OR
- The **VPN access to local site** option is enabled and either the Site-to-site Open VPN tunnel is established or there are data reported from the VPN appliance for the last 7 days.

All the rest of the tenants are considered as inactive tenants. For such tenants the system performs the following:

- Deletes the VPN gateway and all cloud resources related to the tenant.
- Unregisters the VPN appliance.

The inactive tenants are rolled back to their state before the connectivity was configured.

# Working with Disaster Recovery to Cyber Protect Cloud

The basic workflow for using disaster recovery is the following:

1. **Create a recovery server** of the workload that you want to protect in one of the following ways:
   - a. Create a protection plan that includes the **Disaster recovery** module and the **Backup** module with the **What to backup** setting set to **Entire machine** or **System and boot volumes**.
   - b. Apply the plan to your devices. This will automatically set up the default disaster recovery infrastructure.

   > **Note:** Unit administrators cannot create, modify, or apply disaster recovery protection plans.

   - Set up the disaster recovery cloud infrastructure manually and control each step. See "Creating a recovery server."

2. **Configure the connectivity** to the cloud site:
   - Cloud-only mode
   - Site-to-site OpenVPN connection
   - Multi-site IPsec VPN connection
   - Point-to-site connection

3. Configure automated test failover.
4. Perform a test failover.
5. [When a disaster occurs] Perform a production failover.
6. [After the disaster] Perform a failback to the local site.
7. [Optional] Configure runbooks.

# Creating a disaster recovery protection plan

The disaster recovery protection plan is a protection plan in which the **Disaster recovery** module is enabled.

After you enable the disaster recovery functionality and apply the plan to your devices, the cloud network infrastructure (cloud site) is created automatically.

> **Note:**
> - Applying a disaster recovery protection plan creates recovery cloud network infrastructure only if it does not exist. Existing cloud networks are not changed or recreated.
> - After you configure disaster recovery, you will be able to perform a test or production failover from any of the recovery points generated after the recovery server was created for the device. Recovery points (backups) that were generated before the device was protected with disaster recovery (before the recovery server was created) cannot be used for failover.
> - A disaster recovery protection plan cannot be enabled if the IP address of a device cannot be detected.
> - When you apply a protection plan, the same networks and IP addresses are assigned in the cloud site. The IPsec VPN connectivity requires that network segments of the cloud and local sites do not overlap.

## To create a disaster recovery protection plan

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Select the machines that you want to protect.
3. Click **Protect**, and then click **Create plan**. The protection plan default settings open.
4. Configure the backup options. To use the disaster recovery functionality, the plan must back up the entire machine, or only the disks required for booting up and providing the necessary services, to a cloud storage.
5. Enable the **Disaster recovery** module by turning on the switch next to the module name.
6. In the **Location** field, select where to create the disaster recovery infrastructure.
7. Click **Create**.

The plan is created and applied to the selected machines. The default network infrastructure and the recovery servers with default parameters are created.

## What to do next

- Edit the default configuration of the recovery server. See "Editing the default settings of a recovery server."
- Edit the default networking configuration. See "Connectivity and networks."

# Editing the default settings of a recovery server

When you create and apply a disaster recovery protection plan, a recovery server is created with default settings. You can edit these default settings when necessary.

> **Note:** A recovery server is created only if it does not exist. Existing recovery servers are not changed or recreated.

## To edit the default settings of the recovery server

1. Go to **Devices** > **All devices**.
2. Select a device, and click **Disaster recovery**.
3. Edit the default settings of the recovery server.

| Setting | Default value | Description |
|---------|-------------|-------------|
| **CPU and RAM** | auto | The number of virtual CPUs and the amount of RAM for the recovery server. The default settings will be automatically determined based on the original device CPU and RAM configuration. |
| **Cloud network** | auto | Cloud network to which the server will be connected. For details on how cloud networks are configured, see Cloud network infrastructure. |
| **IP address in production network** | auto | The IP address that the server will have in the production network. By default, the IP address of the original machine is set. |
| **Test IP address** | disabled | Test IP address gives you the capability to test a failover in the isolated test network and to connect to the recovery server via RDP or SSH during a test failover. In the test failover mode, the VPN gateway will replace the test IP address with the production IP address by using the NAT protocol. If a test IP address is not specified, the console will be the only way to access the server during a test failover. |
| **Internet Access** | enabled | Enable the recovery server to access the Internet during a real or test failover. By default, TCP port 25 is denied for outbound connections. |
| **Use Public address** | disabled | Having a public IP address makes the recovery server available from the Internet during a failover or test failover. If you do not use a public IP address, the server will be available only in your production network. The public IP address will be shown after you complete the configuration. By default, TCP port 443 is open for inbound connections. |
| **Set RPO threshold** | disabled | RPO threshold defines the maximum allowable time interval between the last recovery point and the current time. The value can be set within 15 -- 60 minutes, 1 -- 24 hours, 1 -- 14 days. |

# Default cloud network infrastructure

The cloud network infrastructure that is created automatically when you apply a disaster recovery protection plan to your workloads consists of the following components:

- **A recovery server for each protected device.** The recovery server is a virtual machine in the cloud that is a copy of the selected device. For each of the selected devices, a recovery server with default settings is created in the **Standby** state (virtual machine not running). The recovery server is sized automatically depending on the CPU and RAM of the protected device.
- **VPN gateway** on the cloud site.
- **Cloud networks** to which the recovery servers are connected.

The system checks devices IP addresses and if there are no existing cloud networks where an IP address fits, it automatically creates suitable cloud networks. If you already have existing cloud networks where the recovery servers IP addresses fit, the existing cloud networks will not be changed or recreated.

Key points about network configuration:

- If you do not have existing cloud networks or you setup disaster recovery configuration for the first time, the cloud networks will be created with maximum ranges recommended by IANA for private use (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16) based on your devices IP address range. You can narrow your network by editing the network mask.
- If you have devices on multiple local networks, the network on the cloud site may become a superset of the local networks. You may reconfigure networks in the **Connectivity** section.
- If you need to set up Site-to-site Open VPN connectivity, download the VPN appliance and configure it. Make sure your cloud network ranges match your local network ranges connected to the VPN appliance.
- To change the default network configuration, navigate to **Disaster Recovery** > **Connectivity**, or on the **Disaster recovery** module of the protection plan, click **Go to connectivity**.

If you revoke, delete, or turn off the **Disaster recovery** module of a protection plan, the recovery servers and cloud networks will not be deleted automatically. You can remove the disaster recovery infrastructure manually, if necessary.
