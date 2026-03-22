---
title: "Creating or updating a user"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/tenant-mapping/creating-user.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:32.911593"
---

# Creating or updating a user

Creating or updating a user
The MSP wants to be able to create a new user or update an existing user under an existing customer tenant in Acronis.

Preconditions

Customer tenant must exist.



Input fields


Field
Value
Mandatory



Customer Tenant name
Text string, or select from a pulldown.


Login
Text string


First name
Text string


Last name
Text string


Email
Text string.


Company administrator

One of:
Enabled
Disabled (default)










Post conditions

User is created under the Customer Tenant indicated.
Activation email is sent to email address provided.