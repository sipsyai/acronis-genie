# Save battery power

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > Save battery power
Save battery power

Use this start condition to prevent a backup if a machine (for example, a laptop or a tablet) is not connected to a power source. Depending on the value of the Backup start conditions option, the skipped backup will or will not start after the machine is connected to a power source.

The following options are available:

Do not start when on battery

A backup will start only if the machine is connected to a power source.

Start when on battery if the battery level is higher than

A backup will start if the machine is connected to a power source or if the battery level is higher than a specified value.

Example

You back up your data every workday at 09:00 PM. If your machine is not connected to a power source, you want to skip the backup to save the battery power and wait until you connect the machine to a power source.

Schedule: Daily, Run Monday to Friday. Start at: 09:00 PM.
Condition: Save battery power, Do not start when on battery.
Backup start conditions: Wait until the conditions are met.

As a result:

If the machine is connected to a power source at 09:00 PM, the backup starts immediately.
If the machine is running on battery power at 09:00 PM, the backup starts when you connect the machine to a power source.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.