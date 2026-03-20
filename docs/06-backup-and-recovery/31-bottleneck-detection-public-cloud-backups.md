---
title: "Bottleneck Detection and Backing Up Workloads to Public Clouds"
section: "Managing the backup and recovery of workloads and files"
subsection: "Bottleneck detection and public cloud backups"
page_range: "685-699"
tags: [bottleneck-detection, performance, activity-details, public-cloud, Microsoft-Azure, Amazon-S3, S3-compatible, IONOS-Cloud, Impossible-Cloud, backup-location, immutability]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#protecting-workloads-public-clouds.html"
---

# Understanding the Detection of Bottlenecks

The bottleneck detection feature helps you understand where you can improve performance by highlighting which component in your system was the slowest during a backup or recovery process. As bottlenecks always occur in any transmission event, they do not necessarily need to be resolved -- your backups may already be fast enough.

You can easily view and track bottlenecks in the **Activity details** tab. In the Cyber Protect console, go to **Monitoring** > **Activities**, and then click the relevant activity.

## What Is a Bottleneck?

Bottlenecks are typically caused due to a slow component in the processing chain. The bottleneck detection feature enables you to track these slow components, helping you understand which of the following component types is the slowest:

- **Source:** Determines if the reading speed from the backup/recovery source is causing a bottleneck.
- **Destination:** Determines if the writing speed to the backup/recovery destination is affecting performance.
- **Agent:** Determines if the agent is processing the data fast enough.

The bottleneck type can change at different times during the backup/recovery activity. The percentages shown in the **Bottleneck** section of the **Activity details** tab represent the percentage of time when this type of bottleneck was encountered (e.g., "Read data from source (workload): 63%" means for 63% of the recovery activity time, the slow speed in reading data was the bottleneck).

> **Note:** Bottleneck statistics are only available for tasks that run more than one minute long. The bottleneck values update dynamically every minute while the corresponding activity is running.

## How to Reduce Bottlenecks

The bottleneck detection feature highlights the read and write data flow between backup components. The read statistics refer to the data flow from the data source to the agent, and the write statistics refer to the data flow between the agent and the backup archive (destination).

To reduce bottlenecks and improve the read/write data flow performance, analyze the channel between the agent and the data source/backup archive. For example, try benchmarking your hard disks if the agent is backing up some local files.

## Viewing Bottleneck Details

You can view detected bottlenecks for any type of backup, backup replication, or recovery process (to any type of destination folder or location), including virtual machine backups, machine backups, and file/folder backups. You can also view bottlenecks for virtual machine replication and failback activities.

### To View Bottleneck Details

1. In the Cyber Protect console, go to **Monitoring** > **Activities**.
2. Click on the relevant activity.
   In the **Activity details** tab, the **Bottleneck** section is shown in blue.
3. Click **Show details** to view the most frequently encountered bottleneck during the backup/recovery operation. The **Bottleneck** section expands to show a summary of the relevant bottleneck types with percentages.

## Supported Workloads, Agents, and Backup Locations

The detection of bottlenecks is available for the following types:

### Disk/image-level backups performed by:
- Agent for Azure, Windows, Linux, Mac
- Agent for VMware (both Virtual Appliance and Windows, including VM replication and failback)
- Agent for Hyper-V, Scale Computing HC3, oVirt (KVM)
- Agent for Virtuozzo Infrastructure Platform, Virtuozzo
- Agent for VMware Cloud Director (vCD-BA)

### File-level backups:
- Agent for Windows, Linux, Mac

### Application-level backups:
- Agent for SQL, Exchange, MySQL/MariaDB, Oracle, SAP HANA

### Backup locations:
- Acronis Cloud storage (including partner-hosted storage)
- Public Cloud storage
- Network shares (SMB + NFS)
- Local folders
- Locations defined by script
- Acronis Secure Zone

---

# Backing Up Workloads to Public Clouds

> **Note:** This feature requires the **Direct Backup to Public Cloud** feature to be enabled for your tenant. Note that adding this functionality to a protection plan may be subject to additional charges.

> **Important:** Backing up workloads to any of the supported public cloud services is possible only for protection agents running on Windows 7 or higher, and Windows Server 2008 R2 SP1 or higher. Agents executing off-host data protection plans while running on an outdated operating system cannot work with locations on public clouds.

You can select public cloud services, such as Microsoft Azure, Amazon S3 (Simple Storage Service), and S3-compatible public cloud storage, as backup destinations in the Cyber Protect console.

> **Note:** Public cloud storage is not supported as destination for Microsoft 365 and Google Workspace backups.

To configure backup locations on public clouds, you must be a Company administrator or Unit administrator, or have one of the following roles: Cyber administrator, Administrator, or User.

## Defining a Backup Location in Microsoft Azure

> **Note:** Required roles: Company administrator, User, Cyber administrator.

You can define backup locations on the Microsoft Azure Blob Storage service, under one of the following Microsoft Azure Storage account types:

- Standard general purpose v2 (StorageV2)
- Premium block blobs

Both administrators and non-administrator users can back up workloads to Microsoft Azure.

### To Define a Backup Location in Microsoft Azure

1. In the Cyber Protect console, either go to **Devices** and select the relevant workload (click the link in **Where to back up** row), or go to **Backup storage**.
2. Click **Add location**.
3. From the **Public clouds** drop-down list, select **Microsoft Azure**.
4. If the relevant subscription is already registered, select it. Otherwise, click **Add** and **Sign in** to the Microsoft login page.
5. In the **Storage account** field, select the relevant account.

> **Note:** Only Microsoft Azure storage accounts with regular endpoint suffixes that contain `core.windows.net` are currently supported. Only the Hot and Cool access tiers are currently supported.

6. Click **Add**.

## Defining a Backup Location in Amazon S3

> **Note:** Required roles: Company administrator, User, Cyber administrator.

> **Note:** Buckets in special Government Cloud regions are not supported as backup locations.

### To Define a Backup Location in Amazon S3

1. In the Cyber Protect console, go to **Devices** or **Backup storage**.
2. Click **Add location**.
3. From the **Public clouds** dropdown list, select **Amazon S3**.
4. If the relevant Amazon S3 connection is already registered, select it. Otherwise, click **Add new connection**.
5. Define the following:
   - **Location name:** Enter the name of the backup location (must be unique to the customer tenant).
   - **Storage Class:** Select from:
     - S3 Standard
     - Standard - Infrequent Access (S3 Standard-IA)
     - One Zone - Infrequent Access (S3 One Zone-IA)
     - S3 Intelligent Tiering
   - **Bucket:** Select the relevant Amazon S3 bucket. If the selected bucket is enabled with Object Lock and Object Versioning features, the **Backup immutability period (days)** checkbox is enabled.

> **Note:** When using S3 Intelligent Tiering, older backup objects can be automatically moved to "Archive Access" or "Deep Archive Access" tiers. Objects in these tiers cannot be accessed instantly and require "rehydration." Recovery from these old backups will fail without first retrieving the old objects from archive tiers.

> **Note:** It is recommended to configure the Lifecycle policy for the bucket if you have set the immutability option. Buckets with Object Versioning and Object Lock features enabled will store object versions forever, resulting in storage consumption growing indefinitely unless a Lifecycle policy is configured.

6. Click **Add**.

## Defining a Backup Location in IONOS Cloud, Impossible Cloud, or S3 Compatible Storage

> **Note:** Required roles: Company administrator, User, or Cyber administrator. Buckets in special GovCloud regions are not supported as backup locations.

### To Define a Backup Location

1. In the Cyber Protect console, go to **Devices** or **Backup storage**.
2. Click **Add location**.
3. From the **Public clouds** dropdown list, select one of: **S3 compatible**, **Impossible Cloud**, **IONOS Cloud Object Storage**.
4. Define the following:
   - **Management agent:** Click **Browse** to select the management agent. This agent establishes initial communication with the storage.
   - **Location name:** Enter the name of the backup location (must be unique).
   - **Bucket:** Select the relevant storage bucket. If the selected bucket is enabled with Object Lock and Versioning features, the **Backup immutability period (days)** checkbox is enabled.
   - [For S3 compatible storage only] Optionally select **Allow using a self-signed certificate of the endpoint** (this skips validation of the certificate chain -- vulnerable to MITM attack, not recommended).
5. Click **Add**.

> **Note:** The immutability option resolves the issue of old object retention by automatically adjusting the immutability period for old objects when newer backup objects still have dependencies on them. The immutability period is never less than the immutability period days value defined during the creation of the backup location.

## Viewing and Updating Public Cloud Backup Locations

You can view and update the Microsoft Azure, Amazon S3, and S3-compatible cloud backup locations that you defined in the **Backup storage** module, or when creating or editing a protection plan.

> **Note:** You cannot manually refresh or delete a public cloud backup location in the **Backup storage** module. The contents of the backup location are updated automatically after each backup or recovery operation.

### To View Public Cloud Backup Locations

1. In the Cyber Protect console, go to **Backup storage**.
2. Select the relevant location to see current backups.
3. (Optional) Click on a backup to view more details.

### To Update a Public Cloud Backup Location in a Protection Plan

1. Go to the relevant protection plan, and select **Edit**.
2. Click the link in the **Where to back up** row.
3. Select from the list of existing backup locations, or click **Add location** to add a new location.
