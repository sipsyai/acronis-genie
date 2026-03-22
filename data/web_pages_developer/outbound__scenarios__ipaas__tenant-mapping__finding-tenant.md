---
title: "Finding a customer tenant"
source: "https://developer.acronis.com/doc/outbound/scenarios/ipaas/tenant-mapping/finding-tenant.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:29:37.109985"
---

# Finding a customer tenant

Finding a customer tenant
The MSP wants to be able to ask if a specific customer tenant exists, and get basic details about the customer tenant if it does.

Preconditions

One or more customer tenants exist.


Note
Tenants can be in trial or production mode.



Input fields


Field
Value
Mandatory



Customer Tenant name
Text string, or select from a pulldown.






Post conditions


If the tenant exists, the integration should return:
tenant_id
Tenant mode (trial or production)
Tenant creation date
Tenant production start date (if the mode is production)




If the tenant does not exist, the integration should return a message like Customer tenant not found.