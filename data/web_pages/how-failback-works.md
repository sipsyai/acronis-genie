# Failback

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Failback
Failback
The availability of this feature depends on the service quotas that are enabled for your account.

A failback is a process of moving the workload from the cloud back to a physical or virtual machine on your local site. You can perform a failback on a recovery server in Failover state, and continue using the server on your local site.

You can perform automated failover to a virtual or physical target machine on your local site. During the failback, you can transfer the backup data to your local site while the virtual machine in the cloud continues to run. This technology helps you to achieve a very short downtime period, which is estimated and displayed in the Cyber Protect console. You can view it and use this information to plan your activities and, if necessary, warn your clients about an upcoming downtime period. If you perform agent-based failback via bootable media, the downtime is even shorter, as only the delta changes will be transferred to the local site.

For a failback to a target physical machine, you can use the agent-based failback via bootable media. For more information, see Performing agent-based failback via bootable media.

For a failback to a target virtual machine, you can use the agent-based failback via bootable media or the agentless failback via hypervisor agent. For more information, see Performing agent-based failback via bootable media and Performing agentless failback via a hypervisor agent.

In specific cases when you cannot use the automated failback procedure, you can perform a manual failback. For more information, see Manual failback.

Runbook operations support the failback in manual mode only. This means that if you start the failback process by executing a runbook that includes a Failback server step, the procedure will require a manual interaction: you must manually recover the machine, and confirm or cancel the failback process from the Disaster Recovery > Servers tab.

Agent-based failback via bootable media

Agentless failback via a hypervisor agent

Manual failback

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.