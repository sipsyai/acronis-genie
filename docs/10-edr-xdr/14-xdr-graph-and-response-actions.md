---
title: "Working with the XDR Graph, Investigating Nodes, and Response Actions"
section: "Extended Detection and Response (XDR)"
subsection: "XDR Graph"
page_range: "1217-1223"
tags: [xdr, graph, nodes, response-actions, integration-errors, icons, investigation, microsoft-365, fortimail, entra-id]
acronis_version: "26.02"
---

# Working with the XDR Graph

The XDR graph adds another enriched perspective to viewing EDR (Endpoint Detection and Response) incidents by correlating detections with events from XDR data sources, including email and identity management metadata.

The type of nodes shown in the graph depend on the XDR integrations. For example, when integrated with email and identity management, the graph will show email nodes, email file attachment nodes, and user identity nodes. When integrated with Microsoft 365 services, the graph will show collaboration application nodes, such as Teams, OneDrive, and SharePoint.

Use the XDR graph to:
- Investigate individual nodes
- Apply response actions to a node
- View integration errors

To access the XDR graph, go to **Protection > Incidents**, click on the relevant incident, and then click the **XDR** tab. The XDR tab is only displayed if XDR is enabled. To refresh the contents of the XDR graph, click **Refresh**.

## How to Analyze the XDR Graph

XDR adds additional details to an EDR incident, such as verifying if the threat came from an email attachment, collaboration application, or a link in an email, and which user was logged in and responsible for opening the malicious attachment. By analyzing the XDR graph, you are provided with additional context of what happened in the incident and if action beyond the functionality of EDR is required, such as blocking the user account, and/or blocking the email sender.

### XDR Graph Elements for Microsoft 365 Integration

- When a malicious file is located in a Microsoft 365 application (OneDrive, SharePoint, Teams, or Outlook), a line is shown to connect the malicious file node to the relevant collaboration application node.

### XDR Graph Elements for FortiMail Workspace Security Integration

- When a malicious file is a direct attachment of an email, a line connects the malicious file node to the email node.
- When the malicious node is a URL node, a line connects the malicious URL node to the email node.
- When a malicious file was extracted from a zip archive attachment (or other type of compressed archive), a file node is created for the zip archive, and a line connects the malicious file node to the attachment node.

## Investigating Individual Nodes

You can view the details of any of the XDR graph nodes. This enables you to drill-down to specific nodes in the graph and to investigate and apply response actions to each node as required.

The nodes displayed will vary according to the XDR integrations implemented. The node details are displayed in the **Overview** tab, and the response actions available for that node are shown in the **Response actions** tab.

There are no response actions available for Indicators of Compromise (IoC) and Indicators of Attack (IoA) nodes.

### Steps to Investigate Individual Nodes

1. In the Cyber Protect console, go to **Protection > Incidents**.
2. Click the investigate icon for the incident you want to investigate.
3. Click the **XDR** tab.
4. Navigate to the relevant node, and click it to display the sidebar for the node.
5. Investigate the information included in the sidebar tabs:

#### Overview Tab

Depending on the node type:
- **Indicator of Attack (IoA) nodes**: Includes the detection timestamp, detection severity, detection description, MITRE tactic and technique, and threat name.
- **Indicator of Compromise (IoC) nodes**: Each IoC node type (process, file, or URL) has its own set of fields, which are also used in EDR.
- **Integration nodes**: Includes details on the selected node depending on the integration. For example, Teams, OneDrive, and SharePoint nodes include the file name, creation date, the user that created the file, the last user to modify the file, and the file size. The email node includes details about the sender's IP address, name, and client used, and the name, format, and size of each attachment.

#### Response Actions Tab

Lists the various response actions available, depending on the integration:
- **FortiMail Workspace Security**: Supports the blacklist sender response action.
- **Microsoft 365**: Supports the terminate user session, forced password reset, and suspend user response actions.

## Applying Response Actions

You can apply various response actions to individual XDR graph nodes.

### Steps to Apply a Response Action

1. In the Cyber Protect console, go to **Protection > Incidents**.
2. Click the investigate icon for the incident.
3. Click the **XDR** tab.
4. Navigate to the relevant node, and click it to display the sidebar. Note that if the node is a grouped identity, email, or collaboration node type (indicated by a label number on the node), the response actions applied to this node are applied to all the sub-nodes in the group node.
5. Click the **Response actions** tab.
6. Click **Execute** for the required response action. When clicking Execute, the other response actions are temporarily disabled. When the action is complete, the other response actions are enabled.
7. (Optional) Click the **Activities** tab to review all response actions applied to the node. Response actions executed for XDR incidents are displayed together with EDR incidents.

## Viewing XDR Integration Errors

If an error occurred during the integration with third party XDR solutions, the Errors dialog is displayed. This dialog displays integration errors, including failures to connect to the integration source or if the integration was configured incorrectly.

The Errors dialog is displayed automatically (if there are errors) when you access the XDR graph. To access this dialog at any other time, click **Errors** in the top right corner of the XDR graph. The **Errors** button is not displayed if there are no current XDR graph errors.

Each error includes the Source (e.g., Perception Point, Microsoft Entra), Timestamp, and Description of the error.

## XDR Graph Icons

The table below lists the various icons currently available in the XDR graph. A node can be 'grouped' to include a number of individual nodes of the same type. The icon representing the node displays a number that indicates the number of nodes within the grouped node.

| Icon | Description |
|------|-------------|
| **Process (IoC)** | Indicator of Compromise indicating a generic or injected process. Labeled with the process name (e.g., processname.exe). |
| **File (IoC)** | Indicator of Compromise indicating a generic, document, executable, or script file. Labeled with the filename (e.g., filename.dll). |
| **URL (IoC)** | Indicator of Compromise indicating a URL. Labeled with the URL (e.g., abc.com). |
| **IoA** | Indicator of Attack. Labeled with the IoA name (e.g., Minikatz). |
| **Workload** | Workload node. Labeled with the workload name (e.g., DESKTOP-D123). |
| **Identity (user)** | Identity node. Labeled with the user account ID (e.g., david.smith@b.com). This node includes information acquired locally by the agent, which does not require a connection to the Microsoft API. |
| **Email** | Email icon indicating a generic Outlook email, attachment, or URL. When integrating with FortiMail Workspace Security, the label shows the sender's email address. When integrating with Microsoft 365, "File found in Outlook" is shown. |
| **OneDrive** | Labeled with "File found in OneDrive". |
| **SharePoint** | Labeled with "File found in SharePoint". |
| **Teams** | Labeled with "File found in Teams". |
| **Microsoft Entra ID** | Labeled with the user account ID (e.g., david.smith@b.com). This node includes the UPN provided from Entra ID. Click the node to show the UPN in the AD Username field. |
