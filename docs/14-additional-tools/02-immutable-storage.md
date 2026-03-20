---
title: "Immutable Storage"
section: "Additional Cyber Protection Tools"
subsection: "Immutable Storage"
page_range: "1483-1487"
tags: [immutable-storage, governance-mode, compliance-mode, backup-protection, ransomware, data-integrity, retention, cloud-storage]
acronis_version: "26.02"
---

# Immutable Storage

Immutable storage provides a critical layer of protection for backup data by preventing deletion or modification of restore points until their retention period expires. This safeguard ensures that backups remain intact even if credentials are compromised, ransomware disables security tools, or administrative errors occur. While enabling immutability may slightly increase storage costs because older restore points cannot be deleted before their retention period expires, this predictable expense is minimal compared to the financial and operational impact of losing critical data. Real-world incidents have demonstrated that immutability can be the difference between a full recovery and catastrophic data loss.

Immutable storage is available for all cloud backups stored in a supported cloud storage instance.

With immutable storage, you can access deleted backups during the specified retention period. You can recover content from these backups, but you cannot change, move, or delete them. When the retention period ends, the deleted backups are permanently deleted.

## What Goes Into Immutable Storage

The immutable storage contains the following backups:

- Backups that are deleted manually.
- Backups that are deleted automatically, according to the settings in the **How long to keep** section in a protection plan or the **Retention rules** section in a cleanup plan.

Deleted backups in the immutable storage still use storage space and are charged accordingly. Deleted tenants are not charged for any storage, including immutable storage.

## Immutable Storage Modes

Immutable storage is available in the following modes:

### Governance Mode

In this mode, all deleted backups remain in immutable storage for the specified retention period. This prevents ransomware or malicious actors from tampering with or erasing backup data and ensures the integrity of backups, which is essential for reliable disaster recovery.

In this mode, you can change the retention period or switch to Compliance mode. Immutable storage can be disabled only by contacting the Support team.

### Compliance Mode

In addition to the benefits of the Governance mode, the Compliance mode helps organizations meet the regulatory requirements for data retention and security by preventing changes in the retention policy, including changing the retention period or disabling it.

> **Important:** Selecting Compliance mode is irreversible. After selecting this mode, you cannot change the retention period or switch back to Governance mode. Immutable storage cannot be disabled in this mode.

## Supported Storages and Agents

- Immutable storage is supported only on the cloud storage.
  - Immutable storage is available for Acronis-hosted and partner-hosted cloud storages that use Acronis Cyber Infrastructure version 4.7.1 or later.
  - All storages that can be used with Acronis Cyber Infrastructure Backup Gateway are supported. For example, Acronis Cyber Infrastructure storage, Amazon S3 and EC2 storages, and Microsoft Azure storage.
  - Immutable storage requires that TCP port 40440 is open for the Backup Gateway service in Acronis Cyber Infrastructure. In version 4.7.1 and later, TCP port 40440 is automatically opened with the **Backup (ABGW) public** traffic type.
- Immutable storage requires a protection agent version 21.12 (build 15.0.28532) or later.
- Only TIBX (Version 12) backups are supported.

## Enabling Immutable Storage

Since September 2024, immutable storage in Governance mode has been enabled by default, with a retention period of 14 days.

You can enable immutable storage for tenants where it is not yet enabled by using either the Cyber Protect console or the Management Portal.

### To Enable Immutable Storage

1. Log in to the Cyber Protect console as an administrator.
2. Go to **Settings** > **System settings**.
3. Scroll through the list of default backups options, and then click **Immutable storage**.
4. Turn on the **Immutable storage** switch.
5. Specify a retention period between 14 and 3650 days. The default retention period is 14 days. A longer retention period will result in increased storage usage.
6. Select the immutable storage mode and, if prompted, confirm your choice:
   - **Governance mode** -- All deleted backups remain in immutable storage for the specified retention period. You can change the retention period or switch to Compliance mode. Immutable storage can be disabled only by contacting the Support team.
   - **Compliance mode** -- In addition to the benefits of the Governance mode, the Compliance mode helps organizations meet the regulatory requirements for data retention and security by preventing changes in the retention policy, including changing the retention period or disabling it.

     > **Important:** Selecting Compliance mode is irreversible. After selecting this mode, you cannot change the retention period or switch back to Governance mode. Immutable storage cannot be disabled in this mode.

7. Click **Save**.
8. To add an existing archive to the immutable storage, create a new backup in that archive by running the corresponding protection plan manually or on a schedule.

   > **Note:** If you delete a backup before adding the archive to the immutable storage, the backup is deleted permanently.

## Disabling Immutable Storage

> **Warning!** We strongly advise against disabling immutable storage:
> - Immutable storage is the last line of defense against accidental or malicious deletion of backups.
> - Ransomware protection alone is not enough -- immutability ensures recoverability even if credentials are compromised.
> - Cost impact is predictable and limited, while the risk of data loss without immutability is high and unpredictable.
> - Industry best practice and insurance requirements increasingly mandate immutable backups.
> - Disabling immutability exposes your organization to SLA breaches, compliance risks, and reputational damage.

> **Important:** Immutable storage can be disabled only in Governance mode and only by the Support team.

After immutable storage is disabled, any backups you delete will be permanently removed. Backups already stored in immutable storage will remain available for up to 14 days (336 hours), or until their retention period ends, whichever comes first.

**Example:** There are two deleted backups in immutable storage -- Backup A with a retention period of 7 days and Backup B with a retention period of 1 year. Immutable storage is disabled:
- If you delete a backup now, it is permanently deleted.
- On day 7, Backup A is permanently deleted (according to its original retention period).
- On day 14, Backup B is permanently deleted (according to the immutable storage grace period, because the original retention period exceeds 14 days).

## Accessing Deleted Backups in Immutable Storage

During the retention period, you can access deleted backups in immutable storage and recover data from them. A deleted backup can be part of a deleted archive or non-deleted archive.

> **Note:** To allow access to deleted backups, port 40440 on the backup storage should be enabled for incoming connections.

### In a Deleted Archive

1. On the **Backup storage** tab, select the cloud storage that contains the deleted backup.
2. To see the deleted archives, click **Show deleted**.
3. Select the archive that contains the backup that you want to recover.
4. Click **Show backups**.
5. Select the backup that you want to recover.
6. Proceed with the recovery operation.

### In a Non-Deleted Archive

1. On the **Backup storage** tab, select the cloud storage that contains the deleted backup.
2. Select the archive that contains the backup that you want to recover.
3. Click **Show backups**, and then click **Show deleted**.
4. Select the backup that you want to recover.
5. Proceed with the recovery operation.

## Viewing Immutable Storage Usage

You can view how much space the immutable storage uses in the Cyber Protect console.

### Limitations

- The reported value includes the total size of all deleted backups and the metadata of the backup archives in the storage. The metadata can be up to 10% of the reported value.
- The value shows usage data from up to 24 hours ago.
- If the actual usage is less than 0.01 GB, it is shown as 0.0 GB.

### To View the Immutable Storage Usage

1. Log in to the Cyber Protect console.
2. Go to **Backup storage** > **Backups**, and then select a cloud storage location that supports immutable storage.
3. Check the **Immutable storage and metadata** column.
