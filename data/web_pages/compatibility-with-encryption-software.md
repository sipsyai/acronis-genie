# Compatibility with encryption software

Managing the backup and recovery of workloads and files > Supported operating systems and environments for backup and recovery > Compatibility with encryption software
Compatibility with encryption software

There are no limitations on backing up and recovering data that is encrypted by file-level encryption software.

Disk-level encryption software encrypts data on the fly. This is why data contained in the backup is not encrypted. Disk-level encryption software often modifies system areas: boot records, or partition tables, or file system tables. These factors affect disk-level backup and recovery, the ability of the recovered system to boot and access to Secure Zone.

You can back up the data encrypted by the following disk-level encryption software:

Microsoft BitLocker Drive Encryption
McAfee Endpoint Encryption
PGP Whole Disk Encryption

To ensure reliable disk-level recovery, follow the common rules and software-specific recommendations.

Common installation rule

We strongly recommend that you install the encryption software before you install the protection agents.

The way of using Secure Zone

Secure Zone must not be encrypted with disk-level encryption. This is the only way to use Secure Zone:

Install the encryption software; then, install the agent.
Create Secure Zone.
Exclude Secure Zone when encrypting the disk or its volumes.
Common backup rule

You can do a disk-level backup in the operating system.

Software-specific recovery procedures
Microsoft BitLocker Drive Encryption

To recover a system that was encrypted by BitLocker:

Boot from the bootable media.
Recover the system. The recovered data will be unencrypted.
Reboot the recovered system.
Turn on BitLocker.

If you only need to recover one partition of a multi-partitioned disk, do so under the operating system. Recovery under bootable media may make the recovered partition undetectable for Windows.

McAfee Endpoint Encryption and PGP Whole Disk Encryption

You can recover an encrypted system partition by using bootable media only.

If the recovered system fails to boot, rebuild Master Boot Record as described in the following Microsoft knowledge base article: https://support.microsoft.com/kb/2622803

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.