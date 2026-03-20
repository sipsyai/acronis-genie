---
title: "EDR Overview and Features"
section: "Endpoint Detection and Response (EDR)"
subsection: "Overview"
page_range: "1132-1135"
tags: [edr, overview, features, advanced-security, xdr, cyber-protection]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#edr-features.html"
---

# Endpoint Detection and Response (EDR)

EDR is part of the Advanced Security + XDR protection pack within the Acronis Cyber Protection service. Adding EDR functionality to a protection plan may be subject to additional charges.

EDR detects suspicious activity on workloads, including attacks that have gone unnoticed. It generates incidents that provide a step-by-step overview of each attack, helping administrators understand how an attack happened and how to prevent it from happening again. With easy-to-understand interpretations of each stage in the attack, the time spent on investigating attacks can be reduced to a matter of minutes.

From version C24.05, EDR functionality can be extended with Extended Detection and Response (XDR). The XDR graph provides an additional, enriched perspective of EDR incidents by correlating detections with events from XDR data sources, which includes email and identity management metadata.

## Why You Need EDR

In today's cyber threat landscape, prevention alone no longer guarantees 100% protection. Some attacks will always make it through prevention layers and successfully penetrate the network. Conventional solutions cannot detect when this happens, leaving attackers free to dwell in environments for days, weeks, or months.

Existing EDR solutions help prevent these "silent failures" by finding and removing attackers quickly. However, they typically require a high level of security expertise or expensive Security Operation Center (SOC) analysts, and analysis of incidents can be extremely time-consuming.

The Acronis Advanced Security + EDR functionality overcomes these limitations by detecting attacks that have gone unnoticed, and helping administrators understand how an attack happened and how to prevent it from happening again. This reduces the time spent on investigating attacks.

### Key Benefits

- **Full visibility**: Understand what happened and how it happened, even for attacks that have gone unnoticed. The evolution of each attack is visually mapped out, step-by-step (from the initial point of entry to viewing the data that was targeted and/or exfiltrated), enabling quick understanding of the scope and impact of an incident.
- **Minimize investigation time**: Reduce incident investigation time from hours to just a matter of minutes. EDR details each step of the attack in clear, easy-to-understand human language, reducing the need for expensive experts or additional headcount.
- **Check for known threats on workloads**: Automatically search workloads for threats from malware, vulnerabilities, and other types of global events that may affect data protection. These threats are referred to as Indicators of Compromise (IoCs), and are based on threat data received from the Cyber Protection Operations Center (CPOC).
- **Respond faster to incidents**: With access to all post-breach activities and a breakdown of each step of the kill chain, perform a number of actions to remediate each attack point. Investigate using remote control and forensic backup, quarantine workloads, and kill malware processes. Recover business operations using Disaster Recovery.
- **Report on security posture with confidence**: With EDR enabled, eliminate much of the insecurity and fear of the impact cyber attacks can have on business. Incident-related information is stored for 180 days and can be used for auditing purposes.

## EDR Features

Endpoint Detection and Response (EDR) includes the following features:

- **Alert notifications when a breach happens**: EDR provides alert notifications whenever an incident occurs. These alerts are highlighted in the main menu of the Cyber Protect console. Click the **Investigate incident** button to be redirected to the incident investigation screen (the cyber kill chain).
- **Manage incidents in the Incident page**: Manage all incidents in the Incidents page (accessed from the **Protection** menu). Filter incidents by severity, workload affected, positivity level, and navigate directly to the cyber kill chain to view the attack storyline node-by-node.
- **Easy to understand visualization of the attack storyline**: EDR provides a visual representation of an attack in an easy readable format, ensuring even non-security personnel can digest the objectives and severity of any attack. EDR details how exactly an attack happened, including how the attacker got in, how they hid their tracks, what harm was caused, and how the attack spread.
- **Recommendations and remediation steps**: EDR provides clear recommendations for resolving attacks. Click the **Remediate entire incident** button to view and follow recommended steps. You can also click **Copilot** to launch the AI-assisted Copilot chat tool for suggested response actions.
- **Check for publicly disclosed attacks using threat feeds**: Review existing, known attacks in threat feeds against workloads. These are automatically generated based on threat data from the Cyber Protection Operations Center (CPOC).
- **Quick glance overview in the dashboard**: View statistics including current threat status, evolution of attacks by severity, efficiency rate of closing incidents, most targeted tactics, and network status of workloads.
- **Extended monitoring**: On Windows and Linux machines, EDR can collect events data continuously, even when there are no particular detections. Extended monitoring consumes additional CPU resources on the protected workload. Verify performance after enabling this feature as it might also increase bandwidth used for communication with the data center.
- **Store security events for 180 days**: EDR collects workload and application events related to incidents and stores them for 180 days. Events that pre-date the 180-day period are deleted based on age and not storage space. Even when EDR is disabled, all previously collected events for an incident are retained and available within the incident investigation screen.
