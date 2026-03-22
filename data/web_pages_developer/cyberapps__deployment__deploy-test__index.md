---
title: "Test environment deployments"
source: "https://developer.acronis.com/doc/cyberapps/deployment/deploy-test/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:55:53.524978"
---

# Test environment deployments

Test environment deployments

There is no approval process for test environment deployment: they are automatically deployed.
Test environment deployments are only visible to the specified test partner tenants.

You cannot delete test environment deployments. Older deployments for any given test deployment partner tenant are superseded by the latest one.

Test environment deployment for development testing

Test environment deployment is generally used to quickly test new CyberApp Version functionality and CyberApp Description content.
For this reason, test environment deployments allow unapproved Versions and Descriptions.


Note
To deploy to the test environment, the Description must be valid. For more information, see Managing Description content.


When you deploy an unapproved Version or Description to the test environment, the state changes to , and can no longer be edited.
Therefore, you must duplicate the Version or Description to continue developing its functionality (Version) or modifying its content (Description).

If you are satisfied with an unapproved, test-deployed Version or Description and want to request production deployment for it, you must send it for approval, as Versions and Descriptions with the  state do not appear as options when creating a production deployment request.


Test environment deployment for pre-production QA testing

Acronis recommends that you deploy any combination of  Version and  Description to your test environment prior to requesting production deployment for the combination.
In this way, you can do a final, pre-production check to ensure that:


The CyberApp functions as you expect it to.
The CyberApp catalog entry looks the way you expect it to.


Note
Approved Versions and Descriptions, when deployed to test, do not change to the  state: they remain in the  state. You can, therefore, deploy them to production with no other action required.


In this section

Deploying to test
Opening the details panel
Opening the details pop-up