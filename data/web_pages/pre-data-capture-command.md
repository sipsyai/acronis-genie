# Pre-data capture command

Managing the backup and recovery of workloads and files > Backup options > Pre/Post data capture commands > Pre-data capture command
Pre-data capture command

To specify a command or batch file to be executed before data capture

Enable the Execute a command before the data capture switch.

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




Do not perform the data capture until the command execution is complete



Selected



Selected



Cleared



Cleared




Result




Preset

Perform the data capture only after the command is successfully executed. Fail the backup if the command execution fails.

Perform the data capture after the command is executed despite execution failure or success.	N/A	Perform the data capture concurrently with the command and irrespective of the command execution result.

* A command is considered failed if its exit code is not equal to zero.

If a script fails due to a conflict related to a required library version in Linux, exclude the LD_LIBRARY_PATH and LD_PRELOAD environmental variables, by adding the following lines in your script:

#!/bin/sh
unset LD_LIBRARY_PATH
unset LD_PRELOAD
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.