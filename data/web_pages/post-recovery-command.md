# Post-recovery command

Managing the backup and recovery of workloads and files > Recovery > Recovery options > Post-recovery command
Post-recovery command

To specify a command/executable file to be executed after the recovery is completed

Enable the Execute a command after the recovery switch.
In the Command... field, type a command or browse to a batch file.
In the Working directory field, specify a path to a directory where the command/batch file will be executed.
In the Arguments field, specify the command execution arguments, if required.

Select the Fail the recovery if the command execution fails check box if successful execution of the command is critical for you. The command is considered failed if its exit code is not equal to zero. If the command execution fails, the recovery status will be set to Error.

When the check box is not selected, the command execution result does not affect the recovery failure or success. You can track the command execution result by exploring the Activities tab.

Click Done.

A post-recovery command will not be executed if the recovery proceeds with reboot.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.