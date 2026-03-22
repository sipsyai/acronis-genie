# Settings of the Disk transfer rate by process monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Disk transfer rate by process monitor
Settings of the Disk transfer rate by process monitor

Disk transfer rate by process monitors the read and write speed of the selected process. If there are multiple instances of the same process, the system will monitor the total usage by all process instances and will generate an alert when the conditions are met.

You can configure the following settings for the monitor.

Setting	Description
Process name	The name of the process that you want to monitor. Enter the process name without the extension.
What to monitor

The speed that you want to monitor.

The following values are available.

Read speed and Write speed. This is the default value.
Read speed
Write speed

Read speed operator

The operator is a conditional function that defines how to measure the performance on the metric.

The following values are available.

More than —This is the default value.
More than or equal to
Less than
Less than or equal to

Read speed threshold

The threshold value and the Operator value determine the normal performance of the monitored metric. When the value of the monitored metric is out of the norm, the system generates an alert.

Enter an integer value (kb/s). The default value is 0 kb/s.


Read speed time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value in the range 1-60 (min). The default value is 5.


Write speed operator

The operator is a conditional function that defines how to measure the performance on the metric.

The following values are available.

More than —This is the default value.
More than or equal to
Less than
Less than or equal to

Write speed threshold

The threshold value and the Operator value determine the normal performance of the monitored metric. When the value of the monitored metric is out of the norm, the system generates an alert.

Enter an integer value (kb/s). The default value is 0 kb/s.


Write speed time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value in the range 1-60 (min). The default value is 5.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.