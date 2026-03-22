# Changing the recovery environment

Managing the backup and recovery of workloads and files > Recovery > Recovery with restart > Changing the recovery environment
Changing the recovery environment

You can change the default recovery environment on Windows workloads.

On Linux workloads, only the Linux recovery environment is available.

To set WinRE
To set Linux
To reset the default settings
In Windows, open Regedit.
Go to HKEY_LOCAL_MACHINE\SOFTWARE\Acronis\BackupAndRecovery\Settings.
Create a new string value, and then name it RebootEnvironmentType.
Open the string value for editing.
In Value data, specify Windows.
Click OK.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.