# Object locking

Additional Cyber Protection tools > Archival storage > S3-compatible features > Object locking
Object locking

Object locking enables Write-Once Read-Many (WORM) capabilities for buckets. With it, you can configure a bucket where data can be written and read, but it cannot be deleted or overwritten.

Object locking is only available for versioned buckets.

You can configure the object locking setting only when you create a bucket, and it cannot be changed it later.

To achieve object immutability, you must add a retention policy (retention mode and retention period) to the object locking capabilities. In the Cyber Protect console, you can configure a retention policy at the bucket level, so that all objects in that bucket use the same retention mode and period.

Configuring a retention policy at the bucket level is optional. For example, you can create a bucket with object locking and without a retention policy. In this case, ensure that object immutability is configured at the object level.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.