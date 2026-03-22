---
title: "Customer mapping"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/mapping/customer-mapping.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:32:52.716252"
---

# Customer mapping

Customer mapping
To be able to match the data between both systems, the MSP must specify which RMM customer corresponds to which Acronis customer tenant.

Preconditions

MSP has enabled the CyberApp.



Basic flow

The vendor’s RMM interface must fetch the data about the MSP’s Acronis tenants using public API
and provide a way to manage the mapping between MSP’s RMM customers and Acronis customers.
The mapping interface must:

Indicate which of the MSP’s RMM customers are mapped.
Allow the MSP to create a mapping of their existing RMM customers and Acronis customers. This will create a link between both systems and start their data synchronization.
Allow the MSP to remove the mapping between their RMM customers and Acronis customers. This will break the link between both systems and stop their data synchronization.





Post conditions
The MSP must be able to see information about the mapping, such as:


Customer name in RMM system.
Acronis customer tenant name.
Mapping status.



Note
It should be possible to filter and sort the values.

The MSP should be able to perform:


Workload registration in the corresponding customer tenant.
Monitoring workload statuses.
Ticketing.
Usage reporting and quota management.




API endpoints


Fetch Tenants Batch
Suggested with parameter(s):



GET /api/2/tenants?parent_id=
GET /api/2/tenants?subtree_root_id=






Notes
When you map customer tenants, you also need to map the device under them.
This can be done by looking at the MAC address and OS version for each customer by fetching a list of all resources.