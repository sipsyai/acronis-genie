---
title: "Multiple partner mapping"
source: "https://developer.acronis.com/doc/outbound/scenarios/rmm/mapping/multi-mapping.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:33:01.115094"
---

# Multiple partner mapping

Multiple partner mapping
If the MSP has multiple partner tenants in Acronis, the MSP may need to provide information about those tenants in the PSA system.

Preconditions

The MSP has enabled the CyberApp.



Basic flow


The MSP must provide valid API client credentials for each Acronis partner tenant.
The integration must use these credentials to authenticate in the Acronis Cyber Protect Cloud by requesting an access token.


The vendor’s PSA interface must fetch the data about the MSP’s Acronis tenants using public API
and provide a way to manage the mapping of the MSP’s PSA customers that are in different Acronis partner tenants.
The mapping should consist of:

Acronis data center.
Acronis partner tenant.
Acronis customers.





API endpoints

Fetch data about Acronis tenants
Request an access token