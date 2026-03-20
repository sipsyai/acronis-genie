---
title: "Supported protection features by OS - Default plans, Forensic backup, CDP, Autodiscovery"
section: "Getting Started with Cyber Protection"
subsection: "Supported protection features by operating system"
page_range: "26-28"
tags: ["features", "os-support", "protection-plans", "forensic-backup", "CDP", "autodiscovery", "compatibility"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#default-plans.html"
---

# Supported protection features by operating system

This topic contains information about the protection features of Cyber Protect Cloud. For the list of operating systems and environments supported by backup and recovery, see "Supported operating systems and environments for backup and recovery" (p. 484).

The protection features are only supported on machines on which a protection agent is installed. They are not available for virtual machines that are backed up in the agentless mode, for example, by Agent for Hyper-V, Agent for VMware, Agent for Virtuozzo Hybrid Infrastructure, Agent for Scale Computing, or Agent for oVirt.

Some features might require additional licensing, depending on the applied licensing model.

## Default protection plans

| Feature | Windows | Linux | macOS |
|---------|---------|-------|-------|
| Remote Workers | Yes | No | No |
| Office Workers (third-party antivirus) | Yes | No | No |
| Office Workers (Cyber Protect antivirus) | Yes | No | No |
| Cyber Protect Essentials (only for Cyber Protect Essentials edition) | Yes | No | No |

See: [Supported operating systems and versions](./11-supported-operating-systems-and-versions.md) for supported Windows versions.

## Forensic backup

| Feature | Windows | Linux | macOS |
|---------|---------|-------|-------|
| Collecting memory dump | Yes | No | No |
| Snapshot of running processes | Yes | No | No |
| Notarization of local image forensic backup | Yes | No | No |
| Notarization of cloud image forensic backup | Yes | No | No |

See: [Supported operating systems and versions](./11-supported-operating-systems-and-versions.md) for supported Windows versions.

## Continuous data protection (CDP)

| Feature | Windows | Linux | macOS |
|---------|---------|-------|-------|
| CDP for files and folders | Yes | No | No |
| CDP for changed files via application tracking | Yes | No | No |

See: [Supported operating systems and versions](./11-supported-operating-systems-and-versions.md) for supported Windows versions.

## Autodiscovery and remote installation

| Feature | Windows | Linux | macOS |
|---------|---------|-------|-------|
| Network-based discovery | Yes | No | No |
| Active Directory-based discovery* | Yes | No | No |
| Template-based discovery (importing machines from a file) | Yes | No | No |
| Manual adding of devices | Yes | No | No |

See: [Supported operating systems and versions](./11-supported-operating-systems-and-versions.md) for supported Windows versions.

*Active Directory-based discovery does not operate as expected with the default configuration of Windows Server 2025 because it enforces LDAP encryption by default.
