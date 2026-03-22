# Failover

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Failover
Failover
The availability of this feature depends on the service quotas that are enabled for your account.

When a recovery server is created, it stays in the Standby state. The corresponding virtual machine does not exist until you start a failover. Before starting a failover process, you must create at least one disk image backup (with bootable volume) of the original machine.

When starting the failover process, you select the recovery point (backup) of the original machine from which a virtual machine with the predefined parameters will be created. The failover operation uses the "run VM from a backup" functionality. The recovery server gets the transition state Finalization. This process implies transferring the server's virtual disks from the backup storage ('cold' storage) to the disaster recovery storage ('hot' storage).

During the Finalization, the server is accessible and operable, although the performance is lower than normal. You can open the server console by clicking the Console is ready link. The link is available in the VM State column on the Disaster Recovery > Servers screen and in the server's Details view.

When the Finalization is completed, the server performance reaches its normal value. The server state changes to Failover. The workload is now switched from the original machine to the recovery server in the cloud site.

If the recovery server has a protection agent inside, the agent service is stopped in order to avoid interference (such as starting a backup or reporting outdated statuses to the backup component).

For Windows machines, if the DeviceInstallDisabled parameter is set to 1 (HKLM\SYSTEM\CurrentControlSet\Services\DeviceInstall\Parameters\DeviceInstallDisabled = 1), the disaster recovery service will set the value to 0 or remove the parameter completely during failover. This is required because Windows must be allowed to install and configure the necessary drivers and devices for the failover process to complete successfully. If you want to keep the original setting, you can manually restore it after the failover operation is complete.

Setting the DeviceInstallDisabled parameter to 1 might impact subsequent disaster recovery operations, including failback and the re-validation steps that are required before initiating failback.

On the diagram below, you can see both the failover and failback processes.

Performing a failover

Stopping a failover

Test failover

Automated test failover

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.