# Support for virtual machine migration

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Support for virtual machine migration
Support for virtual machine migration

This section contains information about migration of virtual machines within a vSphere environment, including migration between ESXi hosts that are part of a vSphere cluster.

vMotion allows moving the state and configuration of a virtual machine to another host, while the machine's disks remain in the same location on a shared storage. Storage vMotion allows moving the disks of a virtual machine from one datastore to another.

Migration with vMotion, including Storage vMotion, is not supported for a virtual machine that runs Agent for VMware (Virtual Appliance), and has to be disabled after the appliance deployment. You should add this virtual machine to the VM overrides list in the vSphere cluster configuration in order to avoid migration of the appliance virtual machine across vSphere cluster nodes.
When a backup of a virtual machine starts, migration with vMotion, including Storage vMotion, is automatically disabled. This virtual machine is temporarily added to the VM overrides list in the vSphere cluster configuration. After the backup finishes, the VM overrides settings are automatically reverted to their previous state.
A backup cannot start for a virtual machine while its migration with vMotion, including Storage vMotion, is in progress. The backup for this machine will start when its migration finishes.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.