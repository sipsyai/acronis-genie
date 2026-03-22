---
title: "Creating new customers"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/mapping/creating.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:32:48.500135"
---

# Creating new customers

Creating new customers
MSP wants to map an existing RMM customer to a new Acronis customer tenant.

Preconditions

MSP has enabled the CyberApp.



Basic flow

For each RMM customer that the MSP wants to map, the MSP can create a new Acronis customer tenant.
The mapping will be applied after the MSP specifies the following settings:

New customer tenants mode dropdown, with 2 values:

Trial
Production (default)


Create accounts based on dropdown, with 2 values:

Company’s primary contact (default)
Company name


Two-factor authentication checkbox (default off)


MSP changes the options, if necessary, and saves the changes.



Post conditions
When mapping is complete, the MSP should be able to perform:


Workload registration under the corresponding customer tenant.
Monitoring workload statuses.
Ticketing.




API endpoints
The associated Acronis tenant and user accounts are created by the CyberApp using Acronis public API as follows:

The customer tenant will be created with the POST /tenants.
Depending on New customer tenants mode selection, the pricing mode of the tenant will be set using the PUT /tenants/{tenant_id}/pricing.
Depending on Two-factor authentication, the two-factor authentication setting will be set using the PUT /tenants/{tenant_id}/mfa/status.

The account is created based on the Company’s primary contact.
The login user info for the new customer tenant will be set to match the first user of the mapped customer in the RMM system:


User login is set to the RMM user’s first name.
User email is set to RMM user’s email.
First name is set to RMM user’s first name.
Last name is set to RMM user’s last name.


After the tenant is created, the account is created with the POST /users.

The CyberApp can activate the created account by setting the user’s password or by sending an activation email to the user’s email.