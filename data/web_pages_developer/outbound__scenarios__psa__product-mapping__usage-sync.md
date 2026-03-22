---
title: "Synchronizing usage"
source: "https://developer.acronis.com/doc/outbound/scenarios/psa/product-mapping/usage-sync.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:31:01.434973"
---

# Synchronizing usage

Synchronizing usage
The MSP wants to see Acronis usage in PSA.

Preconditions

MSP has enabled the CyberApp.
MSP has mapped at least 1 Acronis offering item to the vendor’s PSA system SKU of the product that is sold on a PAYG basis.



Basic flow

The CyberApp should perform automatic usage sync over a specific interval of time (recommended: 24 hours)
using the GET /tenants/{tenant_id}/usages endpoint.



Note
It should be also possible to trigger the usage sync manually.



During the sync, if PSA product is sold:


On a PAYG basis
Update PSA product quantity with the usage of the mapped offering item.



On a PREPAID basis
Skip the update.







Post conditions

Contracts/agreements are updated in vendor’s PSA system.



API endpoints
Quota sync (servers, workstations, storage, etc.) usage for PAYG mode

Fetch tenant usages.


Note
Get the usage value from absolute_value field.

Quota sync for prepaid mode

Fetch tenant usages.


Note

Skip, update is not needed.
Get the usage value from absolute_value field and compare with value (and/or overage in quota object, if overuse notification is required).


Acronis billing scenario
Billing automation with usage report.