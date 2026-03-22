---
title: "Finding a user"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/tenant-mapping/finding-user.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:41.312422"
---

# Finding a user

Finding a user
The MSP wants to be able to ask if a specific user exists, and get basic user details if it does.

Preconditions

One or more users exist under a given Customer Tenant.
Users can be validated or not-validated.
Users can have any set of permissions.



Input fields


Field
Value
Mandatory



Login
Text string






Post conditions


If the user exists, the integration should return:
First name, Last name
Email address
Validation status
Roles




If the user does not exist, the integration should return a message like User was not found.