# Users logged off

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > Users logged off
Users logged off

Use this start condition to postpone a backup until all users log off from a Windows machine.

Example

You run a backup every Friday at 08:00 PM, preferably when all users are logged off. If one of the users is still logged in at 11:00 PM, run the backup anyway.

Schedule: Weekly, on Fridays. Start at: 08:00 PM.
Condition: Users logged off.
Backup start conditions: Wait until the conditions are met, Start the backup anyway after 3 hours.

As a result:

If all users are logged off at 08:00 PM, the backup starts at 08:00 PM.
If the last user logs off between 08:00 PM and 11:00 PM, the backup starts immediately.
If there are still logged-in users at 11:00 PM, the backup starts at 11:00 PM.



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.