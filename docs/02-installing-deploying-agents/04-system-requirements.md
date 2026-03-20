---
title: "System requirements for agents"
section: "Installing and deploying Cyber Protection agents"
subsection: "Before you start"
page_range: "43-46"
tags: ["system-requirements", "disk-space", "RAM", "MTU", "CET", "DLP", "device-control"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#system-requirements-agents.html"
---

# System requirements for agents

## Disk space required for installation

| Agent | Disk space required |
|-------|-------------------|
| Agent for Windows | 1.2 GB |
| Agent for Linux | 2 GB |
| Agent for Mac | 1 GB |
| Agent for SQL and Agent for Windows | 1.2 GB |
| Agent for Exchange and Agent for Windows | 1.3 GB |
| Agent for Data Loss Prevention | 500 MB |
| Agent for Microsoft 365 | 500 MB |
| Agent for Active Directory and Agent for Windows | 2 GB |
| Agent for VMware and Agent for Windows | 1.5 GB |
| Agent for Hyper-V and Agent for Windows | 1.5 GB |
| Agent for Virtuozzo and Agent for Linux | 1 GB |
| Agent for Virtuozzo Hybrid Infrastructure | 700 MB |
| Agent for Oracle and Agent for Windows | 2.2 GB |
| Agent for Oracle and Agent for Linux | 2 GB |
| Agent for MySQL/MariaDB and Agent for Linux | 2 GB |

## Network requirements

We recommend that the protection agents use a network with a maximum transmission unit (MTU) of 1500 bytes. All devices in this network must use the same MTU settings.

## Memory requirements

Backup operations, including deleting backups, require about 1 GB of RAM per 1 TB of backup size. The memory consumption may vary, depending on the amount and type of data being processed by the agents.

> **Note:** The RAM usage might increase when backing up to extra large backup archives (4 TB and more).

On x64 systems, operations with bootable media and disk recovery with restart require at least 1.5 GB of memory.

## Device Control and DLP on CET-enabled processors

On workloads with modern processors which support CET technology (such as 11th Gen Intel Core or AMD Ryzen 7), some features of the Agent for Data Loss Prevention are disabled to prevent conflicts. The following table lists the availability of Device Control and DLP features on systems with such processors.

### Local channels

| Feature | Device Control | DLP |
|---------|---------------|-----|
| Removable storage | n/a | Yes |
| Encrypted removable storage | Yes | n/a |
| Printers | n/a | No |
| Redirected mapped drives | n/a | Yes |
| Redirected clipboard | n/a | No |

### Network communications

| Feature | Device Control | DLP |
|---------|---------------|-----|
| SMTP emails | n/a | Yes |
| Microsoft Outlook (MAPI) | n/a | Yes |
| IBM Notes | n/a | No |
| Webmails | n/a | Yes |
| Instant messaging (ICQ) | n/a | No |
| Instant messaging (Viber) | n/a | No |
| Instant messaging (IRC, Jabber, Skype, Viber) | n/a | Yes |
| File sharing services | n/a | Yes |
| Social networks | n/a | Yes |
| Local network file sharing (SMB) | n/a | Yes |
| Web access (HTTP/HTTPS) | n/a | Yes |
| File transfers (FTP/FTPS) | n/a | Yes |

### Data transfer allowlisting

| Feature | Device Control | DLP |
|---------|---------------|-----|
| Allowlist for device types | n/a | Yes |
| Allowlist for network communications | n/a | Yes |
| Allowlist for remote hosts | n/a | Yes |
| Allowlist for applications | n/a | Yes |

### Peripheral devices

| Feature | Device Control | DLP |
|---------|---------------|-----|
| Removable storage | Yes | Yes |
| Encrypted removable storage | Yes | Yes |
| Printers | No | No |
| MTP-connected mobile devices | No | No |
| Bluetooth adapters | Yes | Yes |
| Optical drives | Yes | Yes |
| Floppy drives | Yes | Yes |
| Windows clipboard | No | No |
| Screenshot capture | No | No |
| Redirected mapped drives | Yes | Yes |
| Redirected clipboard | No | No |

### Cyber Protect Agent self-protection

| Feature | Device Control | DLP |
|---------|---------------|-----|
| Protection from regular end users | Yes | Yes |
| Protection from local system administrators | Yes | Yes |
