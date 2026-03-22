---
title: "CyberApp lifecycle"
source: "https://developer.acronis.com/doc/cyberapps/intro/lifecycle.html"
source_domain: "developer"
scraped_at: "2026-03-22T01:57:51.077298"
---

# CyberApp lifecycle

CyberApp lifecycle
Typical CyberApp development and deployment cycles through the following steps:


Requirements analysis
Determine:


What the purpose of the CyberApp is.
What features the CyberApp will provide.
If the cloud service needs Acronis platform data.
What customer data the CyberApp will process.



Prepare the callback handler and connector
Callback handlers allow cloud platforms to send tenant mapping and request service-specific data.
For more information, see The callback handler.

The connector enables data synchronization between the cloud service and the Acronis platform.
For more information, see The connector.



Develop the CyberApp functionality
The CyberApp Version defines the CyberApp functionality and UI.
For more information, see CyberApp Version.



Add CyberApp marketing materials
Vendors must provide a minimum amount of information about their CyberApp to include in the Acronis catalogs.
Vendors can provide marketing materials to help customers know if the CyberApp fits their needs and to attract Acronis partners to try the CyberApp.
The CyberApp Description stores all the marketing information about a CyberApp.
For more information, see CyberApp Description.



Test
The CyberApp developer deploys a CyberApp Version and Description to their test environment.



Note
Deployment to the test environment does not require Acronis approval.




Approval
Before a Vendor can deploy their CyberApp to a production environment, Acronis must approve both the CyberApp Version and the CyberApp Description.
Approval ensures that the CyberApp complies with Acronis guidelines and CyberApp Standard.
For more information, see CyberApp Version approval and CyberApp Description approval.



Deployment
The ISV requests production deployment of their approved CyberApp Version and CyberApp Description to one or more Acronis production data centers.
Acronis publishes the CyberApp Description details in the Acronis Catalogs.
For more information, see Deploying CyberApps.



Enablement
Acronis partners must enable a CyberApp before they or their customers can use it.
Before an Acronis Partner enables a CyberApp, the ISV cloud service and the Acronis Cyber Platform cannot exchange any Partner or Partner customer data, and any CyberApp UI in the Acronis Cyber Platform is unavailable.

To fully enable a CyberApp, a Partner must:



Open the integration catalog on their data center.
Select and enable the CyberApp.
[Optional] Configure the CyberApp by providing, for example, credentials for the cloud service.



The Acronis Partner might also need to enable the CyberApp for individual customers.
This is done in the following way:



If the cloud service has a single account for all end customers then, on the customer management tab, the Acronis Partner selects the end customer tenants that will use the CyberApp.
If the cloud service has separate accounts for each end customer, the Acronis Partner must map cloud service accounts to end customer tenants. The CyberApp is unavailable for end customer tenants who are not mapped to corresponding cloud service accounts.



When an Acronis Partner enables a CyberApp, they might need to accept legal agreements for themselves and on behalf of their customers (data processing agreement, end-user licensing agreement, terms and conditions, etc.).
The CyberApp is unavailable to end customers that have not accepted agreements and consent for data processing.
An Acronis Partner and their end customers can use a CyberApp when the Acronis Partner enables and configures the CyberApp, and accepts any required legal agreements.
If the CyberApp has any UI, Acronis Cyber Protection Console presents it, and any data exchange with the ISV cloud service is allowed.



Upgrade
The ISV updates or upgrades their CyberApp if the cloud service changes, or the ISV adds a new extension point, or the CyberApp Description changes, the ISV can duplicate the deployed CyberApp Version and/or Description and update them independently.