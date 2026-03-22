# Limitations for Proxmox workloads

Managing the backup and recovery of workloads and files > Protecting Proxmox virtual machines and containers > Limitations for Proxmox workloads
Limitations for Proxmox workloads

The following limitations apply to backup and recovery of Proxmox virtual machines and containers.

General
Virtual machines
Containers

The following features are not supported:

Run as VM
Convert to VM
Application-aware backup
VM replication
You cannot recover virtual disks or containers to CephFS storage.
Disks for which the backup option is disabled in Proxmox VE are not backed up.
During a recovery, selecting the disk provisioning type (thin/thick) will only work if the target storage supports the selected type. For example, LVM storage supports thick disks only. If you select thin disk allocation, this option will be ignored.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.