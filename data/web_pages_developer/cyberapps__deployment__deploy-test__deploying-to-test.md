---
title: "Deploying to test"
source: "https://developer.acronis.com/doc/cyberapps/deployment/deploy-test/deploying-to-test.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:55:44.813630"
---

# Deploying to test

Deploying to test

You can deploy any Version and any valid Description to the test environment.
Test environment deployments do not require Acronis approval: deployment is automatic.


Note

You cannot delete test environment deployments.
Older deployments for any given test deployment partner tenant are superseded by newer ones.



To deploy to your test environment

Open the CyberApp deployment list.
Click Add and select Deploy to test environment.


[Optional] In the Description field, enter a description of the test deployment.

Note
By default, a test deployment Description is set to “Deployment - <today’s date>”


In the Tenants list, select the test deployment tenants.
For each selected tenant, select:


CyberApp Version
All of your Versions are available for test environment deployment, including Versions which are not Approved.



Note

Select No Version to only publish the CyberApp Description to the integration catalog.
For more information, see Deploying to catalog only.





CyberApp Description
Only valid Descriptions can be deployed.



Note

For more information on valid and invalid Descriptions, see Opening a Description





Publishing tag
This adds a text tag at the upper left corner of the Application Catalog card.
The options are:




None
New
Coming soon
Lighthouse



Note
For more information, see Deployment tags.




Deployment status



Visible
Hidden





Click Next.


Review your test deployment settings.
[Optional] Click Back to return to step 3 and make changes.
Click Deploy.


New test deployment requests appear in the deployment list with an initial state of Ready for deployment.
Within a few moments, the state changes to Deploying. A few moments later, it changes again, to Deployed.
For state changes to show in your deployment list, you must refresh the list.
To do this, select a different tab (for example, CYBERAPP DESCRIPTIONS) and then select the DEPLOYMENT tab again.


Note

In the Description list, the deployed Description state changes to Deployed to test environment.
In the Version list, the deployed Version state will change to Deployed to test environment.