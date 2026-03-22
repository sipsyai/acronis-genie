# Azure restore points

Managing the backup and recovery of workloads and files > Backup options > Azure restore points
Azure restore points

There are three Microsoft Azure backup options available when configuring the agentless backup of Microsoft Azure virtual machines:

Azure restore points: Retention
Azure restore points: Consistency level
Azure restore points: Handling unsupported disks
Azure restore points: Retention

This option enables you to define how many Microsoft Azure restore points to keep after a backup (the default is 3). These restore points improve the performance of incremental backups, which use the Changed Block Tracking (CBT) feature.

The maximum number of Azure restore points you can keep is 200 (as recommended by Microsoft), and there must be only one restore point collection created for each virtual machine.

When performing recovery to the original Microsoft Azure virtual machine, from a backup which has the corresponding Azure restore point still available in Microsoft Azure, the recovery process uses this restore point to revert back the virtual machine state automatically, instead of retrieving data from the backup file. This helps optimize the traffic and performance of the recovery.

Note that the restore points rotation logic is managed by the protection plan. If there are two plans applied to the same virtual machine, then each plan treats all restore points inside the collection as its own and rotates backups according to the defined Restore points value.

Azure restore points: Consistency level

This enables you to select the consistency level of the restore points, such as application-consistent restore points or file-system consistent restore points.

This option applies only to virtual machines that are powered on.

You can select one of the following:

Require application-consistent restore points: If the restore point is not application-consistent, the backup will fail.

Note that virtual machine restore points support application consistency for virtual machines running Windows operating systems, and support file-system consistency for virtual machines running Linux operating systems. Application-consistent restore points use VSS writers (or pre/post scripts for Linux) to ensure the consistency of the application data before a restore point is created.

Warn on file-system or crash-consistent restore points: If the restore point is file-system consistent or crash-consistent, the backup completes with a warning.

This option adds a warning to the log and marks the activity with a warning if the snapshot consistency level is file-system consistent and below (crash-consistent).

Warn on crash-consistent restore points: If the restore point is crash-consistent, the backup completes with a warning. File-system consistent and application-consistent restore points do not trigger a warning. This option is selected by default.

This option adds a warning to the log and marks the activity with a warning.

Ignore consistency level: Regardless of the level of consistency of the restore point, the backup will complete successfully.

This option adds an information message to the log and runs the protection plan successfully.

Azure restore points: Handling unsupported disks

This option enables you to determine what to do if a virtual machine with an unmanaged, shared , or Ephemeral disk is being backup up. Note that these types of disks are not supported in Microsoft Azure restore points and cannot be backed up in agentless mode. If you need to back up the data on these disks, install the protection agent inside the guest operating system of the virtual machine.

You can select one of the following:

Ignore unsupported disks: The backup completes successfully, and unsupported disks are skipped.
Warn on unsupported disks: The backup completes with a warning about the unsupported disk. This option is selected by default.
Fail on unsupported disks: The backup fails if the virtual machine with an supported disk is being backed up.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.