---
title: "Provisioning/configuring offering items"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/product-mapping/offer-item.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:30:57.227069"
---

# Provisioning/configuring offering items

Provisioning/configuring offering items

Preconditions
The MSP has:

Enabled the CyberApp.
Mapped Acronis offering items to vendor’s PSA SKUs.
At least 1 mapped customer with an agreement/contract containing 1 mapped Acronis offering item.
Defined a SKUs in PSA.
Defined prices for SKUs in PSA.



Basic flow

The CyberApp should perform automatic sync over a specific interval of time (recommended: 15 minutes).



Note
It should be possible to trigger the sync manually.




During the sync, the CyberApp will provision the offering items in Acronis using the PUT /tenants/{tenant_id}/offering_items endpoint.
If the PSA product is sold:



On a PAYG basis
Enable the mapped offering item and set the quota to unlimited.



On a PREPAID basis
Enable the mapped offering item and set the quota to match the quantity of the PSA product.
The quota should be set as hard, so no overage is done.




Disable all other offering items for that customer, except if that offering item is mapped as “free” provisioning.
Any errors triggered during enabling/disabling offering items should be displayed to the MSP.
For example, disabling offering items with usage is not possible and will cause an error.


Note
Sync errors encountered during the synchronization of 1 customer should not stop the synchronization of other customers.



API endpoints
Enable/disable offering items, and quota limits for a customer

Set tenant offering items.

Alternatively switch edition for a customer

Switch tenant edition.