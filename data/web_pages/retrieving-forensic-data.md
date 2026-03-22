# Retrieving forensic data

Managing the backup and recovery of workloads and files > Backup options > Forensic data > Retrieving forensic data
Retrieving forensic data

You can retrieve forensic data from a backup by downloading or recovering that data.

To retrieve forensic data

In the Cyber Protect console, go to Backup storage.
Select a backup location that supports backup archives with forensic data.
Select a backup archive that contains forensic data, and then click Show backups.

Select a backup (recovery point) that contains forensic data, and then click Recover.

[To download or recover only forensic data files] Click Forensic data.

Files that contain forensic data are shown.

[To download files] Select one or more files, and then click Download.
[To recover files] Select one or more files, and then click Recover.

In Cyber Protect console, you cannot download files that are bigger than 100 MB. Usually, the memory dump file (raw.dmp) is bigger. You can recover this file and then copy it.

You can use the memory dump with third-party forensic software. For example, you can use Volatility Framework (https://www.volatilityfoundation.org/) for further memory analysis.

[To recover the whole backup] Click Entire machine.

Configure the recovery options.
Click Start recovery.
To confirm that you want to overwrite the disks of the target machine, click Start recovery.
To ensure that no changes are made to the disk during the booting process, the recovered machine is not bootable.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.