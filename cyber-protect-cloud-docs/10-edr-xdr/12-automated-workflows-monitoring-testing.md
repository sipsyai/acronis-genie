---
title: "Automated Workflows, Monitoring Mode, and Testing EDR"
section: "Endpoint Detection and Response (EDR)"
subsection: "Automation and Testing"
page_range: "1205-1214"
tags: [edr, automated-workflows, playbooks, monitoring-mode, testing, configuration]
acronis_version: "26.02"
---

# Working with Automated Workflows

You can use Acronis automated workflows to apply a set of predefined actions that can automatically remediate incidents in Endpoint Detection and Response (EDR) and Extended Detection and Response (XDR). These workflows, or playbooks, enable you to streamline your security operations to improve time to respond, while simultaneously reducing the operational burden for managing and responding to security incidents.

There are six predefined EDR workflows, each of which can be configured as required. To access the automated workflows, go to **Management > Workflows**. The displayed list shows which workflows are currently enabled or disabled, their last execution time, and status.

## Endpoint Detection and Response (EDR) Workflows

There are six default EDR workflows:

### 1. Quarantine Threat (when EDR incident is created)

- **Trigger**: EDR incident is created
- **Conditions**: Threat status = "Not mitigated" AND Incident state = "Not started" AND Severity = "High" AND Incident type = "Process detected" OR "Malware detected"
- **Actions**: 1) Stop the process, 2) Quarantine the process, 3) Add a comment (default: "<Workflow name> - High severity threat quarantined"), 4) Close the incident

### 2. Quarantine Threat (when EDR incident is updated)

- **Trigger**: EDR incident is updated
- **Conditions**: Same as above but triggered on update

### 3. Isolate Workload (when EDR incident is created)

- **Trigger**: EDR incident is created
- **Conditions**: Threat status = "Not mitigated" AND Incident state = "Not started" AND Severity = "Critical" AND Verdict = "Malicious"
- **Actions**: 1) Stop the process, 2) Quarantine the process, 3) Isolate the workload, 4) Add a comment (default: "<Workflow name> - Workload <Workload name> has been isolated after critical malware detection"), 5) Send email to selected Cyber Protect console users

### 4. Isolate Workload (when EDR incident is updated)

- **Trigger**: EDR incident is updated
- **Conditions**: Threat status = "Not mitigated" AND Positivity Level > 9 AND Incident type = "Process detected" OR "Malware detected"
- **Actions**: Same as above (isolate workload workflow)

### 5. Malware Incident Requiring Attention

- **Trigger**: EDR incident is created
- **Conditions**: Threat status = "Not mitigated" AND Incident state = "Not started" AND Incident age > 8 hours AND Severity = "High" OR "Critical" AND Verdict = "Malicious" AND Incident type = "Malware detection"
- **Actions**: 1) Stop the process, 2) Quarantine the process, 3) Add a comment (default: "<Workflow name> - High/Critical severity threat quarantine due to no investigation for 8h"), 4) Send email to selected Cyber Protect console users

### 6. Incident Requiring Attention

- **Trigger**: EDR incident is created
- **Conditions**: Threat status = "Not mitigated" AND Incident state = "Not started" AND Incident age > 24 hours AND Severity = "High" OR "Critical" AND Verdict = "Malicious"
- **Actions**: 1) Stop the process, 2) Quarantine the process, 3) Add a comment (default: "<Workflow name> - High/Critical severity threat quarantine due to no investigation for 24h"), 4) Send email to selected Cyber Protect console users

## Configuring an Automated EDR Workflow

You can configure any of the predefined EDR workflows according to your requirements.

### Steps to Configure an EDR Workflow

1. In the Cyber Protect console, go to **Management > Workflows**.
2. In the far right column, click the ellipsis icon (...) in the row of the workflow you want to configure, and then select **Open**. Alternatively, click on the relevant workflow and in the displayed pane, click **Open**. The workflow's conditions and actions are displayed as a visual flowchart.
3. To view and modify any of the workflow's conditions, click the **Condition** block. The condition block defines a set of conditions that must be executed as part of the workflow, and consists of two block types:
   - **All**: All of the conditions in this block should be met to proceed with the next step.
   - **Any**: At least one of the conditions in this block must be met to proceed with the next step.
4. To modify a condition, click the condition and modify the relevant values. When done, click **Update**. You can also delete a condition by clicking the trash can icon next to it.
5. To modify an action, click the action you want to modify. For example, click the action **Send email**, and then modify the selected recipients, body, and subject of the email that is sent as part of this workflow.
6. In the displayed pane, make the relevant changes.
7. (Optional) Modify the additional actions.
8. Click **Save**. If the workflow was not previously enabled and is in **Draft** state, click **Save and enable** to enable it. Alternatively, click **Save** to leave the workflow **Disabled**.

You can enable and disable a workflow from the main workflow screen by clicking on the relevant workflow and selecting **Enable** or **Disable**.

# Enabling Monitoring Mode for Endpoint Detection and Response (EDR)

The monitoring mode in Cyber Protection enables you to use EDR in a production environment. In turn, this enables you to check for any false positives, and make necessary exclusions before fully deploying EDR.

In monitoring mode, nothing is blocked or stopped, and incidents are created, but no responses are initiated.

## Steps to Enable the Monitoring Mode for EDR

1. In the Cyber Protect console, go to **Management > Protection plans**.
2. Select the relevant protection plan from the displayed list, and in the right sidebar, click **Edit**.
3. In the protection plan sidebar, click the arrow icon next to the **Endpoint Detection and Response (EDR)** module to expand the module settings.
4. Enable the **Monitoring mode** toggle.
5. Click **Save**.

When monitoring mode is enabled, a banner is displayed at the top of the incident list in the Incidents page, indicating that monitoring mode is currently enabled and that the list includes incidents that have been generated while in monitoring mode.

Incidents generated while in monitoring mode are flagged with a monitoring mode label. This enables you to quickly identify which incidents were generated while in monitoring mode.

# Testing Endpoint Detection and Response (EDR)

You can test that EDR is working correctly by using the EICAR test file or the EDR simulation tool.

## Using the EICAR Test File

The EICAR test file is a standard file used to test antivirus software. It is not a real virus; it simply contains a text string that triggers antivirus software. You can use this file to test the EDR detection and incident creation process.

## Using the EDR Simulation Tool

Acronis provides an EDR simulation tool that runs a number of simulations on a workload to test that EDR is working correctly. The tool creates simulated attacks on the workload and verifies that incidents are created as expected.

The simulation tool is available for download from the Cyber Protect console. After downloading and running the tool, it generates a report that shows the results of the simulations.
