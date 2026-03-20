---
title: "Recovery Options"
section: "Managing the backup and recovery of workloads and files"
subsection: "Recovery options"
page_range: "668-676"
tags: [recovery-options, backup-validation, boot-mode, error-handling, file-exclusions, flashback, performance, pre-post-commands, SID, VM-power-management, safe-recovery, windows-event-log]
acronis_version: "26.02"
---

# Recovery Options

To modify the recovery options, click **Recovery options** when configuring recovery.

## Availability of the Recovery Options

The set of available recovery options depends on:

- The environment the agent that performs recovery operates in (Windows, Linux, macOS, or bootable media).
- The type of data being recovered (disks, files, virtual machines, application data).

| Recovery option | Disks (Win) | Disks (Linux) | Disks (Bootable media) | Files (Win) | Files (Linux) | Files (macOS) | Files (Bootable media) | VMs (ESXi, Hyper-V, Scale Computing, oVirt, Virtuozzo) | VMs (Azure) | SQL and Exchange (Win) |
|---|---|---|---|---|---|---|---|---|---|---|
| Backup validation | + | + | + | + | + | + | + | + | - | + |
| Boot mode | + | - | - | - | - | - | - | + | - | - |
| Date and time for files | - | - | - | + | + | + | + | - | - | - |
| Error handling | + | + | + | + | + | + | + | + | + | + |
| File exclusions | - | - | - | + | + | + | + | - | - | - |
| File-level security | - | - | - | + | - | - | - | - | - | - |
| Flashback | + | + | + | - | - | - | - | + | - | - |
| Full path recovery | - | - | - | + | + | + | + | - | - | - |
| Mount points | - | - | - | + | - | - | - | - | - | - |
| Performance | + | + | - | + | + | + | - | + | - | + |
| Pre/post commands | + | + | - | + | + | + | - | + | - | + |
| SID changing | + | - | - | - | - | - | - | - | - | - |
| VM power management | - | - | - | - | - | - | - | + | + | - |
| Windows event log | + | - | - | + | - | - | - | Hyper-V only | - | + |

## Backup Validation

This option defines whether to validate a backup to ensure that the backup is not corrupted, before data is recovered from it. This operation is performed by the protection agent.

The preset is: **Disabled**.

> **Note:** Depending on the settings chosen by your service provider, validation might not be available when backing up to the cloud storage.

## Boot Mode

This option is effective when recovering a physical or a virtual machine from a disk-level backup that contains a Windows operating system. This option enables you to select the boot mode (BIOS or UEFI) that Windows will use after the recovery.

If the boot mode of the original machine is different from the selected boot mode, the software will:

- Initialize the disk to which you are recovering the system volume, according to the selected boot mode (MBR for BIOS, GPT for UEFI).
- Adjust the Windows operating system so that it can start using the selected boot mode.

The preset is: **As on the target machine.**

Options:

- **As on the target machine** -- the agent detects the boot mode currently used by Windows and makes adjustments accordingly. This is the safest value.
- **As on the backed-up machine** -- the agent reads the boot mode from the backup and makes adjustments accordingly.
- **BIOS** -- the agent makes the adjustments to use BIOS.
- **UEFI** -- the agent makes the adjustments to use UEFI.

### Recommendations

- Recover the entire disk where the system volume is located.
- Remember that BIOS does not allow using more than 2 TB of disk space.

### Limitations

Transferring between UEFI and BIOS is supported for:

- 64-bit Windows operating systems starting with Windows 7
- 64-bit Windows Server operating systems starting with Windows Server 2008 SP1

When transferring between UEFI and BIOS is not supported, the agent behaves as if the **As on the backed-up machine** setting is chosen. If the target machine supports both UEFI and BIOS, you need to manually enable the boot mode corresponding to the original machine.

## Date and Time for Files

This option is effective only when recovering files. It defines whether to recover the files' date and time from the backup or assign the current date and time.

The preset is: **Enabled** (files will be assigned the current date and time).

## Error Handling

### Re-attempt, if an error occurs

The preset is: **Enabled. Number of attempts: 30. Interval between attempts: 30 seconds.**

When a recoverable error occurs, the program re-attempts to perform the unsuccessful operation. You can set the time interval and the number of attempts. The attempts will be stopped as soon as the operation succeeds OR the specified number of attempts are performed.

### Do not show messages and dialogs while processing (silent mode)

The preset is: **Disabled.**

With silent mode enabled, the program will automatically handle situations requiring user interaction where possible. If an operation cannot continue without user interaction, it will fail. Details of the operation, including errors, can be found in the operation log.

### Ignore errors

This option is effective for file-level recovery. The preset is: **Enabled.**

When enabled, if recovery of a file fails, the recovery operation will continue for the rest of the files. A warning will be displayed on the **Activities** screen. The **Re-attempt, if an error occurs** option will not be triggered because an error is not logged.

When disabled, if recovery of a file fails, the recovery operation will fail. An error will be displayed on the **Activities** screen.

### Save system information if a recovery with reboot fails

This option is effective for a disk or volume recovery to a physical machine running Windows or Linux. The preset is: **Disabled.**

When enabled, you can specify a folder on the local disk, flash/HDD drives, or a network share where the log, system information, and crash dump files will be saved.

## File Exclusions

This option is effective only when recovering files. It defines which files and folders to skip during the recovery process and thus exclude from the list of recovered items.

> **Note:** Exclusions override the selection of data items to recover. For example, if you select to recover file MyFile.tmp and to exclude all .tmp files, file MyFile.tmp will not be recovered.

## File-Level Security

This option is effective when recovering files from disk- and file-level backups of NTFS-formatted volumes. It defines whether to recover NTFS permissions for files along with the files.

The preset is: **Enabled.**

You can choose whether to recover the permissions or let the files inherit their NTFS permissions from the folder to which they are recovered.

## Flashback

This option is effective when recovering disks and volumes on physical and virtual machines, except for Mac. It works only if the volume layout of the disk being recovered exactly matches that of the target disk.

If enabled, only the differences between the data in the backup and the target disk data are recovered. This accelerates recovery of physical and virtual machines. The data is compared at the block level.

- When recovering a physical machine, the preset is: **Disabled**.
- When recovering a virtual machine, the preset is: **Enabled**.

## Full Path Recovery

This option is effective only when recovering data from a file-level backup. If enabled, the full path to the file will be re-created in the target location.

The preset is: **Disabled**.

## Mount Points

This option is effective only in Windows for recovering data from a file-level backup. Enable this option to recover files and folders that were stored on the mounted volumes and were backed up with the enabled Mount points option.

The preset is: **Disabled**.

This option is effective only when you select for recovery a folder that is higher in the folder hierarchy than the mount point.

> **Note:** If the volume is not mounted at the moment of recovery, the data will be recovered directly to the folder that has been the mount point at the time of backing up.

## Performance

This option defines the priority of the recovery process in the operating system. The available settings are: **Low**, **Normal**, **High**.

The preset is: **Normal**.

The priority determines the amount of CPU and system resources allocated to the process. Decreasing the recovery priority will free more resources for other applications. Increasing the priority might speed up the recovery process.

## Pre/Post Commands

The option enables you to define commands to be automatically executed before and after data recovery.

Example: Launch the **Checkdisk** command to find and fix logical file system errors, physical errors, or bad sectors before the recovery starts or after the recovery ends.

The program does not support interactive commands. A post-recovery command will not be executed if the recovery proceeds with reboot.

### Pre-recovery command

1. Enable the **Execute a command before the recovery** switch.
2. In the **Command...** field, type a command or browse to a batch file.
3. In the **Working directory** field, specify the path to the directory where the command will be executed.
4. In the **Arguments** field, specify execution arguments, if required.
5. Select the appropriate options:

| Fail the recovery if the command execution fails* | Do not recover until the command execution is complete | Result |
|---|---|---|
| Selected | Selected | Perform the recovery only after the command is successfully executed. Fail the recovery if the command execution failed. |
| Cleared | Selected | Perform the recovery after the command is executed despite execution failure or success. |
| Cleared | Cleared | Perform the recovery concurrently with the command execution and irrespective of the command execution result. |

*A command is considered failed if its exit code is not equal to zero.

### Post-recovery command

1. Enable the **Execute a command after the recovery** switch.
2. In the **Command...** field, type a command or browse to a batch file.
3. In the **Working directory** field, specify the path to the directory where the command will be executed.
4. In the **Arguments** field, specify execution arguments, if required.
5. Select the **Fail the recovery if the command execution fails** check box if critical.

> **Note:** A post-recovery command will not be executed if the recovery proceeds with reboot.

## SID Changing

This option is effective when recovering Windows 8.1/Windows Server 2012 R2 or earlier. It is not effective when recovery to a virtual machine is performed by Agent for VMware, Agent for Hyper-V, Agent for Scale Computing HC3, or Agent for oVirt.

The preset is: **Disabled**.

The software can generate a unique security identifier (Computer SID) for the recovered operating system. You only need this option to ensure operability of third-party software that depends on Computer SID. Microsoft does not officially support changing SID on a deployed or recovered system. Use this option at your own risk.

## VM Power Management

These options are effective when recovery to a virtual machine is performed by Agent for VMware, Agent for Azure, Agent for Hyper-V, Agent for Virtuozzo, Agent for Scale Computing HC3, or Agent for oVirt.

### Power off target virtual machines when starting recovery

The preset is: **Enabled**.

Recovery to an existing virtual machine is not possible if the machine is online, and so the machine is powered off automatically as soon as the recovery starts. Users will be disconnected and any unsaved data will be lost. Clear the check box if you prefer to power off virtual machines manually before the recovery.

### Power on the target virtual machine when recovery is complete

The preset is: **Disabled**.

After a machine is recovered from a backup to another machine, there is a chance the existing machine's replica will appear on the network. To be on the safe side, power on the recovered virtual machine manually, after you take the necessary precautions.

## Windows Event Log

This option is effective only in Windows operating systems. It defines whether the agents have to log events of the recovery operations in the Application Event Log of Windows (to see this log, run `eventvwr.exe` or select **Control Panel** > **Administrative tools** > **Event Viewer**). You can filter the events to be logged.

The preset is: **Disabled**.

## Safe Recovery

Use safe recovery with **Entire machine** or **Disks/volumes** backups of Windows workloads to ensure that you recover only malware-free data, even if the backup contains infected files.

During a safe recovery operation, the backup is automatically scanned for malware. Then, the protection agent recovers the backup on the target workload and deletes any infected files. As a result, a malware-free backup is recovered.

Additionally, one of the following statuses is assigned to the backup:

- Malware detected
- No malware
- Not scanned

You can use the status to filter the backup archives.

### Limitations

- Safe recovery is supported for physical and virtual Windows machines on which a protection agent is installed.
- Safe recovery is supported for **Entire machine** and **Disks/volumes** backups.
- Only NTFS volumes are scanned for malware. Non-NTFS volumes are recovered without antimalware scanning.
- Safe recovery is not supported for the Continuous data protection (CDP) backup in the archive. To recover the data from the CDP backup, run an additional **Files/folders** recovery operation.
