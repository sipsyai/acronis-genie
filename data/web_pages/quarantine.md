# Quarantine

Configuring your antivirus and antimalware protection > Quarantine
Quarantine

Quarantine is a special, isolated folder on the hard disk of a protected device. If Antivirus &amp; Antimalware protection detects any suspicious files, they are moved in Quarantine to prevent any further spread of threats.

In the Quarantine tab of the Cyber Protection console, you can review suspicious and potentially dangerous files from all protected devices, and decide whether to remove or restore them.

The quarantined files are automatically removed if the device is removed from the environment.
How do files get into the quarantine folder?
In the protection plan, select Quarantine as the default action for infected or suspicious files.

To learn how to create a protection plan, see Creating a protection plan.

While scanning, the Antivirus & Antimalware protection module detects malicious files, and moves them to the secure Quarantine folder.
The module updates the quarantine list to add information about files that were moved to Quarantine.
Files are automatically deleted from the Quarantine folder after the time period defined in the Remove quarantined files after setting in the protection plan. See Quarantine settings.
Managing quarantined files

To manage the quarantined files, go to Protection > Quarantine. The list of quarantined files from all protected devices contains the following information.

Name	Description


File

The name of the quarantined file.


Date quarantined

The date and time when the file was moved in quarantine.


Device

The device on which the infected file was found.


Threat name

The threat name.


Protection plan

The protection plan according to which the suspicious file was moved to Quarantine.

You can perform the following actions on quarantined files:

Delete – permanently remove a quarantined file from all machines. You can delete all files with the same file hash. You can restore all files with the same file hash. Group the files by hash, select needed files and then delete them.
Restore – restore a quarantined file to its original location without any modifications. If there is currently a file with the same name in the original location, then it will be overwritten with the restored file.
The restored file will be added to the allowlist and skipped during further antimalware scans.

Quarantine location on machines

Below is a list of default locations for quarantined files per operating system.

For Windows machines: %programdata%\Acronis\NGMP\quarantine
For Mac machines: /Library/Application Support/Acronis/NGMP/quarantine
For Linux machines: /var/lib/Acronis/NGMP/quarantine

The quarantine storage is under the service provider's self-defense protection.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.