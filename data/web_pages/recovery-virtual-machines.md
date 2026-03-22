# Recovery of virtual machines

Managing the backup and recovery of workloads and files > Recovery > Recovery of virtual machines
Recovery of virtual machines

You can recover a disk-level backup of a virtual machine to a physical machine or another virtual machine. For example, a disk-level backup is an Entire machine backup or a Disk/volumes backup that contains the system disk and boot disk.

Limitations

In the Cyber Protect console, you cannot recover backups of machines that are registered in customer tenants in Compliance mode. See Recovering backups in tenants in Compliance mode.

During a recovery to a virtual machine, Cyber Protect stops the target virtual machine without a prompt. After the recovery, you must restart this machine manually. You can change the default behavior in Recovery options > VM power management.
You can recover a backup of a virtual machine to a physical machine if the disk configuration of the target machine exactly matches the disk configuration in the backup. Alternatively, you can perform a virtual-to-physical migration by using bootable media. See Recovering disks by using bootable media.
You cannot recover macOS virtual machines to Hyper-V hosts because Hyper-V does not support macOS. You can recover macOS virtual machines to a VMware host that is installed on Mac hardware.

See also
Running a virtual machine from a backup (Instant Restore)

Recovering a virtual machine as a physical machine

Recovering a virtual machine as a virtual machine

Recovering containers

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.