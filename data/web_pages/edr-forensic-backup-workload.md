# Run an on-demand forensic backup on a workload

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Remediating incidents > Run an on-demand forensic backup on a workload
Run an on-demand forensic backup on a workload

As part of your investigation into an attack, EDR enables you to run an on-demand forensic backup for audit or further investigation purposes.

To run a forensic backup

In the cyber kill chain, click the workload node you want to run a forensic backup on.
In the displayed sidebar, click the Response Actions tab.
In the Investigate section, click Forensic backup.

[Optional] In the Backup name field, click the edit icon to edit the backup name.
In the Forensic options field, click the displayed link. In the displayed Forensic options dialog, select one of the following:
Collect raw memory dump
Collect kernel memory dump

You can also select the Snapshot of running processes check box to add information about the processes running at the moment the backup starts. This information is stored in a backup image.

Click Save to close the Forensic options dialog.

In the Where to back up field, click the displayed link to define a location for the backup.
[Optional] Click the Encryption option to enable encryption. In the displayed dialog, enter the password for the encrypted backup and select the relevant encryption algorithm.
[Optional] In the Comment field, add a comment. This comment is visible in the Activities tab (for a single node or the entire incident), and can help you (or your colleagues) recall why you took the action when you revisit the incident.
Click Run.

The forensic backup is started. This action can also be viewed in the Activities tabs of both the individual node and the entire incident. For more information, see Understand the actions taken to mitigate an incident.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.