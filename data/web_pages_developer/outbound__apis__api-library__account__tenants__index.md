---
title: "Managing tenants"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/tenants/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:17:51.499398"
---

# Managing tenants

Managing tenants

Operations with tenants are located under the /tenants endpoint of the API.
The API represents tenants and tenant contacts as JSON objects. To find out more about the object structures, see JSON object structures.


Available tenant operations






Operation
Methods and endpoints used



Create a tenant
POST /tenants

Fetch information about an individual tenant
GET /tenants/{tenant_id}

Fetch information about tenants
GET /tenants

Fetch information about child tenants
GET /tenants/{tenant_id}/children

Fetch the production start date of a tenant
GET /tenants/{tenant_id}/pricing

Switch a customer tenant to production mode

GET /tenants/{tenant_id}/pricing
PUT /tenants/{tenant_id}/pricing



Modify tenant properties

GET /tenants/{tenant_id}
PUT /tenants/{tenant_id}



Move a tenant to another tenant

GET /tenants/{tenant_id}
PUT /tenants/{tenant_id}



Limit access to a tenant for higher-level administrators

GET /tenants/{tenant_id}
PUT /tenants/{tenant_id}



Disable a tenant

GET /tenants/{tenant_id}
PUT /tenants/{tenant_id}



Delete a tenant

GET /tenants/{tenant_id}
PUT /tenants/{tenant_id}
DELETE /tenants/{tenant_id}






In this section

JSON object structures
Creating a tenant
Fetching information about an individual tenant
Fetching information about tenants
Fetching information about child tenants
Fetching the production start date of a tenant
Switching a customer tenant to production mode
Modifying tenant properties
Moving a tenant to another tenant
Limiting higher-level administrator access to a tenant
Disabling a tenant
Deleting a tenant