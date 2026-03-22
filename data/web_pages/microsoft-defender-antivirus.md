# Microsoft Defender Antivirus and Microsoft Security Essentials

Configuring your antivirus and antimalware protection > Microsoft Defender Antivirus and Microsoft Security Essentials
Microsoft Defender Antivirus and Microsoft Security Essentials
The availability of this feature depends on the service quotas that are enabled for your account.
Microsoft Defender Antivirus

Microsoft Defender Antivirus is a built-in antimalware component of Microsoft Windows that is delivered starting from Windows 8.

The Microsoft Defender Antivirus (WDA) module allows you to configure Microsoft Defender Antivirus security policy and track its status via the Cyber Protect console.

This module is applicable for the workloads on which Microsoft Defender Antivirus is installed.

If you enable Microsoft Defender Antivirus for real-time protection, the Real-time protection module is automatically disabled in order to prevent conflicts from occurring. Virus/malware detections and quarantine are handled by Microsoft Defender Antivirus, and any EDR incidents related to virus/malware detections are created from information provided by Microsoft Defender Antivirus. EDR includes other detection engines that can create other types of incidents without involvement from Microsoft Defender Antivirus.

Similarly, if you enable Real-time protection, the Microsoft Defender Antivirus module is automatically disabled.

The Tamper protection settings in Windows must also be disabled to ensure Microsoft Defender Antivirus works correctly in Cyber Protect Cloud. For more information, see this knowledge base article.

In addition, if Behavior engine or Antivirus & Antimalware protection are disabled in the protection plan when EDR is enabled, Endpoint Detection and Response (EDR) is also disabled.

Microsoft Security Essentials

Microsoft Security Essentials is a built-in antimalware component of Microsoft Windows that is delivered with Windows versions earlier than 8.

The Microsoft Security Essentials module allows you to configure Microsoft Security Essentials security policy and track its status via the Cyber Protect console.

This module is applicable for the workloads on which Microsoft Security Essentials is installed.

The settings for Microsoft Security Essentials are similar to the settings for Microsoft Defender Antivirus, but you cannot configure real-time protection, and cannot define exclusions via the Cyber Protect console.

Schedule scan

Specify the schedule for scheduled scanning.

Scan mode:

Full – a full check of all files and folders additionally to the items scanned in the quick scan. It required more machine resources for execution compared to the quick scan.
Quick – a quick check of the in-memory processes and folders where malware is typically found. It required less machine resources for execution.

Define the time and day of week when the scan will be performed.

Daily quick scan – define the time for the daily quick scan.

You can set the following options depending on your needs:

Start the scheduled scan when the machine is on but not in use

Check for the latest virus and spyware definitions before running a scheduled scan

Limit CPU usage during the scan to

For more details about the setting for Microsoft Defender Antivirus, refer to https://docs.microsoft.com/en-us/sccm/protect/deploy-use/endpoint-antimalware-policies#scheduled-scans-settings

Default actions

Define the default actions to be performed for the detected threats of different severity levels:

Clean – clean up the detected malware on a workload.
Quarantine – put the detected malware in the quarantine folder but do not remove it.
Remove – remove the detected malware from a workload.
Allow – do not remove or quarantine the detected malware.
User defined – a user will be prompted to specify the action to be performed with the detected malware.
No action – no actions will be taken.
Block – block the detected malware.

For more details about the default actions settings for Microsoft Defender Antivirus, refer to https://docs.microsoft.com/en-us/sccm/protect/deploy-use/endpoint-antimalware-policies#default-actions-settings

Real-time protection

Enable Real-time protection to detect and stop malware from installing or running on workloads.

Scan all downloads – if selected, scanning is performed for all downloaded files and attachments.

Enable behavior monitoring – if selected, behavior monitoring will be enabled.

Scan network files – if selected, network files will be scanned.

Allow full scan on mapped network drives – if selected, mapped network drives will be fully scanned.

Allow email scanning – if enabled, the engine will parse the mailbox and mail files, according to their specific format, in order to analyze the mail bodies and attachments.

For more details about the real-time protection settings for Microsoft Defender Antivirus, refer to https://docs.microsoft.com/en-us/sccm/protect/deploy-use/endpoint-antimalware-policies#real-time-protection-settings

Advanced

Specify the advanced scan settings:

Scan archive files – include archived files such as .zip or .rar files into scanning.
Scan removable drives – scan removable drives during full scans.
Create a system restore point – in some cases an important file or registry entry could be removed as "false positive", then you will be able to recover from a restore point.
Remove quarantined files after – define the period after which the quarantined files will be removed.

Send file samples automatically when a further analysis is required:

Always prompt – you will be asked for confirmation before file sending.
Send safe samples automatically – most samples will be sent automatically except files that may contain personal information. Such files will require additional confirmation.
Send all samples automatically – all samples will be sent automatically.
Disable Windows Defender Antivirus GUI – if selected, the WDA user interface will not be available to a user. You can manage the WDA policies via Cyber Protect console.

MAPS (Microsoft Active Protection Service) – online community that helps you choose how to respond to potential threats.

I don't want to join MAPS – no information will be sent to Microsoft about the software that was detected.
Basic membership – basic information will be sent to Microsoft about the software that was detected.
Advanced membership – more detailed information will be sent to Microsoft about the software that was detected.

For more details, refer to https://www.microsoft.com/security/blog/2015/01/14/maps-in-the-cloud-how-can-it-help-your-enterprise/

For more details about the advanced settings for Microsoft Defender Antivirus, refer to https://docs.microsoft.com/en-us/sccm/protect/deploy-use/endpoint-antimalware-policies#advanced-settings

Exclusions

You can define the following files and folders to be excluded from scanning:

Processes – any file that the defined process reads from or writes to will be excluded from scanning. You need to define a full path to the executable file of the process.
Files and folders – the specified files and folders will be excluded from scanning. You need to define a full path to a folder or file, or define the file extension.

For more details about the exclusion settings for Microsoft Defender Antivirus, refer to https://docs.microsoft.com/en-us/sccm/protect/deploy-use/endpoint-antimalware-policies#exclusion-settings

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.