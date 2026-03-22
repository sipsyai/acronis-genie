# Post-data capture command

Managing the backup and recovery of workloads and files > Backup options > Pre/Post data capture commands > Post-data capture command
Post-data capture command

To specify a command or a batch file to be executed after data capture

Enable the Execute a command after the data capture switch.

In the Command or batch file path on the machine with an agent field, type a command or browse to a batch file.

Commands that require user input (for example, pause) are not supported.

If you use PowerShell, pass the command as an argument to powershell.exe.

For example, use:

powershell.exe -C "New-Item -Force -ItemType file -Path 'C:\temp\file.txt'"

instead of:

New-Item -Force -ItemType file -Path 'C:\temp\file.txt'
In the Working directory field, specify a path to a directory where the command or the batch file will be executed.
In the Arguments field, specify arguments for the command, if required.
Depending on the result you want to obtain, select the appropriate options as described in the table below.
Click Done.
Check box	Selection


Fail the backup if the command execution fails*



Selected



Cleared



Selected



Cleared




Do not back up until the command execution is complete



Selected



Selected



Cleared



Cleared




Result




Preset

Continue the backup only after the command is successfully executed.

Continue the backup after the command is executed despite command execution failure or success.	N/A	Continue the backup concurrently with the command execution and irrespective of the command execution result.

* A command is considered failed if its exit code is not equal to zero.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.