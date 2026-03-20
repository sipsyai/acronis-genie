---
title: "Selecting data to back up"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup"
page_range: "519-525"
tags: ["backup-selection", "entire-machine", "disks", "volumes", "files", "folders", "system-state", "ESXi", "policy-rules", "direct-selection", "OneDrive", "APFS"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#selecting-data-to-back-up.html"
---

# Selecting data to back up

## Selecting entire machine

A backup of an entire machine is a backup of all its non-removable disks.

### Limitations

- Disk-level backups are not supported for encrypted APFS volumes that are locked. During a backup of an entire machine, such volumes are skipped.
- You cannot recover the content of the OneDrive root folder from an **Entire machine** or **Disk/volumes** backup. To recover OneDrive content, create a **Files/folders** backup.

## Selecting disks or volumes

A disk-level backup contains a copy of a disk or a volume in a packaged form. From a disk-level backup, you can recover disks, volumes, folders, and files.

### To select disks or volumes

**Direct selection** (available only for physical machines):

1. In **What to back up**, select **Disks/volumes**.
2. Click **Items to back up**.
3. In **Select items for backup**, select **Directly**.
4. For each workload, select the check boxes next to the disks or volumes to back up.
5. Click **Done**.

**By policy rules:**

1. In **What to back up**, select **Disks/volumes**.
2. Click **Items to back up**.
3. In **Select items for backup**, select **Using policy rules**.
4. Select any of the predefined rules, type your own rules, or combine both.
5. Click **Done**.

### What does a disk or volume backup store?

A disk or volume backup stores a disk or a volume **file system** as a whole, including all information necessary for the operating system to boot.

With **sector-by-sector (raw mode)** enabled, a disk backup stores all the disk sectors. This can be used for backing up disks with unrecognized or unsupported file systems.

**Windows:** A volume backup stores all files and folders (including hidden and system files), the boot record, the FAT if it exists, the root and the zero track with the master boot record (MBR). A disk backup stores all volumes (including hidden and maintenance partitions) and the zero track with the master boot record.

Items **not** included in a disk or volume backup:
- The swap file (pagefile.sys) and the hibernation file (hiberfil.sys) -- they will be re-created with zero size after recovery.
- Windows shadow storage (the path is determined by the registry value **VSS Default Provider** at `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\BackupRestore\FilesNotToBackup`). This means Windows Restore Points are not backed up (starting with Windows Vista).
- If **Volume Shadow Copy Service (VSS)** backup option is enabled, files and folders specified in `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\BackupRestore\FilesNotToSnapshot`.

**Linux:** A volume backup stores all files and directories, a boot record, and the file system super block. A disk backup stores all disk volumes as well as the zero track with the master boot record.

**Mac:** A disk or volume backup stores all files and directories plus a description of the volume layout. Excluded items: system metadata (file system journal and Spotlight index), the Trash, and Time machine backups. Mac disks/volumes are backed up at a file level. Bare metal recovery from disk and volume backups is possible, but sector-by-sector backup mode is not available.

## Policy rules for disks and volumes

### Windows

- `[All Volumes]` -- selects all volumes on the machine.
- Drive letter (e.g., `C:\`) -- selects the volume with the specified drive letter.
- `[Fixed Volumes (physical machines)]` -- selects all volumes of a physical machine, other than removable media. Includes volumes on iSCSI, SCSI, ATAPI, ATA, SSA, SAS, and SATA devices, and on RAID arrays.
- `[BOOT+SYSTEM]` -- selects the system and boot volumes (minimal combination from which you can recover an operating system).
- `[Disk 1]` -- selects the first disk of the machine, including all volumes on that disk.

### Linux

- `[All Volumes]` -- selects all mounted volumes on the machine.
- `/dev/hda1` -- selects the first volume on the first IDE hard disk.
- `/dev/sda1` -- selects the first volume on the first SCSI hard disk.
- `/dev/md1` -- selects the first software RAID hard disk.
- To select other basic volumes, specify `/dev/xdyN`, where:
  - "x" = disk type, "y" = disk number (a for first, b for second), "N" = volume number.
- To select a logical volume, specify its path as it appears after running `ls /dev/mapper` under the root account. For example: `/dev/mapper/vg_1-lv1`

### macOS

- `[All Volumes]` -- selects all mounted volumes on the machine.
- `[Disk 1]` -- selects the first disk including all volumes on that disk.

## Selecting files or folders

Use file-level backup to protect only specific data. File-level backups are smaller than disk-level backups and save storage space.

> **Important:** You cannot recover an operating system from a file-level backup.

### To select files or folders

**Direct selection:**

1. In **What to back up**, select **Files/folders**.
2. In **Items to back up**, click **Specify**.
3. In **Select items for backup**, select **Directly**.
4. Specify the files or folders to back up:
   - Click **Select files and folders**, or click **Local folder** or **Network folder**.
   - You can select a combination of up to 1,000 files and folders.
   - For shared folders, specify the user name and password (anonymous access is not supported).
5. Click **Done**.

**By policy rules:**

1. In **What to back up**, select **Files/folders**.
2. In **Items to back up**, click **Specify**.
3. In **Select items for backup**, select **Using policy rules**.
4. Select predefined rules, type your own rules, or combine both.
5. Click **Done**.

### Limitations

- File-level backup is available only for physical machines or virtual machines with an agent installed (agent-based backup). It is not available in agentless mode.
- You cannot recover the OneDrive root folder content from an **Entire machine** or **Disk/volumes** backup. Create a **Files/folders** backup for OneDrive content.
- You can back up files on iSCSI-connected disks. Some limitations apply if you use Agent for VMware or Agent for Hyper-V.

## Policy rules for files and folders

### Windows

- Full path to a file or folder (e.g., `D:\Work\Text.doc` or `C:\Windows`).
- Predefined rules:
  - `[All Files]` -- selects all files on all volumes.
  - `[All Profiles Folder]` -- selects the folder where all user profiles are located (e.g., `C:\Users`).
- Environment variables:
  - `%ALLUSERSPROFILE%` -- common data of all user profiles (e.g., `C:\ProgramData`).
  - `%PROGRAMFILES%` -- the Program Files folder.
  - `%WINDIR%` -- the Windows folder.
  - You can combine variables with text (e.g., `%PROGRAMFILES%\Java`).

### Linux

- Full path to a file or directory (e.g., `/dev/hda3/file.txt` or `/home/usr/docs/file.txt`).
- Predefined rules:
  - `[All Profiles Folder]` -- selects `/home`.
  - `/home` -- home directory of the common users.
  - `/root` -- root user's home directory.
  - `/usr` -- directory for user-related programs.
  - `/etc` -- system configuration files.

### macOS

- Full path to a file or directory.
- Predefined rules:
  - `[All Profiles Folder]` -- selects `/Users`.

## Selecting system state

System state backup is available for machines running Windows 7 or later on which Agent for Windows is installed. It is not available for virtual machines backed up at the hypervisor level (agentless backup).

To back up system state, in **What to back up**, select **System state**.

A system state backup is comprised of:
- Task scheduler configuration
- VSS Metadata Store
- Performance counter configuration information
- MSSearch Service
- Background Intelligent Transfer Service (BITS)
- The registry
- Windows Management Instrumentation (WMI)
- Component Services Class registration database

## Selecting ESXi configuration

A backup of an ESXi host configuration enables you to recover an ESXi host to bare metal. The recovery is performed under bootable media. The virtual machines running on the host are not included; they can be backed up and recovered separately.

An ESXi host configuration backup includes:
- The bootloader and boot bank partitions of the host
- The host state (configuration of virtual networking and storage, SSL keys, server network settings, and local user information)
- Extensions and patches installed or staged on the host
- Log files

### Prerequisites

- SSH must be enabled in the **Security Profile** of the ESXi host configuration.
- You must know the password for the 'root' account on the ESXi host.

### Limitations

- ESXi configuration backup is not supported for hosts running VMware ESXi 7.0 and later.
- An ESXi configuration cannot be backed up to the cloud storage.

### To select an ESXi configuration

1. Click **Devices** > **All devices**, and select the ESXi hosts to back up.
2. Click **Protect**.
3. In **What to back up**, select **ESXi configuration**.
4. In **ESXi 'root' password**, specify the password for each selected host or apply the same password to all.
