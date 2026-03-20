---
title: "Remediating Incidents"
section: "Endpoint Detection and Response (EDR)"
subsection: "Remediating Incidents"
page_range: "1180-1191"
tags: [edr, remediation, response-actions, network-isolation, patch, kill-chain, allowlist, blocklist, rollback, quarantine]
acronis_version: "26.02"
doc_url: "https://www.acronis.com/en/support/documentation/CyberProtectionService/#edr-remediate-incidents.html"
---

# Remediating Incidents

Endpoint Detection and Response (EDR) enables you to remediate entire incidents, or the individual attack points of an incident. By remediating an entire incident, you can choose the remediation(s) that you want to execute globally on the incident. If you need to manage the incident in more granular detail, you can remediate individual attack points as required.

EDR ensures effective remediation by:
- **Mitigating** - to ensure the threat is stopped
- **Recovering** - to ensure services are back online immediately
- **Preventing** - to ensure techniques used in an attack are prevented in future attacks

Even though the workload is isolated, all Acronis Cyber Protect technologies are still functional and an investigation can be launched.

## Remediate an Entire Incident

By remediating an entire incident, you can quickly and easily choose the remediation(s) that you want to execute globally on the incident. EDR guides you through the remediation process, step by step.

### Steps to Remediate an Entire Incident

1. In the Cyber Protect console, go to **Protection > Incidents**.
2. Click the investigate icon for the incident. The cyber kill chain is displayed.
3. Click **Remediate entire incident**. The Remediate entire incident dialog is displayed.
4. In the **Analyst verdict** section, select one of the following:
   - **True positive**: Select if you are sure the attack is a legitimate attack. You then add remediation and prevention actions.
   - **False positive**: Select if you are sure the attack is not a genuine attack. In this mode, you can define how to prevent the incident from happening again (e.g., adding the incident to a protection plan allowlist). After selecting False positive, you can only define prevention actions.

### Remediation Actions (for True Positive)

The following remediation steps must be performed in sequential order:

1. **Step 1 - Stop threats**: Select to stop all processes related to the threat.
2. **Step 2 - Quarantine threats**: Once the threat is stopped, select to quarantine all malicious and suspicious processes and files.
3. **Step 3 - Rollback changes**: After threats have been quarantined, select to delete any new registry entries, scheduled tasks or files created by the threat (and any of its children threats). The rollback process then reverts any modifications made by the threat (or its children) to the registry, scheduled tasks and/or files existing on the workload prior to the attack.

   To optimize speed, the rollback process tries to recover items from the local cache. Items that fail to be recovered will be recovered by the system from backup images. The rollback process recovers from items in the local cache only (rollback from backup archives will be available in future releases).

   Select **Allow this response action to access encrypted backups using your stored credentials** if access to the relevant backups is encrypted.

   Click **Affected items** to view all items (files, registry, or scheduled tasks) affected by the rollback, the actions applied (Delete, Recover, or None), and if the items are being restored from the local cache or backup images.

4. **Recover workload**: Select to recover a workload if any of the above remediation steps fail (completely or partially). Choose from:
   - **Recover workload from backup**: Recover from a specific recovery point. Click the recovery point edit icon to select from a list of recovery backups.
   - **Disaster recovery failover**: Run disaster recovery if this functionality is enabled in your protection plan. Recommended for critical workloads such as AD servers or database servers.

### Prevention Actions

- **Add to blocklist**: Select and choose the relevant protection plan list. This action ensures all detections of the incident will be blocked from being executed for the selected protection plans.
- **Patch workload**: Select to patch any vulnerable software and prevent attackers from gaining access to the workload. Choose the relevant action to perform once the patch is complete: **Do not restart**, **Always restart**, or **Restart if required**, depending on whether the user is logged in or not.

5. Select the **Change investigation state of the incident to: Closed** check box (if not selected, the investigation state remains in its previous state).
6. Add a **Comment** with details about the remediation.
7. Click **Remediate**. The remediation actions are executed step by step. Once clicked, the button displays **Go to activities** to review all response actions.

## Remediate a False Positive Incident

If you are sure an attack is not a genuine attack (a false positive), you can define how to prevent the incident from happening again.

1. In the cyber kill chain, click **Remediate entire incident**.
2. In the **Analyst verdict** section, select **False positive**.
3. In the **Prevention actions** section, select the **Add to allowlist** check box. From the displayed protection plan list, select the relevant protection plans. This action ensures all detections of the incident will be prevented from being detected for the selected protection plans.
4. Select the **Change investigation state of the incident to: False positive** check box.
5. Click **Remediate**.

## Response Actions for Individual Cyber Kill Chain Nodes

If you need to manage the incident in more granular detail, you can apply various response actions to individual cyber kill chain nodes. Response actions are divided into the following categories:

- **Remediate**: Apply an immediate response to the attack, including managing network isolation for a workload, and the deletion and quarantining of files, processes, and registry values.
- **Investigate**: Run a forensic backup, remote desktop connection, or remote command line or Terminal for a more in-depth investigation (applicable to workloads only).
- **Recovery**: Respond to intensive attacks by running a recovery from backup, or Disaster Recovery failover (applicable to workloads only).
- **Prevent**: Prevent future threats or false positives by adding them to a protection plan allowlist or blocklist.

If an incident is closed, you cannot apply a response action to a node. However, you can reopen a closed incident by changing its investigation state to **Investigating**, and then apply response actions.

### Response Actions by Node Type

| Node | Category | Response Actions |
|------|----------|-----------------|
| **Workload** | Remediate | Manage network isolation, Restart workload |
| | Investigate | Forensic backup, Remote desktop connection, Run remote command line (Windows), Run Terminal (macOS) |
| | Recovery | Recovery from backup, Disaster Recovery failover |
| | Prevent | Patch |
| **Process** | Remediate | Stop process, Quarantine |
| | Prevent | Add to allowlist, Add to blocklist |
| **File** | Remediate | Delete, Quarantine |
| | Prevent | Add to allowlist, Add to blocklist |
| **Registry** | Remediate | Delete |
| **Network** | Prevent | Add to allowlist, Add to blocklist |

## Manage the Network Isolation of a Workload

EDR enables you to manage the network isolation of a workload to stop lateral movement or Command and Control (C&C) activities. All Acronis Cyber Protect technologies are functional even if a workload is isolated, ensuring that an investigation can be fully carried out.

### Isolating a Workload from the Network

1. In the cyber kill chain, click the workload node you want to remediate.
2. In the displayed sidebar, click the **Response Actions** tab.
3. In the **Remediate** section, click **Manage network isolation**.
4. In the **Immediate action after isolation** drop-down list, select from:
   - **Isolate only**
   - **Isolate and backup workload**
   - **Isolate and backup workload with forensic data**
   - **Isolate and power off workload**
5. (Optional) Add a **Message to display** to end users accessing the isolated workload.
6. (Optional) Add a **Comment** visible in the Activities tab.
7. Click **Manage network exclusions** to add ports, URLs, host names, and IP addresses that will have access to the workload during the isolation.
8. Click **Isolate**.

The workload is also shown as **Isolated** under the **Workloads** menu. You can also isolate single or multiple workloads from the **Workloads > Workloads with agents** menu.

### Connecting an Isolated Workload Back to the Network

1. In the cyber kill chain, click the workload node you want to reconnect.
2. Click the **Response Actions** tab.
3. In the **Remediate** section, click **Manage network isolation**.
4. Select from:
   - **Connect to network immediately**: Reconnect the workload directly.
   - **Recover workload from backup before connecting to network**: Select a recovery point, then choose **Recover > Entire workload** or **Recover > Files/folders**.
5. (Optional) Select **Automatically restart the workload if required**.
6. (Optional) Add a **Message to display** and **Comment**.
7. Click **Connect** or **Recover and connect**.

### Managing Network Exclusions

Even when a workload is isolated, you may need additional network connections. Add exclusions for Ports, URL addresses, and Hostname/IP addresses with specific traffic direction (Incoming and outgoing, Incoming only, or Outgoing only).

## Patch a Workload

EDR automatically detects if a workload requires a patch and enables you to patch the workload to prevent vulnerability exploitations. This feature is available only if the partner's workload has a subscription for RMM.

### Steps to Patch a Workload

1. In the cyber kill chain, click the workload node you want to patch.
2. Click the **Response Actions** tab.
3. In the **Remediate** section, click **Patch**.
4. In the **Patches to install** field, click **Select** and choose the relevant patches.
5. In the **Restart options** field, configure restart behavior.
6. Select whether the workload should be restarted after patches are installed.
7. (Optional) Add a **Comment**.
8. Click **Patch**.
