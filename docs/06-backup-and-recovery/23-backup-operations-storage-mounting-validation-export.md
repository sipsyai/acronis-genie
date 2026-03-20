---
title: "Backup operations: storage, mounting volumes, validating, exporting, and deleting backups"
section: "Managing the backup and recovery of workloads and files"
subsection: "Operations with backups"
page_range: "677-682"
tags: ["backup-storage", "mount-volume", "validate-backup", "export-backup", "delete-backup", "orphaned-backups", "backup-archive", "File-Explorer", "read-write-mount"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#deleting-backups.html"
---

# Backup storage

The **Backup storage** tab provides access to all backups, including backups of offline workloads, workloads no longer registered in the console, and backups to public clouds such as Microsoft Azure.

Backups are organized into backup archives, named: `<workload name> - <protection plan name>`.

**Orphaned archives** are archives that are no longer associated to a protection plan, cloud backup plan, or registered workload. Orphaned backups use storage space and are billed accordingly.

> **Warning!** Do not edit backup files manually. This might result in file corruption and make the backups unusable. Corrupted backups are marked as **Unknown** in the console and you can only delete them.

### Access control

- Accounts with the administrator role can access all backups in their tenant or unit.
- Accounts with the user role can only access their own backups.
- Backups stored in a shared location (SMB or NFS share) are visible to all users who have read permissions.

### To manually add a backup location

1. Go to the **Backup storage** tab, and then click **Add location**.
2. Select the location type: Local folder, Network folder, Secure Zone, NFS folder, or Public cloud.
3. Configure the location, and then click **Done**.

### To refresh backup locations

Go to **Backup storage** tab, select a backup location, and in the **Actions** pane click **Refresh**.

### To select a backup (recovery point)

1. Go to **Backup storage** tab, select a backup location.
2. In **Machine to browse from**, select an online machine (required to access certain backups, e.g., SQL databases require a machine running Agent for SQL).
3. Select an archive, click **Show backups**.
4. Select the backup (recovery point).

> **Important:** The machine with the protection agent (**Machine to browse from**) is the default recovery destination for backups of physical machines.

# Mounting volumes from a backup

Mounting volumes from a disk-level backup lets you access the volumes as though they were physical disks.

Mounting in read/write mode enables you to modify the backup content (save, move, create, delete files/folders, and run executables). In this mode, the software creates an incremental backup containing the changes. None of the subsequent backups will contain these changes.

## Requirements

- Available only in Windows by using File Explorer.
- Agent for Windows must be installed on the machine performing the mount.
- The backed-up file system must be supported by the Windows version running.
- The backup must be stored in a local folder, network share (SMB/CIFS), or Secure Zone.

## Usage scenarios

- **Sharing data** -- Mounted volumes can be shared over the network.
- **"Band-aid" database recovery** -- Mount a volume that contains an SQL database from a recently failed machine to provide access to the database until the failed machine is recovered. Can also be used for granular recovery of Microsoft SharePoint data using SharePoint Explorer.
- **Offline virus removal** -- Mount the backup, clean it with antivirus, then recover from this backup.
- **Error check** -- If a recovery with volume resize failed, mount the backup in read/write mode, check the volume for errors with `chkdsk /r`, then recover.

## To mount a volume from a backup

1. Browse to the backup location using File Explorer.
2. Double-click the backup file (named: `<machine name> - <protection plan GUID>`).
3. If the backup is encrypted, enter the encryption password.
4. Double-click a recovery point to see the backed-up volumes.
5. Right-click a volume and select:
   - **Mount** -- Only the last backup in the archive (backup chain) can be mounted in read-write mode.
   - **Mount in read-only mode**.
6. If on a network share, provide access credentials.

The software mounts the selected volume and assigns the first unused letter.

## To unmount a volume

1. Browse to **Computer** (This PC) in File Explorer.
2. Right-click the mounted volume.
3. Click **Unmount**.
4. [If mounted in read/write mode and content was modified] Choose whether to create an incremental backup containing the changes.

# Validating backups

You can validate a backup to verify that you can recover the data.

1. Select the backed-up workload.
2. Click **Recovery**.
3. Select a recovery point.
4. Click the gear icon, and then click **Validate**.
5. Select the agent that will perform the validation.
6. Select the validation method.
7. If the backup is encrypted, provide the encryption password.
8. Click **Start**.

# Exporting backups

The export operation creates a self-sufficient copy of a backup in the location that you specify. The original backup remains untouched. Exporting allows you to separate a specific backup from a chain of incremental and differential backups for fast recovery, for writing onto removable or detachable media, or for other purposes.

The result of an export operation is always a full backup. The exported backup inherits the encryption settings and password from the original.

## To export a backup

1. Select the backed-up workload.
2. Click **Recovery**.
3. Select a recovery point.
4. Click the gear icon, and then click **Export**.
5. Select the agent that will perform the export.
6. If the backup is encrypted, provide the encryption password.
7. Specify the export destination.
8. Click **Start**.

# Deleting backups

A backup archive contains one or more backups (recovery points). You can delete specific backups in an archive or the whole archive.

Deleting the backup archive deletes all backups in it. Deleting all backups of a workload deletes the backup archives that contain these backups.

## To delete backup archives in the console

1. Go to the **Backup storage** tab, and then select the location.
2. Select the archive.
3. Click **Delete**.
4. Confirm your choice.

## To delete specific recovery points

1. Go to the **Backup storage** tab, and then select the location.
2. Select the archive.
3. Click **Show backups**.
4. Select the recovery point to delete.
5. Click the trash can icon.
6. Confirm your choice.

## To delete all backups of a workload

1. On the **Devices** tab, select the workload whose backups you want to delete.
2. Click **Recovery**.
3. Select the backup location, if there are backups in multiple locations.
4. Click **Delete all**.
5. Confirm your choice.
