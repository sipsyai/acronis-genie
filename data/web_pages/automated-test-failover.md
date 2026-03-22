# Automated test failover

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Failover > Automated test failover
Automated test failover

With automated test failover, the recovery server is tested automatically once a week or once a month, without any manual interaction.

The automated test failover process consists of the following parts:

creating a virtual machine from the last recovery point
taking a screenshot of the virtual machine
analyzing if the operating system of the virtual machine starts successfully
notifying you about the test failover status

Automated test failover consumes compute points.

You can configure the automated test failover in the recovery server's settings. For more information, see Configuring automated test failover.

Note that, in very rare cases, automated test failover might be skipped and might not be performed at the scheduled time. This is because production failover has higher priority than automated test failover, so the hardware resources (CPU and RAM) allocated for automated test failover might be temporarily limited to ensure that there are enough resources for a concurrent production failover.

If automated test failover is skipped for some reason, an alert will be raised.

Automated test failover will fail if the backups of the original machine are encrypted by using encryption as a machine property, and the encryption password is not specified when creating the recovery server. For more information about specifying the encryption password, see Creating a recovery server.

Configuring automated test failover

Viewing the automated test failover status

Disabling automated test failover

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.