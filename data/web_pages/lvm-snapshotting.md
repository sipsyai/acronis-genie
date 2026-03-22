# LVM snapshotting

Managing the backup and recovery of workloads and files > Backup options > LVM snapshotting
LVM snapshotting

This option is effective only for physical machines.

This option is effective for disk-level backup of volumes managed by Linux Logical Volume Manager (LVM). Such volumes are also called logical volumes.

This option defines how a snapshot of a logical volume is taken. The backup software can do this on its own or rely on Linux Logical Volume Manager (LVM).

The preset is: By the backup software.

By the backup software. The snapshot data is kept mostly in RAM. The backup is faster, and unallocated space on the volume group is not required. Therefore, we recommend that you change the preset only if you are experiencing problems with backing up logical volumes.
By LVM. The snapshot is stored on unallocated space of the volume group. If the unallocated space is missing, the snapshot will be taken by the backup software.

The snapshot is used only during the backup operation, and is automatically deleted when the backup operation completes. No temporary files are kept.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.