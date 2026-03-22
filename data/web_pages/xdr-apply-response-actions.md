# Applying response actions

Extended Detection and Response (XDR) > Working with the XDR graph > Applying response actions
Applying response actions

You can apply various response actions to individual XDR graph nodes. These response actions enable you to quickly and easily remediate any node.

To apply a response action

In the Cyber Protect console, go to Protection > Incidents.
In the displayed list of incidents, click in the far right column of the incident you want to investigate.
Click the XDR tab.

Navigate to the relevant node, and click it to display the sidebar for the node.

Note that if the node is a grouped identity, email, or collaboration node type (indicated by a label number on the node), the response actions applied to this node are applied to all the sub-nodes in the group node.

Click the Response actions tab.

Click Execute for the required response action.

For example, the FortiMail Workspace Security supports the blacklist sender response action.

For the Microsoft 365 integration, the terminate user session, forced password reset, and suspend user response actions are available.

When clicking Execute, the other response actions are temporarily disabled. When the action is complete, the other response actions are enabled.

(Optional) Click the Activities tab to review all response actions applied to the node. Note that response actions executed for XDR incidents are displayed together with Endpoint Detection and Response (EDR) incidents. For more information, see Understand the actions taken to mitigate an incident.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.