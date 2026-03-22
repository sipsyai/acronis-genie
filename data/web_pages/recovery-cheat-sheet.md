# Recovery cheat sheet

Managing the backup and recovery of workloads and files > Recovery > Recovery cheat sheet
Recovery cheat sheet

The following table summarizes the available recovery methods. Use the table to choose a recovery method that best fits your need.

In the Cyber Protect console, you cannot recover backups in tenants in Compliance mode. See Recovering backups in tenants in Compliance mode.


What to recover	Recovery method


Physical machine
(Windows or Linux)



Using the Cyber Protect console

Using bootable media




Physical machine
(Mac)



Using bootable media




Virtual machine
(Such as VMware, Hyper-V, Red Hat Virtualization (oVirt), Scale Computing HC3, Proxmox)



Using the Cyber Protect console

Using bootable media




Virtual machine
(Virtuozzo Hybrid Server, Virtuozzo Hybrid Infrastructure)



Using the Cyber Protect console




Container

(Virtuozzo Hybrid Server, Proxmox)

Using the Cyber Protect console


ESXi configuration



Using bootable media




Files/Folders



Using the Cyber Protect console

Downloading files from the cloud storage

Using bootable media

Extracting files from local backups




System state



Using the Cyber Protect console




SQL databases



Using the Cyber Protect console




Exchange databases



Using the Cyber Protect console




Exchange mailboxes



Using the Cyber Protect console




Microsoft 365








Mailboxes

(local Agent for Microsoft 365)



Using the Cyber Protect console




Mailboxes

(cloud Agent for Microsoft 365)



Using the Cyber Protect console




Public folders



Using the Cyber Protect console




OneDrive files



Using the Cyber Protect console




SharePoint Online data



Using the Cyber Protect console




Google Workspace






Mailboxes

Using the Cyber Protect console




Google Drive files



Using the Cyber Protect console




Shared drive files



Using the Cyber Protect console

Cross-platform recovery

Cross-platform recovery is available for backups of entire machines and backups of disks that contain an operating system.

A cross-platform recovery is performed in the following cases:

A backup is created by one type of agent but it is recovered by another type of agent.
An agent-based backup is recovered on the hypervisor level (agentless recovery), or an agentless backup is recovered by an agent (agent-based recovery).
A backup is recovered to dissimilar hardware (including virtual hardware).
Some peripheral devices, such as printers, might not be recovered correctly when you perform a cross-platform recovery.

For more information about the possible combinations for cross-platform recovery, see Cross-platform recovery.

Note for Mac users

Starting with 10.11 El Capitan, certain system files, folders, and processes are flagged for protection with an extended file attribute com.apple.rootless. This feature is called System Integrity Protection (SIP). The protected files include preinstalled applications and most of the folders in /system, /bin, /sbin, /usr.

The protected files and folders cannot be overwritten during a recovery under the operating system. If you need to overwrite the protected files, perform the recovery under bootable media.

Starting with macOS Sierra 10.12, rarely used files can be moved to iCloud by the Store in Cloud feature. Small footprints of these files are kept on the file system. These footprints are backed up instead of the original files.

When you recover a footprint to the original location, it is synchronized with iCloud and the original file becomes available. When you recover a footprint to a different location, it cannot be synchronized and the original file will be unavailable.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.