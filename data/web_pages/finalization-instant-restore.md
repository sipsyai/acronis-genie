# Finalization

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Running a virtual machine from a backup (Instant Restore) > Finalization
Finalization

Running a virtual machine directly from a backup requires an uninterrupted connection to both the backup location and the protection agent. If this connection is lost, the machine can become inaccessible or even corrupted.

Finalization is the process of converting this temporary virtual machine into an independent, permanent virtual machine that is stored on production-ready storage. During finalization, the Cyber Protect recovers the machine’s virtual disks and applies all changes that were made while the machine was running. The virtual machine remains powered on throughout the entire process.

Before starting finalization, ensure that the selected storage has enough free space, supports appropriate sharing capabilities, and provides the performance that is required for production workloads.

Finalization is not supported for Hyper-V machines that run on Windows Server 2008/2008 R2 and Microsoft Hyper-V Server 2008/2008 R2 because these operating systems do not provide a required API.

Finalization vs backup recovery

The finalization process is slower than a backup recovery for two main reasons:

During finalization, the protection agent must perform random reads across various parts of the backup. During backup recovery, it reads the backup sequentially, which is significantly faster.
If the virtual machine is running during finalization, the agent must read data from the backup to support both the running virtual machine and the finalization process. In backup recovery, the virtual machine is stopped, which makes data access more efficient.
Finalization of machines running from cloud backups

Finalization requires intensive access to the backed-up data, and its speed depends heavily on the bandwidth between the backup location and the agent. As a result, finalization is typically slower for backups that are stored in the cloud than for backups that are stored locally. If the Internet connection is very slow or unstable, finalizing a machine running from a cloud backup might even fail.

We recommend that you run virtual machines from local backups whenever possible if you plan to perform finalization.

For VMware workloads, finalization speed depends on whether the protection agent is connected to a VMware ESXi host or to vCenter. Due to the way VMware APIs operate, connecting to vCenter can slow down the finalization process. To improve performance, use a dedicated Agent for VMware to perform the Run as VM operation and finalization. Connect this agent to the ESXi host instead of vCenter.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.