# NIC teaming support

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > NIC teaming support
NIC teaming support

Teaming (bonding) of network interface cards (NICs) is preserved both during the recovery of a workload with teamed NICs, and after the recovery.

Network configuration, including NIC teaming, is not preserved when you recover to dissimilar hardware.

You can disable NIC teaming during recovery, if you recover a workload in any of the following ways:

With downloaded bootable media
With Linux-based bootable that is created in Bootable media builder
Via Acronis Startup Recovery Manager
Via one-click recovery
Via recovery with restart, by using the Linux recovery environment

To disable NIC teaming during recovery

On the backed-up machine, open the following configuration file for editing:

Windows:

C:\Program Files\Common Files\Acronis\BackupAndRecoveryAgent\bootagent_msp64.config

Linux:

/usr/lib/Acronis/BackupAndRecoveryAgent/bootagent_msp64.config

In the configuration file, find the following line:

Windows:

<kernel64 name="kernel64.dat" value="product=bootagent media_for_windows" target="abr64ker.dat"/>

Linux:

<kernel64 name="kernel64.dat" value="product=bootagent media_for_linux" target="abr64ker.dat"/>

Edit the line as follows:

Windows

<kernel64 name="kernel64.dat" value="product=bootagent DONT_CREATE_BONDING=1 media_for_windows" target="abr64ker.dat"/>

Linux

<kernel64 name="kernel64.dat" value="product=bootagent DONT_CREATE_BONDING=1 media_for_linux" target="abr64ker.dat"/>

Save the configuration file.

Recover the workload by using any of the supported ways.

As a result, NIC teaming will not be used during recovery.

The recovered workload retains NIC teaming. To disable NIC teaming after recovery, reconfigure the network settings of the workload.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.