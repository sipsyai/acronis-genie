# Policy rules for disks and volumes

Managing the backup and recovery of workloads and files > Selecting data to back up > Selecting disks or volumes > Policy rules for disks and volumes
Policy rules for disks and volumes

When you select disks or volumes to back up, you can use the following policy rules, according to the operating system of the protected workload.

Windows
Linux
macOS
[All Volumes] selects all volumes on the machine.
Drive letter (for example, C:\) selects the volume with the specified drive letter.
[Fixed Volumes (physical machines)] selects all volumes of a physical machine, other than removable media. Fixed volumes include volumes on iSCSI, SCSI, ATAPI, ATA, SSA, SAS, and SATA devices, and on RAID arrays.
[BOOT+SYSTEM] selects the system and boot volumes. This is the minimal combination from which you can recover an operating system.
[Disk 1] selects the first disk of the machine, including all volumes on that disk. To select another disk, type the corresponding number.
See also
Selecting disks or volumes



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.