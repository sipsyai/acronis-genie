# Settings of the Memory usage by process monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Memory usage by process monitor
Settings of the Memory usage by process monitor

Memory usage by process monitors the memory usage of the selected process. If there are multiple instances of the same process, the system will monitor the total usage by all process instances and will generate an alert when the conditions are met.

The agents use the total process working set (private and shared) to estimate the size of the memory usage by process. That is why the size that the widget shows might be different from the size of the memory usage that is shown in Windows Task Manager (private working set).

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

Enter an integer value (kb). The default value is 1.


Time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value in the range 1-60 (min). The default value is 5.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.