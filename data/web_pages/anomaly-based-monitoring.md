# Anomaly-based monitoring

RMM > Monitoring the health and performance of workloads > Anomaly-based monitoring
Anomaly-based monitoring

Anomaly-based monitoring uses machine learning models to create the normal behavior patterns for a workload and to detect anomalies (unexpected spikes in the time-series data) in the workload's behavior. When you activate this monitoring type, the system creates a model and starts training itself and adjusting the model for the specific workload based on the data that it collects from the workload. This means that at the beginning of the training period, the data might not be fully accurate. Creating a reliable model requires at least three weeks of training of the model. As the system collects more data and analyzes historical data sets, it gradually refines the model and creates the dynamic upper and lower thresholds for each metric of the workload. This monitoring type is more flexible as compared to the threshold-based monitoring because the system monitors the values of the parameters and their context. For example, it might be normal for a specific workload to have bigger load in certain hours of the day. A threshold-based monitoring type would falsely interpret this as an abnormal behavior and would trigger an alert.

You can reset the machine learning models of a workload. In this case, the system will delete all data and models for the monitors that are applied to the workload. For more information, see Resetting the machine learning models.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.