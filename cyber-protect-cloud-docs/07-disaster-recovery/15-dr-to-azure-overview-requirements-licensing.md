---
title: "Disaster Recovery to Microsoft Azure - overview, requirements, and licensing"
section: "Implementing disaster recovery"
subsection: "Disaster Recovery to Microsoft Azure"
page_range: "1016-1021"
tags: [Microsoft Azure, DR to Azure, software requirements, supported OS, virtualization platforms, limitations, licensing, Cold DR, Warm DR, Azure subscription]
acronis_version: "26.02"
---

# Disaster Recovery to Microsoft Azure

Disaster Recovery to Microsoft Azure is a cost-efficient disaster recovery solution integrated with the Acronis Cyber Protection service. It leverages the power and flexibility of the Microsoft Azure enterprise-grade platform as a target DR site. This solution uses cold backups (recovery points), which can be stored in Microsoft Azure, Acronis Cyber Protect Cloud, or a partner-hosted cloud storage. The entire DR site configuration and orchestration are managed centrally from the Cyber Protect console. Your own Microsoft Azure subscription is used as the target DR site.

Automation and orchestration include the following capabilities:

- Initial DR site configuration
- Automated test failover with AI-powered screenshot verification
- Orchestrated failover
- Automated failback to both physical and virtual machines, with near-zero downtime
- Runbooks to automate key disaster recovery scenarios
- On-demand workers (temporary agents) that eliminate the need for permanent virtual appliances

## DR deployment models

- **Cold DR** -- Backups are stored in the storage, but no compute resources (virtual machines) are running until a disaster occurs. Cold DR provides cost-effective recovery with minimal Azure infrastructure usage.
- **Warm DR** (coming in future releases) -- Backups are incrementally replicated to the Azure warm storage and, in case of disaster, are ready to run as Azure virtual machines. Warm DR provides near-zero RTO.

You retain full control over the underlying infrastructure and Microsoft Azure capabilities, with the flexibility to use native Azure services or integrate custom solutions -- such as third-party firewalls and SD-WAN appliances -- by connecting them to the selected recovery networks at the DR site. This solution also supports failover of Windows desktops running Windows 10 or Windows 11.

> **Note**
> To use Disaster Recovery to Microsoft Azure, you must have an active subscription to Microsoft Azure.

---

# Software requirements for Disaster Recovery to Microsoft Azure

## Supported operating systems

Protection with a recovery server in Microsoft Azure has been tested for the following operating systems:

- Ubuntu 20.x, 21.x, 22.10, 23.04
- Debian 10.x, 11.x
- Red Hat Enterprise Linux 8.x, 9.x
- Windows Server 2008 R2
- Windows Server 2012/2012 R2
- Windows Server 2016 -- all installation options, except for Nano Server
- Windows Server 2019 -- all installation options, except for Nano Server
- Windows Server 2022 -- all installation options, except for Nano Server
- Windows Server 2025 -- all installation options, except for Nano Server
- Windows 10
- Windows 11

The software may work with other Windows operating systems and Linux distributions, but this is not guaranteed.

## Supported virtualization platforms

Protection of virtual machines with a recovery server has been tested for the following virtualization platforms:

- VMware ESXi 5.1, 5.5, 6.0, 6.5, 6.7, 7.0
- Windows Server 2008 R2 with Hyper-V
- Windows Server 2012/2012 R2 with Hyper-V
- Windows Server 2016 with Hyper-V -- all installation options, except for Nano Server
- Windows Server 2019 with Hyper-V -- all installation options, except for Nano Server
- Windows Server 2022 with Hyper-V -- all installation options, except for Nano Server
- Microsoft Hyper-V Server 2012/2012 R2
- Microsoft Hyper-V Server 2016
- Kernel-based Virtual Machines (KVM) -- fully virtualized guests (HVM) only. Paravirtualized guests (PV) are not supported.

Linux workloads that have agentless backups from a guest OS and have volumes with the Logical Volume Manager (LVM) configurations are supported.

Windows workloads that have agentless backups from a guest OS and have dynamic disks (LDM) configurations are supported.

The software might work with other virtualization platforms and versions, but this is not guaranteed.

## Limitations

The following platforms and configurations are not supported in Disaster Recovery to Microsoft Azure:

1. **Unsupported platforms:**
   - Agents for Virtuozzo
   - macOS

2. **Unsupported configurations:**
   - **Microsoft Windows:** Active Directory service with FRS replication is not supported. Removable media without either GPT or MBR formatting ("superfloppy") are not supported.
   - **Linux:** File systems without a partition table. Linux workloads backed up with an agent from a guest OS with advanced LVM configurations: Striped volumes, Mirrored volumes, RAID 0, RAID 4, RAID 5, RAID 6, or RAID 10 volumes.

   > **Note**
   > Workloads with multiple operating systems installed are not supported.

3. **Unsupported tenant modes:**
   - Disaster recovery is not available when Compliance mode is enabled for the tenant.

4. **Unsupported backup types:**
   - Continuous data protection (CDP) recovery points are incompatible.
   - Forensic backups cannot be used for creating recovery servers.

   > **Important**
   > If you create a recovery server from a backup having a CDP recovery point, then during the failback or creating backup of a recovery server, you will lose the data contained in the CDP recovery point.

Cloud servers are not encrypted.

---

# Licensing for Disaster Recovery to Microsoft Azure

To enable Disaster Recovery to Microsoft Azure, the **DR and direct backup to Azure** offering item must be enabled for your tenant. This offering item enables:

- Disaster Recovery (DR) to Azure that uses the customer's own Azure subscription.
- Direct backup to Azure.

One quota from the offering item is consumed when a recovery server is created or direct backup to Azure is enabled. Only one quota per workload is used, even if both DR and direct backup to Azure are active.

The quota for this offering item that is assigned to your tenant represents the maximum number of workloads that can be protected. A device that uses both Disaster Recovery to Azure and direct backup to Azure protection consumes one quota.

## Hard quota overage

When the hard quota for the offering item is decreased, existing recovery servers might become unlicensed. The number of unlicensed recovery servers depends on the overage. Recovery servers that were in test or production failover remain functional but become unlicensed. Unlicensed recovery servers in the Standby state have limited DR operations. You cannot power on unlicensed servers until they are licensed again.

Increasing the offering item quota automatically assigns licenses to unlicensed devices and clears related alerts.

## Generated alerts

The following alerts are generated when there are issues caused by missing licenses:

- **Recovery server is unlicensed** -- This alert is generated when a server becomes unlicensed.
- **Disaster Recovery protection was disabled for a workload** -- This alert is generated when there are no available licenses.
- **Automated test failover failed** -- This alert is generated when a failover is blocked due to a missing license.

---

# Working with Disaster Recovery to Microsoft Azure

The basic workflow for using disaster recovery is the following:

1. Configure your DR site in Microsoft Azure.
2. Create a recovery server of the workload that you want to protect.
3. [Optional] Configure the connectivity from your local site to the cloud site in Microsoft Azure by using Azure native services, such as Azure site-to-site VPN or Azure ExpressRoute.
4. [Optional] Configure runbooks.
5. Configure automated test failover or perform a test failover.
6. [When a disaster occurs] Perform a production failover.
7. [After the disaster] Perform a failback to the local site.

## Managing access to your Microsoft Azure subscription

Disaster Recovery to Microsoft Azure requires that you connect to a Microsoft Azure subscription in the Cyber Protect console.

You can configure Microsoft Azure subscriptions in the **Infrastructure** > **Public clouds** screen. There, you can also manage your subscriptions, by performing the following tasks: renewing access to the subscription, viewing subscription properties and activities, or removing the subscription.

| Task | Link |
|------|------|
| Add access to a Microsoft Azure subscription | "Adding access to a Microsoft Azure subscription" (p. 710) |
| Renew access to a Microsoft Azure subscription | "Renewing access to a Microsoft Azure subscription" (p. 711) |
| Remove access to a Microsoft Azure subscription | "Removing access to a Microsoft Azure subscription" (p. 712) |

## Cross-subscription configuration issues in Microsoft Azure

If you are using two different subscriptions for Microsoft Azure -- for example, one for direct backup to Azure ("Subscription 1"), and another for the configuration of the DR site ("Subscription 2") -- but you remove the access to "Subscription 1", the following issues will occur:

- **Failover will fail** -- You cannot start a failover, as the backup data is stored in "Subscription 1".
- **Failback will fail** -- If the access to "Subscription 1" is removed after a failover was performed, it will not be possible to access all backup data, preventing backup operations of VM in failover and failback.

> **Important**
> Do not remove or revoke access to the original Azure subscription if backups that are stored there are still used or needed.
