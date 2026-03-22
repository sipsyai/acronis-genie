---
title: "Mapping multiple partners"
source: "https://developer.acronis.com/doc/outbound/scenarios/ticketing/mapping/multiple-partners.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:34:42.154619"
---

# Mapping multiple partners

Mapping multiple partners
In case MSP has multiple Acronis data centers and Acronis partner tenants, the MSP wants to provide information about those tenants within the ticketing system.

Preconditions

MSP has enabled the CyberApp.



Basic flow


MSP must provide valid API client credentials for each Acronis partner tenant.
The CyberApp must use these credentials to authenticate in the Acronis Cyber Protect Cloud by requesting an access token.


The vendor’s ticketing interface must fetch the data about the MSP’s Acronis tenants using public API
and provide a way to manage the mapping of MSP’s ticketing customers that are in different Acronis partner tenants.
The mapping should consist of:

Acronis data center.
Acronis partner tenant.
Acronis customers.





API endpoints


Fetch Tenants Batch.


Suggested with parameter/s:



GET /api/2/tenants?parent_id=
GET /api/2/tenants?subtree_root_id=