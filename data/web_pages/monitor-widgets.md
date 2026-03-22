# Monitor widgets

RMM > Monitoring the health and performance of workloads > Viewing monitor data > Monitor widgets
Monitor widgets

In the monitor widget, you can see the following details about the monitor.

Detail	Description
Monitoring plan	The name of the monitoring plan that contains the monitor. The name of the monitoring plan is a link that opens the monitoring plan in view mode.
Monitor frequency	The time interval at which the monitor collects data from the workload
Last result

The latest value of the monitored metric or the latest state of the event


Last check	The date and time when the monitor collected the last data
Last alert	The date and time when the last alert was generated. The field is displayed only if at least one alert has been generated for the monitor.
Historical graph

For monitors that collect time-series data, the widget displays historical data for a selected period (1 hour, 6 hours, 12 hours, 1 day, 1 week, or 1 month) in a graphical view.

The graph displays the actual values of the metrics during a period that you select. If for some reason the agent did not send the collected data to the cloud, the missing values are displayed as a dotted line that connects the data points with actual values that precede and follow the missing value.

For monitors that are using Anomaly-based monitoring, the graph displays the baselines area, a line that shows the actual values of the metric, and the anomalies. The anomalies are the spikes or values that are out of the baselines and are displayed as red dots on the graph.

If you hover the mouse over the graph, you can see the actual value and the threshold values for a specific time.

The data on the graphs is displayed in the time zone of the local system. That is the time zone of the browser of the workload from which you access the Protection console.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.