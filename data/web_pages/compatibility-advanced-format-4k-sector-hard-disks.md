# Compatibility with Advanced Format (4K-sector) hard disks

Managing the backup and recovery of workloads and files > Supported operating systems and environments for backup and recovery > Compatibility with Advanced Format (4K-sector) hard disks
Compatibility with Advanced Format (4K-sector) hard disks

Backup and recovery are supported on traditional hard disks with 512-byte sector size, and on Advanced Format disks with 4096-byte sector size.

When you recover data from one disk to another, both disks must have the same logical sector size (this is the size that is presented to the operating system). The volumes on the disk are automatically aligned, if necessary. Thus, the start of a cluster in the file system always matches the start of a physical sector on the disk.

International Disk Drive Equipment and Materials Association (IDEMA) specifies two types of Advanced Format disks:

512-byte emulation (512e) disks

These disks have a 512-byte logical sector size.

4K native (4Kn) disks

These disks have a 4096-byte logical sector size.

4Kn disks are commonly used as external drives with USB connection. System boot might not be supported with these disks.

For more information about Advanced Format, see https://idema.org/initiatives/advanced-format.

To check the logical sector size of a disk

Windows
Linux
Ensure that the disk contains an NTFS volume.

Run the following command as an administrator, specifying the drive letter of the NTFS volume (for example, D):

fsutil fsinfo ntfsinfo D:

Check the value in the Bytes Per Sector line.

For example:

Bytes Per Sector: 512
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.