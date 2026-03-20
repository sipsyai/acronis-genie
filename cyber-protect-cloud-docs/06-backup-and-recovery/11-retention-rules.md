---
title: "Retention rules"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup"
page_range: "551-555"
tags: ["retention", "backup-cleanup", "backup-age", "backup-count", "backup-size", "GFS", "monthly", "weekly", "daily", "hourly"]
acronis_version: "26.02"
---

# Retention rules

To delete older backups automatically, configure the backup retention rules in the protection plan. You can base the retention rules on any of the following backup properties:

- **Number** of backups
- **Age** of backups
- **Size** of backups (total)

The available retention rules and their options depend on the backup scheme. The rules are also relevant to agents, workloads, and cloud-to-cloud backups.

Depending on the configuration of the protection plan, retention rules are applied to an archive before or after a backup.

You can disable automatic cleanup by selecting **Keeping backups infinitely** (this might result in increased storage usage and you will have to delete unnecessary old backups manually).

## Important tips

- Retention rules are part of the protection plan. If you revoke or delete a plan, the retention rules in that plan will no longer be applied.
- You can configure a retention rule to run either before or after the backup operation, which results in a different number or size of the retained backups.
- If, according to the backup scheme and format, each backup is stored as a separate file, you cannot delete a backup on which other incremental or differential backups depend. This backup will be deleted according to the retention rules applied to the dependent backups. This may result in increased storage usage because the deletion of some backups is postponed.
- By default, the newest backup that a protection plan creates is never deleted. However, if you configure a retention rule to clean up before a new backup operation and set the number of backups to keep to zero, the newest backup will also be deleted.

> **Warning:** If you apply this retention rule to a backup set with a single backup, and the backup operation fails, you will not be able to recover your data, because the existing backup will be deleted before a new one is created.

## Retention rules according to the backup scheme

| Backup scheme | Schedule options | Available retention rules |
|---|---|---|
| **Always incremental (single-file)** | Monthly, Weekly, Daily, Hourly, Event-triggered | By number of backups. By backup age (separate settings for monthly, weekly, daily, and hourly). Keep backups indefinitely. |
| **Always full** | Monthly, Weekly, Daily, Hourly, Event-triggered | By number of backups. By backup age (separate settings for monthly, weekly, daily, and hourly). By total size of backups. Keep backups indefinitely. |
| **Weekly full, Daily incremental** | Daily, Event-triggered | By number of backups. By backup age (separate settings for weekly and daily). By total size of backups. Keep backups indefinitely. |
| **Monthly full, Weekly differential, Daily incremental (GFS)** | Monthly, Weekly, Daily, Hourly, Event-triggered | By number of backups. By backup age (separate settings for full, differential, and incremental). By total size of backups. Keep backups indefinitely. |
| **Custom** | Monthly, Weekly, Daily, Hourly, Event-triggered | By number of backups. By backup age (separate settings for full, differential, and incremental). By total size of backups. Keep backups indefinitely. |

> **Note:** The **By total size of backups** setting is not available with the **Always incremental (single-file)** backup scheme.

## Why are there monthly backups with an hourly scheme?

Depending on the backup scheme, you can configure the **By backup age** option for monthly, weekly, daily, and hourly backups. These settings are available with all non-custom backup schemes, and are based on time:

| Backup | Description |
|---|---|
| **Monthly** | The first backup each month. |
| **Weekly** | The first backup on the day of the week specified in the **Weekly backup** option. That day is the beginning of the week for retention rules. If a weekly backup is also the first of the month, it is considered a monthly backup; a weekly backup is created the following week. |
| **Daily** | The first backup of the day, unless this backup falls within the definition of a monthly or weekly backup. In that case, a daily backup is created the following day. |
| **Hourly** | The first backup of the hour, unless it falls within the definition of a monthly, weekly, or daily backup. In that case, an hourly backup is created the next hour. |

## Configuring retention rules

1. In the protection plan, expand the **Backup** module.
2. Click **How many to keep**.
3. Select one of the following options:
   - **By number of backups**
   - **By backup age** -- Separate settings for monthly, weekly, daily, and hourly backups are available. The maximum value for all types is 9999. You can also use a single setting for all backups.
   - **By total size of backups** -- Not available with the **Always incremental (single-file)** backup scheme.
   - **Keep backups indefinitely**
4. If you did not select **Keep backups indefinitely**, configure the values for the selected option.
5. If you did not select **Keep backups indefinitely**, select when the retention rules are applied:
   - **After backup** (default)
   - **Before backup** -- Not available when backing up Microsoft SQL Server clusters or Microsoft Exchange Server clusters.
6. Click **Done**.
7. Save the protection plan.
