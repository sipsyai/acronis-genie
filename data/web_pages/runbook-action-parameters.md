# Runbook parameters

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Orchestration (runbooks) > Runbook parameters
Runbook parameters

Runbook parameters are specific settings that you must configure to define a runbook action. There are two categories of runbook parameters - action parameters and completion check parameters.

Action parameters define the runbook behavior depending on the action initial state or result.

Completion check parameters ensure that the server is available and provides the necessary services. If a completion check fails, the action is considered failed.

The following table describes the configurable runbook parameters for each action.

Runbook parameter	Category	Available for action	Description
Continue if already done	Action parameter
Failover server
Start server
Stop server
Failback server


This parameter defines the runbook behavior when the required action is already done (for example, a failover has already been performed or a server is already running). When enabled, the runbook issues a warning and proceeds. When disabled, the action fails, and then the runbook fails too.

By default, this parameter is enabled.


Continue if failed	Action parameter
Failover server
Start server
Stop server
Failback server


This parameter defines the runbook behavior when the required action fails. When enabled, the runbook issues a warning and proceeds. When disabled, the action fails, and then the runbook fails too.

By default, this parameter is disabled.


Ping IP address	Completion check
Start server


The software will ping the production IP address of the cloud server until the server replies or the timeout expires, whichever comes first.


Connect to port (443 by default)	Completion check
Failover server
Start server


The software will try to connect to the cloud server by using its production IP address and the port you specify, until the connection is established or the timeout expires, whichever comes first. This way, you can check if the application that listens on the specified port is running.


Timeout in minutes	Completion check
Failover server
Start server


The default timeout is 10 minutes.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.