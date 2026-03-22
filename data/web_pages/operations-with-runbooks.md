# Operations with runbooks

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Orchestration (runbooks) > Operations with runbooks
Operations with runbooks
The availability of this feature depends on the service quotas that are enabled for your account.

To access the list of operations, hover on a runbook and click the ellipsis icon. When a runbook is not running, the following operations are available:

Execute
Edit
Clone
Delete
Executing a runbook

Every time you click Execute, you are prompted for the execution parameters. These parameters apply to all failover and failback operations included in the runbook. The runbooks specified in the Execute runbook operations inherit these parameters from the main runbook.

Failover and failback mode

Choose whether you want to run a test failover (by default) or a real (production) failover. The failback mode will correspond to the chosen failover mode.

Failover recovery point

Choose the most recent recovery point (by default) or select a point in time in the past. If the latter is the case, the recovery points closest before the specified date and time will be selected for each server.

Stopping a runbook execution

During a runbook execution, you can select Stop in the list of operations. The software will complete all of the already started actions except for those that require user interaction.

Viewing the execution history

When you select a runbook on the Runbooks tab, the software displays the runbook details and execution history. Click the line corresponding to a specific execution to view the execution log.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.