# Error Handling Recovery

Managing the backup and recovery of workloads and files > Recovery > Recovery options > Error handling
Error handling

These options enable you to specify how to handle errors that might occur during recovery.

Re-attempt, if an error occurs

The preset is: Enabled. Number of attempts: 30. Interval between attempts: 30 seconds.

When a recoverable error occurs, the program re-attempts to perform the unsuccessful operation. You can set the time interval and the number of attempts. The attempts will be stopped as soon as the operation succeeds OR the specified number of attempts are performed, depending on which comes first.

Do not show messages and dialogs while processing (silent mode)

The preset is: Disabled.

With the silent mode enabled, the program will automatically handle situations requiring user interaction where possible. If an operation cannot continue without user interaction, it will fail. Details of the operation, including errors, if any, can be found in the operation log.

Ignore errors

This option is effective for file-level recovery.

The preset is: Enabled.

When this option is enabled and recovery of a file fails, the recovery operation will continue for the rest of the files. A warning will be displayed on the Activities screen. The option Re-attempt, if an error occurs will not be triggered because an error is not logged.

When this option is disabled and recovery of a file fails, the recovery operation will fail. An error will be displayed on the Activities screen.

Save system information if a recovery with reboot fails

This option is effective for a disk or volume recovery to a physical machine running Windows or Linux.

The preset is: Disabled.

When this option is enabled, you can specify a folder on the local disk (including flash or HDD drives attached to the target machine) or on a network share where the log, system information, and crash dump files will be saved. This file will help the technical support personnel to identify the problem.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.