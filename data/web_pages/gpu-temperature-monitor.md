# Settings of the GPU temperature monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the GPU temperature monitor
Settings of the GPU temperature monitor

GPU temperature monitors the GPU temperature of the workload.

You can configure the following settings for the monitor.

Setting	Description
Threshold-based monitoring


GPU temperature has exceeded



The maximum value of the monitored metric. If the value is exceeded, the system detects an anomaly.

Enter an integer value (C°). The default value is 80.


Time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value in the range 1-60 (min). The default value is 5.


Anomaly-based monitoring
Model training period

The period during which the system will train the machine learning models based on the data that is collected from the agents, and will then create the normal behavior pattern of the workload. The longer the model training period, the more precise the long-term behavior pattern that the system will create. We recommend that the minimum model training period is twenty-one days.

Enter an integer value (days). The default value is 21.


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

Enter an integer value in the range 1-60 (min). The default value is 15.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.