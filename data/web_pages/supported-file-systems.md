# Supported file systems

Managing the backup and recovery of workloads and files > Supported operating systems and environments for backup and recovery > Supported file systems
Supported file systems

A protection agent can back up any file system that is accessible from the operating system where the agent is installed. For example, Agent for Windows can back up and recover an ext4 file system if the corresponding driver is installed in Windows.

The following table summarizes the file systems that can be backed up and recovered (bootable media supports only recovery). The limitations apply to both the agents and bootable media.

File system	Supported by	Limitations


Agents



Bootable media for Windows and Linux



Bootable media for Mac


FAT16/32	All agents*

+



+

No limitations
NTFS	All agents

+



+


ext2/ext3/ext4	All agents

+



-


HFS+	Agent for Mac	-	+
APFS	Agent for Mac	-	+
Supported starting with macOS High Sierra 10.13
Disk configuration should be re-created manually when recovering to a non-original machine or bare metal.

JFS	Agent for Linux	+	-

File filters (Inclusions/Exclusions) are not supported

Fast incremental/ differential backup cannot be enabled

ReiserFS3	Agent for Linux	+

-


ReiserFS4	Agent for Linux	+	-
File filters (Inclusions/Exclusions) are not supported
Fast incremental/ differential backup cannot be enabled
Volumes cannot be resized during a recovery

ReFS	All agents	+	+
File filters (Inclusions/Exclusions) are not supported
Fast incremental/ differential backup cannot be enabled
Volumes cannot be resized during a recovery
During a file recovery from a ReFS backup, only the content is recovered. Access-control lists (ACL) and alternate streams are not recovered. Sparse files are recovered as regular files.

XFS	All agents	+	+
File filters (Inclusions/Exclusions) are not supported
Fast incremental/ differential backup cannot be enabled
Volumes cannot be resized during a recovery

The fast-incremental backup mode is not supported for the XFS file system. Incremental and differential backups of XFS volumes to the cloud may be significantly slower than comparable ext4 backups that use the fast-incremental mode.


Linux swap	Agent for Linux	+	-	No limitations
exFAT	All agents

+

Bootable media cannot be used for recovery if the backup is stored on exFAT

+
Only disk/volume backup is supported
File filters (Inclusions/Exclusions) are not supported
Individual files cannot be recovered from a backup

*On Windows XP systems, Agent for Windows supports only NTFS-formatted drives.

The software automatically switches to the sector-by-sector mode when backing up drives with unrecognized or unsupported file systems (for example, Btrfs). A sector-by-sector backup is possible for any file system that:

is block-based
spans a single disk
has a standard MBR/GPT partitioning scheme

If the file system does not meet these requirements, the backup fails.

Data Deduplication

In Windows Server 2012 and later, you can enable the Data Deduplication feature for an NTFS volume. Data Deduplication reduces the used space on the volume by storing duplicate fragments of the volume's files only once.

You can back up and recover a data deduplication–enabled volume at a disk level, without limitations. File-level backup is supported, except when using Acronis VSS Provider. To recover files from a disk backup, either run a virtual machine from your backup, or mount the backup on a machine running Windows Server 2012 or later, and then copy the files from the mounted volume.

The Data Deduplication feature of Windows Server is unrelated to the Acronis Backup Deduplication feature.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.