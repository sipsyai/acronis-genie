# Backup cheat sheet

Managing the backup and recovery of workloads and files > Backup cheat sheet
Backup cheat sheet

The following table summarizes the most common backup parameters.

WHAT TO BACK UP

ITEMS TO BACK UP

Selection methods

WHERE TO BACK UP

SCHEDULE

Backup schemes




Disks/volumes (physical machines)



Direct selection

Policy rules

File filters



Cloud

Local folder

Network folder

NFS*

Secure Zone**



Always incremental (Single-file)

Always full

Weekly full, Daily incremental

Monthly full, Weekly differential, Daily incremental (GFS)

Custom (F-D-I)




Disks/volumes (virtual machines)



Policy rules

File filters



Cloud

Local folder

Network folder

NFS*




Files (physical machines only)



Direct selection

Policy rules

File filters



Cloud

Local folder

Network folder

NFS*

Secure Zone**



Always incremental (Single-file)

Always full

Weekly full, Daily incremental

Monthly full, Weekly differential, Daily incremental (GFS)

Custom (F-D-I)




ESXi configuration



Direct selection



Local folder

Network folder

NFS*




System state



Direct selection



Cloud

Local folder

Network folder



Always full

Weekly full, daily incremental

Custom (F-I)

Always incremental (Single-file) - only for SQL databases


SQL databases	Direct selection
Exchange databases	Direct selection


Microsoft 365



Mailboxes

(local Agent for Microsoft 365)



Direct selection



Cloud

Local folder

Network folder



Always incremental (Single-file)




Mailboxes

(cloud Agent for Microsoft 365)

Direct selection

Cloud



Up to 6 backups per day


Public folders	Direct selection


Teams



Direct selection




OneDrive files





Direct selection

Policy rules


SharePoint Online data

Direct selection

Policy rules




Google Workspace



Gmail mailboxes



Direct selection



Cloud



Up to 6 backups per day




Google Drive files





Direct selection

Policy rules


Shared drive files

Direct selection

Policy rules

* Backup to NFS shares is not available in Windows.

** Secure Zone cannot be created on a Mac.

Backups to public cloud require a Local backup storage quota.
How long to keep the backups?

You can keep your backups forever or configure a retention period by the following criteria:

By backup age (single rule / per backup set)
By number of backups
By total size of backups
The By total size of backups retention rule is not available with the Always incremental (single-file) backup scheme or when backing up to the cloud storage.

See Retention rules.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.