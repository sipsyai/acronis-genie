# Failback from Cyber Protect Cloud to an Azure virtual machine

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Failback > Failback from Cyber Protect Cloud to an Azure virtual machine
Failback from Cyber Protect Cloud to an Azure virtual machine

You can perform a failback from Cyber Protect Cloud to the original Azure virtual machine by following the procedure for Performing manual failback and using one of the following recovery options in step 8.

Recovery options

Agentless recovery

Supports recovery only to a new Azure VM that is created automatically.

Configure the Azure connection in the Cyber Protect console (Devices > Add > Microsoft Azure virtual machine).

A backup appliance VM is deployed in the Azure subscription to manage the recovery.

Recovery flow:

On the Backup storage screen, select a backup.

Recover as an Azure virtual machine.

You can use the same flow for physical, virtual, or agent-based backups.

To reduce incurred costs, the appliance virtual machine, when used for recovery only, can be powered on only during recovery, and then turned off manually.

Agent-based recovery

Supports recovery to the same Azure virtual machine (if the original virtual machine with the agent is available) or a new Azure virtual machine that has a new agent installed.

The process consists of the following steps:

Manually create a clean Windows or Linux virtual machine in Azure.
Install the protection agent.
Use the agent to browse and recover backups from Acronis Cloud Storage.

For more information, see Recovering Microsoft Azure and Amazon EC2 machines.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.