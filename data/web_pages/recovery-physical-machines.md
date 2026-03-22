# Recovery of physical machines

Managing the backup and recovery of workloads and files > Recovery > Recovery of physical machines
Recovery of physical machines

You can recover a disk-level backup of a physical machine to another physical machine or to a virtual machine. For example, a disk-level backup is an Entire machine backup or a Disk/volumes backup that contains the system disk and boot disk.

Limitations

In the Cyber Protect console, you cannot recover backups of machines that are registered in customer tenants in Compliance mode. See Recovering backups in tenants in Compliance mode.

In the Cyber Protect console, you cannot recover backups of macOS physical machines to another physical machine.
You cannot recover backups of macOS physical machines to a virtual machine.
During a recovery to a virtual machine, Cyber Protect stops the target virtual machine without a prompt. After the recovery, you must restart this machine manually. You can change the default behavior in Recovery options > VM power management.

If you want to recover one of the following, use bootable media instead of the Cyber Protect console:

A physical machine running macOS.

You cannot recover disk-level backups of Intel-based Macs to Macs that use Apple silicon processors, and vice-versa. You can recover files and folders.
A machine in a customer tenant in Compliance mode.
Any operating system to a bare metal machine or to an offline machine.
The structure of logical volumes. For example, volumes created by Logical Volume Manager in Linux). With the bootable media, you can automatically recreate the logical volume structure.

For more information about recovering machines by bootable media, see Recovering disks by using bootable media.

Recovering a physical machine as a physical machine

Recovering a physical machine as a virtual machine

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.