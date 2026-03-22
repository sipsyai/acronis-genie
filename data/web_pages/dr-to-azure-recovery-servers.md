# Recovery servers in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Recovery servers in Microsoft Azure
Recovery servers in Microsoft Azure

A recovery server is a replica of the original machine that is created from the protected server's backup (recovery point) that is stored in the cloud - Cyber Protect Cloud or Microsoft Azure. In case of a disaster, the workload is switched from the original server to the recovery server in Microsoft Azure.

Recovery servers are either created manually, or automatically - when you apply a disaster recovery protection plan to a workload.

No compute points are charged for running your recovery servers in Microsoft Azure. All compute usage is billed directly to your Microsoft Azure subscription.

MAC address configuration for recovery servers is not available in Disaster Recovery to Microsoft Azure.

Managing recovery servers

The following operations with recovery servers are available in Disaster Recovery to Microsoft Azure:

Operation	Description
Power on	[For servers in the Failover state] Power on the Azure VM (recovery server).
Power off

[For servers in the Failover state] Power off the Azure VM (recovery server).

The power off operation stops the Azure VM but does not deallocate resources. The VM will be in the Stopped (Allocated) state.

In this state, an Azure VM still reserves CPU and memory, incurring compute charges as if it is running. This state preserves the IP address and server placement of the VM.


Force power off	[For servers in the Failover state] Forcefully shut down the recovery server.
Edit settings	Modify the recovery server settings, such as network configurations or RPO thresholds from the Cyber Protect console.
Production failover	Switch workloads to the recovery server in the production network.
Test failover

Test the recovery server in the isolated test network without impacting production.

To avoid conflicts during failover, ensure that production and test networks are configured properly.

Regularly test failover operations to validate the recovery server functionality.


Connect (to console)

[For servers in the Failover state] After clicking Connect and being redirected to Azure, you can connect to the Azure virtual machine by using native Azure options, such as:

Assigning a public IP address and connecting via Remote Desktop Protocol (RDP) or SSH.

Using Azure Bastion, a secure service for connecting to the virtual machine without a public IP.

Creating recovery servers in Microsoft Azure

Editing the recovery server settings

Deleting a recovery server

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.