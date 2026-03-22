# Selecting ESXi configuration

Managing the backup and recovery of workloads and files > Selecting data to back up > Selecting ESXi configuration
Selecting ESXi configuration

A backup of an ESXi host configuration enables you to recover an ESXi host to bare metal. The recovery is performed under bootable media.

The virtual machines running on the host are not included in the backup. They can be backed up and recovered separately.

A backup of an ESXi host configuration includes:

The bootloader and boot bank partitions of the host.
The host state (configuration of virtual networking and storage, SSL keys, server network settings, and local user information).
Extensions and patches installed or staged on the host.
Log files.
Prerequisites
SSH must be enabled in the Security Profile of the ESXi host configuration.
You must know the password for the 'root' account on the ESXi host.
Limitations
ESXi configuration backup is not supported for hosts running VMware ESXi 7.0 and later.
An ESXi configuration cannot be backed up to the cloud storage.

To select an ESXi configuration

Click Devices > All devices, and then select the ESXi hosts that you want to back up.
Click Protect.
In What to back up, select ESXi configuration.
In ESXi 'root' password, specify a password for the 'root' account on each of the selected hosts or apply the same password to all of the hosts.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.