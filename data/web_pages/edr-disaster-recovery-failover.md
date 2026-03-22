# Disaster Recovery failover

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Remediating incidents > Disaster Recovery failover
Disaster Recovery failover

As part of your recovery response to an attack, EDR enables you to run Implementing disaster recovery, which allows you to switch the workload to the recovery server. Note that your workload must have a subscription for Advanced Disaster Recovery.

To run Disaster Recovery failover

In the cyber kill chain, click the workload node you want to recover.
In the displayed sidebar, click the Response Actions tab.
In the Recovery section, click Disaster Recovery failover.

In the Recovery point field, perform the following steps:
Click the current recovery point date to select a recovery point.
In the displayed sidebar, select the relevant recovery point.
If you have an Advanced Disaster Recovery subscription, you can select the relevant recovery server (the offline VM) created in Disaster Recovery. If you do not have a subscription, you will be prompted to configure Disaster Recovery.
[Optional] In the Comment field, add a comment. This comment is visible in the Activities tab (for a single node or the entire incident), and can help you (or your colleagues) recall why you took the action when you revisit the incident.
Click Failover.

The workload is switched to the recovery server. This action can be viewed in the Activities tabs of both the individual node and the entire incident. For more information, see Understand the actions taken to mitigate an incident.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.