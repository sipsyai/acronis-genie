---
title: "Backup options: Pre/Post commands, scheduling, sector-by-sector, splitting, VSS, and more"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup options"
page_range: "606-618"
tags: ["pre-post-commands", "pre-data-capture", "post-data-capture", "scheduling", "sector-by-sector", "splitting", "task-failure", "task-start-conditions", "VSS", "weekly-backup", "Windows-event-log"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#pre-post-commands.html"
---

# Pre/Post commands

The option enables you to define commands to be automatically executed before and after the backup procedure. The program does not support interactive commands (commands that require user input, e.g., "pause").

Execution order: Pre-backup command > Backup > Post-backup command

The agent performs the replication *after* executing the post-backup command.

## Pre-backup command

1. Enable the **Execute a command before the backup** switch.
2. In the **Command or batch file path on the machine with an agent** field, type a command or browse to a batch file. If you use PowerShell, pass the command as an argument to `powershell.exe`. For example: `powershell.exe -C "New-Item -Force -ItemType file -Path 'C:\temp\file.txt'"`
3. Specify the **Working directory** and **Arguments** if required.
4. Select the appropriate options:
   - **Fail the backup if the command execution fails** -- A command is considered failed if its exit code is not equal to zero.
   - **Do not back up until the command execution is complete**
5. Click **Done**.

## Post-backup command

1. Enable the **Execute a command after the backup** switch.
2. Specify command, working directory, and arguments (same rules as pre-backup).
3. If successful execution is critical, select **Fail the backup if the command execution fails**. If not selected, the result of the command execution does not affect the backup status.
4. Click **Done**.

> **Note:** If a script fails due to a conflict related to a required library version in Linux, exclude the `LD_LIBRARY_PATH` and `LD_PRELOAD` environmental variables by adding to your script:
> ```
> #!/bin/sh
> unset LD_LIBRARY_PATH
> unset LD_PRELOAD
> ```

# Pre/Post data capture commands

The option enables you to define commands to be automatically run before and after data capture (taking the data snapshot). Data capture is performed at the beginning of the backup procedure.

Execution order: Pre-backup command > Pre-data capture command > Data capture > Post-data capture command > Write data to the backup set > Post-backup command

### Interaction with other backup options

- If the **Multi-volume snapshot** option is enabled, the pre/post data capture commands will run only once (because snapshots for all volumes are created simultaneously).
- If the **Multi-volume snapshot** option is disabled, the pre/post data capture commands will run for every volume that is being backed up.
- If the **Volume Shadow Copy Service (VSS)** option is enabled: Pre-data capture commands > VSS Suspend > Data capture > VSS Resume > Post-data capture commands

By using the pre/post data capture commands, you can suspend and resume a database or application that is not compatible with VSS.

## Pre-data capture command

1. Enable the **Execute a command before the data capture** switch.
2. Specify command, working directory, and arguments.
3. Select options: **Fail the backup if the command execution fails** and/or **Do not perform the data capture until the command execution is complete**.
4. Click **Done**.

## Post-data capture command

Same procedure as pre-data capture. Enable **Execute a command after the data capture** and configure as needed.

# Scheduling

## Distribute start times within a time window

Preset: **Enabled. Maximum delay: 30 minutes.**

This option defines a random delay that is added to the scheduled start time to avoid network congestion when backing up multiple workloads to a network location. The delay value for each workload is calculated when you apply the protection plan and remains the same until you edit the maximum delay value.

## Limit the number of simultaneously running backups

This option is effective for ESXi and Hyper-V virtual machines only. It limits the number of virtual machines that an agent can back up simultaneously.

Preset:
- Agent for VMware: **Enabled. Maximum number of simultaneously running backups: 10.**
- Agent for Hyper-V: **Enabled. Maximum number of simultaneously running backups: 5.**

# Sector-by-sector backup

Preset: **Disabled**.

This option is effective only for disk-level backup. When enabled, a sector-by-sector backup stores all the disk sectors including sectors that do not contain any data. The resulting backup will be as large as the backed-up disk (or larger if compression is not used).

Use sector-by-sector backup to:
- Back up disks with unrecognized or unsupported file systems
- Back up third-party disk encryption products that are not compatible with Acronis software

> **Note:** Sector-by-sector backup is not available for macOS.

# Splitting

Preset: **Automatic**.

This option defines the behavior of file splitting for backups stored in local or network (SMB) folders.

- **Automatic** -- A backup will be split if it exceeds the maximum file size supported by the file system on the destination. For the Version 12 backup format, the file is split into 200-GB files by default if the file is stored in a local or network (SMB) folder.
- **Fixed size** -- Enter the desired file size or select it from the drop-down list.

# Task failure handling

Preset: **Disabled**.

This option determines the behavior when a backup or recovery task fails. When the option is enabled, the task will be re-attempted automatically.

You can specify the number of attempts (up to 99) and the interval between attempts. The attempts will stop as soon as the task is completed successfully.

# Task start conditions

Preset: **Wait until the conditions are met**.

This option determines the program behavior when a backup is about to start and the start conditions are not met.

- **Wait until the conditions are met** -- The backup will start when all conditions are met.
- **Skip the scheduled backup** -- If the conditions are not met at the scheduled time, the backup will be skipped and will start at the next scheduled time.

You can also specify a period after which the backup starts regardless of the conditions.

# Volume Shadow Copy Service (VSS)

This option is effective only for Windows operating systems.

Preset:
- For disk-level backup of Windows: **Enabled. Automatically select snapshot provider.**
- For file-level backup of Windows: **Enabled. Automatically select snapshot provider.**

The option defines whether a Volume Shadow Copy Service (VSS) provider should take snapshots during backup. By default, the provider is selected automatically. VSS notifies VSS-aware applications that the backup is about to start. This ensures the consistent state of all data used by the applications -- in particular, the completion of all database transactions at the moment of creating the snapshot.

Options:
- **Automatically select snapshot provider** -- Select between Acronis VSS Provider, the OS VSS provider, or other available providers automatically.
- **Use Acronis VSS Provider** -- Use the built-in Acronis VSS Provider.
- **Use the operating system's default provider** -- Use the Windows VSS provider (recommended for compatibility with most applications).
- **Do not use VSS** -- Disable VSS. Snapshot creation will be faster but data consistency of applications whose transactions are not complete when the snapshot is being taken is not guaranteed.
- **Enable full VSS support** -- Available only with **Use Acronis VSS Provider**. VSS writers will ensure that the application data is in a consistent state at the moment of backup. This may slow down the backup process.

## Volume Shadow Copy Service for virtual machines

This option is effective only for agentless backup of virtual machines running a Windows guest OS.

Preset: **Enabled**.

This option determines whether quiesced snapshots of virtual machines are taken. To take a quiesced snapshot, VMware Tools or Hyper-V integration services must be installed on the virtual machine.

When disabled, the backup will contain a crash-consistent snapshot.

# Weekly backup

This option determines which day of the week is considered the "start of the week" for the **Weekly full, Daily incremental** backup scheme and for retention rules.

Preset: **Monday**.

# Windows event log

This option is effective only in Windows.

Preset: **Disabled**.

When enabled, the agents log the events of the backup operations in the Application Event Log of Windows (Event Viewer). You can filter and view these events from the event source "Cyber Backup" or "Online Backup".
