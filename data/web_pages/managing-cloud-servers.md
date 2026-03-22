# Viewing details about cloud servers

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Cloud servers > Viewing details about cloud servers
Viewing details about cloud servers

To view the details of the cloud servers, go to Disaster Recovery > Servers. There are two tabs there: Recovery servers and Primary servers. To show all optional columns in the table, click the gear icon.

You can find the following information about each cloud server by selecting it.

Column name	Description


Name

A cloud server name defined by you


Status

The status reflecting the most severe issue with a cloud server (based on the active alerts)


State

A cloud server state


VM state

The power state of a virtual machine associated with a cloud server


Active location

The location where a cloud server is hosted. For example, Cloud.


RPO threshold

The maximum time interval allowed between the last suitable recovery point for failover and the current time. The value can be set within 15-60 minutes, 1-24 hours, 1-14 days.


RPO compliance



The RPO compliance is the ratio between the actual RPO and RPO threshold. The RPO compliance is shown if the RPO threshold is defined.

It is calculated as follows:

RPO compliance = Actual RPO / RPO threshold

where

Actual RPO = current time – last recovery point time

RPO compliance statuses

Depending on the value of the ratio between the actual RPO and RPO threshold, the following statuses are used:

Compliant. The RPO compliance < 1x. A server meets the RPO threshold.
Exceeded. The RPO compliance <= 2x. A server violates the RPO threshold.
Severely exceeded. The RPO compliance <= 4x. A server violates the RPO threshold more than 2x times.
Critically exceeded. The RPO compliance > 4x. A server violates the RPO threshold more than 4x times.
Pending (no backups). The server is protected with the protection plan but the backup is being created and not completed yet.



Actual RPO

The time passed since the last recovery point creation


Last recovery point

The date and time when the last recovery point was created
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.