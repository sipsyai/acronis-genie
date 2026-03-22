---
title: "Multiple partner mapping"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/tenant-mapping/multiple.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:31:30.908610"
---

# Multiple partner mapping

Multiple partner mapping
The MSP - with several Acronis data centers and multiple Acronis accounts - wants to access all customers in one place within PSA.

Preconditions

The MSP has enabled the CyberApp.



Basic flow

The MSP must provide valid API client credentials for each Acronis partner tenant. The CyberApp must use these credentials
to authenticate in the Acronis Cyber Protect Cloud by requesting an access token.
The vendor’s PSA interface must fetch the data about the MSP’s Acronis tenants using public API
and provide a way to manage the mapping of MSP’s PSA customers that are in different Acronis partner tenants.
The mapping should consist of:

Acronis data center.
Acronis partner tenant.
Acronis customers.





API endpoints


Fetch tenants batch.
Suggested with parameter/s:



GET /api/2/tenants?parent_id=
GET /api/2/tenants?subtree_root_id=