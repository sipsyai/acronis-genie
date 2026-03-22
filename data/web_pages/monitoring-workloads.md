# Monitoring the health and performance of workloads

RMM > Monitoring the health and performance of workloads
Monitoring the health and performance of workloads

You can monitor the system parameters and the health of the workloads in your organization. If a parameter is out of norm, you will be notified immediately and will be able to quickly resolve the issue. You can also configure custom alerts and automatic response actions. These are actions that will be performed automatically to resolve anomalies in workload behavior.

The monitoring functionality requires an installation of Protection agent version 15.0.35324 or later on the workloads.

Monitoring plans

To start monitoring the performance, hardware, software, system, and security parameters of your managed workloads, apply a monitoring plan to them. The monitoring plans consist of different monitors that you can enable and configure. Some monitors support the anomaly-based monitoring type. For more information about monitoring plans, see Monitoring plans. For more information about the available monitors that you can configure in the monitoring plans, see Configurable monitors.

If the agent cannot collect data from a workload for some reason, the system will generate an alert.

Monitoring types

You must configure the monitoring type for each monitor that you enable in the plan. The monitoring type determines the algorithm that the monitor will use to estimate the normal behavior and deviation of the workload. There are two monitoring types: threshold-based and anomaly-based. Some monitors support only the threshold-based monitoring type.

Threshold-based monitoring tracks if the values of the parameters are above or below a threshold value that you configure. With this monitoring type, you are responsible for defining the correct threshold values for the workloads. The system determines the normal behavior based on these static threshold values and without considering other specific conditions that might cause the behavior. For this reason, threshold-based monitoring might be less accurate as compared to anomaly-based monitoring.

Anomaly-based monitoring uses machine learning to create the normal behavior patterns for a workload and to detect abnormal behavior. For more information, see Anomaly-based monitoring.

Anomaly-based monitoring

Supported platforms for monitoring

Configurable monitors

Monitoring plans

Monitoring alerts

Configuring email notification policies

Viewing monitor data

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.