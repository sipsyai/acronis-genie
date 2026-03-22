# Safe recovery

Managing the backup and recovery of workloads and files > Recovery > Safe recovery
Safe recovery

Use safe recovery with Entire machine or Disks/volumes backups of Windows workloads to ensure that you recover only malware-free data, even if the backup contains infected files.

During a safe recovery operation, the backup is automatically scanned for malware. Then, the protection agent recovers the backup on the target workload and deletes any infected files. As a result, a malware-free backup is recovered.

Additionally, one of the following statuses is assigned to the backup:

Malware detected
No malware
Not scanned

You can use the status to filter the backup archives.

Limitations
Safe recovery is supported for physical and virtual Windows machines on which a protection agent is installed.
Safe recovery is supported for Entire machine and Disks/volumes backups.
Only NTFS volumes are scanned for malware. Non-NTFS volumes are recovered without antimalware scanning.

Safe recovery is not supported for the Continuous data protection (CDP) backup in the archive. To recover the data from the CDP backup, run an additional Files/folders recovery operation. For more operation about the CDP backups, see Continuous data protection (CDP).

See also
Antimalware scan of backups
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.