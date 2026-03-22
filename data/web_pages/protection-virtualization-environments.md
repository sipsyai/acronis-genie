# Protection of virtualization environments

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Working in VMware vSphere > Protection of virtualization environments
Protection of virtualization environments

In the Cyber Protect console, you can view the vSphere, Hyper-V, and Virtuozzo environments in their native presentation. After you install and register the corresponding agent, the VMware, Hyper-V, or Virtuozzo tab appears under Devices.

For example, on the VMware tab, you can back up the following vSphere infrastructure objects:

vCenter
Datacenter
Folder
Cluster
ESXi host
Resource pool
Virtual machine

To apply a plan to a selected infrastructure object, click Protect. All child objects will be backed up.

To apply a plan to the parent object of the selected infrastructure object, click Protect group. All child objects of the parent object will be backed up.

For example, if you apply a plan to an ESXi host, all virtual machines on the host will be backed up. If you apply a plan to the parent cluster, all virtual machines on all hosts in this cluster will be backed up.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.