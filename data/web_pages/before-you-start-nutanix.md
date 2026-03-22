# Before You Start Nutanix

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Nutanix AHV > Before you start
Before you start

This appliance is a pre-configured virtual machine that you can deploy to a Nutanix cluster. The appliance contains a protection agent that can back up and recover the virtual machines in the cluster.

System requirements for the virtual appliance

We recommend that you configure the virtual appliance with 4 vCPUs (4 single-core vCPUs or 2 vCPUs with 2 cores each) and 8 GiB of RAM. These settings are sufficient for most operations.

To improve the backup performance and avoid failures related to insufficient RAM memory, you can increase the RAM memory to 16 GiB in more demanding cases. For example, when you expect the backup traffic to exceed 100 MB per second (as in 10-Gigabit networks) or if you back up simultaneously multiple virtual machines with large hard drives (500 GiB or more).

The size of the appliance virtual disk is 8 GiB.

How many virtual appliances do I need?

One virtual appliance can back up and recover all virtual machines in the cluster. You can use multiple virtual appliances per cluster if you want to distribute the bandwidth load of the backup traffic.

If more than one virtual appliance is deployed in the cluster, the automatic redistribution of the backed-up virtual machines occurs when the load imbalance among the appliances reaches 20 percent.

When you deploy an additional virtual appliance, the management server assigns the most appropriate virtual machines to the new appliance, and the load of the existing appliance decreases. When you remove a virtual appliance, the backed-up virtual machines are redistributed among the remaining appliances. Redistribution occurs only if you remove the virtual appliance from the Cyber Protect console. Redistribution will not start if you remove the virtual appliance from the Nutanix Prism Element console or if the appliance gets corrupted.

Limitations

The following operations are not supported:

Application-aware backup
Running a virtual machine from a backup
Replication of virtual machines
Backups of Nutanix volume groups
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.