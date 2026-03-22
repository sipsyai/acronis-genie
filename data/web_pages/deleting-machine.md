# Deleting a virtual machine running from a backup

Managing the backup and recovery of workloads and files > Special operations with virtual machines > Running a virtual machine from a backup (Instant Restore) > Deleting a virtual machine running from a backup
Deleting a virtual machine running from a backup

You can delete a virtual machine that is running from a backup in the Cyber Protect console.

We recommend that you do not delete such machines directly in vSphere, Hyper-V, or Proxmox VE consoles. The backup on which these machines depend might be temporarily locked and it might not be deleted by a scheduled retention rule.

To delete a virtual machine that is running from a backup

In the Cyber Protect console, select a machine that is running from a backup.
In Actions, click Delete.
To confirm your choice, click Delete.

As a result, the machine is removed from the Cyber Protect console, the hypervizor inventory, and the virtual machine storage. All changes that were made to the data while the machine was running, are discarded.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.