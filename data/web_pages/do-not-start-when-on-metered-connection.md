# Do not start when on metered connection

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > Do not start when on metered connection
Do not start when on metered connection

Use this start condition to prevent a backup (including a backup to a local disk) if the machine is connected to the Internet through a connection that is set as metered in Windows. For more information about metered connections in Windows, refer to https://support.microsoft.com/en-us/help/17452/windows-metered-internet-connections-faq.

The additional start condition Do not start when connected to the following Wi-Fi networks is automatically enabled when you enable the Do not start when on metered connection condition. This is an additional measure to prevent backups over mobile hotspots. The following network names are specified by default: android, phone, mobile, and modem.

To remove these names from the list, click the X sign. To add a new name, type it in the empty field.

Example

You back up your data every workday at 09:00 PM. If the machine is connected to the Internet by using a metered connection, you want to skip the backup to save the network traffic and wait for the scheduled start on the next workday.

Schedule: Daily, Run Monday to Friday. Start at: 09:00 PM.
Condition: Do not start when on metered connection.
Backup start conditions: Skip the scheduled backup.

As a result:

At 09:00 PM, if the machine is not connected to the Internet through a metered connection, the backup starts immediately.
At 09:00 PM, if the machine is connected to the Internet through a metered connection, the backup starts on the next workday.
If the machine is always connected to the Internet through a metered connection on workdays at 09:00 PM, the backup never starts.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.