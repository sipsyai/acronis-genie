# Creating a disaster recovery protection plan

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Creating a disaster recovery protection plan
Creating a disaster recovery protection plan

The disaster recovery protection plan is a protection plan in which the Disaster recovery module is enabled.

After you enable the disaster recovery functionality and apply the plan to your devices, the cloud network infrastructure (cloud site) is created automatically. For more information, see Default cloud network infrastructure.

Applying a disaster recovery protection plan creates recovery cloud network infrastructure only if it does not exist. Existing cloud networks are not changed or recreated.

After you configure disaster recovery, you will be able to perform a test or production failover from any of the recovery points generated after the recovery server was created for the device. Recovery points (backups) that were generated before the device was protected with disaster recovery (before the recovery server was created) cannot be used for failover.

A disaster recovery protection plan cannot be enabled if the IP address of a device cannot be detected. For example, when virtual machines are backed up agentless and are not assigned an IP address.

When you apply a protection plan, the same networks and IP addresses are assigned in the cloud site. The IPsec VPN connectivity requires that network segments of the cloud and local sites do not overlap. If a Multi-site IPsec VPN connectivity is configured, and you apply a protection plan to one or several devices later, you must additionally update the cloud networks and reassign the IP addresses of the cloud servers. For more information, see Reassigning IP addresses.

To create a disaster recovery protection plan

In the Cyber Protect console, go to Devices > All devices.
Select the machines that you want to protect.

Click Protect, and then click Create plan.

The protection plan default settings open.

Configure the backup options.

To use the disaster recovery functionality, the plan must back up the entire machine, or only the disks, required for booting up and providing the necessary services, to a cloud storage.


Enable the Disaster recovery module by turning on the switch next to the module name.

In the Location field, select where to create the disaster recovery infrastructure.

Click Create.

The plan is created and applied to the selected machines. The default network infrastructure and the recovery servers with default parameters are created. For more information, see Editing the default settings of a recovery server and Default cloud network infrastructure.

What to do next
You can edit the default configuration of the recovery server. For more information, see Editing the default settings of a recovery server.
You can edit the default networking configuration. For more information, see Connectivity and networks.

Editing the default settings of a recovery server

Default cloud network infrastructure

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.