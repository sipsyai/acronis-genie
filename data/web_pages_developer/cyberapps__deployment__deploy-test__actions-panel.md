---
title: "Opening the details panel"
source: "https://developer.acronis.com/doc/cyberapps/deployment/deploy-test/actions-panel.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:55:40.478319"
---

# Opening the details panel

Opening the details panel

To open the details panel for a test environment deployment

Open the deployment list.
Click the test deployment list entry.




Details displayed
The details panel has two tabs:

OVERVIEW
TARGETS


OVERVIEW
This tab displays the following deployment details:


Description
The deployment request description.



Created
The date and time that you created the deployment request.



Deployed on
The deployment type (Test environment).



State
The deployment state.



Note
For more information, see Deployment request states.




Reason for state update
For production deployment requests, this is a (non-obligatory) comment entered by the person who made the latest state change to the production deployment request.
For test environment deployments, there is no approval process, so there are no manual state updates. Therefore, this field is always blank for test environment deployments.





TARGETS
This tab displays a list of details for each individual test deployment partner tenant:


A deployment state icon indicates the state of the deployment for each tenant:



: Not started
: In progress
: Deployed
: Failed




Tenants
The partner tenant.



CyberApp Version
The Version deployed to the Tenant.



CyberApp Description
The Description deployed to the Tenant.



Publishing tag
Any publishing tag assigned to the deployment:




None
New
Coming soon
Lighthouse



Note
For more information, see Catalog card.




Deployment status
The deployment status:



Visible
Hidden