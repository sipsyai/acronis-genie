---
title: "Managing billing settings"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/billing/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:14:19.189147"
---

# Managing billing settings

Managing billing settings
Operations with billing settings are located under the /tenants/{tenant_id}/{setting_name} endpoint of the API.

Warning

Billing settings can only be set for partner tenants.
Billing settings are not inherited by child tenants, and are set individually for each tenant.



Available branding option operations






Operation
Methods and endpoints used



Set the tier level and the licensing mode for a partner tenant
PUT /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name}

Switch the tier level of a partner tenant
PUT /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name}

Fetch the pricing information for a tenant
GET /applications/{application_id}/settings/tenants/{tenant_id}/{setting_name}




In this section

Billing settings
Setting the partner tenant tier level and the licensing mode
Switching a partner tenant tier level
Fetching the pricing information for a tenant