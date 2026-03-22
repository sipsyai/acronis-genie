# Recovering a virtual machine as a physical machine

Managing the backup and recovery of workloads and files > Recovery > Recovery of virtual machines > Recovering a virtual machine as a physical machine
Recovering a virtual machine as a physical machine

You can recover a disk-level backup of a virtual machine to a physical machine. This operation is called cross-platform recovery (machine migration). For more information, see Cross-platform recovery.

The following procedure describes recovery from the Cyber Protect console. Alternatively, you can use bootable media to recover a backup of a virtual machine to a physical machine. For more information, see Recovering disks by using bootable media.

To recover a virtual machine as a physical machine

In the Cyber Protect console, do one of the following:

On the Devices tab, select a backed-up machine, click Recovery, and then select a backup (recovery point).
On the Backup storage tab, select a backup archive, and then select a backup (recovery point).
Click Recover > Entire machine.
[If prompted] Specify the credentials to access the backup storage, and then click OK.

In Recover to, select Physical machine.

A target machine is automatically selected.

To change the target machine:

Click Target machine.
Select an online machine, and then click OK.
[If prompted] Specify the credentials to access the backup storage, and then click OK.

Configure the disk mapping between the backed-up machine and the target machine.

[To configure the mapping on a disk level]

Click Disk mapping.
Configure the disk mapping between the backed-up machine and the target machine.
Click Done.

[To configure the mapping on a volume level]

Click Disk mapping, and then, in the upper-right corner, click Switch to volume mapping.
Configure the volume mapping between the backed-up machine and the target machine.
Click Done.
You can select individual disks or volumes for recovery. Ensure that the disk or volume configuration of the backed-up machine matches exactly the disk or volume configuration of the target machine.

[Only available for Windows machines] To ensure that the recovered data is malware-free, enable the Safe recovery switch. For more information, see Safe recovery.

Click Start recovery

If you prefer to restart the machine manually after the recovery, clear the Automatically restart the machine, if required checkbox. For more information, see Recovery with restart.

To confirm that you want to overwrite the disks of the target machine, click Start recovery.

You can check the recovery progress in the Cyber Protect console, on the Activities tab.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.