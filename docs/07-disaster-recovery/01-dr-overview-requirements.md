---
title: "About Acronis Disaster Recovery and software requirements"
section: "Implementing disaster recovery"
subsection: "Disaster Recovery to Cyber Protect Cloud"
page_range: "930-934"
tags: [disaster recovery, DRaaS, requirements, supported OS, virtualization, limitations, trial]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#about-cyber-disaster-recovery-cloud.html"
---

# About Acronis Disaster Recovery

Acronis Disaster Recovery is a part of Cyber Protection that provides disaster recovery as a service (DRaaS). Disaster Recovery is a fast and stable solution that, in the event of a man-made or natural disaster, launches recovery servers (exact copies of your local servers) on the disaster recovery (DR) site.

The DR site is a secondary location that ensures that IT operations are restored and continue if the primary site fails. In such a case, DR switches the workloads from the corrupted original machines to the recovery servers at the DR site. The DR site includes the cloud servers and the cloud connectivity (cloud networks).

The DR site can be located in Acronis Cyber Protect Cloud or Microsoft Azure. The availability of the DR site locations depends on the offering items that are enabled for your tenant.

> **Note:** Only one location is supported per customer tenant. If you want to change the location of your DR site, you must first remove the existing configuration, and then create a new one with the new location.

# Disaster Recovery to Cyber Protect Cloud

Disaster Recovery to Cyber Protect Cloud has the following characteristics:

- The location of the DR site is Cyber Protect Cloud.
- The backups (recovery points) of the protected servers are stored in Cyber Protect Cloud.

## The key functionality

> **Note:** Some features might require additional licensing, depending on the applied licensing model.

- Manage the Disaster Recovery service from a single console
- Extend up to 23 local networks to the cloud, by using a secure VPN tunnel
- Establish the connection to the cloud site without any VPN appliance deployment (the cloud-only mode)
- Establish the point-to-site connection to your local and cloud sites
- Protect your machines by using recovery servers in the cloud
- Protect applications and appliances by using primary servers in the cloud
- Perform automatic disaster recovery operations for encrypted backups
- Perform a test failover in the isolated network
- Use runbooks to automate the deployment to the production environment in the cloud

## Software requirements for Disaster Recovery to Cyber Protect Cloud

### Supported operating systems

Protection with a recovery server has been tested for the following operating systems:

- CentOS 6.6, 7.x, 8.x
- Debian 9.x, 10.x, 11.x
- Red Hat Enterprise Linux 6.6, 7.x, 8.x
- Ubuntu 18.04, 20.x, 21.x, 22.04, 22.10
- Oracle Linux 7.3 and 7.9 with Unbreakable Enterprise Kernel
- Windows Server 2008 R2
- Windows Server 2012/2012 R2
- Windows Server 2016 -- all installation options, except for Nano Server
- Windows Server 2019 -- all installation options, except for Nano Server
- Windows Server 2022 -- all installation options, except for Nano Server
- AlmaLinux 8.x, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5
- Rocky Linux 9.x, 8.x
- SUSE Linux Enterprise Server 15

The software may work with other Windows operating systems and Linux distributions, but this is not guaranteed.

### Microsoft Azure VM support

Protection with a recovery server has been tested for Microsoft Azure VM with the following operating systems: Windows Server 2008 R2 through 2022 (all installation options, except for Nano Server), and Ubuntu Server 20.04 LTS - Gen2 (Canonical).

### Supported virtualization platforms

Protection of virtual machines with a recovery server has been tested for the following virtualization platforms:

- VMware ESXi 5.1, 5.5, 6.0, 6.5, 6.7, 7.0
- Windows Server 2008 R2 through 2022 with Hyper-V (all installation options, except for Nano Server)
- Microsoft Hyper-V Server 2012/2012 R2, 2016
- Kernel-based Virtual Machines (KVM) -- fully virtualized guests (HVM) only. Paravirtualized guests (PV) are not supported.
- Red Hat Enterprise Virtualization (RHEV) 3.6
- Red Hat Virtualization (RHV) 4.0
- Citrix XenServer: 6.5, 7.0, 7.1, 7.2
- Nutanix Acropolis Hypervisor (AHV) with Nutanix Acropolis Operating System (AOS): 6.5, 6.6, 6.7, 6.8, 6.10
- Proxmox VE 8.2, 8.3, 8.4, 9.0
- Scale Computing HyperCore 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4
- Virtuozzo Infrastructure 3.5, 4.0, 4.5, 4.6, 4.7, 5.0, 5.1, 5.2, 5.3, 5.4, 6.0, 6.1, 6.2, 6.3

Linux workloads that have agentless backups from a guest OS and have volumes with the Logical Volume Manager (LVM) configurations are supported. Windows workloads that have agentless backups from a guest OS and have dynamic disks (LDM) configurations are supported.

## Limitations

The following platforms and configurations are not supported in Disaster Recovery:

1. **Unsupported platforms:** Agents for Virtuozzo, macOS, Windows desktop operating systems (due to Microsoft product terms), Windows Server Azure Edition.

2. **Unsupported configurations (Microsoft Windows):** Windows desktop operating systems, Active Directory service with FRS replication, removable media without either GPT or MBR formatting ("superfloppy").

3. **Unsupported configurations (Linux):** File systems without a partition table; Linux workloads backed up with an agent from a guest OS that have volumes with advanced LVM configurations (striped, mirrored, RAID 0/4/5/6/10 volumes); for SUSE Linux Enterprise Server 15, configurations with Btrfs are not supported.

   > **Note:** Workloads with multiple operating systems installed are not supported.

4. **Unsupported tenant modes:** Disaster recovery is not available when Compliance mode is enabled for the tenant.

5. **Unsupported backup types:** Continuous data protection (CDP) recovery points are incompatible. Forensic backups cannot be used for creating recovery servers.

   > **Important:** If you create a recovery server from a backup having a CDP recovery point, then during the failback or creating backup of a recovery server, you will lose the data contained in the CDP recovery point.

Additional limitations:
- A recovery server has one network interface. If the original machine has several network interfaces, only one is emulated.
- Cloud servers are not encrypted.

## Disaster Recovery trial version

You can use a trial version of Acronis Disaster Recovery for a period of 30 days. In this case, Disaster Recovery has the following limitations for partner tenants:

- No access to public internet for recovery and primary servers. You cannot assign public IP addresses to the servers.
- IPsec Multi-site VPN is not available.

## Operations with Microsoft Azure virtual machines

You can perform failover of Microsoft Azure virtual machines to Acronis Cyber Protect Cloud. After that, you can perform failback from Acronis Cyber Protect Cloud back to Azure virtual machines. You can configure a Multisite IPsec VPN connectivity between Acronis Cyber Protect Cloud and the Azure VPN gateway.

## Limitations when using Geo-redundant cloud storage

Geo-redundant cloud storage provides a secondary location for your backup data. The secondary location is in a region that is geographically distinct from the primary storage location.

> **Important:** The Disaster Recovery service is not supported if the backup storage location is switched from the primary location to the geo-redundant secondary location.
