# Configuring monitoring alerts

RMM > Monitoring the health and performance of workloads > Monitoring alerts > Configuring monitoring alerts
Configuring monitoring alerts

You can configure the monitor's alert settings when you add a monitor to a monitoring plan, or when you edit a monitor that is already available in a monitoring plan.

To configure monitoring alerts

In the Monitor parameters window, go to the Generate alerts section.

In Alert severity, select the severity that corresponds to the priority of the alert.

Option	Description
Critical	These alerts have the highest priority and are related to issues that are critical for the operation of the workload. Resolve these issues as soon as possible.
Error	An error alert is less severe and indicates that something is wrong or is not behaving normally. Resolve the issues on time to prevent them causing more severe issues.
Warning

A warning alert indicates that there is some condition of which you should be aware, but it might not be causing a problem yet. Resolve these issues after you fix the issues that are causing critical and error alerts.

This is the default value.


Informational	These alerts have the lowest priority. The Informational severity does not indicate a problem. Such alerts provide information about actions that are related to a monitored object.

In Alert frequency, select how often the system should generate an alert when the condition is met.

Option	Description
Once until the check passes

The system will generate an alert one time until the check completes successfully.

This is the default value.


After X consecutive failures	The system will generate an alert after X consecutive failed checks, where X is an integer value.

In Alert message, click the pencil icon to edit the default alert message that will be used when the system generates an alert. You can specify a custom alert message that contains variables. For more information about the variables that you can use, see Monitoring alert variables.

You can configure more than one alert message for some of the monitors.

Enable Alert auto-resolution, if you want the system to automatically resolve the alert when the monitored metric returns to normal state and the behavior is normal again. By default, the setting is enabled.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.