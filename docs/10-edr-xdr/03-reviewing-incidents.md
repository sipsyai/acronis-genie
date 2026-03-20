---
title: "Reviewing Incidents"
section: "Endpoint Detection and Response (EDR)"
subsection: "Reviewing Incidents"
page_range: "1139-1144"
tags: [edr, incidents, review, threat-status, severity, filtering, investigation, dashboard]
acronis_version: "26.02"
---

# Reviewing Incidents

Endpoint Detection and Response (EDR) provides an incident list that includes both prevention (or malware) and suspicious detections on a workload. The incident list gives a quick-glance overview of any attacks or threats affecting workloads, including threats that are yet to be mitigated.

From the incident list, you can quickly determine:

- The security posture of an organization: how many incidents need to be investigated.
- Which are the most critical incidents, and prioritize their investigation according to their severity.
- Which incidents are new or ongoing.

When logged in as a partner administrator, you can view all EDR incidents in a single screen that consolidates incidents from all customers, without the need to access each customer's individual incident view. An additional **Customers** column is displayed, which includes the customer name to which each incident belongs. The widgets shown on the **Overview** dashboard display metrics data aggregated across all customers.

The incident list is accessed from the **Protection** menu in the Cyber Protect console. If Managed Detection and Response (MDR) is enabled on workloads, an additional **MDR ticket** column is displayed showing the ticket number provided by the MDR vendor.

The Cyber Protect console must be open in order to receive incident notifications.

## What Exactly Are Incidents?

Incidents, or security incidents, can be thought of as *containers* of at least one prevention or suspicious detection point (or a mix), and include all the related events and detections of a single attack. These security incidents can also include additional benign events that give further context into what happened.

This enables viewing attack events together in one single incident and understanding the logical steps that the attacker performed. It also helps speed up the investigation time for an attack.

When EDR is enabled in the protection plan, security incidents are created when:

- **A prevention layer stops something**: These incidents are automatically closed by the system according to the protection plan settings. However, you can investigate what exactly the malware did before it was stopped. For example, ransomware is stopped when it starts to encrypt files, but prior to that it could have stolen credentials or installed a service.
- **Suspicious activity is detected by EDR**: These are detections that should be investigated and remediated. By reviewing the visually enhanced cyber kill chain, you can easily apply the relevant remediation actions.

## Prioritize Which Incidents Need Immediate Attention

The Cyber Protect console incident list can be accessed at any time from the **Protection** menu. Always analyze and prioritize the incidents that are ongoing or not mitigated.

### How to Analyze Which Security Incidents Need Immediate Attention

The incident list enables you to analyze and prioritize the listed incidents:

- **View which incidents are currently not mitigated**: Quickly understand from the incident list if any attacks are currently in progress. Any incidents that are not mitigated, as indicated in the **Threat status** column, should be looked at immediately (by default, the incident list is filtered to display these incidents).
- **Understand the scope and impact of incidents**: Based on filtering of newly opened or ongoing attacks, understand the severity for the filtered incidents as well as the impact on your business.

### Filtering the Incident List

1. At the top of the Incident list, click **Filter** to filter the displayed list of incidents. Available filters include:
   - **Threat status**: Not Mitigated (default filter)
   - **Incident type**: All or specific types
   - **Investigation state**: All, Not started, Investigating, False positive, Closed
   - **Updated**: Time range (e.g., Last month)
   - **Severity**: All, Critical, High, Medium
   - **Attack info**: All or specific attack types
   - **Positivity level**: Range from 1 to 10
2. When done, click **Apply**.

### Viewing Which Incidents Are Currently Not Mitigated

The **Threat status** column shows if the incident is **Mitigated** or **Not mitigated**. The threat status is automatically defined by EDR; any incident that is not mitigated should be investigated as soon as possible. Refine the displayed incident list further by applying filters (e.g., filter by threat status *and* severity).

The **Threat status** widget provides a quick glance overview of the current threat status. Data displayed in this widget reflects the filters applied.

### Understanding the Scope and Impact of Incidents

Quickly understand the scope and impact of incidents by reviewing the **Severity**, **Attack info**, and **Positivity level** columns:

- **Severity** column: The severity of an incident can be **Critical**, **High**, or **Medium**.
  - **Critical**: Severe risk of malicious cyber activity with the risk of compromising critical hosts in the environment.
  - **High**: High risk of malicious cyber activity with the risk of severe damage in the environment.
  - **Medium**: Increased risk of malicious cyber activity.
  - The EDR algorithm takes into consideration the workload type as well as the scope of each step of the attack. For example, an incident which includes steps related to credential theft is set to **Critical**.

- **Incident type** column: Indicates why an incident was created, including:
  - Ransomware detected
  - Malware detected
  - Suspicious process detected
  - Malicious process detected
  - Suspicious URL blocked
  - Malicious URL blocked

- **Attack info** column: Shows which attack techniques are in use and whether there is a common theme or pattern.

- **Positivity level** column: Indicates how likely an incident is a true malicious attack, with a score between 1-10 (the higher the score, the more likely the attack is truly malicious).

### Dashboard Widgets

- **Severity history**: Shows incident severity over time (Critical, High, Medium counts).
- **Detection by tactics**: Displays the various attack techniques used (Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Impact, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Resource Development), with values in green or red indicating increase or decrease over the previous specified time range.

By default, the incident list is sorted according to the **Updated** column, which details the date and time the incident was last updated with new detections. Any existing incident can be updated at any time, even if the incident was previously closed.

## Analyze Incident Details

During the incident review stage, analyze the details of each incident from the EDR incident list.

### Steps to Analyze Incident Details

1. In the Cyber Protect console, go to **Protection > Incidents**. The Incident list is displayed.
2. Click on the incident you want to review. The details for the selected incident are displayed.
3. In the **Overview** tab, review the incident and workload details, including current threat status and severity. Define the **Investigation state** (select from Investigating, Not started, False positive, or Closed), and select a user to assign the incident to via the **Assignee** drop-down list.
4. Click the **Attack Info** tab to review details of the attack and the techniques used. Click the link next to each listed attack technique to review further information on MITRE.org.
5. Click the **Activities** tab to review any action taken in the cyber kill chain to mitigate an incident.
6. Click **Investigate incident** to access the cyber kill chain where you can investigate the incident node-by-node.
