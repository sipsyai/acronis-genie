# Check device IP address

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > Check device IP address
Check device IP address

Use this start condition to prevent a backup (including a backup to a local disk) if any of the machine IP addresses are within or outside of the specified IP address range. Thus, for example, you can avoid large data transit charges when backing up machines of users who are overseas, or you can prevent backups over a Virtual Private Network (VPN) connection.

The following options are available:

Start if outside IP range
Start if within IP range

With either option, you can specify several ranges. Only IPv4 addresses are supported.

Example

You back up your data every workday at 09:00 PM. If the machine is connected to the corporate network by using a VPN tunnel, you want to skip the backup.

Schedule: Daily, Run Monday to Friday. Start at 09:00 PM.
Condition: Check device IP address, Start if outside IP range, From: <beginning of the VPN IP address range>, To: <end of the VPN IP address range>.
Backup start conditions: Wait until the conditions are met.

As a result:

If the machine IP address is not in the specified range at 09:00 PM, the backup starts immediately.
If the machine IP address is in the specified range at 09:00 PM, the backup starts when the machine obtains a non-VPN IP address.
If the machine IP address is always in the specified range on workdays at 09:00 PM, the backup never starts.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.