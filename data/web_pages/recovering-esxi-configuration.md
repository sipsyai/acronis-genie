# Recovering ESXi configuration

Managing the backup and recovery of workloads and files > Recovery > Recovering ESXi configuration
Recovering ESXi configuration

To recover an ESXi configuration, you need Linux-based bootable media. For information about how to create bootable media, refer to Creating physical bootable media.

If you are recovering an ESXi configuration to a non-original host and the original ESXi host is still connected to the vCenter Server, disconnect and remove this host from the vCenter Server to avoid unexpected issues during the recovery. If you want to keep the original host along with the recovered one, you can add it again after the recovery is complete.

The virtual machines running on the host are not included in an ESXi configuration backup. They can be backed up and recovered separately.

To recover an ESXi configuration

Boot the target machine by using the bootable media.
Click Manage this machine locally.
On the welcome screen, click Recover.
Click Select data, and then click Browse.

Specify the backup location:

Browse to the folder under Local folders or Network folders.

Click OK to confirm your selection.

In Show, select ESXi configurations.
Select the backup from which you want to recover the data. If prompted, type the password for the backup.
Click OK.

In Disks to be used for new datastores, do the following:

Under Recover ESXi to, select the disk where the host configuration will be recovered. If you are recovering the configuration to the original host, the original disk is selected by default.
[Optional] Under Use for new datastore, select the disks where new datastores will be created. Be careful because all data on the selected disks will be lost. If you want to preserve the virtual machines in the existing datastores, do not select any disks.
If any disks for new datastores are selected, select the datastore creation method in How to create new datastores: Create one datastore per disk or Create one datastore on all selected HDDs.
[Optional] In Network mapping, change the result of automatic mapping of the virtual switches present in the backup to the physical network adapters.
[Optional] Click Recovery options to specify additional settings.
Click OK to start the recovery.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.