---
title: "Off-host data protection plans"
section: "Working with plans"
subsection: null
page_range: "241-244"
tags: ["off-host", "replication", "backup-replication", "offload", "data-processing"]
acronis_version: "26.02"
---

# Off-host data protection plans

> **Note:** In service-based billing mode, this feature requires the **Servers** quota to be enabled under Standard Protection as a prerequisite, but using the feature does not affect the quota usage. With solution-based billing mode, this functionality is available in customer tenants that use **Ultimate protection**.

Replication, validation, and cleanup are usually performed by the protection agent that performs the backup. This puts additional load on the machine on which the agent is running, even after the backup process is complete. To offload the machine, you can create off-host data protection plans — that is, separate plans for replication, validation, cleanup, and conversion to a virtual machine.

With the off-host data protection plans, you can do the following:

- Choose different agents for the backup and off-host data protection operations
- Schedule the off-host data processing operations during off-peak hours to minimize the network bandwidth consumption
- Schedule the off-host data processing operations during non-business hours, if you do not want to install a dedicated agent for off-host data processing

> **Note:** The off-host data processing plans run according to the time settings (including the time zone) of the machine on which the protection agent is installed. For a virtual appliance (for example, Agent for VMware or Agent for Scale Computing HC3), you can configure the time zone in the graphical user interface of the agent.

## Backup replication

Backup replication is copying a backup to another location. As an off-host data processing operation, it is configured in a backup replication plan. Backup replication can also be part of a protection plan.

### Creating a backup replication plan

1. In the Cyber Protect console, click **Management** > **Backup replication**.
2. Click **Create plan**.
3. In **Agent**, select the agent that will perform the replication. You can select any agent that has access both to the source location and the replication locations.
4. In **Items to replicate**, select the archives or backup locations to replicate. To switch between archives and locations, use the **Locations / Backups** switch in the upper-right corner. If you select multiple encrypted archives, their encryption password must be the same. For archives with different encryption passwords, create separate plans.
5. In **Destination**, specify the replication location.
6. In **How to replicate**, select which backups (also known as recovery points) to replicate:
   - **All backups**
   - **Only full backups**
   - **Only the last backup**
7. In **Schedule**, configure the replication schedule. Ensure that the last replicated backup will still be available in its original location when the backup replication starts.
8. In **Retention rules**, specify the retention rules for the target location:
   - **By number of backups**
   - **By backup age** (separate settings for monthly, weekly, daily, and hourly backups)
   - **By total size of backups**
   - **Keep backups indefinitely**
9. [If you selected encrypted archives] Enable the **Backup password** switch and provide the encryption password.
10. [Optional] To modify the plan options, click the gear icon, and configure as required.
11. Click **Create**.

### What to replicate

You can replicate individual backup sets or whole backup locations. When you replicate a backup location, all backup sets in it are replicated. Backup sets consist of backups (also known as recovery points). You must select which backups to replicate.

| | Always incremental (single-file) | Always full | Weekly full, Daily incremental | Monthly full, Weekly differential, Daily incremental (GFS) |
|---|---|---|---|---|
| **All backups** | All backups in the backup set | All backups in the backup set | All backups in the backup set | All backups in the backup set |
| **Only full backups** | Only the first backup, which is full | All backups | One backup every week* | One backup every month* |
| **Only last backup** | Only the newest backup in the backup set* | Only the newest backup in the backup set* | Only the newest in the backup set, regardless of its type* | Only the newest in the backup set, regardless of its type* |

*When configuring the schedule, ensure the last replicated backup is still available in its original location when replication starts.

### Supported locations for off-host data processing

| Backup location | Supported as a source | Supported as a target |
|----------------|----------------------|----------------------|
| Cloud storage | + | + |
| Local folder | + | + |
| Network folder | + | + |
| Public cloud | + | + |
| NFS folder | – | – |
| Secure Zone | – | – |
