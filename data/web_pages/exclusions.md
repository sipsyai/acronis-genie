# Protection exclusions

Configuring your antivirus and antimalware protection > Antivirus and antimalware protection > Antivirus and antimalware protection settings > Protection exclusions
Protection exclusions

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