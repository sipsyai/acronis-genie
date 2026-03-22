# Software requirements for Disaster Recovery to Cyber Protect Cloud

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Software requirements for Disaster Recovery to Cyber Protect Cloud
Software requirements for Disaster Recovery to Cyber Protect Cloud
Supported operating systems

Protection with a recovery server has been tested for the following operating systems:

CentOS 6.6, 7.x, 8.x
Debian 9.x, 10.x, 11.x
Red Hat Enterprise Linux 6.6, 7.x, 8.x
Ubuntu 18.04, 20.x, 21.x, 22.04, 22.10
Oracle Linux 7.3 and 7.9 with Unbreakable Enterprise Kernel
Windows Server 2008 R2
Windows Server 2012/2012 R2
Windows Server 2016 – all installation options, except for Nano Server
Windows Server 2019 – all installation options, except for Nano Server

Windows Server 2022 – all installation options, except for Nano Server

AlmaLinux 8.x, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5

Rocky Linux 9.x, 8.x

SUSE Linux Enterprise Server 15

The software may work with other Windows operating systems and Linux distributions, but this is not guaranteed.

Protection with a recovery server has been tested for Microsoft Azure VM with the following operating systems.

Windows Server 2008 R2
Windows Server 2012/2012 R2
Windows Server 2016 – all installation options, except for Nano Server
Windows Server 2019 – all installation options, except for Nano Server

Windows Server 2022 – all installation options, except for Nano Server

Ubuntu Server 20.04 LTS - Gen2 (Canonical). For more information about accessing the recovery server console, see this knowledge base article.

Supported virtualization platforms

Protection of virtual machines with a recovery server has been tested for the following virtualization platforms:

VMware ESXi 5.1, 5.5, 6.0, 6.5, 6.7, 7.0
Windows Server 2008 R2 with Hyper-V
Windows Server 2012/2012 R2 with Hyper-V
Windows Server 2016 with Hyper-V – all installation options, except for Nano Server
Windows Server 2019 with Hyper-V – all installation options, except for Nano Server
Windows Server 2022 with Hyper-V – all installation options, except for Nano Server
Microsoft Hyper-V Server 2012/2012 R2
Microsoft Hyper-V Server 2016
Kernel-based Virtual Machines (KVM) — fully virtualized guests (HVM) only. Paravirtualized guests (PV) are not supported.
Red Hat Enterprise Virtualization (RHEV) 3.6
Red Hat Virtualization (RHV) 4.0
Citrix XenServer: 6.5, 7.0, 7.1, 7.2
Nutanix Acropolis Hypervisor (AHV) with Nutanix Acropolis Operating System (AOS): 6.5, 6.6, 6.7, 6.8, 6.10
Proxmox VE 8.2, 8.3, 8.4, 9.0
Scale Computing HyperCore 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4
Virtuozzo Infrastructure 3.5, 4.0, 4.5, 4.6, 4.7, 5.0, 5.1, 5.2, 5.3, 5.4, 6.0, 6.1, 6.2, 6.3

The VPN appliance has been tested for the following virtualization platforms:

VMware ESXi 5.1, 5.5, 6.0, 6.5, 6.7
Windows Server 2008 R2 with Hyper-V
Windows Server 2012/2012 R2 with Hyper-V
Windows Server 2016 with Hyper-V – all installation options, except for Nano Server
Windows Server 2019 with Hyper-V – all installation options, except for Nano Server
Windows Server 2022 with Hyper-V – all installation options, except for Nano Server
Microsoft Hyper-V Server 2012/2012 R2
Microsoft Hyper-V Server 2016

Linux workloads that have agentless backups from a guest OS and have volumes with the Logical Volume Manager (LVM) configurations are supported.

Windows workloads that have agentless backups from a guest OS and have dynamic disks (LDM) configurations are supported.

The software might work with other virtualization platforms and versions, but this is not guaranteed.

Limitations

The following platforms and configurations are not supported in Disaster Recovery:

Unsupported platforms:

Agents for Virtuozzo
macOS

Windows desktop operating systems are not supported due to Microsoft product terms.

Windows Server Azure Edition

Azure Edition is a special version of Windows Server that was built specifically to run either as an Azure IaaS virtual machine (VM) in Azure or as a VM on an Azure Stack HCI cluster. Unlike the Standard and Datacenter editions, Azure Edition is not licensed to run on bare metal hardware, Windows client Hyper-V, Windows Server Hyper-V, third-party hypervisors, or in third-party clouds.

Unsupported configurations:

Microsoft Windows

Windows desktop operating systems are not supported (due to Microsoft product terms).
Active Directory service with FRS replication is not supported.
Removable media without either GPT or MBR formatting (so-called "superfloppy") are not supported.

Linux

File systems without a partition table.

Linux workloads that are backed up with an agent from a guest OS and have volumes with the following advanced Logical Volume Manager (LVM) configurations: Striped volumes, Mirrored volumes, RAID 0, RAID 4, RAID 5, RAID 6, or RAID 10 volumes.

For SUSE Linux Enterprise Server 15, configurations with Btrfs are not supported.

Workloads with multiple operating systems installed are not supported.

Unsupported tenant modes:

Disaster recovery is not available when Compliance mode is enabled for the tenant.

Unsupported backup types:

Continuous data protection (CDP) recovery points are incompatible.

If you create a recovery server from a backup having a CDP recovery point, then during the failback or creating backup of a recovery server, you will loose the data contained in the CDP recovery point.

Forensic backups cannot be used for creating recovery servers.

A recovery server has one network interface. If the original machine has several network interfaces, only one is emulated.

Cloud servers are not encrypted.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.