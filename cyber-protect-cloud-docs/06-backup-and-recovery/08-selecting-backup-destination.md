---
title: "Selecting a backup destination"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup"
page_range: "526-530"
tags: ["backup-destination", "cloud-storage", "local-folder", "network-folder", "NFS", "Secure-Zone", "public-cloud", "script-defined", "SMB", "CIFS", "DFS"]
acronis_version: "26.02"
---

# Selecting a backup destination

Click **Where to back up**, and then select one of the following destinations:

## Cloud storage

Backups will be stored in the cloud data center.

> **Note:** Backups to public cloud require a **Local backup** storage quota.

## Local folders

If a single machine is selected, browse to a folder on the selected machine or type the folder path. If multiple machines are selected, type the folder path. Backups will be stored in this folder on each of the selected physical machines or on the machine where the agent for virtual machines is installed. If the folder does not exist, it will be created.

## Network folder

This is a folder shared via SMB/CIFS/DFS. Browse to the required shared folder or enter the path in the following format (where `<host>` is a full DNS domain name or an IPv4 address):

- **SMB/CIFS shares:**
  - `\\<host>\<path>\`
  - `smb://<host>/<path>/`
- **DFS shares:**
  - `\\<host>\<DFS root>\<path>`

Then, click the arrow button. If prompted, specify the user name and password for the shared folder. You can change these credentials at any time by clicking the key icon next to the folder name.

> **Note:** Backing up to a folder with anonymous access is not supported.

## Public cloud

This option is available if the **Direct Backup to Public Cloud** feature is enabled for your tenant. It enables you to configure a direct backup to a public cloud compatible storage (such as Microsoft Azure), without the need to deploy additional components. Select and connect to the relevant public cloud, as required.

> **Note:** Backups to public cloud require a **Local backup** storage quota.

## NFS folder

Available for machines running Linux or macOS. Verify that the `nfs-utils` package is installed on the Linux server where the Agent for Linux is installed.

Browse to the required NFS folder or enter the path in the following format:

```
nfs://<host>/<exported folder>:/<subfolder>
```

> **Note:** It is not possible to back up to an NFS folder protected with a password.

## Secure Zone

Available if it is present on each of the selected machines. Secure Zone is a secure partition on a disk of the backed-up machine. This partition has to be created manually prior to configuring a backup.

## Advanced storage option: Defined by a script

> **Note:** This functionality is available only in the Advanced edition of the Cyber Protection service.

**Defined by a script** (available for machines running Windows)

You can store each machine's backups in a folder defined by a script. The software supports scripts written in JScript, VBScript, or Python 3.5. When deploying the protection plan, the software runs the script on each machine. The script output for each machine should be a local or network folder path. If a folder does not exist, it will be created (limitation: scripts written in Python cannot create folders on network shares). On the **Backup storage** tab, each folder is shown as a separate backup location.

In **Script type**, select the script type (**JScript**, **VBScript**, or **Python**), and then import, or copy and paste the script. For network folders, specify access credentials with read/write permissions.

**Example JScript** (backup to `\\bkpsrv\<machine name>`):
```javascript
WScript.Echo("\\\\bkpsrv\\" + WScript.CreateObject("WScript.Network").ComputerName);
```

**Example JScript** (backup to a local folder):
```javascript
WScript.Echo("C:\\Backup");
```

> **Note:** The location path in these scripts is case-sensitive. `C:\Backup` and `C:\backup` are displayed as different locations in the Cyber Protect console. Also, use upper case for the drive letter.

## About Secure Zone

Secure Zone is a secure partition on a disk of the backed-up machine. It can store backups of disks or files of this machine.

Should the disk experience a physical failure, the backups located in the Secure Zone may be lost. That is why Secure Zone should not be the only location where a backup is stored. In enterprise environments, Secure Zone can be thought of as an intermediate location used for backup when an ordinary location is temporarily unavailable or connected through a slow or busy channel.

### Why use Secure Zone?

- Enables recovery of a disk to the same disk where the disk's backup resides.
- Offers a cost-effective method for protecting data from software malfunction, virus attack, human error.
- Eliminates the need for a separate media or network connection to back up or recover data (useful for roaming users).
- Can serve as a primary destination when using replication of backups.

### Limitations

- Secure Zone cannot be organized on a Mac.
- Secure Zone is a partition on a basic disk. It cannot be organized on a dynamic disk or created as a logical volume (managed by LVM).
- Secure Zone is formatted with FAT32. Because FAT32 has a 4-GB file size limit, larger backups are split when saved to Secure Zone. This does not affect the recovery procedure and speed.

### How creating Secure Zone transforms the disk

- Secure Zone is always created at the end of the hard disk.
- If there is no or not enough unallocated space at the end of the disk, but there is unallocated space between volumes, the volumes will be moved to add more unallocated space to the end.
- When all unallocated space is collected but is still not enough, the software will take free space from the volumes you select, proportionally reducing the volumes' size.
- The software will not decrease a volume where free space is or becomes less than 25 percent of the total volume size.
- Moving or resizing the volume from which the system is booted requires a reboot.

> **Important:** Specifying the maximum possible Secure Zone size is not advisable. You will end up with no free space on any volume, which might cause the operating system or applications to work unstably and even fail to start.

### How to create Secure Zone

1. Select the machine that you want to create Secure Zone on.
2. Click **Details** > **Create Secure Zone**.
3. Under **Secure Zone disk**, click **Select**, and then select a hard disk. The software calculates the maximum possible size.
4. Enter the Secure Zone size or drag the slider (minimum ~50 MB; maximum = disk's unallocated space + total free space on all volumes).
5. If all unallocated space is not enough, the software will take free space from existing volumes. Click **Select volumes** to exclude some volumes if desired.
6. [Optional] Enable the **Password protection** switch and specify a password.
7. Click **Create**. The software displays the expected partition layout. Click **OK**.
8. Wait while the software creates Secure Zone.

### How to delete Secure Zone

1. Select a machine with Secure Zone.
2. Click **Details**.
3. Click the gear icon next to **Secure Zone**, and then click **Delete**.
4. [Optional] Specify the volumes to which the freed space will be added (by default, all volumes are selected).
5. Click **Delete**.
