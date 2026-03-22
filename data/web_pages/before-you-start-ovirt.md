# Before You Start Ovirt

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for oVirt (Virtual Appliance) > Before you start
Before you start

This appliance is a preconfigured virtual machine that you deploy in a Red Hat Virtualization/oVirt environment. The appliance contains a protection agent that can back up and recover the virtual machines in the environment.

System requirements for the agent

By default, the virtual appliance uses 2 vCPUs and 4 GiB of RAM. These settings are sufficient for most operations.

To improve the backup performance and avoid failures related to insufficient RAM, you can increase the number of vCPUs to four, and the RAM to 8 GiB in more demanding cases. For example, when you expect the backup traffic to exceed 100 MB per second (as in 10-Gigabit networks) or if you simultaneously back up multiple virtual machines with large hard drives (500 GiB or more).

The size of the appliance virtual disk is 8 GiB.

How many agents do I need?

One virtual appliance can back up and recover all virtual machines in the environment. You can use multiple virtual appliances if you want to distribute the bandwidth load of the backup traffic.

If more than one virtual appliance is deployed in the environment, the automatic redistribution of the backed-up virtual machines occurs when the load imbalance among the appliances reaches 20 percent.

When you deploy an additional virtual appliance, the management server assigns the most appropriate virtual machines to the new appliance, and the load of the existing appliance decreases. When you remove a virtual appliance, the backed-up virtual machines are redistributed among the remaining appliances. Redistribution occurs only if you remove the virtual appliance from the Cyber Protect console. Redistribution will not start if you remove the virtual appliance from the Red Hat Virtualization/oVirt Administration Portal or if the appliance gets corrupted.

To check which agent manages a specific machine

In the Cyber Protect console, click Devices, and then select oVirt.
Click the gear icon in the upper-right corner of the table, and under System, select the Agent checkbox.
Check the name of the agent in the column that appears.
Limitations

The following operations are not supported for Red Hat Virtualization/oVirt virtual machines:

Application-aware backup
Running a virtual machine from a backup
Replication of virtual machines
Changed block tracking
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.