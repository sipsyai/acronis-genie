# How to investigate incidents in the cyber kill chain

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Investigating incidents > How to investigate incidents in the cyber kill chain
How to investigate incidents in the cyber kill chain

You can investigate each and every step of an attack in the cyber kill chain. Follow the cyber kill chain's easy to comprehend sentences and graphs to understand each step of the attack, which in turn help you to minimize investigation time.

To begin an investigation in the cyber kill chain

In the Cyber Protect console, go to Protection > Incidents.

In the displayed list of incidents, click in the far right column of the incident you want to investigate. The cyber kill chain for the selected incident is displayed.

View a summary of the incident in the threat status bar at the top of the page. The threat status bar includes the following information:
Current threat status: The threat status is automatically defined by the system. Any incident that is Not mitigated should be investigated as soon as possible.
An incident is set to Mitigated when a restore from backup has been successfully completed or when all detections have been successfully remediated by a stop process, quarantine, or rollback action.

An incident is set to Not mitigated when a restore from backup has not been successfully completed or when at least one detection has not been successfully remediated by a stop process, quarantine, or rollback action.

You can also manually set the threat status to Mitigated or Not mitigated. When selecting either status, you are prompted to enter a comment. This comment is saved as part of the investigation activities, and can be viewed in the Activities tab. Note that EDR can still revert the threat status to Mitigated or Not mitigated if new detections were discovered for the incident or response actions were run and were completed successfully.
Incident severity: Critical, High, or Medium. For more information, see Reviewing incidents.
Current investigation state: One of Investigating, Not started (the default state), False positive, or Closed. You should change the state when you start investigating the incident so that other colleagues are aware of any changes to the incident.
Positivity level: Indicates how likely an incident is a true malicious attack, between a range of 1-10. For more information, see Reviewing incidents.

Incident type: One or more of Ransomware detected, Malware detected, Suspicious process detected, Malicious process detected, Microsoft Defender detection, Suspicious URL blocked, and Malicious URL blocked.

If Microsoft Defender Antivirus is enabled for real-time protection instead of Acronis Real-time protection, only the Microsoft Defender detection, Suspicious URL blocked, and Malicious URL blocked incident types are displayed.

If Managed Detection and Response (MDR) is enabled on the workload, an MDR ticket field is displayed. You can view details of the MDR ticket created for the incident, and the MDR security analyst assigned to the incident.

When the incident was created and updated: Date and time the incident was detected, or when the incident was last updated with new detections recorded inside the incident.

Click the Legend tab to view the various nodes that make up the kill chain graph, and define which nodes to view. For further information, see Understanding and customizing the cyber kill chain view.
Investigate and remediate the incident by performing the following steps. Note that this is the typical workflow for investigating and remediating an incident, but may vary according to each incident and your own requirements.
Investigate each stage of the attack in the Attack stages tab. For further information, see Investigate the attack stages of an incident.

Click Remediate entire incident to apply remediation actions. For further information, see Remediate an entire incident. You can also remediate individual nodes in the cyber kill chain, as described in Response actions for individual cyber kill chain nodes.

Alternatively, click Copilot to launch the AI-assisted Copilot chat tool. Copilot provides response options, depending on the incident, and relevant contextual information for the incident, such as details about the attack type. You can select the relevant response option, and then follow the onscreen instructions. These response options are described in Response actions for individual cyber kill chain nodes.

There is a monthly limit of 1000 requests per partner tenant when using Copilot. When this limit is reached, an error message is displayed, informing you that you have exceeded the monthly limit.
Review the actions that were taken to mitigate the incident in the Activities tab. For more information, see Understand the actions taken to mitigate an incident.
Understanding and customizing the cyber kill chain view

To understand the nodes impacted in the cyber kill chain, access the legend. The legend displays all of the nodes involved in an incident, enabling you to understand how the various nodes have been impacted by the attacker. You can also define the nodes you want to hide or display in the cyber kill chain.

To access the legend

Click the arrow icon to the right of the Legend section.

The Legend section expands, as shown below.

There are four main colors used in the legend, which enable you to quickly understand what happened to each node in the cyber kill chain, as shown below. These color-coded nodes are also included in the attack stages, as described in Investigate the attack stages of an incident.

To hide or display nodes in the cyber kill chain

In the expanded Legend section, ensure is displayed next to the nodes you want to display in the cyber kill chain. If the displayed icon is , click the icon to change it to.
To hide a node in the cyber kill chain, click . The icon changes to and the node is not displayed in the cyber kill chain.

Investigate the attack stages of an incident

What information is included in an attack stage?

Investigate individual nodes in the cyber kill chain

Understand the actions taken to mitigate an incident

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.