# Investigating individual nodes

Extended Detection and Response (XDR) > Working with the XDR graph > Investigating individual nodes
Investigating individual nodes

You can view the details of any of the XDR graph nodes. This enables you to drill-down to specific nodes in the graph and to investigate and apply response actions to each node as required.

The nodes displayed will vary according to the XDR integrations implemented. The node details are displayed in the Overview tab, and the response actions available for that node are shown in the Response actions tab.

There are no response actions available for Indicators of Compromise (IoC) and Indicators of Attack (IoA) nodes.

To investigate individual nodes

In the Cyber Protect console, go to Protection > Incidents.
In the displayed list of incidents, click in the far right column of the incident you want to investigate.
Click the XDR tab.

Navigate to the relevant node, and click it to display the sidebar for the node.

For example, clicking the email node in the example below opens the sidebar for the node.

Investigate the information included in the sidebar tabs:
Overview: This tab includes details about the selected node, depending on the node type.

Indicator of Attack (IoA) nodes: Includes the detection timestamp, detection severity, detection description, MITRE tactic and technique, and threat name.

Indicator of Compromise (IoC) nodes: Each IoC node type (process, file, or URL) has its own set of fields, which are also used in Endpoint Detection and Response (EDR). For more information, see Investigate individual nodes in the cyber kill chain.

Integration nodes: Includes details on the selected node, depending on the integration.

For example, the Teams, OneDrive, and SharePoint nodes include the file name, its creation date, the user that created the file, the last user to modify the file, and the file size.

Similarly, the email node includes details about the senders IP address, name, and client used, and the name, format, and size of each attachment.

Response actions: This tab lists the various response actions available, depending on the integration. For example, the email node will display options to block the sender's email as malicious, and delete attachments. For more information, see Applying response actions.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.