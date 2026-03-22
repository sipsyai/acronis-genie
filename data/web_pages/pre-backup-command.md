# Pre-backup command

Managing the backup and recovery of workloads and files > Backup options > Pre/Post commands > Pre-backup command
Pre-backup command

To specify a command or batch file to be executed before the backup starts

Enable the Execute a command before the backup switch.

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

Perform the backup only after the command is successfully executed. Fail the backup if the command execution fails.

Perform the backup after the command is executed despite execution failure or success.	N/A	Perform the backup concurrently with the command execution and irrespective of the command execution result.

* A command is considered failed if its exit code is not equal to zero.

If a script fails due to a conflict related to a required library version in Linux, exclude the LD_LIBRARY_PATH and LD_PRELOAD environmental variables, by adding the following lines in your script:

#!/bin/sh
unset LD_LIBRARY_PATH
unset LD_PRELOAD
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.