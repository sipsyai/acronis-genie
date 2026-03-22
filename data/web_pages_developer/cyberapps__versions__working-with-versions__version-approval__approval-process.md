---
title: "Version approval process"
source: "https://developer.acronis.com/doc/cyberapps/versions/working-with-versions/version-approval/approval-process.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:10:32.619933"
---

# Version approval process

Version approval process
CyberApp Versions must be approved by Acronis before you can deploy them.

Note
As part for the Version approval process, Acronis also verifies the callback handler. For more information, see Callback handler verification.


The Version approval process
The approval process flow is illustrated here:


Important

When either you or Acronis change a Version’s approval process state, Vendor Portal requests a comment.
This comment should include the reason for and/or details of the state change.
This information is displayed in the Version list actions and details panel in the Reason for state update field.



Note

To open the actions and details panel, click a CyberApp Version list entry.



When you send a Version for approval, the Version becomes read-only and the state changes to In review.
There are two possible outcomes of an Acronis approval review:



Approval
Acronis changes the Version state to Approved.
The Version can now be used in a deployment.
Neither you nor Acronis can change the Version any more.
You can duplicate the Version or open and view the content.



Acronis requests improvements
Acronis changes the Version state to Awaiting improvement and specifies the recommended improvements in the Reason for state update field of the actions and details panel.
The Version remains read-only until you change the state back to Draft by selecting the Edit action.
When you have made the improvements, you should resend the Version for approval.