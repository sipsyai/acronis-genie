---
title: "Protecting Oracle DB, SAP HANA, MySQL/MariaDB, and Proxmox"
section: "Managing the backup and recovery of workloads and files"
subsection: "Protecting databases and Proxmox workloads"
page_range: "867-876"
tags: [Oracle-Database, SAP-HANA, MySQL, MariaDB, Proxmox, application-aware-backup, database-recovery, table-recovery, container-backup, Agent-for-Proxmox, stored-routines]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#protecting-mysql-mariadb-data.html"
---

# Protecting Oracle Database

Protection of Oracle Database is described in a separate document available at:
`https://dl.managed-protection.com/u/pdf/OracleBackup_whitepaper_en-US.pdf`

# Protecting SAP HANA

Protection of SAP HANA is described in a separate document available at:
`https://dl.managed-protection.com/u/pdf/SAP_HANA_backup_whitepaper_en-US.pdf`

# Protecting MySQL and MariaDB Data

You can protect MySQL or MariaDB data with application-aware backup. It collects application metadata and allows granular recovery on the instance, database, or table level.

Agent for MySQL/MariaDB is bundled with Agent for Linux (64-bit) and can be installed only on 64-bit Linux-based operating systems.

## Limitations

- MySQL or MariaDB clusters are not supported.
- Instances running in Docker containers are not supported.
- Instances running on BTRFS file systems are not supported.
- System databases (`sys`, `mysql`, `information_schema`, `performance_schema`) and databases with no tables cannot be recovered to live instances. They can be recovered as files when recovering the whole instance.
- Recovery is supported only to target instances of the same version or later, with restrictions:
  - Recovery from MySQL 5.x to MySQL 8.x is not supported.
  - Recovery to a later MySQL 5.x version (including minor versions) is supported only via recovery of the whole instance as files.
- Recovery from backups stored on Secure Zone is not supported.
- Databases and tables cannot be recovered by Agent for MySQL/MariaDB running on a machine with AppArmor (recover as files or entire machine instead).
- Recovery to target databases configured with symbolic links is not supported.

## Known Issues

If encountering issues recovering data from password-protected Samba shares, log out from the Cyber Protect console and log back in. Select the recovery point and click **MySQL/MariaDB databases** (not Entire machine or Files/folders).

## Configuring an Application-Aware Backup

### Prerequisites

- At least one MySQL or MariaDB instance must be running.
- The protection agent must be started under the root user.
- Application-aware backup is available only with **Entire machine** selected as backup source.
- The **Sector-by-sector** backup option must be disabled.

### Configuration Steps

1. In the Cyber Protect console, select machines running MySQL or MariaDB instances.
2. Create a protection plan with the backup module enabled.
3. In **What to back up**, select **Entire machine**.
4. Click **Application backup**, enable the switch next to **MySQL/MariaDB Server**.
5. Select how to specify instances:
   - **For all workloads** -- same connection parameters for all instances.
   - **For specific workloads** -- per-instance connection parameters.
6. Click **Add instance** to configure:
   - Connection type: TCP socket (IP address and port) or Unix socket (socket path).
   - Credentials with the following privileges: `FLUSH_TABLES` OR `RELOAD` for all databases (`*.*`), and `SELECT` for `information_schema.tables`.
7. Click **Done**.

## Recovery Options Summary

| What to recover | Recover as | Recover to |
|---|---|---|
| MySQL/MariaDB Server | Entire machine | Machine with Agent for Linux |
| MySQL/MariaDB Server | Files or folders | Machine with Agent for Linux |
| Instance | Files | Machine with Agent for MySQL/MariaDB |
| Database | Same or new database | Original or another instance (Agent for MySQL/MariaDB) |
| Table | Same or new table | Original or another instance/database (Agent for MySQL/MariaDB) |

### Recovering Instances

1. Select the machine, click **Recovery**, select a recovery point.
2. Click **Recover** > **MySQL/MariaDB databases**.
3. Select the instance, click **Recover as files**.
4. Under **Path**, select target directory.
5. Click **Start recovery**.

### Recovering Databases

1. Select the machine, click **Recovery**, select a recovery point.
2. Click **Recover** > **MySQL/MariaDB databases**.
3. Drill down to the desired instance and databases.
4. Select databases, click **Recover**.
5. Click **Target MySQL/MariaDB instance** to specify connection parameters and credentials with privileges: `INSERT`, `CREATE`, `DROP`, `LOCK_TABLES`, `ALTER`, `SELECT`.
6. Verify target database (or rename for new database recovery).
7. Under **Overwrite existing databases**, select overwriting mode.
8. Click **Start recovery**.

### Recovering Tables

1. Select the machine, click **Recovery**, select a recovery point.
2. Click **Recover** > **MySQL/MariaDB databases**.
3. Drill down to the desired instance, database, and tables.
4. Select tables, click **Recover**.
5. Specify target instance credentials (same privileges as for databases).
6. Verify target table (or rename for new table recovery).
7. Under **Overwrite existing tables**, select overwriting mode.
8. Click **Start recovery**.

### Recovering Stored Routines

When recovering a whole MySQL instance, stored routines are automatically recovered. For individual databases or new databases, stored routines must be manually recovered:

1. On the original machine, export routines:
   ```
   mysqldump -p [source_database_name] --routines --no-create-info --no-data > [exported_db_routines.sql]
   ```
2. On the recovered machine, open MySQL command line client:
   ```
   mysql> use [recovered_database_name];
   mysql> source [path_to_exported_db_routines.sql];
   ```

---

# Protecting Proxmox Virtual Machines and Containers

You can perform agentless backup of Proxmox virtual machines and containers by installing Agent for Proxmox on the protected host. Agent for Proxmox is bundled with Agent for Linux (64-bit).

## Requirements

- Proxmox VE 8.2 or later.
- In clustered environments, install an agent on each node.
- A **Virtual Machine** quota is required per Proxmox VM or container.

## Supported Storage

- **Virtual machines:** All storages on which a VM can be created.
- **Containers:** LVM Thin, Ceph/RBD, BtrFS.

## Supported Backup Locations

Cloud storage (including partner-hosted), public cloud storages, network folders (SMB/NFS), local folders.

## Limitations

### General

- Not supported: Run as VM, Convert to VM, Application-aware backup, VM replication.
- Cannot recover virtual disks or containers to CephFS storage.
- Disks with the backup option disabled in Proxmox VE are not backed up.
- Disk provisioning type selection depends on target storage support.

### Virtual Machines

- Not backed up: VM templates, detached disks, snapshots, TPM state device content.
- At least one `Directory` storage is required for temporary files.
- Changed block tracking (CBT) is not available for powered-off VMs and VMs that went through a power cycle.
- During backup, powered-off VMs are powered on and kept in a frozen state (no RAM/CPU usage).
- Locked/hibernated VMs cannot be backed up.

### Containers

- Only LVM Thin, Ceph/RBD, BtrFS storage types are supported.
- Containers with disabled snapshots are not supported.
- CBT is not available.
- `OS type` property is not recovered.

## Installing Agent for Proxmox

Install locally on the protected host via graphical user interface or command-line interface. After installation, all VMs and containers appear in the Cyber Protect console under **Devices** > **Proxmox**.

## Backing Up Proxmox Workloads

Create a protection plan (only the **Backup** module is available for Proxmox workloads). You can also back up the Proxmox host separately as a Linux server, using file filters to exclude VM data directories.

## Recovering Proxmox Workloads

A Proxmox virtual machine can be recovered as:
- A physical machine.
- The original or a new VM on the same hypervisor.
- A new machine on a different hypervisor (cross-platform recovery).

A Proxmox container can be recovered as:
- The original container.
- A new Proxmox container (cross-platform recovery is not supported for containers).

You can recover files from backed-up Proxmox VMs and containers to the Proxmox host or attached network storage. File-level recovery directly to a VM or container is not supported.
