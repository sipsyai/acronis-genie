# Disabling immutable storage

Additional Cyber Protection tools > Immutable storage > Disabling immutable storage
Disabling immutable storage

We strongly advise against disabling immutable storage:

Immutable storage is the last line of defense against accidental or malicious deletion of backups.
Ransomware protection alone is not enough—immutability ensures recoverability even if credentials are compromised.
Cost impact is predictable and limited, while the risk of data loss without immutability is high and unpredictable.
Industry best practice and insurance requirements increasingly mandate immutable backups.
Disabling immutability exposes your organization to SLA breaches, compliance risks, and reputational damage.
Immutable storage can be disabled only in Governance mode and only by the Support team.

After immutable storage is disabled, any backups you delete will be permanently removed. Backups already stored in immutable storage will remain available for up to 14 days (336 hours), or until their retention period ends, whichever comes first.

For example:

There are two deleted backups in immutable storage:

Backup A with a retention period of 7 days.
Backup B with a retention period of 1 year.

Immutable storage is disabled.

If you delete a backup now, it is permanently deleted.
On day 7, Backup A is permanently deleted (according to its original retention period).
On day 14, Backup B is permanently deleted (according to the immutable storage grace period, because the original retention period exceeds 14 days).

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.