# Selecting disks or volumes

Managing the backup and recovery of workloads and files > Selecting data to back up > Selecting disks or volumes
Selecting disks or volumes

A disk-level backup contains a copy of a disk or a volume in a packaged form. From a disk-level backup, you can recover disks, volumes, folders, and files.

You can select the disks or volumes to back up for each individual workload in the protection plan (direct selection) or you can configure policy rules for multiple workloads. Additionally, you can exclude specific files from a backup, or include only specific files to it, by configuring file filters. For more information, see File filters (Inclusions/Exclusions).

To select disks or volumes

Direct selection
By policy rules

Direct selection is available only for physical machines.

In What to back up, select Disks/volumes.
Click Items to back up.
In Select items for backup, select Directly.
For each of the workloads included in the protection plan, select the check boxes next to the disks or volumes to back up.
Click Done.
Limitations

Disk-level backups are not supported for encrypted APFS volumes that are locked. During a backup of an entire machine, such volumes are skipped.

You cannot recover the content of the OneDrive root folder from an Entire machine or Disk/volumes backup, even though the OneDrive folder is shown when browsing the backup archive in a file manager app, such as File Explorer. When browsing the archive in the Cyber Protect console, the OneDrive folder is not shown. When browsing the archive in the Web Restore console, the OneDrive folder is shown as a file but recovery from this backup is not possible.

To be able to recover the content of the OneDrive folder, create a Files/folders backup. Files that are not available on the device will be shown in the archive, but cannot be recovered.

You can back up disks that are connected via the iSCSI protocol to a physical machine. However, limitations apply if you use Agent for VMware or Agent for Hyper-V for backing up the iSCSI-connected disks. For more information, see Limitations.

What does a disk or volume backup store?

Policy rules for disks and volumes

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.