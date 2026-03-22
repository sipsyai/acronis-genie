# Supported operating systems and environments for backup and recovery

Managing the backup and recovery of workloads and files > Supported operating systems and environments for backup and recovery
Supported operating systems and environments for backup and recovery

The information below applies to backup and recovery. For details about supported protection features by operating system, see Supported protection features by operating system.

Agent for Windows

FIPS-compliant mode is supported on 64-bit operating systems. See FIPS-compliant mode.

This agent includes a component for antivirus and antimalware protection and URL filtering that supports a different set of operating systems. See Supported operating systems for antivirus and antimalware protection.

The list of supported operating systems below applies to backup and recovery.
Windows 10 version 1809 and later – Home, Pro, Education, Enterprise, IoT Enterprise and LTSC (formerly LTSB) editions
Windows Server 2019 – all installation options, except for Nano Server
Windows 11 – all editions
Windows Server 2022 – all installation options, except for Nano Server
Windows Server 2025 – all installation options, except for Nano Server
Before you upgrade the operating system of a protected workload where a protection agent or the management server is installed, note the following:
In the case of a major version upgrade (for example, from Windows 7 to Windows 10), you must reinstall the agent or management server after the upgrade, to ensure its proper operation.
In the case of a minor update within a major version (for example, Windows 10 version 20H2 to Windows 10 version 21H1), you do not need to reinstall the agent after updating the operating system.
Agent for Windows (Legacy)

This agent includes a component for antivirus and antimalware protection and URL filtering that supports a different set of operating systems. See Supported operating systems for antivirus and antimalware protection.

The list of supported operating systems below applies to backup and recovery.

Windows XP Professional SP1 (x64), SP2 (x64), SP3 (x86)

On Windows XP systems, Agent for Windows supports only NTFS-formatted drives.
Windows Server 2003 SP1/2003 R2 and later – Standard and Enterprise editions (x86, x64)
Windows Small Business Server 2003/2003 R2
Windows Server 2008, Windows Server 2008 SP2* – Standard, Enterprise, Datacenter, Foundation, and Web editions (x86, x64)
Windows Small Business Server 2008, Windows Small Business Server 2008 SP2*

Windows 7 – all editions

To use Cyber Protection with Windows 7, you must install the following updates from Microsoft before installing the protection agent:

Windows 7 Extended Security Updates (ESU)
KB4474419
KB4490628

For more information on the required updates, see this knowledge base article.

Windows Server 2008 R2* – Standard, Enterprise, Datacenter, Foundation, and Web editions
Windows Home Server 2011*
Windows MultiPoint Server 2010*/2011*/2012
Windows Small Business Server 2011* – all editions
Windows 8/8.1 – all editions (x86, x64), except for the Windows RT editions
Windows Server 2012/2012 R2 – all editions
Windows Storage Server 2003/2008/2008 R2/2012/2012 R2/2016
Windows 10 version 1803 and earlier – Home, Pro, Education, Enterprise, IoT Enterprise and LTSC (formerly LTSB) editions
Windows Server 2016 – all installation options, except for Nano Server

* To use Cyber Protection with this version of Windows, you must install the SHA2 code signing support update from Microsoft (KB4474419) before installing the protection agent.

For information on issues related to the SHA2 code signing support update, see this knowledge base article.

Before you upgrade the operating system of a protected workload where a protection agent or the management server is installed, note the following:
In the case of a major version upgrade (for example, from Windows 7 to Windows 10), you must reinstall the agent or management server after the upgrade, to ensure its proper operation.
In the case of a minor update within a major version (for example, Windows 10 version 20H2 to Windows 10 version 21H1), you do not need to reinstall the agent after updating the operating system.
Agent for SQL, Agent for Active Directory, Agent for Exchange (for database backup and application-aware backup)

These agents are delivered as part of Agent for Windows and Agent for Windows (Legacy). With Agent for Windows, FIPS-compliant mode is supported on 64-bit operating systems. See FIPS-compliant mode.

Each of these agents is supported on the same Windows versions as Agent for Windows and Agent for Windows (Legacy), and can be installed on a machine running a supported version of the respective application, with the following exception:

Windows Server 2025 is not supported.
Agent for Data Loss Prevention

This agent is delivered as part of Agent for Windows and Agent for Windows (Legacy). With Agent for Windows, FIPS-compliant mode is supported on 64-bit operating systems. See FIPS-compliant mode.

Device control

Microsoft Windows 7 Service Pack 1 and later
Microsoft Windows Server 2008 R2 – Windows Server 2022
macOS 10.15 (Catalina)
macOS 11.2.3 (Big Sur)
macOS 12 (Monterey)
macOS 13 (Ventura)
macOS 14 (Sonoma)
macOS 15 (Sequoia)
Agent for Data Loss Prevention for macOS supports only x64 processors. Apple silicon ARM-based processors are not supported.

Data loss prevention

Microsoft Windows 7 Service Pack 1 and later
Microsoft Windows Server 2008 R2 – Windows Server 2022

Agent for Data Loss Prevention might be installed on unsupported macOS systems because it is an integral part of Agent for Mac. In this case, the Cyber Protect console will indicate that Agent for Data Loss Prevention is installed on the computer, but the device control and data loss prevention functionality will not work. Device control functionality will only work on macOS systems that are supported by Agent for Data Loss Prevention.

Agent for File Sync & Share

This agent is delivered as part of Agent for Windows and Agent for Windows (Legacy).

Agent for File Sync & Share supports a different set of operating systems than Agent for Windows and Agent for Windows (Legacy).

To check the operating systems that Agent for File Sync & Share supports, see the Cyber Files Cloud documentation.

Agent for Exchange (for mailbox backup)

This agent is delivered as part of Agent for Windows and Agent for Windows (Legacy). With Agent for Windows, FIPS-compliant mode is supported on 64-bit operating systems. See FIPS-compliant mode.

Windows Server 2008 – Standard, Enterprise, Datacenter, Foundation, and Web editions (x86, x64)

Windows Small Business Server 2008

Windows 7 – all editions

Windows Server 2008 R2 – Standard, Enterprise, Datacenter, Foundation, and Web editions

Windows MultiPoint Server 2010/2011/2012

Windows Small Business Server 2011 – all editions

Windows 8/8.1 – all editions (x86, x64), except for the Windows RT editions

Windows Server 2012/2012 R2 – all editions

Windows Storage Server 2008/2008 R2/2012/2012 R2

Windows 10 – Home, Pro, Education, and Enterprise editions

Windows Server 2016 – all installation options, except for Nano Server

Windows Server 2019 – all installation options, except for Nano Server

Windows 11 – all editions

Windows Server 2022 – all installation options, except for Nano Server

Agent for Microsoft 365

This agent is delivered as part of Agent for Windows and Agent for Windows (Legacy). With Agent for Windows, FIPS-compliant mode is supported on 64-bit operating systems. See FIPS-compliant mode.

Windows Server 2008 – Standard, Enterprise, Datacenter, Foundation, and Web editions (x64 only)

Windows Small Business Server 2008

Windows Server 2008 R2 – Standard, Enterprise, Datacenter, Foundation, and Web editions

Windows Home Server 2011

Windows Small Business Server 2011 – all editions

Windows 8/8.1 – all editions (x64 only), except for the Windows RT editions

Windows Server 2012/2012 R2 – all editions

Windows Storage Server 2008/2008 R2/2012/2012 R2/2016 (x64 only)

Windows 10 – Home, Pro, Education, and Enterprise editions (x64 only)

Windows Server 2016 – all installation options (x64 only), except for Nano Server

Windows Server 2019 – all installation options (x64 only), except for Nano Server

Windows 11 – all editions

Windows Server 2022 – all installation options, except for Nano Server

Agent for Oracle

This agent is delivered as part of Agent for Windows, Agent for Windows (Legacy), and Agent for Linux (64-bit). With Agent for Windows and Agent for Linux, FIPS-compliant mode is supported on 64-bit operating systems.

Windows Server 2008R2 – Standard, Enterprise, Datacenter, and Web editions (x86, x64)

Windows Server 2012R2 – Standard, Enterprise, Datacenter, and Web editions (x86, x64)

Linux – any kernel and distribution supported by Agent for Linux (listed below)

Agent for MySQL/MariaDB

This agent is delivered as part of Agent for Linux (64-bit).

FIPS-compliant mode is supported. See FIPS-compliant mode.

Linux – any kernel and distribution supported by Agent for Linux (listed below)
Agent for Linux

FIPS-compliant mode is supported. See FIPS-compliant mode.

This agent includes a component for antivirus and antimalware protection and URL filtering that supports a different set of operating systems. See Supported operating systems for antivirus and antimalware protection.

The list of supported operating systems below applies to backup and recovery.

Cyber Protect Cloud supports x86 and x86_64 Linux distributions that use the following components:

Kernel version from 2.6.9 to 6.15

Supported kernel versions are listed according to the releases in www.kernel.org. Some distributions, such as Red Hat Enterprise Linux, backport new features to older kernel versions. Such distribution-specific kernels might not be supported even though their version is within the supported range.

The GNU C library (glibc) 2.3.4 or later

The following distributions have been specifically tested. However, even if your Linux distribution or kernel version is not listed below, it might still work correctly in all required scenarios, due to the specifics of the Linux operating systems. If you encounter issues while using Cyber Protect Cloud with your combination of distribution and kernel version, contact the Support team for further investigation.

Red Hat Enterprise Linux 4.x, 5.x, 6.x, 7.x, 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 8.10*, 9.0*, 9.1*, 9.2*, 9.3*, 9.4*, 9.5*, 9.6*, 9.7*, 10*, 10.1*

Ubuntu 9.10, 10.04, 10.10, 11.04, 11.10, 12.04, 12.10, 13.04, 13.10, 14.04, 14.10, 15.04, 15.10, 16.04, 16.10, 17.04, 17.10, 18.04, 18.10, 19.04, 19.10, 20.04, 20.10, 21.04, 21.10, 22.04, 22.10, 23.04, 23.10, 24.04, 24.10, 25.04, 25.10

Fedora 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39, 40, 41, 42, 43

Configurations with Btrfs are not supported. For more information, see Supported file systems.

SUSE Linux Enterprise Server 10, 11, 12, 15

Configurations with Btrfs are not supported. For more information, see Supported file systems.

Debian 4.x, 5.x, 6.x, 7.0, 7.2, 7.4, 7.5, 7.6, 7.7, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.11, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 10, 11, 12, 13

CentOS 5.x, 6.x, 7.x, 8.x*

CentOS Stream 8*, 9*, 10*

Oracle Linux 5.x, 6.x, 7.x, 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 9.0*, 9.1*, 9.2*, 9.3*, 9.4*, 9.5*, 9.6*, 9.7*, 10*, 10.1* – both Unbreakable Enterprise Kernel and Red Hat Compatible Kernel

Installing the protection agent on Oracle Linux 8.6 and later, on which Secure Boot is enabled, requires manual signing of kernel modules. For more information on how to sign a kernel module, see this knowledge base article.

CloudLinux 5.x, 6.x, 7.x, 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 8.10*, 9.4*, 9.5*, 9.6*, 10*

ClearOS 5.x, 6.x, 7.x

AlmaLinux 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 8.10*, 9.0*, 9.1*, 9.2*, 9.3*, 9.4*, 9.5*, 9.6*, 9.7*, 10*, 10.1*

Rocky Linux 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 8.10*, 9.0*, 9.1*, 9.2*, 9.3*, 9.4*, 9.5*, 9.6*, 9.7*, 10*, 10.1*

ALT Linux 7.0

* Starting from version 8.4, supported only with kernels 4.18 and later.

Before you upgrade the operating system of a protected workload where the Cyber Protection agent or a management server is installed, note the following.
In the case of a major version upgrade, you must reinstall the agent or the management server after the upgrade to ensure its proper operation.
Before you install a new kernel version, check the Agent for Linux section to verify that the version is supported.
Agent for Mac

This agent includes a component for antivirus and antimalware protection and URL filtering that supports a different set of operating systems. See Supported operating systems for antivirus and antimalware protection.

The list of supported operating systems below applies to backup and recovery.

Both x64 and ARM architecture (used in Apple silicon processors such as Apple M1, M2, and later) are supported.

You cannot recover disk-level backups of Intel-based Macs to Macs that use Apple silicon processors, and vice-versa. You can recover files and folders.
macOS High Sierra 10.13
macOS Mojave 10.14
macOS Catalina 10.15
macOS Big Sur 11
macOS Monterey 12
macOS Ventura 13
macOS Sonoma 14
macOS Sequoia 15
macOS Tahoe 26
The agent also supports all minor versions of the operating systems listed above. For example, macOS Sonoma 14.5.

Starting from version C23.07, Cyber Protect Cloud does not support the following operating systems: OS X Yosemite 10.10, OS X El Capitan 10.11, and macOS Sierra 10.12.

Cyber Protect Monitor does not support macOS versions 10.x and 11.x.

We strongly recommend that you upgrade your operating system to a supported version in order to ensure compatibility and be able to use the full functionality of Cyber Protect Cloud.

Agent for VMware (Virtual Appliance)

This agent is delivered as a virtual appliance that runs on an ESXi host.

FIPS-compliant mode is supported. See FIPS-compliant mode.

VMware ESXi 4.1, 5.0, 5.1, 5.5, 6.0, 6.5, 6.7, 7.0, 8.0

In FIPS-compliant mode, only VMware ESXi 8.0 is supported.

Agent for VMware (Windows)

This agent is delivered as part of Agent for Windows and Agent for Windows (Legacy). With Agent for Windows, FIPS-compliant mode is supported on 64-bit operating systems. See FIPS-compliant mode.

This agent is supported on the same Windows versions as Agent for Windows and Agent for Windows (Legacy) with the following limitations:

32-bit operating systems are not supported.
Windows XP, Windows Server 2003/2003 R2, and Windows Small Business Server 2003/2003 R2 are not supported.
In FIPS-compliant mode, only VMware ESXi 8.0 is supported.
Agent for Hyper-V

This agent is delivered as part of Agent for Windows and Agent for Windows (Legacy). With Agent for Windows, FIPS-compliant mode is supported on 64-bit operating systems. See FIPS-compliant mode.

Windows Server 2008 (x64 only) with Hyper-V role, including Server Core installation mode
Windows Server 2008 R2 with Hyper-V role, including Server Core installation mode
Microsoft Hyper-V Server 2008/2008 R2
Windows Server 2012/2012 R2 with Hyper-V role, including Server Core installation mode
Microsoft Hyper-V Server 2012/2012 R2
Windows 8, 8.1 (x64 only) with Hyper-V
Windows 10 – Pro, Education, and Enterprise editions with Hyper-V
Windows 11 – Pro, Education, and Enterprise editions with Hyper-V
Windows Server 2016 with Hyper-V role – all installation options, except for Nano Server
Microsoft Hyper-V Server 2016
Windows Server 2019 with Hyper-V role – all installation options, except for Nano Server
Microsoft Hyper-V Server 2019
Windows Server 2022 – all installation options, except for Nano Server
Windows Server 2025 – all installation options, except for Nano Server
Agent for Virtuozzo

This agent is delivered as part of Agent for Linux (64-bit).

FIPS-compliant mode is supported. See FIPS-compliant mode.

Virtuozzo 6.0.10, 6.0.11, 6.0.12, 7.0.13, 7.0.14
Virtuozzo Hybrid Server 7.5
Agent for Virtuozzo Hybrid Infrastructure

This agent is delivered as a virtual appliance that runs on a Virtuozzo Hybrid Infrastructure host.

FIPS-compliant mode is supported. See FIPS-compliant mode.

Virtuozzo Hybrid Infrastructure 3.5, 4.0, 4.5, 4.6, 4.7, 5.0, 5.1, 5.2, 5.3, 5.4, 6.0, 6.1, 6.2, 6.3

Agent for Scale Computing HC3

This agent is delivered as a virtual appliance that runs on a Scale Computing HC3 host.

FIPS-compliant mode is supported. See FIPS-compliant mode.

Scale Computing HyperCore 8.8, 8.9, 9.0, 9.1, 9.2, 9.3, 9.4

Agent for oVirt

This agent is delivered as a virtual appliance that runs on a KVM hypervisor host managed by oVirt.

FIPS-compliant mode is supported. See FIPS-compliant mode.

Red Hat Virtualization 4.2, 4.3, 4.4, 4.5

Agent for Synology

This agent is delivered as a virtual appliance that runs on a Synology NAS.

DiskStation Manager 6.2.x, 7.x

Agent for Synology supports only NAS devices with x86_64 processors. ARM processors are not supported. See the Synology knowledge center.

Agent for Azure

This agent is delivered as a virtual appliance that runs in your Microsoft Azure Subscription.

Agent for Nutanix

This agent is delivered as a virtual appliance that runs in a Nutanix AHV cluster.

Nutanix Acropolis Operating System (AOS) 6.5, 6.6, 6.7, 6.8, 6.10

Cyber Protect Monitor

With Agent for Windows

Windows 10 version 1809 and later
Windows Server 2019 and later

With Agent for Windows (Legacy)

Windows 7 and later
Windows Server 2008 R2 and later

With Agent for Mac

All macOS versions that are supported by Agent for Mac, except macOS 10.x and macOS 11.x.

Supported Microsoft SQL Server versions

Supported Microsoft Exchange Server versions

Supported Microsoft SharePoint versions

Supported Oracle Database versions

Supported SAP HANA versions

Supported MySQL versions

Supported MariaDB versions

Supported virtualization platforms

Compatibility with Dell EMC Data Domain storages

Supported file systems

Supported operations with logical volumes

Compatibility with encryption software

Compatibility with Advanced Format (4K-sector) hard disks

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.