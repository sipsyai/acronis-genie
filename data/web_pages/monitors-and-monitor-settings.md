# Configurable monitors

RMM > Monitoring the health and performance of workloads > Configurable monitors
Configurable monitors

The monitoring functionality supports the following monitors, divided into six categories: Hardware, Performance, Software, System, Security, and Custom.

Monitor	Description	Supported operating systems	Frequency of data collection	Support of anomaly-based monitoring

Availability


Hardware
Disk space	Monitors the free space on a specific drive of the workload.

Windows

macOS

1 minute	Yes

Standard protection (service-based licensing mode)

Security and RMM (solution-based licensing mode)


CPU temperature	Monitors the CPU temperature.

Windows

macOS

30 sec	Yes

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


GPU temperature	Monitors the GPU temperature.

Windows

macOS

30 sec	Yes

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Hardware changes	Monitors the hardware changes, such as adding, removing, or replacing hardware on a workload

Windows

macOS

24 hours	No

Standard protection (service-based licensing mode)

Security and RMM (solution-based licensing mode)


Performance
CPU usage	Monitors the overall CPU usage (by all CPUs on the workload).

Windows

macOS

30 sec	Yes

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Memory usage	Monitors the overall memory usage (by all memory slots on the workload).

Windows

macOS

30 sec	Yes

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Disk transfer rate	Monitors the read and write speed of each physical disk on the workload.

Windows

macOS

30 sec	Yes

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Network usage	Monitors the incoming and outgoing traffic for each network adapter of the workload.

Windows

macOS

30 sec	Yes

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


CPU usage by process	Monitors the CPU usage by certain process.

Windows

macOS

30 sec	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Memory usage by process	Monitors the memory usage by the selected process.

Windows

macOS

30 sec	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Disk transfer rate by process	Monitors the read and write speed of the selected process.

Windows

macOS

30 sec	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Network usage by process	Monitors the incoming and outgoing traffic of the selected process.

Windows

macOS

30 sec	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Software
Windows service status	Monitors the status of the selected Windows service (Running or Stopped).	Windows	30 sec	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Process status	Monitors the status of the selected process (Running or Stopped).

Windows

macOS

30 sec	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Installed software	Monitors the installation, update, or deletion of software applications.

Windows

macOS

24 hours	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


System
Last system restart	Monitors when the workload was restarted.

Windows

macOS

1 hour	No

Standard protection (service-based licensing mode)

Security and RMM (solution-based licensing mode)


Windows event log	Monitors specific business-critical events in the Windows event logs.

Windows

10 min	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Files and folders size	Monitors the total size of the selected files or folders.

Windows

macOS

10 min	No

Standard protection (service-based licensing mode)

Security and RMM (solution-based licensing mode)


Security
Windows Update status	Monitors the Windows Update status of the workload and whether the latest updates are installed.	Windows	15 min	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Firewall status	Monitors the status of the built-in or third-party firewall that is installed on the workload.

Windows

macOS

5 min	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Antimalware software status	Monitors the status of the built-in or third-party antimalware software that is installed on the workload.

Windows

macOS

5 min	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Failed logins	Monitors unsuccessful login attempts on the workload.

Windows

1 hour	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


AutoRun status	Monitors if the AutoRun feature for removable storage media is enabled.

Windows

1 hour	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)


Custom
Custom	Monitors custom objects via running scripts.

Windows

macOS

custom	No

Security and RMM (solution-based licensing mode)

RMM service (service-based licensing mode)

Settings of the Disk space monitor

Settings of the CPU temperature monitor

Settings of the GPU temperature monitor

Settings of the Hardware changes monitor

Settings of the CPU usage monitor

Settings of the Memory usage monitor

Settings of the Disk transfer rate monitor

Settings of the Network usage monitor

Settings of the CPU usage by process monitor

Settings of the Memory usage by process monitor

Settings of the Disk transfer rate by process monitor

Settings of the Network usage by process monitor

Settings of the Windows service status monitor

Settings of the Process status monitor

Settings of the Installed software monitor

Settings of the Last system restart monitor

Settings of the Windows event log monitor

Settings of the Files and folders size monitor

Settings of the Windows Update status monitor

Settings of the Firewall status monitor

Settings of the Failed logins monitor

Settings of the Antimalware software status monitor

Settings of the AutoRun feature status monitor

Settings of the Custom monitor

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.