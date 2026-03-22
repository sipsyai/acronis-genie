# Understand the actions taken to mitigate an incident

Endpoint Detection and Response (EDR) > How to use Endpoint Detection and Response (EDR) > Investigating incidents > Understand the actions taken to mitigate an incident
Understand the actions taken to mitigate an incident

After you have reviewed an incident and investigated how the attack occurred, you will typically apply response actions. Once you have applied response actions, these actions can be viewed in a number of places to get a better understanding of what steps have been taken to mitigate the incident.

Incidents created by prevention layers automatically apply the actions configured in the protection plan. For detection points, you need to define the relevant response actions to mitigate each attack scenario.

To understand the response actions taken, you can view all the response actions applied to an entire incident, or view the actions applied to a specific node in the incident cyber kill chain.

To view all response actions applied to an incident

In the Cyber Protect console, go to Protection > Incidents.
In the displayed list of incidents, click in the far right column of the incident you want to investigate. The cyber kill chain for the selected incident is displayed.
Click the Activities tab.

The list of response actions already applied to the incident is displayed.

If the response action was initiated as part of an automated workflow, the Initiated by field will show Automated workflow. For more information, see Working with automated workflows.
You can perform a number of actions on the displayed list:
Click on an activity type row to display more information about the selected activity. The information is displayed in a sidebar, as shown in Step 3, and includes details on who initiated the action, its status, file path, and any comments added by the initiator.
Use the Search box to search for a specific action.
Click Filter to apply filters to the list.
Select the Group by impacted entity check box to group relevant actions according to entity.
Click  to show / hide the list of completed actions.

Ensure is displayed next to the actions you want to display. If you want to hide an action from the displayed list, click again to change it to .

To view response actions applied to a specific node

In the cyber kill chain, click on a node to view the sidebar for that node.
Click the Activities tab.

To get a complete understanding of what actions were applied and why, you may need to scroll through the applied response actions for the node. For example, for remote desktop connection actions, you can view who started the action and when, the duration of the action, and its overall status (if it succeeded, failed, or succeeded with errors).

If the response action was initiated as part of an automated workflow, the Initiated by field will show Automated workflow. For more information, see Working with automated workflows.
Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.