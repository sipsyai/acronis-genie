# Failback from Microsoft Azure to an Azure virtual machine

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failback in Microsoft Azure > Failback from Microsoft Azure to an Azure virtual machine
Failback from Microsoft Azure to an Azure virtual machine

You can perform a failback from a Microsoft Azure virtual machine to the original Azure virtual machine by following the procedure for Performing a manual failback from Microsoft Azure and using one of the following recovery options in step 8:

Recovery options

Agentless recovery

Supports recovery only to a new Azure VM that is created automatically.

Process: Configure the Azure connection in the Cyber Protect console (Devices > Add > Microsoft Azure virtual machine).

A backup appliance VM is deployed in the Azure subscription to manage the recovery.

Recovery flow:

On the Backup storage screen, select a backup. Recover as an Azure VM.

You can use the same flow for physical, virtual, or agent-based backups.

Cost consideration: The appliance VM, when used for recovery only, can be powered on only during recovery, then turned off manually.

Agent-based recovery

Supports recovery to the same Azure VM (if the original VM with the agent is available) or a new Azure VM that has a new agent installed.

Process: Manually create a clean Windows/Linux VM in Azure. Install the protection agent. Use the agent to browse and recover backups from Acronis Cloud Storage.

For more information, see Recovering Microsoft Azure and Amazon EC2 machines.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.