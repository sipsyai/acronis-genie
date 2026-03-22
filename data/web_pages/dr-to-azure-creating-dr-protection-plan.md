# Creating a disaster recovery protection plan with Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Creating a disaster recovery protection plan with Microsoft Azure
Creating a disaster recovery protection plan with Microsoft Azure

The disaster recovery protection plan is a protection plan in which the Disaster recovery module is enabled.

For Microsoft Azure, the DR site location must be configured. It is not possible to apply a protection plan with an Azure DR location if it was not configured.

Applying a disaster recovery protection plan creates cloud recovery servers. Existing cloud networks are not changed or recreated.

After you configure disaster recovery, you will be able to perform a test or production failover from any of the recovery points (backups) that were generated after the recovery server for the device was created. You cannot use recovery points that were generated before the device was protected with disaster recovery (before the recovery server was created).

A disaster recovery protection plan cannot be enabled if the IP address of a device cannot be detected. For example, when virtual machines are backed up agentless and are not assigned an IP address. In this case, we recommend that you create a recovery server manually.

When you apply a protection plan, recovery servers are configured in the subnet that was configured in the mapping rules during the configuration of the DR site location, based on the IP address of the original device. If the IP address matches any of the specified source local networks, the recovery server will be created in the corresponding Azure recovery network and subnet. The last octet of the private IP will be taken from the original machine's IP address.

To create a disaster recovery protection plan

In the Cyber Protect console, go to Devices > All devices.
Select the machines that you want to protect.

Click Protect, and then click Create plan.

The protection plan default settings open.

Configure the backup options.

To use the disaster recovery functionality, the plan must back up the entire machine, or only the disks, required for booting up and providing the necessary services, to the Cloud storage or Microsoft Azure storage.


Enable the Disaster recovery module by turning on the switch next to the module name.

In the Location field, select Microsoft Azure.

Click Create.

The plan is created and applied to the selected machines. The recovery servers with default parameters are created.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.