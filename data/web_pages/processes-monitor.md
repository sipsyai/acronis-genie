# Settings of the Process status monitor

RMM > Monitoring the health and performance of workloads > Configurable monitors > Settings of the Process status monitor
Settings of the Process status monitor

Process status monitors whether the selected process is running or stopped. If there are multiple instances of the same process, the system will monitor each instance of the process and will generate the alert when the conditions are met for all instances of the process.

You can configure the following settings for the monitor.

Setting	Description
Process name

The name of the process that you want to monitor. Enter the name of the executable file without the extension.


Process status

If the process is in the selected status, the system will generate an event.

The following values are available.

Running
Stopped—This is the default value.

Time period

The system will generate an alert for a detected issue only if the metric value is out of the norm during the specified period.

Enter an integer value in the range 1-60 (min). The default value is 1.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.