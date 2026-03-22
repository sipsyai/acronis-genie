# Operations with runbooks in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Runbooks in Microsoft Azure > Operations with runbooks in Microsoft Azure
Operations with runbooks in Microsoft Azure
The availability of this feature depends on the service quotas that are enabled for your account.

When a runbook is not running, the following operations are available: execute, edit, clone, view details, and delete.

Execute
Edit
Clone
View details
Delete

Every time you click Execute, you are prompted for the execution parameters. These parameters apply to all failover and failback operations that are included in the runbook. If there are runbooks that are specified in the Execute runbook operations, they will inherit these parameters from the main runbook.

To execute a runbook

In the Cyber Protect console, go to Disaster Recovery > Runbooks.

Click the runbook that you want to execute, and then click Execute.

In the Execution parameters window, configure the parameters.

Parameter	Description
Failover and failback mode

Select whether you want to run a test failover (by default) or a real (production) failover. The failback mode will correspond to the selected failover mode.


Failover recovery point

Select the most recent recovery point (by default) or select a point in time in the past. If you select a point in time in the past, the recovery points that are closest before the specified date and time will be selected for each server.

Click Start.

The runbook execution starts. You can stop the runbook execution. The software will complete all of the already started actions except the ones that require user interaction.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.