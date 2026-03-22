# Post-backup command

Managing the backup and recovery of workloads and files > Backup options > Pre/Post commands > Post-backup command
Post-backup command

To specify a command or batch file to be executed after the backup completes

Enable the Execute a command after the backup switch.

In the Command or batch file path on the machine with an agent field, type a command or browse to a batch file.

Commands that require user input (for example, pause) are not supported.

If you use PowerShell, pass the command as an argument to powershell.exe.

For example, use:

powershell.exe -C "New-Item -Force -ItemType file -Path 'C:\temp\file.txt'"

instead of:

New-Item -Force -ItemType file -Path 'C:\temp\file.txt'
In the Working directory field, specify a path to a directory where the command or the batch file will be executed.
In the Arguments field, specify arguments for the command, if required.

If successful execution of the command is critical, select the Fail the backup if the command execution fails checkbox.

A command is considered failed if its exit code is not equal to zero. If the command execution fails, the backup status is set to Error.

If the Fail the backup if the command execution fails checkbox is not selected, the result of the command execution does not affect the backup status.

You can check the result of the command execution on the Activities tab.

Click Done.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.