---
title: "Mapping customers"
source: "https://developer.acronis.com/doc/outbound/scenarios/ticketing/mapping/customers.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:34:33.680384"
---

# Mapping customers

Mapping customers
The MSP wants to map Acronis customers to ticketing customers/clients, and see information about them.

Preconditions

MSP has enabled the CyberApp.



Basic flow

The vendor’s ticketing interface must fetch the data about the MSP’s Acronis tenants using public API
and provide a way to manage the mapping between MSP’s ticketing customers and Acronis customers.
The mapping interface must:

Indicate which MSP’s ticketing customers are mapped.

Allow MSP to create a mapping of their existing ticketing customers and Acronis customers.
This will create a link between both systems and start their data synchronization.



Allow MSP to remove the mapping between their ticketing customers and Acronis customers.
This will break the link between both systems and stop their data synchronization.





Once the customer mapping is done, MSP must be able to see the information about the mapping.
For example:


Customer name in ticketing system.
Acronis customer tenant name.
Mapping status.


It should be possible to filter and sort the values.
MSP should be able to perform:

Workload registration in the corresponding customer tenant.
Monitoring workload statuses.
Ticketing.
Usage reporting and quota management.





API endpoints
Map to existing customers


Fetch tenants batch.
Suggested with parameter/s:
*   GET /api/2/tenants?parent_id=
*   GET /api/2/tenants?subtree_root_id=



Scenario for fetching workload statuses


Fetch a list of all resources.
Suggested with parameter/s:
*   GET /api/resource_management/v4/resources?type=resource.machine&include_attributes=true