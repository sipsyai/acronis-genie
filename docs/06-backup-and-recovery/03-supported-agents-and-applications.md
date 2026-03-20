---
title: "Supported agents and application versions"
section: "Managing the backup and recovery of workloads and files"
subsection: "Supported operating systems and environments for backup and recovery"
page_range: "487-495"
tags: ["agents", "VMware", "Hyper-V", "Virtuozzo", "Scale-Computing", "oVirt", "Synology", "Azure", "Nutanix", "SQL-Server", "Exchange", "Oracle", "MySQL", "MariaDB", "SAP-HANA", "SharePoint"]
acronis_version: "26.02"
---

# Supported agents and application versions

## Agent for Microsoft 365

FIPS-compliant mode is supported on 64-bit operating systems.

Supported on the same Windows versions as Agent for Windows and Agent for Windows (Legacy), with the following limitation:
- All Windows versions must be x64 only (except Windows 8/8.1 which also supports x86).
- Windows Storage Server versions must be x64 only.

## Agent for Oracle

Delivered as part of Agent for Windows, Agent for Windows (Legacy), and Agent for Linux (64-bit). FIPS-compliant mode is supported on 64-bit operating systems.

- Windows Server 2008R2, 2012R2 — Standard, Enterprise, Datacenter, and Web editions (x86, x64)
- Linux — any kernel and distribution supported by Agent for Linux

## Agent for MySQL/MariaDB

Delivered as part of Agent for Linux (64-bit). FIPS-compliant mode is supported.

- Linux — any kernel and distribution supported by Agent for Linux

## Agent for Exchange (for mailbox backup)

FIPS-compliant mode is supported on 64-bit operating systems.

- Windows Server 2008 — Standard, Enterprise, Datacenter, Foundation, and Web editions (x86, x64)
- Windows Small Business Server 2008
- Windows 7 — all editions
- Windows Server 2008 R2 — Standard, Enterprise, Datacenter, Foundation, and Web editions
- Windows MultiPoint Server 2010/2011/2012
- Windows Small Business Server 2011 — all editions
- Windows 8/8.1 — all editions (x86, x64), except for the Windows RT editions
- Windows Server 2012/2012 R2 — all editions
- Windows Storage Server 2008/2008 R2/2012/2012 R2
- Windows 10 — Home, Pro, Education, and Enterprise editions
- Windows Server 2016/2019 — all installation options, except for Nano Server
- Windows 11 — all editions
- Windows Server 2022 — all installation options, except for Nano Server

## Agent for VMware (Virtual Appliance)

Delivered as a virtual appliance that runs on an ESXi host. FIPS-compliant mode is supported.

- VMware ESXi 4.1, 5.0, 5.1, 5.5, 6.0, 6.5, 6.7, 7.0, 8.0
- In FIPS-compliant mode, only VMware ESXi 8.0 is supported.

## Agent for VMware (Windows)

Delivered as part of Agent for Windows and Agent for Windows (Legacy). FIPS-compliant mode is supported on 64-bit operating systems.

Supported on the same Windows versions as Agent for Windows and Agent for Windows (Legacy) with the following limitations:
- 32-bit operating systems are not supported.
- Windows XP, Windows Server 2003/2003 R2, and Windows Small Business Server 2003/2003 R2 are not supported.
- In FIPS-compliant mode, only VMware ESXi 8.0 is supported.

## Agent for Hyper-V

FIPS-compliant mode is supported on 64-bit operating systems.

- Windows Server 2008 (x64 only) with Hyper-V role, including Server Core installation mode
- Windows Server 2008 R2 with Hyper-V role, including Server Core installation mode
- Microsoft Hyper-V Server 2008/2008 R2
- Windows Server 2012/2012 R2 with Hyper-V role, including Server Core installation mode
- Microsoft Hyper-V Server 2012/2012 R2
- Windows 8, 8.1 (x64 only) with Hyper-V
- Windows 10 — Pro, Education, and Enterprise editions with Hyper-V
- Windows 11 — Pro, Education, and Enterprise editions with Hyper-V
- Windows Server 2016 with Hyper-V role — all installation options, except for Nano Server
- Microsoft Hyper-V Server 2016
- Windows Server 2019 with Hyper-V role — all installation options, except for Nano Server
- Microsoft Hyper-V Server 2019
- Windows Server 2022 — all installation options, except for Nano Server
- Windows Server 2025 — all installation options, except for Nano Server

## Agent for Virtuozzo

Delivered as part of Agent for Linux (64-bit). FIPS-compliant mode is supported.

- Virtuozzo 6.0.10, 6.0.11, 6.0.12, 7.0.13, 7.0.14
- Virtuozzo Hybrid Server 7.5

## Agent for Virtuozzo Hybrid Infrastructure

Delivered as a virtual appliance. FIPS-compliant mode is supported.

- Virtuozzo Hybrid Infrastructure 3.5, 4.0, 4.5, 4.6, 4.7, 5.0, 5.1, 5.2, 5.3, 5.4, 6.0, 6.1, 6.2, 6.3

## Agent for Scale Computing HC3

Delivered as a virtual appliance. FIPS-compliant mode is supported.

- Scale Computing HyperCore 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4

## Agent for oVirt

Delivered as a virtual appliance on a KVM hypervisor host managed by oVirt. FIPS-compliant mode is supported.

- Red Hat Virtualization 4.2, 4.3, 4.4, 4.5

## Agent for Synology

Delivered as a virtual appliance on a Synology NAS.

- DiskStation Manager 6.2.x, 7.x
- Only NAS devices with x86_64 processors are supported. ARM processors are not supported.

## Agent for Azure

Delivered as a virtual appliance in your Microsoft Azure Subscription.

## Agent for Nutanix

Delivered as a virtual appliance in a Nutanix AHV cluster.

- Nutanix Acropolis Operating System (AOS) 6.5, 6.6, 6.7, 6.8, 6.10

## Cyber Protect Monitor

- With Agent for Windows: Windows 10 version 1809 and later; Windows Server 2019 and later
- With Agent for Windows (Legacy): Windows 7 and later; Windows Server 2008 R2 and later
- With Agent for Mac: All macOS versions supported by Agent for Mac, except macOS 10.x and macOS 11.x

---

# Supported application versions

## Microsoft SQL Server

- Microsoft SQL Server 2022, 2019, 2017, 2016, 2014, 2012, 2008 R2, 2008, 2005
- The SQL Server Express editions are supported as well.

> **Note:** Microsoft SQL backup is supported only for databases running on NTFS, REFS, and FAT32 file systems. ExFat is not supported.

## Microsoft Exchange Server

- Microsoft Exchange Server Subscription Edition (SE)
- Microsoft Exchange Server 2019 — all editions
- Microsoft Exchange Server 2016 — all editions
- Microsoft Exchange Server 2013 — all editions, Cumulative Update 1 (CU1) and later
- Microsoft Exchange Server 2010 — all editions, all service packs. Mailbox backup and granular recovery from database backups are supported starting with Service Pack 1 (SP1).
- Microsoft Exchange Server 2007 — all editions, all service packs. Mailbox backup and granular recovery from database backups are not supported.

## Microsoft SharePoint

- Microsoft SharePoint 2013
- Microsoft SharePoint Server 2010 SP1
- Microsoft SharePoint Foundation 2010 SP1
- Microsoft Office SharePoint Server 2007 SP2*
- Microsoft Windows SharePoint Services 3.0 SP2*

*SharePoint Explorer with these versions requires a SharePoint recovery farm. The backups or databases must originate from the same SharePoint version.

## Oracle Database

- Oracle Database version 11g, all editions
- Oracle Database version 12c, all editions
- Oracle Database version 19c, all editions
- Oracle Database version 21c, all editions

Only single-instance configurations are supported.

## SAP HANA

- HANA 2.0 SPS 03 installed in RHEL 7.6 running on a physical machine or VMware ESXi virtual machine.
- HANA 2.0 SPS 03 installed in SUSE 15 with XFS file system.

SAP HANA does not support recovery of multitenant database containers by using storage snapshots. Only containers with one tenant database are supported.

## MySQL

- 5.5.x — Community Server, Enterprise, Standard, and Classic editions
- 5.6.x — Community Server, Enterprise, Standard, and Classic editions
- 5.7.x — Community Server, Enterprise, Standard, and Classic editions
- 8.0.x — Community Server, Enterprise, Standard, and Classic editions

## MariaDB

- 10.0.x, 10.1.x, 10.2.x, 10.3.x, 10.4.x, 10.5.x, 10.6.x, 10.7.x
