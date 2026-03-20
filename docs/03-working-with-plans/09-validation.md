---
title: "Validation"
section: "Working with plans"
subsection: "Off-host data protection plans"
page_range: "245-247"
tags: ["validation", "checksum", "VM-heartbeat", "screenshot-validation", "backup-verification"]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#validation.html"
---

# Validation

> **Note:** In service-based billing mode, this feature requires the **Servers** quota to be enabled under Standard Protection as a prerequisite, but using the feature does not affect the quota usage. With solution-based billing mode, this functionality is available in customer tenants that use **Ultimate protection**.

You can validate a backup to verify that you can recover the data.

When you validate a backup, you apply a validation method to a backup archive or backup location. Validation of a backup location validates all archives in this location.

To validate a backup as an off-host data processing operation, you must create a validation plan. To validate a backup without creating a validation plan, follow the procedure in "Validating backups" (p. 681).

## Supported locations for validation

| Backup location | Checksum verification | Run as virtual machine: VM heartbeat | Run as virtual machine: Screenshot validation |
|----------------|----------------------|-------------------------------------|---------------------------------------------|
| Cloud storage | + | + | + |
| Local folder | + | + | + |
| Network folder | + | + | + |
| NFS folder | – | – | – |
| Secure Zone | – | – | – |

> **Note:** The validation option is not available for public cloud backups due to the prohibitive costs of reading an entire archive from a public cloud.

## Validation methods

You can select one or more validation methods. If multiple validation methods are selected, they are applied in the following order:

1. VM heartbeat (part of the **Run as virtual machine** validation option)
2. Screenshot validation (part of the **Run as virtual machine** validation option)
3. Checksum verification

The **Run as virtual machine** validation option is available only for disk-level backups that contain an operating system. You can use it on ESXi or Hyper-V hosts that are managed by a protection agent (Agent for VMware or Agent for Hyper-V).

### VM heartbeat

With this validation method, the agent runs a virtual machine from the backup, connects to VMware Tools or Hyper-V Integration Services, and then checks the heartbeat response to ensure that the operating system has started successfully. If the connection fails, the agent attempts to connect every two minutes, to a total of five times. If none of the attempts are successful, the validation fails.

Regardless of the number of validation plans and validated backups, the agent that performs the validation runs one virtual machine at a time. When the validation result is clear, the agent deletes the virtual machine, and then runs the next one.

> **Note:** Use this method only when you validate backups of VMware virtual machines by running these backups as virtual machines on an ESXi host, and backups of Hyper-V virtual machines by running them as virtual machines on a Hyper-V host.

### Screenshot validation

With this validation method, the agent runs a virtual machine from the backup and, while the virtual machine is booting, screenshots are taken for a specific period.

A machine intelligence (MI) module checks the screenshots, and a screenshot is attached to each validated backup (recovery point).

If a screenshot contains a login screen, no more screenshots are taken, and that screenshot is attached. If no screenshot contains a login screen, screenshots are taken until the timeout period ends, and then the last screenshot is attached.

In the Cyber Protect console, you can download the attached screenshot within one year of the validation.

Screenshot validation is supported by agent version 15.0.30971 (released in November, 2022) and later.

> **Note:** Screenshot validation works best with backups of Windows and Linux systems with a GUI-based login screen. This method is not optimized for Linux systems with a console login screen.

### Checksum verification

Validation via checksum verification calculates a checksum for every data block that can be recovered from the backup, and then compares it to the original checksum for the data block that was written during the backup process. The only exception is validation of file-level backups that are located in the cloud storage. These backups are validated by checking the consistency of the metadata that is saved in the backup.

Validation via checksum verification is a time-consuming operation, even for incremental or differential backups, which are usually small in size. The validation operation includes all data that must be recovered, which might be contained in more than one backup.

A successful validation via checksum verification ensures high probability of data recovery. However, validation via this method does not check all factors that can influence the recovery process.

### Changing the timeout for VM heartbeat and screenshot validation

When you validate a backup by running it as a virtual machine, you can configure the timeout between booting the virtual machine and sending the heartbeat request or taking a screenshot.

The default period is as follows:
- **One minute** — For backups stored on a local folder or a network share.
- **Five minutes** — For backups stored in the cloud storage.
