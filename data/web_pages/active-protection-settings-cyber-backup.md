# Active Protection settings in Cyber Backup Standard

Configuring your antivirus and antimalware protection > Active Protection in the Cyber Backup Standard edition > Active Protection settings in Cyber Backup Standard
Active Protection settings in Cyber Backup Standard

In the Cyber Backup Standard edition, you can configure the following Active Protection features:

Action on detection
Self-protection
Network folder protection
Server-side protection
Cryptomining process detection
Exclusions
Active Protection for Linux supports the following settings: Action on detection, Network folder protection, and Exclusions. Network folder protection is always on and not configurable.
Action on detection

In the Action on detection section, select one of the available options:

Notify only

The software will generate an alert about the process suspected of ransomware activity.

Stop the process

The software will generate an alert and stop the process suspected of ransomware activity.

Revert using cache

The software will generate an alert, stop the process, and revert the file changes by using the service cache.

Default setting: Revert using cache.

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

Network folder protection

The Protect network folders mapped as local drives setting defines whether Active protection protects from local malicious processes network folders that are mapped as local drives.

This setting applies to folders shared via SMB or NFS protocols.

If a file was originally located on a mapped drive, it cannot be saved to the original location when extracted from the cache by the Revert using cache action. Instead, it will be saved to the folder specified in this setting. The default folder is C:\ProgramData\Acronis\Restored Network Files for Windows, and Library/Application Support/Acronis/Restored Network Files/ for macOS. If this folder does not exist, it will be created. If you want to change this path, specify a local folder. Network folders, including folders on mapped drives, are not supported.

Default setting: On.

Server-side protection

This feature defines whether Active Protection protects network folders that are shared by you from the external incoming connections from other servers in the network that may potentially bring threats.

The availability of this feature depends on the service quotas that are enabled for your account.

Default setting: Off.

The availability of this feature depends on the license that you have.
Server-side protection is not supported for Linux.

To set trusted connections

In the Create protection plan window, expand the Antivirus & Antimalware protection module.
Click Server-side protection.
Use the Server-side protection toggle to enable it.
Select the Trusted tab.
In the Trusted connections field, click Add to define connections that will be allowed to modify data.
In the ComputerName/Account field, type the name of the computer and the account of the machine where the protection agent is installed. For example, MyComputer\TestUser.
In the Host name field, type the host name of the machine that is allowed to connect to the machine using the protection agent.

Click the check mark to the right to save the connection definition.

Click Done.

To set blocked connections

In the Create protection plan window, expand the Antivirus & Antimalware protection module.
Click Server-side protection.
Use the Server-side protection toggle to enable it.
Select the Blocked tab.
In the Blocked connections field, click Add to define connections that will not be allowed to modify data.
In the ComputerName/Account field, type the name of the computer and the account of the machine where the protection agent is installed. For example, MyComputer\TestUser.
In the Host name field, type the host name of the machine that is allowed to connect to the machine using the protection agent.

Select the check box to the right to save the connection definition.

Click Done.
Cryptomining detection

Cryptomining malware degrades the performance of useful applications, increases electricity bills, and may cause system crashes and even hardware damage due to abuse. The Cryptomining process detection feature protects your devices against cryptomining malware to prevent unsanctioned using of computer resources.

Administrators can enable Cryptomining process detection, without enabling Active Protection. Default setting: Enabled.

The availability of this feature depends on the license that you have.
Cryptomining process detection is not supported for Linux.

To configure Cryptomining process detection

In the Create protection plan window, expand the Antivirus & Antimalware protection module.
Click Cryptomining process detection.
Use the Detect cryptomining processes toggle to enable or disable the feature.
Select what to do with processes suspected of cryptomining activities:

Default setting: Stop the process

Notify only—The software generates an alert.

Stop the process — The software generates an alert and stops the process.

Click Done to apply the selected options to your protection plan.
Exclusions

Protection exclusions enable you to eliminate false positives when a trusted program is considered ransomware or malware. You can define trusted and blocked items by adding them to the protection exclusions list.

In the trusted items list, you can add files, processes, and folders to consider them as safe in the system, and to prevent any future detections for these.

In the blocked items list, you can add processes and hashes. This option guarantees that those processes will be blocked, and your workload will be safe.

Default setting: No exclusions are defined by default.

Protection exclusion item	Blocked	Trusted
Hash

When a hash is added to the blocked list, the system will stop the process, based on the provided hash.

For example, when you add this MD5 hash, 938c2cc0dcc05f2b68c4287040cfcf71, the process associated with this hash will be blocked.



When a hash is added to the trusted list, the system will know what processes have to be ignored by monitoring, based on the provided hash.

For example, when you add this MD5 hash, 938c2cc0dcc05f2b68c4287040cfcf71, the process associated with this hash will be trusted and excluded from monitoring.


Process

When a process is added to the blocked list, the system will know that those processes must to be monitored, and the processes will always be blocked.

For example, if you add this path C:\Users\user1\application\nppInstaller.exe to the blocked list, this specific process will be blocked, and when you will try to open it, it will not be allowed to start.



When a process is added to the trusted list, the system will exclude that process from monitoring.

For example, if you add this path: C:\Users\user1\application\nppInstaller.exe, this specific process will be excluded from monitoring, and antivirus will not interfere with this process. If you add this expression: C:\Users\user1\application\*.exe, all processes in the application folder will be excluded.

Processes signed by Microsoft are always trusted.

File/folder	 	When a file or a folder is added to the trusted list, the system will know that those files or folders should always be considered safe, and there is no need for those to be scanned/monitored.

To specify the items that will always be trusted

Open the protection plan for editing.

For example, click the ellipsis (...) next to the name of the protection plan and select Edit.

Expand the Antivirus and Antimalware protection module.
Select the Exclusions option.

The Protection exclusions window opens.

In the Trusted items section, click Add to select from the available options:
To trust files, folders, or processes, select the File/folder/process option. The Add file/folder/process window opens.
In the File/process/folder field, enter the path for each process, folder, or file on a new line.
Select the Add as file/folder checkbox to trust the file/folder.

Examples of folder description: D:\folder\, /home/Folder/folder2, F:\

Select the Add as process checkbox to trust a process. The selected processes will be excluded from monitoring.

You can specify the full path to a process or use wild card. For example, to exclude all processes in the Temp folder, you can enter C:\Windows\Temp\*.exe.

Local network paths are also supported. For example, \\localhost\folderpath\file.exe

To add MD5 hashes to the list of trusted items, select the Hash option. The Add hash window opens.
Here, you can insert MD5 hashes on separate lines to be included as trusted in the Protection exclusions list. Based on these hashes, Cyber Protection will exclude the processes described by the MD5 hashes from being monitored.

In the Description field, enter a short description, so that you can recognize your change in the list of trusted items. For example, reasons and purposes for the exclusion, time stamps, and so on.

If there are multiple items added in a single entry, there can only be one comment captured for the multiple items.

Click Add, and then click Done.

To specify the items that will always be blocked

Open the protection plan.
Expand the Antivirus and Antimalware protection module.
Select the Protection exclusions option.

The Protection exclusions window opens.

In the Blocked items section, click Add and select from the available options:
To block processes, select the Process option. The Add process window opens.
In the Process field, enter the path for each process on a new line.
These processes will not be able to start as long as Active Protection is enabled on the machine.
To block hashes, select the Hash option. The Add hash window opens.
In the Hash field, enter the hash for each process on a new line.

In the Description field, enter a short description, so that you can recognize your change in the list of blocked items. For example, reasons and purposes for the exclusion, time stamps, and other.

If there are multiple items added in a single entry, there can only be one comment captured for the multiple items.

Click Add, and then click Done.

Using wildcards to define exclusions

To define exclusions, you can use the wildcard characters * and ?. The asterisk (*) substitutes for zero or more characters. The question mark (?) substitutes for zero or exactly one character. Environment variables, such as %AppData%, cannot be used.

You can use a wildcard (*) to add items to the exclusion lists.

Wildcards can be used in the middle or the end of a description.

Examples of accepted wildcards in descriptions:

C:\*.pdf

D:\folders\file.*

C:\Users\*\AppData\Roaming

Wildcards cannot be used at the beginning of a description.

Examples of unaccepted wildcards in descriptions:

*.docx

*:\folder\

Using variables to define exclusions

You can also use variables to add items to the Protection exclusions list, with the following limitations:

For Windows, only SYSTEM variables are supported. User specific variables, for example, %USERNAME%, %APPDATA% are not supported. Variables with {username} are not supported. For more information, see https://ss64.com/nt/syntax-variables.html.
For macOS, environment variables are not supported.
For Linux, environment variables are not supported.

Examples of supported formats:

%WINDIR%\Media
%public%
%CommonProgramFiles%\Acronis\
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.