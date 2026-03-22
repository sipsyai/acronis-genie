# Agent-based failback via bootable media from Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failback in Microsoft Azure > Agent-based failback via bootable media from Microsoft Azure
Agent-based failback via bootable media from Microsoft Azure
The availability of this feature depends on the service quotas that are enabled for your account.

The agent-based failback via bootable media process is optimized for performing a failback to the original physical or virtual machine. During this process, only the delta changes are transferred to the local site.

The agent-based failback process via bootable media to a target physical or virtual machine consists of the following phases:

Planning. During this phase, you restore the IT infrastructure at your local site (such as the hosts and the network configurations), configure the failback parameters, and plan when to start the data transfer.

Data transfer. During this phase, the data is transferred from the cloud site to the local site while the virtual machine in the cloud continues to run. You can start the next phase - switchover - at any time during the data transfer phase, but you should consider the following relations.

The longer you remain in the data transfer phase,

the longer the virtual machine in the cloud continues to run.
the more data will be transferred to your local site.
the higher the cost you will pay (you spend more compute points).
the shorter the downtime period that you will experience during the switchover phase.

If you want to minimize the downtime, start the switchover phase after more than 90% of the data is transferred to the local site.

If you can afford to experience a longer downtime period, and do not want to spend more compute points for running the virtual machine in the cloud, you can start the switchover phase earlier.

The data transfer process uses a flashback technology. This technology compares the data that is available on the target machine to the data of the virtual machine in the cloud. If part of the data is already available on the target machine, it will not be transferred again. This technology makes the data transfer phase faster.

For this reason, we recommend that you restore the server to the original machine on your local site.

Switchover. During this phase, the virtual machine in the cloud is turned off, and the remaining data - including the last backup increment - is transferred to the local site. If no backup plan is applied on the recovery server, a backup will be performed automatically during the switchover phase, which will slow down the process.

Validation. During this phase, the machine on the local site is ready, and you can reboot it using a Linux-based bootable media. You can verify if the virtual machine is working correctly, and:
If everything is working as expected, confirm the failback. After the failback confirmation, the virtual machine in the cloud is deleted, and the recovery server returns to the Standby state. This is the end of the failback process.
If something is wrong, you can cancel the failover and return to the planning phase.

After the bootable media has been rebooted, you will not be able to use it again. If, at the validation phase, you discover something wrong, you must register a new bootable media and start the failback process again.

However, as flashback technology will be used, the data that is already on the local site will not be transferred again, and the failback process will be much faster.

Performing agent-based failback via bootable media from Microsoft Azure

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.