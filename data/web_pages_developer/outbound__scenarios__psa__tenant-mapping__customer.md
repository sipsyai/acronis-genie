---
title: "Customer mapping"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/tenant-mapping/customer.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:31:22.484539"
---

# Customer mapping

Customer mapping
The MSP wants to map Acronis customers to PSA customers/clients, and see information about them.

Preconditions

The MSP has enabled the CyberApp.



Basic flow

The MSP should be able to map existing PSA customers to existing Acronis customer tenants.
The MSP should be able to choose an existing PSA customer and create a new Acronis customer tenant to map it to.
The MSP should be able to remove mapping between PSA customers and Acronis customer tenants.

After confirmation, un-mapping is done. The link between customers in the two systems is removed. Customers are no longer synced.
There needs to be an indication that these customers are no longer mapped.



Once mapping is done, The MSP needs to see information within the CyberApp.
For example:



PSA customer
Mapping status
Acronis customer tenant



It should be possible to filter and sort.
The MSP should be able to perform:

Workload registration under correct customer tenant
Monitoring of workload statuses
Ticketing
Usage reporting and quota management





API endpoints
Map to existing customers


Fetch tenants batch.
Suggested with parameter/s:



GET /api/2/tenants?parent_id=
GET /api/2/tenants?subtree_root_id=




Scenario for fetching workload statuses


Fetch a list of all resources.
Suggested with parameter/s:



GET /api/resource_management/v4/resources?type=resource.machine&include_attributes=true