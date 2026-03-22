# Remediate a false positive incident

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Remediating incidents > Remediate a false positive incident
Remediate a false positive incident

If you are sure an attack is not a genuine attack, in other words a false positive, you can define how to prevent the incident from happening again. For example, you can add the incident to a protection plan allowlist.

To remediate a false positive incident

In the cyber kill chain for the selected incident, click Remediate entire incident. The Remediate entire incident dialog is displayed.
In the Analyst verdict section, select False positive.

In the Prevention actions section, select the Add to allowlist check box. From the displayed protection plan list, select the relevant protection plans.

This prevention action ensures all detections of the incident will be prevented from being detected for the selected protection plans.

Select the Change investigation state of the incident to: False positive check box.
Click Remediate.

Once clicked, the button displays Go to activities. Click Go to activities to review the response actions applied to the incident. For more information, see Understand the actions taken to mitigate an incident.




Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.