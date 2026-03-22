# Enabling immutable storage

Additional Cyber Protection tools > Immutable storage > Enabling immutable storage
Enabling immutable storage

Since September 2024, immutable storage in Governance mode has been enabled by default, with a retention period of 14 days.

You can enable immutable storage for tenants where it is not yet enabled by using either the Cyber Protect console or the Management Portal. Both provide the same settings. The steps below use the Cyber Protect console. For more information, see Configuring immutable storage in the administrator guide.

To enable immutable storage

Log in to the Cyber Protect console as an administrator.
Go to Settings > System settings.
Scroll through the list of default backups options, and then click Immutable storage.
Turn on the Immutable storage switch.

Specify a retention period between 14 and 3650 days.

The default retention period is 14 days. A longer retention period will result in increased storage usage.

Select the immutable storage mode and, if prompted, confirm your choice.

Governance mode

In this mode, all deleted backups remain in immutable storage for the specified retention period. This prevents ransomware or malicious actors from tampering with or erasing backup data and ensures the integrity of backups, which is essential for reliable disaster recovery.

In this mode, you can change the retention period or switch to Compliance mode. Immutable storage can be disabled only by contacting the Support team.

Compliance mode

In addition to the benefits of the Governance mode, the Compliance mode helps organizations meet the regulatory requirements for data retention and security by preventing changes in the retention policy, including changing the retention period or disabling it.

Selecting Compliance mode is irreversible. After selecting this mode, you cannot change the retention period or switch back to Governance mode. Immutable storage cannot be disabled in this mode.
Click Save.

To add an existing archive to the immutable storage, create a new backup in that archive by running the corresponding protection plan manually or on a schedule.

If you delete a backup before adding the archive to the immutable storage, the backup is deleted permanently.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.