# Versioning

Additional Cyber Protection tools > Archival storage > S3-compatible features > Versioning
Versioning

You can enable versioning at the bucket level:

In a versioned bucket, multiple versions of an object can exist. A new version is created when an object is uploaded, overwritten, or deleted. For example, when an object is deleted, it is not physically removed from the storage. Instead, a delete marker is added to the current object version, and the previous version remains accessible.

In an unversioned bucket, each object has only one version at a time. Overwrites and deletions are permanent.

Versioning prevents accidental or malicious deletion, or overwriting of objects, but it results in increased storage space. To trim a versioned bucket, you can use a lifecycle policy.

Versioning is automatically enabled when you enable object locking.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.