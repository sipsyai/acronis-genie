# Before You Start Agent Synology

Installing and deploying Cyber Protection agents > Deploying virtual appliances > Deploying Agent for Synology > Before you start
Before you start

With Agent for Synology, you can back up files and folders from and to Synology NAS devices. The NAS-specific properties and access permissions for shares, folders, and files are preserved.

Agent for Synology runs on the NAS device. Thus, you can use the resources of the device for off-host data processing operations, such as backup replication, validation, and cleanup. To learn more about these operations, refer to Off-host data protection plans.

Agent for Synology supports only NAS devices with x86_64 processors. ARM processors are not supported. See the Synology knowledge center.

You can recover a backup to the original or a new location on the NAS device, and to a network folder that is accessible through that device. Backups in the cloud storage can also be recovered to a non-original NAS device on which Agent for Synology is installed.

The table below summarizes the available backup sources and destinations.

What to backup

Items to backup

(Backup source)



Where to backup

(Backup destination)


Files/folders

Local folder*

Cloud storage


Local folder*


Network folder (SMB)**	Network folder (SMB)**
NFS folder
Public clouds***

* Including USB drives that are attached to the NAS device.

Encrypted folders are not supported. These folders are not shown in the Cyber Protection graphical user interface.

** Using external network shares as backup source or backup destination via the SMB protocol is only available for agents running on Synology DiskStation Manager 6.2.3 and later. The data hosted on the Synology NAS itself, including in hosted network shares, can be backed up without limitations.

*** Backup to public clouds, such as Microsoft Azure, Amazon, or S3-compatible storages, is supported only by Agent for Synology 7.x. Agent for Synology 6.x does not support this backup destination due to limitations of the Linux kernel of Synology DSM 6.x.

Limitations

Agent for Synology supports only NAS devices with x86_64 processors. ARM processors are not supported. See the Synology knowledge center.

Backed-up encrypted shares are recovered as non-encrypted.
Backed-up shares for which the File compression option is enabled are recovered with this option disabled.
You can recover to a Synology NAS device only backups that are created by Agent for Synology.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.