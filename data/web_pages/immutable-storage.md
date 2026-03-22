# Immutable storage

Additional Cyber Protection tools > Immutable storage
Immutable storage

Immutable storage provides a critical layer of protection for backup data by preventing deletion or modification of restore points until their retention period expires. This safeguard ensures that backups remain intact even if credentials are compromised, ransomware disables security tools, or administrative errors occur. While enabling immutability may slightly increase storage costs because older restore points cannot be deleted before their retention period expires, this predictable expense is minimal compared to the financial and operational impact of losing critical data. Real-world incidents have demonstrated that immutability can be the difference between a full recovery and catastrophic data loss.

Immutable storage is available for all cloud backups stored in a supported cloud storage instance. See Supported storages and agents.

With immutable storage, you can access deleted backups during the specified retention period. You can recover content from these backups, but you cannot change, move, or delete them. When the retention period ends, the deleted backups are permanently deleted.

The immutable storage contains the following backups:

Backups that are deleted manually.
Backups that are deleted automatically, according to the settings in the How long to keep section in a protection plan or the Retention rules section in a cleanup plan.

Deleted backups in the immutable storage still use storage space and are charged accordingly.

Deleted tenants are not charged for any storage, including immutable storage.

Immutable storage modes

Immutable storage is available in the following modes:

Governance mode

In this mode, all deleted backups remain in immutable storage for the specified retention period. This prevents ransomware or malicious actors from tampering with or erasing backup data and ensures the integrity of backups, which is essential for reliable disaster recovery.

In this mode, you can change the retention period or switch to Compliance mode. Immutable storage can be disabled only by contacting the Support team.

Compliance mode

In addition to the benefits of the Governance mode, the Compliance mode helps organizations meet the regulatory requirements for data retention and security by preventing changes in the retention policy, including changing the retention period or disabling it.

Selecting Compliance mode is irreversible. After selecting this mode, you cannot change the retention period or switch back to Governance mode. Immutable storage cannot be disabled in this mode.
Supported storages and agents

Immutable storage is supported only on the cloud storage.

Immutable storage is available for Acronis-hosted and partner-hosted cloud storages that use Acronis Cyber Infrastructure version 4.7.1 or later.
All storages that can be used with Acronis Cyber Infrastructure Backup Gateway are supported. For example, Acronis Cyber Infrastructure storage, Amazon S3 and EC2 storages, and Microsoft Azure storage.
Immutable storage requires that TCP port 40440 is open for the Backup Gateway service in Acronis Cyber Infrastructure. In version 4.7.1 and later, TCP port 40440 is automatically opened with the Backup (ABGW) public traffic type. For more information about the traffic types, see Acronis Cyber Infrastructure documentation.
Immutable storage requires a protection agent version 21.12 (build 15.0.28532) or later.
Only TIBX (Version 12) backups are supported.

Enabling immutable storage

Disabling immutable storage

Accessing deleted backups in immutable storage

Viewing immutable storage usage

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.