# Supported virtualization platforms

Managing the backup and recovery of workloads and files > Supported operating systems and environments for backup and recovery > Supported virtualization platforms
Supported virtualization platforms

The following tables summarize how various virtualization platforms are supported.

For more information about the differences between the agent-based and agentless backup, see Agent-based and agentless backup.

If you use a virtualization platform or version that is not listed below, the Agent-based backup (Backup from inside a guest OS) method should still work correctly in all required scenarios. If you encounter issues with the agent-based backup, contact the Support team for further investigation.

VMware (Broadcom)
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)




VMware vSphere versions: 4.1, 5.0, 5.1, 5.5, 6.0, 6.5, 6.7, 7.0, 8.0

VMware vSphere editions:

VMware vSphere Essentials*

VMware vSphere Essentials Plus*

VMware vSphere Standard*

VMware vSphere Advanced

VMware vSphere Enterprise

VMware vSphere Enterprise Plus



Supported

Devices > Add > Virtualization hosts > Broadcom (VMware) ESXi > Agent for installation in Windows

or

Devices > Add > Virtualization hosts > Broadcom (VMware) ESXi > Virtual appliance (OVF)



Supported

Devices > Add > Workstations or Servers > Windows or Linux


VMware vSphere Hypervisor (Free ESXi)**	Not supported

Supported

Devices > Add > Workstations or Servers > Windows or Linux




VMware Server (VMware Virtual server)

VMware Workstation

VMware ACE

VMware Player

Not supported

Supported

Devices > Add > Workstations or Servers > Windows or Linux

* In these editions, the HotAdd transport for virtual disks is supported on vSphere 5.0 and later. On version 4.1, backups may run slower.

** Backup at a hypervisor level is not supported for vSphere Hypervisor because this product restricts access to Remote Command Line Interface (RCLI) to read-only mode. The agent works during the vSphere Hypervisor evaluation period while no serial key is entered. Once you enter a serial key, the agent stops functioning.

Cyber Protect Cloud officially supports any update within the supported major vSphere version.

For example, vSphere 8.0 support includes support for any update within this version, unless stated otherwise. That is, vSphere 8.0 Update 1 is also supported along with originally released vSphere 8.0.

Support for specific VMware vSphere version means that vSAN of the corresponding version is also supported. For example, support for vSphere 8.0 means that vSAN 8.0 is also supported.

Limitations
Fault tolerant machines

Agent for VMware backs up a fault tolerant machine only if fault tolerance was enabled in VMware vSphere 6.0 and later. If you upgraded from an earlier vSphere version, it is enough to disable and enable fault tolerance for each machine. If you are using an earlier vSphere version, install an agent in the guest operating system.

Independent disks and RDM

Agent for VMware does not back up Raw Device Mapping (RDM) disks in physical compatibility mode or independent disks. The agent skips these disks and adds warnings to the log. You can avoid the warnings by excluding independent disks and RDMs in physical compatibility mode from the protection plan. If you want to back up these disks or data on these disks, install an agent in the guest operating system.

In-guest iSCSI connection

Agent for VMware does not back up LUN volumes connected by an iSCSI initiator that works within the guest operating system. Because the ESXi hypervisor is not aware of such volumes, the volumes are not included in hypervisor-level snapshots and are omitted from a backup without a warning. If you want to back up these volumes or data on these volumes, install an agent in the guest operating system.

Encrypted virtual machines (introduced in VMware vSphere 6.5)
Encrypted virtual machines are backed up in an unencrypted state. If encryption is critical to you, enable encryption of backups when creating a protection plan.
Recovered virtual machines are always unencrypted. You can manually enable encryption after the recovery is complete.
If you back up encrypted virtual machines, we recommend that you also encrypt the virtual machine where Agent for VMware is running. Otherwise, operations with encrypted machines may be slower than expected. Apply the VM Encryption Policy to the agent's machine by using vSphere Web Client.
Encrypted virtual machines will be backed up via LAN, even if you configure the SAN transport mode for the agent. The agent will fall back on the NBD transport because VMware does not support SAN transport for backing up encrypted virtual disks.

Secure Boot

VMware virtual machines: (introduced in VMware vSphere 6.5) Secure Boot is disabled after a virtual machine is recovered as a new virtual machine. You can manually enable this option after the recovery is complete. This limitation applies to VMware.
Hyper-V virtual machines: For all Generation 2 virtual machines, Secure Boot is disabled after the machine is recovered to both new virtual machine or an existing virtual machine.

ESXi configuration backup is not supported for VMware vSphere 7.0 or later.

Virtual machines with empty Instance UUID do not appear in the Cyber Protect console

VMware virtual machines with an empty Instance UUID vSphere property (vc.uuid) are not listed in the Cyber Protect console. For more information on how to resolve this issue, see this knowledge base article.

Network settings on the protection agent

A backup of a VMware virtual machine can fail if the protection agent cannot resolve the name of the ESXi host registered in vCenter to an IP address, even if the vCenter host name can be resolved. The following error is shown: "You do not have access rights to this file."

To resolve the issue, edit the network settings of the protection agent, by configuring the DNS or modifying the /etc/hosts file. To verify the fix, on the machine with the protection agent, run the following command:

ping <ESXi host name>

Supported operations for machines with logical volumes

Backup and recovery of workloads with logical volumes, such as LDM in Windows (dynamic disks) and LVM in Linux, are supported with some limitations. For more information about the limitations, see Supported operations with logical volumes.

Public clouds
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)


Amazon EC2 instances	Not supported

Supported

Devices > Add > Workstations or Servers > Windows or Linux


Microsoft Azure virtual machines

Supported

Devices > Add > Microsoft Azure virtual machines



Supported

Devices > Add > Workstations or Servers > Windows or Linux

Microsoft

Hyper-V virtual machines running on a hyper-converged cluster with Storage Spaces Direct (S2D) are supported. Storage Spaces Direct is also supported as a backup storage.

Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)




Windows Server 2008 (x64) with Hyper-V

Windows Server 2008 R2 with Hyper-V

Microsoft Hyper-V Server 2008/2008 R2

Windows Server 2012/2012 R2 with Hyper-V

Microsoft Hyper-V Server 2012/2012 R2

Windows 8, 8.1 (x64) with Hyper-V

Windows 10 with Hyper-V

Windows 11 with Hyper-V

Windows Server 2016 with Hyper-V – all installation options, except for Nano Server

Microsoft Hyper-V Server 2016

Windows Server 2019 with Hyper-V – all installation options, except for Nano Server

Microsoft Hyper-V Server 2019

Windows Server 2022 with Hyper-V – all installation options, except for Nano Server

Windows Server 2025 with Hyper-V – all installation options, except for Nano Server



Supported

Devices > Add > Virtualization hosts > Microsoft Hyper-V



Supported

Devices > Add > Workstations or Servers > Windows or Linux




Microsoft Virtual PC 2004, 2007

Windows Virtual PC

Not supported

Supported

Devices > Add > Workstations or Servers > Windows or Linux


Microsoft Virtual Server 2005	Not supported

Supported

Devices > Add > Workstations or Servers > Windows or Linux

Hyper-V virtual machines running on a hyper-converged cluster with Storage Spaces Direct (S2D) are supported. Storage Spaces Direct is also supported as a backup storage.
Limitations
Pass-through disks

Agent for Hyper-V does not back up pass-through disks. During backup, the agent skips these disks and adds warnings to the log. You can avoid the warnings by excluding pass-through disks from the protection plan. If you want to back up these disks or data on these disks, install an agent in the guest operating system.

Hyper-V guest clustering

Agent for Hyper-V does not support backup of Hyper-V virtual machines that are nodes of a Windows Server Failover Cluster. A VSS snapshot at the host level can even temporarily disconnect the external quorum disk from the cluster. If you want to back up these machines, install agents in the guest operating systems.

In-guest iSCSI connection

Agent for Hyper-V does not back up LUN volumes connected by an iSCSI initiator that works within the guest operating system. Because the Hyper-V hypervisor is not aware of such volumes, the volumes are not included in hypervisor-level snapshots and are omitted from a backup without a warning. If you want to back up these volumes or data on these volumes, install an agent in the guest operating system.

Dependency on the Microsoft WMI subsystem

Agentless backups of Hyper-V virtual machines depend on the Microsoft WMI subsystem, and in particular on the Msvm_VirtualSystemManagementService class. If the WMI queries fail, the backups will also fail. For more information about the Msvm_VirtualSystemManagementService class, see the Microsoft documentation.

Virtual machines with PMEM disks

Backup of Hyper-V virtual machines that have persistent memory (PMEM) disks is not supported.

Cross-platform recovery

If Agent for Hyper-V recovers a backup, which is created by another agent, as a new Hyper-V virtual machine, the resulting machine is Generation 1.

Secure Boot

To guarantee the booting up of Generation 2 Hyper-V virtual machines that are recovered, Secure Boot is disabled. You can re-enable it manually in the Hyper-V management tool. For more information about Secure Boot and Generation 2 virtual machines, see the Microsoft documentation.

Crash-consistent backups of Linux virtual machines

Backups of Linux virtual machines running on a Hyper-V 2019 host fail over to crash-consistent snapshots, due to a Microsoft limitation (inability to create production checkpoints for Linux virtual machines). To avoid warnings during a backup, disable the VSS for Virtual Machines backup option in the protection plan.

Running a virtual machine from a backup

Running a virtual machine from a backup on a Hyper-V host fails if the backup is located on the same volume as the path selected for the mounted VM disks. To resolve the issue, select a different volume for the path of the mounted VM disks. The space will be used only for changes generated inside the mounted virtual machine, and will not take the entire size of the virtual disk.

Supported operations for machines with logical volumes

Backup and recovery of workloads with logical volumes, such as LDM in Windows (dynamic disks) and LVM in Linux, are supported with some limitations. For more information about the limitations, see Supported operations with logical volumes.

Scale Computing
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)


Scale Computing HyperCore 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4

Supported

Devices > Add > Virtualization hosts > Scale Computing HyperCore



Supported

Devices > Add > Workstations or Servers > Windows or Linux

Limitations

Backup of replicated virtual machines

Virtual machines that are replicated by the native Scale Computing VM replication feature cannot be backed up.

Supported operations for machines with logical volumes

Backup and recovery of workloads with logical volumes, such as LDM in Windows (dynamic disks) and LVM in Linux, are supported with some limitations. For more information about the limitations, see Supported operations with logical volumes.

Proxmox VE
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)


Proxmox VE 7.x, 8, and 8.1

Not supported



Supported only for fully virtualized (HVM) guests. Paravirtualized (PV) guests are not supported.

Devices > Add > Workstations or Servers > Windows or Linux


Proxmox VE 8.2, 8.3, 8.4, 9.0

Supported

Devices > Add > Virtualization hosts > Proxmox VE



Supported only for fully virtualized (aka HVM) guests. Paravirtualized (aka PV) guests are not supported.

Devices > Add > Workstations or Servers > Windows or Linux

Citrix Hypervisor/XenServer
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)


Citrix Hypervisor/XenServer 4.1.5, 5.5, 5.6, 6.0, 6.1, 6.2, 6.5, 7.0, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 8.0, 8.1, 8.2	Not supported

Supported only for fully virtualized (aka HVM) guests. Paravirtualized (aka PV) guests are not supported.

Devices > Add > Virtualization hosts > Citrix Hypervisor/XenServer > Windows or Linux

Red Hat and Linux
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)




Red Hat Enterprise Virtualization (RHEV) 2.2, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6

Red Hat Virtualization (RHV) 4.0, 4.1

Not supported

Supported

Devices > Add > Workstations or Servers > Windows or Linux




Red Hat Virtualization (managed by oVirt) 4.2, 4.3, 4.4, 4.5



Supported

Devices > Add > Virtualization hosts > Red Hat Virtualization (oVirt)



Supported

Devices > Add > Workstations or Servers > Windows or Linux


Kernel-based Virtual Machines (KVM)	Not supported

Supported

Devices > Add > KVM > Windows or Linux


Kernel-based Virtual Machines (KVM) managed by oVirt 4.3 running on Red Hat Enterprise Linux 7.6, 7.7 or CentOS 7.6, 7.7

Supported

Devices > Add > Virtualization hosts > Red Hat Virtualization (oVirt)



Supported

Devices > Add > Workstations or Servers > Windows or Linux


Kernel-based Virtual Machines (KVM) managed by oVirt 4.4 running on Red Hat Enterprise Linux 8.x or CentOS Stream 8.x

Supported

Devices > Add > Virtualization hosts> Red Hat Virtualization (oVirt)



Supported

Devices > Add > Workstations or Servers > Windows or Linux


Kernel-based Virtual Machines (KVM) managed by oVirt 4.5 running on Red Hat Enterprise Linux 8.x or CentOS Stream 8.x

Supported

Devices > Add > Virtualization hosts > Red Hat Virtualization (oVirt)



Supported

Devices > Add > Workstations or Servers > Windows or Linux

Limitations

Supported operations for machines with logical volumes

Backup and recovery of workloads with logical volumes, such as LDM in Windows (dynamic disks) and LVM in Linux, are supported with some limitations. For more information about the limitations, see Supported operations with logical volumes.

Parallels
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)


Parallels Workstation	Not supported

Supported

Devices > Add > Workstations or Servers > Windows or Linux


Parallels Server 4 Bare Metal	Not supported

Supported

Devices > Add > Workstations or Servers > Windows or Linux

Oracle
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)


Oracle Linux Virtualization Manager (based on oVirt)* 4.3

Supported

Devices > Add > Virtualization hosts > Oracle LVM (oVirt)



Supported

Devices > Add > Workstations or Servers > Windows or Linux


Oracle VM Server 3.0, 3.3, 3.4	Not supported

Supported only for fully virtualized (aka HVM) guests. Paravirtualized (aka PV) guests are not supported.

Devices > Add > Workstations or Servers > Windows or Linux


Oracle VM VirtualBox 4.x	Not supported

Supported

Devices > Add > Workstations or Servers > Windows or Linux

*Oracle Linux Virtualization Manager is supported by Agent for oVirt.

Limitations

Supported operations for machines with logical volumes

Backup and recovery of workloads with logical volumes, such as LDM in Windows (dynamic disks) and LVM in Linux, are supported with some limitations. For more information about the limitations, see Supported operations with logical volumes.

Nutanix
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)



Nutanix Acropolis Operating System (AOS) 6.5, 6.6, 6.7, 6.8, 6.10

Supported

Devices > Add > Virtualization hosts > Nutanix AHV



Supported

Devices > Add > Virtualization hosts > Nutanix AHV > Windows or Linux

Virtuozzo Hybrid Server
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)


Virtuozzo 6.0.10, 6.0.11, 6.0.12

Supported

Devices > Add > Virtualization hosts > Virtuozzo



Supported for virtual machines only. Containers are not supported.

Devices > Add > Workstations or Servers > Windows or Linux


Virtuozzo 7.0.13, 7.0.14

Supported for ploop containers only. Virtual machines are not supported.

Devices > Add > Virtualization hosts > Virtuozzo



Supported for virtual machines only. Containers are not supported.

Devices > Add > Workstations or Servers > Windows or Linux


Virtuozzo Hybrid Server 7.5

Supported

Devices > Add > Virtualization hosts > Virtuozzo



Supported for virtual machines only. Containers are not supported.

Devices > Add > Workstations or Servers > Windows or Linux

Limitations

Supported operations for machines with logical volumes

Backup and recovery of workloads with logical volumes, such as LDM in Windows (dynamic disks) and LVM in Linux, are supported with some limitations. For more information about the limitations, see Supported operations with logical volumes.

Virtuozzo Hybrid Infrastructure
Platform

Agentless backup

(Backup at the hypervisor level)



Agent-based backup

(Backup from inside a guest OS)


Virtuozzo Hybrid Infrastructure 3.5, 4.5, 4.6, 4.7, 5.0, 5.1, 5.2, 5.3, 5.4, 6.0, 6.1, 6.2, 6.3, 7.0

Supported

Devices > Add > Virtualization hosts > Virtuozzo Hybrid infrastructure



Supported

Devices > Add > Workstations or Servers > Windows or Linux

Limitations

Agentless backup of VMs with disks on an external iSCSI storage

You cannot back up VMs from Virtuozzo Hybrid Infrastructure, if VM disks are placed on external iSCSI volumes (attached to the VHI cluster).

Supported operations for machines with logical volumes

Backup and recovery of workloads with logical volumes, such as LDM in Windows (dynamic disks) and LVM in Linux, are supported with some limitations. For more information about the limitations, see Supported operations with logical volumes.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.