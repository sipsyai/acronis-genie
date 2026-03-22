# Retention policy

Additional Cyber Protection tools > Archival storage > S3-compatible features > Retention policy
Retention policy

A retention policy ensures object immutability by preventing object versions from being deleted during a specified period. This feature is commonly used to meet regulatory compliance requirements, or to protect critical data from accidental or unauthorized deletion.

In the Cyber Protect console, you can configure a retention policy at the bucket level. The policy applies to all objects placed in the bucket.

You can configure a retention policy during bucket creation or later, when you edit a bucket.

Configuring a retention policy requires that object locking is enabled for the bucket.

A retention policy consists of the following elements:

Retention period
Retention mode

A retention period has a fixed duration of between 1 day to 100 years, during which an object version remains locked. When this period ends, the object version can be deleted.

The retention period applies to individual object versions. That is, different versions of the same object can have different retention durations.

For example:

You configure a 10-day retention period for a bucket, and upload object X to it. This version of object X cannot be deleted for 10 days.
On the next day, you change the retention period to 20 days, and upload object X again. The new version of object X cannot be deleted for 20 days, while the initial version remains locked for its original 10-day retention period.

Cyber Protect supports the following retention modes:

Governance mode: Object versions are protected from deletion or modification by most users. However, users with special permissions can override retention settings, if necessary. For example, you can ask the Support team for assistance with deleting an object. This mode is useful for testing retention policies before enforcing them under compliance mode.
Compliance mode: Object versions cannot be deleted or overwritten by any user, including administrators. Retention mode cannot be changed, and retention period cannot be shortened. This mode is used to enforce strict regulatory compliance.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.