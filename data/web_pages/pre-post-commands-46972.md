# Pre Post Commands 46972

Managing the backup and recovery of workloads and files > Backup options > Pre/Post commands
Pre/Post commands

The option enables you to define the commands to be automatically executed before and after the backup procedure.

The following scheme illustrates when pre/post commands are executed.

Pre-backup command	Backup	Post-backup command

Examples of how you can use the pre/post commands:

Delete some temporary files from the disk before starting backup.
Configure a third-party antivirus product to be started each time before the backup starts.
Selectively copy backups to another location. This option may be useful because the replication configured in a protection plan copies every backup to subsequent locations.

The agent performs the replication after executing the post-backup command.

The program does not support interactive commands, i.e. commands that require user input (for example, "pause").

Pre-backup command

Post-backup command




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.