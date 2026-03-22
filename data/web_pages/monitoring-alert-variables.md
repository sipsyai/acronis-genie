# Monitoring alert variables

RMM > Monitoring the health and performance of workloads > Monitoring alerts > Monitoring alert variables
Monitoring alert variables

You can configure different alert variables for different monitors. To use a variable, it must be enclosed in {{}}.

The following table provides more information about the available variables.

Variable	Description	Available for monitor
plan_name	The name of the policy	All monitors
monitor_name	The name of the sub policy in the monitoring plan	All monitors
workload_name	The name of the workload	All monitors
threshold_value	Specific monitoring conditions or thresholds for generating an alert	All monitors that support threshold-based monitoring.
threshold_unit	The unit that is associated with the threshold value. For example, %, MB, or mb/s.	All monitors that support threshold-based monitoring.
time_period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

All monitors that support threshold-based monitoring.
time_unit	The unit that will be associated with the time period (sec/min/hours/day).	All monitors that support threshold-based monitoring.
anomaly_value	The anomaly value	All monitors that support anomaly-based monitoring.
anomaly_unit	The unit that will be associated with the anomaly value	All monitors that support anomaly-based monitoring.
deviation_value	The deviation value	All monitors that support anomaly-based monitoring.
deviation_unit	The unit that will be associated with the deviation value	All monitors that support anomaly-based monitoring.
drive_name	The drive for Windows, or partition for macOS	Disk space,
CPU_model	The model of the monitored CPU	CPU temperature
GPU_model	The model of the monitored GPU	GPU temperature
hardware_model	The model of the monitored component	Hardware changes
hardware_component	The type of monitored hardware	Hardware changes
hardware_model_old	The model of the monitored component that was replaced	Hardware changes
hardware_model_new	The model of the new monitored component that was added	Hardware changes
disk_model	The model of the disk	Disk transfer rate
network_adapter_model	The model of the network adapter	Network usage
process_name	The name of the process

CPU usage by process

Memory usage by process

Disk transfer rate by process

Network usage by process

Process status


service_name	The name of the service

Windows service status


software_name	The name of the software application	Installed software
software_version	The version of the software application	Installed software
software_version_old	The version of the software application before the update	Installed software
software_version_new	The version of the new or updated software application	Installed software
number_of_occurrences	The number of times an event appears in the log	Windows event log
event_types	The type of the event	Windows event log
event_source	The source of the event	Windows event log
event_log_name	The name of the event	Windows event log
firewall_software_name	The name of the firewall software	Firewall status
antimalware_software_name	The name of the antimalware software	Antimalware software status
user_name	The name of the user	AutoRun feature status
script_name	The name of the script	Custom
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.