# Backups of cloud servers

Implementing disaster recovery > Disaster Recovery to Cyber Protect Cloud > Cloud servers > Backups of cloud servers
Backups of cloud servers

Primary and recovery servers are backed up agentless on the cloud site. These backups have the following restrictions.

The only possible backup location is the cloud storage. Primary servers are backed up to the Primary servers backup storage.

Microsoft Azure backup locations are not supported.

A backup plan cannot be applied to multiple servers. Each server must have its own backup plan, even if all of the backup plans have the same settings.
Only one backup plan can be applied to a server.
Application-aware backup is not supported.
Encryption is not available.
Backup options are not available.

When you delete a primary server, its backups are also deleted.

A recovery server is backed up only in the failover state. Its backups continue the backup sequence of the original server. When a failback is performed, the original server can continue this backup sequence. So, the backups of the recovery server can only be deleted manually or as a result of applying the retention rules. When a recovery server is deleted, its backups are always kept.

The backup plans for cloud servers are performed according to UTC time.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.