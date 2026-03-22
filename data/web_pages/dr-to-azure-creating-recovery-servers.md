# Creating recovery servers in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Recovery servers in Microsoft Azure > Creating recovery servers in Microsoft Azure
Creating recovery servers in Microsoft Azure

Recovery servers are automatically created when you apply a disaster recovery protection plan to a workload. If a disaster recovery protection plan is not applied to the workload, you can create a recovery server manually.

Prerequisites

A backup plan is applied to the workload.

The DR site in Microsoft Azure is configured.

To create a recovery server in Microsoft Azure

In the Cyber Protect console, go to Devices > All devices.

Click the workload that you want to protect with Disaster Recovery, and then, in the Actions menu, click Disaster recovery.

Click Create recovery server.

In the Create recovery server wizard, on the Server configuration tab, configure the settings, and then click Next.

Setting	Description
CPU and RAM

Size of the Azure VM. Compute usage is charged directly to your Microsoft Azure subscription by Microsoft or your partner. If some Azure VM sizes are not available, check your Azure subscription limitations.

The following Azure VM types are excluded from selection:

A-series (deprecated in Microsoft Azure)

VM types that are based on ARM CPU architecture

The default settings are automatically determined based on the original device CPU and RAM configuration. The RAM is matched by rounding up to the nearest B-family VM size that meets or exceeds the original RAM value, and selecting the lowest available CPU core number that satisfies the RAM requirement. If RAM data from the original machine is unavailable (for example, for Azure VMs that use agentless backups), a minimal B-family VM size is selected by default. If the selected VM series or size is not available in the target region or subscription, the system automatically selects the closest available size from any B-family series within that region.


Disk type

Disk type of the Azure VM. The disk type that you select will be applied to all recovery server disks.

Only locally redundant storage (LRS) disk types are available for selection.

Premium SSD v2 and Ultra SSD are not available for selection.

Premium SSD v2 is automatically assigned during a failover, if 4K sector disks are detected in the backup of the original workload.


Name	Name for the recovery server that is visible in the Cyber Protect console. This name is not used for the Azure VM.
Description	Description of the recovery server

On the Network tab, configure the settings for the production and test network, and then click Next.

Setting	Description
Network

(For Production network)

The Azure Virtual Network (VNet) and subnet for production failover.

During a production failover, the server will be connected to this Azure network.


IP address in production network

(For Production network)

By default, the last octet of the original machine's IP address is derived within the production network range, but you can change the IP address at any time before the failover. When the server is in the Failover state, you can modify the IP address directly in Azure.


Network

(For Test network)

The Azure VNet and subnet for test failover. We recommend that the test network is isolated within a separate VNet.

During a test failover, the server will be connected to this Azure network.


IP address in test network

(For Test network)

By default, the last octet is derived from the original machine, within the test network range, but you can change the IP address at any time before the failover. When the server is in the Testing failover state, you can modify the IP address directly in Azure.

By default, no public IP is assigned to the recovery server, for security reasons. Without a public IP, the recovery server is only accessible from the local network. If necessary, assign a public IP directly in the Azure portal.

By default, Internet access is enabled for resources in Azure. No additional configuration is required to allow outbound internet traffic. If you need to restrict or isolate outgoing Internet access in a test network, you must configure appropriate security controls, such as Network Security Group (NSG) rules, User Defined Routes (UDRs), or Azure Firewall policies, depending on your requirements.

On the Automated test failover tab, do the following:

Turn on the Automated test failover switch.

Configure the settings.

Setting	Description
Schedule	Automated test failover runs once per month.
VM startup timeout / Minutes	The maximum period during which the system tries to start a virtual machine in Azure and take a screenshot to verify if the operating system loaded successfully. This period does not include the time for restoring the data from a cold backup archive, as this duration depends on the size of the archive. Additionally, Azure VM compute hours are not counted during the data restoration time.
Use as default timeout	Select this checkbox if you want to save the VM startup timeout / Minutes value as default. In this case, the value will be populated automatically when you enable automated test failover for other recovery servers.

Click Next.

On the Settings tab, do the following:

RPO threshold defines the maximum allowable time interval between the last recovery point and the current time. You can set a value within 15 – 60 minutes, 1 – 24 hours, 1 – 14 days.

[Optional] [If the backups for the selected machine are encrypted by using encryption as a machine property], specify the password that will be automatically used when creating a virtual machine for the recovery server from the encrypted backup.

Click Enter password, and then enter the password for the encrypted backup and define a name for the credentials.

By default, you will see the most recent backup in the list.

To view all the backups, select Show all backups.
Click Save.

Although the password that you specify will be stored in a secure credentials store, saving passwords might be against your compliance obligations.

Click Create.

The recovery server is created and is in the Standby state. No compute points are charged. All compute usage is billed directly to your Azure subscription.

You can configure firewall rules for the VM only in the in the Azure portal. By default, for VMs in test and production failover, all inbound connections are prohibited, and all outbound connections to Internet are allowed within the production and test VNet.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.