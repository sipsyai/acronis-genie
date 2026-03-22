# Investigate individual nodes in the cyber kill chain

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Investigating incidents > Investigate individual nodes in the cyber kill chain
Investigate individual nodes in the cyber kill chain

In addition to reviewing the attack stages, you can also navigate through each of the attack nodes in the cyber kill chain. This enables you to drill-down to specific nodes in the cyber kill chain and to investigate and remediate each node as required.

For example, you can determine how likely an incident is a true malicious attack. Based on your investigation, you can also apply a number of response actions to the node, including isolate a workload or quarantine a suspicious file.

To investigate individual nodes in the cyber kill chain

In the Cyber Protect console, go to Protection > Incidents.
In the displayed list of incidents, click in the far right column of the incident you want to investigate. The cyber kill chain for the selected incident is displayed.
Navigate to the relevant node, and click it to display the sidebar for the node.
Click the node to expand it and display associated nodes.

For example. clicking the powershell.exe node in the example below opens the sidebar for the node. You can also click the arrow icon next to the node to view the associated nodes, including files and registry values, that may be affected by the powershell.exe node. In turn, you can click on these associated nodes to investigate further.

Investigate the information included in the sidebar tabs:
Overview: Includes two main sections that provide a security summary of the attacked node.
Security analysis: Provides an analysis of the attacked node, including the EDR verdict on the threat (such as suspicious activity), the objective of the attack according to MITRE attack techniques (click on the link to go to the MITRE website), the reason for detection, and the number of workloads that may be affected by the attack (click the n Workloads link to view the affected workloads).
The n Workloads link means that the specific malicious or suspicious object has been found on other workloads. It does not mean that the attack is happening on these other workloads, but that there is an indicator of compromise on these other workloads. The attack may have already happened (and created another incident), or the attacker is preparing to hit these other workloads using their attack "toolkit".
Details: Includes details about the node, including its type, name and current state, path to the node, and any file hashes and digital signatures (such as MD5 and certificate serial numbers).
Scripting Activities: Includes details of any scripts invoked or loaded in the attack. Click  to copy the script to your clipboard for further investigation.
The Scripting Activities tab is only displayed for process nodes that run commands or scripts (such as cmd or PowerShell commands).
Response Actions: Includes a number of sections that provide additional investigation, remediation and prevention actions, depending on the node type.

For example, for workload nodes, you can define a number of responses that include a forensic backup and a restore from backup. Alternatively, for malicious or suspicious nodes, you can stop or quarantine the node, rollback changes made by the attack, and add it to a protection plan allowlist or blocklist.

For more information about applying response actions to specific nodes, see Response actions for individual cyber kill chain nodes.

Activities: Displays the actions applied to the incident in chronological order. For more information, see Understand the actions taken to mitigate an incident.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.