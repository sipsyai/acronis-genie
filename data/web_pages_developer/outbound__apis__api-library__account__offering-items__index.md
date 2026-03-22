---
title: "Managing offering items and quotas"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/offering-items/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:16:17.102662"
---

# Managing offering items and quotas

Managing offering items and quotas

Operations with offering items and quotas are located under the /tenants/{tenant_id}/offering_items endpoint of the API.
The API represents offering items and quotas as a JSON objects. To find out more about the object structures, see JSON object structure.


Available offering item and quota operations






Operation
Methods and endpoints used



Fetch available offering items for a tenant
GET /tenants/{tenant_id}/offering_items

Switch edition for a tenant
PUT /tenants/{tenant_id}/edition

Change offering item quotas for a tenant
PUT /tenants/{tenant_id}/offering_items

Enable or disable an offering item
PUT /tenants/{tenant_id}/offering_items




In this section

JSON object structure
Fetching available offering items
Switching the edition of a service
Changing quotas
Enabling/disabling an offering item