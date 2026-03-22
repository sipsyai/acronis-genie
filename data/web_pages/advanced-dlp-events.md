# Data Loss Prevention events

Data Loss Prevention > Data Loss Prevention events
Data Loss Prevention events

Data Loss prevention generates events in the DLP events view as follows.

During observation mode, events are generated for all justified data transfers.
During enforcement mode, events are generated based on the Write in log action configured for each policy rule that is triggered.

To view the events for a rule in the data flow policy

Log in to the Cyber Protect console as an administrator.
Navigate to Protection > Data flow policy.
Locate the rule for which you want to view the events and click the ellipsis at the end of the rule line.
Select View events.

To view details about an event in the DLP events view

Log in to the Cyber Protect console as an administrator.
Navigate to Protection > DLP events.
Click an event in the list to view more details about it.
The Event details pane expands to the right.
Scroll down and up in the Event details pane to view the available information.
The details that are displayed in the pane depend on the type of rule and rule settings that triggered the event.

To filter events in the DLP events list

Log in to the Cyber Protect console as an administrator.
Navigate to Protection > DLP events.
In the upper left, click Filter.
Select sensitivity category, workload, action type, user, and channel from the drop-down menus.

You can select more than one item in the drop-down menus. Filtering applies the logical operator OR between items in the same menu, but the logical operator AND is used between items from different menus.

For example, if you select PHI and PII sensitivity category, the result will return all events that contain PHI or PII, or both. If you select sensitivity category PHI and action Write access, only events that match both categories will appear in the filtered result.

Click Apply.
To view all events again, click Filter, then Reset to default, and finally click Apply.

To search for events in the DLP events list

Repeat steps 1-2 from the procedure above.
From the drop-down list to the right of Filter, select a category in which you want to search: Sender, Destination, Process, Message subject, or Reason.
In the text box, enter the phrase you are interested in and confirm by pressing Enter on the keyboard.

Only events matching the phrase you entered appear in the list.

To reset the list of events, click the X sign in the search text box and press Enter.

To view the list of events related to specific rules in the data flow policy

Log in to the Cyber Protect console as an administrator.
Navigate to Protection > Data flow policy.
Select the check box in front of the name of the policy rule you are interested in.

You can select multiple policy rules if needed.

Click View events.

The view switches to Protection > DLP events and the events that are related to the policy rules that you selected appear in the list.

Back to Top



Last build date: Tuesday, March 10, 2026

User Guide for Cyber Protect Cloud Console26.02.