---
title: "Managing locations and storages"
source: "https://developer.acronis.com/doc/outbound/apis/api-library/account/locations/index.html"
source_domain: "developer"
scraped_at: "2026-03-22T02:15:34.990609"
---

# Managing locations and storages

Managing locations and storages

Locations are the groups, registered on the platform, which incorporate infrastructure components.
Storage is represented as an infrastructure component, such as Acronis-hosted cloud storage or partner-hosted storage, which can be registered on the platform, and offered in the form of an offering item.

Location operations are located under the /locations endpoint of the API.
Storage operations are located under the /infras endpoint of the API.
The API represents locations and storages as JSON objects. To find out more about the object structures, see Location object structure and Storage object structure.



Warning
Before proceeding, consider the following when operating with locations and storages:

When disabling a service, the service will become unavailable within the
manipulated tenant and its sub-tenants, and all data related to this service
will be deleted.
When forcing the deletion of a storage, all data related to this storage will be deleted.
All listed operations are irreversible.



Available location operations






Operation
Methods and endpoints used



Create new location for storages
POST /locations

Fetch existing locations of a tenant

GET /locations
GET /tenants/{tenant_id}/locations



Update a location
PUT /locations/{location_id}

Delete a location
DELETE /locations/{location_id}

Register a storage
POST /infra

Fetch existing storages of a tenant

GET /infra
GET /location/{location_id}/infra



Update a storage
PUT /infra/{infra_id}

Move a storage
PUT /infra/{infra_id}

Delete a storage
DELETE /infra/{infra_id}




In this section

Location object structure
Storage object structure
Creating a location
Fetching locations
Updating a location
Deleting a location
Registering a storage
Fetching storages
Updating a storage
Moving a storage
Deleting a storage