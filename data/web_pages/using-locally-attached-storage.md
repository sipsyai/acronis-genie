# Using locally attached storage

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Using locally attached storage
Using locally attached storage

With Agent for VMware (Virtual Appliance) or Agent for Scale Computing HC3, you can use locally attached storage to eliminate the network traffic between the protection agent and the backup location.

Locally attached storage (LAS) is designed for small environments with a single protection agent (virtual appliance). Using multiple protection agents with locally attached storage in the same environment might result in duplicated backups, because the virtual machines are randomly distributed among the agents, and each agent uses its own locally attached storage.

In VMware environments, you can use multiple virtual appliances if you manually bind each virtual appliance to all virtual machines that this appliance will back up. For more information, see Virtual machine binding.

The recommended disk size for locally attached storage is up to 5 TB. Larger disks might also work but such configurations are not tested. You can attach larger disks at your own risk.

If you need to back up more than 5 TB of data, we recommend that you use a different storage type. For example, you can attach a virtual disk to a virtual machine in the environment, and then create a network share on this disk. Then, you can use the network share as a backup destination, instead of using locally attached storage.

You can configure locally attached storage when you deploy a virtual appliance, or you can configure the storage later.

For more information about configuring local storage while deploying a virtual appliance, see Configuring the virtual appliance (for VMware) and Configuring the virtual appliance (for Scale Computing).

To configure local storage after deploying a virtual appliance

In your virtual machine environment, select the virtual appliance, and then open its settings for editing.

Add a new hard disk to the virtual appliance.

The disk size must be at least 10 GB.

If you use a disk that contains data, the data will be deleted.

In your virtual machine environment, open the console of the virtual appliance.

Under Local storages, click Refresh.

The Create storage button becomes active.

Click Create storage, and then select the disk that you added to the virtual appliance.

Select a drive letter.

Specify a disk label.

The label length is limited to 16 characters, due to file system restrictions.

Click OK.
Click Yes.

To select locally attached storage as a backup destination

When you create a protection plan, in Where to back up, select Local folders, and then specify the drive letter of locally attached storage. For example, D:\.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.