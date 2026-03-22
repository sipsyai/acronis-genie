---
title: "Deploying to domain controllers"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/deploying/deployment-domain.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:32:01.943015"
---

# Deploying to domain controllers

Deploying to domain controllers

Preconditions

MSP has enabled the integration.
MSP has mapped customer tenants.
A registration token has been fetched via Acronis API.
Has administrator credentials for the domain controller.



Basic flow

The MSP selects whether they want to install, update or uninstall the Acronis Cyber Protect Cloud agent.
Select Domain Controller if the target endpoint is a Windows domain controller. Select none in all other cases.
When deploying the Acronis agent to a domain controller, provide local admin credentials (need to have admin credentials on the domain controller).



API endpoints
The flow itself should be the same as the Installing the Acronis agent scenario, but with additional development applied to the installation scripts, using additional parameters and conditions.

Note
There are currently no blog articles describing this scenario.