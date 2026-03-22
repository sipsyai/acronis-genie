# Cross-platform recovery

Managing the backup and recovery of workloads and files > Recovery > Cross-platform recovery
Cross-platform recovery

You can recover a disk-level backup to a physical machine or to a virtual machine. For example, a disk-level backup is an Entire machine backup or a Disk/volumes backup that contains the system disk and the boot disk.

Cross-platform recovery (machine migration) is performed in the following cases:

When you recover a backup of a physical machine to a virtual machine.
When you recover a backup of a virtual machine to a physical machine.

When you recover a backup of a virtual machine to a virtual machine on a different type of hypervisor.

If a virtual machine is backed up by a protection agent installed inside the guest operating system, the backup is treated as a physical machine backup.

The following tables summarize the available options for cross-platform recovery according to the backed-up workload.

Physical machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Broadcom (VMware) ESXi virtual machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Microsoft Microsoft Azure virtual machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Microsoft Hyper-V virtual machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Virtuozzo Hybrid Server virtual machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Virtuozzo Hybrid Server container
Target workload	Supported
Physical machine	No
Broadcom (VMware) ESXi virtual machine	No
Microsoft Azure virtual machine	No
Microsoft Hyper-V virtual machine	No
Virtuozzo Hybrid Server virtual machine	No
Virtuozzo Hybrid Server container	Yes
Virtuozzo Hybrid Infrastructure virtual machine	No
Scale Computing HyperCore virtual machine	No
RHV/oVirt virtual machine	No
Nutanix virtual machine	No
Proxmox virtual machine	No
Proxmox container	No
Virtuozzo Hybrid Infrastructure virtual machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Scale Computing HyperCore virtual machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Red Hat Virtualization/oVirt virtual machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Nutanix virtual machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Proxmox virtual machine
Target workload	Supported
Physical machine	Yes
Broadcom (VMware) ESXi virtual machine	Yes
Microsoft Azure virtual machine	Yes
Microsoft Hyper-V virtual machine	Yes*
Virtuozzo Hybrid Server virtual machine	Yes
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	Yes
Scale Computing HyperCore virtual machine	Yes
RHV/oVirt virtual machine	Yes
Nutanix virtual machine	Yes
Proxmox virtual machine	Yes
Proxmox container	No
Proxmox container
Target workload	Supported
Physical machine	No
Broadcom (VMware) ESXi virtual machine	No
Microsoft Azure virtual machine	No
Microsoft Hyper-V virtual machine	No
Virtuozzo Hybrid Server virtual machine	No
Virtuozzo Hybrid Server container	No
Virtuozzo Hybrid Infrastructure virtual machine	No
Scale Computing HyperCore virtual machine	No
RHV/oVirt virtual machine	No
Nutanix virtual machine	No
Proxmox virtual machine	No
Proxmox container	Yes
The Secure Boot setting is not backed up. If Secure Boot is enabled on the original machine, the virtual machine recovered as a new machine will not boot. To start the recovered machine, disable Secure Boot in the VM console after recovery.
* EFI-based machines are recovered as Generation 2 virtual machines.
* You cannot recover macOS virtual machines to Hyper-V hosts because Hyper-V does not support macOS. You can recover macOS virtual machines to VMware hosts that are installed on Mac hardware.
Cross-platform recovery via bootable media

You can perform a cross-platform recovery by using bootable media.

We recommend that you use bootable media instead of the Cyber Protect console in the following cases:

Performing a migration that is not natively supported.

For example, use bootable media to recover a physical machine or a non-Virtuozzo Hybrid Server virtual machine as a Virtuozzo Hybrid Server virtual machine on a Virtuozzo host.

Performing migration of a Linux machine that contains logical volumes (LVM).

Use Agent for Linux or bootable media to create the backup, and then use bootable media to recover the backup.

Providing drivers for specific hardware that is critical for the system bootability.

Build bootable media that can use the required drivers. For more information, see Bootable Media Builder.

See also
Recovery of physical machines
Recovery of virtual machines
Recovering disks by using bootable media

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.