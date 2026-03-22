# Protecting Proxmox virtual machines and containers

Managing the backup and recovery of workloads and files > Protecting Proxmox virtual machines and containers
Protecting Proxmox virtual machines and containers

You can perform agentless backup of Proxmox virtual machines and containers by installing Agent for Proxmox on the protected host.

Agent for Proxmox is bundled with Agent for Linux (64-bit), and requires that Agent for Linux is also installed on the host. For more information about how to download the installation file, see Downloading protection agents.

Hosts running Proxmox VE 8.2 or later are supported. In clustered environments, you must install an agent on each node.

A Virtual Machine quota is required per Proxmox VE virtual machine or container. No quota is required for the machine on which Agent for Proxmox runs.​

The following Proxmox storages are supported for backup and recovery:

For virtual machines: All storages on which a virtual machine can be created
For containers: LVM Thin, Ceph/RBD, BtrFS

The following backup location are available for Proxmox virtual machines and containers:

The cloud storage (including partner-hosted storage)
Public cloud storages
Network folders on SMB and NFS shares
Local folders

Limitations for Proxmox workloads

Installing Agent for Proxmox

Backing up Proxmox workloads

Recovering Proxmox workloads

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.