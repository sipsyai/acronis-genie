# Remediate an entire incident

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Remediating incidents > Remediate an entire incident
Remediate an entire incident

By remediating an entire incident, you can quickly and easily choose the remediation(s) that you want to execute globally on the incident. Endpoint Detection and Response (EDR) guides you through the remediation process, step by step.

If you need to manage your network and the incident in more granular detail, see Response actions for individual cyber kill chain nodes.

To remediate an entire incident

In the Cyber Protect console, go to Protection > Incidents.
In the displayed list of incidents, click  in the far right column of the incident you want to investigate. The cyber kill chain for the selected incident is displayed.

Click Remediate entire incident. The Remediate entire incident dialog is displayed.

In the Analyst verdict section, based on your investigation of the incident, select one of the following:
True positive: Select if you are sure the attack is a legitimate attack. Once selected, you then add remediation and prevention actions, as described in the following steps.
False positive: Select if you are sure the attack is not a genuine attack. In this mode, you can define how to prevent this from happening again, such as by adding the incident to a protection plan allowlist.
After selecting False positive, you can only define prevention actions. For more information, see Remediate a false positive incident.
In the Remediation actions section, perform the following remediation steps. Note that they must be performed in sequential order; for example, you cannot select Step 2 before Step 1 is completed.
Step 1 - Stop threats: Select the check box to stop all processes related to the threat.
Step 2 - Quarantine threats: Once the threat is stopped, select the check box to quarantine all malicious and suspicious processes and files.
Step 3 - Rollback changes: After threats have been quarantined, select the check box to delete any new registry entries, scheduled tasks or files created by the threat (and any of its children threats). The rollback process then reverts any modifications made by the threat (or its children) to the registry, scheduled tasks and/or files existing on the workload prior to the attack. To optimize speed, the rollback process tries to recover items from the local cache. Items that fail to be recovered will be recovered by the system from backup images.
The rollback process recovers from items in the local cache only. Rollback from backup archives will be available in future releases.

Select the Allow this response action to access encrypted backups using your stored credentials check box if access to the relevant backups is encrypted. EDR accesses the stored user credentials to decrypt the encrypted archives and search for the relevant files.

You can also click Affected items to view all items (files, registry, or scheduled tasks) affected by the rollback, the actions applied (Delete, Recover, or None), and if the items are being restored from the local cache or backup images.

Recover workload: Select the check box to recover a workload if any of the above remediation steps fail, whether completely or partially.

Select one of the following recovery options:

Recover workload from backup: Enables you to recover a workload from a specific recovery point. Click the recovery point edit icon to select from a list of recovery backups.
Disaster recovery failover: Enables you to run disaster recovery, if you have this functionality enabled in your protection plan. We recommend that you use this option for critical workloads, such as AD servers, or database servers. For more information, see Implementing disaster recovery.
In the Prevention actions section, select the relevant remediation steps:
Add to blocklist: Select the checkbox and from the displayed protection plan list, select the relevant protection plans. This prevention action ensures all detections of the incident will be blocked from being executed for the selected protection plans.
Patch workload: Select the checkbox to patch any vulnerable software and prevent attackers from gaining access to the workload. You can then select the relevant action to perform once the patch is complete (Do not restart, Always restart, or Restart if required), depending if the user is logged in or not.

Select the Change investigation state of the incident to: Closed check box. If not selected, the investigation state remains in its previous state.
Click Remediate. The remediation actions you selected are executed, step by step, with the progress of each remediation step shown in the Remediate entire incident dialog.

Once clicked, the button displays Go to activities. Click Go to activities to review all response actions applied to the incident. For more information, see Understand the actions taken to mitigate an incident.

Remediate a false positive incident

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.