# Self-protection

Configuring your antivirus and antimalware protection > Antivirus and antimalware protection > Antivirus and antimalware protection settings > Self-protection
Self-protection

Self-protection prevents unauthorized changes to the software's own processes, registry records, executable and configuration files, and backups located in your local folders.

Administrators can enable Self-protection, without enabling Active Protection.

Default setting: On.

Self-protection is not supported for Linux.

To enable Self-protection

In the Create protection plan window, expand the Antivirus & Antimalware protection module.
Click Self-protection.
Use the Self-protection toggle to enable it.
Agent uninstallation protection

The Agent uninstallation protection setting prevents users or software from uninstalling Agent for Windows or modifying its components outside the configured maintenance window.

Default setting: Enabled

To disable Agent uninstallation protection

Disabling the Agent uninstallation protection setting puts the protected workloads at security risk.
When the Self-protection feature is enabled, clear the Agent uninstallation protection checkbox.
Click Done.
This option does not prevent automatic updates of the Cyber Protection agent.

Every attempt to uninstall or modify the protection agent outside the maintenance window triggers an alert.

An administrator user can review the alert and decide whether to allow modifications to the agent for 1 hour, or configure a maintenance window with duration between 1 hour and 7 days. See To allow the modification of an agent with uninstallation protection enabled.

Allowing processes to modify backups

The Allow specific processes to modify backups setting is only available when the Self-protection setting is enabled.

It applies to files in local folders with the following extensions:

.tibx
.tib
.tia

The Allow specific processes to modify backups setting lets you specify the processes that are allowed to modify the backup files, even though these files are protected by self-protection. This is useful, for example, if you remove backup files or move them to a different location by using a script.

When this setting is disabled, the backup files can be modified only by processes signed by the backup software vendor. This allows the software to apply retention rules and to remove backups when a user requests this from the web interface. Other processes, no matter suspicious or not, cannot modify the backups.

When this setting is enabled, you can allow other processes to modify the backups.

Default setting: Disabled.

To enable Allow specific processes to modify backups

When the Self-protection feature is enabled, select the Allow specific processes to modify backups checkbox.
In the Process to modify backups field, click Add.
Enter the full path to the process executable, starting with the drive letter.

Click the check mark to the right to save the process.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.