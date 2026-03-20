---
title: "Investigating Individual Nodes and IoC Threat Feeds"
section: "Endpoint Detection and Response (EDR)"
subsection: "Investigating Nodes and IoC"
page_range: "1172-1180"
tags: [edr, investigating, nodes, cyber-kill-chain, ioc, threat-feed, indicators-of-compromise, activities]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#edr-review-attacked-nodes.html"
---

# Investigate Individual Nodes in the Cyber Kill Chain

In addition to reviewing the attack stages, you can also navigate through each of the attack nodes in the cyber kill chain. This enables you to drill-down to specific nodes and to investigate and remediate each node as required.

For example, you can determine how likely an incident is a true malicious attack. Based on your investigation, you can also apply a number of response actions to the node, including isolate a workload or quarantine a suspicious file.

## Steps to Investigate Individual Nodes

1. In the Cyber Protect console, go to **Protection > Incidents**.
2. In the displayed list of incidents, click the investigate icon in the far right column of the incident you want to investigate. The cyber kill chain is displayed.
3. Navigate to the relevant node, and click it to display the sidebar for the node. Click the node to expand it and display associated nodes. You can also click the arrow icon next to the node to view the associated nodes (files and registry values that may be affected).

## Node Sidebar Tabs

### Overview Tab

Includes two main sections that provide a security summary of the attacked node:

- **Security analysis**: Provides an analysis of the attacked node, including the EDR verdict on the threat (such as suspicious activity), the objective of the attack according to MITRE attack techniques (click the link to go to the MITRE website), the reason for detection, and the number of workloads that may be affected by the attack (click the **n Workloads** link to view the affected workloads).

  The **n Workloads** link means that the specific malicious or suspicious object has been *found* on other workloads. It does not mean that the attack is happening on these other workloads, but that there is an indicator of compromise on them. The attack may have already happened (and created another incident), or the attacker is preparing to hit these other workloads using their attack "toolkit".

- **Details**: Includes details about the node, including its type, name and current state, path to the node, and any file hashes and digital signatures (such as MD5 and certificate serial numbers).

### Scripting Activities Tab

Includes details of any scripts invoked or loaded in the attack. Click the copy icon to copy the script to your clipboard for further investigation. This tab is only displayed for process nodes that run commands or scripts (such as cmd or PowerShell commands).

### Response Actions Tab

Includes a number of sections that provide additional investigation, remediation and prevention actions, depending on the node type. For example, for workload nodes, you can define a number of responses that include a forensic backup and a restore from backup. For malicious or suspicious nodes, you can stop or quarantine the node, rollback changes made by the attack, and add it to a protection plan allowlist or blocklist.

### Activities Tab

Displays the actions applied to the incident in chronological order. Each activity shows details on who initiated the action, its status, file path, and any comments added by the initiator. If the response action was initiated as part of an automated workflow, the **Initiated by** field will show **Automated workflow**.

## Understand the Actions Taken to Mitigate an Incident

After reviewing and investigating an incident, you will typically apply response actions. These actions can be viewed to get a better understanding of what steps have been taken to mitigate the incident.

Incidents created by prevention layers automatically apply the actions configured in the protection plan. For detection points, you need to define the relevant response actions to mitigate each attack scenario.

### Viewing All Response Actions Applied to an Incident

1. In the Cyber Protect console, go to **Protection > Incidents**.
2. Click the investigate icon for the incident. The cyber kill chain is displayed.
3. Click the **Activities** tab. The list of response actions already applied to the incident is displayed.

### Completed Actions Categories

The Activities tab displays completed actions organized into categories:

**Remediated:**
- Isolated workloads
- Connected to network
- Patched
- Restarted workload
- Stopped process
- Quarantined
- Rollback changes
- Deleted

**Recovered:**
- Recovered from backup
- Disaster recovery failover

**Prevent:**
- Added to allowlist
- Added to blocklist

**Investigation:**
- Forensic backup
- Remote desktop connection

**Other:**
- Comments
- Change investigation state
- Change threat status
- Change assignee

### Actions on the Activities List

You can perform a number of actions on the displayed list:
- Click on an activity type row to display more information in a sidebar (details on who initiated the action, its status, file path, and any comments)
- Use the **Search** box to search for a specific action
- Click **Filter** to apply filters to the list
- Select the **Group by impacted entity** check box to group relevant actions according to entity
- Toggle visibility of completed actions

### Viewing Response Actions for a Specific Node

1. In the cyber kill chain, click on a node to view the sidebar for that node.
2. Click the **Activities** tab. The response actions applied for that node are shown, including who started the action, when, the duration, and its overall status.

# Check for Indicators of Compromise (IoCs) from Publicly Known Attacks

EDR includes the ability to review existing, known attacks in threat feeds against your workloads. These threat feeds are automatically generated based on threat data received from the Cyber Protection Operations Center (CPOC). EDR enables you to verify whether or not a threat is impacting your workload, and then take the necessary steps to nullify the threat.

Threat feeds are accessed from the **Monitoring** menu in the Cyber Protect console. If the protection plan does not have EDR enabled, additional threat feed functionality is not displayed.

To review specific threat details, click on a threat feed. You can view the number of IoCs detected and workloads affected, and drilldown to workloads that contain unmitigated IoCs.

## Define Threat Feed Settings

1. In the Cyber Protect console, go to **Monitoring > Threat feed**.
2. On the displayed Threat feed page, click **Settings**.
3. In the displayed dialog, select from the following options:

| Option | Description |
|--------|-------------|
| **Search for indicators of compromise (IOCs)** | Enable the automatic search for IOCs on your workloads. When enabled, the Action on detection and Generate alert options are also displayed. |
| **Action on detection** | From the dropdown list, select the action to take when a threat is discovered: No action, Quarantine, Delete, or Isolate workloads. |
| **Generate alert** | Select to generate an alert if an IOC is found on a workload. The alert will be displayed in the Alerts page. |

4. Click **Apply**.

## Review and Mitigate IOCs on Affected Workloads

When EDR is enabled in a protection plan, you can view known threats affecting workloads and mitigate any remaining IOCs that were not automatically mitigated.

1. In the Cyber Protect console, go to **Monitoring > Threat feed**.
2. Click on a thread to display the details for that threat.
3. In the **Indicators of compromise (IOCs) prevalence** section, click the **n workloads** link to view workloads with unmitigated IOCs.
4. Click on the relevant workload and review its details. You can run specific functionality on the workload, including defining additional URLs to filter and blocking malicious processes.

## Review and Analyze Discovered IOCs

You can review and analyze specific indicators of compromise (IOCs) to view individual workloads affected and mitigate the IOC.

1. In the Cyber Protect console, go to **Monitoring > Threat feed**.
2. Click on a thread to display the details for that threat.
3. In the **Indicators of compromise (IOCs) prevalence** section, click the **Total IOCs found** link. The Found indicators page is displayed with columns for File name, File hash, Threat status, Workload, and File path.
4. (Optional) Use the **Filter** option to filter IOCs by status. Use **Search** to find specific IOCs.
5. To view the workload affected by an IOC, click the link in the **Workload** column to perform actions such as run patch management or modify a protection plan.
6. (Optional) In the **File hash** column, click **Show** to display the file hashes found for a specific IOC. Click the copy icon to copy the file hash to a text editor.
