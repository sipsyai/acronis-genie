# Creating a backup replication plan

Working with plans > Off-host data protection plans > Backup replication > Creating a backup replication plan
Creating a backup replication plan

To replicate backups as an off-host data processing operation, you create a backup replication plan.

To create a backup replication plan

In the Cyber Protect console, click Management > Backup replication.

Click Create plan.

In Agent, select the agent that will perform the replication.

You can select any agent that has access both to the source location and the replication locations.

In Items to replicate, select the archives or backup locations to replicate.

To switch between archives and locations, use the Locations / Backups switch in the upper-right corner.

If you select multiple encrypted archives, their encryption password must be the same. For archives that use different encryption passwords, create separate plans.

In Destination, specify the replication location.

In How to replicate, select which backups (also known as recovery points) to replicate.

The following options are available:

All backups
Only full backups
Only the last backup

For more information about these options, refer to What to replicate.

In Schedule, configure the replication schedule.

When configuring the schedule of the backup replication plan, ensure that the last replicated backup will still be available in its original location when the backup replication starts. If this backup is not available in the original location, for example, because it was deleted by a retention rule, the whole archive will be replicated as a full backup. This might be very time-consuming and will use additional storage space.

In Retention rules, specify the retention rules for the target location.

The following options are available:

By number of backups
By backup age (separate settings for monthly, weekly, daily, and hourly backups)
By total size of backups

Keep backups indefinitely

Selecting this option will result in increased storage usage. You must delete the unnecessary backups manually.
[If you selected encrypted archives in Items to replicate] Enable the Backup password switch, and then provide the encryption password.

To modify the plan options, click the gear icon, and then configure the options as required.

Click Create.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.