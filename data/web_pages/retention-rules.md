# Retention rules

Managing the backup and recovery of workloads and files > Retention rules
Retention rules

To delete older backups automatically, configure the backup retention rules in the protection plan.

You can base the retention rules on any of the following backup properties:

Number
Age
Size

The available retention rules and their options depend on the backup scheme. The rules are also relevant to agents, workloads, and cloud to cloud backups. For more information, see Retention rules according to the backup scheme.

Depending on the configuration of the protection plan, retention rules are applied to an archive before or after a backup.

You can disable the automatic cleanup of older backups, by selecting the Keeping backups infinitely option while configuring the retention rules. This might result in increased storage usage, and you have to delete the unnecessary old backups manually.

Important tips
Retention rules are part of the protection plan. If you revoke or delete a plan, the retention rules in that plan will no longer be applied. For more information about how to delete the backups that you no longer need, see Deleting backups.

You can configure a retention rule to run either before or after the backup operation, which results in a different number or size of the retained backups.

For example, in How many to keep > By number of backups, you select 2. The following table compares the results of applying the retention rules before or after the backup.

Before backup	After backup

A cleanup operation runs. Two backups are kept.
A backup operation runs. A new backup is created.

Result: Three backups are available.


A backup operation runs. A new backup is created.
A cleanup operation runs. Two backups are kept.

Result: Two backups are available.

If, according to the backup scheme and backup format, each backup is stored as a separate file, you cannot delete a backup on which other incremental or differential backups depend. This backup will be deleted according to the retention rules applied to the dependent backups. This configuration may result in increased storage usage because the deletion of some backups is postponed. Also, the backup age, number, or size of backups may exceed the values that you specified. For more information about how to change this behavior, see Backup consolidation.

By default, the newest backup that a protection plan creates is never deleted. However, if you configure a retention rule to clean up the backups before starting a new backup operation, and set the number of backups to keep to zero, the newest backup will also be deleted.

If you apply this retention rule to a backup set with a single backup, and the backup operation fails, you will not be able to recover your data, because the existing backup will be deleted before a new one is created.

Retention rules according to the backup scheme

Configuring retention rules

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.