---
title: "Protecting Microsoft Applications"
section: "Managing the backup and recovery of workloads and files"
subsection: "Protecting Microsoft applications"
page_range: "746-776"
tags: [Microsoft-SQL, Microsoft-Exchange, SharePoint, Active-Directory, domain-controller, application-aware-backup, database-backup, mailbox-backup, AAG, DAG, granular-recovery]
acronis_version: "26.02"
---

# Protecting Microsoft Applications

## Protection Methods

There are two methods of protecting Microsoft applications:

- **Database backup** -- A file-level backup of the databases and the metadata associated with them. The databases can be recovered to a live application or as files.
- **Application-aware backup** -- A disk-level backup that also collects the applications' metadata. This enables browsing and recovery of the application data without recovering the entire disk or volume. The disk or volume can also be recovered as a whole, making it a single solution for both disaster recovery and data protection.

For Microsoft Exchange Server, you can also opt for **Mailbox backup** -- a backup of individual mailboxes via the Exchange Web Services protocol. The mailboxes or mailbox items can be recovered to a live Exchange Server or to Microsoft 365. Mailbox backup is supported for Microsoft Exchange Server 2010 Service Pack 1 (SP1) and later.

## Protecting Microsoft SharePoint

A Microsoft SharePoint farm consists of front-end servers that run SharePoint services, database servers that run Microsoft SQL Server, and (optionally) application servers. To protect an entire SharePoint farm:

- Back up all of the database servers with application-aware backup.
- Back up all of the unique front-end servers and application servers with usual disk-level backup.

The backups of all servers should be done on the same schedule. To protect only the content, you can back up the content databases separately.

## Protecting a Domain Controller

A machine running Active Directory Domain Services can be protected by application-aware backup. If a domain contains more than one domain controller, and you recover one of them, a nonauthoritative restore is performed and a USN rollback will not occur after the recovery.

## Recovery Methods Summary

| Application | From a database backup | From an application-aware backup | From a disk backup |
|---|---|---|---|
| Microsoft SQL Server | Databases to a live SQL Server instance; Databases as files | Entire machine; Databases to a live SQL Server instance; Databases as files | Entire machine |
| Microsoft Exchange Server | Databases to a live Exchange; Databases as files; Granular recovery to Exchange or Microsoft 365* | Entire machine; Databases to a live Exchange; Databases as files; Granular recovery to Exchange or Microsoft 365* | Entire machine |
| Microsoft SharePoint database servers | Databases to a live SQL Server instance; Databases as files; Granular recovery by using SharePoint Explorer | Entire machine; Databases to a live SQL Server instance; Databases as files; Granular recovery by using SharePoint Explorer | Entire machine |
| Microsoft SharePoint front-end web servers | - | - | Entire machine |
| Active Directory Domain Services | - | Entire machine | - |

*Granular recovery is also available from a mailbox backup.

## Requirements for Application-Aware Backups

### Common Requirements

**For Microsoft SQL Server:**
- At least one Microsoft SQL Server instance is started.
- The SQL writer for VSS is turned on.

**For Microsoft Exchange Server:**
- The Microsoft Exchange Information Store service is started.
- Windows PowerShell is installed (version 2.0+ for Exchange 2010+).
- Microsoft .NET Framework is installed (version 2.0+ for Exchange 2007, version 3.5+ for Exchange 2010+).
- The Exchange writer for VSS is turned on.

> **Note:** Agent for Exchange needs a temporary storage to operate. By default, the temporary files are located in `%ProgramData%\Acronis\Temp`. Ensure at least 15% free space relative to an Exchange database size.

**On a domain controller:**
- The Active Directory writer for VSS is turned on.

**When creating a protection plan:**
- For physical machines, the Volume Shadow Copy Service (VSS) backup option is enabled.
- For virtual machines, the VSS for virtual machines backup option is enabled.

### Additional Requirements for Application-Aware Backups

- **Entire machine** must be selected for backup. The **Sector-by-sector** backup option must be disabled.
- **ESXi virtual machines:** Must meet VMware's requirements for application-consistent backup. VMware Tools must be installed and up-to-date. User Account Control (UAC) must be disabled, or use built-in domain administrator (DOMAIN\Administrator) credentials.
- **Hyper-V virtual machines:** Guest OS must be Windows Server 2008 or later. No dynamic disks. Network connection between host and guest is required. UAC must be disabled or use built-in domain administrator credentials. Hyper-V Integration Services must be installed.

> **Note:** Agentless application-aware backup is not supported for Hyper-V and VMware ESXi virtual machines running Windows Server 2022 or Windows Server 2025. Use agent-based backup instead.

### Required User Rights

- **For SQL Server:** Member of the **Backup Operators** or **Administrators** group on the machine and a member of the **sysadmin** role on each instance. Only Windows authentication is supported.
- **For Exchange Server:** Exchange 2007: member of **Administrators** group and **Exchange Organization Administrators** role group. Exchange 2010+: member of **Administrators** group and **Organization Management** role group.
- **For Active Directory:** Domain administrator.

## Database Backup

### Selecting SQL Databases

A backup of an SQL database contains the database files (.mdf, .ndf), log files (.ldf), and other associated files. The SQL transaction logs are truncated after each successful backup.

1. Click **Devices** > **Microsoft SQL**.
2. Browse to the data that you want to back up (AAGs, machines, SQL Server instances, individual databases).
3. Select the data to back up and click **Protect**.
4. If prompted, provide credentials (member of **Backup Operators** or **Administrators** group and **sysadmin** role).

### Selecting Exchange Server Data

| Exchange version | Data items | User rights |
|---|---|---|
| 2007 | Storage groups | Membership in the **Exchange Organization Administrators** role group |
| 2010/2013/2016/2019 | Databases, Database Availability Groups (DAG) | Membership in the **Server Management** role group |

1. Click **Devices** > **Microsoft Exchange**.
2. Browse and select the data to back up (DAGs, machines, databases, or mailboxes if configured).
3. If prompted, provide credentials.
4. Click **Protect**.

## Protecting Always On Availability Groups (AAG)

The backup software supports *only* the Always On Availability Group (AAG) for SQL Server 2012 or later. Other cluster configurations (FCI, database mirroring, log shipping) are *not* supported.

For successful cluster backup and recovery, Agent for SQL must be installed on each node of the WSFC cluster.

### Backing Up Databases in an AAG

1. Install Agent for SQL on each node.
2. Select the AAG itself (not individual nodes) to backup.

> **Warning!** The database set must be exactly the same in all nodes. If even one set is different, the cluster backup will not work correctly.

3. Configure the "Cluster backup mode" backup option.

### Recovery of Databases in an AAG

1. Select the databases to recover and the recovery point.
2. Follow the SQL database recovery steps. The software automatically defines a cluster node for recovery.

> **Important:** A database included in an AAG cannot be overwritten during a recovery. You need to exclude the target database from the AAG before the recovery or recover the database as a new non-AAG one.

## Protecting Database Availability Groups (DAG)

Cluster-aware backup is supported *only* for DAG in Exchange Server 2010 or later. Other cluster configurations (SCC, CCR for Exchange 2007) are *not* supported.

DAG is a group of up to 16 Exchange Mailbox servers. Agent for Exchange has to be installed on each node of the Exchange cluster. With cluster-aware backup, you back up only one copy of the clustered data. If the data changes its location within the cluster due to a switchover or failover, the software will track all relocations.

### Backing Up Exchange Cluster Data

1. Select the DAG as described in "Selecting Exchange Server data."
2. Configure the "Cluster backup mode" backup option.

> **Important:** For cluster-aware backup, ensure to select the DAG itself. Selecting individual nodes or databases inside the DAG will result in the **Cluster backup mode** option being ignored.

### Recovering the Exchange Cluster Data

1. Select the recovery point for the database (selecting an entire cluster is not possible).
2. Follow the Exchange database recovery steps. The software automatically defines a cluster node for recovery.

## Application-Aware Backup

Application-aware disk-level backup is available for individual physical machines, ESXi virtual machines, and Hyper-V virtual machines. It is not available for device groups.

When you back up a machine running Microsoft SQL Server, Microsoft Exchange Server, or Active Directory Domain Services, enable **Application backup** for additional protection.

### Benefits

- Applications are backed up in a consistent state and will be available immediately after the machine is recovered.
- You can recover SQL and Exchange databases, mailboxes, and mailbox items without recovering the entire machine.
- SQL transaction logs are truncated after each successful backup.
- If a domain contains more than one domain controller, a nonauthoritative restore is performed.

## Mailbox Backup

Mailbox backup is supported for Microsoft Exchange Server 2010 SP1 and later. The agent must be installed on a machine in the same Active Directory forest as the Microsoft Exchange Server and connected to the Client Access server role (CAS).

> **Note:** You can also recover mailboxes and mailbox items from database backups and application-aware backups.

### To Connect Agent for Exchange to CAS

1. Click **Devices** > **Add** > **Microsoft Exchange Server** > **Exchange mailboxes**.
2. In **Client Access server**, specify the FQDN of the machine where the CAS role is enabled.
3. In **Authentication type**, select **Kerberos** (default) or **Basic**.
4. [For basic auth] Select **HTTPS** or **HTTP** protocol. Optionally select **Check SSL certificate**.
5. Provide credentials (member of **Server Management** and **Recipient Management** role groups, with **ApplicationImpersonation** management role enabled).
6. Click **Add**.

## Recovering SQL Databases

You can recover SQL databases to the original instance, to a different instance on the original machine, or to an instance on a non-original target machine (Agent for SQL must be installed on the target). You can also recover databases as files.

### Recovery States

- **Ready to use (RESTORE WITH RECOVERY)** -- default. Database is ready for use after recovery.
- **Non-operational (RESTORE WITH NORECOVERY)** -- database is non-operational; additional transaction logs can be applied.
- **Read-only (RESTORE WITH STANDBY)** -- read-only access; uncommitted transactions are saved in a temporary standby file.

### Recovering System Databases

All system databases of an instance are recovered at once. The software automatically restarts the destination instance in single-user mode. System databases can only be recovered to an instance of the same version and are always recovered in the "ready to use" state.

### Recovering SQL Databases as Files

Useful for data mining, audit, or further processing by third-party tools. Select the databases, click **Recover** > **Databases as files** (or **Recover as files**), specify the target path, click **Start recovery**.

## Recovering Exchange Databases

You can recover Exchange Server data to a live Exchange Server (original or of the same version with the same FQDN). Agent for Exchange must be installed on the target machine.

### To a Live Exchange Server

1. Select the machine or database and click **Recovery**.
2. Select a recovery point.
3. Click **Recover** > **Exchange databases** (or **Databases to an Exchange server**).
4. By default, databases are recovered to the original ones. To recover as a different database, specify the new database name and path.
5. Click **Start recovery**.

### As Files

Select the databases, click **Recover** > **Exchange databases** (or **Databases as files**), select the target folder, click **Start recovery**.

### Mounting Exchange Server Databases

After recovering database files, bring the databases online by mounting them using Exchange Management Console or Exchange Management Shell. Use the `Eseutil /r <Enn>` command to bring a database from a Dirty Shutdown state to a Clean Shutdown state before mounting.

## Recovering Exchange Mailboxes and Mailbox Items

You can recover Exchange mailboxes and mailbox items from database backups (including DAG), application-aware backups, and mailbox backups.

Recoverable items include: Mailboxes (except archive mailboxes), public folders, public folder items, email folders, email messages, calendar events, tasks, contacts, journal entries, and notes.

### Recovery to an Exchange Server

Granular recovery can be performed to Microsoft Exchange Server 2010 SP1 and later. When a mailbox is recovered to an existing mailbox, existing items with matching IDs are overwritten. Recovery of mailbox items recreates the full path in the target folder.

### Recovery to Microsoft 365

Recovery of Exchange data items to Microsoft 365, and vice versa, is supported on the condition that Agent for Microsoft 365 is installed locally.

### To Recover Mailboxes

1. Select the machine or database containing the data, click **Recovery**.
2. Select a recovery point.
3. Click **Recover** > **Exchange mailboxes**.
4. Select the mailboxes to recover. Click **Recover**.
5. [To Microsoft 365] In **Recover to**, select **Microsoft 365**, specify the target mailbox.
6. [To Exchange] Click **Target machine with Microsoft Exchange Server** to select the target.
7. [Optional] Click **Database to re-create any missing mailboxes**.
8. Click **Start recovery**.

### To Recover Mailbox Items

1. Navigate to the mailbox, select items to recover (search by subject, sender, recipient, date for emails; by title and date for events; by name, email, phone for contacts).
2. Click **Recover**.
3. Select the recovery target (Exchange Server or Microsoft 365), specify the target mailbox and folder.
4. Click **Start recovery**.

## Copying Microsoft Exchange Server Libraries

When recovering Exchange mailboxes or items to Microsoft 365, you may need to copy libraries from the backed-up machine to the machine with Agent for Microsoft 365.

| Exchange Server version | Libraries | Default location |
|---|---|---|
| 2010 | ese.dll, esebcli2.dll, store.exe | `%ProgramFiles%\Microsoft\Exchange Server\V14\bin` |
| 2013 | ese.dll | `%ProgramFiles%\Microsoft\Exchange Server\V15\bin` |
| | msvcr110.dll | `%WINDIR%\system32` |
| 2016, 2019 | ese.dll | `%ProgramFiles%\Microsoft\Exchange Server\V15\bin` |
| | msvcr110.dll, msvcp110.dll | `%WINDIR%\system32` |

The libraries should be placed in the folder `%ProgramData%\Acronis\ese`.

## Changing Access Credentials

You can change access credentials for SQL Server or Exchange Server without re-installing the agent:

1. Click **Devices**, and then click **Microsoft SQL** or **Microsoft Exchange**.
2. Select the AAG, DAG, SQL Server instance, or Exchange Server.
3. Click **Specify credentials**.
4. Specify the new credentials, and then click **OK**.
