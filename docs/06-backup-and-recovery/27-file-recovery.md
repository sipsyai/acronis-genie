---
title: "File Recovery and Verification"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovering files"
page_range: "655-662"
tags: [file-recovery, web-restore, notary-service, asign, bootable-media, system-state, esxi-recovery, extracting-files]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#safe-recovery.html"
---

# Recovering Files

## Recovering Files in the Cyber Protect Console

> **Note:** In the Cyber Protect console, you cannot recover backups in tenants in Compliance mode.

1. Select the machine that originally contained the data that you want to recover.
2. Click **Recovery**.
3. Select the recovery point. Note that recovery points are filtered by location. If the selected machine is physical and it is offline, recovery points are not displayed. Do any of the following:
   - [Recommended] If the backup location is cloud or shared storage, click **Select machine**, select a target machine that is online, and then select a recovery point.
   - Select a recovery point on the Backup storage tab.
   - Download the files from the cloud storage.
   - Use bootable media.
4. Click **Recover** > **Files/folders**.
5. Browse to the required folder or use the search bar to find the required files and folders. Search is language-independent. You can use wildcard characters (* and ?).

> **Note:** Search is not available for disk-level backups that are stored in the cloud storage.

6. Select the files that you want to recover.
7. If you want to save the files as a .zip file, click **Download**, select the location, and click **Save**. Otherwise, skip this step. Downloading is not available if your selection contains folders or the total size exceeds 100 MB.
8. Click **Recover**. In **Recover to**, click to select the target for the recovery operation, or leave the default target. The following targets are available:
   - **The source machine** (if a protection agent is installed on it).
   - **Other machines** on which a protection agent is installed -- physical machines, virtual machines, and virtualization hosts. You cannot recover files to virtual machines on which a protection agent is not installed (except for Virtuozzo virtual machines).
   - **Virtuozzo containers or virtual machines** (with some limitations).
9. In **Path**, select the recovery destination: the original location, a local folder, or a network folder accessible from the target machine.

> **Note:** Symbolic links are not supported.

10. Click **Start recovery**.
11. Select one of the file overwriting options:
    - **Overwrite existing files**
    - **Overwrite an existing file if it is older**
    - **Do not overwrite existing files**

## Downloading Files in the Web Restore Console

In the Web Restore console, you can browse the cloud storage, view the contents of the backups, and download backed-up files and folders. The Web Restore console is only accessible to Customer-level user accounts with the following roles: Company administrator, Protection administrator, Protection user. All accounts can access only their own backups. Partner-level user accounts cannot access the Web Restore console.

### Limitations

- You cannot download backed-up disks, volumes, or whole recovery points.
- When you browse disk-level backups, logical volumes (such as LVM and LDM) are not shown.
- You cannot browse backups of system state, SQL databases, and Exchange databases.

### To download files and folders from the cloud storage

1. In the Cyber Protection console, select the required workload, and then click **Recovery**.
2. [If multiple backup locations are available] Select the backup location, and then click **More ways to recover**.
3. Click **Download files**.
4. Under **Machines**, click the workload name, and then click the backup archive.
5. Click the backup number (recovery point) and navigate to the required items.
6. Select the check boxes next to the items that you want to download.

> **Note:** If you select multiple items, they will be downloaded as a ZIP file.

7. Click **Download**.

## Verifying File Authenticity with Notary Service

If notarization was enabled during backup, you can verify the authenticity of a backed-up file.

1. Select the file as described in the recovery steps above.
2. Ensure that the selected file is marked with the notarized icon.
3. Do one of the following:
   - Click **Verify** -- the software checks the file authenticity and displays the result.
   - Click **Get certificate** -- a certificate confirming the file notarization is opened in a web browser, with instructions for manual verification.

## Signing a File with ASign

ASign is a service that allows multiple people to sign a backed-up file electronically. This feature is available only for file-level backups stored in the cloud storage. Only one file version can be signed at a time.

ASign can be used for electronic signing of: rental/lease agreements, sales contracts, asset purchase agreements, loan agreements, permission slips, financial documents, insurance documents, liability waivers, healthcare documents, research papers, NDAs, offer letters, and more.

### To sign a file version

1. Select the file from the recovery interface.
2. Ensure that the correct date and time is selected on the left panel.
3. Click **Sign this file version**.
4. Specify the password for the cloud storage account.
5. Add other signees by specifying their email addresses.
6. Click **Invite to sign** to send invitations to the signees.
7. Once the process is complete, go to the ASign web page and click **Get document** to download a PDF containing the Signature Certificate and the Audit Trail.

## Recovering Files by Using Bootable Media

Running the bootable media requires 1.5 GB of RAM.

1. Boot the target machine by using the bootable media.
2. Click **Manage this machine locally** or click **Rescue Bootable Media** twice.
3. If a proxy server is enabled, click **Tools** > **Proxy server** and configure the proxy.
4. [Optional] Click **Tools** > **Register media in the Cyber Protection service** and specify the registration token.
5. On the welcome screen, click **Recover**.
6. Click **Select data**, and then click **Browse**.
7. Specify the backup location (Cloud storage, Local folders, Network folders, or public cloud).
8. Select the backup from which you want to recover the data. If prompted, type the password.
9. In **Backup contents**, select **Folders/files**.
10. Select the data that you want to recover. Click **OK**.
11. Under **Where to recover**, specify a folder. Optionally, prohibit overwriting or exclude files from recovery.
12. [Optional] Click **Recovery options** to specify additional settings.
13. Click **OK** to start the recovery.

## Extracting Files from Local Backups

You can browse the contents of backups and extract files that you need using Windows File Explorer.

### Requirements

- Available only in Windows using File Explorer.
- Supported file systems: FAT16, FAT32, NTFS, ReFS, Ext2, Ext3, Ext4, XFS, or HFS+.

### Prerequisites

- A protection agent must be installed on the machine from which you browse a backup.
- The backup must be stored in a local folder or on a network share (SMB/CIFS).

### To extract files from a backup

1. Browse to the backup location by using File Explorer.
2. Double-click the backup file (named: `<machine name> - <protection plan GUID>`).
3. If the backup is encrypted, enter the encryption password.
4. Double-click the recovery point.
5. Browse to the required folder.
6. Copy the required files to any folder on the file system.

## Limitations for Recovering Files in the Cyber Protect Console

### Tenants in Compliance Mode

You cannot recover backups in tenants in Compliance mode from the Cyber Protect console.

### Recovery to Virtuozzo Containers or Virtual Machines

- QEMU Guest Agent must be installed on the target virtual machine.
- [Containers only] Mount points inside containers cannot be used as target for recovery.
- When recovering files to a Windows VM with "File-level security" recovery option enabled, the archive bit attribute is set on the recovered files.
- Files with non-ANSI characters in their names are recovered with incorrect names on machines running Windows Server 2012 or older.
- To recover files to CentOS or Red Hat Enterprise Linux VMs that run on Virtuozzo Hybrid Server, you must edit the `qemu-ga` file at `/etc/sysconfig/`, clear the `BLACKLIST_RPC=` line, and restart the QEMU Guest Agent: `systemctl restart qemu-guest-agent`.

## Recovering System State

1. Select the machine for which you want to recover the system state.
2. Click **Recovery**.
3. Select a system state recovery point (filtered by location).
4. Click **Recover system state**.
5. Confirm that you want to overwrite the system state with its backed-up version.

## Recovering ESXi Configuration

To recover an ESXi configuration, you need Linux-based bootable media.

If you are recovering to a non-original host and the original ESXi host is still connected to the vCenter Server, disconnect and remove this host from the vCenter Server to avoid unexpected issues during the recovery.

> **Note:** The virtual machines running on the host are not included in an ESXi configuration backup. They can be backed up and recovered separately.

### To recover an ESXi configuration

1. Boot the target machine by using the bootable media.
2. Click **Manage this machine locally**.
3. On the welcome screen, click **Recover**.
4. Click **Select data**, and then click **Browse**.
5. Specify the backup location (Local folders or Network folders). Click **OK**.
6. In **Show**, select **ESXi configurations**.
7. Select the backup to recover. If prompted, type the password.
8. Click **OK**.
9. In **Disks to be used for new datastores**:
   - Under **Recover ESXi to**, select the disk for the host configuration recovery.
   - [Optional] Under **Use for new datastore**, select the disks for new datastores (be careful -- all data on selected disks will be lost).
10. If new datastore disks are selected, select the datastore creation method: **Create one datastore per disk** or **Create one datastore on all selected HDDs**.
11. [Optional] In **Network mapping**, change the mapping of virtual switches to physical network adapters.
12. [Optional] Click **Recovery options** to specify additional settings.
13. Click **OK** to start the recovery.
