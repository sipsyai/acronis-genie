---
title: "Managing branding options"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/branding/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:14:48.676575"
---

# Managing branding options

Managing branding options

Operations with branding options are located under the /tenants/{tenant_id}/brand endpoint of the API.


Important
Branding options cannot be managed for Customer and Unit tenants.


Available branding option operations






Operation
Methods and endpoints used



Enable branding for a tenant
POST /tenants/{tenant_id}/brand

Disable branding for a tenant
DELETE /tenants/{tenant_id}/brand

Fetch branding options for a tenant
GET /tenants/{tenant_id}/brand

Update branding options for a tenant
PUT /tenants/{tenant_id}/brand

Configure the “Buy URL” option for upselling
PUT /tenants/{tenant_id}/brand

Update brand logo
POST /tenants/{tenant_id}/brand/logo




In this section

Enabling branding for a tenant
Disabling branding for a tenant
Fetching the branding options of a tenant
Updating branding options for a tenant
Configuring the “Buy URL” option
Updating the brand logo