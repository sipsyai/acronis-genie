# Forensic data

Managing the backup and recovery of workloads and files > Backup options > Forensic data
Forensic data

Viruses, malware, and ransomware can carry out malicious activities, such as stealing or changing data. These activities may need to be investigated, which is possible only if digital evidence is provided. However, pieces of digital evidence, such as files or activity traces, may be deleted or the machine on which the malicious activity has been completed may become unavailable.

Backups with forensic data allow investigators to analyze disk areas that are not usually included in a regular disk backup. By enabling the Forensic data backup option, you can collect the following pieces of digital evidence that can be used in forensic investigations:

Snapshots of unused disk space
Memory dumps
Snapshots of running processes

Backups with forensic data are automatically notarized.

The Forensic data backup option is available for Entire machine backups of Windows workloads that run the following operating systems:

Windows 8.1 and later
Windows Server 2012 R2 and later

Backups with forensic data are not available for the following workloads:

Workloads that are connected to the network through VPN, and do not have direct access to the Internet.
Workloads with disks that are encrypted by BitLocker.

Backups with forensic data are supported by the following backup locations:

Cloud storage
Network folder

Local folder

Local folder is supported only on external hard drives that are connected to the backed-up workload via USB.

Local dynamic disks are not supported as a location for backups with forensic data.

Forensic backup process

During a forensic backup, the following operations are performed:

A raw memory dump and a list of running processes is captured.
The backed-up workload restarts and the bootable media interface opens.
A backup that includes both the used and unallocated space is created.
The backed-up disks are notarized.
The operating system of the workload reboots, and other configured operations run. For example, replication, retention, validation.

Configuring collection of forensic data

Retrieving forensic data

Viewing backup archives that contain forensic data

Notarization of backups with forensic data

The tool "tibxread" for getting the backed-up data

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.