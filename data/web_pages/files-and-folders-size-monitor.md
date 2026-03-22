# Settings of the Files and folders size monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Files and folders size monitor
Settings of the Files and folders size monitor

Files and folders size monitors the total size of the selected files and folders.

You can configure the following settings for the monitor.

Setting	Description
Files or folders to monitor

The paths to the files or folders that you want to monitor. You can also specify files or folders that you want to exclude from monitoring.

You can use the following wildcard characters.

* — for zero or more characters in a file or folder name
? — for exactly one character in a file or folder name

For Windows workloads:

The full path should start from the drive letter followed by the :\ separator.
You can use slash or backslash as a path separator character.
The file or folder name must not end with a space or a period.

For macOS workloads:

The full path should start from the root directory.
You can use slash as a path separator character.
The file or folder name must not end with a space or a period.

Operator

The operator is a conditional function that defines how to measure the performance on the metric.

The following values are available.

More than —This is the default value.
Less than

Threshold value

The threshold value and the Operator value determine the normal performance of the monitored metric. When the value of the monitored metric is out of the norm, the system generates an alert.

Enter an integer value (MB).


Time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value in the range 10-60 (min). The default value is 10.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.