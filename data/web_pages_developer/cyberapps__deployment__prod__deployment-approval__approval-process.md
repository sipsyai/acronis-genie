---
title: "Production deployment request approval process"
source: "https://developer.acronis.com/doc/cyberapps/deployment/prod/deployment-approval/approval-process.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:56:33.093861"
---

# Production deployment request approval process

Production deployment request approval process
CyberApp production deployment requests must be approved by Acronis before the CyberApp deployment is enabled.

The production deployment request approval process
The approval process flow is illustrated here:


Important

When either you or Acronis change a production deployment request’s approval process state, Vendor Portal requests a comment.
This comment should include the reason for and/or details of the state change.
This information is displayed in the production deployment request list actions and details panel in the Reason for state update field.



Note

To open the actions and details panel, click a CyberApp production deployment request in the deployments list entry.



When you send a production deployment request for approval, the production deployment request becomes read-only and the state changes to In review.
There are three possible outcomes of an Acronis approval review:



Approval
Acronis changes the production deployment request state to Deployed.
The CyberApp deploys, as specified in the request.
Neither you nor Acronis can change the production deployment request any more.



Acronis requests improvements
Acronis changes the production deployment request state to Awaiting improvement and specifies the recommended improvements in the Reason for state update field of the actions and details panel.
The production deployment request remains read-only until you change the state back to Draft by selecting the Edit action.
When you have made the improvements, you should resend the production deployment request for approval.



Acronis takes over





Acronis takes over process

If you decide that you would rather Acronis take the lead in preparing the CyberApp production deployment, you can request that Acronis take over the production deployment request in the comment when you send the production deployment request for approval.
Alternatively, your assigned Acronis manager might recognize that you are having trouble preparing the CyberApp production deployment, and take over to save your time and efforts.

When Acronis take over a production deployment request, they clone (duplicate) their own version of your production deployment request and assign an internal CyberApp resource to finish it off.
After that, the Acronis manager can decide whether to request your confirmation for the changes or simply pre-approve and deploy it.

Acronis changes the production deployment request state to Taken for correction and specifies the reasons in the Reason for state update field of the actions and details panel.
Neither you nor Acronis can change the originally submitted production deployment request any more, and the approval process for it is terminated.

Acronis clones the original production deployment request, and the cloned production deployment request is marked as In correction.
You cannot modify the cloned production deployment request.
Acronis modifies the cloned production deployment request on your behalf and requests your confirmation for modifications (although there are some rare occasions when Acronis skips requesting confirmation).
When Acronis requests confirmation of modifications, Acronis changes the cloned production deployment request state to Needs confirmation and specifies the modifications in the Reason for state update field of the actions and details panel.
You can either:




Decline the modifications.
The approval process terminates, and the cloned production deployment request state changes to Declined.
Neither you nor Acronis can change the cloned production deployment request any more.



Agree to the modifications.
The cloned production deployment request state changes to In review.
The production deployment request remains read-only for you, and Acronis either requests further improvements (undertaken by Acronis) or approves and deploys the cloned production deployment request.



Request improvement to the modifications.
The cloned production deployment request state changes to Awaiting improvement, then to In correction when Acronis begins your requested corrections.
The cloned production deployment request remains read-only for you.
When ready, Acronis requests your confirmation again (although there are some occasions when Acronis will skip requesting confirmation).




The cycle of correction, confirmation, and review continues until either you decline the cloned production deployment request, or you agree to the corrections and Acronis approves and deploys the cloned production deployment.