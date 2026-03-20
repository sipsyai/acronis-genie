---
title: "Investigating Incidents"
section: "Endpoint Detection and Response (EDR)"
subsection: "Investigating Incidents"
page_range: "1164-1171"
tags: [edr, investigating, cyber-kill-chain, attack-stages, mitre, copilot, nodes, legend]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#edr-investigate-incident.html"
---

# Investigating Incidents

Endpoint Detection and Response (EDR) enables you to investigate an entire incident, including all of the attack stages and objects (processes, registries, scheduled tasks, and domains) impacted by an attack. These objects are represented by nodes in the easy-to-understand cyber kill chain.

Each and every step of an attack is viewed in the cyber kill chain, which provides a detailed interpretation of how and why the incident happened. The cyber kill chain uses easy to understand sentences and graphs that help explain each step of the attack, in turn helping to minimize investigation time.

You can quickly understand the scope and impact of an incident, with the attack evolution mapped to the MITRE framework. This enables you to analyze what happened in each step of an attack, including:

- The initial point of entry
- How the attack was executed
- Any escalations of privileges
- Avoidance detection techniques
- Lateral movements to other workloads
- Credential theft
- Exfiltration attempts

You can also click **Copilot** to launch the Copilot chat tool, which enables you to enter multiple requests and receive suggested response actions for the selected incident.

Each object impacted in the attack, whether it is a process, registry, scheduled task or domain, is represented by a node in the cyber kill chain.

## How to Investigate Incidents in the Cyber Kill Chain

### Steps to Begin an Investigation

1. In the Cyber Protect console, go to **Protection > Incidents**.
2. In the displayed list of incidents, click the investigate icon in the far right column of the incident you want to investigate. The cyber kill chain for the selected incident is displayed.
3. View a summary of the incident in the threat status bar at the top of the page. The threat status bar includes:
   - **Current threat status**: Automatically defined by the system. Any incident that is **Not mitigated** should be investigated as soon as possible.
   - **Incident severity**: Critical, High, or Medium.
   - **Current investigation state**: One of Investigating, Not started (default), False positive, or Closed.
   - **Positivity level**: Indicates how likely an incident is a true malicious attack (range of 1-10).
   - **Incident type**: One or more of Ransomware detected, Malware detected, Suspicious process detected, Malicious process detected, Microsoft Defender detection, Suspicious URL blocked, and Malicious URL blocked.
   - **MDR ticket**: If MDR is enabled on the workload, displays ticket details (Ticket ID, User assigned, Status, Priority, Last updated).
   - **Created and Updated timestamps**: Date and time the incident was detected and last updated.

### Threat Status Details

An incident is set to **Mitigated** when a restore from backup has been successfully completed or when all detections have been successfully remediated by a stop process, quarantine, or rollback action.

An incident is set to **Not mitigated** when a restore from backup has not been successfully completed or when at least one detection has not been successfully remediated by a stop process, quarantine, or rollback action.

You can also manually set the threat status to Mitigated or Not mitigated. When selecting either status, you are prompted to enter a comment. This comment is saved as part of the investigation activities and can be viewed in the Activities tab. EDR can still revert the threat status if new detections were discovered for the incident or response actions were run and completed successfully.

If Microsoft Defender Antivirus is enabled for real-time protection instead of Acronis Real-time protection, only the Microsoft Defender detection, Suspicious URL blocked, and Malicious URL blocked incident types are displayed.

4. Click the **Legend** tab to view the various nodes that make up the kill chain graph, and define which nodes to view.
5. Investigate and remediate the incident:
   a. Investigate each stage of the attack in the **Attack stages** tab.
   b. Click **Remediate entire incident** to apply remediation actions. You can also remediate individual nodes in the cyber kill chain. Alternatively, click **Copilot** to launch the AI-assisted Copilot chat tool for response options and contextual information about the attack type.

### Copilot

Copilot is an AI-assisted chat tool that can:
- Provide a summarized description of the incident
- Recommend response actions for the incident
- Provide a list of recent incidents on the workload
- Search for incidents on other workloads similar to the current incident

There is a monthly limit of 1000 requests per partner tenant when using Copilot.

## Understanding and Customizing the Cyber Kill Chain View

To understand the nodes impacted in the cyber kill chain, access the legend. The legend displays all of the nodes involved in an incident, enabling you to understand how the various nodes have been impacted by the attacker. You can also define the nodes you want to hide or display.

### Legend Node Types

| Node Type | Description |
|-----------|-------------|
| Workload | The workload affected |
| Process | Processes involved in the attack |
| File | Files impacted |
| Network | Network connections |
| Registry | Registry entries modified |
| Involved | Nodes involved but not necessarily malicious |
| Malicious threat | Confirmed malicious nodes |
| Incident trigger | The node that triggered the incident |

### Node Color Coding

There are four main colors used in the legend to quickly understand what happened to each node:

- **Grey (Involved)**: The node is involved but not necessarily malicious
- **Yellow (Suspicious activity)**: The node shows suspicious behavior
- **Red (Malicious threat)**: The node is confirmed as malicious
- **Star (Incident trigger)**: The node that triggered the incident creation

### Hiding or Displaying Nodes

1. In the expanded Legend section, ensure the visibility icon is enabled for nodes you want to display.
2. To hide a node in the cyber kill chain, click the visibility icon to toggle it off.

## Investigate the Attack Stages of an Incident

The attack stages provide easy to understand interpretations of every incident. Each attack stage summarizes what exactly happened, and what were the objects (referred to as *nodes* in the cyber kill chain) targeted.

Each stage of the attack provides the information to resolve three crucial questions:

- What was the attacker's objective?
- How did the attacker achieve this objective?
- Which nodes were targeted?

The interpretation provided ensures the time spent on investigating an incident is greatly reduced, as you no longer need to go through each security event from a timeline or graph node and then try to create an interpretation of the attack.

The attack stages also include information about compromised files that contain sensitive information, such as credit card numbers and social security numbers (shown in the **Collection** stage).

### How to Navigate Attack Stages

Attack stages are listed in chronological order. Scroll down to see the complete list. To investigate a specific attack stage further, click anywhere in the attack stage to navigate to the relevant node in the cyber kill chain graph.

### Attack Stage Elements

| Element | Description |
|---------|-------------|
| **Header** | Describes what the attacker tried to do, and their objective (e.g., Credential Access), with a link to a known MITRE ATT&CK technique. If an attack stage is not a known MITRE ATT&CK technique, the header text will not be linked. |
| **Timestamp** | The time the attack stage occurred. |
| **Technique** | How the attacker technically achieved their objective, and what objects (registry entries, files, or scheduled tasks) were affected. Included in the text description of the attack. |

### Example Attack Stages

A typical attack may include the following stages in chronological order:

1. **Execution**: User executes a suspicious file on the workload
2. **Defense Evasion**: A file was masquerading as a benign document type
3. **Command And Control**: A TCP connection is established on an unusual port to an unknown domain
4. **Collection**: The adversary collects files containing sensitive information and compresses them into an archive
5. **Exfiltration**: The adversary tries to steal data by exfiltrating the archive via an existing TCP connection
