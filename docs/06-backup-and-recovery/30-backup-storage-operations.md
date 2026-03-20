---
title: "Backup Storage, Mounting Volumes, Validating, Exporting, and Deleting Backups"
section: "Managing the backup and recovery of workloads and files"
subsection: "Operations with backups"
page_range: "677-684"
tags: [backup-storage, mounting-volumes, validating-backups, exporting-backups, deleting-backups, backup-archives, web-restore]
acronis_version: "26.02"
---

# Operations with Backups

## Backup Storage

The **Backup storage** tab provides access to all backups, including backups of offline workloads, backups of workloads that are no longer registered in the Cyber Protect console, and backups to public clouds, such as Microsoft Azure.

Backups are organized into backup archives. The archives are named according to the following template:

```
<workload name> - <protection plan name>
```

The following archives are orphaned:

- Archives that are no longer associated to a protection plan or cloud backup plan.
- Archives that are no longer associated to a registered workload.

> **Note:** Orphaned backups use storage space and are billed accordingly.

Backups that are stored in a shared location (such as an SMB or NFS share) are visible to all users who have read permissions for that location. It is recommended to restrict read permissions for the locations in which you store backups.

> **Note:** Use backup replication instead of moving backup files manually.

> **Warning!** Do not edit the backup files manually. This might result in file corruption and make the backups unusable. In the Cyber Protect console, corrupted backups are marked as **Unknown**, and you can only delete them. For assistance with corrupted backups, contact the Support team.

### Access Control in Cloud Storage

Access to backups depends on the user role:

- Accounts with the administrator role can access all backups in their tenant or unit.
- Accounts with the user role can only access their own backups.

Backup locations that are used in protection plans are automatically added to the **Backup storage** tab. Cloud-to-cloud backups are shown in **Backup storage** > **Cloud applications backups**.

A backup location (except for the cloud storage) disappears from the **Backup storage** tab if all workloads that are backed up to that location are deleted from the Cyber Protect console. If a new backup to this location occurs, the location is added again with all backups that are stored in it.

### To Manually Add a Backup Location

> **Note:** This operation is available only if you have an online agent.

1. Log in to the Cyber Protect console.
2. Go to the **Backup storage** tab, and then click **Add location**.
3. Select the location type: Local folder, Network folder, Secure Zone, NFS folder, or Public cloud.
4. Configure the location, and then click **Done**.

### To Refresh the Backup Locations

If you manually added or removed backups, you must refresh the location to sync the change with the Cyber Protect console.

1. Log in to the Cyber Protect console.
2. Go to the **Backup storage** tab, and then select a backup location.
3. [Not applicable to Cloud application backups] In **Machine to browse from**, select an online machine.
4. In the **Actions** pane, click **Refresh**.

### To Filter the Backup Archives

1. Log in to the Cyber Protect console.
2. Go to the **Backup storage** tab, and then select a backup location.
3. In the main grid, click the gear icon and enable the columns that you want to see.
4. To filter the backups, click the column name.

### To Select a Backup (Recovery Point)

1. Log in to the Cyber Protect console.
2. Go to the **Backup storage** tab, and then select a backup location. Only backups that you can access are shown.
3. [Not applicable to Cloud application backups] In **Machine to browse from**, select an online machine. Accessing some backups requires a specific agent.

> **Important:** The machine with the protection agent (**Machine to browse from**) is the default recovery destination for backups of physical machines. If you want to recover such a backup to a different machine, select that machine in **Machine to browse from**.

4. Select an archive from which you want to recover the data.
5. Click **Show backups**.
6. Select the backup (recovery point).

## Mounting Volumes from a Backup

Mounting volumes from a disk-level backup lets you access the volumes as though they were physical disks. Mounting volumes in the read/write mode enables you to modify the backup content -- save, move, create, delete files or folders, and run executables consisting of one file. In this mode, the software creates an incremental backup that contains the changes you make to the backup content. Note that none of the subsequent backups will contain these changes.

### Requirements

- Available only in Windows by using File Explorer.
- Agent for Windows must be installed on the machine that performs the mount operation.
- The backed-up file system must be supported by the Windows version that the machine is running.
- The backup must be stored in a local folder, on a network share (SMB/CIFS), or in the Secure Zone.

### Usage Scenarios

- **Sharing data:** Mounted volumes can be easily shared over the network.
- **Band-aid database recovery solution:** Mount a volume that contains an SQL database from a recently failed machine. This will provide access to the database until the failed machine is recovered. This approach can also be used for granular recovery of Microsoft SharePoint data by using SharePoint Explorer.
- **Offline virus removal:** If a machine is infected, mount its backup, clean it with an antivirus program (or find the latest backup that is not infected), and then recover the machine from this backup.
- **Error check:** If a recovery with volume resize has failed, mount the backup in the read/write mode, check the mounted volume for errors using the `chkdsk /r` command. After the errors are fixed and a new incremental backup is created, recover the system from this backup.

### To Mount a Volume from a Backup

1. Browse to the backup location by using File Explorer.
2. Double-click the backup file (named: `<machine name> - <protection plan GUID>`).
3. If the backup is encrypted, enter the encryption password.
4. Double-click the recovery point. File Explorer displays the backed-up volumes.

> **Note:** Double-click a volume to browse its content. You can copy files and folders from the backup to any folder on the file system.

5. Right-click a volume to mount, and then select one of the following options:
   - **Mount** (note: only the last backup in the archive/backup chain can be mounted in read-write mode)
   - **Mount in read-only mode**
6. If the backup is stored on a network share, provide access credentials.

The software mounts the selected volume. The first unused letter is assigned to the volume.

### To Unmount a Volume

1. Browse to **Computer** (**This PC** in Windows 8.1 and later) by using File Explorer.
2. Right-click the mounted volume.
3. Click **Unmount**.
4. [Optional] If the volume was mounted in read/write mode and its content was modified, select whether to create an incremental backup containing the changes.

## Validating Backups

You can validate a backup to verify that you can recover the data.

> **Note:** In service-based billing mode, this feature requires the **Servers** quota to be enabled under Standard Protection as a prerequisite. With solution-based billing mode, this functionality is available in customer tenants that use **Ultimate protection**.

### To Validate a Backup

1. Select the backed-up workload.
2. Click **Recovery**.
3. Select a recovery point (filtered by location). If the workload is offline, use one of the alternative methods to access recovery points (Select machine, Backup storage tab).
4. Click the gear icon, and then click **Validate**.
5. Select the agent that will perform the validation.
6. Select the validation method.
7. If the backup is encrypted, provide the encryption password.
8. Click **Start**.

## Exporting Backups

The export operation creates a self-sufficient copy of a backup in the location that you specify. The original backup remains untouched. Exporting backups allows you to separate a specific backup from a chain of incremental and differential backups for fast recovery, for writing onto removable or detachable media, or for other purposes.

> **Note:** In service-based billing mode, this feature requires the **Servers** quota. With solution-based billing mode, this functionality is available in customer tenants that use **Ultimate protection**.

The result of an export operation is always a full backup. The backup file name is the same as that of the original backup, except for the sequence number. If multiple backups from the same backup chain are exported to the same location, a four-digit sequence number is appended.

The exported backup inherits the encryption settings and password from the original backup. When exporting an encrypted backup, you must specify the password.

### To Export a Backup

1. Select the backed-up workload.
2. Click **Recovery**.
3. Select a recovery point.
4. Click the gear icon, and then click **Export**.
5. Select the agent that will perform the export.
6. If the backup is encrypted, provide the encryption password.
7. Specify the export destination.
8. Click **Start**.

## Deleting Backups

A backup archive contains one or more backups. You can delete specific backups (recovery points) in an archive or the whole archive. Deleting the backup archive deletes all backups in it. Deleting all backups of a workload deletes the backup archives that contain these backups.

> **Note:** Continuous data protection prevents the deletion of backup archives. If you want to manually delete a backup that is created with CDP enabled, you need to revoke or delete the corresponding protection plan first.

> **Warning!** If immutable storage is disabled, backed-up data is permanently deleted and cannot be recovered.

### On the Devices Tab (Online Workloads Only)

1. In the Cyber Protect console, go to **Devices** > **All devices**.
2. Select the workload backups of which you want to delete.
3. Click **Recovery**.
4. [If more than one backup location is available] Select the backup location.
5. [To delete all backups] Click **Delete all** and confirm.
6. [To delete a specific backup] Select the backup, click **Actions** > **Delete**, and confirm.

### On the Backup Storage Tab (Online and Offline Workloads)

1. In the Cyber Protect console, go to **Backup storage**.
2. Select the location from which you want to delete backups.
3. Select the backup archive.
4. [To delete the whole archive] Click **Delete** and confirm.
5. [To delete a specific backup] Click **Show backups**, select the backup, click **Actions** > **Delete**, and confirm.

### In the Web Restore Console (Cloud Storage Only)

1. In the Cyber Protection console, go to **Devices** > **All devices**.
2. Select the workload and click **Recovery**.
3. [If multiple backup locations] Select the backup location, then click **More ways to recover**.
4. Click **Download files** -- you are redirected to the Web Restore console.
5. Under **Machines**, click the workload name.
6. Under **Last version**, click the date, and then click **Delete**.
7. Click **Delete** to confirm.

### Deleting Backups Outside the Cyber Protect Console

If you delete backups using the Web Restore console or using a file manager, you must refresh the backup location in the Cyber Protect console to sync the changes.

1. In the Cyber Protect console, go to **Backup storage**.
2. Select the backup location in which the deleted backups were stored.
3. In the **Actions** pane, click **Refresh**.
