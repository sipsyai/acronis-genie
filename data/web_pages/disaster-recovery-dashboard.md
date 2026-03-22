# Disaster recovery dashboard

Implementing disaster recovery > Disaster recovery dashboard
Disaster recovery dashboard

The disaster recovery Dashboard page contains widgets that provide a real-time overview and actionable insights for your disaster recovery site throughout its lifecycle. This helps you to:

Quickly detect and resolve problems by monitoring the status of recovery and primary servers.
Avoid overuse of compute points by monitoring the number of servers that consume them.
Disaster recovery - eligible devices

The widget shows the total number of devices that are protected by Disaster recovery (have a recovery server) and the total number of devices that are eligible for protection by Disaster recovery.

To go to the All devices page where you can configure Disaster recovery for the eligible devices, click Protect.

Health check

The widget shows information about the health of your disaster recovery infrastructure. You can check the state of the site configuration, network availability (available for Disaster Recovery to Cyber Protect Cloud only), and if there are missing service quotas.

To view more information about detected issues (warnings or errors), click View issues.

Automated test failover

The widget shows information about the automated test failover operations of your recovery servers.

To start configuring automated test failover for your servers, click Configure.

To download the data from the widget, click Report, and then choose the format - PDF or CSV.

The PDF report includes screenshots of the result of the automated test failover operations, which you can use to check the readiness of the servers for disaster recovery.

Recovery servers in failover

The widget shows the number and status of the recovery servers that are in production or test failover.

If there are no recovery servers currently running in the cloud, you will see a zero. If there is an issue with any server, you will see a warning or an error status.

The displayed compute points usage per hour is a real-time snapshot, not a historical value. This means that if, for example, you have two recovery servers and each one of them uses eight points, you will see a total of 16 points displayed in the widget.

You can use this information to estimate the cost of running these servers, and also as a reminder to stop a failover of a server that you do not need anymore.

Primary servers

The widget is available for Disaster Recovery to Cyber Protect Cloud only. It shows the number and status of the primary servers in your environment, and their compute point usage per hour. You can use this information to quickly spot and resolve any issues.

The displayed compute points usage per hour is a real-time snapshot, not a historical value. This means that if, for example, you have two recovery servers and each one of them uses eight points, you will see a total of 16 points displayed in the widget.

You can use this information to estimate the cost of running these servers, and also as a reminder to stop a failover of a server that you do not need anymore.

Cloud server alerts

The widget shows the latest alerts by severity, so that you can see critical alerts at a glance. The Alert type and Recovery server values in the widget are links that open the alert details and recovery server details, respectively.

Compute points usage

This widget shows the number of compute points that were used in your environment for the last 6 months - the current month and each of the past five months.

You can download a detailed report as a CSV or PDF file. The report includes the following information about the servers that used compute points, for each month: server name, server type, state, started by, start time, stop time, hours on during the month, compute usage per hour, and total compute points usage for the month.

To download the data from the widget, click Report, and then select the file format that you prefer.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.