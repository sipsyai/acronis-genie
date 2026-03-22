# Fits the time interval

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > Fits the time interval
Fits the time interval

Use this start condition to restrict a backup start to a specified interval.

Example

A company backs up user data and servers to different locations on the same network-attached storage.

The workday starts at 08:00 AM and ends at 05:00 PM. User data should be backed up as soon as the users log off, but not earlier than 04:30 PM.

The company's servers are backed up every day at 11:00 PM. User data should preferably be backed up before 11:00 PM, in order to free network bandwidth for the server backups.

Backing up user data takes no more than one hour, so the latest backup start time is 10:00 PM. If a user is still logged in within the specified time interval, or logs off at any other time, the backup of the user data should be skipped.

Event: When a user logs off the system. Specify the user account: Any user.
Condition: Fits the time interval from 04:30 PM to 10:00 PM.
Backup start conditions: Skip the scheduled backup.

As a result:

If the user logs off between 04:30 PM and 10:00 PM, the backup starts immediately.
If the user logs off at any other time, the backup is skipped.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.