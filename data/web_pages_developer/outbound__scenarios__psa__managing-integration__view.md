---
title: "Viewing statistics"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/managing-integration/view.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:30:44.465870"
---

# Viewing statistics

Viewing statistics
The MSP wants to be able to view CyberApp parameters.

Preconditions

The MSP has enabled the CyberApp.



Basic flow
The vendor’s PSA interface must display the information about the CyberApp.
For example:

CyberApp configuration status.
Total number of customers.
The number of mapped customers.
The number of generated tickets.



API endpoints
Data is pulled through API
If partner has a structure of partners/folders/customers.


Fetch tenants batch.
Suggested with parameter/s:



GET /api/2/tenants?parent_id=
GET /api/2/tenants?subtree_root_id=




If partner has only customers

Fetch tenant children.


Note
Counters are configured via development.