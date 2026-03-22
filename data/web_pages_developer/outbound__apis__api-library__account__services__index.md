---
title: "Managing services"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/services/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:13.509164"
---

# Managing services

Managing services

Operations with services (also called ‘applications’) are located under the /applications endpoint of the API.
The API represents services as a JSON objects. To find out more about the service object structure, see JSON object structure.


Important
Before you start, consult the this Acronis Knowledge Base article to check service availability on the target data center.


Available service operations






Operation
Methods and endpoints used



Fetch information about all platform services
GET /applications

Fetch information about services enabled for a tenant

GET /tenants/{tenant_id}/applications
GET /applications [Optional]



Fetch information about an individual service

GET /tenants/{tenant_id}/applications
GET /applications/{application_id}



Enable a service for a sub-tenant

GET /tenants/{tenant_id}
GET /tenants/{tenant_id}/applications
GET /applications
POST /applications/{application_id}/bindings/tenants/{tenant_id}



Disable a service for a sub-tenant

GET /tenants/{tenant_id}/applications
GET /applications
DELETE /applications/{application_id}/bindings/tenants/{tenant_id}






In this section

JSON object structure
Fetching information about all platform services
Fetching information about services enabled for a tenant
Fetching information about an individual service
Enabling a service for a sub-tenant
Disabling a service for a sub-tenant