---
title: "Bootable media recovery and file recovery"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovery"
page_range: "653-657"
tags: ["bootable-media", "file-recovery", "disk-recovery", "LVM", "APFS", "cloud-storage", "registration-code", "Web-Restore-console", "download-files", "overwrite-options"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#creating-bootable-media.html"
---

# Recovering disks by using bootable media

Running the bootable media requires 1.5 GB of RAM.

> **Note:** You cannot recover disk-level backups of Intel-based Macs to Macs that use Apple silicon processors, and vice-versa. You can recover files and folders.

## To recover disks by using bootable media

1. Boot the target machine by using bootable media.
2. [Only when recovering a Mac] If you are recovering APFS-formatted disks/volumes to a non-original machine or to bare metal, re-create the original disk configuration manually:
   a. Click **Disk Utility**.
   b. Erase and format the target disk into APFS.
   c. Re-create the original disk configuration.
   d. Click **Disk Utility** > **Quit Disk Utility**.
3. Click **Manage this machine locally** or click **Rescue Bootable Media** twice, depending on the media type.
4. If a proxy server is enabled in your network, click **Tools** > **Proxy server**, and specify the proxy server host name/IP address, port, and credentials.
5. [Optional] When recovering Windows or Linux, click **Tools** > **Register media in the Cyber Protection service**, and then specify the registration token. This lets you access cloud storage without entering credentials.
6. On the welcome screen, click **Recover**.
7. Click **Select data**, and then click **Browse**.
8. Specify the backup location:
   - **Cloud storage** -- Enter the credentials of the account to which the backed-up machine is assigned. You can also use a **registration code** instead (click **Use registration code** > **Request the code**; the code is valid for one hour).
   - **Local folders** or **Network folders** -- Browse to the folder.
   - **Public cloud storage** (Azure, Amazon S3, S3-compatible) -- First click **Register media in the Cyber Protection service**, then configure recovery using the web interface.
9. Select the backup from which you want to recover. If prompted, type the password.
10. In **Backup contents**, select the disks to recover. Click **OK**.
11. Under **Where to recover**, the software automatically maps the selected disks to the target disks. Re-map disks manually if needed.

> **Note:** Changing disk layout may affect the operating system bootability. Use the original machine's disk layout unless you feel fully confident of success.

12. [When recovering Linux] If the backed-up machine had logical volumes (LVM) and you want to reproduce the original LVM structure:
    a. Ensure that the number of target machine disks and each disk capacity are equal to or exceed those of the original machine, and then click **Apply RAID/LVM**.
    b. Review the volume structure, and then click **Apply RAID/LVM** to create it.
13. [Optional] Click **Recovery options** to specify additional settings.
14. Click **OK** to start the recovery.

# Recovering files

## Recovering files in the Cyber Protect console

> **Note:** In the Cyber Protect console, you cannot recover backups in tenants in Compliance mode.

1. Select the machine that originally contained the data you want to recover.
2. Click **Recovery**.
3. Select the recovery point. Note that recovery points are filtered by location.
   - If the selected machine is physical and offline, recovery points are not displayed. Use one of these alternatives:
     - Click **Select machine**, select a target machine that is online, and then select a recovery point.
     - Select a recovery point on the **Backup storage** tab.
     - Download the files from the cloud storage.
     - Use bootable media.
4. Click **Recover** > **Files/folders**.
5. Browse to the required folder or use the search bar. Search is language-independent. You can use wildcards (* and ?).

> **Note:** Search is not available for disk-level backups that are stored in the cloud storage.

6. Select the files that you want to recover.
7. If you want to save the files as a .zip file, click **Download**, select the location, and click **Save**. Downloading is not available if your selection contains folders or the total size exceeds 100 MB.
8. Click **Recover**.
9. In **Recover to**, click to select the target for the recovery operation or leave the default target:
   - The source machine (if a protection agent is installed on it)
   - Other machines on which a protection agent is installed (physical machines, virtual machines, virtualization hosts, or virtual appliances). You cannot recover files to VMs on which a protection agent is not installed (except Virtuozzo VMs).
   - Virtuozzo containers or virtual machines (with some limitations)
10. In **Path**, select the recovery destination:
    - The original location (when recovering to the original machine)
    - A local folder or locally attached storage on the target machine (symbolic links are not supported)
    - A network folder that is accessible from the target machine
11. Click **Start recovery**.
12. Select one of the file overwriting options:
    - **Overwrite existing files**
    - **Overwrite an existing file if it is older**
    - **Do not overwrite existing files**

## Downloading files in the Web Restore console

In the Web Restore console, you can browse the cloud storage, view the contents of backups, and download backed-up files and folders.

Web Restore console is only accessible to Customer-level user accounts with the following roles: Company administrator, Protection administrator, Protection user. All accounts can access only their own backups. Partner-level user accounts cannot access the Web Restore console.

### Limitations

- You cannot download backed-up disks, volumes, or whole recovery points.
- When you browse disk-level backups, logical volumes (LVM and LDM) are not shown.
- You cannot browse backups of system state, SQL databases, and Exchange databases.

### To download files and folders from the cloud storage

1. In the Cyber Protection console, select the required workload, and then click **Recovery**.
2. [If multiple backup locations are available] Select the backup location, and then click **More ways to recover**.
3. Click **Download files**.
4. Under **Machines**, click the workload name, and then click the backup archive.
5. Click the backup number (recovery point), and then navigate to the required items.
6. Select the check boxes next to the items you want to download. If you select multiple items, they will be downloaded as a ZIP file.
7. Click **Download**.
