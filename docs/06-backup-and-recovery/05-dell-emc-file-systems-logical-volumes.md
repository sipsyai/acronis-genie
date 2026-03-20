---
title: "Dell EMC compatibility, supported file systems, and logical volumes"
section: "Managing the backup and recovery of workloads and files"
subsection: "Supported operating systems and environments for backup and recovery"
page_range: "506-513"
tags: ["Dell-EMC", "Data-Domain", "file-systems", "NTFS", "ext4", "ReFS", "XFS", "APFS", "exFAT", "logical-volumes", "LDM", "LVM", "encryption", "BitLocker", "4K-sector", "retention-lock"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#supported-file-systems.html"
---

# Dell EMC compatibility, supported file systems, and logical volumes

## Compatibility with Dell EMC Data Domain storages

You can use Dell EMC Data Domain devices as backup storage. A backup scheme that regularly creates full backups (for example **Always full**) is recommended.

### Retention lock

Retention lock (Governance mode) is supported. If retention lock is enabled on the Data Domain storage, you must add the `AR_RETENTION_LOCK_SUPPORT` environment variable to the machine with the protection agent that uses this storage as a backup destination.

> **Note:** Dell EMC Data Domain storages with enabled retention lock are not supported by Agent for Mac.

When retention lock is enabled, backups on the storage will not be deleted by the retention rules in the protection plan. No error will be shown. The backups will be deleted when the retention lock expires and the retention rules are applied again.

### Adding the AR_RETENTION_LOCK_SUPPORT variable

**In Windows:**

1. Log in as administrator to the machine with the protection agent.
2. In **Control Panel**, go to **System and Security** > **System** > **Advanced system settings**.
3. On the **Advanced** tab, click **Environment Variables**.
4. In the **System variables** panel, click **New**.
5. Add:
   - Variable name: `AR_RETENTION_LOCK_SUPPORT`
   - Variable value: `1`
6. Click **OK** and restart the machine.

**In Linux:**

1. Log in as administrator to the machine with the protection agent.
2. Go to the `/sbin` directory, and open the `acronis_mms` file for editing.
3. Above the line `export LD_LIBRARY_PATH`, add:
   ```
   export AR_RETENTION_LOCK_SUPPORT=1
   ```
4. Save the file and restart the machine.

**In a virtual appliance:**

1. Log in as administrator to the virtual appliance.
2. Go to the `/bin` directory, and open the `autostart` file for editing.
3. Under the line `export LD_LIBRARY_PATH`, add:
   ```
   export AR_RETENTION_LOCK_SUPPORT=1
   ```
4. Save the file and restart the virtual appliance.

## Supported file systems

A protection agent can back up any file system accessible from the operating system where the agent is installed. The software automatically switches to sector-by-sector mode when backing up drives with unrecognized or unsupported file systems (for example, Btrfs).

| File system | Agents | Bootable media (Win/Linux) | Bootable media (Mac) | Limitations |
|-------------|--------|---------------------------|---------------------|-------------|
| **FAT16/32** | All agents* | Yes | Yes | No limitations |
| **NTFS** | All agents | Yes | Yes | No limitations |
| **ext2/ext3/ext4** | All agents | Yes | No | No limitations |
| **HFS+** | Agent for Mac | No | Yes | No limitations |
| **APFS** | Agent for Mac | No | Yes | Supported from macOS High Sierra 10.13. Disk configuration should be re-created manually when recovering to a non-original machine or bare metal. |
| **JFS** | Agent for Linux | Yes | No | File filters not supported. Fast incremental/differential backup cannot be enabled. |
| **ReiserFS3** | Agent for Linux | Yes | No | File filters not supported. Fast incremental/differential backup cannot be enabled. |
| **ReiserFS4** | Agent for Linux | Yes | No | File filters not supported. Fast incremental/differential backup cannot be enabled. Volumes cannot be resized during recovery. |
| **ReFS** | All agents | Yes | Yes | File filters not supported. Fast incremental/differential backup cannot be enabled. Volumes cannot be resized during recovery. During file recovery, only content is recovered (ACLs and alternate streams are not). Sparse files are recovered as regular files. |
| **XFS** | All agents | Yes | Yes | File filters not supported. Fast incremental/differential backup cannot be enabled. Volumes cannot be resized during recovery. Incremental and differential backups of XFS volumes to the cloud may be significantly slower than comparable ext4 backups using fast-incremental mode. |
| **Linux swap** | Agent for Linux | Yes | No | No limitations |
| **exFAT** | All agents | Yes (bootable media cannot be used for recovery if the backup is stored on exFAT) | Yes | Only disk/volume backup supported. File filters not supported. Individual files cannot be recovered from a backup. |

*On Windows XP systems, Agent for Windows supports only NTFS-formatted drives.

### Sector-by-sector backup requirements

A sector-by-sector backup is possible for any file system that:
- Is block-based
- Spans a single disk
- Has a standard MBR/GPT partitioning scheme

If the file system does not meet these requirements, the backup fails.

### Data Deduplication

In Windows Server 2012 and later, you can enable the Data Deduplication feature for an NTFS volume. You can back up and recover a data deduplication-enabled volume at a disk level without limitations. File-level backup is supported except when using Acronis VSS Provider. The Data Deduplication feature of Windows Server is unrelated to the Acronis Backup Deduplication feature.

## Supported operations with logical volumes

Backup and recovery of workloads with logical volumes, such as LDM in Windows (dynamic disks) and LVM in Linux, are supported with the following limitations.

### Backup

| Agent-based backup | Agentless backup |
|---|---|
| Logical volumes are backed on per volume basis. File filters (Inclusions/Exclusions) are supported. | When a logical volume is detected on a disk, the disk is backed up in sector-by-sector (RAW) mode. The partition structure is not analyzed and no volume images are stored separately. Individual LDM or LVM volumes cannot be selected as backup source. Only **Entire machine** is available. File filters are not supported. |

### Recovery

| | From agent-based backup | From agentless backup |
|---|---|---|
| **Agent-based recovery** | Per-volume recovery is available. File and folder recovery is available. You can recover a Linux machine with LVM volumes from an agent-based backup in public cloud to a new machine by using backup replication and bootable media. | Per-volume recovery is not available. File and folder recovery is available. |
| **Agentless recovery** | Machine migration (P2V, V2P, V2V) is not supported. To recover data from an agent-based backup, use bootable media. File and folder recovery is available. | Per-volume recovery is not available. Entire machine recovery is available. File and folder recovery is available. The **Run as VM** operation is supported. Conversion to VMware ESXi, Microsoft Hyper-V, and Scale Computing HC3 is supported. |

## Compatibility with encryption software

There are no limitations on backing up and recovering data encrypted by *file-level* encryption software.

*Disk-level* encryption software encrypts data on the fly. This is why data contained in the backup is not encrypted. Disk-level encryption software often modifies system areas: boot records, partition tables, or file system tables.

Supported disk-level encryption software:
- Microsoft BitLocker Drive Encryption
- McAfee Endpoint Encryption
- PGP Whole Disk Encryption

**Common installation rule:** Install the encryption software before you install the protection agents.

**Secure Zone:** Must not be encrypted with disk-level encryption. Exclude Secure Zone when encrypting the disk or its volumes.

### Software-specific recovery procedures

**Microsoft BitLocker Drive Encryption:**
1. Boot from the bootable media.
2. Recover the system (recovered data will be unencrypted).
3. Reboot the recovered system.
4. Turn on BitLocker.

For multi-partitioned disks, recover individual partitions under the operating system (recovery under bootable media may make the recovered partition undetectable for Windows).

**McAfee Endpoint Encryption and PGP Whole Disk Encryption:**
Recover an encrypted system partition by using bootable media only. If the recovered system fails to boot, rebuild the Master Boot Record as described at https://support.microsoft.com/kb/2622803.

## Compatibility with Advanced Format (4K-sector) hard disks

Backup and recovery are supported on traditional 512-byte sector disks and on Advanced Format disks with 4096-byte sector size. When recovering data from one disk to another, both disks must have the same logical sector size. Volumes on the disk are automatically aligned.

IDEMA specifies two types of Advanced Format disks:
- **512-byte emulation (512e) disks** - 512-byte logical sector size
- **4K native (4Kn) disks** - 4096-byte logical sector size (commonly used as external drives with USB connection; system boot might not be supported)

**To check the logical sector size:**

*Windows:*
```
fsutil fsinfo ntfsinfo D:
```
Check the **Bytes Per Sector** line.

*Linux:*
```
parted /dev/sdb print
```
Check the first value in the **Sector size (logical/physical)** line.
