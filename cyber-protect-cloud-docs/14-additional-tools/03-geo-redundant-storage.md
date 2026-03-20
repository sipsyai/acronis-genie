---
title: "Geo-Redundant Storage"
section: "Additional Cyber Protection Tools"
subsection: "Geo-Redundant Storage"
page_range: "1487-1489"
tags: [geo-redundant-storage, replication, disaster-recovery, cloud-storage, data-durability, backup-storage]
acronis_version: "26.02"
---

# Geo-Redundant Storage

With Geo-redundant storage, your backed-up data is asynchronously copied to a replication location that is geographically distant to the primary backup location. Thus, the data remains durable and accessible even if the primary location becomes unavailable.

The replicated data uses the same amount of storage space as the original data.

## Limitations

- Geo-redundant storage might not be available in all data centers.
- Geo-redundancy is supported only with the cloud storage. It is not supported with third-party storages, such as partner-hosted storages or public cloud storages.
- Location for the replicated data depends on your datacenter.
- Additional limitations apply when you use Geo-redundant storage with Disaster Recovery.

## Enabling Geo-Redundant Storage

### Prerequisites

- A storage that supports geo-redundancy is assigned to the customer tenant.
- Geo-redundant storage is provisioned for the customer tenant in Management Portal. Geo-redundant storage cannot be provisioned if a non-compatible storage is assigned. For example, a partner-hosted storage.

You can enable Geo-redundant storage on the main screen of the Cyber Protect console or on the **Settings** tab. The result of both procedures is the same.

### On the Main Screen

1. Log in to the Cyber Protect console as administrator.
2. A warning message appears at the top of the Cyber Protect console.
3. In the warning message, click **Enable Geo-redundant cloud storage**.
4. To acknowledge your understanding of replication locations and fees, select the checkbox.
5. To confirm your choice, click **Enable**.

As a result, Geo-redundant storage is enabled and backed-up data will be copied to the replication location.

### On the Settings Tab

1. Log in to the Cyber Protect console as administrator.
2. Go to **Settings** > **System settings**.
3. Collapse the list of default backup options, and then click **Geo-redundant cloud storage**.
4. Enable the **Geo-redundant cloud storage** switch.
5. Click **Save**.
6. To acknowledge your understanding of replication locations and fees, select the checkbox.
7. To confirm your choice, click **Enable**.

As a result, Geo-redundant storage is enabled and backed-up data will be copied to the replication location.

## Disabling Geo-Redundant Storage

You can disable Geo-redundant storage in the Cyber Protect console.

### To Disable Geo-Redundant Storage

1. Log in to the Cyber Protect console as administrator.
2. Go to **Settings** > **System settings**.
3. Collapse the list of default backup options, and then click **Geo-redundant cloud storage**.
4. Disable the **Geo-redundant cloud storage** switch.
5. Click **Save**.
6. To confirm your choice, type **Disable**, and then click **Disable**.

As a result, Geo-redundant storage is disabled. Replicated data will be deleted within one day.

## Viewing the Geo-Replication Status

Geo-replication status shows if the data from the primary backup location is copied to the replication location. The following statuses are possible:

| Status | Description |
|--------|-------------|
| **In sync** | Data was copied to the replication location. |
| **Syncing** | Data is being copied to the replication location. The duration of this operation depends on the size of the data. |
| **On hold** | Data replication is temporarily suspended. |
| **Disabled** | Data replication is disabled. |

### To Check the Replication Status

1. Log in to the Cyber Protect console.
2. On the **Backup storage** tab, select the backup location, and then select the backup archive.
3. Click **Details**, and then check the status in the **Geo-replication status** section.
