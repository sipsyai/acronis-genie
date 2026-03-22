# Settings of the Windows service status monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Windows service status monitor
Settings of the Windows service status monitor

Windows service status monitors whether the selected Windows service is running or stopped.

You can configure the following settings for the monitor.

Setting	Description
Service name

The name of the Windows service that you want to monitor.

You can select a service name from the list of Windows services. The list is populated by all agents of the tenant after software inventory scan completes successfully on the workloads. You can also add a service name that is not in the list. This is the only available option if software inventory scan was not performed on the workloads.


Service status

If the service is in the selected status, the system will generate an event.

The following values are available.

Running
Stopped—This is the default value.

Time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value in the range 1-60 (min). The default value is 1.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.