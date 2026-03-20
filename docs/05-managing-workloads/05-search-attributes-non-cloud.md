---
title: "Search attributes for non-cloud-to-cloud workloads"
section: "Managing workloads in the Cyber Protect console"
subsection: "Search attributes for non-cloud-to-cloud workloads"
page_range: "411-424"
tags: [search, workloads, attributes, dynamic groups, query, filtering]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#attributes-dynamic-groups.html"
---

# Search attributes for non-cloud-to-cloud workloads

The following table summarizes the attributes that you can use in your search queries for non-cloud-to-cloud workloads.

## General attributes

| Attribute | Meaning | Search query examples | Group creation |
|-----------|---------|----------------------|----------------|
| `name` | Workload name: host name for physical machines, name for virtual machines, database name, email address for mailboxes | `name = 'en-00'` | Yes |
| `id` | Device ID. To see the device ID, under **Devices**, select the device, click **Details** > **All properties**. The ID is shown in the `id` field. | `id != '4B2A7A93-A44F-4155-BDE3-A023C57C9431'` | Yes |
| `resourceType` | Workload type. Possible values include: `'machine'`, `'exchange'`, `'mssql_server'`, `'mssql_instance'`, `'mssql_database'`, `'mssql_database_folder'`, `'msexchange_database'`, `'msexchange_storage_group'`, `'msexchange_mailbox.msexchange'`, `'msexchange_mailbox.office365'`, `'mssql_aag_group'`, `'mssql_aag_database'`, `'virtual_machine.vmww'`, `'virtual_machine.vmwesx'`, `'virtual_host.vmwesx'`, `'virtual_cluster.vmwesx'`, and many more virtualization types including Hyper-V, Parallels, RHEV, KVM, Xen, VCD, oVirt, Azure, Nutanix, and `'bootable_media'`. | `resourceType = 'machine'`; `resourceType in ('virtual_center.vmwesx', 'machine')` | Yes |
| `chassis` | Chassis type. Possible values: `laptop`, `desktop`, `server`, `other`, `unknown` | `chassis = 'laptop'`; `chassis IN ('laptop', 'desktop')` | Yes |
| `ip` | IP address (only for physical machines) | `ip RANGE ('10.250.176.1','10.250.176.50')` | Yes |
| `comment` | Comment for a device. Can be specified automatically or manually. Default: for physical Windows machines, the computer description is automatically copied as a comment (synchronized every 15 minutes). Empty for other devices. | `comment = 'important machine'`; `comment = ''` (all machines without a comment) | Yes |

### Comment details

For devices on which a protection agent is installed, there are two separate comment fields:

- **Agent comment** -- For physical Windows machines, the computer description is automatically copied as a comment, synchronized every 15 minutes. Empty for other devices. The automatic synchronization is disabled if there is manually added text in the comment field.
- **Device comment** -- If the agent comment is specified automatically, it is copied as a device comment. Manually added agent comments are not copied as device comments. Device comments are not copied as agent comments.

If both comments are specified, the device comment has priority. To refresh automatically synchronized comments, restart the Managed Machine Service in **Windows Services** or run:

```
net stop mms
net start mms
```

## System attributes

| Attribute | Meaning | Search query examples | Group creation |
|-----------|---------|----------------------|----------------|
| `isOnline` | Workload availability. Values: `true`, `false` | `isOnline = true` | No |
| `hasAsz` | Secure Zone availability. Values: `true`, `false` | `hasAsz = true` | Yes |
| `tzOffset` | Timezone offset from UTC, in minutes | `tzOffset = 120`; `tzOffset > 120` | Yes |

## CPU, memory, disks

| Attribute | Meaning | Search query examples | Group creation |
|-----------|---------|----------------------|----------------|
| `cpuArch` | CPU architecture. Values: `'x64'`, `'x86'` | `cpuArch = 'x64'` | Yes |
| `cpuName` | CPU name | `cpuName LIKE '%XEON%'` | Yes |
| `memorySize` | RAM size in megabytes | `memorySize < 1024` | Yes |
| `diskSize` | Hard drive size in gigabytes or megabytes (only for physical machines) | `diskSize < 300GB`; `diskSize >= 3000000MB` | No |

## Operating system

| Attribute | Meaning | Search query examples | Group creation |
|-----------|---------|----------------------|----------------|
| `osName` | Operating system name | `osName LIKE '%Windows XP%'` | Yes |
| `osType` | Operating system type. Values: `'windows'`, `'linux'`, `'macosx'` | `osType = 'windows'`; `osType IN ('linux', 'macosx')` | Yes |
| `osArch` | Operating system architecture. Values: `'x64'`, `'x86'` | `cpuArch = 'x86'` | Yes |
| `osProductType` | OS product type. Values: `'dc'` (Domain Controller), `'server'`, `'workstation'`. Note: When the domain controller role is assigned on a Windows server, osProductType changes from `server` to `dc`. | `osProductType = 'server'` | Yes |
| `osSp` | Service pack of the operating system | `osSp = 1` | Yes |
| `osVersionMajor` | Major version of the operating system | `osVersionMajor = 1` | Yes |
| `osVersionMinor` | Minor version of the operating system | `osVersionMinor > 1` | Yes |

## Agent

| Attribute | Meaning | Search query examples | Group creation |
|-----------|---------|----------------------|----------------|
| `agentVersion` | Version of the installed protection agent | `agentVersion LIKE '12.0.*'` | Yes |
| `hostId` | Internal ID of the protection agent. To see it, under **Devices**, select the device, click **Details** > **All properties**, and check the `id` value of the `agent` property. | `hostId = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'` | Yes |
| `virtualType` | Virtual machine type. Values: `'vmwesx'`, `'mshyperv'`, `'pcs'`, `'hci'`, `'scale'`, `'ovirt'`, `'vcd'` | `virtualType = 'vmwesx'` | Yes |
| `insideVm` | Virtual machine with an agent inside. Values: `true`, `false` | `insideVm = true` | Yes |

## Location

| Attribute | Meaning | Search query examples | Group creation |
|-----------|---------|----------------------|----------------|
| `tenant` | Name of the tenant to which the device belongs | `tenant = 'Unit 1'` | Yes |
| `tenantId` | Identifier of the tenant to which the device belongs. Shown in the `ownerId` field under **Details** > **All properties**. | `tenantId = '3bfe6ca9-9c6a-4953-9cb2-a1323f454fc9'` | Yes |
| `ou` | Devices belonging to the specified Active Directory organizational unit | `ou IN ('RnD', 'Computers')` | Yes |
| `customerUuid` | Devices belonging to the specified Customer tenant ID | `customerUuid = 'd96c5dde-5466-489d-9c74-df7dbd8c2148'` | No |

## Status

| Attribute | Meaning | Search query examples | Group creation |
|-----------|---------|----------------------|----------------|
| `state` | Device state. Values: `'idle'`, `'interactionRequired'`, `'canceling'`, `'backup'`, `'recover'`, `'install'`, `'reboot'`, `'failback'`, `'testReplica'`, `'run_from_image'`, `'finalize'`, `'failover'`, `'replicate'`, `'createAsz'`, `'deleteAsz'`, `'resizeAsz'` | `state = 'backup'` | No |
| `status` | Protection status. Values: `ok`, `warning`, `error`, `critical`, `protected`, `notProtected` | `status = 'ok'`; `status IN ('error', 'warning')` | No |
| `protectedByPlan` | Devices protected by a protection plan with a given ID | `protectedByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'` | No |
| `okByPlan` | Devices protected by a plan with OK status | `okByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'` | No |
| `errorByPlan` | Devices protected by a plan with Error status | `errorByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'` | No |
| `warningByPlan` | Devices protected by a plan with Warning status | `warningByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'` | No |
| `runningByPlan` | Devices protected by a plan with Running status | `runningByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'` | No |
| `interactionByPlan` | Devices protected by a plan with Interaction Required status | `interactionByPlan = '4B2A7A93-A44F-4155-BDE3-A023C57C9431'` | No |
| `lastBackupTime`* | Date and time of the last successful backup. Format: `'YYYY-MM-DD HH:MM'` | `lastBackupTime > '2023-03-11'`; `lastBackupTime is null` | No |
| `lastBackupTryTime`* | Time of the last backup attempt. Format: `'YYYY-MM-DD HH:MM'` | `lastBackupTryTime >= '2023-03-11'` | No |
| `nextBackupTime`* | Time of the next backup. Format: `'YYYY-MM-DD HH:MM'` | `nextBackupTime >= '2023-08-11'` | No |
| `lastVAScanTime`* | Date and time of the last successful vulnerability assessment | `lastVAScanTime > '2023-03-11'`; `lastVAScanTime is null` | Yes |
| `lastVAScanTryTime`* | Time of the last vulnerability assessment attempt | `lastVAScanTimeTryTime >= '2022-03-11'` | Yes |
| `nextVAScanTime`* | Time of the next vulnerability assessment | `nextVAScanTime <= '2023-08-11'` | Yes |
| `network_status` | Network isolation status for Endpoint detection and response (EDR). Values: `connected`, `isolated` | `network_status= 'connected'` | Yes |

> **Note:** If you skip the hour and minutes value, the start time is considered to be YYYY-MM-DD 00:00, and the end time is considered to be YYYY-MM-DD 23:59:59. For example, `lastBackupTime = 2023-01-20` means that the search results will include all backups from the interval `lastBackupTime >= 2023-01-20 00:00` and `lastBackupTime <= 2023-01-20 23:59:59`.
