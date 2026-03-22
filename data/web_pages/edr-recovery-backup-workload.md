# Recovery from backup

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Remediating incidents > Recovery from backup
Recovery from backup

As part of your recovery response to an attack, EDR enables you to recover your entire machine from backup or specific files or folders.

To recover your workload from backup

In the cyber kill chain, click the workload node you want to recover.
In the displayed sidebar, click the Response Actions tab.
In the Recovery section, click Recover from backup.

In the Recovery point field, click Select and then perform the following steps:
In the displayed sidebar, select the relevant recovery point.
Click Recover > Entire workload to recover all the files and folders on the workload.

Or

Click Recover > Files/folders to recover specific files and folders on the workload. You are then prompted to select the relevant files or folders. Once selected, you can view the items selected for recovery by clicking the relevant value in the Items to be recovered field.

If the recovery point you select is encrypted, you will be prompted for the password.
[Optional] Select the Automatically restart the workload check box. This option is relevant only if you selected Recover > Entire workload in Step 4.
[Optional] In the Comment field, add a comment. This comment is visible in the Activities tab (for a single node or the entire incident), and can help you (or your colleagues) recall why you took the action when you revisit the incident.
Click Start recovery.

The process to recover the workload starts. The progress for this action can be viewed in the Activities tabs of both the individual node and the entire incident. For more information, see Understand the actions taken to mitigate an incident.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.