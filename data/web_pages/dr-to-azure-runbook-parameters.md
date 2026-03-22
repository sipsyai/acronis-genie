# Runbook parameters in Microsoft Azure

Implementing disaster recovery > Disaster Recovery to Microsoft Azure > Runbooks in Microsoft Azure > Runbook parameters in Microsoft Azure
Runbook parameters in Microsoft Azure

Runbook parameters are specific settings that you must configure to define a runbook action. They define the runbook behavior depending on the action initial state or result.

The following table describes the configurable runbook parameters for each action.

Runbook parameter	Available for action	Description
Continue if already done
Failover server
Start server
Stop server
Failback server


This parameter defines the runbook behavior when the required action is already done (for example, a failover has already been performed or a server is already running). When enabled, the runbook issues a warning and proceeds. When disabled, the action fails, and then the runbook fails too.

By default, this parameter is enabled.


Continue if failed
Failover server
Start server
Stop server
Failback server


This parameter defines the runbook behavior when the required action fails. When enabled, the runbook issues a warning and proceeds. When disabled, the action fails, and then the runbook fails too.

By default, this parameter is disabled.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.