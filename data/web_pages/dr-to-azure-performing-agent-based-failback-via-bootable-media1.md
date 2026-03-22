# Performing agent-based failback via bootable media from Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failback in Microsoft Azure > Performing agent-based failback via bootable media from Microsoft Azure
Performing agent-based failback via bootable media from Microsoft Azure
The availability of this feature depends on the service quotas that are enabled for your account.

You can perform agent-based failback via bootable media from Microsoft Azure to a target physical or virtual machine on your local site.

The data transfer process uses a flashback technology. This technology compares the data that is available on the target machine to the data of the virtual machine in the cloud. If part of the data is already available on the target machine, it will not be transferred again. This technology makes the data transfer phase faster.

For this reason, we recommend that you restore the server to the original machine on your local site.

Prerequisites

The agent that you will use to perform failback is online and is not currently used for another failback operation.
Your Internet connection is stable.

A registered bootable media is available.

For more information, see Creating bootable media to recover operating systems.

The target machine is the original machine on your local site, or has the same firmware as the original machine.
There is at least one full backup of the virtual machine in the cloud.

To perform a failback to a physical machine

In the Cyber Protect console, go to Disaster Recovery > Servers.
Select the recovery server that is in the Failover state.
Click the Failback tab.
In the Failback type field, select Agent-based via bootable media.

In the Target bootable media field, click Specify, select the bootable media, and then click Done.

We recommend that you use ready-made bootable media as it is already configured. For more information, see Creating bootable media to recover operating systems.

To change the default disk mapping, in the Disk mapping field, click Specify, map the disks of the backup to the disks of the target machine, and then click Done.

Click Start data transfer and then, in the confirmation window, click Start.

If there is no backup of the virtual machine in the cloud, the system will perform a backup automatically before the data transfer phase.

The data transfer phase starts. The console displays the following information:

Field	Description
Progress

This parameter shows how much data is already transferred to the local site, and the total amount of data that must be transferred.

The total amount of data includes the data from the last backup before the data transfer phase was started, and the backups of the newly generated data (backup increments), as the virtual machine continues to run during the data transfer phase. For this reason, the Progress values increase with time.

As the system uses a flashback technology during the data transfer and does not transfer the data that is already available on the target machine, the progress might be faster than what is initially calculated by the console.


Downtime estimation

This parameter shows how much time the virtual machine in the cloud will be unavailable if you start the switchover phase now. The value is calculated based on the values of the Progress parameter, and decreases with time.

As the system uses a flashback technology during the data transfer and does not transfer the data that is already available on the target machine, the downtime might be much shorter than the value that is initially displayed in the console.

Click Switchover and then, in the confirmation window, click Switchover again.

The switchover phase starts. The console displays the following information:

Field	Description
Progress

This parameter shows the progress of restoring the machine on the local site.


Estimated time to finish

This parameter shows the approximate time when the switchover phase will be completed and you will be able to start the machine on the local site.

If no backup plan is applied to the virtual machine in the cloud, a backup will be performed automatically during the switchover phase, which will cause a longer downtime.

After the Switchover phase completes, reboot the bootable media, and then verify that the physical machine on your local site is working as expected.

For more information, see Recovering disks by using bootable media.

Click Confirm failback and then, in the confirmation window, click Confirm to finalize the process.

The virtual machine in the cloud is deleted, and the recovery server returns to the Standby state.

Applying a protection plan on the recovered server is not part of the failback process. After the failback process completes, apply a protection plan on the recovered server to ensure that it is protected again. You may apply the same protection plan that was applied on the original server, or a new protection plan that has the Disaster recovery module enabled.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.