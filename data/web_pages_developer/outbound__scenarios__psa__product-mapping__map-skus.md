---
title: "Mapping Acronis offering items to PSA SKUs"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/product-mapping/map-skus.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:30:52.868472"
---

# Mapping Acronis offering items to PSA SKUs

Mapping Acronis offering items to PSA SKUs
The MSP wants to be able to map PSA SKUs to an Acronis offering item.

Preconditions

The MSP has enabled the CyberApp.
The MSP has defined a list of SKUs in the vendor’s PSA system.
The MSP has defined prices for SKUs in the vendor’s PSA system.



Basic flow

The MSP selects an edition “Per GB” or “Per Workload”.
The MSP needs to be able to map Acronis offering items to SKUs in the vendor’s PSA system.



Notes

It should not be possible to map 2 Acronis offering items to 1 PSA SKU.
It should not be possible to map 2 PSA SKUs to 1 Acronis offering item.
It should be possible to mark 1 or more offering items as free provisioning (not controlled by CyberApp synchronization).
Only those billing modes/editions/offering items that are available to the partner should be available for mapping.
There can be more than 1 storage under 1 location. This means you need to provide mapping for each one of them.
It should be possible to establish extra mappings for each storage that covers:

Class1 backup storage usage (free).
Class2 backup storage usage (billable).


If geo-redundancy is available, then you need to provide extra mapping for each of the following offering items (Reason: Billing is different (higher) for these types of storage)

Backup storage.
Class2 usage.
M365-protected seats.
Google Workspace-protected seats.





Post conditions
Acronis offering item is mapped to the vendor’s PSA system SKU.


API endpoints
Fetch offering items per partner (parent of mapped customer)


Fetch offering items available for tenant child.
Suggested with parameter/s: edition=*


GET /api/2/tenants/<tenant_id>/offering_items/available_for_child?edition=*