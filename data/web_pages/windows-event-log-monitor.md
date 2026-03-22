# Settings of the Windows event log monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Windows event log monitor
Settings of the Windows event log monitor

Windows event log monitors specific business-critical events in the Windows event logs.

You can configure the following settings for the monitor.

Setting	Description
Event log name

Select a certain event log from a list of Windows event logs that are available in Windows Event Viewer.

The following values are available.

Any —This is the default value.
Application
Security
System

Event source

Event source name

You can select the value from a list of event sources that are collected from all agents of the tenant or enter a new source name manually.

If the software inventory scan is disabled for the tenant, the event source list will be empty.


Matching mode

In this field, you can specify whether to connect the Event IDs, Event type, and Event description settings by using the Any or the All operator.

The following values are available.

Any —This is the default value. An alert will be generated only if any of the selected criteria is matched.
All — An alert will be generated if all the selected criteria are matched.

Event IDs

Enter one or multiple event IDs separated by comma. If the system finds in the event log any of the event codes that you entered in this field, it generates an alert.


Event type

Select one or multiple event types that you want to monitor.

The following values are available.

Any — This is the default value.
Error
Warning
Information
Success-audit
Failure-audit

Event description

Specific keywords or phrases in the event description for which you want to search. Each keyword or phrase that you enter must be enclosed in quotation marks and must be separated by comma. If the system finds any of the keywords or phrases that you entered, it will generate an alert.


Number of occurrences

The minimum number of occurrences in the log that an event must have during the time period for the system to generate an alert.

Enter an integer value in the range 1-1000.


Time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value and then select the unit: minutes or hours. The default value is 60 minutes.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.