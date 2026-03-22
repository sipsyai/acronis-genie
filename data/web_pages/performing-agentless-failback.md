# Performing agentless failback via a hypervisor agent

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Failback > Performing agentless failback via a hypervisor agent
Performing agentless failback via a hypervisor agent
The availability of this feature depends on the service quotas that are enabled for your account.

You can perform an agentless failback to a target virtual machine on your local site via a hypervisor agent.

Prerequisites

The agent that you will use to perform failback is online and is not currently used for another failback operation.
Your internet connection is stable.
There is at least one full backup of the virtual machine in the cloud.

To perform an agentless failback to a virtual machine via a hypervisor agent

In the Cyber Protect console, go to Disaster Recovery > Servers.
Select the recovery server that is in the Failover state.
Click the Failback tab.

In the Failback parameters section, in the Failback type field, select Agentless via hypervisor agent, and then configure the other parameters.

Note that by default, some of the Failback parameters are populated automatically with suggested values, but you can change them.

The following table provides more information about the Failback parameters.

Parameter	Description
Backup size

Amount of data that will be transferred to your local site during the failback process.

After you start the failback process to a target virtual machine, the Backup size will be increasing during the data transfer phase, because the virtual machine in the cloud will continue to run and generate new data.

To calculate the estimated downtime period during the failback process to a target virtual machine, take 10% of the Backup size value (as we recommend that you start the switchover phase after 90% of the data is transferred to your local site), and divide it by the value of your Internet speed.

The value of the Internet speed will decrease when you perform several failback processes at the same time.


Target machine location

Failback location: a VMware ESXi host or a Microsoft Hyper-V host.

You can select from all the hosts that have an agent which is registered with the Cyber Protection service.


Agent

Agent which will perform the failback operation.

You can use one agent to perform one failback operation at the same time.

You can select an agent that is online and is not currently used for another failback process, has a version which supports the failback functionality, and has rights to access the backup.

Note that you can install several agents on VMware ESXi hosts, and start a separate failback process using each of them. These failback processes can be performed at the same time.


Target machine settings

Virtual machine settings:

Virtual processors. Select the number of virtual processors.

Memory. Select how much memory the virtual machine will have.

Units. Select the units for the memory.

Network adapters. To add a network adapter, click Add, and select a network in the Network field.

When you are ready with the changes, click Done.


Path

(For Microsoft Hyper-V hosts) Folder on the host where your machine will be stored.

Ensure that there is enough free memory space on the host for the machine.


Datastore

(For VMware ESXi hosts) Datastore on the host where your machine will be stored.

Ensure that there is enough free memory space on the host for the machine.


Provisioning mode

Method of allocation of the virtual disk.

For Microsoft Hyper-V hosts:

Dynamically expanding (default value).

Fixed size.

For Microsoft Hyper-V hosts:

Thin (default value).

Thick.


Target machine name

Name of the target machine. By default, the target machine name is the same as the recovery server name.

The target machine name must be unique on the selected Target machine location.

Click Start data transfer, and then in the confirmation window, click Start.

If there is no backup of the virtual machine in the cloud, the system will perform a backup automatically before the data transfer phase.

The Data transfer phase starts. The console displays the following information:

Field	Description
Progress

This parameter shows how much data is already transferred to the local site, and the total amount of data that must be transferred.

The total amount of data includes the data from the last backup before the data transfer phase was started, and the backups of the newly generated data (backup increments), as the virtual machine continues to run during the data transfer phase. For this reason, both values of the Progress parameter increase with time.


Downtime estimation

This parameter shows how much time the virtual machine in the cloud will be unavailable if you start the switchover phase now. The value is calculated based on the values of the Progress parameter, and decreases with time.

Click Switchover and then, in the confirmation window, click Switchover again.

The switchover phase starts. The console displays the following information:

Field	Description
Progress

This parameter shows the progress of restoring the machine on the local site.


Estimated time to finish

This parameter shows the approximate time when the switchover phase will be completed and you will be able to start the machine on the local site.

If no backup plan is applied to the virtual machine in the cloud, a backup will be performed automatically during the switchover phase, which will cause a longer downtime.

After the Switchover phase completes and the virtual machine at your local site is started automatically, validate that it is working as expected.

Click Confirm failback, and then in the confirmation window, click Confirm to finalize the process.

The virtual machine in the cloud is deleted, and the recovery server returns to the Standby state.

Applying a protection plan on the recovered server is not part of the failback process. After the failback process completes, apply a protection plan on the recovered server to ensure that it is protected again. You may apply the same protection plan that was applied on the original server, or a new protection plan that has the Disaster recovery module enabled.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.