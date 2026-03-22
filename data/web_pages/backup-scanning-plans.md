# Backup scanning plans

Working with plans > Backup scanning plans
Backup scanning plans

To scan backups for malware (including ransomware), create a backup scanning plan.

Backup scanning plans are not supported for all workloads and backup storages. For more details, see Limitations.

To create a backup scanning plan

In the Cyber Protect console, go to Management > Backup scanning.
In the Actions pane, click Create plan.

Change the default plan name.

In Backups to scan, click Specify.

[Optional] To add a new location, click Add, select the location, and then click Done.
Click Locations or Backups to select the scope for the plan.

Select entire location or individual archives in a location.

You can select one or more items.

Click Done.

[If the selected archives are encrypted] In Encryption, enable the toggle, and then enter the encryption password.

The password you specified will be used for the scanning of all backups in the plan, so all selected archives must use the same encryption password. For archives that use different encryption passwords, create separate plans.

Click Create.

As a result, a backup scanning plan is created. The cloud agent will automatically scan the selected archives once an hour. You cannot change the plan schedule or the period between two consecutive scans.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.