# Restart a workload

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Remediating incidents > Restart a workload
Restart a workload

As part of your remediation response to an attack, EDR enables you to immediately restart a workload, or restart the workload according to a predefined timeout period.

To restart a workload

In the cyber kill chain, click the workload node you want to set a restart schedule for.
In the displayed sidebar, click the Response Actions tab.
In the Remediate section, click Restart workload.

In the Restart timeout field, click the displayed link, and then select one of the following:
Set timeout: In the Restart timeout dialog, set the restart period for the workload, and then click Save.
Restart immediately: Select to restart the workload immediately.
[Optional] Select the Fail if end-user is logged in check box to ensure the workload is not restarted if the user is logged in.
In the Message to display field, add a message to display to users when they access the isolated workload.
[Optional] In the Comment field, add a comment. This comment is visible in the Activities tab (for a single node or the entire incident), and can help you (or your colleagues) recall why you took the action when you revisit the incident.
Click Restart.

The workload is set to restart according to the schedule defined. This action can also be viewed in the Activities tabs of both the individual node and the entire incident. For more information, see Understand the actions taken to mitigate an incident.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.