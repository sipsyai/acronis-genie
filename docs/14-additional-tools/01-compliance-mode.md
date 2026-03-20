---
title: "Compliance Mode"
section: "Additional Cyber Protection Tools"
subsection: "Compliance Mode"
page_range: "1481-1483"
tags: [compliance-mode, encryption, backup-encryption, aes-256, security, password, recovery, limitations]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#compliance-mode.html"
---

# Compliance Mode

The Compliance mode is designed for clients with higher security demands. This mode requires mandatory encryption for all backups and allows only locally set encryption passwords.

With the Compliance mode, all backups created in a customer tenant and its units are automatically encrypted with the AES algorithm and a 256-bit key. Users can set the encryption passwords only on the protected devices, and cannot set them in the protection plans.

> **Important:** The Compliance mode cannot be disabled.

## Limitations

- The Compliance mode is compatible only with agents version 15.0.26390 or higher.
- The Compliance mode is not available for devices running Red Hat Enterprise Linux 4.x or 5.x, and their derivatives.
- Cloud services cannot access encryption passwords. Due to this limitation, some features are not available for tenants in Compliance mode.

## Unsupported Features

The following features are not available for tenants in Compliance mode:

- Recovery through the Cyber Protect console
- File-level browsing of backups through the Cyber Protect console
- Access to the Web Restore console
- Cloud-to-cloud backup
- Website backup
- Application backup
- Backup of mobile devices
- Antimalware scan of backups
- Safe recovery
- Automatic creation of corporate allowlists
- Data protection map
- Disaster recovery
- Reports and dashboards related to the unavailable features

## Setting the Encryption Password

You must set the encryption password locally, on the protected device. You cannot set the encryption password in the protection plan. Without a password, creating backups will fail.

> **Warning!** There is no way to recover encrypted backups if you lose or forget the password.

You can set the encryption password in the following ways:

1. During the installation of a protection agent (for Windows, macOS, and Linux).
2. By using the command line (for Windows and Linux). This is the only way to set an encryption password on a virtual appliance. For more information on how to set an encryption password with the **Acropsh** tool, see "Encryption" (p. 558).
3. In the Cyber Protect Monitor (for Windows and macOS).

### To Set the Encryption Password in the Cyber Protect Monitor

1. On the protected device, log on as an administrator.
2. Click the Cyber Protect Monitor icon in the notification area (in Windows) or the menu bar (in macOS).
3. Click the gear icon.
4. Click **Encryption**.
5. Set the encryption password.
6. Click **OK**.

## Changing the Encryption Password

You can change the encryption password before a protection plan creates any backups.

We recommend that you do not change the encryption password after backups are created, because subsequent backups will fail. To continue protecting the same machine, you must create a new protection plan for it. Changing both the encryption password and the protection plan will result in creating new backups that are encrypted with the changed password. The backups that were created before these changes will not be affected.

Alternatively, you can keep the applied protection plan, and change only the backup file name in it. This will also result in creating new backups that are encrypted with the changed password.

You can change the encryption password in the following ways:

1. In the Cyber Protect Monitor (for Windows and macOS).
2. By using the command line (for Windows and Linux).

## Recovering Backups in Tenants in Compliance Mode

With Compliance mode, you cannot recover backups in the Cyber Protect console. The following options are available:

- Recovering an entire machine, its disks, or files, by using bootable media.
- Extracting files from local backups of Windows machines with installed agent, by using Windows File Explorer.
