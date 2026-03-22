# Conversion to a virtual machine

Working with plans > Off-host data protection plans > Conversion to a virtual machine
Conversion to a virtual machine

In service-based billing mode, this feature requires the Servers quota to be enabled under Standard Protection as a prerequisite, but using the feature does not affect the quota usage.

With solution-based billing mode, this functionality is available in customer tenants that use Ultimate protection.

With a conversion to VM plan, you can create a virtual machine from a disk-level backup that includes an operating system. Thus, you can quickly start a pre-created standby machine or perform cross-platform recovery. For example, you can recover a backup of a physical or virtual machine to a different hypervisor.

You can schedule the plan and incrementally apply backed-up changes to the resulting virtual machine.

You can convert a backup to a virtual machine by using a protection agent that has access to the backup archive. For more information about the available options, see Types of conversion to virtual machine.

Conversion or Running a virtual machine from a backup (Instant Restore)

Both operations provide a virtual machine that you can start if the original workload fails.

Conversion to a virtual machine uses CPU and memory resources during the conversion process, and the resulting virtual machine uses storage space on the datastore. However, the performance of the resulting virtual machine is better, compared to the machine that was created by the Run as VM operation (Instant Restore).

Running a virtual machine from a backup (Instant Restore) uses resources only while the virtual machine is running. In this case, datastore space is required only for storing changes to the virtual disks. The host does not access the virtual disks directly. Instead, it communicates with the agent, which reads data from the backup. As a result, performance is lower than that of a machine that was created via a conversion to VM plan. Also, with Instant Restore, the resulting virtual machine is temporary. For more information, see Running a virtual machine from a backup (Instant Restore).

Limitations
Conversion to a virtual machine is available only for disk-level backups. If a backup includes the system volume, and contains all of the information necessary for the operating system to start, the resulting virtual machine can start on its own. Otherwise, you can add its virtual disks to another virtual machine.
Backups that are stored on NFS cannot be converted.
Backups that are stored in Secure Zone can be converted only by the agent that is running on the same machine.
If the backup contains Linux logical volumes (LVM), you must create it by using Agent for VMware, Agent for Hyper-V, Agent for Scale Computing HC3, or Agent for Proxmox. Converted machines must match the platform of the original machine (VMware ESXi, Hyper-V, Scale Computing HC3, or Proxmox VE). Cross-hypervisor conversion is not supported.
When backups of a Windows machine are converted to VMware Workstation or VHDX files, the resulting virtual machine inherits the CPU type from the machine that performs the conversion. As a result, the corresponding CPU drivers are installed in the guest operating system. If it is started on a host with a different CPU type, the guest system displays a driver error. Update this driver manually.

With Proxmox, conversion to a virtual machine is also supported on storages that do not provide snapshot capabilities. In such cases, incremental updates of the resulting virtual machine are not possible. For more details about the storage types that are supported by Proxmox, see https://pve.proxmox.com/pve-docs/chapter-pvesm.html.

Types of conversion to virtual machine

Creating a conversion plan

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.