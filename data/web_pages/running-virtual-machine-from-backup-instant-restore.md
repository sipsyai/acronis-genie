# Running a virtual machine from a backup (Instant Restore)

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Running a virtual machine from a backup (Instant Restore)
Running a virtual machine from a backup (Instant Restore)

By using Run as VM, you can start a virtual machine from a disk-level backup that contains an operating system. This operation, also known as Instant Restore, quickly brings a virtual machine online.

While this virtual machine is running, its disks are emulated directly from the backup, and storage space is only required for recording the on-going changes.

The virtual machine that is created by using Run as VM is designed for short-term use. Typical use cases include:

Disaster recovery: Instantly bring online a copy of a failed machine.
Backup verification: Run a machine directly from its backup to confirm that the guest operating system and applications function correctly.
Accessing application data: Use the application’s native management tools on the running machine to access or extract required data.

We recommend that you keep the temporary machine for up to three days, and then remove it or convert it to a regular virtual machine, by finalizing it.

While the temporary virtual machine exists, retention rules cannot be applied to the backup on which it relies. However, backups of the original machine can continue to run normally.

Prerequisites
At least one agent (depending on the hypervisor, Agent for VMware, Agent for Hyper-V, or Agent for Proxmox) must be registered in the Cyber Protection console.
The backup from which you run the temporary virtual machine can be located in a network folder or in a local folder. If you select a network folder, the protection agent must be able to access it. You can also run the virtual machine from a backup that is stored in cloud storage. However, performance will be slower because this operation requires intensive random-access reads from the backup.
Run as VM requires either a backup of the entire machine or a backup of all volumes that are needed for the operating system to start.
To run a virtual machine from a backup, you can use backups of both physical and virtual machines. You cannot use backups of containers.
If the backup contains Linux logical volumes (LVM), you must create it by using Agent for VMware, Agent for Hyper-V, or Agent for Proxmox. The temporary virtual machine must match the platform of the original machine (VMware ESXi, Hyper-V, or Proxmox).

Finalization

Running a virtual machine from a backup

Deleting a virtual machine running from a backup

Finalizing a virtual machine running from a backup

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.