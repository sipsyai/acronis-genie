# Pre-recovery command

Managing the backup and recovery of workloads and files > Recovery > Recovery options > Pre-recovery command
Pre-recovery command

To specify a command/batch file to be executed before the recovery process starts

Enable the Execute a command before the recovery switch.
In the Command... field, type a command or browse to a batch file. The program does not support interactive commands, i.e. commands that require user input (for example, "pause".)
In the Working directory field, specify a path to a directory where the command/batch file will be executed.
In the Arguments field specify the command’s execution arguments, if required.
Depending on the result you want to obtain, select the appropriate options as described in the table below.
Click Done.
Check box	Selection


Fail the recovery if the command execution fails*



Selected



Cleared



Selected



Cleared




Do not recover until the command execution is complete



Selected



Selected



Cleared



Cleared




Result




Preset

Perform the recovery only after the command is successfully executed. Fail the recovery if the command execution failed.

Perform the recovery after the command is executed despite execution failure or success.

N/A

Perform the recovery concurrently with the command execution and irrespective of the command execution result.

* A command is considered failed if its exit code is not equal to zero.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.