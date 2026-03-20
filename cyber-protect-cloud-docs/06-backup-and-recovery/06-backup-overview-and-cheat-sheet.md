---
title: "Backup overview and cheat sheet"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup"
page_range: "514-518"
tags: ["backup", "protection-plan", "cheat-sheet", "backup-schemes", "retention", "schedule", "cloud-storage", "local-folder", "network-folder"]
acronis_version: "26.02"
---

# Backup overview and cheat sheet

## Backup overview

A protection plan with the Backup module enabled is a set of rules that specify how the given data will be protected on a given machine. A protection plan can be applied to multiple machines at the time of its creation, or later.

### To create the first protection plan with the Backup module enabled

1. Select the machines that you want to back up.
2. Click **Protect**.
3. To create a new plan, click **Create plan**. Enable the **Backup** module and unroll the settings.
4. [Optional] Modify the protection plan name by clicking the default name.
5. [Optional] Modify the Backup module parameters by clicking the corresponding setting of the protection plan panel.
6. [Optional] To modify the backup options, click **Change** next to **Backup options**.
7. Click **Create**.

The Backup module settings include:
- **What to back up** (e.g., Entire machine)
- **Continuous data protection (CDP)**
- **Where to back up** (e.g., Cloud storage)
- **Schedule** (e.g., Monday to Friday at 05:45 PM)
- **How long to keep** (e.g., Monthly: 6 months, Weekly: 4 weeks, Daily: 7 days)
- **Encryption**
- **Application backup**
- **Backup options**

### To apply an existing protection plan

1. Select the machines that you want to back up.
2. Click **Protect**. If a common protection plan is already applied, click **Add plan**.
3. Select a protection plan to apply.
4. Click **Apply**.

## Backup cheat sheet

The following table summarizes the most common backup parameters.

### Physical machines (agent-based)

| What to back up | Selection methods | Where to back up | Backup schemes |
|---|---|---|---|
| Disks/volumes | Direct selection, Policy rules | Cloud, Local folder | Always incremental (Single-file), Always full |
| | File filters | Network folder, NFS*, Secure Zone** | Weekly full / Daily incremental, Monthly full / Weekly differential / Daily incremental (GFS), Custom (F-D-I) |
| Files (physical machines only) | Direct selection, Policy rules, File filters | Cloud, Local folder, Network folder, NFS*, Secure Zone** | Always incremental (Single-file), Always full, Weekly full / Daily incremental, Monthly full / Weekly differential / Daily incremental (GFS), Custom (F-D-I) |

### Virtual machines (agentless backup)

| What to back up | Selection methods | Where to back up | Backup schemes |
|---|---|---|---|
| Disks/volumes | Policy rules, File filters | Cloud, Local folder, Network folder, NFS* | Weekly full / Daily incremental, Monthly full / Weekly differential / Daily incremental (GFS), Custom (F-D-I) |

### Other workload types

| What to back up | Selection methods | Where to back up | Backup schemes |
|---|---|---|---|
| ESXi configuration | Direct selection | Local folder, Network folder, NFS* | Always full, Weekly full / daily incremental, Custom (F-I) |
| System state | Direct selection | Cloud, Local folder, Network folder | Always full, Weekly full / daily incremental, Custom (F-I) |
| SQL databases | Direct selection | Cloud, Local folder, Network folder | Always incremental (Single-file) - only for SQL databases |
| Exchange databases | Direct selection | Cloud, Local folder, Network folder | Same as SQL |
| Microsoft 365 Mailboxes | Direct selection | Cloud | Always incremental (Single-file) |
| Microsoft 365 (local Agent) | Direct selection | Local folder, Network folder | Always incremental (Single-file) |
| Microsoft 365 (cloud Agent) - Mailboxes, Public folders, Teams, OneDrive files, SharePoint Online data | Direct selection (+ Policy rules for OneDrive/SharePoint) | Cloud | Up to 6 backups per day |
| Google Workspace - Gmail, Drive files, Shared drive files | Direct selection (+ Policy rules for Drive/Shared) | Cloud | Up to 6 backups per day |

> **Notes:**
> - \* Backup to NFS shares is not available in Windows.
> - \*\* Secure Zone cannot be created on a Mac.
> - Backups to public cloud require a **Local backup** storage quota.

## How long to keep the backups?

You can keep your backups forever or configure a retention period by the following criteria:

- By backup age (single rule / per backup set)
- By number of backups
- By total size of backups

> **Note:** The **By total size of backups** retention rule is not available with the **Always incremental (single-file)** backup scheme or when backing up to the cloud storage.
