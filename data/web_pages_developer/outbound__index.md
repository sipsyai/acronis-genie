---
title: "Outbound integrations"
source: "https://developer.acronis.com/doc/outbound/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:28:29.679250"
---

# Outbound integrations

Outbound integrations

Through the public API endpoints, Acronis users can monitor and manage mission-critical Acronis Cyber Platform features from a third-party platform.
Examples include:



Configuring which features of Acronis Cyber Platform are available to MSPs and their customers.
Setting up usage quotas and collecting actual usage data.
Listing available workloads and Protection Plans, and assigning Protection Plans to workloads.
Receiving and processing alerts raised by Acronis Cyber Platform.



Development and deployment process


Analyze requirements
Determine:


The purpose of the integration.
Features that the integration will provide.
The Acronis platform data that the integration needs.
The Acronis API endpoints that the integration will use.


Note
For a list of typical outbound integration types, including scenario API details, see outbound integration scenarios.



Create a proxy CyberApp.
This is necessary to list the integration on the Acronis integration catalogs.
MSPs can then find and enable the integration directly within the Acronis Cyber Platform.



Note
For more information on CyberApps, see Inbound integrations (CyberApps).



Register as a partner.
Access Vendor Portal.
Create the CyberApp.

Important

When you create a CyberApp, it is assigned a unique code. Note this down, as you need it to implement API identification during development of the functionality, and to activate or deactivate the integration for MSPs who enable it in the integration catalog.
You can retrieve the CyberApp code later, if you cannot find it.




Create a CyberApp Description and provide marketing materials
This determines how your integration will be presented in our integrations catalog and inside the Acronis Cyber Protect Platform.
For more information, see Marketing a CyberApp.


Note
You can do this step at any point prior to production deployment.





Develop the integration functionality
As part of the integration, you must implement the following:




Add an API identification to every API query sent to Acronis by adding a header with a key of X-Application-Secret, with the value set to CyberApp code from step 2c, above.
This helps Acronis monitor API load and resolve any API issues that might occur.



As part of the integration configuration scenario, immediately after you have validated the Acronis API keys that the MSP will provide, you should make a single query to activate the integration for this tenant.
In this query, use the CyberApp code from step 2c, above, as application_code.
This will allow us to show in the Acronis Cyber Protect Platform that your integration is active for this tenant.



If your integration includes a scenario where it can be disabled or switched off, we recommend that you also implement a single deactivation query.
In this query, use the CyberApp code from step 2c, above, as application_code.
This will allow us to show the correct activation status for your integration in the Acronis Cyber Protect Platform, should the MSP turn the integration off at some point.






Verify and deploy the integration.
For more information, see Verifying an outbound integration and Deploying the CyberApp.




In this section

Outbound integration scenarios
Acronis platform APIs
Scripts
Outbound integration verification
Deploying the CyberApp
Activating an outbound integration
Deactivating an outbound integration