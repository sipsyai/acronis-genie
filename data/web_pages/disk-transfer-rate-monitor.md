# Settings of the Disk transfer rate monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Disk transfer rate monitor
Settings of the Disk transfer rate monitor

Disk transfer rate monitors the read and write speed of each physical disk on the workload.

You can configure the following settings for the monitor.

Setting	Description
Threshold-based monitoring
What to monitor

Select the speed that you want to monitor.

The following values are available.

Read speed and Write speed. This is the default value.
Read speed
Write speed

Read speed operator

The operator is a conditional function that defines how to measure the performance on the metric.

The following values are available.

More than. This is the default value.
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


Anomaly-based monitoring
Model training period

The period during which the system will train the machine learning models based on the data that is collected from the agents, and will then create the normal behavior pattern of the workload. The longer the model training period, the more precise the long-term behavior pattern that the system will create. We recommend that the minimum model training period is twenty-one days.

Enter an integer value (days). The default value is 21.


Receive anomaly alerts during the training period

If you select this setting, you will receive alerts about anomalies during the model training period. These alerts might be false, because the models are still being trained and might not be accurate enough.

By default, the setting is selected.


What to monitor

Select the speed that you want to monitor.

The following values are available.

Read speed and Write speed. This is the default value.
Read speed
Write speed

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

Anomaly duration (Read speed)

The system will generate an alert for a detected anomaly only if the abnormal behavior persists for the specified period.

Enter an integer value in the range 1--60 (min).

The default value it 25.


Anomaly duration (Write speed)

The system will generate an alert for a detected anomaly only if the abnormal behavior persists for the specified period.

Enter an integer value in the range 1--60 (min).

The default value it 25.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.