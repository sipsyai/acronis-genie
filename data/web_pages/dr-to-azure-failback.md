# Failback in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failback in Microsoft Azure
Failback in Microsoft Azure

Failback is a process of moving the workload from the cloud back to a physical or virtual machine on your local site. You can perform a failback when a recovery server is in the Failover state, and then continue using the server on your local site.

You can perform automated failover to a virtual or physical target machine on your local site. During the failback, you can transfer the backup data to your local site while the virtual machine in the cloud continues to run. This technology helps you achieve a very short downtime period, which is estimated and displayed in the Cyber Protect console. You can view it and use this information to plan your activities and, if necessary, warn your clients about an upcoming downtime period. If you perform agent-based failback via bootable media, the downtime is even shorter, as only the delta changes will be transferred to the local site.

For a failback to a target physical machine, you can use the agent-based failback via bootable media. For more information, see Agent-based failback via bootable media from Microsoft Azure.

For a failback to a target virtual machine, you can use the agent-based failback via bootable media or the agentless failback via hypervisor agent. For more information, see Performing agent-based failback via bootable media from Microsoft Azure and Performing agentless failback via a hypervisor agent from Microsoft Azure.

When you cannot use the automated failback procedure, you can perform a manual failback. For more information, see Manual failback from Microsoft Azure.

Runbook operations support the failback in manual mode only. This means that if you start the failback process by executing a runbook that includes a Failback server step, the procedure will require a manual interaction: you must manually recover the machine, and confirm or cancel the failback process from the Disaster Recovery > Servers tab

Agent-based failback via bootable media from Microsoft Azure

Agentless failback via a hypervisor agent from Microsoft Azure

Manual failback from Microsoft Azure

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.