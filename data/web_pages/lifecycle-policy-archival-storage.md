# Lifecycle policy

Additional Cyber Protection tools > Archival storage > S3-compatible features > Lifecycle policy
Lifecycle policy

A lifecycle policy automatically deletes objects that you no longer need.

You can configure a lifecycle policy at the bucket level for the following types of objects:

Current versions of objects

In a versioned bucket, the current version of the object is marked as deleted after the specified period. Previous (non-current) versions remain available.

In a non-versioned bucket, the object is permanently deleted after the specified period.

Non-current versions of objects

After the specified period, these versions are permanently deleted. This option provides efficient management of the used storage space.

Lifecycle policies cannot override retention policies. If an object is protected by a retention period, it cannot be deleted until that period expires. However, you can configure a lifecycle policy with a duration longer than the retention period, ensuring that objects are automatically deleted after they are no longer protected.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.