# Running a virtual machine from a backup

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Running a virtual machine from a backup (Instant Restore) > Running a virtual machine from a backup
Running a virtual machine from a backup

You can run a virtual machine from a disk-level backup that includes an operating system.

The Run as VM operation (Instant Restore) is not supported for backups that are stored on S3-compatible object storages.

The Run as VM operation (Instant Restore) is supported for backups that are stored in Microsoft Azure. However, this operation results in significant egress traffic, which is billed by Microsoft. Typical egress traffic for a Windows machine running from a Microsoft Azure backup is approximately 5 GB from powering on the virtual machine until logging in to it.

To run a virtual machine form a backup (Instant Restore)

VMware ESXi
Microsoft Hyper-V
Proxmox VE
In the Cyber Protect console, select a backup (recovery point) that you want to run as a virtual machine.
Click Run as VM.

In Power state, choose whether the new virtual machine will start automatically after creation.

In Target machine, select VMware ESXi as a hypervisor, select a location and name for the resulting virtual machine, and then click OK.

In Datastore, select storage for the virtual machine.

While the virtual machine is running, changes to its virtual disks are written to storage. Ensure that the selected storage has enough free space. If you plan to make the virtual machine permanent, select storage that is appropriate for production workloads.

[Optional] In VM settings, edit the memory size or network connections of the virtual machine, and then click OK.
Click Run now.

As a result, the virtual machine that is run from a backup appears in the Cyber Protect console with one of the following icons:

for VMware ESxi,  for Hyper-V, and  for Proxmox VE. You cannot back up these machines.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.