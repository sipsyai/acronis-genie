# Recovering files in the Cyber Protect console

Managing the backup and recovery of workloads and files > Recovery > Recovering files > Recovering files in the Cyber Protect console
Recovering files in the Cyber Protect console

In the Cyber Protect console, you cannot recover backups in tenants in Compliance mode. See Recovering backups in tenants in Compliance mode.

Select the machine that originally contained the data that you want to recover.
Click Recovery.

Select the recovery point. Note that recovery points are filtered by location.

If the selected machine is physical and it is offline, recovery points are not displayed. Do any of the following:

[Recommended] If the backup location is cloud or shared storage (i.e. other agents can access it), click Select machine, select a target machine that is online, and then select a recovery point.
Select a recovery point on the Backup storage tab.
Download the files from the cloud storage.
Use bootable media.
Click Recover > Files/folders.

Browse to the required folder or use the search bar to obtain the list of the required files and folders.

Search is language-independent.

You can use one or more wildcard characters (* and ?). For more details about using wildcards, refer to File filters (Inclusions/Exclusions).

Search is not available for disk-level backups that are stored in the cloud storage.

Select the files that you want to recover.

If you want to save the files as a .zip file, click Download, select the location to save the data to, and click Save. Otherwise, skip this step.

Downloading is not available if your selection contains folders or the total size of the selected files exceeds 100 MB. To retrieve larger amounts of data from the cloud, use the procedure Downloading files in the Web Restore console.

Click Recover.

In Recover to, click to select the target for the recovery operation, or leave the default target. The default target varies according to the source of the backup.

The following targets are available:

The source machine (if a protection agent is installed on it).

This is the machine that originally contained the files that you want to recover.

Other machines on which a protection agent is installed – physical machines, virtual machines, and virtualization hosts on which a protection agent is installed, or virtual appliances.

You can recover files to physical machines, virtual machines, and virtualization hosts on which a protection agent is installed. You cannot recover files to virtual machines on which a protection agent is not installed (except for Virtuozzo virtual machines).

Virtuozzo containters or virtual machines.

You can recover files to Virtuozzo containers and virtual machines with some limitations. For more information about them, refer to Limitations for recovering files in the Cyber Protect console.

In Path, select the recovery destination. You can select one of the following:

[When recovering to the original machine] The original location.

A local folder or locally attached storage on the target machine.

Symbolic links are not supported.

A network folder that is accessible from the target machine.

For example, when recovering files from a Microsoft Azure virtual machine, the network folder must be accessible to the Agent for Azure deployed on the virtual machine.

Click Start recovery.

Select one of the file overwriting options:

Overwrite existing files
Overwrite an existing file if it is older
Do not overwrite existing files

You can check the recovery progress in the Cyber Protect console, on the Activities tab.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.