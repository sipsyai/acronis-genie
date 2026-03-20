---
title: "Supported operating systems - Linux and macOS"
section: "Managing the backup and recovery of workloads and files"
subsection: "Supported operating systems and environments for backup and recovery"
page_range: "488-491"
tags: ["backup", "recovery", "supported-os", "Linux", "macOS", "kernel", "RHEL", "Ubuntu", "Debian", "CentOS", "Rocky", "AlmaLinux"]
acronis_version: "26.02"
---

# Agent for Linux

FIPS-compliant mode is supported. This agent includes a component for antivirus and antimalware protection and URL filtering that supports a different set of operating systems.

Cyber Protect Cloud supports x86 and x86_64 Linux distributions that use the following components:

- **Kernel version** from 2.6.9 to 6.15
  Supported kernel versions are listed according to the releases in www.kernel.org. Some distributions, such as Red Hat Enterprise Linux, backport new features to older kernel versions. Such distribution-specific kernels might not be supported even though their version is within the supported range.
- **The GNU C library (glibc)** 2.3.4 or later

The following distributions have been specifically tested. However, even if your Linux distribution or kernel version is not listed below, it might still work correctly in all required scenarios, due to the specifics of the Linux operating systems.

### Tested distributions

- **Red Hat Enterprise Linux** 4.x, 5.x, 6.x, 7.x, 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 8.10*, 9.0*, 9.1*, 9.2*, 9.3*, 9.4*, 9.5*, 9.6*, 9.7*, 10*, 10.1*
- **Ubuntu** 9.10, 10.04, 10.10, 11.04, 11.10, 12.04, 12.10, 13.04, 13.10, 14.04, 14.10, 15.04, 15.10, 16.04, 16.10, 17.04, 17.10, 18.04, 18.10, 19.04, 19.10, 20.04, 20.10, 21.04, 21.10, 22.04, 22.10, 23.04, 23.10, 24.04, 24.10, 25.04, 25.10
- **Fedora** 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 37, 38, 39, 40, 41, 42, 43

  > **Important:** Configurations with Btrfs are not supported.

- **SUSE Linux Enterprise Server** 10, 11, 12, 15

  > **Important:** Configurations with Btrfs are not supported.

- **Debian** 4.x, 5.x, 6.x, 7.0, 7.2, 7.4, 7.5, 7.6, 7.7, 8.0, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 8.8, 8.11, 9.0, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 10, 11, 12, 13
- **CentOS** 5.x, 6.x, 7.x, 8.x*
- **CentOS Stream** 8*, 9*, 10*
- **Oracle Linux** 5.x, 6.x, 7.x, 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 9.0*, 9.1*, 9.2*, 9.3*, 9.4*, 9.5*, 9.6*, 9.7*, 10*, 10.1* — both Unbreakable Enterprise Kernel and Red Hat Compatible Kernel

  > **Note:** Installing the protection agent on Oracle Linux 8.6 and later, on which Secure Boot is enabled, requires manual signing of kernel modules.

- **CloudLinux** 5.x, 6.x, 7.x, 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 8.10*, 9.0*, 9.1*, 9.2*, 9.3*, 9.4*, 9.5*, 9.6*, 10*
- **ClearOS** 5.x, 6.x, 7.x
- **AlmaLinux** 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 8.10*, 9.0*, 9.1*, 9.2*, 9.3*, 9.4*, 9.5*, 9.6*, 9.7*, 10*, 10.1*
- **Rocky Linux** 8.0, 8.1, 8.2, 8.3, 8.4*, 8.5*, 8.6*, 8.7*, 8.8*, 8.9*, 8.10*, 9.0*, 9.1*, 9.2*, 9.3*, 9.4*, 9.5*, 9.6*, 9.7*, 10*, 10.1*
- **ALT Linux** 7.0

\* Starting from version 8.4, supported only with kernels 4.18 and later.

> **Important:** Before you upgrade the operating system of a protected workload where the Cyber Protection agent or a management server is installed:
> - In the case of a major version upgrade, you must reinstall the agent or management server.
> - Before you install a new kernel version, check the "Agent for Linux" section to verify that the version is supported.

---

# Agent for Mac

This agent includes a component for antivirus and antimalware protection and URL filtering that supports a different set of operating systems.

Both x64 and ARM architecture (used in Apple silicon processors such as Apple M1, M2, and later) are supported.

> **Note:** You cannot recover disk-level backups of Intel-based Macs to Macs that use Apple silicon processors, and vice-versa. You can recover files and folders.

### Supported macOS versions

- macOS High Sierra 10.13
- macOS Mojave 10.14
- macOS Catalina 10.15
- macOS Big Sur 11
- macOS Monterey 12
- macOS Ventura 13
- macOS Sonoma 14
- macOS Sequoia 15
- macOS Tahoe 26

> **Note:** The agent also supports all minor versions of the operating systems listed above. For example, macOS Sonoma 14.5.

> **Important:** Starting from version C23.07, Cyber Protect Cloud does not support the following operating systems: OS X Yosemite 10.10, OS X El Capitan 10.11, and macOS Sierra 10.12. Cyber Protect Monitor does not support macOS 10.x and 11.x.
