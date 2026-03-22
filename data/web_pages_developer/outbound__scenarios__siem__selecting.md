---
title: "Selecting customers"
source: "https://developer.acronis.com/doc/outbound/scenarios/siem/selecting.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:34:04.205211"
---

# Selecting customers

Selecting customers
The MSP wants to have the option to select customers to display Acronis data for in the SIEM.

Preconditions
The MSP must be able to see all partner and customer tenants.
Acronis data should consist of:

Acronis data center.
Acronis partner tenant.
Acronis customer.



Basic flow
The MSP chooses which Acronis tenants for which to display data within the SIEM.


Post conditions
The MSP sees data only for the selected partner and customer tenants.


API endpoints


Fetch Tenants Batch.
Suggested with parameter/s:



GET /api/2/tenants?parent_id=
GET /api/2/tenants?subtree_root_id=