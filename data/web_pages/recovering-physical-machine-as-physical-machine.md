# Recovering a physical machine as a physical machine

Managing the backup and recovery of workloads and files > Recovery > Recovery of physical machines > Recovering a physical machine as a physical machine
Recovering a physical machine as a physical machine

You can recover a disk-level backup of a physical machine to the original machine or to a new machine.

This procedure describes recovery from the Cyber Protect console. Alternatively, you can use bootable media to recover a backup (including a backup of an offline machine) to a physical machine. For more information, see Recovering disks by using bootable media.

To recover a physical machine as a physical machine

In the Cyber Protect console, do one of the following:

[For online machines] On the Devices tab, select a backed-up machine, click Recovery, and then select a backup (recovery point).

The recovery points are filtered by backup storage.

[For online and offline machines] On the Backup storage tab, select a backup archive, and then select a backup (recovery point).

[For offline machines] [If the backup location is the cloud storage or a shared storage that other agents can access]

On the Devices tab, select a backed-up machine, and then click Recovery.
Click Select machine, select a target machine that is online, and then click OK.
Select a backup (recovery point).

Click Recover > Entire machine.

A target machine is automatically selected.

[If prompted] Specify the credentials to access the backup storage, and then click OK.

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

[Only available for Windows machines] To ensure that the recovered data is malware-free, enable the Safe recovery switch. For more information, see Safe recovery.

Click Start recovery.

If you prefer to restart the machine manually after the recovery, clear the Automatically restart the machine, if required checkbox. For more information, see Recovery with restart.

To confirm that you want to overwrite the disks of the target machine, click Start recovery.

You can check the recovery progress in the Cyber Protect console, on the Activities tab.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.