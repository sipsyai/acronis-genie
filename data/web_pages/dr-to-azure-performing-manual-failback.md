# Performing a manual failback from Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failback in Microsoft Azure > Performing a manual failback from Microsoft Azure
Performing a manual failback from Microsoft Azure
The availability of this feature depends on the service quotas that are enabled for your account.

You can perform a manual failback from Microsoft Azure to a target physical or virtual machine on your local site.

To perform a manual failback

In the Cyber Protect console, go to Disaster Recovery > Servers.

Select the recovery server that is in the Failover state.

Click the Failback tab.

In the Target field, select Physical machine.

Click the gear icon, and then enable the Use manual mode switch.

[Optional] Calculate the estimated downtime period during the failback process, by dividing the Backup size value by the value of your Internet speed.

The value of the Internet speed will decrease when you perform several failback processes at the same time.

Click Switchover, and then in the confirmation window, click Switchover again.

The virtual machine on the cloud site is turned off.

If no backup plan is applied to the virtual machine in the cloud, a backup will be performed automatically during the switchover phase, which will cause a longer downtime.

Recover the server from the cloud backup to the physical or virtual machine on your local site.

For more information, see Recovery of virtual machines and Recovery of physical machines.

If you are performing a failback from a Microsoft Azure virtual machine to the original Azure virtual machine, use the recovery options that are described in Failback from Microsoft Azure to an Azure virtual machine.

Ensure that the recovery is completed and the recovered machine works properly, and click Machine is restored.

If everything is working as expected, click Confirm failback, and then in the confirmation window, click Confirm again.

The recovery server and recovery points become ready for the next failover. To create new recovery points, apply a protection plan to the new local server.

Applying a protection plan on the recovered server is not part of the failback process. After the failback process completes, apply a protection plan on the recovered server to ensure that it is protected again. You may apply the same protection plan that was applied on the original server, or a new protection plan that has the Disaster recovery module enabled.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.