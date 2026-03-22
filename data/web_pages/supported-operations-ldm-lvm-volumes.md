# Supported operations with logical volumes

Managing the backup and recovery of workloads and files > Supported operating systems and environments for backup and recovery > Supported operations with logical volumes
Supported operations with logical volumes

Backup and recovery of workloads with logical volumes, such as LDM in Windows (dynamic disks) and LVM in Linux, are supported with the following limitations.

Backup

Agent-based backup is a backup created by a protection agent that is installed on the workload or by a bootable media.

Agentless backup is available only for virtual machines. The agentless backup is performed on the hypervisor level by agent that can back up and recover all virtual machines in the environment. No individual agents are installed on the protected virtual machines.

For more information about the differences between agent-based and agentless backup, see Agent-based and agentless backup.

Agent-based backup	Agentless backup

Logical volumes are backed on per volume basis.
File filters (Inclusions/Exclusions) are supported.


When a logical volume is detected on a disk, the disk is backed up in the sector-by-sector (RAW) mode. The partition structure of the disk is not analyzed and no volume images are stored separately.

Individual LDM or LVM volumes cannot be selected as backup source – neither by direct selection nor by using policy rules. Only Entire machine is available in the What to back up section of a protection plan.

File filters (Inclusions/Exclusions) are not supported. Any configured inclusions or exclusions will be ignored.

Recovery

Agent-based recovery is a recovery performed by an agent that is installed on the workload or by a bootable media.

Agentless recovery supports only virtual machines as targets. The agentless recovery is a performed on the hypervisor level by agent that can back up and recover all virtual machines in the environment. You do not have to create manually a target machine to which the backup is recovered.

From agent-based backup	From agentless backup
Agent-based recovery

Per-volume recovery is available.

File and folder recovery is available.

You can recover a Linux machine with LVM volumes from an agent-based backup in public cloud to a new machine by using backup replication and bootable media.

First, replicate the backup from the public cloud location to a network share or local disk. Then, use a Linux-based bootable media (with Linux-like volume representation) to recreate the LVM structure and recover the machine.



Per-volume recovery is not available.

File and folder recovery is available.


Agentless recovery

Machine migration (P2V, V2P, and V2V) is not supported. To recover data from an agent-based backup, use bootable media.

The Run as VM operation is not supported.

File and folder recovery is available.



Per-volume recovery is not available.

Entire machine recovery is available.

File and folder recovery is available.

The Run as VM operation is supported. To make the virtual machine bootable, you might need to change the boot order. For more information, see this knowledge base article.

Conversion to the following types of virtual machine is supported:

VMware ESXi

Microsoft Hyper-V

Scale Computing HC3

See also
Agent-based and agentless backup
Supported operating systems and environments for backup and recovery
Cross-platform recovery

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.