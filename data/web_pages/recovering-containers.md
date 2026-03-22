# Recovering containers

Managing the backup and recovery of workloads and files > Recovery > Recovery of virtual machines > Recovering containers
Recovering containers

You can recover a backed-up container to the original container or to a new container on the same hypervisor.

Cross-platform recovery is not supported for containers.

To recover a container

Virtuozzo container
Proxmox container

In the Cyber Protect console, do one of the following:

On the Devices tab, select a backed-up container, click Recovery, and then select a backup (recovery point).
On the Backup storage tab, select a backup archive, and then select a backup (recovery point).

Click Recover > Entire machine.

The original container is selected as a target container.

[If prompted] Specify the credentials to access the backup storage, and then click OK.

To change the target container:

Click Target container.
[If multiple hypervisors are available] Select Virtuozzo.

[To perform recovery to a new container]

Select New container.
Select a host.
In Container name, specify a name for the new container.
Click OK.

[To perform recovery to an existing container]

Select Existing container.
Select the target container.
Click OK.
[If prompted] Specify the credentials to access the backup storage, and then click OK.

[When recovering to a new container] Configure additional options:

To change the storage for the virtual machine, click Storage, and then select a storage.

To change the disk mapping or exclude some of the backed-up disks from the recovery, click Disk mapping.

Configure the disk mapping or select the disks that you want to recover.
Click Done.

To change the memory size, the number of virtual processors, or the network connections of the target machine, click Container settings.

Configure the settings.
Click OK.
Click Start recovery
[When recovering to an existing container] To confirm that you want to overwrite the target container, click Start recovery.

You can check the recovery progress in the Cyber Protect console, on the Activities tab.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.