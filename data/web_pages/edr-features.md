# EDR features

Endpoint Detection and Response (EDR) > Why you need Endpoint Detection and Response (EDR) > EDR features
EDR features

Endpoint Detection and Response (EDR) includes the following features:

Receive alert notifications when a breach happens
Manage your incidents in the Incident page
Easy to understand visualization of the attack storyline
Recommendations and remediation steps
Check for publicly disclosed attacks on your workloads using threat feeds
Quick glance overview in the dashboard
Extended monitoring
Store security events for 180 days
Receive alert notifications when a breach happens

EDR provides alert notifications whenever an incident occurs. These alerts are highlighted in the main menu of the Cyber Protect console. You can then investigate an alert by clicking the Investigate incident button, which redirects you to the incident investigation screen (otherwise known as the cyber kill chain).

For more information, see Reviewing incidents.

Manage your incidents in the Incident page

EDR enables you to manage all your incidents in the Incidents page (accessed from the Protection menu in the Cyber Protect console). You can filter the information on the Incidents page according to your requirements, to quickly and easily understand the current status of the incidents, including their severity, workload affected, and positivity level. You can also navigate directly to the cyber kill chain to view the attack storyline, node-by-node.

For more information about the Incidents page, see Reviewing incidents.

Easy to understand visualization of the attack storyline

EDR provides a visual representation of an attack in an easy readable format. This ensures that even non-security personnel can digest the objectives and severity of any attack. There's really no need for a Security Operation Center (SOC) service or to hire security experts; EDR details how exactly an attack happened, including:

How the attacker got in
How the attacker hid their tracks
What harm was caused
How the attack spread

For more information, see How to investigate incidents in the cyber kill chain.

Recommendations and remediation steps

EDR provides clear and easy to implement recommendations for resolving attacks on a workload. To resolve an attack quickly, click the Remediate entire incident button to view and follow recommended steps for mitigating the incident. These recommended steps enable you to rapidly resume operations affected by an attack. However, if you want to take more granule remediation steps, you can navigate to each node and remediate it with the relevant action.

You can also click Copilot to launch the AI-assisted Copilot chat tool to enter multiple requests and receive suggested response actions for the selected incident.

For more information, see Remediating incidents.

Check for publicly disclosed attacks on your workloads using threat feeds

EDR includes the ability to review existing, known attacks in threat feeds against your workloads. These threat feeds are automatically generated based on threat data received from the Cyber Protection Operations Center (CPOC); EDR enables you to verify whether or not a threat is impacting your workload, and then take the necessary steps to nullify the threat.

For more information, see Check for indicators of compromise (IOCs) from publicly known attacks on your workloads.

Quick glance overview in the dashboard

EDR provides a range of statistics within the Cyber Protect console dashboard. You can view:

The current threat status, including the number of incidents that need to be investigated.
The evolution of attacks by severity, indicating possible attack campaigns.
The efficiency rate of closing down incidents.
The most targeted tactics used to attack your customers.
The network status of the workload, meaning whether it is isolated or connected.
Extended monitoring

On Windows and Linux machines, EDR can collect events data continuously, even when there are no particular detections.

Extended monitoring consumes additional CPU resources on the protected workload, so we recommend to verify its performance after enabling the feature. Depending on the number of collected events, it might also increase the bandwidth used for communication with the data center.
Store security events for 180 days

EDR collects workload and application events related to incidents and stores them for 180 days. Events that pre-date the 180-day period are deleted (event deletion is based on age and not according to storage space). Note that even when EDR is disabled, all previously collected events for an incident are retained, and will be available within the incident investigation screen.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.