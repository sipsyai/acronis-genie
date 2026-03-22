# User is idle

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > User is idle
User is idle

"User is idle" means that a screen saver is running on the machine or the machine is locked.

Example

Run a backup every day at 09:00 PM, preferably when the user is idle. If the user is still active by 11:00 PM, run the backup anyway.

Schedule: Daily, Run every day. Start at: 09:00 PM.
Condition: User is idle.
Backup start conditions: Wait until the conditions are met, Start the task anyway after 2 hours.

As a result:

If the user is idle before 09:00 PM, the backup starts at 09:00 PM.
If the user becomes idle between 09:00 PM and 11:00 PM, the backup starts immediately.
If the user is still active at 11:00 PM, the backup starts at 11:00 PM.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.