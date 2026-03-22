# Performance and backup window

Managing the backup and recovery of workloads and files > Backup options > Performance and backup window
Performance and backup window

This option enables you to set one of three levels of backup performance (high, low, prohibited) for every hour within a week. This way, you can define a time window when backups are allowed to start and run. The high and low performance levels are configurable in terms of the process priority and output speed.

This option is not available for backups executed by the cloud agents, such as website backups or backups of servers located on the cloud recovery site.

This option is effective only for the backup and backup replication processes. Post-backup commands and other operations included in a protection plan (for example, validation) will run regardless of this option.

The preset is: Disabled.

When this option is disabled, backups are allowed to run at any time, with the following parameters (no matter if the parameters were changed against the preset value):

CPU priority: Low (in Windows, it corresponds to Below normal)
Output speed: Unlimited

When this option is enabled, scheduled backups are allowed or blocked according to the performance parameters specified for the current hour. At the beginning of an hour when backups are blocked, a backup process is automatically stopped and an alert is generated. Even if scheduled backups are blocked, a backup can be started manually. It will use the performance parameters of the most recent hour when backups were allowed.

You can configure performance and backup window for every replication location individually. To access the settings of the replication location, in the protection plan, click the gear icon next to the location name, and then click Performance and backup window.
Backup window

Each rectangle represents an hour within a week day. Click a rectangle to cycle through the following states:

Green: backup is allowed with the parameters specified in the green section below.

Blue: backup is allowed with the parameters specified in the blue section below.

This state is not available if the backup format is set to Version 11.

Gray: backup is blocked.

You can click and drag to change the state of multiple rectangles simultaneously.

CPU priority

This parameter defines the priority of the backup process in the operating system.

The available settings are: Low, Normal, High.

The priority of a process running in a system determines the amount of CPU and system resources allocated to that process. Decreasing the backup priority will free more resources for other applications. Increasing the backup priority might speed up the backup process by requesting the operating system to allocate more resources like the CPU to the backup application. However, the resulting effect will depend on the overall CPU usage and other factors like disk in/out speed or network traffic.

This option sets the priority of the backup process (service_process.exe) in Windows and the niceness of the backup process (service_process) in Linux and macOS.

The table below summarizes the mapping for this setting in Windows, Linux, and macOS.

Cyber Protection priority

Windows
priority



Linux and macOS
niceness


Low	Below normal	10
Normal	Normal	0
High	High	-10
Output speed during backup

This parameter enables you to limit the hard drive writing speed (when backing up to a local folder) or the speed of transferring the backup data through the network (when backing up to a network share or to cloud storage).

When this option is enabled, you can specify the maximum allowed output speed:

As a percentage of the estimated writing speed of the destination hard disk (when backing up to a local folder) or of the estimated maximum speed of the network connection (when backing up to a network share or cloud storage).

This setting works only if the agent is running in Windows.

In KB/second (for all destinations).
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.