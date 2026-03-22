# Backup format

Managing the backup and recovery of workloads and files > Backup options > Backup format
Backup format

The Backup format option defines the format of the backups created by the protection plan. This option is available only for protection plans that already use the version 11 backup format. If this is the case, you can change the backup format to version 12. After you switch the backup format to version 12, the option becomes unavailable.

Version 11

The legacy format preserved for backward compatibility.

You cannot back up Database Availability Groups (DAG) by using the backup format version 11. Backing up of DAG is supported only in the version 12 format.

Version 12

The backup format that was introduced in Acronis Backup 12 for faster backup and recovery. Each backup chain (a full or differential backup, and all incremental backups that depend on it) is saved to a single TIBX file.

Backup format and backup files

For backup locations that can be browsed with a file manager (such as local or network folders), the backup format determines the number of files and their extension. The following table lists the files that can be created per machine or mailbox.

Always incremental (single-file)	Other backup schemes


Version 11 backup format



One TIB file and one XML metadata file



Multiple TIB files and one XML metadata file




Version 12 backup format



One TIBX file per backup chain (a full or differential backup, and all incremental backups that depend on it). If the size of a file stored in a local or network (SMB) folder exceeds 200 GB, the file is split to 200-GB files by default.

Changing the backup format to version 12 (TIBX)

If you change the backup format from version 11 (TIB format) to version 12 (TIBX format):

The next backup will be full.
In backup locations that can be browsed with a file manager (such as local or network folders), a new TIBX file will be created. The new file will have the name of the original file, appended with the _v12A suffix.
Retention rules and replication will be applied only to the new backups.
The old backups will not be deleted and will remain available on the Backup storage tab. You can delete them manually.
The old cloud backups will not consume the Cloud storage quota.
The old local backups will consume the Local backup quota until you delete them manually.
In-archive deduplication

The TIBX backup format of version 12 supports in-archive deduplication that brings the following advantages:

Significantly reduced backup size, with built-in block-level deduplication for any type of data
Efficient handling of hard links ensures that there are no storage duplicates
Hash-based chunking

In-archive deduplication is enabled by default for all backups in the TIBX format. You do not have to enable it in the backup options, and you cannot disable it.

Backup format compatibility across different product versions

For information about backup format compatibility, see this knowledge base article.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.