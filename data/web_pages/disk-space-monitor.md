# Settings of the Disk space monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Disk space monitor
Settings of the Disk space monitor

Disk space monitors the free space on a specific drive of the workload.

When calculating the space, the monitor uses binary bytes (1024 bytes per KB, 1024 KB per MB, and 1024 MB per GB) for both Windows and macOS workloads.

You can configure the following settings for the monitor.

Setting	Description
Threshold-based monitoring
Drive

The drive that you want to monitor.

The following values are available.

System drive —This is the default value.

This is the drive or partition on a computer where the operating system (OS) is installed. On Windows systems, the system drive is usually the C: drive by default, but this can vary depending on the setup.

Any drive

Operator

The operator is a conditional function that defines how to measure the performance on the metric.

The following values are available.

Less than —This is the default value.
Less than or equal to

Disk free space threshold

The threshold value and the Operator value determine the normal performance of the monitored metric. When the value of the monitored metric is out of the norm, the system generates an alert.

Enter an integer value in the range 1-100 (%). The default value is 20.


Include removable drives

This setting is available if the Drive value is Any drive.

Select this setting if you want to add removable drives, like USB flash drives, for monitoring. By default, the setting is disabled.


Time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value in the range 1-60 (min). The default value is 30.


Anomaly-based monitoring
Drive

The drive that you want to monitor.

The following values are available.

System drive —This is the default value.

This is the drive or partition on a computer where the operating system (OS) is installed. On Windows systems, the system drive is usually the C: drive by default, but this can vary depending on the setup.

Any drive

Model training period

The period during which the system will train the machine learning models based on the data that is collected from the agents, and will then create the normal behavior pattern of the workload. The longer the model training period, the more precise the long-term behavior pattern that the system will create. We recommend that the minimum model training period is twenty-one days.

Enter an integer value (days). The default value is 21.


Receive anomaly alerts during the training period

If you select this setting, you will receive alerts about anomalies during the model training period. These alerts might be false, because the models are still being trained and might not be accurate enough.

By default, the setting is selected.


Sensitivity level

The sensitivity level acts as a preliminary filter for anomalies if their values are within a specific range. This filter operates independently from the anomaly detection algorithm. Its purpose is to stop the anomalies that are in the specified range from being processed by the anomaly detection algorithm.

During the training period:

The algorithm is trained using the data that is collected during the training.

The algorithm performs anomaly detection on the training data.

A filtering process based on mean and standard deviation is applied.

Any anomalies that are in the specified interval are filtered.

From the remaining anomalous data points, the anomaly with the lowest anomaly level is selected. This level (a float number between 0 and 1) is recorded in the model.

During the prediction:

The algorithm predicts anomalies on the inference data.

The predicted anomalies are filtered based on the mean and standard deviation, according to the sensitivity level.

The remaining anomalies are further filtered based on the following principle: values above the threshold level are considered an anomaly, while values below the threshold level are considered normal behavior.

The following values are available.

Low — The low level equals the mean value and the standard deviation value.
Normal — This is the default value. The normal level equals the mean value and two times the standard deviation value.
High — The high level equals the mean value and three times the standard deviation value.

Anomaly duration

The system will generate an alert for a detected anomaly only if the abnormal behavior persists for the specified period.

The default value is 30 minutes.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.