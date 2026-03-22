# Remote operations with bootable media

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Remote operations with bootable media
Remote operations with bootable media

To see the bootable media in the Cyber Protect console, first you need to register it as described in Registering the bootable media.

After you register the media in the Cyber Protect console, it appears on the Devices > Bootable media tab. A bootable media disappears from this tab when it has been offline for more than 30 days.

You can manage the bootable media remotely in the Cyber Protect console. For example, you can recover data, restart or shut down the machine booted with the media, or view information, activities, and alerts about the media.

Running the bootable media requires 1.5 GB of RAM.

Remote operation with bootable media is not supported with LVM/LDM volumes.

You cannot update the bootable media remotely, on the Settings > Agents tab in the Cyber Protect console.

To update the bootable media, create a new one, as described in the Bootable Media Builder section. Alternatively, download the ready-made media, by clicking your account icon > Downloads > Bootable media in the Cyber Protect console.

To recover files or folders with bootable media remotely

In the Cyber Protect console, go to Devices > Bootable media.
Select the media that you want to use for data recovery.
Click Recovery.
Select the location, and then select the backup that you need. Note that backups are filtered by location.
Select the recovery point, and then click Recover files/folders.

Browse to the required folder or use the search bar to obtain the list of the required files and folders.

Search is language-independent.

You can use one or more wildcard characters (* and ?). For more details about using wildcards, refer to File filters (Inclusions/Exclusions).

Click to select the files that you want to recover, and then click Recover.
In Path, select the recovery destination.

For advanced recovery configuration, click Recovery options. For more information, refer to Recovery options.

Click Start recovery.

Select one of the file overwriting options:

Overwrite existing files

Overwrite an existing file if it is older

Do not overwrite existing files

Choose whether to restart the machine automatically.

Click Proceed to start the recovery.

You can check the recovery progress in the Cyber Protect console, on the Activities tab.

To recover disks, volumes, or entire machines with bootable media remotely

On the Devices tab, go to the Bootable media group, and then select the media that you want to use for data recovery.
Click Recovery.
Select the location, and then select the backup that you need. Note that backups are filtered by location.

Select the recovery point, and then click Recover > Entire machine.

If necessary, configure the target machine and volume mapping as described in Recovery of physical machines.

For advanced recovery configuration, click Recovery options. For more information, refer to Recovery options.
Click Start recovery.
Confirm that you want to overwrite the disks with their backed-up versions. Choose whether to restart the machine automatically.

You can check the recovery progress in the Cyber Protect console, on the Activities tab.

To restart the booted machine remotely

On the Devices tab, go to the Bootable media group, and then select the media that you want to use for data recovery.
Click Reboot.
Confirm that you want to restart the machine booted with the media.

To shut down the booted machine remotely

On the Devices tab, go to the Bootable media group, and then select the media that you want to use for data recovery.
Click Shut down.
Confirm that you want to shut down the machine booted with the media.

To view information about the bootable media

On the Devices tab, go to the Bootable media group, and then select the media that you want to use for data recovery.
Click Details, Activities, or Alerts to see the corresponding information.

To delete bootable media remotely

On the Devices tab, go to the Bootable media group, and then select the media that you want to use for data recovery.
Click Delete to delete the bootable media from the Cyber Protect console.
Confirm that you want to delete the bootable media.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.