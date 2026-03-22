# Creating buckets

Additional Cyber Protection tools > Archival storage > Managing buckets in archival storage > Creating buckets
Creating buckets

You can create buckets in the Cyber Protect console.

Prerequisites

You have an access key pair. See Generating an access key pair.

To create a bucket

In the Cyber Protect console, go to Backup storage > Archival storage.
Click Add bucket.

Specify the bucket name.

The bucket name must be globally unique. It must contain between 3 and 63 characters, and can include lowercase letters (a-z from the English alphabet), digits (0–9), hyphens, and dots. It cannot start with a hyphen or a dot. If the name does not meet these requirements, the Add button on this screen is disabled.

Under Access mode, select Public or Private.

For more information, see Access mode.

You can change the access mode later, by editing the bucket properties.

Under Versioning, select Enable or Disable.

For more information, see Versioning.

If you create an unversioned bucket, you can enable versioning at any time.

If you create a versioned bucket, you cannot disable versioning, but you can suspend it. If you suspend versioning, the existing object versions remain intact. However, newly uploaded objects will not be versioned, and deleting an object will not create a new version. As a result, you will not be able to recover deleted objects by using version history.

Under Object locking, select Enable or Disable.

You cannot change this setting later.

Object locking is only available for versioned buckets. For more information, see Object locking.

Object locking is a prerequisite for a retention policy. For more information, see Configuring a retention policy.

Click Add.

As a result, an empty bucket is created. To upload and manage objects in the bucket, connect to the storage via a third-party client. For more information, see Accessing archival storage via third-party clients.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.