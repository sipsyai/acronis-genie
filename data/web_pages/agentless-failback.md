# Agentless failback via a hypervisor agent

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Failback > Agentless failback via a hypervisor agent
Agentless failback via a hypervisor agent
The availability of this feature depends on the service quotas that are enabled for your account.

The agentless failback via a hypervisor agent process is optimized for performing a failback to a new virtual machine. If you want to perform a failback to the original virtual machine, follow the procedure for agent-based failback via bootable media.

The agentless failback via a hypervisor agent consists of four phases.

Planning. During this phase, you restore the IT infrastructure at your local site (such as the hosts and the network configurations), configure the failback parameters, and plan when to start the data transfer.

To minimize the total time for the failback process, we recommend that you start the data transfer phase immediately after you set up your local servers, and then continue with the configuration of the network and the rest of the local infrastructure during the data transfer phase.

Data transfer. During this phase, the data is transferred from the cloud site to the local site while the virtual machine in the cloud continues to run. You can start the next phase - switchover - at any time during the data transfer phase, but you should consider the following relations.

The longer you remain in the data transfer phase,

the longer the virtual machine in the cloud continues to run.
the more data will be transferred to your local site.
the higher the cost you will pay (you spend more compute points).
the shorter the downtime period that you will experience during the switchover phase.

If you want to minimize the downtime, start the switchover phase after more than 90% of the data is transferred to the local site.

If you can afford to experience a longer downtime period, and do not want to spend more compute points for running the virtual machine in the cloud, you can start the switchover phase earlier.

If you cancel the failback process during the data transfer phase, the transferred data will not be deleted from the local site. To avoid potential issues, manually delete the transferred data before you start a new failback process. The following data transfer process will start from the beginning.

Switchover. During this phase, the virtual machine in the cloud is turned off, and the remaining data - including the last backup increment - is transferred to the local site. If no backup plan is applied on the recovery server, a backup will be performed automatically during the switchover phase, which will slow down the process.

You can view the estimated time to finish (downtime period) of this phase in the Cyber Protect console. When all the data is transferred to the local site (there is no data loss, and the virtual machine on the local site is an exact copy of the virtual machine in the cloud), the switchover phase completes. The virtual machine on the local site is recovered, and the validation phase starts automatically.

Validation. During this phase, the virtual machine on the local site is ready and automatically started. You can verify if the virtual machine is working correctly, and:

If everything is working as expected, confirm the failback. After the failback confirmation, the virtual machine in the cloud is deleted, and the recovery server returns to the Standby state. This is the end of the failback process.
If something is wrong, you can cancel the switchover and return to the data transfer phase.

Performing agentless failback via a hypervisor agent

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.