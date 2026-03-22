# Failover in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failover in Microsoft Azure
Failover in Microsoft Azure
The availability of this feature depends on the service quotas that are enabled for your account.
Production failover

Failover is the process switching the workload from the original server at your local site to the recovery server.

When a recovery server is created, it stays in the Standby state. The corresponding virtual machine does not exist in Microsoft Azure until you start a failover. Before you start a failover, you must create at least one disk image backup (with bootable volume) of the original machine.

When you start a failover, you select the recovery point (backup) of the original machine from which a virtual machine with the predefined parameters will be created in Microsoft Azure.

When the failover completes, the recovery server state changes to Failover. The workload is now switched from the original machine to the recovery server in Microsoft Azure.

If the recovery server has a protection agent, to avoid interference (such as starting a backup or reporting outdated statuses to the backup component), the agent service is stopped.

Test failover

Test failover is a process of creating a temporary VM in an isolated Azure virtual network (VNet) and test recovery procedures, configurations, and applications functionality. For more information, see Test failover in Microsoft Azure.

Automated test failover

Automated test failover in Microsoft Azure validates backup integrity by booting a recovery server VM from the latest backup and capturing a screenshot to confirm that the operating system started successfully. If enabled, automated test failover is started once a month. For more information, see Automated test failover in Microsoft Azure.

Failover of Windows machines

For Windows machines, if the DeviceInstallDisabled parameter is set to 1 (HKLM\SYSTEM\CurrentControlSet\Services\DeviceInstall\Parameters\DeviceInstallDisabled = 1), the disaster recovery service will set the value to 0 or remove the parameter completely during failover. This is required because Windows must be allowed to install and configure the necessary drivers and devices for the failover process to complete successfully. If you want to keep the original setting, you can manually restore it after the failover operation is complete.

Setting the DeviceInstallDisabled parameter to 1 might impact subsequent disaster recovery operations, including failback and the re-validation steps that are required before initiating failback.

IP Address conflict handling in failover

If the configured IP address in the production network is already in use at the time of the production failover, another available IP address from the same network will be assigned automatically.

If the configured test network IP address is already in use at the time of the test failover, another available IP address from the test network will be assigned.

Recovery of recovery server in failover to a previous point in time

To recover a server in failover, initiate a new failover from a different recovery point to restore operations.

Failover widgets

During production and test failover, you can see information about the failover performance (recovery speed) and bottlenecks on the Activities tab of the recovery server details. To view the Bottleneck widget, expand the Creating virtual machine activity, and then in the Copying data from the backup to the virtual machine disks subactivity, expand Bottleneck.

Performing a production failover in Microsoft Azure

Test failover in Microsoft Azure

Automated test failover in Microsoft Azure

Requirements and limitations for failover of Linux VMs to Microsoft Azure

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.