---
title: "Recovery servers and failover in Microsoft Azure"
section: "Implementing disaster recovery"
subsection: "Disaster Recovery to Microsoft Azure"
page_range: "1029-1040"
tags: [Azure recovery servers, Azure failover, production failover, test failover, automated test failover, Azure VM, IP conflict, Linux failover, worker deployment]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#dr-to-azure-recovery-servers.html"
---

# Recovery servers in Microsoft Azure

A recovery server is a replica of the original machine that is created from the protected server's backup (recovery point) that is stored in the cloud -- Cyber Protect Cloud or Microsoft Azure. In case of a disaster, the workload is switched from the original server to the recovery server in Microsoft Azure.

Recovery servers are either created manually, or automatically -- when you apply a disaster recovery protection plan to a workload.

No compute points are charged for running your recovery servers in Microsoft Azure. All compute usage is billed directly to your Microsoft Azure subscription.

MAC address configuration for recovery servers is not available in Disaster Recovery to Microsoft Azure.

## Managing recovery servers

The following operations with recovery servers are available in Disaster Recovery to Microsoft Azure:

| Operation | Description |
|-----------|-------------|
| **Power on** | [For servers in the Failover state] Power on the Azure VM (recovery server). |
| **Power off** | [For servers in the Failover state] Power off the Azure VM. The power off operation stops the Azure VM but does not deallocate resources. The VM will be in the Stopped (Allocated) state. In this state, an Azure VM still reserves CPU and memory, incurring compute charges as if it is running. This state preserves the IP address and server placement of the VM. |
| **Force power off** | [For servers in the Failover state] Forcefully shut down the recovery server. |
| **Edit settings** | Modify the recovery server settings, such as network configurations or RPO thresholds from the Cyber Protect console. |
| **Production failover** | Switch workloads to the recovery server in the production network. |
| **Test failover** | Test the recovery server in the isolated test network without impacting production. To avoid conflicts during failover, ensure that production and test networks are configured properly. Regularly test failover operations to validate the recovery server functionality. |
| **Connect (to console)** | [For servers in the Failover state] After clicking **Connect** and being redirected to Azure, you can connect to the Azure virtual machine by using native Azure options, such as: assigning a public IP address and connecting via RDP or SSH, or using Azure Bastion for a secure connection without a public IP. |

## Creating recovery servers in Microsoft Azure

Recovery servers are automatically created when you apply a disaster recovery protection plan to a workload. If a disaster recovery protection plan is not applied to the workload, you can create a recovery server manually.

### Prerequisites

- A backup plan is applied to the workload.
- The DR site in Microsoft Azure is configured.

### To create a recovery server in Microsoft Azure

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Click the workload that you want to protect with Disaster Recovery, and then, in the **Actions** menu, click **Disaster recovery**.
3. Click **Create recovery server**.
4. In the **Create recovery server** wizard, on the **Server configuration** tab, configure the settings, and then click **Next**.

| Setting | Description |
|---------|-------------|
| **CPU and RAM** | Size of the Azure VM. Compute usage is charged directly to your Microsoft Azure subscription. The following Azure VM types are excluded: A-series (deprecated) and ARM CPU architecture types. The default settings are automatically determined based on the original device CPU and RAM configuration, rounding up to the nearest B-family VM size. If RAM data from the original machine is unavailable, a minimal B-family VM size is selected by default. |
| **Disk type** | Disk type of the Azure VM. Only locally redundant storage (LRS) disk types are available. Premium SSD v2 and Ultra SSD are not available. Premium SSD v2 is automatically assigned during a failover if 4K sector disks are detected. |
| **Name** | Name for the recovery server visible in the Cyber Protect console. This name is not used for the Azure VM. |
| **Description** | Description of the recovery server. |

5. On the **Network** tab, configure the settings for the production and test network, and then click **Next**.

| Setting | Description |
|---------|-------------|
| **Network** (Production) | The Azure Virtual Network (VNet) and subnet for production failover. |
| **IP address in production network** | By default, the last octet of the original machine's IP address is derived within the production network range. You can change the IP address at any time before the failover. |
| **Network** (Test) | The Azure VNet and subnet for test failover. We recommend that the test network is isolated within a separate VNet. |
| **IP address in test network** | By default, the last octet is derived from the original machine, within the test network range. |

> **Note**
> - By default, no public IP is assigned to the recovery server, for security reasons. Without a public IP, the recovery server is only accessible from the local network. If necessary, assign a public IP directly in the Azure portal.
> - By default, Internet access is enabled for resources in Azure. If you need to restrict or isolate outgoing Internet access in a test network, you must configure appropriate security controls, such as NSG rules, User Defined Routes (UDRs), or Azure Firewall policies.

6. On the **Automated test failover** tab, do the following:
   a. [Optional] Turn on the **Automated test failover** switch.
   b. [Optional] Configure the settings:

   | Setting | Description |
   |---------|-------------|
   | **Schedule** | Automated test failover runs once per month. |
   | **VM startup timeout / Minutes** | The maximum period during which the system tries to start a virtual machine in Azure and take a screenshot. This period does not include the time required to restore data from a cold backup archive. Azure VM compute hours are not counted during the data restoration time. |
   | **Use as default timeout** | Select this checkbox to save the VM startup timeout value as the default for other recovery servers. |

   c. Click **Next**.

7. On the **Settings** tab, do the following:
   a. [Optional] RPO threshold defines the maximum allowable time interval between the last recovery point and the current time. Values: 15 - 60 minutes, 1 - 24 hours, 1 - 14 days.
   b. [Optional] If the backups are encrypted, specify the password for the encrypted backup.
8. Click **Create**.

The recovery server is created and is in the Standby state. No compute points are charged. All compute usage is billed directly to your Azure subscription.

> **Note**
> You can configure firewall rules for the VM only in the Azure portal. By default, for VMs in test and production failover, all inbound connections are prohibited, and all outbound connections to Internet are allowed within the production and test VNet.

## Editing the recovery server settings

1. In the Cyber Protect console, go to **Disaster Recovery** > **Recovery servers**.
2. Click the server whose settings you want to edit, and then click **Edit**.
3. Edit the recovery server settings.
4. Click **Save**.

## Deleting a recovery server

1. In the Cyber Protect console, go to **Disaster Recovery** > **Recovery servers**.
2. Click the server that you want to delete, and then click **Delete**.
3. In the confirmation window, click **Delete**.

---

# Failover in Microsoft Azure

## Production failover

Failover is the process switching the workload from the original server at your local site to the recovery server. When a recovery server is created, it stays in the **Standby** state. The corresponding virtual machine does not exist in Microsoft Azure until you start a failover. Before you start a failover, you must create at least one disk image backup (with bootable volume) of the original machine.

When you start a failover, you select the recovery point (backup) of the original machine from which a virtual machine with the predefined parameters will be created in Microsoft Azure. When the failover completes, the recovery server state changes to **Failover**. The workload is now switched from the original machine to the recovery server in Microsoft Azure.

If the recovery server has a protection agent, to avoid interference (such as starting a backup or reporting outdated statuses to the backup component), the agent service is stopped.

### Failover of Windows machines

For Windows machines, if the `DeviceInstallDisabled` parameter is set to 1, the disaster recovery service will set the value to 0 or remove the parameter completely during failover. This is required for driver and device installation.

### IP Address conflict handling in failover

If the configured IP address in the production network is already in use at the time of the production failover, another available IP address from the same network will be assigned automatically. If the configured test network IP address is already in use at the time of the test failover, another available IP address from the test network will be assigned.

### Recovery of recovery server in failover to a previous point in time

To recover a server in failover from a different recovery point, initiate a new failover from a different recovery point to restore operations.

### Failover widgets

During production and test failover, you can see information about failover performance (recovery speed) and bottlenecks on the **Activities** tab of the recovery server details. To view the **Bottleneck** widget, expand the **Creating virtual machine** activity, and then in the **Copying data from the backup to the virtual machine disks** subactivity, expand **Bottleneck**.

### Performing a production failover in Microsoft Azure

1. In the Cyber Protect console, go to **Disaster Recovery** > **Recovery servers**.
2. Click the server that you want to fail over, and then click **Failover**.
3. In the **Server failover** window, select **Production failover**, and then select the recovery point (backup) from which the cloud server will be started.
4. Click **Start**.

When failover completes, the service starts running on the virtual machine in Azure. Clicking **Connect** will redirect you to the virtual machine in Azure.

---

# Test failover in Microsoft Azure

A test failover is a vital part of the Disaster Recovery as a Service (DRaaS) strategy in Microsoft Azure. It enables organizations to validate recovery processes without affecting production environments. This is done by simulating the recovery of a virtual machine (VM) from a selected recovery point (backup). The process creates a temporary VM in an isolated Azure virtual network (VNet) to test recovery procedures, configurations, and applications functionality.

### Test failover process

The test failover process consists of the following phases:

1. **Initiation** -- You select a recovery point and start the test failover.
2. **Worker (temporary agent) deployment** -- A worker that is used for the test failover operation is automatically deployed. The initial deployment for a test or production failover may take several minutes. Starting workers for subsequent failovers should be faster.
3. **Data restoration** -- Data is copied from the backup storage to a temporary Azure Blob Storage container. After the data is copied, the Blob Storage content is converted into a managed disk, which is then used to start the temporary VM.
4. **Recovery VM creation** -- The recovery VM is connected to the preconfigured isolated Azure VNet and subnet. By default, the VM is assigned an IP address where the last octet matches the original machine's IP address.
5. **Verification** -- After the VM is created, clicking the **Connect** button will redirect you to the specific VM in the Azure portal. Perform all necessary tests to verify application behavior, connectivity, and recovery objectives.

### Stopping the test failover

Stopping the test failover deletes the temporary VM and associated resources and the worker. If an encryption password was used, it is automatically deleted from the credential store.

### Performing a test failover in Microsoft Azure

> **Important**
> You can perform failover only from recovery points (backups) that were created after the recovery server of the device was created. At least one recovery point must be created. The maximum number of recovery points that is supported is 100.

### Prerequisites

- The recovery server is configured in Azure location and has at least one recovery point.
- An isolated Azure VNet and subnet for the test failover.
- Network security group (NSG) rules are configured to meet your requirements.

### To perform a test failover in Microsoft Azure

1. In the Cyber Protect console, go to **Disaster Recovery** > **Recovery servers**.
2. Click the server that you want to fail over, and then click **Failover**.
3. In the **Server failover** window, select **Test failover**, and then select the recovery point (backup).
4. Click **Start**.
5. If the backup is encrypted, enter the encryption password. [Optional] Save the password to a secure credentials store.
6. Test the recovery server via Console, RDP/SSH, or by running a script.
7. When the test is complete, click **Stop testing**. Changes made during the test failover are not saved.

---

# Automated test failover in Microsoft Azure

Automated test failover in Microsoft Azure validates backup integrity by booting a recovery server VM from the latest backup and capturing a screenshot to confirm that the operating system started successfully.

With automated test failover, the recovery server is tested automatically once a week or once a month, without any manual interaction.

The automated test failover process:

1. Creating a virtual machine in Microsoft Azure from the latest recovery point.
2. Taking a screenshot of the virtual machine.
3. Analyzing if the operating system of the virtual machine starts successfully.
4. Notifying you about the test failover status.

> **Note**
> Automated test failover consumes Azure VM compute hours.

## Configuring automated test failover in Microsoft Azure

1. In the Cyber Protect console, go to **Disaster Recovery** > **Dashboard**.
2. In the **Automated test failover** widget, click **Configure**.
3. Select one or more recovery servers and then click **Next**.
4. Turn on the **Automated test failover** switch.
5. In the **Schedule** field, select how often automated test failover should be performed (**Monthly** or **Weekly**).
6. [Optional] In **VM startup timeout / Minutes**, change the default value. Note: This timeout does not include the time required to restore data from a cold backup archive. Azure VM compute hours are not counted during the data restoration process. During cold data restore, Azure temporarily creates a standard Blob storage, which is later converted into a managed disk for the VM.
7. [Optional] To save the timeout value as the default, select **Set as default timeout**.
8. Click **Configure**.

## Viewing and disabling automated test failover

To view: go to **Disaster Recovery** > **Recovery servers**, select the recovery server, and check the **Automated test failover** section. [Optional] Click **Show screenshot**.

To disable: select the recovery server, click **Edit**, go to the **Automated test failover** tab, turn off the switch, and click **Save**.

---

# Requirements and limitations for failover of Linux VMs to Microsoft Azure

## Requirements

### Azure VM Agent installation with Internet access

The Azure VM Agent is automatically installed during test and production failover. The required Linux tools (e.g., **cloud-init**, network drivers) are fetched from public repositories (e.g., `archive.ubuntu.com` or `mirror.centos.org`). For security, you can allow outbound https only to specific repositories.

### Azure VM Agent installation without Internet access

You must manually install the Azure VM Agent on the source Linux machine before failover. Without the agent, the failover may fail or result in limited VM functionality.

## Limitations

- **Internet dependency**: No Internet access on the target Azure VM will require an Azure agent to be preinstalled on the original workload. No access to Internet might prevent post-failover updates.

## Recommendations

- Allow Internet access for production and test VNet before a failover (this is a default setup).
- Restrict outbound access to only specific Linux repositories if you know them before a failover.
- You can use internal mirrors or VPN to minimize Internet reliance.
- Run regular test failovers to ensure environment readiness.
