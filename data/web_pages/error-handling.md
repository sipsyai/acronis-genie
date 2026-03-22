# Error handling

Managing the backup and recovery of workloads and files > Backup options > Error handling
Error handling

These options enable you to specify how to handle errors that might occur during backup.

Re-attempt, if an error occurs

The preset is: Enabled. Number of attempts: 30. Interval between attempts: 30 seconds.

When a recoverable error occurs, Cyber Protect re-attempts to perform the unsuccessful operation. You can set the maximum number of re-attempts and the interval between them. If the operation cannot finish successfully after the maximum number of re-attempts, it fails.

For backups to a network location or a cloud storage (Acronis Cloud storage or a public cloud storage, such as Amazon, Azure, S3-compatible, or Impossible Cloud), the error handling depends on the moment when the error occurs.

Error occurs when the backup starts	Error occurs during an ongoing backup


The number of re-attempts depends on the response from the storage API. If the API returns a response that is considered as retriable (for example, error "503 Service unavailable"), it might take up to two hours for the operation to fail.

Typically, this scenario is more likely for a cloud storage than for a network location.



The number of retries depends on the Error handling settings that are configured in the protection plan.

For example, 30 retries with 30-second interval between each retry.

For backups to local folders, the Error handling settings only apply to errors that occur during an ongoing backup. If an error occurs when the backup starts, the backup operation fails immediately.

Do not show messages and dialogs while processing (silent mode)

The preset is: Enabled.

With the silent mode enabled, the program will automatically handle situations requiring user interaction (except for handling bad sectors, which is defined as a separate option). If an operation cannot continue without user interaction, it will fail. Details of the operation, including errors, if any, can be found in the operation log.

Ignore bad sectors

The preset is: Disabled.

When this option is disabled, each time the program comes across a bad sector, the backup activity will be assigned the Interaction required status. In order to back up the valid information on a rapidly dying disk, enable ignoring bad sectors. The rest of the data will be backed up and you will be able to mount the resulting disk backup and extract valid files to another disk.

Skipping bad sectors is not supported on Linux. You can back up Linux systems with bad sectors in offline mode, by using the bootable media builder in the on-premises version of Cyber Protect. Using the on-premises bootable media builder requires a separate license. Contact support for assistance.
Re-attempt, if an error occurs during VM snapshot creation

The preset is: Enabled. Number of attempts: 3. Interval between attempts: 5 minutes.

When taking a virtual machine snapshot fails, the program re-attempts to perform the unsuccessful operation. You can set the time interval and the number of attempts. The attempts will be stopped as soon as the operation succeeds OR the specified number of attempts are performed, depending on which comes first.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.