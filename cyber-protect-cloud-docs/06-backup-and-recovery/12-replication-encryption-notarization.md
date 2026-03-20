---
title: "Replication, encryption, and notarization"
section: "Managing the backup and recovery of workloads and files"
subsection: "Backup"
page_range: "556-562"
tags: ["replication", "encryption", "AES-256", "notarization", "blockchain", "backup-security", "physical-data-shipping", "off-site", "password"]
acronis_version: "26.02"
---

# Replication

With replication, each new backup is automatically copied to a replication location. The backups in the replication location do not depend on the backups in the source location, and vice versa.

Only the last backup in the source location is replicated. However, if earlier backups are not replicated (for example, due to a network connection problem), the replication operation will include all backups created after the last successful replication.

If a replication operation is interrupted, the processed data will be used by the next replication operation.

## Usage examples

- **Ensuring reliable recovery** -- Store backups both on-site (for immediate recovery) and off-site (to guarantee that backups stay safe in case of storage failure or natural disaster).
- **Using cloud storage to protect data from a natural disaster** -- Replicate the backups to the cloud storage by transferring only the data changes.
- **Keeping only the latest recovery points** -- Configure retention rules to delete older backups from a fast storage, to save on storage costs.

## Supported locations

| Location | As source location | As replication location |
|---|---|---|
| Local folder | Yes | Yes |
| Network folder | Yes | Yes |
| Cloud storage | No* | Yes |
| Secure Zone | Yes | Yes |
| Public cloud | No* | Yes |

*Replication from public cloud is available only in off-host data processing plans.

## To enable replication

1. In a protection plan, expand the **Backup** module, and then click **Add location**.

> **Note:** The **Add location** option is not available when you select the cloud storage in **Where to back up**.

2. From the list of available locations, select the replication location. The location appears as **2nd location**, **3rd location**, **4th location**, or **5th location**.
3. [Optional] Click the gear icon to configure options:
   - **Performance and backup window** -- define the replication performance.
   - **Remove location** -- delete the currently selected replication location.
   - [Only for cloud storage] **Physical Data Shipping** -- save the initial backup on a removable storage device and ship it for upload to the cloud storage, instead of replicating it over the Internet. Suitable for slow network connections or large files. Requires a Physical Data Shipping service quota.
4. [Optional] In **How many to keep** under the replication location, configure the retention rules for that location.
5. [Optional] Repeat steps 1-4 to add more replication locations (up to four: 2nd through 5th location). If you select **Cloud storage**, you cannot add more replication locations.

> **Important:** If you enable backup and replication in the same protection plan, ensure that the replication completes before the next scheduled backup. If the replication is still in progress, the scheduled backup will not start. To avoid this dependency, use a separate plan for backup replication.

# Encryption

Cyber Protect uses two levels of security to protect backed-up data from unauthorized access.

Backed-up data is encrypted with a 256-bit key, which is in turn encrypted by using the SHA-2 (256-bit) hash of a user-provided encryption password as a key, as follows:

1. When creating a protection plan with encryption enabled, the user specifies an encryption password.

> **Warning:** Cyber Protect does not store this password. Recovering a lost password is not possible.

2. Password-Based Key Derivation Function 2 (PBKDF2) is applied to the user-provided encryption password 1,048,576 times (2^20). As a result, a SHA-2 (256-bit) hash is created. This is the first key, which is used to encrypt the second key.
3. A random 256-bit key is created by using OpenSSL. This is the second key, which is used to encrypt the backed-up data.
4. The second key is encrypted by using Advanced Encryption Standard (AES-256), and the hash that is derived from the user-provided encryption password.
5. The encrypted second key is added to the backup archive.
6. Backed-up data is encrypted by using AES-256 GCM and the second key.
7. When recovering data, the user must provide the encryption password. The hash of that password is the first encryption key. This key is used to decrypt the second key. With the second key, the backup archive can be decrypted and recovered.

> **Note:** Using the AES-256 algorithm with a strong password provides quantum-resistant encryption. It is safe against cryptanalytic attacks that rely on quantum computing.

We recommend that you encrypt all backups stored in the cloud storage, especially if your company is subject to regulatory compliance.

## Configuring encryption in the protection plan

In a protection plan, encryption is enabled by default. The AES-256 algorithm is used.

For accounts in Compliance mode, you cannot configure encryption in the protection plan. Use encryption as a machine property instead.

1. In a protection plan, expand the **Backup** module.
2. In **Encryption**, click **Specify password**.
3. Specify and confirm the encryption password.
4. Click **OK**.

> **Warning:** There is no way to recover encrypted backups if you lose or forget the password.

You cannot change the encryption settings after you apply the protection plan. To use different encryption settings, create a new plan.

## Configuring encryption as a machine property

You can configure backup encryption as a machine property. In this case, backup encryption is not configured in the protection plan, but on the protected workload. Encryption as a machine property uses the AES algorithm with a 256-bit key (AES-256).

Configuring encryption as a machine property affects the protection plans in the following way:
- **Protection plans already applied to the machine:** If the encryption settings in a protection plan are different, the backups will fail.
- **Protection plans applied to the machine later:** The encryption settings saved on the machine will override the encryption settings in the protection plan. Any backup will be encrypted, even if encryption is disabled in the Backup module settings.

For accounts in Compliance mode, only encryption as a machine property is available.

If you have more than one Agent for VMware connected to the same vCenter Server, and you configure encryption as a machine property, you must use the same encryption password on all machines with Agent for VMware, because of the load balancing between the agents.

### On the command line

1. Log in as administrator (Windows) or root user (Linux).
2. Navigate to the **acropsh** tool:
   - Windows: `<installation_path>\PyShell\bin\` (where `<installation_path>` is `%ProgramFiles%\BackupClient`)
   - Linux: `/usr/sbin/`
   - Virtual appliance: `/./sbin/`
3. Run: `acropsh.exe -m manage_creds --set-password` (Windows) or `acropsh -m manage_creds --set-password` (Linux/VA)
4. Enter the encryption password at the interactive prompt.

Alternatively, prepare a text file containing `--set-password <password>` and run: `acropsh -m manage_creds @<file_path>`. Delete the file after this procedure.

### In Cyber Protect Monitor (Windows and macOS)

1. Click the Cyber Protect Monitor icon.
2. Click the gear icon, and then click **Settings** > **Encryption**.
3. Select **Set a password for this machine**. Specify and confirm the encryption password.
4. Click **Save**.

### To reset the encryption settings

Run: `acropsh.exe -m manage_creds --reset` (Windows) or `acropsh -m manage_creds --reset` (Linux/VA).

> **Important:** If you reset the encryption as a machine property or change the encryption password after a protection plan creates a backup, the next backup operation will fail. To continue backing up the workload, create a new protection plan.

# Notarization

Notarization enables you to prove that a file is authentic and unchanged since it was backed up. We recommend that you enable notarization when backing up your legal document files or other files that require proved authenticity.

Notarization is available only for file-level backups. Files that have a digital signature are skipped, because they do not need to be notarized.

Notarization is *not* available:
- If the backup format is set to **Version 11**
- If the backup destination is Secure Zone

## How to use notarization

To enable notarization of all files selected for backup (except for files that have a digital signature), enable the **Notarization** switch when creating a protection plan.

When configuring recovery, the notarized files will be marked with a special icon, and you can verify the file authenticity.

## How it works

During a backup, the agent calculates the hash codes of the backed-up files, builds a hash tree (based on the folder structure), saves the tree in the backup, and then sends the hash tree root to the notary service. The notary service saves the hash tree root in the Ethereum blockchain database to ensure that this value does not change.

When verifying file authenticity, the agent calculates the hash of the file and compares it with the hash stored in the hash tree inside the backup. If these hashes do not match, the file is considered not authentic. Otherwise, the file authenticity is guaranteed by the hash tree.

To verify that the hash tree itself was not compromised, the agent sends the hash tree root to the notary service, which compares it with the one stored in the blockchain database. If the hashes match, the selected file is guaranteed to be authentic.
