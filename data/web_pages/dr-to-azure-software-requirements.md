# Software requirements for Disaster Recovery to Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Software requirements for Disaster Recovery to Microsoft Azure
Software requirements for Disaster Recovery to Microsoft Azure
Supported operating systems

Protection with a recovery server in Microsoft Azure has been tested for the following operating systems:

Ubuntu 20.x, 21.x, 22.10, 23.04
Debian 10.x, 11.x
Red Hat Enterprise Linux 8.x, 9.x
Windows Server 2008 R2
Windows Server 2012/2012 R2
Windows Server 2016 – all installation options, except for Nano Server
Windows Server 2019 – all installation options, except for Nano Server
Windows Server 2022 – all installation options, except for Nano Server

Windows Server 2025 – all installation options, except for Nano Server

Windows 10

Windows 11

The software may work with other Windows operating systems and Linux distributions, but this is not guaranteed.

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

Linux workloads that have agentless backups from a guest OS and have volumes with the Logical Volume Manager (LVM) configurations are supported.

Windows workloads that have agentless backups from a guest OS and have dynamic disks (LDM) configurations are supported.

The software might work with other virtualization platforms and versions, but this is not guaranteed.

Limitations

The following platforms and configurations are not supported in Disaster Recovery to Microsoft Azure:

Unsupported platforms:

Agents for Virtuozzo
macOS

Unsupported configurations:

Microsoft Windows

Active Directory service with FRS replication is not supported.
Removable media without either GPT or MBR formatting (so-called "superfloppy") are not supported.

Linux

File systems without a partition table.

Linux workloads that are backed up with an agent from a guest OS and have volumes with the following advanced Logical Volume Manager (LVM) configurations: Striped volumes, Mirrored volumes, RAID 0, RAID 4, RAID 5, RAID 6, or RAID 10 volumes.

Workloads with multiple operating systems installed are not supported.

Unsupported tenant modes:

Disaster recovery is not available when Compliance mode is enabled for the tenant.

Unsupported backup types:

Continuous data protection (CDP) recovery points are incompatible.

If you create a recovery server from a backup having a CDP recovery point, then during the failback or creating backup of a recovery server, you will loose the data contained in the CDP recovery point.

Forensic backups cannot be used for creating recovery servers.

Cloud servers are not encrypted.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.