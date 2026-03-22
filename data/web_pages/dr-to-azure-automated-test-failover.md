# Automated test failover in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Failover in Microsoft Azure > Automated test failover in Microsoft Azure
Automated test failover in Microsoft Azure

Automated test failover in Microsoft Azure validates backup integrity by booting a recovery server VM from the latest backup and capturing a screenshot to confirm that the operating system started successfully.

With automated test failover, the recovery server is tested automatically once a week or once a month, without any manual interaction.

The automated test failover process consists of the following parts:

Creating a virtual machine in Microsoft Azure from the latest recovery point.
Taking a screenshot of the virtual machine.
Analyzing if the operating system of the virtual machine starts successfully.
Notifying you about the test failover status.

Automated test failover consumes Azure VM compute hours.

You can configure the automated test failover in the recovery server's settings. For more information, see Configuring automated test failover in Microsoft Azure.

If automated test failover is skipped for some reason, an alert will be raised.

Automated test failover will fail if the backups of the original machine are encrypted by using encryption as a machine property, and the encryption password is not specified when creating the recovery server. For more information about specifying the encryption password, see Creating recovery servers in Microsoft Azure.

Configuring automated test failover in Microsoft Azure

Viewing the automated test failover status

Disabling automated test failover

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.