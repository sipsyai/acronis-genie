# Predefined scripts

Managing the backup and recovery of workloads and files > Creating bootable media to recover operating systems > Bootable Media Builder > Predefined scripts
Predefined scripts

Bootable Media Builder provides the following predefined scripts:

Recovery from the cloud storage (entire_pc_cloud)
Recovery from a network share (entire_pc_share)

The scripts are located in the following folders on the machine where Bootable Media Builder is installed:

In Windows: %ProgramData%\Acronis\MediaBuilder\scripts\
In Linux: /var/lib/Acronis/MediaBuilder/scripts/
Recovery from the cloud storage

In Bootable Media Builder, specify the following script parameters:

The backup file name.

A password that the script will use to access encrypted backups.

Recovery from a network share

In Bootable Media Builder, specify the following script parameters:

The path to the network share.
The user name and password for the network share.

The backup file name. To find out the backup file name:

In the Cyber Protect console, go to Backup storage > Locations.
Select the network share (click Add location if the share is not listed).
Select the backup.
Click Details. The file name is displayed under Backup file name.

A password that the script will use to access encrypted backups.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.