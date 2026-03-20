---
title: "Backup and recovery overview - Supported Windows operating systems"
section: "Managing the backup and recovery of workloads and files"
subsection: "Supported operating systems and environments for backup and recovery"
page_range: "484-486"
tags: ["backup", "recovery", "supported-os", "Windows", "Agent-for-Windows", "Legacy", "DLP", "device-control"]
acronis_version: "26.02"
---

# Managing the backup and recovery of workloads and files

The backup module enables backup and recovery of physical and virtual machines, files, and databases to local or cloud storage.

## Supported operating systems and environments for backup and recovery

The information below applies to backup and recovery. For details about supported protection features by operating system, see [Supported protection features by operating system](../01-getting-started/10a-supported-features-protection-plans-and-backup.md).

## Agent for Windows

FIPS-compliant mode is supported on 64-bit operating systems.

This agent includes a component for antivirus and antimalware protection and URL filtering that supports a different set of operating systems. See "Supported operating systems for antivirus and antimalware protection" (p. 1062).

The list of supported operating systems below applies to backup and recovery:

- Windows 10 version 1809 and later — Home, Pro, Education, Enterprise, IoT Enterprise and LTSC (formerly LTSB) editions
- Windows Server 2019 — all installation options, except for Nano Server
- Windows 11 — all editions
- Windows Server 2022 — all installation options, except for Nano Server
- Windows Server 2025 — all installation options, except for Nano Server

> **Important:** Before you upgrade the operating system of a protected workload where a protection agent or the management server is installed, note:
> - In the case of a major version upgrade (e.g., from Windows 7 to Windows 10), you must reinstall the agent or management server after the upgrade.
> - In the case of a minor update within a major version (e.g., Windows 10 version 20H2 to 21H1), you do not need to reinstall the agent.

## Agent for Windows (Legacy)

This agent includes a component for antivirus and antimalware protection and URL filtering that supports a different set of operating systems.

- Windows XP Professional SP1 (x64), SP2 (x64), SP3 (x86)
  > **Note:** On Windows XP systems, Agent for Windows supports only NTFS-formatted drives.
- Windows Server 2003 SP1/2003 R2 and later — Standard and Enterprise editions (x86, x64)
- Windows Small Business Server 2003/2003 R2
- Windows Server 2008, Windows Server 2008 SP2* — Standard, Enterprise, Datacenter, Foundation, and Web editions (x86, x64)
- Windows Small Business Server 2008, Windows Small Business Server 2008 SP2*
- Windows Server 2008 R2* — Standard, Enterprise, Datacenter, Foundation, and Web editions
- Windows Home Server 2011*
- Windows MultiPoint Server 2010*/2011*/2012
- Windows Small Business Server 2011* — all editions
- Windows 8/8.1 — all editions (x86, x64), except for the Windows RT editions
- Windows Server 2012/2012 R2 — all editions
- Windows Storage Server 2003/2008/2008 R2/2012/2012 R2/2016
- Windows 10 version 1803 and earlier — Home, Pro, Education, Enterprise, IoT Enterprise and LTSC (formerly LTSB) editions
- Windows Server 2016 — all installation options, except for Nano Server
- Windows 7 — all editions

> **Note:** To use Cyber Protection with Windows 7, you must install the following updates from Microsoft:
> - Windows 7 Extended Security Updates (ESU)
> - KB4474419
> - KB4490628

> **Note:** * To use Cyber Protection with these versions, you must install the SHA2 code signing support update from Microsoft (KB4474419) before installing the protection agent.

## Agent for SQL, Agent for Active Directory, Agent for Exchange (database backup and application-aware backup)

These agents are delivered as part of Agent for Windows and Agent for Windows (Legacy). With Agent for Windows, FIPS-compliant mode is supported on 64-bit operating systems.

Each of these agents is supported on the same Windows versions as Agent for Windows and Agent for Windows (Legacy), with the following exception:

- Windows Server 2025 is not supported.

## Agent for Data Loss Prevention

This agent is delivered as part of Agent for Windows and Agent for Windows (Legacy). With Agent for Windows, FIPS-compliant mode is supported on 64-bit operating systems.

### Device control

- Microsoft Windows 7 Service Pack 1 and later
- Microsoft Windows Server 2008 R2 — Windows Server 2022
- macOS 10.15 (Catalina)
- macOS 11.2.3 (Big Sur)
- macOS 12 (Monterey)
- macOS 13 (Ventura)
- macOS 14 (Sonoma)
- macOS 15 (Sequoia)

> **Note:** Agent for Data Loss Prevention for macOS supports only x64 processors. Apple silicon ARM-based processors are not supported.

### Data loss prevention

- Microsoft Windows 7 Service Pack 1 and later
- Microsoft Windows Server 2008 R2 — Windows Server 2022
