# The backup location\u0027s host is available

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > The backup location's host is available
The backup location's host is available

"The backup location's host is available" means that the machine that hosts the backup location is available over the network.

This condition is applicable to network folders, the cloud storage, and locations managed by a storage node.

This condition does not cover the availability of the location itself—only the host availability. For example, if the host is available, but the network folder on this host is not shared or the credentials for the folder are no longer valid, the condition is still considered met.

Example

You run backups to a network folder every workday at 09:00 PM. If the machine that hosts the folder is not available at that moment (for example, due to maintenance), you want to skip the backup and wait for the scheduled start on the next workday.

Schedule: Daily, Run Monday to Friday. Start at: 09:00 PM.
Condition: The backup location's host is available.
Backup start conditions: Skip the scheduled backup.

As a result:

If the host is available at 09:00 PM, the backup starts immediately.
If the host is not available at 09:00 PM, the backup starts the next workday (if the host is available at 09:00 PM on this day).
If the host is never available on workdays at 09:00 PM, the backup never starts.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.