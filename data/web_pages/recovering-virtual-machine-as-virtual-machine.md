# Recovering a virtual machine as a virtual machine

Managing the backup and recovery of workloads and files > Recovery > Recovery of virtual machines > Recovering a virtual machine as a virtual machine
Recovering a virtual machine as a virtual machine

You can recover a backup of a virtual machine to the original hypervisor or to a different type of hypervisor. Recovery to a different type of hypervisor is called cross-platform recovery (machine migration). For more information, see Cross-platform recovery.

Recovering to a virtual machine on which a protection agent is not installed is done on the hypervisor level. This is an agentless recovery.

Recovery to a virtual machine on which a protection agent is installed is an agent-based recovery. This type of recovery is the same as a recovery to a physical machine.

Prerequisites

An agent for the relevant hypervisor is installed in your environment. For example, recovery to a VMware ESXi virtual machine requires Agent for VMware that is installed and registered in the Cyber Protect console.

To recover a virtual machine as a virtual machine

The procedures are listed according to the type of the target virtual machine.

VMware ESXi
Azure
Hyper-V
Virtuozzo
Virtuozzo Hybrid Infrastructure
Scale Computing HC3
oVirt
Nutanix
Proxmox

In the Cyber Protect console, do one of the following:

On the Devices tab, select a backed-up machine, click Recovery, and then select a backup (recovery point).
On the Backup storage tab, select a backup archive, and then select a backup (recovery point).

Click Recover > Entire machine.

The original virtual machine is selected as a target machine.

[If prompted] Specify the credentials to access the backup storage, and then click OK.

To change the target machine:

Click Target machine.
[If multiple hypervisors are available] Select VMware ESXi.

[To perform recovery to a new machine]

Select New machine.
Select a host.
In Machine name, specify a name for the new machine.
Click OK.

[To perform recovery to an existing machine]

Select Existing machine.
Select the target machine.
Click OK.
[If prompted] Specify the credentials to access the backup storage, and then click OK.

[When recovering to a new machine] Configure additional options:

To change the storage for the virtual machine, click Datastore, and then select a datastore.

To change the disk mapping or exclude some of the backed-up disks from the recovery, click Disk mapping.

Configure the disk mapping or select the disks that you want to recover.
Click Done.

To change the memory size, the number of virtual processors, or the network connections of the target machine, click VM settings.

Configure the settings.
Click OK.
Click Start recovery
[When recovering to an existing machine] To confirm that you want to overwrite the target machine, click Start recovery.

You can check the recovery progress in the Cyber Protect console, on the Activities tab.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.