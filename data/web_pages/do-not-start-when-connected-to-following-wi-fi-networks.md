# Do not start when connected to the following Wi-Fi networks

Managing the backup and recovery of workloads and files > Backup schedule > Running a backup on a schedule > Do not start when connected to the following Wi-Fi networks
Do not start when connected to the following Wi-Fi networks

Use this start condition to prevent a backup (including a backup to a local disk) if the machine is connected to any of the specified wireless networks (for example, if you want to restrict backups through a mobile phone hotspot).

You can specify the Wi-Fi network names, also known as service set identifiers (SSID). The restriction applies to all networks that contain the specified name as a substring in their name, not case-sensitive. For example, if you specify phone as the network name, the backup will not start when the machine is connected to any of the following networks: John's iPhone, phone_wifi, or my_PHONE_wifi.

The start condition Do not start when connected to the following Wi-Fi is automatically enabled when you enable the Do not start when on metered connection condition. The following network names are specified by default: android, phone, mobile, and modem.

To remove these names from the list, click the X sign. To add a new name, type it in the empty field.

Example

You back up your data every workday at 09:00 PM. If the machine is connected to the Internet through a mobile hotspot, you want to skip the backup and wait for the scheduled start on the next workday.

Schedule: Daily, Run Monday to Friday. Start at: 09:00 PM.
Condition: Do not start when connected to the following networks, Network name: <SSID of the hotspot network>.
Backup start conditions: Skip the scheduled backup.

As a result:

If the machine is not connected to the specified network at 09:00 PM, the backup starts immediately.
If the machine is connected to the specified network at 09:00 PM, the backup starts the next workday.
If the machine is always connected to the specified network on workdays at 09:00 PM, the backup never starts.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.