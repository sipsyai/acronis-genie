# Configuring a CDP backup

Managing the backup and recovery of workloads and files > Continuous data protection (CDP) > Configuring a CDP backup
Configuring a CDP backup

You can configure Continuous data protection in the Backup module of a protection plan. For more information on how to create a protection plan, refer to Creating a protection plan.

To configure the Continuous data protection settings

In the Backup module of a protection plan, enable the Continuous data protection (CDP) switch.

This switch is available only for the following data sources:

Entire machine

Disk/volumes

Files/folders

In Items to protect continuously, configure Continuous data protection for Applications or Files/folders, or both.

Click Applications to configure CDP backup for files that are modified by specific applications.

You can select applications from predefined categories or add other applications by specifying the path to the their executable file, for example:

C:\Program Files\Microsoft Office\Office16\WINWORD.EXE
*:\Program Files (x86)\Microsoft Office\Office16\WINWORD.EXE

Click Files/folders to configure CDP backup for files in specific locations.

You can define these locations by using selection rules or by selecting the files and folders directly.

[For all machines] To create a selection rule, use the text box.

You can use the full paths to files or paths with wildcard characters (* and ?). The asterisk matches zero or more characters. The question mark matches a single character.

To create a CDP backup for a folder, you must specify its content by using the asterisk wildcard character:

Correct path: D:\Data\*

Incorrect path: D:\Data\

[For online machines] To select files and folders directly:
In Machine to browse from, select the machine on which the files or folders reside.

Click Select files and folders to browse the selected machine.

Your direct selection creates a selection rule. If you apply the protection plan to multiple machines and a selection rule is not valid for a machine, it will be skipped on this machine.

In the protection plan pane, click Create.

As a result, the data that you specified will be backed up continuously between the scheduled backups.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.