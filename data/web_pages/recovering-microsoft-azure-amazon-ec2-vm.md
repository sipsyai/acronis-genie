# Recovering Microsoft Azure and Amazon EC2 machines

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Agent-based backup of Microsoft Azure and Amazon EC2 virtual machines > Recovering Microsoft Azure and Amazon EC2 machines
Recovering Microsoft Azure and Amazon EC2 machines

Follow this procedure for Microsoft Azure virtual machines if you do not use Agent for Azure.

If you use Agent for Azure, you can recover an Entire machine backup as a virtual machine directly. For more information, see Recovery of physical machines and Recovery of virtual machines.

To recover a machine as a new Microsoft Azure or Amazon EC2 virtual machine

Create a new virtual machine from an image or template in Microsoft Azure or Amazon EC2.

The new machine must have the same disk configuration as the machine that you want to recover.

On the new machine, install Agent for Windows or Agent for Linux.

Recover the backed-up machine as described in Recovery of physical machines.

When you configure the recovery, select the new machine as the target machine.

For Microsoft Azure virtual machines, this recovery procedure applies only to backups of machines that contain all necessary drivers to run in Azure natively (backups of Azure virtual machines, local Hyper-V machines, or machines running Windows Server 2016 or later). For cross-platform recovery, see this knowledge base article.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.