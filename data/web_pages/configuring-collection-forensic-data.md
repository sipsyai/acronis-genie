# Configuring collection of forensic data

Managing the backup and recovery of workloads and files > Backup options > Forensic data > Configuring collection of forensic data
Configuring collection of forensic data

You can configure collection of forensic data by using the backup options in a protection plan.

To configure collection of forensic data

In the Cyber Protect console, go to Devices > All devices.
Select a workload, and then click Protect.
Click Add plan, and then click Create plan > Protection.
In the protection plan, ensure that the Backup module is enabled and expanded.
In What to back up, select Entire machine.

To configure collection of forensic data, In Backup options, click Change.

Click Forensic data.
Enable the Collect forensic data switch.

Click Done.

You cannot change the forensic data settings after you apply the protection plan. To use different forensic data settings, create and apply a new protection plan.

In Where to back up, specify a backup location.
In Schedule, configure the plan schedule.

To configure the encryption password, in Encryption, click Specify a password.

Type and confirm the password.
Click OK.
Click Create.

As a result, a protection plan is created and applied. During the backup, a memory dump and a snapshot of the running processes is captured. After the backup completes, you can retrieve the forensic data and analyze it.

The memory dump may contain sensitive data, such as passwords.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.