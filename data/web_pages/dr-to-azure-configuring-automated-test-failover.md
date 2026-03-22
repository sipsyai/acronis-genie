# Configuring automated test failover in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failover in Microsoft Azure > Configuring automated test failover in Microsoft Azure
Configuring automated test failover in Microsoft Azure

By configuring automated test failover, you can test your recovery server without performing any manual actions.

To configure automated test failover of a recovery server in Microsoft Azure

In the Cyber Protect console, go to Disaster Recovery > Dashboard.

In the Automated test failover widget, click Configure.

In the Automated test failover configuration dialog, select one or more recovery servers for which you want to configure automated test failover, and then click Next.

Turn on the Automated test failover switch.

In the Schedule field, select how often automated test failover should be performed.

Option	Description
Monthly	Automated test failover is performed at the beginning of each month.
Weekly	Automated test failover is performed every week.

In VM startup timeout / Minutes, change the default value of the maximum period during which the system tries to start the virtual machine in Azure and take a screenshot to verify if the operating system loaded successfully.

This timeout does not include the time required to restore data from a cold backup archive. The timer starts when the virtual machine starts booting.

During cold data restore, Azure temporarily creates a standard Blob storage, which is later converted into a managed disk for the VM.

Azure VM compute hours are not counted during the data restoration process.

To save the VM startup timeout / Minutes value as the default and have it populated automatically when you enable automated test failover for the other recovery servers, select Set as default timeout.

Click Configure.

On the Recovery servers tab, you can see that the automated test failover started. After it completes, the virtual machine will be deleted and you can find the link to the screenshot of the validated operating system in the recovery server details.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.