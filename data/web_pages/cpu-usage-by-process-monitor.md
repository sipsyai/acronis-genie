# Settings of the CPU usage by process monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the CPU usage by process monitor
Settings of the CPU usage by process monitor

CPU usage by process monitors the CPU usage of the selected process. If there are multiple instances of the same process, the system will monitor the total usage by all process instances and will generate an alert when the conditions are met.

You can configure the following settings for the monitor.

Setting	Description
Process name	Name of the process that you want to monitor. Enter the process name without the extension.
Operator

The operator is a conditional function that defines how to measure the performance on the metric.

The following values are available.

More than —This is the default value.
More than or equal to
Less than
Less than or equal to

Threshold

The threshold value and the Operator value determine the normal performance of the monitored metric. When the value of the monitored metric is out of the norm, the system generates an alert.

Enter an integer value in the range 1-100 (%). The default value is 90.


Time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value in the range 1-60 (min). The default value is 5.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.